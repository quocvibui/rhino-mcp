"""
Scene query tools for Rhino
Get information about what's in the current scene
"""

import mcp.types as types


SCENE_TOOLS = [
	types.Tool(
		name="get_scene_info",
		description="Get complete scene information including all objects, layers, and their properties",
		inputSchema={
			"type": "object",
			"properties": {}
		}
	),
	types.Tool(
		name="get_all_objects",
		description="List all objects in the scene with their types and locations",
		inputSchema={
			"type": "object",
			"properties": {}
		}
	),
	types.Tool(
		name="get_object_details",
		description="Get detailed information about selected object",
		inputSchema={
			"type": "object",
			"properties": {}
		}
	),
	types.Tool(
		name="get_bounding_box",
		description="Get bounding box of selected objects",
		inputSchema={
			"type": "object",
			"properties": {}
		}
	)
]


def handle_scene_tool(name, args, send_fn):
	"""
	Handle scene query tool calls
	name: Tool name
	args: Tool arguments
	send_fn: Function to send script to Rhino
	return: List of TextContent responses
	"""
	handlers = {
		"get_scene_info": _get_scene_info,
		"get_all_objects": _get_all_objects,
		"get_object_details": _get_object_details,
		"get_bounding_box": _get_bounding_box
	}

	handler = handlers.get(name)
	if not handler:
		return [types.TextContent(
			type="text",
			text="ERROR: Unknown scene tool: {0}".format(name)
		)]

	return handler(args, send_fn)


def _get_scene_info(args, send_fn):
	"""
	Get complete scene information
	"""
	script = """
import rhinoscriptsyntax as rs

# Get all objects
all_objects = rs.AllObjects()
obj_count = len(all_objects) if all_objects else 0

# Get layers
layers = rs.LayerNames()
layer_count = len(layers) if layers else 0

# Get units
units = rs.UnitSystemName()

# Count by type
type_counts = {}
type_names = {
	1: "Point",
	2: "Point Cloud",
	4: "Curve",
	8: "Surface",
	16: "Polysurface",
	32: "Mesh"
}

if all_objects:
	for obj in all_objects:
		obj_type = rs.ObjectType(obj)
		type_name = type_names.get(obj_type, "Other")
		type_counts[type_name] = type_counts.get(type_name, 0) + 1

print "SUCCESS: Scene Information"
print "Total Objects: " + str(obj_count)
print "Total Layers: " + str(layer_count)
print "Units: " + str(units)
print ""
print "Objects by Type:"
if type_counts:
	for obj_type, count in sorted(type_counts.items()):
		print "  " + obj_type + ": " + str(count)
else:
	print "  No objects in scene"
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _get_all_objects(args, send_fn):
	"""
	List all objects with details
	"""
	script = """
import rhinoscriptsyntax as rs

all_objects = rs.AllObjects()

if not all_objects:
	print "SUCCESS: No objects in scene"
else:
	print "SUCCESS: Objects in scene ({0} total)".format(len(all_objects))
	print ""

	type_names = {
		1: "Point",
		2: "Point Cloud",
		4: "Curve",
		8: "Surface",
		16: "Polysurface",
		32: "Mesh"
	}

	for i, obj in enumerate(all_objects[:50]):
		obj_type = rs.ObjectType(obj)
		type_name = type_names.get(obj_type, "Type " + str(obj_type))
		layer = rs.ObjectLayer(obj)

		# Get center point for location
		bbox = rs.BoundingBox(obj)
		if bbox:
			center_x = (bbox[0][0] + bbox[6][0]) / 2
			center_y = (bbox[0][1] + bbox[6][1]) / 2
			center_z = (bbox[0][2] + bbox[6][2]) / 2
			location = "({0:.1f}, {1:.1f}, {2:.1f})".format(center_x, center_y, center_z)
		else:
			location = "N/A"

		print "{0}. {1} on layer '{2}' at {3}".format(i+1, type_name, layer, location)

	if len(all_objects) > 50:
		print ""
		print "... and {0} more objects".format(len(all_objects) - 50)
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _get_object_details(args, send_fn):
	"""
	Get detailed object information
	"""
	script = """
import rhinoscriptsyntax as rs

obj = rs.GetObject("Select object for details", preselect=True)

if obj:
	obj_type = rs.ObjectType(obj)
	layer = rs.ObjectLayer(obj)
	color = rs.ObjectColor(obj)
	name = rs.ObjectName(obj)

	type_names = {
		1: "Point",
		2: "Point Cloud",
		4: "Curve",
		8: "Surface",
		16: "Polysurface",
		32: "Mesh"
	}

	print "SUCCESS: Object Details"
	print "Type: " + type_names.get(obj_type, "Type " + str(obj_type))
	print "Layer: " + layer
	print "Color: " + str(color)
	if name:
		print "Name: " + name

	# Type-specific info
	if obj_type == 4:
		length = rs.CurveLength(obj)
		degree = rs.CurveDegree(obj)
		is_closed = rs.IsCurveClosed(obj)
		print "Curve Length: {0:.2f}".format(length)
		print "Curve Degree: " + str(degree)
		print "Closed: " + str(is_closed)

	elif obj_type == 8:
		area = rs.SurfaceArea(obj)
		if area:
			print "Surface Area: {0:.2f}".format(area[0])
		is_closed = rs.IsSurfaceClosed(obj, 0) and rs.IsSurfaceClosed(obj, 1)
		print "Closed: " + str(is_closed)

	elif obj_type == 16:
		volume = rs.SurfaceVolume(obj)
		if volume:
			print "Volume: {0:.2f}".format(volume[0])
		is_closed = rs.IsPolysurfaceClosed(obj)
		print "Closed: " + str(is_closed)

	# Bounding box
	bbox = rs.BoundingBox(obj)
	if bbox:
		print ""
		print "Bounding Box:"
		print "  Min: ({0:.2f}, {1:.2f}, {2:.2f})".format(bbox[0][0], bbox[0][1], bbox[0][2])
		print "  Max: ({0:.2f}, {1:.2f}, {2:.2f})".format(bbox[6][0], bbox[6][1], bbox[6][2])
else:
	print "ERROR: No object selected"
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _get_bounding_box(args, send_fn):
	"""
	Get bounding box of selection or all objects
	"""
	script = """
import rhinoscriptsyntax as rs

objects = rs.SelectedObjects()
if not objects:
	objects = rs.AllObjects()
	scope = "all objects"
else:
	scope = "selected objects"

if objects:
	bbox = rs.BoundingBox(objects)
	if bbox:
		min_pt = bbox[0]
		max_pt = bbox[6]
		size_x = max_pt[0] - min_pt[0]
		size_y = max_pt[1] - min_pt[1]
		size_z = max_pt[2] - min_pt[2]

		print "SUCCESS: Bounding Box for " + scope
		print "Min Point: ({0:.2f}, {1:.2f}, {2:.2f})".format(min_pt[0], min_pt[1], min_pt[2])
		print "Max Point: ({0:.2f}, {1:.2f}, {2:.2f})".format(max_pt[0], max_pt[1], max_pt[2])
		print "Size: {0:.2f} x {1:.2f} x {2:.2f}".format(size_x, size_y, size_z)
		print "Center: ({0:.2f}, {1:.2f}, {2:.2f})".format(
			(min_pt[0] + max_pt[0])/2,
			(min_pt[1] + max_pt[1])/2,
			(min_pt[2] + max_pt[2])/2
		)
	else:
		print "ERROR: Could not compute bounding box"
else:
	print "ERROR: No objects in scene"
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]
