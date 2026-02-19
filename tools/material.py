"""
MCP tools for material operations
"""

from .utils import send_to_rhino


def register_tools(mcp):
	"""Register all material tools with the MCP server"""

	@mcp.tool()
	def add_material_to_object(object_id: str, color_r: int = 255, color_g: int = 255, color_b: int = 255) -> str:
		"""
		Add a material to an object and set its color
		object_id: ID of the object
		color_r, color_g, color_b: Material color RGB values (0-255)
		"""
		try:
			params = {"object_id": object_id, "color": [color_r, color_g, color_b]}
			result = send_to_rhino("add_material_to_object", params)
			return f"Added material with color RGB({color_r}, {color_g}, {color_b}) to object"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def add_material_to_layer(layer_name: str) -> str:
		"""
		Add a material to a layer
		layer_name: Name of the layer
		"""
		try:
			result = send_to_rhino("add_material_to_layer", {"layer_name": layer_name})
			return f"Added material to layer '{layer_name}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def set_material_color(object_id: str, color_r: int, color_g: int, color_b: int) -> str:
		"""
		Set the color of an object's material
		object_id: ID of the object
		color_r, color_g, color_b: RGB color values (0-255)
		"""
		try:
			params = {"object_id": object_id, "color": [color_r, color_g, color_b]}
			send_to_rhino("set_material_color", params)
			return f"Set material color to RGB({color_r}, {color_g}, {color_b})"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def set_material_transparency(object_id: str, transparency: float) -> str:
		"""
		Set the transparency of an object's material
		object_id: ID of the object
		transparency: Transparency value (0.0=opaque to 1.0=fully transparent)
		"""
		try:
			params = {"object_id": object_id, "transparency": transparency}
			send_to_rhino("set_material_transparency", params)
			return f"Set material transparency to {transparency}"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def set_material_shine(object_id: str, shine: float) -> str:
		"""
		Set the shininess of an object's material
		object_id: ID of the object
		shine: Shine value (0.0=matte to 255.0=glossy)
		"""
		try:
			params = {"object_id": object_id, "shine": shine}
			send_to_rhino("set_material_shine", params)
			return f"Set material shine to {shine}"
		except Exception as e:
			return f"Error: {e}"
