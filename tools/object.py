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
			params = {"name": name}
			result = send_to_rhino("set_object_name", params)
			return "Set object name to '{0}'".format(name)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def set_object_color(color_r: int, color_g: int, color_b: int) -> str:
		"""
		Set color for selected objects
		color_r, color_g, color_b: RGB color values (0-255)
		Objects must be selected in Rhino first
		"""
		try:
			params = {"color": [color_r, color_g, color_b]}
			result = send_to_rhino("set_object_color", params)
			count = result.get("count", 0)
			return "Set color for {0} objects to RGB({1}, {2}, {3})".format(
				count, color_r, color_g, color_b)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def set_object_layer(layer_name: str) -> str:
		"""
		Move selected objects to a different layer
		layer_name: Target layer name
		Objects must be selected in Rhino first
		"""
		try:
			params = {"layer": layer_name}
			result = send_to_rhino("set_object_layer", params)
			count = result.get("count", 0)
			return "Moved {0} objects to layer '{1}'".format(count, layer_name)
		except Exception as e:
			return "Error: {0}".format(str(e))
