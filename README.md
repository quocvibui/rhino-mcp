# Rhino MCP

AI-powered 3D modeling in Rhino 7 through Model Context Protocol.

## Overview

Production-ready Rhino 7 MCP server with 49 comprehensive tools for geometry creation, transformation, boolean operations, curve/surface manipulation, layer management, and analysis.

**Key Features:**
- Safe JSON protocol over TCP sockets
- IronPython 2.7 compatible for Rhino 7
- FastMCP for clean tool registration
- Comprehensive scene understanding for Claude
- Direct scripting API (use without Claude)

## Documentation

- **[MCP.md](MCP.md)** - Using with Claude Desktop (AI-assisted 3D modeling)
- **[SCRIPT.md](SCRIPT.md)** - Direct scripting without Claude (algorithmic generation)
- **[STYLE.md](STYLE.md)** - Code style guide
- **script/** - Example pattern generation scripts

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Rhino Listener

Open Rhino 7 and run:

```
_-RunPythonScript "/path/to/rhino_mcp/rhino_listener.py" _Enter
```

Replace `/path/to/rhino_mcp/` with your actual installation path.

You should see:
```
============================================================
RhinoMCP Listener
============================================================
Active on localhost:54321
49 commands available
JSON protocol
Ready to receive commands
============================================================
```

### 3. Configure Claude Desktop

Edit: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
	"mcpServers": {
		"rhino": {
			"command": "/usr/local/bin/python3",
			"args": ["/path/to/rhino_mcp/src/server.py"]
		}
	}
}
```

Replace `/path/to/rhino_mcp/` with your actual installation path.

### 4. Restart Claude Desktop

Close and reopen Claude Desktop to load the MCP server.

### 5. Test

Try in Claude:
```
Get scene info from Rhino
Create a box at origin with size 10x10x10
Create a sphere at (20, 0, 0) with radius 5
```

## Architecture

### JSON Protocol

Commands are JSON:
```json
{
	"type": "create_box",
	"params": {"width": 10, "depth": 10, "height": 10, "x": 0, "y": 0, "z": 0}
}
```

Responses are JSON:
```json
{
	"status": "success",
	"result": {"id": "uuid", "type": "box"}
}
```

### Components

**rhino_listener.py** - Runs in Rhino (IronPython 2.7)
- Socket server on port 54321
- Receives JSON commands
- Executes rhinoscriptsyntax functions
- Returns JSON responses

**src/server.py** - MCP server (Python 3.10+)
- FastMCP server with 49 tools
- Sends JSON to Rhino
- Handles responses

## Tools (49 Total)

### Scene Understanding (2)
- **get_scene_info** - Object counts, layers, units, locations
- **get_selected_objects** - Query selection details

### Basic Geometry (7)
- **create_point**, **create_line**, **create_circle**
- **create_arc**, **create_ellipse**
- **create_polyline**, **create_curve**

### 3D Solids (5)
- **create_box**, **create_sphere**, **create_cylinder**
- **create_cone**, **create_torus**

### Transformations (6)
- **move_objects**, **rotate_objects**, **scale_objects**
- **mirror_objects**, **copy_objects**, **array_linear**

### Boolean Operations (3)
- **boolean_union** - Combine solids
- **boolean_difference** - Subtract solids
- **boolean_intersection** - Keep overlapping volume

### Curve Operations (5)
- **join_curves**, **explode_curves**, **offset_curve**
- **fillet_curves**, **extend_curve**

### Surface Operations (3)
- **extrude_curve_straight** - Extrude up/down
- **revolve_curve** - Revolve around axis
- **loft_curves** - Smooth surface through curves

### Layer Management (6)
- **create_layer**, **delete_layer**, **set_current_layer**
- **set_layer_color**, **set_layer_visibility**, **list_layers**

### Analysis (4)
- **measure_distance**, **measure_curve_length**
- **measure_area**, **measure_volume**

### Object Properties (3)
- **set_object_name**, **set_object_color**, **set_object_layer**

### Selection (5)
- **select_all**, **select_by_type**, **select_by_layer**
- **unselect_all**, **delete_selected**

## Usage Examples

### Create Geometry
```
Create a box 10x10x10 at origin
Create a sphere at (20,0,0) with radius 5
Create a circle at origin with radius 8
Create an arc at (0,10,0) with radius 5 from 0 to 180 degrees
```

### Transformations
```
Select all objects
Move objects by (10, 0, 0)
Rotate objects 45 degrees around origin
Scale objects by factor 2 from origin
```

### Boolean Operations
```
Create a box and sphere that overlap
Select all
Boolean union to combine them into one solid
```

### Layer Organization
```
Create layer "Walls" with red color (255,0,0)
Set current layer to "Walls"
Create geometry (it goes on Walls layer)
```

### Surface Modeling
```
Create a circle at origin
Select the circle
Extrude it straight up by height 20
```

## Testing

### Comprehensive Test Suite

The test suite verifies all 49 commands plus error handling (51 tests total).

Run tests:
```bash
python3 test_rhino_listener.py
```

Features:
- Tests all 49 commands organized by category
- 0.3 second delay between tests to prevent Rhino crashes
- Pass/fail tracking with percentages
- Detailed error reporting for failed tests
- No Claude Desktop required

Test categories:
1. Scene Understanding (2 tests)
2. Basic Geometry (7 tests)
3. 3D Solids (5 tests)
4. Transformations (6 tests)
5. Boolean Operations (3 tests)
6. Curve Operations (5 tests)
7. Surface Operations (3 tests)
8. Layer Management (7 tests)
9. Analysis Tools (4 tests)
10. Object Properties (3 tests)
11. Selection & Management (5 tests)
12. Error Handling (1 test)

Example output:
```
RHINO MCP COMPREHENSIVE TEST SUITE
======================================================================

Checking Rhino connection...
Connection OK

[1/11] SCENE UNDERSTANDING (2 tests)
----------------------------------------------------------------------
  PASS: get_scene_info
  PASS: get_selected_objects

...

======================================================================
TEST RESULTS SUMMARY
======================================================================

Total Tests:  51
Passed:       51 (100.0%)
Failed:       0 (0.0%)

SUCCESS: All tests passed!
======================================================================
```

## File Structure

```
rhino_mcp/
├── rhino_listener.py                 # Rhino listener (49 commands)
├── src/
│   └── server.py                     # MCP server (49 tools)
├── script/                           # Example pattern scripts
│   ├── linear_array.py               # Line of spheres
│   ├── grid_pattern.py               # 2D grid of boxes
│   ├── spiral.py                     # 3D spiral of points
│   ├── parametric_tower.py           # Lofted twisting tower
│   ├── fractal_tree.py               # Recursive tree structure
│   ├── wave_surface.py               # Sine wave surface
│   └── building_generator.py         # Multi-story building
├── test_rhino_listener.py            # Test suite (51 tests)
├── requirements.txt                  # Dependencies
├── README.md                         # Documentation
├── MCP.md                            # Claude Desktop guide
├── SCRIPT.md                         # Direct scripting guide
├── STYLE.md                          # Code style guide
└── AI_Development_Guidelines.md      # Development rules
```

## Troubleshooting

### Cannot connect to Rhino
- Ensure Rhino 7 is running
- Verify listener script is active
- Check port 54321 is not blocked

### Invalid syntax error in Rhino
- Ensure using rhino_listener.py
- Check IronPython 2.7 compatibility
- Verify json module available

### MCP server fails to start
- Check Python 3.10+ installed
- Verify mcp and fastmcp installed: `pip install mcp fastmcp`
- Check paths in Claude config are absolute

### Tools not appearing in Claude
- Restart Claude Desktop after config change
- Check MCP server logs in: `~/Library/Logs/Claude/`
- Verify server.py path is correct

## Development

Follow STYLE.md:
- Tabs for indentation
- lowercase_with_underscores naming
- Concise docstrings
- Functions do one thing
- No emojis or decoration

## Testing Results

Comprehensive test suite covers all functionality:
- 51 tests total (49 commands + error handling + multi-param tests)
- Organized into 12 categories
- Pass/fail tracking with percentages
- Detailed error reporting
- 0.3s delay between tests for stability

## Requirements

- Python 3.10+ (for MCP server)
- IronPython 2.7 (built into Rhino 7)
- Rhino 7 for macOS
- mcp package
- fastmcp package

## Tested On

This project was developed and tested on:
- **Hardware:** Mac Silicon (Apple Silicon)
- **OS:** macOS Tahoe 26.0 (Darwin 25.0.0)
- **Rhino:** Rhino 7 for macOS
- **Python:** Python 3.10+

All 51 tests pass on this configuration. Community contributions for other platforms welcome.

## License

MIT License - see [LICENSE](LICENSE) file for details.

Free to use, modify, and distribute for any purpose.

## Credits

Built for Rhino 7 using RhinoScriptSyntax API and Model Context Protocol.
Implements safer JSON protocol instead of reference implementation's exec() approach.
