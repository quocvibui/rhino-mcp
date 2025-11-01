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
