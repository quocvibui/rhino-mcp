"""
MCP tools for analysis and measurement
"""

from .utils import send_to_rhino


def register_tools(mcp):
	"""Register all analysis/utility tools with the MCP server"""

	@mcp.tool()
	def measure_distance(point1_x: float, point1_y: float, point1_z: float,
						 point2_x: float, point2_y: float, point2_z: float) -> str:
		"""
		Measure distance between two points
		point1_x, point1_y, point1_z: First point coordinates
		point2_x, point2_y, point2_z: Second point coordinates
		"""
		try:
			params = {
				"point1": [point1_x, point1_y, point1_z],
				"point2": [point2_x, point2_y, point2_z]
			}
			result = send_to_rhino("measure_distance", params)
			distance = result.get("distance", 0)
			return "Distance: {0}".format(distance)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def measure_curve_length() -> str:
		"""
		Measure length of selected curve
		One curve must be selected in Rhino first
		"""
		try:
			result = send_to_rhino("measure_curve_length")
			length = result.get("length", 0)
			return "Curve length: {0}".format(length)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def measure_area() -> str:
		"""
		Measure area of selected surface or closed curve
		One surface or closed planar curve must be selected in Rhino first
		"""
		try:
			result = send_to_rhino("measure_area")
			area = result.get("area", 0)
			return "Area: {0}".format(area)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def measure_volume() -> str:
		"""
		Measure volume of selected solid
		One closed solid must be selected in Rhino first
		"""
		try:
			result = send_to_rhino("measure_volume")
			volume = result.get("volume", 0)
			return "Volume: {0}".format(volume)
		except Exception as e:
			return "Error: {0}".format(str(e))
