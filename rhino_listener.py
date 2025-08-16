# rhino_listener.py
# Starts a tiny TCP server *inside* Rhino and executes JSON commands on the UI thread.

import os, json, socket, threading, time
import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino
from System import Action

PORT = int(os.getenv("MCP_PORT", "62111"))          # can be overridden by parent process
DOC  = os.getenv("MCP_DOC")                         # optional target .3dm at startup

def _ui(action):
    """Run a callable on Rhino's UI thread."""
    Rhino.RhinoApp.InvokeOnUiThread(Action(action))

def _ensure_doc_open():
    """Open or create DOC if provided."""
    if not DOC:
        return
    try:
        active_path = Rhino.RhinoDoc.ActiveDoc.Path or ""
        if os.path.exists(DOC):
            if os.path.realpath(active_path) != os.path.realpath(DOC):
                # New instance typically has an untitled doc -> no save prompt
                rs.Command('_-Open "{}" _Enter'.format(DOC))
        else:
            rs.Command('_-New _None _Enter')
            rs.Command('_-SaveAs "{}" _Enter'.format(DOC))
    except Exception as e:
        Rhino.RhinoApp.WriteLine("Listener: doc open error: {}".format(e))

def _cmd_create_box(args):
    w  = float(args.get("width", 10))
    h  = float(args.get("height", 10))
    d  = float(args.get("depth", 10))
    x  = float(args.get("x", 0))
    y  = float(args.get("y", 0))
    z  = float(args.get("z", 0))

    def run():
        try:
            rs.EnableRedraw(True)
            p0 = (x,         y,         z)
            p1 = (x + w,     y,         z)
            p2 = (x + w,     y + d,     z)
            p3 = (x,         y + d,     z)
            p4 = (x,         y,         z + h)
            p5 = (x + w,     y,         z + h)
            p6 = (x + w,     y + d,     z + h)
            p7 = (x,         y + d,     z + h)
            box_id = rs.AddBox([p0,p1,p2,p3,p4,p5,p6,p7])
            Rhino.RhinoApp.WriteLine("Listener: created box {}x{}x{} at ({},{},{}) -> {}".format(w,h,d,x,y,z,box_id))
        except Exception as e:
            Rhino.RhinoApp.WriteLine("Listener: create_box error: {}".format(e))
    _ui(run)
    return {"ok": True}

def _handle_message(line):
    try:
        msg = json.loads(line)
        cmd = msg.get("cmd")
        args = msg.get("args", {})
        if cmd == "create_box":
            return _cmd_create_box(args)
        return {"ok": False, "error": "unknown cmd '{}'".format(cmd)}
    except Exception as e:
        return {"ok": False, "error": str(e)}

def _serve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", PORT))
    s.listen(5)
    Rhino.RhinoApp.WriteLine("Listener: TCP server on 127.0.0.1:{} (doc='{}')".format(PORT, DOC or "(active)"))

    while True:
        conn, addr = s.accept()
        try:
            data = b""
            while True:
                chunk = conn.recv(65536)
                if not chunk:
                    break
                data += chunk
                if b"\n" in data:
                    break
            line = data.decode("utf-8").strip()
            reply = _handle_message(line)
            conn.sendall((json.dumps(reply) + "\n").encode("utf-8"))
        except Exception as e:
            try:
                conn.sendall((json.dumps({"ok": False, "error": str(e)}) + "\n").encode("utf-8"))
            except:
                pass
        finally:
            conn.close()

# Kick off
_ensure_doc_open()
t = threading.Thread(target=_serve)
t.daemon = True
t.start()
Rhino.RhinoApp.WriteLine("Listener: started.")
