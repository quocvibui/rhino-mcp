"""
MCP tools for curve operations
"""

from .utils import send_to_rhino


def register_tools(mcp):
	"""Register all curve operation tools with the MCP server"""

	@mcp.tool()
	def join_curves() -> str:
		"""
		Join selected curves into a single curve
		Curves must be selected in Rhino first and should be connected
		"""
		try:
			result = send_to_rhino("join_curves")
			count = result.get("count", 0)
			return f"Joined curves into {count} result(s)"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def explode_curves() -> str:
		"""
		Explode selected curves into segments
		Breaks polylines and polycurves into individual segments
		Curves must be selected in Rhino first
		"""
		try:
			result = send_to_rhino("explode_curves")
			count = result.get("count", 0)
			return f"Exploded curves into {count} segments"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def offset_curve(distance: float) -> str:
		"""
		Offset selected curves by a distance
		distance: Offset distance (positive or negative)
		Curves must be selected in Rhino first
		"""
		try:
			result = send_to_rhino("offset_curve", {"distance": distance})
			count = result.get("count", 0)
			return f"Offset {count} curves by distance {distance}"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def fillet_curves(radius: float) -> str:
		"""
		Fillet two selected curves with a radius
		radius: Fillet radius
		Exactly 2 curves must be selected in Rhino first
		"""
		try:
			send_to_rhino("fillet_curves", {"radius": radius})
			return f"Created fillet with radius {radius}"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def extend_curve(extension: float) -> str:
		"""
		Extend selected curves by a length
		extension: Extension length
		Curves must be selected in Rhino first
		"""
		try:
			send_to_rhino("extend_curve", {"extension": extension})
			return f"Extended curve by {extension}"
		except Exception as e:
			return f"Error: {e}"
