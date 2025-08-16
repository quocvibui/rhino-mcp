# rhino_box_server.py
# Minimal Claude MCP server that creates a Rhino .3dm with a single box
# and (on macOS) opens it in Rhino.

import os, sys, tempfile, time, subprocess, logging
from typing import Optional

# MCP (FastMCP) – concise tool decorator API
from mcp.server.fastmcp import FastMCP  # official Python SDK's FastMCP interface
# Geometry I/O
import rhino3dm

# Important for MCP: avoid stdout logging on stdio transports
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

mcp = FastMCP("Rhino Box Server")

# Simple unit mapper (rhino3dm uses UnitSystem enum)
_UNIT_MAP = {
    "Millimeters": rhino3dm.UnitSystem.Millimeters,
    "Centimeters": rhino3dm.UnitSystem.Centimeters,
    "Meters":      rhino3dm.UnitSystem.Meters,
    "Inches":      rhino3dm.UnitSystem.Inches,
    "Feet":        rhino3dm.UnitSystem.Feet,
}

@mcp.tool()
def create_box(
    width: float = 100.0,
    depth: float = 100.0,
    height: float = 100.0,
    units: str = "Millimeters",
    save_path: Optional[str] = None,
    open_in_rhino: bool = True,
) -> str:
    """
    Create a new .3dm containing a single box at the world origin.

    Args:
        width:  Box size in X (in chosen units).
        depth:  Box size in Y (in chosen units).
        height: Box size in Z (in chosen units).
        units:  One of Millimeters, Centimeters, Meters, Inches, Feet.
        save_path: Optional absolute path to write the .3dm.
        open_in_rhino: On macOS, open the file when done.

    Returns:
        A message with the file path written.
    """
    # 1) Build a File3dm and set units
    model = rhino3dm.File3dm()
    model.Settings.ModelUnitSystem = _UNIT_MAP.get(units, rhino3dm.UnitSystem.Millimeters)

    # 2) Make a box on WorldXY
    plane = rhino3dm.Plane.WorldXY
    box = rhino3dm.Box(
        plane,
        rhino3dm.Interval(0.0, float(width)),
        rhino3dm.Interval(0.0, float(depth)),
        rhino3dm.Interval(0.0, float(height)),
    )

    # Python rhino3dm typically uses Brep.CreateFromBox(box)
    brep = rhino3dm.Brep.CreateFromBox(box)

    attrs = rhino3dm.ObjectAttributes()
    attrs.Name = "MCP_Box"
    model.Objects.AddBrep(brep, attrs)

    # 3) Save it
    if not save_path:
        save_path = os.path.join(
            tempfile.gettempdir(),
            f"mcp_box_{int(time.time())}.3dm",
        )

    ok = model.Write(save_path)
    if not ok:
        return "Failed to write 3dm file."

    # 4) Optionally open it (macOS)
    if open_in_rhino and sys.platform == "darwin":
        # Using 'open <file>' lets macOS choose the default .3dm handler (Rhino).
        try:
            subprocess.run(["open", save_path], check=False)
        except Exception as e:
            logging.warning("Could not open file automatically: %s", e)

    return f"Box created and saved to: {save_path}"

if __name__ == "__main__":
    # STDIO transport for Claude Desktop
    mcp.run(transport="stdio")
