"""
Layer management tools for Rhino
Create, delete, set current, set color, visibility
"""

import mcp.types as types


LAYERS_TOOLS = [
	types.Tool(
		name="add_layer",
		description="Add a new layer to document",
		inputSchema={
			"type": "object",
			"properties": {
				"name": {"type": "string", "description": "Layer name"},
				"color": {
					"type": "array",
					"items": {"type": "integer", "minimum": 0, "maximum": 255},
					"description": "RGB color [r, g, b]",
					"minItems": 3,
					"maxItems": 3
				}
			},
			"required": ["name"]
		}
	),
	types.Tool(
		name="delete_layer",
		description="Delete a layer from document",
		inputSchema={
			"type": "object",
			"properties": {
				"name": {"type": "string", "description": "Layer name to delete"}
			},
			"required": ["name"]
		}
	),
	types.Tool(
		name="set_current_layer",
		description="Set the current active layer",
		inputSchema={
			"type": "object",
			"properties": {
				"name": {"type": "string", "description": "Layer name"}
			},
			"required": ["name"]
		}
	),
	types.Tool(
		name="set_layer_color",
		description="Set layer color",
		inputSchema={
			"type": "object",
			"properties": {
				"name": {"type": "string", "description": "Layer name"},
				"color": {
					"type": "array",
					"items": {"type": "integer", "minimum": 0, "maximum": 255},
					"description": "RGB color [r, g, b]",
					"minItems": 3,
					"maxItems": 3
				}
			},
			"required": ["name", "color"]
		}
	),
	types.Tool(
		name="layer_visible",
		description="Set layer visibility on or off",
		inputSchema={
			"type": "object",
			"properties": {
				"name": {"type": "string", "description": "Layer name"},
				"visible": {"type": "boolean", "description": "Visibility state"}
			},
			"required": ["name", "visible"]
		}
	),
	types.Tool(
		name="list_layers",
		description="List all layers in document",
		inputSchema={
			"type": "object",
			"properties": {}
		}
	)
]


def handle_layers_tool(name, args, send_fn):
	"""
	Handle layers tool calls
	name: Tool name
	args: Tool arguments
	send_fn: Function to send script to Rhino
	return: List of TextContent responses
	"""
	handlers = {
		"add_layer": _add_layer,
		"delete_layer": _delete_layer,
		"set_current_layer": _set_current_layer,
		"set_layer_color": _set_layer_color,
		"layer_visible": _layer_visible,
		"list_layers": _list_layers
	}

	handler = handlers.get(name)
	if not handler:
		return [types.TextContent(
			type="text",
			text=f"ERROR: Unknown layers tool: {name}"
		)]

	return handler(args, send_fn)


def _add_layer(args, send_fn):
	"""
	Add new layer
	"""
	name = args.get("name", "NewLayer")
	color = args.get("color", None)

	color_str = f", color={tuple(color)}" if color else ""

	script = f"""
import rhinoscriptsyntax as rs

layer_name = "{name}"
if not rs.IsLayer(layer_name):
	layer = rs.AddLayer(layer_name{color_str})
	if layer:
		print(f"SUCCESS: Layer '{{layer_name}}' created")
	else:
		print("ERROR: Failed to create layer")
else:
	print(f"ERROR: Layer '{{layer_name}}' already exists")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _delete_layer(args, send_fn):
	"""
	Delete layer
	"""
	name = args.get("name", "")

	script = f"""
import rhinoscriptsyntax as rs

layer_name = "{name}"
if rs.IsLayer(layer_name):
	result = rs.DeleteLayer(layer_name)
	if result:
		print(f"SUCCESS: Layer '{{layer_name}}' deleted")
	else:
		print("ERROR: Failed to delete layer - may contain objects")
else:
	print(f"ERROR: Layer '{{layer_name}}' does not exist")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _set_current_layer(args, send_fn):
	"""
	Set current layer
	"""
	name = args.get("name", "")

	script = f"""
import rhinoscriptsyntax as rs

layer_name = "{name}"
if rs.IsLayer(layer_name):
	rs.CurrentLayer(layer_name)
	print(f"SUCCESS: Current layer set to '{{layer_name}}'")
else:
	print(f"ERROR: Layer '{{layer_name}}' does not exist")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _set_layer_color(args, send_fn):
	"""
	Set layer color
	"""
	name = args.get("name", "")
	color = args.get("color", [0, 0, 0])

	script = f"""
import rhinoscriptsyntax as rs

layer_name = "{name}"
if rs.IsLayer(layer_name):
	rs.LayerColor(layer_name, {tuple(color)})
	rs.Redraw()
	print(f"SUCCESS: Layer '{{layer_name}}' color set")
else:
	print(f"ERROR: Layer '{{layer_name}}' does not exist")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _layer_visible(args, send_fn):
	"""
	Set layer visibility
	"""
	name = args.get("name", "")
	visible = args.get("visible", True)

	script = f"""
import rhinoscriptsyntax as rs

layer_name = "{name}"
if rs.IsLayer(layer_name):
	rs.LayerVisible(layer_name, {visible})
	rs.Redraw()
	state = "visible" if {visible} else "hidden"
	print(f"SUCCESS: Layer '{{layer_name}}' set to {{state}}")
else:
	print(f"ERROR: Layer '{{layer_name}}' does not exist")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _list_layers(args, send_fn):
	"""
	List all layers
	"""
	script = """
import rhinoscriptsyntax as rs

layers = rs.LayerNames()
if layers:
	current = rs.CurrentLayer()
	print(f"SUCCESS: Found {len(layers)} layers")
	print(f"Current layer: {current}")
	print("Layers:")
	for layer in sorted(layers):
		visible = "visible" if rs.LayerVisible(layer) else "hidden"
		marker = "*" if layer == current else " "
		print(f"{marker} {layer} ({visible})")
else:
	print("ERROR: No layers found")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]
