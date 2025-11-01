"""
MCP tools for object transformations
"""

from .utils import send_to_rhino


def register_tools(mcp):
	"""Register all transformation tools with the MCP server"""

	@mcp.tool()
	def move_objects(dx: float, dy: float, dz: float) -> str:
		"""
		Move selected objects by a displacement vector
		dx: Displacement in X direction
		dy: Displacement in Y direction
		dz: Displacement in Z direction
		Objects must be selected in Rhino first
		"""
		try:
			params = {"displacement": [dx, dy, dz]}
			result = send_to_rhino("move_objects", params)
			moved = result.get("moved", 0)
			return "Moved {0} objects by ({1}, {2}, {3})".format(moved, dx, dy, dz)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def rotate_objects(center_x: float, center_y: float, center_z: float,
					   angle: float) -> str:
		"""
		Rotate selected objects around Z-axis
		center_x, center_y, center_z: Rotation center point
		angle: Rotation angle in degrees
		Objects must be selected in Rhino first
		"""
		try:
			params = {
				"center": [center_x, center_y, center_z],
				"angle": angle
			}
			result = send_to_rhino("rotate_objects", params)
			count = result.get("count", 0)
			return "Rotated {0} objects by {1} degrees".format(count, angle)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def scale_objects(center_x: float, center_y: float, center_z: float,
					  scale_factor: float) -> str:
		"""
		Scale selected objects uniformly from a center point
		center_x, center_y, center_z: Scale center point
		scale_factor: Scale factor (2.0 = double size, 0.5 = half size)
		Objects must be selected in Rhino first
		"""
		try:
			params = {
				"center": [center_x, center_y, center_z],
				"scale": scale_factor
			}
			result = send_to_rhino("scale_objects", params)
			scaled = result.get("scaled", 0)
			return "Scaled {0} objects by factor {1}".format(scaled, scale_factor)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def mirror_objects(start_x: float, start_y: float, start_z: float,
					   end_x: float, end_y: float, end_z: float) -> str:
		"""
		Mirror selected objects across a line
		start_x, start_y, start_z: Start point of mirror line
		end_x, end_y, end_z: End point of mirror line
		Objects must be selected in Rhino first
		"""
		try:
			params = {
				"start": [start_x, start_y, start_z],
				"end": [end_x, end_y, end_z]
			}
			result = send_to_rhino("mirror_objects", params)
			mirrored = result.get("mirrored", 0)
			return "Mirrored {0} objects".format(mirrored)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def copy_objects(dx: float, dy: float, dz: float) -> str:
		"""
		Copy selected objects to a new location
		dx: Displacement in X direction
		dy: Displacement in Y direction
		dz: Displacement in Z direction
		Objects must be selected in Rhino first
		"""
		try:
			params = {"displacement": [dx, dy, dz]}
			result = send_to_rhino("copy_objects", params)
			copied = result.get("copied", 0)
			return "Copied {0} objects".format(copied)
		except Exception as e:
			return "Error: {0}".format(str(e))

	@mcp.tool()
	def array_linear(dx: float, dy: float, dz: float, count: int) -> str:
		"""
		Create a linear array of selected objects
		dx, dy, dz: Spacing between copies
		count: Number of copies to create
		Objects must be selected in Rhino first
		"""
		try:
			params = {
				"displacement": [dx, dy, dz],
				"count": count
			}
			result = send_to_rhino("array_linear", params)
			created = result.get("created", 0)
			return "Created linear array with {0} new objects".format(created)
		except Exception as e:
			return "Error: {0}".format(str(e))
