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
			return f"Selected {count} objects"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def select_by_type(object_type: str) -> str:
		"""
		Select objects by type
		object_type: Type to select - 'point', 'curve', 'surface', 'polysurface', 'mesh'
		"""
		try:
			result = send_to_rhino("select_by_type", {"type": object_type})
			count = result.get("count", 0)
			return f"Selected {count} {object_type} objects"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def select_by_layer(layer_name: str) -> str:
		"""
		Select all objects on a specific layer
		layer_name: Layer name to select objects from
		"""
		try:
			result = send_to_rhino("select_by_layer", {"layer": layer_name})
			count = result.get("count", 0)
			return f"Selected {count} objects on layer '{layer_name}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def unselect_all() -> str:
		"""
		Deselect all objects in Rhino
		Clears the current selection
		"""
		try:
			send_to_rhino("unselect_all")
			return "Deselected all objects"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def delete_selected() -> str:
		"""
		Delete all currently selected objects in Rhino.
		Use select_all first if you want to delete everything.
		"""
		try:
			result = send_to_rhino("delete_selected")
			deleted = result.get("deleted", 0)
			return f"Deleted {deleted} objects"
		except Exception as e:
			return f"Error: {e}"
