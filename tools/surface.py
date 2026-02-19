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

	@mcp.tool()
	def create_pipe(curve_id: str, radius: float, cap: int = 1) -> str:
		"""
		Create a pipe surface along a curve
		curve_id: ID of the rail curve
		radius: Pipe radius
		cap: 0=none, 1=flat, 2=round
		"""
		try:
			result = send_to_rhino("create_pipe", {"curve_id": curve_id, "radius": radius, "cap": cap})
			count = result.get("count", 0)
			return f"Created pipe with {count} surface(s)"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def sweep1(rail_id: str, shape_ids: str) -> str:
		"""
		Sweep cross-section curves along a single rail curve
		rail_id: ID of the rail curve
		shape_ids: Comma-separated IDs of cross-section curves
		"""
		try:
			shapes = [s.strip() for s in shape_ids.split(",")]
			result = send_to_rhino("sweep1", {"rail": rail_id, "shapes": shapes})
			count = result.get("count", 0)
			return f"Created sweep1 with {count} surface(s)"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def sweep2(rail1_id: str, rail2_id: str, shape_ids: str) -> str:
		"""
		Sweep cross-section curves along two rail curves
		rail1_id: ID of the first rail curve
		rail2_id: ID of the second rail curve
		shape_ids: Comma-separated IDs of cross-section curves
		"""
		try:
			shapes = [s.strip() for s in shape_ids.split(",")]
			result = send_to_rhino("sweep2", {"rails": [rail1_id, rail2_id], "shapes": shapes})
			count = result.get("count", 0)
			return f"Created sweep2 with {count} surface(s)"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def create_planar_surface(curve_ids: str) -> str:
		"""
		Create a planar surface from closed planar curves
		curve_ids: Comma-separated IDs of closed planar curves
		"""
		try:
			ids = [s.strip() for s in curve_ids.split(",")]
			result = send_to_rhino("create_planar_surface", {"curve_ids": ids})
			count = result.get("count", 0)
			return f"Created {count} planar surface(s)"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def create_edge_surface(curve_ids: str) -> str:
		"""
		Create an edge surface from 2, 3, or 4 edge curves
		curve_ids: Comma-separated IDs of 2-4 edge curves
		"""
		try:
			ids = [s.strip() for s in curve_ids.split(",")]
			result = send_to_rhino("create_edge_surface", {"curve_ids": ids})
			return f"Created edge surface"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def create_network_surface(curve_ids: str, continuity: int = 1) -> str:
		"""
		Create a network surface from a grid of curves
		curve_ids: Comma-separated IDs of curves forming a network
		continuity: 0=position, 1=tangency, 2=curvature
		"""
		try:
			ids = [s.strip() for s in curve_ids.split(",")]
			result = send_to_rhino("create_network_surface", {"curve_ids": ids, "continuity": continuity})
			return f"Created network surface"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def create_patch(object_ids: str, uspan: int = 10, vspan: int = 10) -> str:
		"""
		Create a patch surface from curves and/or points
		object_ids: Comma-separated IDs of input curves/points
		uspan: U direction span count
		vspan: V direction span count
		"""
		try:
			ids = [s.strip() for s in object_ids.split(",")]
			result = send_to_rhino("create_patch", {"object_ids": ids, "uspan": uspan, "vspan": vspan})
			return f"Created patch surface"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def offset_surface(surface_id: str, distance: float) -> str:
		"""
		Offset a surface by a distance
		surface_id: ID of the surface to offset
		distance: Offset distance (positive or negative)
		"""
		try:
			result = send_to_rhino("offset_surface", {"surface_id": surface_id, "distance": distance})
			return f"Offset surface by {distance}"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def split_brep(brep_id: str, cutter_id: str) -> str:
		"""
		Split a brep with another brep or surface
		brep_id: ID of the brep to split
		cutter_id: ID of the cutting brep/surface
		"""
		try:
			result = send_to_rhino("split_brep", {"brep_id": brep_id, "cutter_id": cutter_id})
			count = result.get("count", 0)
			return f"Split brep into {count} pieces"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def fillet_surfaces(surface1_id: str, surface2_id: str, radius: float) -> str:
		"""
		Create a fillet between two surfaces
		surface1_id: ID of the first surface
		surface2_id: ID of the second surface
		radius: Fillet radius
		"""
		try:
			result = send_to_rhino("fillet_surfaces", {"surface1_id": surface1_id, "surface2_id": surface2_id, "radius": radius})
			count = result.get("count", 0)
			return f"Created fillet with {count} surface(s)"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def cap_planar_holes(brep_id: str) -> str:
		"""
		Cap all planar holes in a brep/polysurface
		brep_id: ID of the brep to cap
		"""
		try:
			result = send_to_rhino("cap_planar_holes", {"brep_id": brep_id})
			return f"Capped planar holes"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def extrude_curve_along_curve(curve_id: str, path_id: str) -> str:
		"""
		Extrude a curve along another curve path
		curve_id: ID of the profile curve to extrude
		path_id: ID of the path curve
		"""
		try:
			result = send_to_rhino("extrude_curve_along_curve", {"curve_id": curve_id, "path_id": path_id})
			return f"Extruded curve along path"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def extrude_curve_to_point(curve_id: str, point_x: float, point_y: float, point_z: float) -> str:
		"""
		Extrude a curve to a point (creates a cone-like surface)
		curve_id: ID of the curve to extrude
		point_x, point_y, point_z: Target point coordinates
		"""
		try:
			result = send_to_rhino("extrude_curve_to_point", {"curve_id": curve_id, "point": [point_x, point_y, point_z]})
			return f"Extruded curve to point ({point_x}, {point_y}, {point_z})"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def duplicate_edge_curves(brep_id: str) -> str:
		"""
		Duplicate the edge curves of a brep/surface
		brep_id: ID of the brep/surface
		"""
		try:
			result = send_to_rhino("duplicate_edge_curves", {"brep_id": brep_id})
			count = result.get("count", 0)
			return f"Duplicated {count} edge curves"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def duplicate_surface_border(surface_id: str) -> str:
		"""
		Duplicate the border curves of a surface
		surface_id: ID of the surface
		"""
		try:
			result = send_to_rhino("duplicate_surface_border", {"surface_id": surface_id})
			count = result.get("count", 0)
			return f"Duplicated {count} border curves"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def join_surfaces(surface_ids: str) -> str:
		"""
		Join multiple surfaces/polysurfaces into one polysurface
		surface_ids: Comma-separated IDs of surfaces to join
		"""
		try:
			ids = [s.strip() for s in surface_ids.split(",")]
			result = send_to_rhino("join_surfaces", {"surface_ids": ids})
			return f"Joined surfaces"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def explode_polysurfaces(brep_id: str) -> str:
		"""
		Explode a polysurface into individual surfaces
		brep_id: ID of the polysurface to explode
		"""
		try:
			result = send_to_rhino("explode_polysurfaces", {"brep_id": brep_id})
			count = result.get("count", 0)
			return f"Exploded polysurface into {count} surfaces"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def unroll_surface(surface_id: str) -> str:
		"""
		Unroll a developable surface flat
		surface_id: ID of the surface to unroll
		"""
		try:
			result = send_to_rhino("unroll_surface", {"surface_id": surface_id})
			count = result.get("count", 0)
			return f"Unrolled surface into {count} object(s)"
		except Exception as e:
			return f"Error: {e}"
