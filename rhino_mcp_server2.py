#!/usr/bin/env python3
"""
Rhino3D MCP Server for macOS
Uses Rhino's command line interface and Python scripting
"""

import asyncio
import subprocess
import tempfile
import os
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
import mcp.types as types

server = Server("rhino3d-server")

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available Rhino tools"""
    return [
        types.Tool(
            name="create_box",
            description="Create a simple box in Rhino",
            inputSchema={
                "type": "object",
                "properties": {
                    "width": {"type": "number", "default": 10},
                    "height": {"type": "number", "default": 10},
                    "depth": {"type": "number", "default": 10},
                    "x": {"type": "number", "default": 0},
                    "y": {"type": "number", "default": 0},
                    "z": {"type": "number", "default": 0},
                    "docPath": {"type": "string", "description": "Full path to a .3dm to open/edit (optional)"},
                    "newInstance": {"type": "boolean", "default": False, "description": "Launch a new Rhino instance"}
                }
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    """Handle tool calls"""
    if name == "create_box":
        return await create_box(arguments)
    else:
        raise ValueError(f"Unknown tool: {name}")

async def create_box(args: dict) -> list[types.TextContent]:
    """Create a box in Rhino using a Rhino-Python script"""
    try:
        # Params
        width = args.get("width", 10)
        height = args.get("height", 10)
        depth = args.get("depth", 10)
        x = args.get("x", 0)
        y = args.get("y", 0)
        z = args.get("z", 0)
        doc_path = args.get("docPath")
        new_instance = bool(args.get("newInstance", False))

        # Rhino-Python script (EnableRedraw + 8-corner AddBox)
        script_content = f'''
import rhinoscriptsyntax as rs
rs.EnableRedraw(True)

# 8-corner box: bottom loop CCW, then matching top loop
p0 = ({x},           {y},           {z})
p1 = ({x + width},   {y},           {z})
p2 = ({x + width},   {y + depth},   {z})
p3 = ({x},           {y + depth},   {z})
p4 = ({x},           {y},           {z + height})
p5 = ({x + width},   {y},           {z + height})
p6 = ({x + width},   {y + depth},   {z + height})
p7 = ({x},           {y + depth},   {z + height})

box_id = rs.AddBox([p0, p1, p2, p3, p4, p5, p6, p7])

if box_id:
    print("Created box: {width}x{height}x{depth} at ({x},{y},{z})")
    print("Box ID: " + str(box_id))
else:
    print("Error: Failed to create box")
'''
        # Temp file (use realpath to avoid /tmp symlink issues)
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(script_content)
            f.flush()
            script_path = f.name
        script_path_real = os.path.realpath(script_path)

        try:
            # Build macro:
            #  - '!' cancels any active command
            #  - Use parenthesized RunPythonScript (most reliable on macOS)
            #  - ONLY open/create the doc when starting a NEW instance.
            #    For live edits, skip Open so we don't hit blocking prompts.
            macro_parts = ['!']

            if doc_path and new_instance:
                if os.path.exists(doc_path):
                    macro_parts.append(f'_-Open "{doc_path}" _Enter')
                else:
                    macro_parts.append('_-New _None _Enter')
                    macro_parts.append(f'_-SaveAs "{doc_path}" _Enter')

            macro_parts.append(f'_-RunPythonScript ( "{script_path_real}" ) _Enter')
            macro = " ".join(macro_parts)

            # Launch Rhino via macOS 'open'; add -n to force args delivery when needed
            cmd = ["open"]
            if new_instance:
                cmd.append("-n")
            cmd += ["-a", "Rhino 7", "--args", "-runscript", macro]

            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            if doc_path and new_instance:
                prefix = f'Opened "{doc_path}" and '
            elif doc_path:
                prefix = f'(Using current active doc; expected "{doc_path}") '
            else:
                prefix = ''
            detail = f'{prefix}added {width}x{height}x{depth} box at ({x},{y},{z}).'
            return [types.TextContent(type="text", text="Sent script to Rhino. " + detail)]

        finally:
            # Don't delete immediately; Rhino may still be reading it.
            pass

    except Exception as e:
        return [types.TextContent(type="text", text=f"Error creating box: {str(e)}")]

async def main():
    # Run the server using stdin/stdout streams
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
