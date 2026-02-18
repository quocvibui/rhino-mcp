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
			send_to_rhino("create_point", {"x": x, "y": y, "z": z})
			return f"Created point at ({x}, {y}, {z})"
		except Exception as e:
			return f"Error: {e}"

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
			send_to_rhino("create_line", params)
			return f"Created line from ({start_x}, {start_y}, {start_z}) to ({end_x}, {end_y}, {end_z})"
		except Exception as e:
			return f"Error: {e}"

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
			send_to_rhino("create_circle", params)
			return f"Created circle with radius {radius} at ({center_x}, {center_y}, {center_z})"
		except Exception as e:
			return f"Error: {e}"

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
			send_to_rhino("create_arc", params)
			return f"Created arc with radius {radius} from {start_angle} to {end_angle} degrees"
		except Exception as e:
			return f"Error: {e}"

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
			send_to_rhino("create_ellipse", params)
			return f"Created ellipse with radii {x_radius}x{y_radius}"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def create_polyline(points: list[list[float]]) -> str:
		"""
		Create a polyline through multiple points
		points: List of points, each point is [x, y, z]
		Example: [[0,0,0], [10,0,0], [10,10,0], [0,10,0]]
		"""
		try:
			send_to_rhino("create_polyline", {"points": points})
			return f"Created polyline with {len(points)} points"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def create_curve(points: list[list[float]], degree: int = 3) -> str:
		"""
		Create a smooth interpolated curve through points
		points: List of points, each point is [x, y, z]
		degree: Curve degree (3 for cubic, higher for smoother)
		"""
		try:
			send_to_rhino("create_curve", {"points": points, "degree": degree})
			return f"Created curve with {len(points)} points, degree {degree}"
		except Exception as e:
			return f"Error: {e}"
