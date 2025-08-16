#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Rhino3D MCP Server for macOS
Launches/targets Rhino and runs a Python script inside Rhino
that ensures the document exists, opens it, adds a box, and saves.
"""

import asyncio
import subprocess
import tempfile
import os
import sys
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
import mcp.types as types

RHINO_APP_NAME = "Rhino 7"  # Change to "Rhino 8" if you’re on 8

server = Server("rhino3d-server")

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="create_box",
            description="Create a simple box in Rhino; creates/opens docPath and saves",
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
                    "newInstance": {"type": "boolean", "default": False, "description": "Force a new Rhino instance"}
                }
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "create_box":
        return await create_box(arguments)
    raise ValueError(f"Unknown tool: {name}")

def _rhino_python_script(width, height, depth, x, y, z, doc_path):
    # This code runs INSIDE Rhino. Keep it ASCII-only to avoid encoding issues on Rhino 7.
    doc_literal = ('r"%s"' % doc_path) if doc_path else "None"
    return (
        "# coding: utf-8\n"
        "from __future__ import print_function\n"
        "import rhinoscriptsyntax as rs\n"
        "import Rhino\n"
        "import scriptcontext as sc\n"
        "import System\n"
        "import System.IO as IO\n"
        "doc_path = " + doc_literal + "\n"
        "\n"
        "def ensure_target_document(path):\n"
        "    try:\n"
        "        if not path:\n"
        "            return True\n"
        "        if IO.File.Exists(path):\n"
        "            Rhino.RhinoApp.RunScript('-Open \"{}\" _Enter'.format(path), False)\n"
        "        else:\n"
        "            # Save current (untitled) doc as the target to CREATE the file\n"
        "            Rhino.RhinoApp.RunScript('-SaveAs \"{}\" _Enter'.format(path), False)\n"
        "        return True\n"
        "    except Exception as e:\n"
        "        print('[MCP] ensure_target_document error: {}'.format(e))\n"
        "        return False\n"
        "\n"
        "ok = ensure_target_document(doc_path)\n"
        "if not ok:\n"
        "    print('[MCP] Could not open or create target document.')\n"
        "else:\n"
        "    p0 = (%s, %s, %s)\n"
        "    p1 = (%s, %s, %s)\n"
        "    p2 = (%s, %s, %s)\n"
        "    p3 = (%s, %s, %s)\n"
        "    p4 = (%s, %s, %s)\n"
        "    p5 = (%s, %s, %s)\n"
        "    p6 = (%s, %s, %s)\n"
        "    p7 = (%s, %s, %s)\n"
        "    box_id = rs.AddBox([p0,p1,p2,p3,p4,p5,p6,p7])\n"
        "    if box_id:\n"
        "        print('[MCP] Created box %s x %s x %s at (%s,%s,%s)')\n"
        "        Rhino.RhinoApp.RunScript('_-Save _Enter', False)\n"
        "    else:\n"
        "        print('[MCP] Error: AddBox returned None')\n"
        % (
            x, y, z,
            x + width, y, z,
            x + width, y + depth, z,
            x, y + depth, z,
            x, y, z + height,
            x + width, y, z + height,
            x + width, y + depth, z + height,
            x, y + depth, z + height,
            width, height, depth, x, y, z
        )
    )

async def create_box(args: dict) -> list[types.TextContent]:
    try:
        width = float(args.get("width", 10))
        height = float(args.get("height", 10))
        depth = float(args.get("depth", 10))
        x = float(args.get("x", 0))
        y = float(args.get("y", 0))
        z = float(args.get("z", 0))
        doc_path = args.get("docPath")
        new_instance = bool(args.get("newInstance", False))

        # Write the in-Rhino script to a temp file
        script_content = _rhino_python_script(width, height, depth, x, y, z, doc_path)
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write(script_content)
            f.flush()
            script_path = f.name

        # Build the macro: only run our Python script (it handles open/new/save)
        macro = '_-RunPythonScript "{}" _Enter'.format(script_path)

        # Launch Rhino via macOS 'open' so it stays open
        cmd = ["open"]
        if new_instance:
            cmd.append("-n")
        cmd += ["-a", RHINO_APP_NAME, "--args", "-runscript", macro]

        # Fire-and-forget; do not wait/block
        subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        where = (' in "{}"'.format(doc_path)) if doc_path else " in the active document"
        return [types.TextContent(
            type="text",
            text="Sent script to Rhino; will create/open the target and add the box{}.".format(where)
        )]
    except Exception as e:
        return [types.TextContent(type="text", text="Error creating box: {}".format(e))]

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
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main())
