# Quick Start Guide

## Prerequisites

1. Rhino 7 for macOS installed
2. Python 3.8+ installed
3. MCP client (Claude Desktop or compatible)

## Installation

```bash
cd /path/to/rhino_mcp
pip install -r requirements.txt
```

## Step-by-Step Setup

### Step 1: Start Rhino 7

Open Rhino 7 application

### Step 2: Load Listener in Rhino

In Rhino command line, type:

```
_-RunPythonScript
```

When prompted for file path, enter the full path:

```
/Users/quocbui/Desktop/Projects/rhino_mcp/rhino_listener.py
```

Press Enter

You should see:

```
============================================================
Rhino MCP Listener
============================================================
Rhino MCP Listener active on localhost:54321
Ready to receive commands from MCP server
============================================================
```

Keep Rhino open with this listener running.

### Step 3: Configure MCP Client

For Claude Desktop, edit config file:

macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`

Add this configuration:

```json
{
	"mcpServers": {
		"rhino": {
			"command": "python3",
			"args": [
				"/Users/quocbui/Desktop/Projects/rhino_mcp/src/server.py"
			]
		}
	}
}
```

Replace path with your actual project path.

### Step 4: Restart MCP Client

Close and reopen Claude Desktop or your MCP client.

### Step 5: Verify Connection

In Claude, try a simple command:

```
Create a box at origin with size 10x10x10
```

You should see the box appear in Rhino.

## Testing Without Rhino

To test that the server loads correctly without Rhino:

```bash
python3 test_tools.py
```

This will list all 47 available tools.

## Common Issues

### Listener fails to start in Rhino
- Check Python is enabled in Rhino
- Verify rhinoscriptsyntax imports correctly
- Look for error messages in Rhino command history

### MCP client cannot connect
- Verify path to server.py is absolute and correct
- Check Python 3 is in PATH
- Ensure mcp package is installed

### Commands fail with connection error
- Ensure Rhino is running
- Verify listener script is active
- Check port 54321 is not blocked

## Example Commands

### Geometry Creation
```
Add a circle at (10, 10, 0) with radius 5
Create a line from (0, 0, 0) to (10, 10, 10)
Add a polygon with 6 sides, radius 8 at origin
```

### 3D Solids
```
Create a sphere at (20, 0, 0) with radius 5
Add a cylinder at origin, radius 5, height 20
Make a torus at (0, 30, 0) with radii 10 and 2
```

### Layer Management
```
Create a layer named "Geometry" with red color
Set current layer to "Geometry"
List all layers
```

### Object Operations
```
Select all objects
Move selected objects by (10, 0, 0)
Rotate objects 45 degrees around origin
Scale objects by factor 2
```

### View Control
```
Zoom to show all objects
Set view to top
Set display mode to shaded
```

## Tips

1. Keep Rhino visible to see geometry being created
2. Listener runs in background - no need to restart
3. If connection fails, check Rhino command history for errors
4. Use clear, specific commands for best results

## Next Steps

- Explore all 47 tools in PROJECT_SUMMARY.md
- Read full documentation in README.md
- Check tool details in src/tools/ modules
