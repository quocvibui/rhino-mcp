#!/usr/bin/env python3
# rhino_mcp_server2.py  -- MCP tool that talks to the Rhino listener
import asyncio, os, sys, json, time, socket, tempfile, subprocess
from pathlib import Path

from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
import mcp.types as types

APP_DIR = Path("~/Library/Application Support/rhino_mcp").expanduser()
PORT_FILE = APP_DIR / "port.txt"
LISTENER_PATH = Path("/Users/quocbui/desktop/rhino_mcp/rhino_listener.py")
RHINO_APP_NAME = "Rhino 7"

server = Server("rhino3d-server")

def _read_port_from_file():
    try:
        with open(PORT_FILE, "r") as f:
            return int(f.read().strip())
    except:
        return None

def _is_port_open(port: int, host="127.0.0.1") -> bool:
    try:
        s = socket.create_connection((host, port), timeout=0.2)
        s.close()
        return True
    except:
        return False

def _launch_rhino_and_start_listener(new_instance: bool) -> None:
    # Use macOS 'open' so we don't block; pass a macro that runs the listener script.
    macro = f'_-RunPythonScript "{str(LISTENER_PATH)}" _Enter'
    cmd = ["open"]
    if new_instance:
        cmd.append("-n")
    cmd += ["-a", RHINO_APP_NAME, "--args", "-runscript", macro]
    subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def _send_request(port: int, payload: dict, timeout=5.0) -> dict:
    s = socket.create_connection(("127.0.0.1", port), timeout=timeout)
    try:
        s.sendall((json.dumps(payload) + "\n").encode("utf-8"))
        s.settimeout(timeout)
        buf = b""
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            buf += chunk
            if b"\n" in buf:
                line, _rest = buf.split(b"\n", 1)
                return json.loads(line.decode("utf-8"))
        return {"ok": False, "error": "no response"}
    finally:
        try: s.close()
        except: pass

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="create_box",
            description="Create a simple box in Rhino (socket-based live edit)",
            inputSchema={
                "type": "object",
                "properties": {
                    "width": {"type": "number", "default": 10},
                    "height": {"type": "number", "default": 10},
                    "depth": {"type": "number", "default": 10},
                    "x": {"type": "number", "default": 0},
                    "y": {"type": "number", "default": 0},
                    "z": {"type": "number", "default": 0},
                    "docPath": {"type": "string", "description": "Target .3dm for this session (optional)"},
                    "newInstance": {"type": "boolean", "default": False, "description": "Force a brand new Rhino instance"},
                    "instancePort": {"type": "number", "description": "Reuse a specific Rhino listener port (advanced)"}
                },
                "required": []
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name != "create_box":
        raise ValueError(f"Unknown tool: {name}")
    return await create_box(arguments)

async def create_box(args: dict) -> list[types.TextContent]:
    try:
        width  = float(args.get("width", 10))
        height = float(args.get("height", 10))
        depth  = float(args.get("depth", 10))
        x = float(args.get("x", 0))
        y = float(args.get("y", 0))
        z = float(args.get("z", 0))
        doc_path = args.get("docPath") or None
        new_instance = bool(args.get("newInstance", False))
        pinned_port = args.get("instancePort")

        # 1) Decide which port to use
        port = int(pinned_port) if pinned_port else _read_port_from_file()

        # 2) If no listener or port closed, (re)launch Rhino and start the listener
        if not port or not _is_port_open(port):
            _launch_rhino_and_start_listener(new_instance)
            # Wait for port file and socket to become ready
            t0 = time.time()
            port = None
            while time.time() - t0 < 20.0:
                port = _read_port_from_file()
                if port and _is_port_open(port):
                    break
                time.sleep(0.5)
            if not port or not _is_port_open(port):
                return [types.TextContent(type="text", text=f"Error: Could not reach Rhino listener.")]

        # 3) Send the create_box request
        payload = {
            "action": "create_box",
            "width": width, "height": height, "depth": depth,
            "x": x, "y": y, "z": z,
            "docPath": doc_path
        }
        resp = _send_request(port, payload, timeout=10.0)

        if resp.get("ok"):
            target = f'Opened "{doc_path}" and ' if doc_path else ""
            msg = f"Live edit OK. {target}added {width}x{height}x{depth} box at ({x},{y},{z})."
            return [types.TextContent(type="text", text=msg)]
        else:
            return [types.TextContent(type="text", text=f"Listener error: {resp.get('error')}")]

    except Exception as e:
        return [types.TextContent(type="text", text=f"Server error: {e}")]

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="rhino3d-server",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={}
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main())
