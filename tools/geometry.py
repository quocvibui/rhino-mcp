"""
MCP tools for basic geometry creation
"""

from .utils import send_to_rhino


def register_tools(mcp):
	"""Register all geometry tools with the MCP server"""

	@mcp.tool()
	def create_point(x: float, y: float, z: float = 0) -> str:
		"""
		Create a point in Rhino
		x: X coordinate
		y: Y coordinate
		z: Z coordinate (default 0)
		"""
		try:
			result = send_to_rhino("create_point", {"x": x, "y": y, "z": z})
			return "Created point at ({0}, {1}, {2})".format(x, y, z)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def create_line(start_x: float, start_y: float, start_z: float,
					end_x: float, end_y: float, end_z: float) -> str:
		"""
		Create a line in Rhino between two points
		start_x, start_y, start_z: Start point coordinates
		end_x, end_y, end_z: End point coordinates
		"""
		try:
			params = {
				"start": [start_x, start_y, start_z],
				"end": [end_x, end_y, end_z]
			}
			result = send_to_rhino("create_line", params)
			return "Created line from ({0}, {1}, {2}) to ({3}, {4}, {5})".format(
				start_x, start_y, start_z, end_x, end_y, end_z)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def create_circle(center_x: float, center_y: float, center_z: float, radius: float) -> str:
		"""
		Create a circle in Rhino
		center_x, center_y, center_z: Center point coordinates
		radius: Circle radius
		"""
		try:
			params = {
				"center": [center_x, center_y, center_z],
				"radius": radius
			}
			result = send_to_rhino("create_circle", params)
			return "Created circle with radius {0} at ({1}, {2}, {3})".format(
				radius, center_x, center_y, center_z)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def create_arc(center_x: float, center_y: float, center_z: float,
				   radius: float, start_angle: float, end_angle: float) -> str:
		"""
		Create an arc in Rhino
		center_x, center_y, center_z: Center point coordinates
		radius: Arc radius
		start_angle: Start angle in degrees
		end_angle: End angle in degrees
		"""
		try:
			params = {
				"center": [center_x, center_y, center_z],
				"radius": radius,
				"start_angle": start_angle,
				"end_angle": end_angle
			}
			result = send_to_rhino("create_arc", params)
			return "Created arc with radius {0} from {1} to {2} degrees".format(
				radius, start_angle, end_angle)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def create_ellipse(center_x: float, center_y: float, center_z: float,
					   x_radius: float, y_radius: float) -> str:
		"""
		Create an ellipse in Rhino
		center_x, center_y, center_z: Center point coordinates
		x_radius: Radius in X direction
		y_radius: Radius in Y direction
		"""
		try:
			params = {
				"center": [center_x, center_y, center_z],
				"x_radius": x_radius,
				"y_radius": y_radius
			}
			result = send_to_rhino("create_ellipse", params)
			return "Created ellipse with radii {0}x{1}".format(x_radius, y_radius)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def create_polyline(points: list[list[float]]) -> str:
		"""
		Create a polyline through multiple points
		points: List of points, each point is [x, y, z]
		Example: [[0,0,0], [10,0,0], [10,10,0], [0,10,0]]
		"""
		try:
			result = send_to_rhino("create_polyline", {"points": points})
			return "Created polyline with {0} points".format(len(points))
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def create_curve(points: list[list[float]], degree: int = 3) -> str:
		"""
		Create a smooth interpolated curve through points
		points: List of points, each point is [x, y, z]
		degree: Curve degree (3 for cubic, higher for smoother)
		"""
		try:
			result = send_to_rhino("create_curve", {"points": points, "degree": degree})
			return "Created curve with {0} points, degree {1}".format(len(points), degree)
		except Exception as e:
			return "Error: {0}".format(str(e))
