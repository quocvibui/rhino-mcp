"""
Curve operation tools for Rhino
Join, explode, offset, fillet, chamfer, extend
"""

import mcp.types as types


CURVES_TOOLS = [
	types.Tool(
		name="join_curves",
		description="Join multiple curves into one",
		inputSchema={
			"type": "object",
			"properties": {
				"delete_input": {
					"type": "boolean",
					"description": "Delete input curves after join",
					"default": True
				}
			}
		}
	),
	types.Tool(
		name="explode_curve",
		description="Explode a curve into segments",
		inputSchema={
			"type": "object",
			"properties": {
				"delete_input": {
					"type": "boolean",
					"description": "Delete input curve after explode",
					"default": True
				}
			}
		}
	),
	types.Tool(
		name="offset_curve",
		description="Offset a curve by distance",
		inputSchema={
			"type": "object",
			"properties": {
				"distance": {"type": "number", "description": "Offset distance"}
			},
			"required": ["distance"]
		}
	),
	types.Tool(
		name="fillet_curves",
		description="Fillet two curves with radius",
		inputSchema={
			"type": "object",
			"properties": {
				"radius": {"type": "number", "description": "Fillet radius"}
			},
			"required": ["radius"]
		}
	),
	types.Tool(
		name="extend_curve",
		description="Extend a curve by length",
		inputSchema={
			"type": "object",
			"properties": {
				"length": {"type": "number", "description": "Extension length"},
				"side": {
					"type": "integer",
					"description": "Side to extend: 0=start, 1=end, 2=both",
					"default": 1
				}
			},
			"required": ["length"]
		}
	)
]


def handle_curves_tool(name, args, send_fn):
	"""
	Handle curves tool calls
	name: Tool name
	args: Tool arguments
	send_fn: Function to send script to Rhino
	return: List of TextContent responses
	"""
	handlers = {
		"join_curves": _join_curves,
		"explode_curve": _explode_curve,
		"offset_curve": _offset_curve,
		"fillet_curves": _fillet_curves,
		"extend_curve": _extend_curve
	}

	handler = handlers.get(name)
	if not handler:
		return [types.TextContent(
			type="text",
			text=f"ERROR: Unknown curves tool: {name}"
		)]

	return handler(args, send_fn)


def _join_curves(args, send_fn):
	"""
	Join selected curves
	"""
	delete_input = args.get("delete_input", True)

	script = f"""
import rhinoscriptsyntax as rs

curves = rs.GetObjects("Select curves to join", rs.filter.curve, preselect=True)
if curves and len(curves) > 1:
	joined = rs.JoinCurves(curves, delete_input={delete_input})
	if joined:
		rs.Redraw()
		print(f"SUCCESS: Joined {{len(curves)}} curves into {{len(joined)}} result(s)")
	else:
		print("ERROR: Failed to join curves")
elif curves:
	print("ERROR: Need at least 2 curves to join")
else:
	print("ERROR: No curves selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _explode_curve(args, send_fn):
	"""
	Explode selected curve
	"""
	delete_input = args.get("delete_input", True)

	script = f"""
import rhinoscriptsyntax as rs

curve = rs.GetObject("Select curve to explode", rs.filter.curve, preselect=True)
if curve:
	segments = rs.ExplodeCurves(curve, delete_input={delete_input})
	if segments:
		rs.Redraw()
		print(f"SUCCESS: Exploded curve into {{len(segments)}} segments")
	else:
		print("ERROR: Failed to explode curve")
else:
	print("ERROR: No curve selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _offset_curve(args, send_fn):
	"""
	Offset selected curve
	"""
	distance = args.get("distance", 1)

	script = f"""
import rhinoscriptsyntax as rs

curve = rs.GetObject("Select curve to offset", rs.filter.curve, preselect=True)
if curve:
	point = rs.GetPoint("Pick side to offset")
	if point:
		offset = rs.OffsetCurve(curve, point, {distance})
		if offset:
			rs.Redraw()
			print("SUCCESS: Curve offset by {distance}")
		else:
			print("ERROR: Failed to offset curve")
	else:
		print("ERROR: No point selected")
else:
	print("ERROR: No curve selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _fillet_curves(args, send_fn):
	"""
	Fillet two curves
	"""
	radius = args.get("radius", 1)

	script = f"""
import rhinoscriptsyntax as rs

curve1 = rs.GetObject("Select first curve", rs.filter.curve)
curve2 = rs.GetObject("Select second curve", rs.filter.curve)

if curve1 and curve2:
	fillet = rs.FilletCurves(curve1, curve2, radius={radius})
	if fillet:
		rs.Redraw()
		print("SUCCESS: Curves filleted with radius {radius}")
	else:
		print("ERROR: Failed to fillet curves")
else:
	print("ERROR: Need two curves selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _extend_curve(args, send_fn):
	"""
	Extend selected curve
	"""
	length = args.get("length", 1)
	side = args.get("side", 1)

	script = f"""
import rhinoscriptsyntax as rs

curve = rs.GetObject("Select curve to extend", rs.filter.curve, preselect=True)
if curve:
	extended = rs.ExtendCurveLength(curve, {side}, 0, {length})
	if extended:
		rs.Redraw()
		print("SUCCESS: Curve extended by {length}")
	else:
		print("ERROR: Failed to extend curve")
else:
	print("ERROR: No curve selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]
