"""
MCP tools for document/scene operations
"""

import json
from .utils import send_to_rhino


def register_tools(mcp):
	"""Register all document tools with the MCP server"""

	@mcp.tool()
	def get_scene_info() -> str:
		"""
		Get comprehensive information about the current Rhino scene.
		Returns details about all objects, layers, units, and object counts.
		This should be called first to understand what's already in the scene.
		"""
		try:
			result = send_to_rhino("get_scene_info")
			return json.dumps(result, indent=2)
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def get_selected_objects() -> str:
		"""
		Get information about currently selected objects in Rhino.
		Returns details about each selected object including type, layer, and location.
		"""
		try:
			result = send_to_rhino("get_selected_objects")
			return json.dumps(result, indent=2)
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def get_document_info() -> str:
		"""
		Get document information including name, path, and units
		"""
		try:
			result = send_to_rhino("get_document_info")
			return json.dumps(result, indent=2)
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def set_unit_system(unit_system: int) -> str:
		"""
		Set the document unit system
		unit_system: Unit system number (0=None, 1=Microns, 2=Millimeters, 3=Centimeters, 4=Meters, 8=Inches, 9=Feet)
		"""
		try:
			send_to_rhino("set_unit_system", {"system": unit_system})
			unit_names = {0: "None", 1: "Microns", 2: "Millimeters", 3: "Centimeters", 4: "Meters", 8: "Inches", 9: "Feet"}
			name = unit_names.get(unit_system, str(unit_system))
			return f"Set unit system to {name}"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def enable_redraw(enable: bool = True) -> str:
		"""
		Enable or disable viewport redraw (disable for batch operations)
		enable: True to enable redraw, False to disable
		"""
		try:
			send_to_rhino("enable_redraw", {"enable": enable})
			return f"Redraw {'enabled' if enable else 'disabled'}"
		except Exception as e:
			return f"Error: {e}"
