# Using Rhino MCP with Claude Desktop

This guide explains how to use the MCP server to let Claude AI control Rhino 7 interactively.

## Architecture

```
Claude Desktop <--> MCP Server <--> Rhino Listener <--> Rhino 7
   (UI)             (main.py)        (server.py)     (3D modeling)
```

Claude Desktop talks to the MCP server, which sends JSON commands over TCP to Rhino.

## Setup

### 1. Start Rhino Listener

Open Rhino 7 and run:

```
_-RunPythonScript "/path/to/rhino-mcp/server.py" _Enter
```

Replace `/path/to/rhino-mcp/` with your actual installation path.

You should see:
```
============================================================
RhinoMCP Listener
============================================================
Starting background listener thread...
Listener started successfully
50 commands ready
============================================================
```

### 2. Configure Claude Desktop

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
	"mcpServers": {
		"rhino": {
			"command": "/usr/local/bin/python3",
			"args": ["/path/to/rhino-mcp/src/server.py"]
		}
	}
}
```

Replace `/path/to/rhino-mcp/` with your actual installation path.

### 3. Restart Claude Desktop

Close and reopen Claude Desktop to load the MCP server.

### 4. Verify Connection

In Claude Desktop, type:
```
Get scene info from Rhino
```

Claude should respond with information about your Rhino scene (object counts, layers, units).

### 5. Customizing your Claude Project
Our current Rhino MCP allows for code execution, this means Claude can execute code directly
in Rhino. In order to get the best result. Drop the documents in `resources/` into your project folder. Add this instruction to the project:
```
If you have problems with debugging, search up: "https://developer.rhino3d.com/api/RhinoScriptSyntax/" or "RhinoAPI", "RhinoScriptSyntax"
```

## Usage Examples

### Basic Geometry

```
Create a box at origin with size 10x10x10
Create a sphere at (20, 0, 0) with radius 5
Create a circle at (40, 0, 0) with radius 8
```

### Transformations

```
Select all objects
Move objects by (10, 0, 0)
Rotate objects 45 degrees around origin
```

### Boolean Operations

```
Create two overlapping boxes
Select all
Boolean union to combine them
```

### Complex Modeling

```
Create a circle at origin with radius 5
Select it
Extrude the circle up by height 20
```

### Layer Management

```
Create a layer called "Walls" with red color (255,0,0)
Set current layer to "Walls"
Create a box (it will go on the Walls layer)
```

### Code Execution
```
Create for me a Voronoi pattern
Create for me grid with varying circle sizes
```

## How It Works

1. You type a natural language request in Claude Desktop
2. Claude analyzes your request and decides which MCP tools to call
3. The MCP server (src/server.py) formats the command as JSON
4. JSON is sent to Rhino listener on localhost:54321
5. Rhino listener executes the command using rhinoscriptsyntax
6. Result is returned as JSON through the chain back to Claude
7. Claude presents the result in natural language

## Troubleshooting

### Tools not appearing in Claude

- Check MCP server logs: `~/Library/Logs/Claude/mcp-server-rhino.log`
- Verify paths in config are absolute, not relative
- Ensure Python 3.10+ is installed: `python3 --version`
- Check FastMCP is installed: `pip3 list | grep fastmcp`

### Cannot connect to Rhino

- Ensure Rhino 7 is running
- Verify listener script is active (check Rhino command line for status message)
- Test connection manually: `python3 test.py`

### Commands fail

- Check Rhino command line for error messages
- Verify objects are selected when required (use "select all" first)
- Some operations require specific geometry types (e.g., boolean operations need closed solids)

## Tips

### Scene Understanding First

Always start by getting scene info:
```
Get scene info from Rhino
```

This helps Claude understand what's already in your scene.

### Selection is Key

Many operations require objects to be selected first:
```
Select all objects
Move objects by (5, 0, 0)
```

### Layer Organization

Use layers to organize complex models:
```
Create layer "Foundation" with gray color
Set current layer to "Foundation"
Create geometry for foundation
Create layer "Walls" with white color
Set current layer to "Walls"
Create geometry for walls
```

### Iterative Modeling

Claude can help with iterative design:
```
Create 10 spheres in a line, each 20 units apart
Select them all
Scale them by factor 1.5
```

## Limitations

- MCP server must be running (restarts with Claude Desktop)
- Rhino listener must be manually started in Rhino
- No real-time feedback (Claude polls for results)
- Complex parametric modeling is better done with Grasshopper
- File I/O operations not supported (save/open/export)

## Advanced Usage (Unstable)

### Multi-step Workflows

Claude can execute complex multi-step operations:
```
Create a parametric tower:
1. Create 10 circles stacked vertically, each 5 units apart
2. Make each circle slightly smaller than the one below
3. Loft them into a smooth surface
4. Create a central cylinder for structure
5. Boolean difference to hollow it out
```

### Analysis and Feedback

Claude can analyze your model:
```
Measure the volume of the selected object
Calculate the total surface area
Compare these values and suggest optimizations
```

### Batch Operations

Claude can perform batch operations:
```
Create a grid of 5x5 boxes, each 10x10x10, spaced 15 units apart
Color them in a gradient from red to blue
```

## See Also

- **[SCRIPT.md](SCRIPT.md)** - Write standalone Python scripts to control Rhino
- **[README.md](README.md)** - Full project documentation
- **[IMPLEMENTED.md](IMPLEMENTED.md)** - Implemented features
- **[TESTING.md](TESTING.md)** - How to test with Claude
- **[test.py](test.py)** - Test of 49 commands