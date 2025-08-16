# rhino_listener.py  -- runs INSIDE Rhino (IronPython 2.7)
import os, socket, threading, json, time
import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

APP_DIR = os.path.expanduser("~/Library/Application Support/rhino_mcp")
PORT_FILE = os.path.join(APP_DIR, "port.txt")
HOST = "127.0.0.1"

def _log(msg):
    try:
        Rhino.RhinoApp.WriteLine("[Listener] " + str(msg))
    except:
        print("[Listener] " + str(msg))

def _ensure_dirs():
    if not os.path.isdir(APP_DIR):
        try: os.makedirs(APP_DIR)
        except: pass

def _pick_port():
    _ensure_dirs()
    # Reuse saved port if possible
    try:
        with open(PORT_FILE, "r") as f:
            p = int(f.read().strip())
            return p
    except:
        pass
    # Find a free one
    p = 53700
    while p < 54000:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((HOST, p))
            s.close()
            with open(PORT_FILE, "w") as f:
                f.write(str(p))
            return p
        except:
            try: s.close()
            except: pass
            p += 1
    raise Exception("No free port found")

def _safe_command(macro):
    try:
        return rs.Command(macro, True)
    except:
        _log("Command failed: " + macro)
        return False

def _ensure_doc_open(doc_path):
    if not doc_path:
        return
    active_path = None
    try:
        active_path = sc.doc.Path
    except:
        active_path = None
    if active_path and active_path.lower() == doc_path.lower():
        return
    if not os.path.exists(doc_path):
        _log("Creating new doc: " + doc_path)
        _safe_command("_-New _None _Enter")
        _safe_command("_No")  # answer possible 'Save changes?' from New
        _safe_command('_-SaveAs "{}" _Enter'.format(doc_path))
        return
    _safe_command("_No")  # answer 'Save changes?' if switching docs
    _safe_command('_-Open "{}" _Enter'.format(doc_path))

def _add_box(x, y, z, w, d, h):
    p0 = (x,     y,     z)
    p1 = (x+w,   y,     z)
    p2 = (x+w,   y+d,   z)
    p3 = (x,     y+d,   z)
    p4 = (x,     y,     z+h)
    p5 = (x+w,   y,     z+h)
    p6 = (x+w,   y+d,   z+h)
    p7 = (x,     y+d,   z+h)
    bid = rs.AddBox([p0,p1,p2,p3,p4,p5,p6,p7])
    try:
        sc.doc.Views.Redraw()
    except:
        pass
    return bid

def _handle_request(req):
    action = req.get("action")
    if action == "create_box":
        dp = req.get("docPath")
        _ensure_doc_open(dp)
        bid = _add_box(
            float(req.get("x", 0.0)),
            float(req.get("y", 0.0)),
            float(req.get("z", 0.0)),
            float(req.get("width", 10.0)),
            float(req.get("depth", 10.0)),
            float(req.get("height", 10.0)),
        )
        if bid:
            _log("Created box {}x{}x{} at ({},{},{}).".format(
                req.get("width"), req.get("height"), req.get("depth"),
                req.get("x"), req.get("y"), req.get("z")
            ))
            return {"ok": True, "boxId": str(bid)}
        return {"ok": False, "error": "Failed to create box"}
    return {"ok": False, "error": "Unknown action: " + str(action)}

def _client_thread(conn, addr):
    try:
        buf = ""
        while True:
            data = conn.recv(4096)
            if not data:
                break
            buf += data.decode("utf-8")
            while "\n" in buf:
                line, buf = buf.split("\n", 1)
                line = line.strip()
                if not line:
                    continue
                try:
                    req = json.loads(line)
                    resp = _handle_request(req)
                except Exception as e:
                    resp = {"ok": False, "error": "bad request: " + str(e)}
                conn.sendall((json.dumps(resp) + "\n").encode("utf-8"))
    except:
        pass
    try: conn.close()
    except: pass

def _serve(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, port))
    s.listen(5)
    _log("TCP listener on {}:{}".format(HOST, port))
    while True:
        try:
            c, a = s.accept()
            t = threading.Thread(target=_client_thread, args=(c, a))
            t.setDaemon(True)
            t.start()
        except:
            time.sleep(0.1)

def start():
    try:
        port = _pick_port()
    except Exception as e:
        _log("Failed to pick port: " + str(e))
        return
    t = threading.Thread(target=_serve, args=(port,))
    t.setDaemon(True)
    t.start()
    _log("Listener started.")
    try:
        with open(PORT_FILE, "w") as f:
            f.write(str(port))
    except:
        pass

if __name__ == "__main__":
    start()
