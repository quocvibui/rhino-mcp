"""
Surface operation tools for Rhino
Extrude, revolve, loft, sweep
"""

import mcp.types as types


SURFACES_TOOLS = [
	types.Tool(
		name="extrude_curve",
		description="Extrude a curve straight along path",
		inputSchema={
			"type": "object",
			"properties": {
				"direction": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Extrusion direction vector [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				}
			},
			"required": ["direction"]
		}
	),
	types.Tool(
		name="revolve_curve",
		description="Revolve a curve around axis",
		inputSchema={
			"type": "object",
			"properties": {
				"axis_start": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Axis start point [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				},
				"axis_end": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Axis end point [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				},
				"angle": {
					"type": "number",
					"description": "Rotation angle in degrees",
					"default": 360
				}
			},
			"required": ["axis_start", "axis_end"]
		}
	),
	types.Tool(
		name="loft_curves",
		description="Loft surface through curves",
		inputSchema={
			"type": "object",
			"properties": {
				"closed": {
					"type": "boolean",
					"description": "Create closed loft",
					"default": False
				}
			}
		}
	),
	types.Tool(
		name="sweep_curve",
		description="Sweep rail curve along path",
		inputSchema={
			"type": "object",
			"properties": {
				"closed": {
					"type": "boolean",
					"description": "Create closed sweep",
					"default": False
				}
			}
		}
	),
	types.Tool(
		name="plane_surface",
		description="Create planar surface from curves",
		inputSchema={
			"type": "object",
			"properties": {}
		}
	)
]


def handle_surfaces_tool(name, args, send_fn):
	"""
	Handle surfaces tool calls
	name: Tool name
	args: Tool arguments
	send_fn: Function to send script to Rhino
	return: List of TextContent responses
	"""
	handlers = {
		"extrude_curve": _extrude_curve,
		"revolve_curve": _revolve_curve,
		"loft_curves": _loft_curves,
		"sweep_curve": _sweep_curve,
		"plane_surface": _plane_surface
	}

	handler = handlers.get(name)
	if not handler:
		return [types.TextContent(
			type="text",
			text=f"ERROR: Unknown surfaces tool: {name}"
		)]

	return handler(args, send_fn)


def _extrude_curve(args, send_fn):
	"""
	Extrude curve straight
	"""
	direction = args.get("direction", [0, 0, 1])

	script = f"""
import rhinoscriptsyntax as rs

curve = rs.GetObject("Select curve to extrude", rs.filter.curve, preselect=True)
if curve:
	start = (0, 0, 0)
	end = {tuple(direction)}
	surface = rs.ExtrudeCurveStraight(curve, start, end)
	if surface:
		rs.Redraw()
		print("SUCCESS: Curve extruded along {tuple(direction)}")
	else:
		print("ERROR: Failed to extrude curve")
else:
	print("ERROR: No curve selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _revolve_curve(args, send_fn):
	"""
	Revolve curve around axis
	"""
	axis_start = args.get("axis_start", [0, 0, 0])
	axis_end = args.get("axis_end", [0, 0, 1])
	angle = args.get("angle", 360)

	script = f"""
import rhinoscriptsyntax as rs

curve = rs.GetObject("Select curve to revolve", rs.filter.curve, preselect=True)
if curve:
	axis_start = {tuple(axis_start)}
	axis_end = {tuple(axis_end)}
	surface = rs.RevolveSurface(curve, axis_start, axis_end, {angle})
	if surface:
		rs.Redraw()
		print("SUCCESS: Curve revolved {angle} degrees")
	else:
		print("ERROR: Failed to revolve curve")
else:
	print("ERROR: No curve selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _loft_curves(args, send_fn):
	"""
	Loft surface through curves
	"""
	closed = args.get("closed", False)

	script = f"""
import rhinoscriptsyntax as rs

curves = rs.GetObjects("Select curves to loft", rs.filter.curve, preselect=True)
if curves and len(curves) >= 2:
	loft = rs.AddLoftSrf(curves, loft_type=0, closed={closed})
	if loft:
		rs.Redraw()
		print(f"SUCCESS: Lofted {{len(curves)}} curves")
	else:
		print("ERROR: Failed to loft curves")
elif curves:
	print("ERROR: Need at least 2 curves to loft")
else:
	print("ERROR: No curves selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _sweep_curve(args, send_fn):
	"""
	Sweep rail along path
	"""
	closed = args.get("closed", False)

	script = f"""
import rhinoscriptsyntax as rs

rail = rs.GetObject("Select rail curve", rs.filter.curve)
shape = rs.GetObject("Select shape curve", rs.filter.curve)

if rail and shape:
	sweep = rs.AddSweep1(rail, [shape], closed={closed})
	if sweep:
		rs.Redraw()
		print("SUCCESS: Sweep surface created")
	else:
		print("ERROR: Failed to create sweep")
else:
	print("ERROR: Need both rail and shape curves")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _plane_surface(args, send_fn):
	"""
	Create planar surface from curve
	"""
	script = """
import rhinoscriptsyntax as rs

curve = rs.GetObject("Select planar curve", rs.filter.curve, preselect=True)
if curve:
	if rs.IsCurvePlanar(curve) and rs.IsCurveClosed(curve):
		surface = rs.AddPlanarSrf(curve)
		if surface:
			rs.Redraw()
			print("SUCCESS: Planar surface created")
		else:
			print("ERROR: Failed to create surface")
	else:
		print("ERROR: Curve must be planar and closed")
else:
	print("ERROR: No curve selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]
