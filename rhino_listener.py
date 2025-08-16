# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import sys
import socket
import json
import threading
import time

import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

PORT_FILE = os.path.expanduser('~/Library/Application Support/rhino_mcp/port.txt')
PORT_MIN, PORT_MAX = 53700, 53999

# ---- Single-instance guard -----------------------------------------------

def _get_state():
    st = sc.sticky.get('mcp_listener_state')
    if st is None:
        st = {}
        sc.sticky['mcp_listener_state'] = st
    return st

# ---- Utilities ------------------------------------------------------------

def _write_port(p):
    d = os.path.dirname(PORT_FILE)
    try:
        if not os.path.exists(d):
            os.makedirs(d)
        with open(PORT_FILE, 'w') as f:
            f.write(str(p))
    except Exception as e:
        print("[Listener] Failed to write port file: {0}".format(e))

def _choose_port():
    import random
    for _ in range(200):
        p = random.randint(PORT_MIN, PORT_MAX)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('127.0.0.1', p))
            s.listen(50)
            return s, p
        except Exception:
            try:
                s.close()
            except Exception:
                pass
            continue
    raise RuntimeError('No free TCP port available')

def _reply(conn, obj):
    try:
        data = json.dumps(obj) + "\n"
        try:
            conn.sendall(data.encode('utf-8'))
        except Exception:
            conn.sendall(data)
    except Exception:
        pass

def _read_line(conn, timeout_sec, maxlen):
    """Read one '\n'-terminated line with a timeout and max length."""
    conn.settimeout(0.25)
    deadline = time.time() + timeout_sec
    buf = []
    total = 0
    while time.time() < deadline:
        try:
            chunk = conn.recv(4096)
            if not chunk:
                break
            try:
                chunk = chunk.decode('utf-8')
            except Exception:
                chunk = chunk.decode('utf-8', 'ignore')
            buf.append(chunk)
            total += len(chunk)
            if total > maxlen:
                return None, "request too large"
            if chunk.find('\n') != -1:
                s = ''.join(buf)
                line = s.split('\n', 1)[0]
                return line, None
        except socket.timeout:
            continue
        except Exception as e:
            return None, str(e)
    return None, "read timeout"

# ---- Run code on Rhino UI thread -----------------------------------------

def _on_ui(func, *args, **kwargs):
    """Invoke callable on Rhino UI thread synchronously; return (ok, result_or_error)."""
    result_box = []
    error_box = []

    def runner():
        try:
            result_box.append(func(*args, **kwargs))
        except Exception as ex:
            error_box.append(str(ex))

    # Invoke is synchronous; will block until finished
    Rhino.RhinoApp.InvokeOnUiThread(runner)

    if error_box:
        return False, error_box[0]
    return True, (result_box[0] if result_box else None)

# ---- Rhino operations (must run on UI) -----------------------------------

def _safe_open_doc(path):
    """Open or create target .3dm without prompts."""
    if not path:
        raise ValueError('missing path')
    path = os.path.expanduser(path)
    if path.lower().endswith('.3dm') is False:
        raise ValueError('path must end with .3dm')

    # Close any command prompts & avoid modified prompts
    try:
        Rhino.RhinoDoc.ActiveDoc.Modified = False
    except Exception:
        pass

    # Make sure directory exists when creating a new file
    try:
        dirn = os.path.dirname(path)
        if dirn and not os.path.exists(dirn):
            os.makedirs(dirn)
    except Exception:
        pass

    if os.path.exists(path):
        rs.Command('_-Open "{}" _Enter'.format(path), False)
    else:
        rs.Command('_-New _NoTemplate _Enter', False)
        rs.Command('_-SaveAs "{}" _Enter'.format(path), False)
    return True

def _add_box(x, y, z, w, d, h):
    # 8-point box
    p0 = (x, y, z)
    p1 = (x + w, y, z)
    p2 = (x + w, y + d, z)
    p3 = (x, y + d, z)
    p4 = (x, y, z + h)
    p5 = (x + w, y, z + h)
    p6 = (x + w, y + d, z + h)
    p7 = (x, y + d, z + h)
    rs.EnableRedraw(False)
    try:
        bid = rs.AddBox([p0, p1, p2, p3, p4, p5, p6, p7])
    finally:
        rs.EnableRedraw(True)
    if not bid:
        raise RuntimeError('AddBox failed')
    return True

# ---- Per-connection worker ------------------------------------------------

def _handle_conn(conn, addr):
    try:
        line, err = _read_line(conn, timeout_sec=8.0, maxlen=1 << 20)
        if err:
            _reply(conn, {"ok": False, "error": err})
            return
        try:
            req = json.loads(line.strip())
        except Exception as e:
            _reply(conn, {"ok": False, "error": "bad json: {0}".format(e)})
            return

        act = req.get('action')

        if act == 'ping':
            _reply(conn, {"ok": True, "pong": True})
            return

        if act == 'shutdown':
            st = _get_state()
            ev = st.get('stop_event')
            if ev:
                ev.set()
            _reply(conn, {"ok": True})
            return

        if act == 'open_doc':
            path = req.get('path', '')
            ok, res = _on_ui(_safe_open_doc, path)
            if ok:
                _reply(conn, {"ok": True})
            else:
                _reply(conn, {"ok": False, "error": res})
            return

        if act == 'create_box':
            doc_path = req.get('docPath')
            if doc_path:
                ok, res = _on_ui(_safe_open_doc, doc_path)
                if not ok:
                    _reply(conn, {"ok": False, "error": "open_doc failed: {0}".format(res)})
                    return
            try:
                x = float(req.get('x', 0))
                y = float(req.get('y', 0))
                z = float(req.get('z', 0))
                w = float(req.get('width', 10))
                d = float(req.get('depth', 10))
                h = float(req.get('height', 10))
            except Exception as e:
                _reply(conn, {"ok": False, "error": "bad numeric args: {0}".format(e)})
                return

            ok, res = _on_ui(_add_box, x, y, z, w, d, h)
            if ok:
                _reply(conn, {"ok": True})
            else:
                _reply(conn, {"ok": False, "error": res})
            return

        _reply(conn, {"ok": False, "error": "unknown action: {0}".format(act)})

    finally:
        try:
            conn.close()
        except Exception:
            pass

# ---- Server thread --------------------------------------------------------

def _server_thread(sock, port, stop_event):
    print("[Listener] TCP listener on 127.0.0.1:{0}".format(port))
    sys.stdout.flush()
    _write_port(port)
    sock.settimeout(1.0)
    while not stop_event.is_set():
        try:
            conn, addr = sock.accept()
        except socket.timeout:
            continue
        except Exception:
            break
        t = threading.Thread(target=_handle_conn, args=(conn, addr))
        t.daemon = True
        t.start()
    try:
        sock.close()
    except Exception:
        pass
    print("[Listener] Stopped.")
    sys.stdout.flush()

# ---- Entry point ----------------------------------------------------------

def start_listener():
    st = _get_state()
    if st.get('running'):
        print("[Listener] Already running on port {0}".format(st.get('port')))
        sys.stdout.flush()
        return

    sock, port = _choose_port()
    stop_event = threading.Event()
    st['running'] = True
    st['port'] = port
    st['stop_event'] = stop_event
    st['sock'] = sock

    print("[Listener] Listener started.")
    sys.stdout.flush()
    th = threading.Thread(target=_server_thread, args=(sock, port, stop_event))
    th.daemon = True
    st['thread'] = th
    th.start()

if __name__ == "__main__":
    start_listener()
