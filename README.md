# Rhino MCP Server

Model Context Protocol server for Rhino 7 integration with Claude and other LLM applications.

## Overview

Rhino MCP enables AI assistants to create and manipulate 3D geometry in Rhino 7 through a comprehensive set of tools organized by functionality. The server communicates with Rhino via socket connection for real-time geometry creation and manipulation.

## Features

### Geometry Tools
- Points, lines, circles, arcs, ellipses
- Polylines and regular polygons
- Parametric curve creation

### 3D Solids
- Box, sphere, cylinder, cone, torus
- Parametric solid primitives

### Curve Operations
- Join and explode curves
- Offset, fillet, extend
- Curve manipulation tools

### Surface Operations
- Extrude straight and along path
- Revolve around axis
- Loft through curves
- Sweep rail operations
- Planar surfaces

### Layer Management
- Create and delete layers
- Set current layer
- Layer colors and visibility
- List all layers

### Object Operations
- Select all or by layer
- Delete, move, copy objects
- Rotate, scale, mirror
- Object information queries

### View Control
- Zoom extents and selected
- Standard views (top, front, perspective, etc)
- Camera position and target
- Display modes (wireframe, shaded, rendered)

### Document Tools
- Clear document
- Document information
- Set units (mm, cm, m, inches, feet)
- Save document
- Count objects by type

## Requirements

- Python 3.8 or higher
- Rhino 7 for macOS
- MCP Python SDK

## Installation

1. Clone or download this repository

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Configure MCP client to use this server

## Setup

### 1. Start Rhino Listener

Open Rhino 7 and run the listener script:

```
_-RunPythonScript "/full/path/to/rhino_listener.py" _Enter
```

The listener will start in the background and display:
```
============================================================
Rhino MCP Listener
============================================================
Rhino MCP Listener active on localhost:54321
Ready to receive commands from MCP server
============================================================
```

Keep Rhino running with the listener active.

### 2. Configure MCP Client

Add to your MCP client configuration (e.g., Claude Desktop):

```json
{
	"mcpServers": {
		"rhino": {
			"command": "python",
			"args": ["/full/path/to/rhino_mcp/src/server.py"]
		}
	}
}
```

### 3. Start Using

With Rhino running and listener active, your MCP client can now execute Rhino commands.

## Usage Examples

### Create Basic Geometry

```
Create a box at origin with size 10x10x10
Add a sphere at (20, 0, 0) with radius 5
Draw a circle at (0, 20, 0) with radius 8
```

### Layer Management

```
Create a new layer called "Geometry" with red color
Set current layer to "Geometry"
List all layers in the document
```

### Object Operations

```
Select all objects
Move selected objects by vector (10, 0, 0)
Copy objects to (0, 20, 0)
Rotate objects 45 degrees around origin
```

### Surface Modeling

```
Create a circle and extrude it up by 20 units
Revolve a curve around the Z axis
Loft surfaces through multiple curves
```

## Architecture

```
rhino_mcp/
├── src/
│   ├── server.py          # Main MCP server entry point
│   ├── tools/             # Tool modules by category
│   │   ├── geometry.py    # Basic geometry tools
│   │   ├── solids.py      # 3D primitives
│   │   ├── curves.py      # Curve operations
│   │   ├── surfaces.py    # Surface operations
│   │   ├── layers.py      # Layer management
│   │   ├── objects.py     # Object operations
│   │   ├── view.py        # View and camera
│   │   └── document.py    # Document operations
│   └── utils/
│       ├── rhino_comm.py  # Socket communication
│       └── validators.py  # Input validation
├── rhino_listener.py      # Rhino-side listener script
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## How It Works

1. MCP client sends tool request to server
2. Server generates RhinoScript Python code
3. Code sent to Rhino via socket on port 54321
4. Rhino listener executes code in context
5. Result returned to server and client

## Troubleshooting

### Connection Refused Error
- Ensure Rhino 7 is running
- Verify listener script is active in Rhino
- Check no other process is using port 54321

### Script Execution Errors
- Check Rhino command history for detailed errors
- Verify object selection when required
- Ensure valid parameters for operations

### Listener Not Starting
- Check Python is available in Rhino
- Verify rhinoscriptsyntax module loads correctly
- Look for error messages in Rhino command line

## Development

### Code Style

Follow STYLE.md and AI_Development_Guidelines.md:
- Tabs for indentation
- lowercase_with_underscores for functions/variables
- Concise docstrings with param descriptions
- Functions do one thing well
- Keep line length under 100 characters

### Adding New Tools

1. Add tool definition to appropriate module in src/tools/
2. Implement handler function
3. Add to module's TOOLS list
4. Handler will be automatically registered

## License

Open source - use freely for any purpose.

## Credits

Built for Rhino 7 using RhinoScriptSyntax API and Model Context Protocol.
