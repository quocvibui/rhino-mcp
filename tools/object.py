"""
MCP tools for object properties
"""

from .utils import send_to_rhino


def register_tools(mcp):
	"""Register all object property tools with the MCP server"""

	@mcp.tool()
	def set_object_name(name: str) -> str:
		"""
		Set name for selected object
		name: Object name to set
		One object must be selected in Rhino first
		"""
		try:
			send_to_rhino("set_object_name", {"name": name})
			return f"Set object name to '{name}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def set_object_color(color_r: int, color_g: int, color_b: int) -> str:
		"""
		Set color for selected objects
		color_r, color_g, color_b: RGB color values (0-255)
		Objects must be selected in Rhino first
		"""
		try:
			result = send_to_rhino("set_object_color", {"color": [color_r, color_g, color_b]})
			count = result.get("count", 0)
			return f"Set color for {count} objects to RGB({color_r}, {color_g}, {color_b})"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def set_object_layer(layer_name: str) -> str:
		"""
		Move selected objects to a different layer
		layer_name: Target layer name
		Objects must be selected in Rhino first
		"""
		try:
			result = send_to_rhino("set_object_layer", {"layer": layer_name})
			count = result.get("count", 0)
			return f"Moved {count} objects to layer '{layer_name}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def hide_objects() -> str:
		"""
		Hide the currently selected objects
		Objects must be selected in Rhino first
		"""
		try:
			result = send_to_rhino("hide_objects")
			count = result.get("count", 0)
			return f"Hidden {count} objects"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def show_objects(object_ids: str = "") -> str:
		"""
		Show hidden objects. If no IDs provided, shows all hidden objects.
		object_ids: Comma-separated object IDs to show (optional)
		"""
		try:
			params = {}
			if object_ids:
				params["object_ids"] = [s.strip() for s in object_ids.split(",")]
			result = send_to_rhino("show_objects", params)
			count = result.get("count", 0)
			return f"Shown {count} objects"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def lock_objects() -> str:
		"""
		Lock the currently selected objects (prevents editing)
		Objects must be selected in Rhino first
		"""
		try:
			result = send_to_rhino("lock_objects")
			count = result.get("count", 0)
			return f"Locked {count} objects"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def unlock_objects(object_ids: str = "") -> str:
		"""
		Unlock locked objects. If no IDs provided, unlocks all locked objects.
		object_ids: Comma-separated object IDs to unlock (optional)
		"""
		try:
			params = {}
			if object_ids:
				params["object_ids"] = [s.strip() for s in object_ids.split(",")]
			result = send_to_rhino("unlock_objects", params)
			count = result.get("count", 0)
			return f"Unlocked {count} objects"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def is_object_solid(object_id: str) -> str:
		"""
		Check if an object is a solid (closed polysurface or closed mesh)
		object_id: ID of the object to check
		"""
		try:
			result = send_to_rhino("is_object_solid", {"object_id": object_id})
			solid = result.get("solid", False)
			return f"Object is {'solid' if solid else 'not solid'}"
		except Exception as e:
			return f"Error: {e}"
