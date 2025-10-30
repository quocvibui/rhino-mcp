"""
View and camera tools for Rhino
Zoom, viewport control, camera settings
"""

import mcp.types as types


VIEW_TOOLS = [
	types.Tool(
		name="zoom_extents",
		description="Zoom to show all objects",
		inputSchema={
			"type": "object",
			"properties": {}
		}
	),
	types.Tool(
		name="zoom_selected",
		description="Zoom to selected objects",
		inputSchema={
			"type": "object",
			"properties": {}
		}
	),
	types.Tool(
		name="set_view",
		description="Set viewport to standard view",
		inputSchema={
			"type": "object",
			"properties": {
				"view": {
					"type": "string",
					"description": "View name: top, bottom, left, right, front, back, perspective",
					"enum": ["top", "bottom", "left", "right", "front", "back", "perspective"]
				}
			},
			"required": ["view"]
		}
	),
	types.Tool(
		name="set_camera",
		description="Set camera position and target",
		inputSchema={
			"type": "object",
			"properties": {
				"location": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Camera location [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				},
				"target": {
					"type": "array",
					"items": {"type": "number"},
					"description": "Camera target [x, y, z]",
					"minItems": 3,
					"maxItems": 3
				}
			},
			"required": ["location", "target"]
		}
	),
	types.Tool(
		name="set_display_mode",
		description="Set viewport display mode",
		inputSchema={
			"type": "object",
			"properties": {
				"mode": {
					"type": "string",
					"description": "Display mode: wireframe, shaded, rendered, ghosted",
					"enum": ["wireframe", "shaded", "rendered", "ghosted"]
				}
			},
			"required": ["mode"]
		}
	)
]


def handle_view_tool(name, args, send_fn):
	"""
	Handle view tool calls
	name: Tool name
	args: Tool arguments
	send_fn: Function to send script to Rhino
	return: List of TextContent responses
	"""
	handlers = {
		"zoom_extents": _zoom_extents,
		"zoom_selected": _zoom_selected,
		"set_view": _set_view,
		"set_camera": _set_camera,
		"set_display_mode": _set_display_mode
	}

	handler = handlers.get(name)
	if not handler:
		return [types.TextContent(
			type="text",
			text=f"ERROR: Unknown view tool: {name}"
		)]

	return handler(args, send_fn)


def _zoom_extents(args, send_fn):
	"""
	Zoom to show all objects
	"""
	script = """
import rhinoscriptsyntax as rs

rs.ZoomExtents()
print("SUCCESS: Zoomed to extents")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _zoom_selected(args, send_fn):
	"""
	Zoom to selected objects
	"""
	script = """
import rhinoscriptsyntax as rs

objects = rs.SelectedObjects()
if objects:
	rs.ZoomSelected()
	print(f"SUCCESS: Zoomed to {len(objects)} selected objects")
else:
	print("ERROR: No objects selected")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _set_view(args, send_fn):
	"""
	Set standard view
	"""
	view = args.get("view", "perspective")

	script = f"""
import rhinoscriptsyntax as rs

view_name = "{view}"
view_map = {{
	"top": rs.ViewCPlaneTop,
	"bottom": rs.ViewCPlaneBottom,
	"left": rs.ViewCPlaneLeft,
	"right": rs.ViewCPlaneRight,
	"front": rs.ViewCPlaneFront,
	"back": rs.ViewCPlaneBack
}}

if view_name in view_map:
	view_map[view_name]()
	print(f"SUCCESS: View set to {{view_name}}")
elif view_name == "perspective":
	rs.Command("_SetView _Perspective")
	print("SUCCESS: View set to perspective")
else:
	print(f"ERROR: Unknown view '{{view_name}}'")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _set_camera(args, send_fn):
	"""
	Set camera position and target
	"""
	location = args.get("location", [10, 10, 10])
	target = args.get("target", [0, 0, 0])

	script = f"""
import rhinoscriptsyntax as rs

view = rs.CurrentView()
if view:
	location = {tuple(location)}
	target = {tuple(target)}
	rs.ViewCameraTarget(view, location, target)
	print(f"SUCCESS: Camera set to location {tuple(location)}, target {tuple(target)}")
else:
	print("ERROR: No active view")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]


def _set_display_mode(args, send_fn):
	"""
	Set display mode
	"""
	mode = args.get("mode", "shaded")

	mode_map = {
		"wireframe": "Wireframe",
		"shaded": "Shaded",
		"rendered": "Rendered",
		"ghosted": "Ghosted"
	}

	rhino_mode = mode_map.get(mode, "Shaded")

	script = f"""
import rhinoscriptsyntax as rs

view = rs.CurrentView()
if view:
	rs.ViewDisplayMode(view, "{rhino_mode}")
	print(f"SUCCESS: Display mode set to {rhino_mode}")
else:
	print("ERROR: No active view")
"""

	response = send_fn(script)
	return [types.TextContent(type="text", text=response)]
