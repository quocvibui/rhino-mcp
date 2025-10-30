"""
Basic geometry tools for Rhino
Points, lines, circles, arcs, polylines, polygons
"""

import mcp.types as types


GEOMETRY_TOOLS = [
	types.Tool(
		name="add_point",
		description="Add a point to Rhino document",
		inputSchema={
			"type": "object",
			"properties": {
				"x": {"type": "number", "description": "X coordinate"},
				"y": {"type": "number", "description": "Y coordinate"},
				"z": {"type": "number", "description": "Z coordinate", "default": 0}
			},
			"required": ["x", "y"]
		}
	),
	types.Tool(
		name="add_line",
		description="Add a line between two points",
		inputSchema={
			"type": "object",
			"properties": {
				"start": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Start point [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				},
				"end": {
					"type": "array",
					"items": {"type": "number"},
					"description": "End point [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				}
			},
			"required": ["start", "end"]
		}
	),
	types.Tool(
		name="add_circle",
		description="Add a circle to Rhino document",
		inputSchema={
			"type": "object",
			"properties": {
				"center": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Center point [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				},
				"radius": {"type": "number", "description": "Circle radius"}
			},
			"required": ["center", "radius"]
		}
	),
	types.Tool(
		name="add_arc",
		description="Add a circular arc through three points",
		inputSchema={
			"type": "object",
			"properties": {
				"start": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Start point [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				},
				"end": {
					"type": "array",
					"items": {"type": "number"},
					"description": "End point [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				},
				"point_on_arc": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Point on arc [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				}
			},
			"required": ["start", "end", "point_on_arc"]
		}
	),
	types.Tool(
		name="add_polyline",
		description="Add a polyline through multiple points",
		inputSchema={
			"type": "object",
			"properties": {
				"points": {
					"type": "array",
					"items": {
						"type": "array",
						"items": {"type": "number"},
						"minItems": 3,
						"maxItems": 3
					},
					"description": "List of points [[x1,y1,z1], [x2,y2,z2], ...]",
					"minItems": 2
				}
			},
			"required": ["points"]
		}
	),
	types.Tool(
		name="add_polygon",
		description="Add a regular polygon",
		inputSchema={
			"type": "object",
			"properties": {
				"center": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Center point [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				},
				"radius": {"type": "number", "description": "Polygon radius"},
				"sides": {"type": "integer", "description": "Number of sides", "minimum": 3}
			},
			"required": ["center", "radius", "sides"]
		}
	),
	types.Tool(
		name="add_ellipse",
		description="Add an ellipse",
		inputSchema={
			"type": "object",
			"properties": {
				"center": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Center point [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				},
				"radius_x": {"type": "number", "description": "X radius"},
				"radius_y": {"type": "number", "description": "Y radius"}
			},
			"required": ["center", "radius_x", "radius_y"]
		}
	)
]


def handle_geometry_tool(name, args, send_fn):
	"""
	Handle geometry tool calls
	name: Tool name
	args: Tool arguments
	send_fn: Function to send script to Rhino
	return: List of TextContent responses
	"""
	handlers = {
		"add_point": _add_point,
		"add_line": _add_line,
		"add_circle": _add_circle,
		"add_arc": _add_arc,
		"add_polyline": _add_polyline,
		"add_polygon": _add_polygon,
		"add_ellipse": _add_ellipse
	}

	handler = handlers.get(name)
	if not handler:
		return [types.TextContent(
			type="text",
			text=f"ERROR: Unknown geometry tool: {name}"
		)]

	return handler(args, send_fn)


def _add_point(args, send_fn):
	"""
	Add point to Rhino
	"""
	x = args.get("x", 0)
	y = args.get("y", 0)
	z = args.get("z", 0)

	script = f"""
import rhinoscriptsyntax as rs
pt = rs.AddPoint({x}, {y}, {z})
if pt:
	rs.Redraw()
	print("SUCCESS: Point added at ({x}, {y}, {z})")
else:
	print("ERROR: Failed to add point")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _add_line(args, send_fn):
	"""
	Add line to Rhino
	"""
	start = args.get("start", [0, 0, 0])
	end = args.get("end", [1, 1, 1])

	script = f"""
import rhinoscriptsyntax as rs
line = rs.AddLine({tuple(start)}, {tuple(end)})
if line:
	rs.Redraw()
	print("SUCCESS: Line added from {tuple(start)} to {tuple(end)}")
else:
	print("ERROR: Failed to add line")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _add_circle(args, send_fn):
	"""
	Add circle to Rhino
	"""
	center = args.get("center", [0, 0, 0])
	radius = args.get("radius", 1)

	script = f"""
import rhinoscriptsyntax as rs
circle = rs.AddCircle({tuple(center)}, {radius})
if circle:
	rs.Redraw()
	print("SUCCESS: Circle added with radius {radius} at {tuple(center)}")
else:
	print("ERROR: Failed to add circle")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _add_arc(args, send_fn):
	"""
	Add arc to Rhino
	"""
	start = args.get("start", [0, 0, 0])
	end = args.get("end", [1, 0, 0])
	point_on_arc = args.get("point_on_arc", [0.5, 0.5, 0])

	script = f"""
import rhinoscriptsyntax as rs
arc = rs.AddArc3Pt({tuple(start)}, {tuple(point_on_arc)}, {tuple(end)})
if arc:
	rs.Redraw()
	print("SUCCESS: Arc added through 3 points")
else:
	print("ERROR: Failed to add arc")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _add_polyline(args, send_fn):
	"""
	Add polyline to Rhino
	"""
	points = args.get("points", [[0, 0, 0], [1, 1, 1]])

	points_str = str([tuple(pt) for pt in points])

	script = f"""
import rhinoscriptsyntax as rs
polyline = rs.AddPolyline({points_str})
if polyline:
	rs.Redraw()
	print("SUCCESS: Polyline added with {len(points)} points")
else:
	print("ERROR: Failed to add polyline")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _add_polygon(args, send_fn):
	"""
	Add polygon to Rhino
	"""
	center = args.get("center", [0, 0, 0])
	radius = args.get("radius", 1)
	sides = args.get("sides", 6)

	script = f"""
import rhinoscriptsyntax as rs
import math

center = {tuple(center)}
radius = {radius}
sides = {sides}

points = []
for i in range(sides):
	angle = (2 * math.pi * i) / sides
	x = center[0] + radius * math.cos(angle)
	y = center[1] + radius * math.sin(angle)
	z = center[2]
	points.append((x, y, z))

points.append(points[0])

polygon = rs.AddPolyline(points)
if polygon:
	rs.Redraw()
	print(f"SUCCESS: Polygon with {{sides}} sides added")
else:
	print("ERROR: Failed to add polygon")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _add_ellipse(args, send_fn):
	"""
	Add ellipse to Rhino
	"""
	center = args.get("center", [0, 0, 0])
	radius_x = args.get("radius_x", 1)
	radius_y = args.get("radius_y", 0.5)

	script = f"""
import rhinoscriptsyntax as rs
plane = rs.PlaneFromNormal({tuple(center)}, (0, 0, 1))
ellipse = rs.AddEllipse(plane, {radius_x}, {radius_y})
if ellipse:
	rs.Redraw()
	print("SUCCESS: Ellipse added with radii {radius_x} x {radius_y}")
else:
	print("ERROR: Failed to add ellipse")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]
