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

	@mcp.tool()
	def create_rectangle(center_x: float, center_y: float, center_z: float,
						 width: float, height: float) -> str:
		"""
		Create a rectangle curve
		center_x, center_y, center_z: Center point of the rectangle plane
		width: Width of the rectangle
		height: Height of the rectangle
		"""
		try:
			params = {"center": [center_x, center_y, center_z], "width": width, "height": height}
			result = send_to_rhino("create_rectangle", params)
			return f"Created rectangle {width}x{height}"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def create_spiral(center_x: float, center_y: float, center_z: float,
					  top_x: float, top_y: float, top_z: float,
					  pitch: float, turns: float, radius0: float,
					  radius1: float = -1) -> str:
		"""
		Create a spiral curve
		center_x, center_y, center_z: Base center point
		top_x, top_y, top_z: Top point (defines axis direction)
		pitch: Distance between turns
		turns: Number of turns
		radius0: Starting radius
		radius1: Ending radius (-1 = same as radius0)
		"""
		try:
			r1 = radius0 if radius1 < 0 else radius1
			params = {
				"point0": [center_x, center_y, center_z],
				"point1": [top_x, top_y, top_z],
				"pitch": pitch, "turns": turns,
				"radius0": radius0, "radius1": r1
			}
			result = send_to_rhino("create_spiral", params)
			return f"Created spiral with {turns} turns"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def create_nurbs_curve(points: str, degree: int = 3) -> str:
		"""
		Create a NURBS curve from control points
		points: Semicolon-separated control points, each as 'x,y,z' (e.g. '0,0,0;10,5,0;20,0,0')
		degree: Curve degree (default 3)
		"""
		try:
			pts = [[float(c) for c in p.split(",")] for p in points.split(";")]
			params = {"points": pts, "degree": degree}
			result = send_to_rhino("create_nurbs_curve", params)
			return f"Created NURBS curve with {len(pts)} control points, degree {degree}"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def create_blend_curve(curve1_id: str, curve2_id: str,
						   continuity: int = 1) -> str:
		"""
		Create a blend curve between two curves
		curve1_id: ID of the first curve
		curve2_id: ID of the second curve
		continuity: 0=position, 1=tangency, 2=curvature
		"""
		try:
			params = {"curve1": curve1_id, "curve2": curve2_id, "continuity": continuity}
			result = send_to_rhino("create_blend_curve", params)
			return f"Created blend curve with continuity {continuity}"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def fillet_curves(radius: float) -> str:
		"""
		Create a fillet arc between two selected curves
		radius: Fillet radius
		Exactly 2 curves must be selected in Rhino first
		"""
		try:
			result = send_to_rhino("fillet_curves", {"radius": radius})
			return f"Created fillet with radius {radius}"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def divide_curve(curve_id: str, segments: int, create_points: bool = True) -> str:
		"""
		Divide a curve into equal segments
		curve_id: ID of the curve
		segments: Number of segments
		create_points: Whether to create point objects at divisions
		"""
		try:
			result = send_to_rhino("divide_curve", {"curve_id": curve_id, "segments": segments, "create_points": create_points})
			count = result.get("count", 0)
			return f"Divided curve into {count} points"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def divide_curve_length(curve_id: str, length: float, create_points: bool = True) -> str:
		"""
		Divide a curve by arc length
		curve_id: ID of the curve
		length: Segment arc length
		create_points: Whether to create point objects at divisions
		"""
		try:
			result = send_to_rhino("divide_curve_length", {"curve_id": curve_id, "length": length, "create_points": create_points})
			count = result.get("count", 0)
			return f"Divided curve into {count} points by length {length}"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def split_curve(curve_id: str, parameters: str) -> str:
		"""
		Split a curve at parameter values
		curve_id: ID of the curve
		parameters: Comma-separated parameter values (0.0-1.0 normalized)
		"""
		try:
			params_list = [float(p.strip()) for p in parameters.split(",")]
			result = send_to_rhino("split_curve", {"curve_id": curve_id, "parameters": params_list})
			count = result.get("count", 0)
			return f"Split curve into {count} segments"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def close_curve(curve_id: str) -> str:
		"""
		Close an open curve
		curve_id: ID of the curve to close
		"""
		try:
			result = send_to_rhino("close_curve", {"curve_id": curve_id})
			return f"Closed curve"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def reverse_curve(curve_id: str) -> str:
		"""
		Reverse the direction of a curve
		curve_id: ID of the curve to reverse
		"""
		try:
			result = send_to_rhino("reverse_curve", {"curve_id": curve_id})
			return f"Reversed curve direction"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def rebuild_curve(curve_id: str, degree: int = 3, point_count: int = 10) -> str:
		"""
		Rebuild a curve with new degree and control point count
		curve_id: ID of the curve to rebuild
		degree: New curve degree
		point_count: New number of control points
		"""
		try:
			result = send_to_rhino("rebuild_curve", {"curve_id": curve_id, "degree": degree, "point_count": point_count})
			return f"Rebuilt curve with degree {degree} and {point_count} control points"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def project_curve_to_surface(curve_ids: str, surface_ids: str,
								 dir_x: float = 0, dir_y: float = 0, dir_z: float = -1) -> str:
		"""
		Project curves onto surfaces along a direction
		curve_ids: Comma-separated curve IDs
		surface_ids: Comma-separated surface IDs
		dir_x, dir_y, dir_z: Projection direction vector
		"""
		try:
			curves = [s.strip() for s in curve_ids.split(",")]
			surfaces = [s.strip() for s in surface_ids.split(",")]
			params = {"curve_ids": curves, "surface_ids": surfaces, "direction": [dir_x, dir_y, dir_z]}
			result = send_to_rhino("project_curve_to_surface", params)
			count = result.get("count", 0)
			return f"Projected {count} curve(s) onto surface"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def curve_closest_point(curve_id: str, point_x: float, point_y: float, point_z: float) -> str:
		"""
		Find the closest point on a curve to a given point
		curve_id: ID of the curve
		point_x, point_y, point_z: Test point coordinates
		"""
		try:
			import json
			result = send_to_rhino("curve_closest_point", {"curve_id": curve_id, "point": [point_x, point_y, point_z]})
			return json.dumps(result, indent=2)
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def evaluate_curve(curve_id: str, parameter: float) -> str:
		"""
		Evaluate a curve at a parameter to get point and tangent
		curve_id: ID of the curve
		parameter: Parameter value along the curve
		"""
		try:
			import json
			result = send_to_rhino("evaluate_curve", {"curve_id": curve_id, "parameter": parameter})
			return json.dumps(result, indent=2)
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def curve_start_end_points(curve_id: str) -> str:
		"""
		Get the start and end points of a curve
		curve_id: ID of the curve
		"""
		try:
			import json
			result = send_to_rhino("curve_start_end_points", {"curve_id": curve_id})
			return json.dumps(result, indent=2)
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def curve_curve_intersection(curve1_id: str, curve2_id: str) -> str:
		"""
		Find intersections between two curves
		curve1_id: ID of the first curve
		curve2_id: ID of the second curve
		"""
		try:
			import json
			result = send_to_rhino("curve_curve_intersection", {"curve1": curve1_id, "curve2": curve2_id})
			return json.dumps(result, indent=2)
		except Exception as e:
			return f"Error: {e}"
