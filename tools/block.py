"""
MCP tools for block (instance definition) operations
"""

import json
from .utils import send_to_rhino


def register_tools(mcp):
	"""Register all block tools with the MCP server"""

	@mcp.tool()
	def create_block(object_ids: str, base_x: float, base_y: float, base_z: float,
					 block_name: str) -> str:
		"""
		Create a block definition from objects
		object_ids: Comma-separated IDs of objects to include in block
		base_x, base_y, base_z: Base insertion point
		block_name: Name for the block definition
		"""
		try:
			ids = [s.strip() for s in object_ids.split(",")]
			params = {
				"object_ids": ids,
				"base_point": [base_x, base_y, base_z],
				"name": block_name
			}
			send_to_rhino("create_block", params)
			return f"Created block '{block_name}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def insert_block(block_name: str, x: float, y: float, z: float,
					 scale: float = 1.0, rotation: float = 0) -> str:
		"""
		Insert a block instance into the document
		block_name: Name of the block definition
		x, y, z: Insertion point
		scale: Uniform scale factor (default 1.0)
		rotation: Rotation angle in degrees (default 0)
		"""
		try:
			params = {
				"name": block_name,
				"point": [x, y, z],
				"scale": [scale, scale, scale],
				"rotation": rotation
			}
			result = send_to_rhino("insert_block", params)
			return f"Inserted block '{block_name}' at ({x}, {y}, {z})"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def explode_block(block_id: str) -> str:
		"""
		Explode a block instance into individual objects
		block_id: ID of the block instance to explode
		"""
		try:
			result = send_to_rhino("explode_block", {"block_id": block_id})
			count = result.get("count", 0)
			return f"Exploded block into {count} objects"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def delete_block(block_name: str) -> str:
		"""
		Delete a block definition
		block_name: Name of the block definition to delete
		"""
		try:
			send_to_rhino("delete_block", {"name": block_name})
			return f"Deleted block '{block_name}'"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def list_blocks() -> str:
		"""
		List all block definitions in the document
		"""
		try:
			result = send_to_rhino("list_blocks")
			return json.dumps(result, indent=2)
		except Exception as e:
			return f"Error: {e}"
