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
			return "Joined curves into {0} result(s)".format(count)
		except Exception as e:
			return "Error: {0}".format(str(e))

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
			return "Exploded curves into {0} segments".format(count)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def offset_curve(distance: float) -> str:
		"""
		Offset selected curves by a distance
		distance: Offset distance (positive or negative)
		Curves must be selected in Rhino first
		"""
		try:
			params = {"distance": distance}
			result = send_to_rhino("offset_curve", params)
			count = result.get("count", 0)
			return "Offset {0} curves by distance {1}".format(count, distance)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def fillet_curves(radius: float) -> str:
		"""
		Fillet two selected curves with a radius
		radius: Fillet radius
		Exactly 2 curves must be selected in Rhino first
		"""
		try:
			params = {"radius": radius}
			result = send_to_rhino("fillet_curves", params)
			return "Created fillet with radius {0}".format(radius)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def extend_curve(extension: float) -> str:
		"""
		Extend selected curves by a length
		extension: Extension length
		Curves must be selected in Rhino first
		"""
		try:
			params = {"extension": extension}
			result = send_to_rhino("extend_curve", params)
			return "Extended curve by {0}".format(extension)
		except Exception as e:
			return "Error: {0}".format(str(e))
