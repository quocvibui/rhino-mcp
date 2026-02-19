"""
MCP tools for user data operations
"""

import json
from .utils import send_to_rhino


def register_tools(mcp):
	"""Register all user data tools with the MCP server"""

	@mcp.tool()
	def set_user_text(object_id: str, key: str, value: str) -> str:
		"""
		Set user text (key-value metadata) on an object
		object_id: ID of the object
		key: Metadata key name
		value: Metadata value
		"""
		try:
			params = {"object_id": object_id, "key": key, "value": value}
			send_to_rhino("set_user_text", params)
			return f"Set user text '{key}' = '{value}' on object"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def get_user_text(object_id: str, key: str = "") -> str:
		"""
		Get user text from an object. If no key specified, returns all key-value pairs.
		object_id: ID of the object
		key: Specific key to retrieve (optional, empty = get all)
		"""
		try:
			params = {"object_id": object_id}
			if key:
				params["key"] = key
			result = send_to_rhino("get_user_text", params)
			return json.dumps(result, indent=2)
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def set_document_user_text(key: str, value: str) -> str:
		"""
		Set document-level user text (key-value metadata)
		key: Metadata key name
		value: Metadata value
		"""
		try:
			params = {"key": key, "value": value}
			send_to_rhino("set_document_user_text", params)
			return f"Set document user text '{key}' = '{value}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def get_document_user_text(key: str = "") -> str:
		"""
		Get document-level user text. If no key specified, returns all key-value pairs.
		key: Specific key to retrieve (optional, empty = get all)
		"""
		try:
			params = {}
			if key:
				params["key"] = key
			result = send_to_rhino("get_document_user_text", params)
			return json.dumps(result, indent=2)
		except Exception as e:
			return f"Error: {e}"
