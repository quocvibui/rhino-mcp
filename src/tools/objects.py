"""
Object management tools for Rhino
Select, delete, move, copy, rotate, scale, mirror
"""

import mcp.types as types


OBJECTS_TOOLS = [
	types.Tool(
		name="select_all",
		description="Select all objects in document",
		inputSchema={
			"type": "object",
			"properties": {}
		}
	),
	types.Tool(
		name="select_by_layer",
		description="Select all objects on a layer",
		inputSchema={
			"type": "object",
			"properties": {
				"layer": {"type": "string", "description": "Layer name"}
			},
			"required": ["layer"]
		}
	),
	types.Tool(
		name="delete_objects",
		description="Delete selected objects",
		inputSchema={
			"type": "object",
			"properties": {}
		}
	),
	types.Tool(
		name="move_objects",
		description="Move selected objects by vector",
		inputSchema={
			"type": "object",
			"properties": {
				"vector": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Movement vector [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				}
			},
			"required": ["vector"]
		}
	),
	types.Tool(
		name="copy_objects",
		description="Copy selected objects by vector",
		inputSchema={
			"type": "object",
			"properties": {
				"vector": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Copy vector [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				}
			},
			"required": ["vector"]
		}
	),
	types.Tool(
		name="rotate_objects",
		description="Rotate selected objects around axis",
		inputSchema={
			"type": "object",
			"properties": {
				"center": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Rotation center [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				},
				"angle": {"type": "number", "description": "Rotation angle in degrees"}
			},
			"required": ["center", "angle"]
		}
	),
	types.Tool(
		name="scale_objects",
		description="Scale selected objects uniformly",
		inputSchema={
			"type": "object",
			"properties": {
				"origin": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Scale origin [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				},
				"factor": {"type": "number", "description": "Scale factor"}
			},
			"required": ["origin", "factor"]
		}
	),
	types.Tool(
		name="mirror_objects",
		description="Mirror selected objects across plane",
		inputSchema={
			"type": "object",
			"properties": {
				"plane_origin": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Mirror plane origin [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				},
				"plane_normal": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Mirror plane normal [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				}
			},
			"required": ["plane_origin", "plane_normal"]
		}
	),
	types.Tool(
		name="object_info",
		description="Get information about selected object",
		inputSchema={
			"type": "object",
			"properties": {}
		}
	)
]


def handle_objects_tool(name, args, send_fn):
	"""
	Handle objects tool calls
	name: Tool name
	args: Tool arguments
	send_fn: Function to send script to Rhino
	return: List of TextContent responses
	"""
	handlers = {
		"select_all": _select_all,
		"select_by_layer": _select_by_layer,
		"delete_objects": _delete_objects,
		"move_objects": _move_objects,
		"copy_objects": _copy_objects,
		"rotate_objects": _rotate_objects,
		"scale_objects": _scale_objects,
		"mirror_objects": _mirror_objects,
		"object_info": _object_info
	}

	handler = handlers.get(name)
	if not handler:
		return [types.TextContent(
			type="text",
			text=f"ERROR: Unknown objects tool: {name}"
		)]

	return handler(args, send_fn)


def _select_all(args, send_fn):
	"""
	Select all objects
	"""
	script = """
import rhinoscriptsyntax as rs

objects = rs.AllObjects()
if objects:
	rs.SelectObjects(objects)
	print(f"SUCCESS: Selected {len(objects)} objects")
else:
	print("ERROR: No objects in document")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _select_by_layer(args, send_fn):
	"""
	Select objects by layer
	"""
	layer = args.get("layer", "")

	script = f"""
import rhinoscriptsyntax as rs

layer_name = "{layer}"
if rs.IsLayer(layer_name):
	objects = rs.ObjectsByLayer(layer_name)
	if objects:
		rs.SelectObjects(objects)
		print(f"SUCCESS: Selected {{len(objects)}} objects on layer '{{layer_name}}'")
	else:
		print(f"ERROR: No objects on layer '{{layer_name}}'")
else:
	print(f"ERROR: Layer '{{layer_name}}' does not exist")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _delete_objects(args, send_fn):
	"""
	Delete selected objects
	"""
	script = """
import rhinoscriptsyntax as rs

objects = rs.SelectedObjects()
if objects:
	count = len(objects)
	rs.DeleteObjects(objects)
	rs.Redraw()
	print(f"SUCCESS: Deleted {count} objects")
else:
	print("ERROR: No objects selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _move_objects(args, send_fn):
	"""
	Move selected objects
	"""
	vector = args.get("vector", [0, 0, 0])

	script = f"""
import rhinoscriptsyntax as rs

objects = rs.SelectedObjects()
if objects:
	translation = {tuple(vector)}
	for obj in objects:
		rs.MoveObject(obj, translation)
	rs.Redraw()
	print(f"SUCCESS: Moved {{len(objects)}} objects by {tuple(vector)}")
else:
	print("ERROR: No objects selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _copy_objects(args, send_fn):
	"""
	Copy selected objects
	"""
	vector = args.get("vector", [0, 0, 0])

	script = f"""
import rhinoscriptsyntax as rs

objects = rs.SelectedObjects()
if objects:
	translation = {tuple(vector)}
	for obj in objects:
		rs.CopyObject(obj, translation)
	rs.Redraw()
	print(f"SUCCESS: Copied {{len(objects)}} objects by {tuple(vector)}")
else:
	print("ERROR: No objects selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _rotate_objects(args, send_fn):
	"""
	Rotate selected objects
	"""
	center = args.get("center", [0, 0, 0])
	angle = args.get("angle", 90)

	script = f"""
import rhinoscriptsyntax as rs

objects = rs.SelectedObjects()
if objects:
	center = {tuple(center)}
	axis = (0, 0, 1)
	for obj in objects:
		rs.RotateObject(obj, center, {angle}, axis)
	rs.Redraw()
	print(f"SUCCESS: Rotated {{len(objects)}} objects by {angle} degrees")
else:
	print("ERROR: No objects selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _scale_objects(args, send_fn):
	"""
	Scale selected objects
	"""
	origin = args.get("origin", [0, 0, 0])
	factor = args.get("factor", 1)

	script = f"""
import rhinoscriptsyntax as rs

objects = rs.SelectedObjects()
if objects:
	origin = {tuple(origin)}
	scale = [{factor}, {factor}, {factor}]
	for obj in objects:
		rs.ScaleObject(obj, origin, scale)
	rs.Redraw()
	print(f"SUCCESS: Scaled {{len(objects)}} objects by factor {factor}")
else:
	print("ERROR: No objects selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _mirror_objects(args, send_fn):
	"""
	Mirror selected objects
	"""
	plane_origin = args.get("plane_origin", [0, 0, 0])
	plane_normal = args.get("plane_normal", [1, 0, 0])

	script = f"""
import rhinoscriptsyntax as rs

objects = rs.SelectedObjects()
if objects:
	origin = {tuple(plane_origin)}
	normal = {tuple(plane_normal)}
	for obj in objects:
		rs.MirrorObject(obj, origin, normal)
	rs.Redraw()
	print(f"SUCCESS: Mirrored {{len(objects)}} objects")
else:
	print("ERROR: No objects selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _object_info(args, send_fn):
	"""
	Get object information
	"""
	script = """
import rhinoscriptsyntax as rs

obj = rs.GetObject("Select object for info", preselect=True)
if obj:
	obj_type = rs.ObjectType(obj)
	layer = rs.ObjectLayer(obj)
	color = rs.ObjectColor(obj)

	print(f"SUCCESS: Object information:")
	print(f"  Type: {obj_type}")
	print(f"  Layer: {layer}")
	print(f"  Color: {color}")

	if obj_type == 4:
		length = rs.CurveLength(obj)
		print(f"  Curve length: {length:.2f}")
	elif obj_type == 8:
		area = rs.SurfaceArea(obj)
		if area:
			print(f"  Surface area: {area[0]:.2f}")
else:
	print("ERROR: No object selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]
