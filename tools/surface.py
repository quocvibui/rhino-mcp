"""
MCP tools for surface and solid creation
"""

from .utils import send_to_rhino


def register_tools(mcp):
	"""Register all surface/solid tools with the MCP server"""

	@mcp.tool()
	def create_box(width: float = 10, depth: float = 10, height: float = 10,
				   x: float = 0, y: float = 0, z: float = 0) -> str:
		"""
		Create a box in Rhino
		width: Box width (X direction)
		depth: Box depth (Y direction)
		height: Box height (Z direction)
		x, y, z: Position coordinates (default 0, 0, 0)
		"""
		try:
			params = {
				"width": width, "depth": depth, "height": height,
				"x": x, "y": y, "z": z
			}
			send_to_rhino("create_box", params)
			return f"Created box {width}x{depth}x{height} at ({x}, {y}, {z})"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def create_sphere(center_x: float, center_y: float, center_z: float,
					  radius: float) -> str:
		"""
		Create a sphere in Rhino
		center_x, center_y, center_z: Center point coordinates
		radius: Sphere radius
		"""
		try:
			params = {
				"center": [center_x, center_y, center_z],
				"radius": radius
			}
			send_to_rhino("create_sphere", params)
			return f"Created sphere with radius {radius} at ({center_x}, {center_y}, {center_z})"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def create_cylinder(base_x: float, base_y: float, base_z: float,
						height: float, radius: float) -> str:
		"""
		Create a cylinder in Rhino
		base_x, base_y, base_z: Base center point coordinates
		height: Cylinder height
		radius: Cylinder radius
		"""
		try:
			params = {
				"base": [base_x, base_y, base_z],
				"height": height,
				"radius": radius
			}
			send_to_rhino("create_cylinder", params)
			return f"Created cylinder with radius {radius}, height {height} at ({base_x}, {base_y}, {base_z})"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def create_cone(base_x: float, base_y: float, base_z: float,
					height: float, radius: float) -> str:
		"""
		Create a cone in Rhino
		base_x, base_y, base_z: Base center point coordinates
		height: Cone height
		radius: Base radius
		"""
		try:
			params = {
				"base": [base_x, base_y, base_z],
				"height": height,
				"radius": radius
			}
			send_to_rhino("create_cone", params)
			return f"Created cone with base radius {radius}, height {height} at ({base_x}, {base_y}, {base_z})"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def create_torus(center_x: float, center_y: float, center_z: float,
					 major_radius: float, minor_radius: float) -> str:
		"""
		Create a torus in Rhino
		center_x, center_y, center_z: Center point coordinates
		major_radius: Major radius (distance from center to tube center)
		minor_radius: Minor radius (tube radius)
		"""
		try:
			params = {
				"center": [center_x, center_y, center_z],
				"major_radius": major_radius,
				"minor_radius": minor_radius
			}
			send_to_rhino("create_torus", params)
			return f"Created torus with radii {major_radius}/{minor_radius}"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def extrude_curve_straight(height: float) -> str:
		"""
		Extrude selected curves straight up to create surfaces
		height: Extrusion height in Z direction
		Closed curves will create solids, open curves will create surfaces
		Curves must be selected in Rhino first
		"""
		try:
			send_to_rhino("extrude_curve_straight", {"height": height})
			return f"Extruded curves with height {height}"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def revolve_curve(axis_start_x: float, axis_start_y: float, axis_start_z: float,
					  axis_end_x: float, axis_end_y: float, axis_end_z: float,
					  angle: float = 360) -> str:
		"""
		Revolve selected curves around an axis to create surfaces
		axis_start_x, axis_start_y, axis_start_z: Axis start point
		axis_end_x, axis_end_y, axis_end_z: Axis end point
		angle: Rotation angle in degrees (default 360 for full revolution)
		Curves must be selected in Rhino first
		"""
		try:
			params = {
				"axis_start": [axis_start_x, axis_start_y, axis_start_z],
				"axis_end": [axis_end_x, axis_end_y, axis_end_z],
				"angle": angle
			}
			result = send_to_rhino("revolve_curve", params)
			count = result.get("count", 0)
			return f"Revolved {count} curves by {angle} degrees"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def loft_curves() -> str:
		"""
		Create a lofted surface through selected curves
		Creates smooth surface transitioning between curves
		At least 2 curves must be selected in Rhino first
		"""
		try:
			send_to_rhino("loft_curves")
			return "Created lofted surface"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def boolean_union() -> str:
		"""
		Perform boolean union on selected objects
		Combines multiple solids into one
		At least 2 objects must be selected in Rhino first
		"""
		try:
			result = send_to_rhino("boolean_union")
			count = result.get("count", 0)
			return f"Boolean union created {count} result(s)"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def boolean_difference() -> str:
		"""
		Perform boolean difference on selected objects
		Subtracts all objects after the first from the first object
		At least 2 objects must be selected in Rhino first
		"""
		try:
			result = send_to_rhino("boolean_difference")
			count = result.get("count", 0)
			return f"Boolean difference created {count} result(s)"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def boolean_intersection() -> str:
		"""
		Perform boolean intersection on selected objects
		Keeps only the overlapping volume
		At least 2 objects must be selected in Rhino first
		"""
		try:
			result = send_to_rhino("boolean_intersection")
			count = result.get("count", 0)
			return f"Boolean intersection created {count} result(s)"
		except Exception as e:
			return f"Error: {e}"
