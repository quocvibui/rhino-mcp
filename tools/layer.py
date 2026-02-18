"""
MCP tools for layer management
"""

import json
from .utils import send_to_rhino


def register_tools(mcp):
	"""Register all layer management tools with the MCP server"""

	@mcp.tool()
	def create_layer(name: str, color_r: int = 0, color_g: int = 0, color_b: int = 0) -> str:
		"""
		Create a new layer in Rhino
		name: Layer name
		color_r, color_g, color_b: RGB color values (0-255), default black
		"""
		try:
			params = {
				"name": name,
				"color": [color_r, color_g, color_b]
			}
			send_to_rhino("create_layer", params)
			return f"Created layer '{name}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def delete_layer(name: str) -> str:
		"""
		Delete a layer from Rhino
		name: Layer name to delete
		Layer must be empty (no objects on it)
		"""
		try:
			send_to_rhino("delete_layer", {"name": name})
			return f"Deleted layer '{name}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def set_current_layer(name: str) -> str:
		"""
		Set the current active layer in Rhino
		name: Layer name to make current
		New objects will be created on this layer
		"""
		try:
			send_to_rhino("set_current_layer", {"name": name})
			return f"Set current layer to '{name}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def set_layer_color(name: str, color_r: int, color_g: int, color_b: int) -> str:
		"""
		Set the color of a layer
		name: Layer name
		color_r, color_g, color_b: RGB color values (0-255)
		"""
		try:
			params = {
				"name": name,
				"color": [color_r, color_g, color_b]
			}
			send_to_rhino("set_layer_color", params)
			return f"Set layer '{name}' color to RGB({color_r}, {color_g}, {color_b})"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def set_layer_visibility(name: str, visible: bool) -> str:
		"""
		Set layer visibility (show/hide)
		name: Layer name
		visible: True to show, False to hide
		"""
		try:
			params = {
				"name": name,
				"visible": visible
			}
			send_to_rhino("set_layer_visibility", params)
			status = "visible" if visible else "hidden"
			return f"Set layer '{name}' to {status}"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def list_layers() -> str:
		"""
		Get list of all layers in the document
		Returns layer names and their properties
		"""
		try:
			result = send_to_rhino("list_layers")
			return json.dumps(result, indent=2)
		except Exception as e:
			return f"Error: {e}"
