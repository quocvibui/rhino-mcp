"""
3D solid primitives for Rhino
Box, sphere, cylinder, cone, torus
"""

import mcp.types as types


SOLIDS_TOOLS = [
	types.Tool(
		name="add_box",
		description="Add a box solid to Rhino",
		inputSchema={
			"type": "object",
			"properties": {
				"width": {"type": "number", "description": "Box width (X)", "default": 10},
				"depth": {"type": "number", "description": "Box depth (Y)", "default": 10},
				"height": {"type": "number", "description": "Box height (Z)", "default": 10},
				"x": {"type": "number", "description": "X position", "default": 0},
				"y": {"type": "number", "description": "Y position", "default": 0},
				"z": {"type": "number", "description": "Z position", "default": 0}
			}
		}
	),
	types.Tool(
		name="add_sphere",
		description="Add a sphere to Rhino",
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
				"radius": {"type": "number", "description": "Sphere radius"}
			},
			"required": ["center", "radius"]
		}
	),
	types.Tool(
		name="add_cylinder",
		description="Add a cylinder to Rhino",
		inputSchema={
			"type": "object",
			"properties": {
				"base": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Base center point [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				},
				"height": {"type": "number", "description": "Cylinder height"},
				"radius": {"type": "number", "description": "Cylinder radius"}
			},
			"required": ["base", "height", "radius"]
		}
	),
	types.Tool(
		name="add_cone",
		description="Add a cone to Rhino",
		inputSchema={
			"type": "object",
			"properties": {
				"base": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Base center point [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				},
				"height": {"type": "number", "description": "Cone height"},
				"radius": {"type": "number", "description": "Base radius"}
			},
			"required": ["base", "height", "radius"]
		}
	),
	types.Tool(
		name="add_torus",
		description="Add a torus to Rhino",
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
				"major_radius": {"type": "number", "description": "Major radius"},
				"minor_radius": {"type": "number", "description": "Minor radius"}
			},
			"required": ["center", "major_radius", "minor_radius"]
		}
	)
]


def handle_solids_tool(name, args, send_fn):
	"""
	Handle solids tool calls
	name: Tool name
	args: Tool arguments
	send_fn: Function to send script to Rhino
	return: List of TextContent responses
	"""
	handlers = {
		"add_box": _add_box,
		"add_sphere": _add_sphere,
		"add_cylinder": _add_cylinder,
		"add_cone": _add_cone,
		"add_torus": _add_torus
	}

	handler = handlers.get(name)
	if not handler:
		return [types.TextContent(
			type="text",
			text=f"ERROR: Unknown solids tool: {name}"
		)]

	return handler(args, send_fn)


def _add_box(args, send_fn):
	"""
	Add box to Rhino
	"""
	width = args.get("width", 10)
	depth = args.get("depth", 10)
	height = args.get("height", 10)
	x = args.get("x", 0)
	y = args.get("y", 0)
	z = args.get("z", 0)

	script = f"""
import rhinoscriptsyntax as rs

p0 = ({x}, {y}, {z})
p1 = ({x + width}, {y}, {z})
p2 = ({x + width}, {y + depth}, {z})
p3 = ({x}, {y + depth}, {z})
p4 = ({x}, {y}, {z + height})
p5 = ({x + width}, {y}, {z + height})
p6 = ({x + width}, {y + depth}, {z + height})
p7 = ({x}, {y + depth}, {z + height})

box = rs.AddBox([p0, p1, p2, p3, p4, p5, p6, p7])
if box:
	rs.Redraw()
	print("SUCCESS: Box {width}x{depth}x{height} added at ({x}, {y}, {z})")
else:
	print("ERROR: Failed to add box")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _add_sphere(args, send_fn):
	"""
	Add sphere to Rhino
	"""
	center = args.get("center", [0, 0, 0])
	radius = args.get("radius", 1)

	script = f"""
import rhinoscriptsyntax as rs
sphere = rs.AddSphere({tuple(center)}, {radius})
if sphere:
	rs.Redraw()
	print("SUCCESS: Sphere with radius {radius} added at {tuple(center)}")
else:
	print("ERROR: Failed to add sphere")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _add_cylinder(args, send_fn):
	"""
	Add cylinder to Rhino
	"""
	base = args.get("base", [0, 0, 0])
	height = args.get("height", 10)
	radius = args.get("radius", 5)

	script = f"""
import rhinoscriptsyntax as rs
base_pt = {tuple(base)}
height_vec = (0, 0, {height})
top_pt = (base_pt[0], base_pt[1], base_pt[2] + {height})

plane = rs.PlaneFromNormal(base_pt, (0, 0, 1))
circle = rs.AddCircle(plane, {radius})
cylinder = rs.ExtrudeCurveStraight(circle, base_pt, top_pt)

if cylinder:
	rs.DeleteObject(circle)
	rs.Redraw()
	print("SUCCESS: Cylinder with radius {radius} and height {height} added")
else:
	print("ERROR: Failed to add cylinder")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _add_cone(args, send_fn):
	"""
	Add cone to Rhino
	"""
	base = args.get("base", [0, 0, 0])
	height = args.get("height", 10)
	radius = args.get("radius", 5)

	script = f"""
import rhinoscriptsyntax as rs
base_pt = {tuple(base)}
apex = (base_pt[0], base_pt[1], base_pt[2] + {height})

plane = rs.PlaneFromNormal(base_pt, (0, 0, 1))
cone = rs.AddCone(plane, {height}, {radius})

if cone:
	rs.Redraw()
	print("SUCCESS: Cone with radius {radius} and height {height} added")
else:
	print("ERROR: Failed to add cone")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _add_torus(args, send_fn):
	"""
	Add torus to Rhino
	"""
	center = args.get("center", [0, 0, 0])
	major_radius = args.get("major_radius", 5)
	minor_radius = args.get("minor_radius", 1)

	script = f"""
import rhinoscriptsyntax as rs
plane = rs.PlaneFromNormal({tuple(center)}, (0, 0, 1))
torus = rs.AddTorus(plane, {major_radius}, {minor_radius})

if torus:
	rs.Redraw()
	print("SUCCESS: Torus with radii {major_radius}/{minor_radius} added")
else:
	print("ERROR: Failed to add torus")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]
