"""
MCP tools for view operations
"""

import json
from .utils import send_to_rhino


def register_tools(mcp):
	"""Register all view tools with the MCP server"""

	@mcp.tool()
	def set_view_camera(camera_x: float, camera_y: float, camera_z: float,
						target_x: float, target_y: float, target_z: float) -> str:
		"""
		Set the camera position and target for the active view
		camera_x, camera_y, camera_z: Camera position
		target_x, target_y, target_z: Camera target point
		"""
		try:
			params = {
				"camera": [camera_x, camera_y, camera_z],
				"target": [target_x, target_y, target_z]
			}
			send_to_rhino("set_view_camera", params)
			return f"Set camera to ({camera_x}, {camera_y}, {camera_z}) targeting ({target_x}, {target_y}, {target_z})"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def zoom_extents() -> str:
		"""
		Zoom the active view to show all objects
		"""
		try:
			send_to_rhino("zoom_extents")
			return "Zoomed to extents"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def zoom_selected() -> str:
		"""
		Zoom the active view to show selected objects
		Objects must be selected in Rhino first
		"""
		try:
			send_to_rhino("zoom_selected")
			return "Zoomed to selected objects"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def get_view_info() -> str:
		"""
		Get information about the current view including camera, target, and display mode
		"""
		try:
			result = send_to_rhino("get_view_info")
			return json.dumps(result, indent=2)
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def set_display_mode(mode: str) -> str:
		"""
		Set the display mode for the active viewport
		mode: Display mode name ('Wireframe', 'Shaded', 'Rendered', 'Ghosted', 'XRay', 'Technical', 'Artistic', 'Pen')
		"""
		try:
			send_to_rhino("set_display_mode", {"mode": mode})
			return f"Set display mode to '{mode}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def add_named_view(name: str) -> str:
		"""
		Save the current view as a named view
		name: Name for the view
		"""
		try:
			send_to_rhino("add_named_view", {"name": name})
			return f"Saved named view '{name}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def restore_named_view(name: str) -> str:
		"""
		Restore a previously saved named view
		name: Name of the view to restore
		"""
		try:
			send_to_rhino("restore_named_view", {"name": name})
			return f"Restored named view '{name}'"
		except Exception as e:
			return f"Error: {e}"
