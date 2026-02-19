"""
RhinoScriptSyntax surface functions
"""

import rhinoscriptsyntax as rs


def add_box(corners):
	"""Add a box"""
	box_id = rs.AddBox(corners)
	if box_id:
		rs.Redraw()
		return {"status": "success", "id": str(box_id)}
	return {"status": "error", "message": "Failed to add box"}


def add_sphere(center, radius):
	"""Add a sphere"""
	sphere_id = rs.AddSphere(center, radius)
	if sphere_id:
		rs.Redraw()
		return {"status": "success", "id": str(sphere_id)}
	return {"status": "error", "message": "Failed to add sphere"}


def add_cone(base, height_point, radius):
	"""Add a cone"""
	cone_id = rs.AddCone(base, height_point, radius)
	if cone_id:
		rs.Redraw()
		return {"status": "success", "id": str(cone_id)}
	return {"status": "error", "message": "Failed to add cone"}


def add_torus(base, major_radius, minor_radius):
	"""Add a torus"""
	torus_id = rs.AddTorus(base, major_radius, minor_radius)
	if torus_id:
		rs.Redraw()
		return {"status": "success", "id": str(torus_id)}
	return {"status": "error", "message": "Failed to add torus"}


def extrude_curve_straight(curve_id, start, end):
	"""Extrude curve straight"""
	result = rs.ExtrudeCurveStraight(curve_id, start, end)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to extrude curve"}


def add_rev_srf(curve_id, axis, start_angle=0, end_angle=360):
	"""Add surface of revolution"""
	result = rs.AddRevSrf(curve_id, axis, start_angle, end_angle)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to create revolution surface"}


def add_loft_srf(curve_ids):
	"""Add lofted surface"""
	result = rs.AddLoftSrf(curve_ids)
	if result and len(result) > 0:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to create loft surface"}


def boolean_union(obj_ids):
	"""Boolean union"""
	result = rs.BooleanUnion(obj_ids, delete_input=True)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to perform boolean union"}


def boolean_difference(obj_ids):
	"""Boolean difference"""
	if len(obj_ids) < 2:
		return {"status": "error", "message": "Need at least 2 objects"}
	result = rs.BooleanDifference([obj_ids[0]], obj_ids[1:], delete_input=True)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to perform boolean difference"}


def boolean_intersection(obj_ids):
	"""Boolean intersection"""
	if len(obj_ids) < 2:
		return {"status": "error", "message": "Need at least 2 objects"}
	result = rs.BooleanIntersection([obj_ids[0]], obj_ids[1:], delete_input=True)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to perform boolean intersection"}


def surface_area(obj_id):
	"""Get surface area"""
	area = rs.SurfaceArea(obj_id)
	if area:
		return {"status": "success", "area": area[0]}
	return {"status": "error", "message": "Failed to get surface area"}


def surface_volume(obj_id):
	"""Get surface volume"""
	volume = rs.SurfaceVolume(obj_id)
	if volume:
		return {"status": "success", "volume": volume[0]}
	return {"status": "error", "message": "Failed to get volume"}


def is_surface(obj_id):
	"""Check if object is a surface"""
	return rs.IsSurface(obj_id)


def is_polysurface(obj_id):
	"""Check if object is a polysurface"""
	return rs.IsPolysurface(obj_id)


def add_pipe(curve_id, parameters, radii, cap=1):
	"""Add a pipe surface along a curve"""
	result = rs.AddPipe(curve_id, parameters, radii, cap=cap)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to create pipe"}


def add_sweep1(rail, shapes, closed=False):
	"""Sweep shapes along a single rail"""
	result = rs.AddSweep1(rail, shapes, closed)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to create sweep1"}


def add_sweep2(rails, shapes, closed=False):
	"""Sweep shapes along two rails"""
	result = rs.AddSweep2(rails, shapes, closed)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to create sweep2"}


def add_planar_srf(curve_ids):
	"""Create planar surface from closed planar curves"""
	result = rs.AddPlanarSrf(curve_ids)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to create planar surface"}


def add_edge_srf(curve_ids):
	"""Create edge surface from 2-4 edge curves"""
	result = rs.AddEdgeSrf(curve_ids)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to create edge surface"}


def add_network_srf(curves, continuity=1, edge_tolerance=0):
	"""Create network surface from curves"""
	result = rs.AddNetworkSrf(curves, continuity, edge_tolerance)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to create network surface"}


def add_patch(object_ids, uspan=10, vspan=10):
	"""Create patch surface from curves/points"""
	result = rs.AddPatch(object_ids, (uspan, vspan))
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to create patch surface"}


def offset_surface(surface_id, distance):
	"""Offset a surface"""
	result = rs.OffsetSurface(surface_id, distance)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to offset surface"}


def split_brep(brep_id, cutter_id):
	"""Split a brep with another brep"""
	result = rs.SplitBrep(brep_id, cutter_id)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to split brep"}


def fillet_surfaces(srf1, srf2, radius):
	"""Fillet between two surfaces"""
	result = rs.FilletSurfaces(srf1, srf2, radius)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to fillet surfaces"}


def cap_planar_holes(brep_id):
	"""Cap planar holes in a brep"""
	result = rs.CapPlanarHoles(brep_id)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to cap planar holes"}


def extrude_curve_along_curve(curve_id, path_id):
	"""Extrude a curve along another curve"""
	result = rs.ExtrudeCurve(curve_id, path_id)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to extrude curve along curve"}


def extrude_curve_to_point(curve_id, point):
	"""Extrude a curve to a point"""
	result = rs.ExtrudeCurvePoint(curve_id, point)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to extrude curve to point"}


def duplicate_edge_curves(brep_id, select=False):
	"""Duplicate edge curves of a brep"""
	result = rs.DuplicateEdgeCurves(brep_id, select)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to duplicate edge curves"}


def duplicate_surface_border(surface_id):
	"""Duplicate surface border curves"""
	result = rs.DuplicateSurfaceBorder(surface_id)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to duplicate surface border"}


def join_surfaces(surface_ids, delete_input=True):
	"""Join multiple surfaces into a polysurface"""
	result = rs.JoinSurfaces(surface_ids, delete_input)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to join surfaces"}


def explode_polysurfaces(brep_id, delete_input=True):
	"""Explode a polysurface into individual surfaces"""
	result = rs.ExplodePolysurfaces(brep_id, delete_input)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to explode polysurface"}


def unroll_surface(surface_id):
	"""Unroll a surface"""
	result = rs.UnrollSurface(surface_id)
	if result:
		rs.Redraw()
		unrolled = result[0]
		curves = result[1] if len(result) > 1 else []
		ids = [str(unrolled)]
		if curves:
			ids.extend([str(c) for c in curves])
		return {"status": "success", "count": len(ids), "ids": ids}
	return {"status": "error", "message": "Failed to unroll surface"}
