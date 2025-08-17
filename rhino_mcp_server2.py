#!/usr/bin/env python3
"""
Simple Rhino3D MCP Server using socket communication
Works with Rhino 7 on macOS
"""

import asyncio
import socket
import json
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
import mcp.types as types

server = Server("rhino3d-server")

# Rhino socket connection settings
RHINO_HOST = "localhost"
RHINO_PORT = 54321

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
                    "z": {"type": "number", "default": 0}
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

async def send_to_rhino(script: str) -> str:
    """Send Python script to Rhino via socket"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((RHINO_HOST, RHINO_PORT))
        
        # Send script
        sock.send(script.encode('utf-8'))
        
        # Receive response
        response = sock.recv(1024).decode('utf-8')
        sock.close()
        
        return response
        
    except ConnectionRefusedError:
        return "ERROR: Cannot connect to Rhino. Make sure Rhino is running and the socket server is started."
    except Exception as e:
        return f"ERROR: {str(e)}"

async def create_box(args: dict) -> list[types.TextContent]:
    """Create a box in Rhino"""
    try:
        # Get parameters
        width = args.get("width", 10)
        height = args.get("height", 10)
        depth = args.get("depth", 10)
        x = args.get("x", 0)
        y = args.get("y", 0)
        z = args.get("z", 0)
        
        # Create Python script for Rhino using 8-corner method
        script = """
import rhinoscriptsyntax as rs

# Create box using the 8-corner method required by rs.AddBox
# bottom rectangle (counterclockwise), then the matching top rectangle
p0 = (%s,           %s,           %s)
p1 = (%s,   %s,           %s)
p2 = (%s,   %s,   %s)
p3 = (%s,           %s,   %s)
p4 = (%s,           %s,           %s)
p5 = (%s,   %s,           %s)
p6 = (%s,   %s,   %s)
p7 = (%s,           %s,   %s)

box_id = rs.AddBox([p0, p1, p2, p3, p4, p5, p6, p7])

if box_id:
    rs.Redraw()
    print("Created box: %sx%sx%s at (%s,%s,%s)")
    print("Box ID: " + str(box_id))
    print("SUCCESS")
else:
    print("Error: Failed to create box")
""" % (x, y, z,                           # p0
       x + width, y, z,                   # p1
       x + width, y + depth, z,           # p2
       x, y + depth, z,                   # p3
       x, y, z + height,                  # p4
       x + width, y, z + height,          # p5
       x + width, y + depth, z + height,  # p6
       x, y + depth, z + height,          # p7
       width, height, depth, x, y, z)     # for print statements
        
        # Send to Rhino
        response = await send_to_rhino(script)
        
        if "SUCCESS" in response:
            return [types.TextContent(
                type="text",
                text=f"✅ Created {width}x{height}x{depth} box at ({x},{y},{z}) in Rhino!"
            )]
        else:
            return [types.TextContent(
                type="text",
                text=f"❌ {response}"
            )]
        
    except Exception as e:
        return [types.TextContent(
            type="text",
            text=f"❌ Error: {str(e)}"
        )]

async def main():
    from mcp.server.stdio import stdio_server
    
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