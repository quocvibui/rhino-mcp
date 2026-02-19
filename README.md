# Rhino MCP

AI-powered 3D modeling in Rhino 8 through Model Context Protocol.

## Overview

MCP server with 135 tools for code execution, geometry creation, surface/curve/mesh operations, transformations, booleans, layer/material/group/block management, views, annotations, and analysis in Rhino 8.

**Key Features:**
- 135 comprehensive 3D modeling tools
- Safe JSON protocol over TCP sockets
- Modular architecture for easy expansion
- CPython 3 compatible (Rhino 8)
- Direct scripting API (works without Claude)

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Rhino Listener

In Rhino 8, run:
```
_-RunPythonScript "/path/to/rhino-mcp/server.py" _Enter
```

You should see:
```
============================================================
RhinoMCP Listener
============================================================
Starting background listener thread...
Listener started successfully
135 commands ready
============================================================
```

### 3. Configure Claude Desktop

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
	"mcpServers": {
		"rhino": {
			"command": "/usr/local/bin/python3",
			"args": ["/path/to/rhino-mcp/main.py"]
		}
	}
}
```

### 4. Restart Claude Desktop & Test

Try: `Get scene info from Rhino and create a box at origin`

### 5. Customizing your Claude Project
Our current Rhino MCP allows for code execution, this means Claude can execute code directly
in Rhino. In order to get the best result. Drop the documents in `resources/` into your project folder. Add this instruction to the project:
```
If you have problems with debugging, search up: "https://developer.rhino3d.com/api/RhinoScriptSyntax/" or "RhinoAPI", "RhinoScriptSyntax"
```

## Documentation

- **[MCP.md](MCP.md)** - Using with Claude Desktop
- **[SCRIPT.md](SCRIPT.md)** - Direct scripting without Claude
- **[TESTING.md](TESTING.md)** - Testing guide
- **[IMPLEMENTED.md](IMPLEMENTED.md)** - Implementation features and status
- **[STYLE.md](STYLE.md)** - Code style guide

## Architecture

```
┌─────────────────┐
│  Claude Desktop │ (Python 3.10+)
└────────┬────────┘
         │ MCP Protocol
         ▼
┌─────────────────┐
│    main.py      │ FastMCP server with 135 tools
│    tools/       │ Modular tool definitions
└────────┬────────┘
         │ JSON over TCP (localhost:54321)
         ▼
┌─────────────────┐
│   server.py     │ Socket server (CPython 3 - Rhino 8)
│   rhino/        │ RhinoScriptSyntax wrappers
└─────────────────┘
         │
         ▼
    Rhino 8 API
```

**Three Layers:**

1. **MCP Layer** (`main.py`, `tools/`) - Python 3.10+, exposes 135 tools to Claude
2. **Socket Server** (`server.py`) - CPython 3, runs inside Rhino 8
3. **Rhino Modules** (`rhino/`) - Organized by API category

## File Structure

```
rhino-mcp/
├── main.py                    # MCP server entry point
├── server.py                  # Rhino socket server
├── test.py                    # Test suite (185 tests)
├── tools/                     # MCP tool definitions (16 modules)
│   ├── utils.py               # Shared socket communication
│   ├── geometry.py            # Geometry creation tools
│   ├── surface.py             # Surface/solid tools
│   ├── curve.py               # Curve tools
│   ├── mesh.py                # Mesh tools
│   ├── transformation.py      # Transform tools
│   ├── layer.py               # Layer management tools
│   ├── object.py              # Object property tools
│   ├── selection.py           # Selection tools
│   ├── document.py            # Document/scene tools
│   ├── group.py               # Group tools
│   ├── view.py                # View/camera tools
│   ├── block.py               # Block instance tools
│   ├── material.py            # Material tools
│   ├── annotation.py          # Annotation tools
│   ├── userdata.py            # User data tools
│   └── utility.py             # Measurement + code execution
├── rhino/                     # RhinoScriptSyntax wrappers (16 modules)
│   ├── commands.py            # High-level command routing (135 commands)
│   ├── curve.py               # Curve functions
│   ├── surface.py             # Surface functions
│   ├── mesh.py                # Mesh functions
│   ├── object.py              # Object manipulation
│   ├── selection.py           # Selection functions
│   ├── layer.py               # Layer functions
│   ├── geometry.py            # Geometry functions
│   ├── plane.py               # Plane functions
│   ├── document.py            # Document functions
│   ├── group.py               # Group functions
│   ├── view.py                # View/camera functions
│   ├── block.py               # Block functions
│   ├── material.py            # Material functions
│   ├── annotation.py          # Annotation functions
│   ├── userdata.py            # User data functions
│   └── utility.py             # Utility functions
├── script/                    # Example scripts
│   ├── linear_array.py
│   ├── spiral.py
│   └── ...
└── resources/                 # Drop into your Claude Project folder
    └── ...
```

## Usage Examples

```
# Geometry
Create a box 10x10x10 at origin
Create a sphere at (20,0,0) with radius 5

# Transformations
Select all objects
Move them by (10, 0, 0)
Rotate them 45 degrees around origin

# Booleans
Create two overlapping boxes
Select all and boolean union them

# Layers
Create layer "Walls" with red color
Set current layer to "Walls"

# Analysis
Measure the distance between (0,0,0) and (10,0,0)
Select the circle and measure its area

# Mesh
Create a mesh from selected surfaces
Boolean union the selected meshes

# Views
Set display mode to Wireframe
Zoom to fit all objects

# Materials
Add a red material to the selected object
Set material transparency to 50%

# Code Execution
Create for me a spiral staircase in Rhino
```

## Testing

Run comprehensive test suite:
```bash
python3 test.py
```

Tests all 135 commands plus error handling (185 tests total). See [TESTING.md](TESTING.md) for details.

## Troubleshooting

**Cannot connect to Rhino**
- Ensure Rhino 8 is running with listener active
- Check port 54321 is available

**Invalid syntax in Rhino**
- server.py and rhino/ modules use CPython 3 (Rhino 8)
- Verify `rhino/` module is accessible

**MCP server fails**
- Check Python 3.10+ installed
- Run: `pip install -r requirements.txt`
- Use absolute paths in Claude config

**Tools not in Claude**
- Restart Claude Desktop after config change
- Check logs: `~/Library/Logs/Claude/`

## Requirements

- **Python 3.10+** (for MCP server)
- **Rhino 8** for macOS (ships with CPython 3)
- **mcp** and **fastmcp** packages

## Tested On

- macOS (Apple Silicon)
- Rhino 8 for macOS
- Python 3.10+

All 185 tests pass. Community contributions for other platforms welcome.

**Note:** All commands are dispatched to Rhino's UI thread to prevent macOS threading crashes.

## License

MIT License - see [LICENSE](LICENSE) file for details.
