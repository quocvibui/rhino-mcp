"""
Document operation tools for Rhino
New, save, open, clear, units
"""

import mcp.types as types


DOCUMENT_TOOLS = [
	types.Tool(
		name="clear_document",
		description="Clear all objects from document",
		inputSchema={
			"type": "object",
			"properties": {}
		}
	),
	types.Tool(
		name="document_info",
		description="Get document information",
		inputSchema={
			"type": "object",
			"properties": {}
		}
	),
	types.Tool(
		name="set_document_units",
		description="Set document units",
		inputSchema={
			"type": "object",
			"properties": {
				"units": {
					"type": "string",
					"description": "Unit type: millimeters, centimeters, meters, inches, feet",
					"enum": ["millimeters", "centimeters", "meters", "inches", "feet"]
				}
			},
			"required": ["units"]
		}
	),
	types.Tool(
		name="save_document",
		description="Save current document",
		inputSchema={
			"type": "object",
			"properties": {
				"filepath": {"type": "string", "description": "Save file path"}
			},
			"required": ["filepath"]
		}
	),
	types.Tool(
		name="count_objects",
		description="Count objects in document by type",
		inputSchema={
			"type": "object",
			"properties": {}
		}
	)
]


def handle_document_tool(name, args, send_fn):
	"""
	Handle document tool calls
	name: Tool name
	args: Tool arguments
	send_fn: Function to send script to Rhino
	return: List of TextContent responses
	"""
	handlers = {
		"clear_document": _clear_document,
		"document_info": _document_info,
		"set_document_units": _set_document_units,
		"save_document": _save_document,
		"count_objects": _count_objects
	}

	handler = handlers.get(name)
	if not handler:
		return [types.TextContent(
			type="text",
			text=f"ERROR: Unknown document tool: {name}"
		)]

	return handler(args, send_fn)


def _clear_document(args, send_fn):
	"""
	Clear all objects
	"""
	script = """
import rhinoscriptsyntax as rs

objects = rs.AllObjects()
if objects:
	count = len(objects)
	rs.DeleteObjects(objects)
	rs.Redraw()
	print(f"SUCCESS: Cleared {count} objects from document")
else:
	print("SUCCESS: Document already empty")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _document_info(args, send_fn):
	"""
	Get document information
	"""
	script = """
import rhinoscriptsyntax as rs

objects = rs.AllObjects()
layers = rs.LayerNames()
units = rs.UnitSystemName()

print("SUCCESS: Document information:")
print(f"  Objects: {len(objects) if objects else 0}")
print(f"  Layers: {len(layers) if layers else 0}")
print(f"  Units: {units}")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _set_document_units(args, send_fn):
	"""
	Set document units
	"""
	units = args.get("units", "millimeters")

	units_map = {
		"millimeters": 2,
		"centimeters": 3,
		"meters": 4,
		"inches": 8,
		"feet": 9
	}

	unit_code = units_map.get(units, 2)

	script = f"""
import rhinoscriptsyntax as rs

rs.UnitSystem({unit_code})
print(f"SUCCESS: Document units set to {units}")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _save_document(args, send_fn):
	"""
	Save document
	"""
	filepath = args.get("filepath", "")

	script = f"""
import rhinoscriptsyntax as rs

filepath = r"{filepath}"
result = rs.Command(f"_-Save \"{{filepath}}\" _Enter", False)
if result:
	print(f"SUCCESS: Document saved to {{filepath}}")
else:
	print("ERROR: Failed to save document")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _count_objects(args, send_fn):
	"""
	Count objects by type
	"""
	script = """
import rhinoscriptsyntax as rs

objects = rs.AllObjects()
if objects:
	type_counts = {}
	type_names = {
		1: "Point",
		2: "Point Cloud",
		4: "Curve",
		8: "Surface",
		16: "Polysurface",
		32: "Mesh"
	}

	for obj in objects:
		obj_type = rs.ObjectType(obj)
		type_name = type_names.get(obj_type, f"Type {obj_type}")
		type_counts[type_name] = type_counts.get(type_name, 0) + 1

	print(f"SUCCESS: Object counts (total {len(objects)}):")
	for type_name, count in sorted(type_counts.items()):
		print(f"  {type_name}: {count}")
else:
	print("SUCCESS: No objects in document")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]
