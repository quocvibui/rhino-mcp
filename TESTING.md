# Rhino MCP Testing Guide

Complete testing guide for verifying Rhino MCP works correctly with Rhino 8.

## Prerequisites

1. **Rhino 8** installed and running
2. **Python 3.10+** installed on your system
3. **MCP dependencies** installed: `pip install -r requirements.txt`

## Step 1: Start the Rhino Listener

In Rhino 8's command line, run:

```
_-RunPythonScript "/path/to/rhino-mcp/server.py" _Enter
```

Replace `/path/to/rhino-mcp/` with your actual path.

You should see this output in Rhino's command line:

```
============================================================
RhinoMCP Listener
============================================================
Starting background listener thread...
Listener started successfully
50 commands ready
============================================================
```

If you see errors:
- **"ModuleNotFoundError"** - Check that `server.py` can find the `rhino/` directory. The script auto-adds its parent directory to `sys.path`.
- **"Address already in use"** - Port 54321 is occupied. Close any previous Rhino instance or restart Rhino.

## Step 2: Run the Automated Test Suite

Open a terminal and run:

```bash
cd /path/to/rhino-mcp
python3 test.py
```

This runs 51 tests across 11 categories:

| Category | Tests | What's Tested |
|----------|-------|---------------|
| Scene Understanding | 2 | get_scene_info, get_selected_objects |
| Basic Geometry | 7 | point, line, circle, arc, ellipse, polyline, curve |
| 3D Solids | 5 | box, sphere, cylinder, cone, torus |
| Transformations | 6 | move, rotate, scale, mirror, copy, array |
| Boolean Operations | 3 | union, difference, intersection |
| Curve Operations | 5 | join, explode, offset, fillet, extend |
| Surface Operations | 3 | extrude, revolve, loft |
| Layer Management | 6 | create, delete, current, color, visibility, list |
| Analysis Tools | 4 | distance, curve length, area, volume |
| Object Properties | 3 | name, color, layer |
| Selection & Management | 5 | select all, by type, by layer, unselect, delete |
| Error Handling | 1 | unknown command returns error |

**Expected result:**
```
======================================================================
TEST RESULTS SUMMARY
======================================================================

Total Tests:  51
Passed:       51 (100.0%)
Failed:       0 (0.0%)

SUCCESS: All tests passed!
======================================================================
```

### Common Test Failures

**"Cannot connect to Rhino"** - The listener isn't running. Go back to Step 1.

**rotate_objects fails** - All commands now run on the UI thread via `InvokeOnUiThread`. If rotation still fails, restart Rhino and try again.

**Boolean operations fail** - Ensure the scene is clean. Booleans need proper overlapping solids. The test creates its own geometry, but leftover objects from previous runs can interfere.

## Step 3: Test MCP Connection with Claude Desktop

### 3a. Configure Claude Desktop

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

Restart Claude Desktop after saving.

### 3b. Verify MCP Tools Load

In Claude Desktop, you should see Rhino tools available. Ask:

```
Get the current scene info from Rhino
```

**Expected**: Claude calls `get_scene_info` and returns details about objects, layers, and units.

### 3c. Test Geometry Creation

```
Create a sphere at position (0, 0, 0) with radius 5
```

**Expected**: A sphere appears in Rhino at the origin.

```
Create a box at position (20, 0, 0) with width 10, depth 10, and height 10
```

**Expected**: A box appears at x=20.

### 3d. Test Transformations

```
Select all objects in Rhino
```

```
Move the selected objects by (0, 10, 0)
```

**Expected**: Objects shift 10 units in Y.

```
Rotate the selected objects around point (0, 0, 0) by 45 degrees
```

**Expected**: Objects rotate 45 degrees around origin.

### 3e. Test Boolean Operations

```
Unselect all objects
```

```
Create a box at (0, 40, 0) with dimensions 10x10x10
```

```
Create another box at (5, 40, 0) with dimensions 10x10x10
```

```
Select all objects and perform a boolean union
```

**Expected**: The two boxes merge into one solid.

### 3f. Test Layer Management

```
Create a new layer named "TestLayer" with color RGB(255, 0, 0)
```

```
Set the current layer to "TestLayer"
```

```
List all layers in the document
```

**Expected**: Layers listed including the new red "TestLayer".

### 3g. Test Code Execution

```
Create for me a spiral staircase in Rhino
```

**Expected**: Claude uses `execute_python_code` to write and run a script that generates a spiral staircase.

### 3h. Test Analysis

```
Create a sphere at origin with radius 5
Select the sphere
Measure its volume
```

**Expected**: Volume approximately 523.6 (4/3 * pi * 5^3).

## Step 4: Manual Socket Test (Optional)

For debugging connection issues, test the socket directly with Python:

```python
import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)
sock.connect(("localhost", 54321))

command = json.dumps({
	"type": "get_scene_info",
	"params": {}
})

sock.sendall(command.encode("utf-8"))
response = sock.recv(8192)
sock.close()

print(json.loads(response.decode("utf-8")))
```

**Expected**: JSON response with `"status": "success"` and scene data.

## Troubleshooting

### Listener won't start in Rhino 8

- Make sure you're using `_-RunPythonScript` (with underscores and dash)
- Verify Rhino 8 is using CPython 3 (default for new scripts)
- If using the legacy IronPython editor, switch to the new ScriptEditor

### Port already in use

```bash
lsof -i :54321
```

Kill the process using that port, or restart Rhino.

### MCP server not loading in Claude

- Check Claude logs: `~/Library/Logs/Claude/`
- Verify Python path: `which python3`
- Test MCP server directly: `python3 main.py` (should start without errors)
- Ensure `mcp` and `fastmcp` are installed: `pip3 list | grep -i mcp`

### Commands time out

- Rhino may be busy with a long operation
- The default socket timeout is 10 seconds
- Complex boolean or loft operations can take time
- Add delays between rapid-fire commands

## Success Criteria

All of the following should work:

- [ ] Listener starts in Rhino 8 without errors
- [ ] `python3 test.py` passes all 51 tests
- [ ] Claude Desktop shows Rhino tools
- [ ] `get_scene_info` returns scene data via Claude
- [ ] Geometry creation works (box, sphere, circle)
- [ ] Transformations work (move, rotate, scale)
- [ ] Boolean operations work (union, difference)
- [ ] Layer management works (create, list)
- [ ] Code execution works (parametric scripts)
- [ ] Analysis tools work (distance, area, volume)
