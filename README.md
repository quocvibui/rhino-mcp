# Rhino MCP

AI-powered 3D modeling in Rhino 7 through Model Context Protocol.

## Overview

Production-ready MCP server with 49 tools for geometry creation, transformation, boolean operations, curve/surface manipulation, layer management, and analysis in Rhino 7.

**Key Features:**
- 49 comprehensive 3D modeling tools
- Safe JSON protocol over TCP sockets
- Modular architecture for easy expansion
- IronPython 2.7 compatible (Rhino 7)
- Direct scripting API (works without Claude)

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Rhino Listener

In Rhino 7, run:
```
_-RunPythonScript "/path/to/rhino-mcp/server.py" _Enter
```

You should see:
```
============================================================
RhinoMCP Listener
============================================================
Active on localhost:54321
49 commands available
Ready to receive commands
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

## Documentation

- **[MCP.md](MCP.md)** - Using with Claude Desktop
- **[SCRIPT.md](SCRIPT.md)** - Direct scripting without Claude
- **[TESTING.md](TESTING.md)** - Testing guide
- **[STYLE.md](STYLE.md)** - Code style guide
- **[IMPLEMENTED.md](IMPLEMENTED.md)** - Implementation status

## Architecture

```
┌─────────────────┐
│  Claude Desktop │ (Python 3.10+)
└────────┬────────┘
         │ MCP Protocol
         ▼
┌─────────────────┐
│    main.py      │ FastMCP server with 49 tools
│    tools/       │ Modular tool definitions
└────────┬────────┘
         │ JSON over TCP (localhost:54321)
         ▼
┌─────────────────┐
│   server.py     │ Socket server (IronPython 2.7)
│   rhino/        │ RhinoScriptSyntax wrappers
└─────────────────┘
         │
         ▼
    Rhino 7 API
```

**Three Layers:**

1. **MCP Layer** (`main.py`, `tools/`) - Python 3.10+, exposes 49 tools to Claude
2. **Socket Server** (`server.py`) - IronPython 2.7, runs inside Rhino
3. **Rhino Modules** (`rhino/`) - 26 modules organized by API category

## Tools (49)

### Geometry (12)
Points, lines, circles, arcs, ellipses, polylines, curves, boxes, spheres, cylinders, cones, torus

### Transformations (6)
Move, rotate, scale, mirror, copy, linear array

### Boolean Operations (3)
Union, difference, intersection

### Curve Operations (5)
Join, explode, offset, fillet, extend

### Surface Operations (3)
Extrude straight, revolve, loft

### Layer Management (6)
Create, delete, set current, color, visibility, list

### Analysis (4)
Measure distance, curve length, area, volume

### Selection (5)
Select all, by type, by layer, unselect, delete selected

### Object Properties (3)
Set name, color, layer

### Scene Understanding (2)
Get scene info, get selected objects

## File Structure

```
rhino-mcp/
├── main.py                    # MCP server entry point
├── server.py                  # Rhino socket server
├── test.py                    # Test suite (51 tests)
├── tools/                     # MCP tool definitions (26 modules)
│   ├── utils.py               # Shared socket communication
│   ├── geometry.py            # Geometry creation tools
│   ├── transformation.py      # Transform tools
│   ├── surface.py             # Surface tools
│   ├── curve.py               # Curve tools
│   ├── selection.py           # Selection tools
│   └── ...                    # 21 more modules
├── rhino/                     # RhinoScriptSyntax wrappers (26 modules)
│   ├── commands.py            # High-level command routing (49 commands)
│   ├── curve.py               # Curve functions
│   ├── surface.py             # Surface functions
│   ├── object.py              # Object manipulation
│   └── ...                    # 22 more modules
└── script/                    # Example scripts (7)
    ├── linear_array.py
    ├── spiral.py
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
```

## Testing

Run comprehensive test suite:
```bash
python3 test.py
```

Tests all 49 commands plus error handling (51 tests total). To do MCP testing, check out [TESTING.md](TESTING.md) for details.

## Troubleshooting

**Cannot connect to Rhino**
- Ensure Rhino 7 is running with listener active
- Check port 54321 is available

**Invalid syntax in Rhino**
- Use `server.py` (IronPython 2.7), not `main.py`
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
- **IronPython 2.7** (built into Rhino 7)
- **Rhino 7** for macOS
- **mcp** and **fastmcp** packages

## Tested On

- macOS Tahoe 26.0 (Darwin 25.0.0)
- Mac Silicon (Apple Silicon)
- Rhino 7 for macOS
- Python 3.10+

All 51 tests pass. Community contributions for other platforms welcome.

## License

MIT License - see [LICENSE](LICENSE) file for details.
