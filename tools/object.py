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
