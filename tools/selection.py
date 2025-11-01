"""
MCP tools for object selection
"""

from .utils import send_to_rhino


def register_tools(mcp):
	"""Register all selection tools with the MCP server"""

	@mcp.tool()
	def select_all() -> str:
		"""
		Select all objects in the Rhino document
		"""
		try:
			result = send_to_rhino("select_all")
			count = result.get("count", 0)
			return "Selected {0} objects".format(count)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def select_by_type(object_type: str) -> str:
		"""
		Select objects by type
		object_type: Type to select - 'point', 'curve', 'surface', 'polysurface', 'mesh'
		"""
		try:
			params = {"type": object_type}
			result = send_to_rhino("select_by_type", params)
			count = result.get("count", 0)
			return "Selected {0} {1} objects".format(count, object_type)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def select_by_layer(layer_name: str) -> str:
		"""
		Select all objects on a specific layer
		layer_name: Layer name to select objects from
		"""
		try:
			params = {"layer": layer_name}
			result = send_to_rhino("select_by_layer", params)
			count = result.get("count", 0)
			return "Selected {0} objects on layer '{1}'".format(count, layer_name)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def unselect_all() -> str:
		"""
		Deselect all objects in Rhino
		Clears the current selection
		"""
		try:
			result = send_to_rhino("unselect_all")
			return "Deselected all objects"
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def delete_selected() -> str:
		"""
		Delete all currently selected objects in Rhino.
		Use select_all first if you want to delete everything.
		"""
		try:
			result = send_to_rhino("delete_selected")
			deleted = result.get("deleted", 0)
			return "Deleted {0} objects".format(deleted)
		except Exception as e:
			return "Error: {0}".format(str(e))
