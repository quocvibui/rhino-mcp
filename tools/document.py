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
			return "Error: {0}".format(str(e))

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
			return "Error: {0}".format(str(e))
