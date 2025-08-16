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

async def create_box(args: dict) -> list[types.TextContent]:
    """Create a box in Rhino using Python script"""
    try:
        # Get parameters with defaults
        width = args.get("width", 10)
        height = args.get("height", 10)
        depth = args.get("depth", 10)
        x = args.get("x", 0)
        y = args.get("y", 0)
        z = args.get("z", 0)
        
        # Create Python script for Rhino
        script_content = f'''
import rhinoscriptsyntax as rs

# Create box using the 8-corner method required by rs.AddBox
# bottom rectangle (counterclockwise), then the matching top rectangle
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
        
        # Write script to temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(script_content)
            script_path = f.name
        
        try:
            # Run the script in Rhino
            # This assumes Rhino is in Applications folder
            rhino_path = "/Applications/Rhino 7.app/Contents/MacOS/Rhinoceros"
            
            if not os.path.exists(rhino_path):
                return [types.TextContent(
                    type="text",
                    text="Error: Rhino 7 not found. Please make sure Rhino 7 is installed."
                )]
            
            # Execute the script (launch Rhino without waiting so the app stays open)
            cmd = ["open", "-a", "Rhino 7", "--args", "-runscript", f'_-RunPythonScript "{script_path}" _Enter']
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            if result.returncode == 0:
                return [types.TextContent(
                    type="text",
                    text=f"Box creation script sent to Rhino. Check Rhino for the new {width}x{height}x{depth} box at ({x},{y},{z})"
                )]
            else:
                return [types.TextContent(
                    type="text",
                    text=f"Error running script: {result.stderr}"
                )]
                
        finally:
            pass
        
    except Exception as e:
        return [types.TextContent(
            type="text", 
            text=f"Error creating box: {str(e)}"
        )]

async def main():
    # Run the server using stdin/stdout streams
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