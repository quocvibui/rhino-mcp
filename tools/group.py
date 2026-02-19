"""
MCP tools for group operations
"""

import json
from .utils import send_to_rhino


def register_tools(mcp):
	"""Register all group tools with the MCP server"""

	@mcp.tool()
	def create_group(group_name: str, object_ids: str = "") -> str:
		"""
		Create a new group, optionally adding objects to it
		group_name: Name for the new group
		object_ids: Comma-separated object IDs to add to group (optional)
		"""
		try:
			params = {"name": group_name}
			if object_ids:
				params["object_ids"] = [s.strip() for s in object_ids.split(",")]
			result = send_to_rhino("create_group", params)
			return f"Created group '{group_name}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def delete_group(group_name: str) -> str:
		"""
		Delete a group (does not delete the objects in it)
		group_name: Name of the group to delete
		"""
		try:
			send_to_rhino("delete_group", {"name": group_name})
			return f"Deleted group '{group_name}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def add_to_group(group_name: str, object_ids: str) -> str:
		"""
		Add objects to an existing group
		group_name: Name of the target group
		object_ids: Comma-separated object IDs to add
		"""
		try:
			ids = [s.strip() for s in object_ids.split(",")]
			result = send_to_rhino("add_to_group", {"name": group_name, "object_ids": ids})
			count = result.get("count", 0)
			return f"Added {count} objects to group '{group_name}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def remove_from_group(group_name: str, object_ids: str) -> str:
		"""
		Remove objects from a group
		group_name: Name of the group
		object_ids: Comma-separated object IDs to remove
		"""
		try:
			ids = [s.strip() for s in object_ids.split(",")]
			result = send_to_rhino("remove_from_group", {"name": group_name, "object_ids": ids})
			count = result.get("count", 0)
			return f"Removed {count} objects from group '{group_name}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def list_groups() -> str:
		"""
		List all groups in the document
		"""
		try:
			result = send_to_rhino("list_groups")
			return json.dumps(result, indent=2)
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def select_by_group(group_name: str) -> str:
		"""
		Select all objects in a group
		group_name: Name of the group
		"""
		try:
			result = send_to_rhino("select_by_group", {"name": group_name})
			count = result.get("count", 0)
			return f"Selected {count} objects from group '{group_name}'"
		except Exception as e:
			return f"Error: {e}"
