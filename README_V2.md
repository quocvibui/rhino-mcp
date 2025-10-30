# Rhino MCP v2.0 - Improved Implementation

AI-powered 3D modeling in Rhino 7 through Model Context Protocol.

## What's New in v2.0

**JSON Protocol** - Safer and more reliable than raw Python execution
**FastMCP** - Cleaner, simpler server implementation
**Pure Python** - No C# plugin installation required
**Better Scene Understanding** - Claude gets complete context
**IronPython 2.7 Compatible** - Works with Rhino 7 out of the box

## Quick Start

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Rhino Listener

Open Rhino 7 and run:

```
_-RunPythonScript "/Users/quocbui/Desktop/Projects/rhino_mcp/rhino_listener.py" _Enter
```

You should see:

```
============================================================
RhinoMCP Listener v2.0 - JSON Protocol
============================================================
RhinoMCP Listener active on localhost:54321
Using JSON protocol
Ready to receive commands
```

### 3. Configure Claude Desktop

Edit config at: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "rhino": {
      "command": "/usr/local/bin/python3",
      "args": [
        "/Users/quocbui/Desktop/Projects/rhino_mcp/src/server_fastmcp.py"
      ]
    }
  }
}
```

### 4. Restart Claude Desktop

Close and reopen Claude Desktop to load the MCP server.

### 5. Test It

In Claude, try:

```
Get scene info from Rhino
Create a box at origin with size 10x10x10
Create a sphere at (20, 0, 0) with radius 5
```

## Architecture

### JSON Protocol

Commands are sent as JSON:

```json
{
  "type": "create_box",
  "params": {
    "width": 10,
    "depth": 10,
    "height": 10,
    "x": 0,
    "y": 0,
    "z": 0
  }
}
```

Responses are JSON:

```json
{
  "status": "success",
  "result": {
    "id": "uuid",
    "type": "box"
  }
}
```

### Components

**rhino_listener.py** - Runs in Rhino, receives JSON commands
**server_fastmcp.py** - FastMCP server, sends JSON commands
**Claude Desktop** - Calls MCP tools to control Rhino

## Current Tools

### Scene Query

**get_scene_info** - Get complete scene information
- Total objects and layers
- Object types and counts
- Object locations and properties
- Document units

### Geometry Creation

**create_point** - Create a point
**create_line** - Create a line
**create_box** - Create a box
**create_sphere** - Create a sphere

## Testing Without Claude

Run the test script:

```bash
python3 test_rhino_listener.py
```

This tests the JSON protocol directly without needing Claude Desktop.

## Advantages Over Reference Implementation

### 1. Pure Python
- No C# plugin to install
- No Visual Studio build required
- Works immediately with Rhino 7

### 2. JSON Protocol
- Safer than exec()
- Better error handling
- Easier to debug

### 3. FastMCP
- Cleaner code
- Simpler tool registration
- Better type hints

### 4. Better for Claude
- Comprehensive scene queries
- Clear tool descriptions
- Structured responses

## Troubleshooting

### Cannot connect to Rhino
- Ensure Rhino 7 is running
- Verify listener script is active
- Check port 54321 is not blocked

### "invalid syntax" error in Rhino
- Script is IronPython 2.7 compatible
- Check you're using correct Python 2 syntax
- Verify json module is available

### MCP server fails to start
- Check Python 3.10+ is installed
- Verify `mcp` and `fastmcp` are installed
- Check paths in Claude config are absolute

## Next Steps

1. Add more geometry tools (cylinders, cones, curves)
2. Add object selection with filters
3. Add transformations (move, rotate, scale)
4. Add layer management
5. Add material properties

## Development

Follows STYLE.md:
- Tabs for indentation
- lowercase_with_underscores naming
- Concise docstrings
- Functions do one thing
- No emojis or decoration

## Comparison with jingcheng-chen/rhinomcp

| Feature | Their Implementation | Our Implementation |
|---------|---------------------|-------------------|
| Language | C# + Python | Pure Python |
| Installation | Yak package manager | Simple script |
| Protocol | JSON | JSON |
| MCP Library | FastMCP | FastMCP |
| Rhino Version | 7+ | 7 |
| Port | 1999 | 54321 |
| Scene Query | Limited (30 objects) | Comprehensive |
| Deployment | Complex | Simple |

## License

Open source - use freely for any purpose.
