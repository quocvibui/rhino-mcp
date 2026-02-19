"""
High-level command wrappers for Rhino operations
These functions accept params dict and handle common patterns like
working with selected objects, parameter extraction, etc.
Compatible with CPython 3 (Rhino 8)
"""

import math
import rhinoscriptsyntax as rs
import Rhino
import System
from io import StringIO

from . import curve, surface, geometry, layer, object as obj, selection, utility, plane, document
from . import mesh, group, view, block, material, annotation, userdata


# ============================================================================
# GEOMETRY COMMANDS
# ============================================================================

def create_point(params):
	"""Create a point"""
	x = params.get("x", 0)
	y = params.get("y", 0)
	z = params.get("z", 0)
	result = geometry.add_point(x, y, z)
	return {"status": result["status"], "result": {"id": result.get("id"), "type": "point"}} if result["status"] == "success" else result


def create_line(params):
	"""Create a line"""
	start = params.get("start", [0, 0, 0])
	end = params.get("end", [1, 1, 1])
	result = curve.add_line(start, end)
	return {"status": result["status"], "result": {"id": result.get("id"), "type": "line"}} if result["status"] == "success" else result


def create_circle(params):
	"""Create a circle"""
	center = params.get("center", [0, 0, 0])
	radius = params.get("radius", 5)
	result = curve.add_circle(center, radius)
	return {"status": result["status"], "result": {"id": result.get("id"), "type": "circle"}} if result["status"] == "success" else result


def create_arc(params):
	"""Create an arc with center, radius, and angles"""
	center = params.get("center", [0, 0, 0])
	radius = params.get("radius", 5)
	start_angle = params.get("start_angle", 0)
	end_angle = params.get("end_angle", 180)

	# Convert angles to 3 points for AddArc3Pt
	p = plane.plane_from_normal(center, [0, 0, 1])
	start_rad = math.radians(start_angle)
	end_rad = math.radians(end_angle)
	mid_angle = (start_rad + end_rad) / 2

	start_pt = [center[0] + radius * math.cos(start_rad),
				center[1] + radius * math.sin(start_rad),
				center[2]]
	end_pt = [center[0] + radius * math.cos(end_rad),
			  center[1] + radius * math.sin(end_rad),
			  center[2]]
	mid_pt = [center[0] + radius * math.cos(mid_angle),
			  center[1] + radius * math.sin(mid_angle),
			  center[2]]

	result = curve.add_arc_3pt(start_pt, mid_pt, end_pt)
	return {"status": result["status"], "result": {"id": result.get("id"), "type": "arc"}} if result["status"] == "success" else result


def create_ellipse(params):
	"""Create an ellipse"""
	center = params.get("center", [0, 0, 0])
	x_radius = params.get("x_radius", 5)
	y_radius = params.get("y_radius", 3)

	p = plane.plane_from_normal(center, (0, 0, 1))
	result = curve.add_ellipse(p, x_radius, y_radius)
	return {"status": result["status"], "result": {"id": result.get("id"), "type": "ellipse"}} if result["status"] == "success" else result


def create_polyline(params):
	"""Create a polyline"""
	points = params.get("points", [[0, 0, 0], [1, 1, 1], [2, 0, 0]])
	result = curve.add_polyline(points)
	return {"status": result["status"], "result": {"id": result.get("id"), "type": "polyline"}} if result["status"] == "success" else result


def create_curve(params):
	"""Create an interpolated curve"""
	points = params.get("points", [[0, 0, 0], [1, 1, 1], [2, 0, 0]])
	degree = params.get("degree", 3)
	result = curve.add_interp_curve(points, degree)
	return {"status": result["status"], "result": {"id": result.get("id"), "type": "curve"}} if result["status"] == "success" else result


# ============================================================================
# 3D SOLIDS
# ============================================================================

def create_box(params):
	"""Create a box"""
	width = params.get("width", 10)
	depth = params.get("depth", 10)
	height = params.get("height", 10)
	x = params.get("x", 0)
	y = params.get("y", 0)
	z = params.get("z", 0)

	p0 = (x, y, z)
	p1 = (x + width, y, z)
	p2 = (x + width, y + depth, z)
	p3 = (x, y + depth, z)
	p4 = (x, y, z + height)
	p5 = (x + width, y, z + height)
	p6 = (x + width, y + depth, z + height)
	p7 = (x, y + depth, z + height)

	result = surface.add_box([p0, p1, p2, p3, p4, p5, p6, p7])
	return {"status": result["status"], "result": {"id": result.get("id"), "type": "box"}} if result["status"] == "success" else result


def create_sphere(params):
	"""Create a sphere"""
	center = params.get("center", [0, 0, 0])
	radius = params.get("radius", 5)
	result = surface.add_sphere(center, radius)
	return {"status": result["status"], "result": {"id": result.get("id"), "type": "sphere"}} if result["status"] == "success" else result


def create_cylinder(params):
	"""Create a cylinder"""
	base = params.get("base", [0, 0, 0])
	height = params.get("height", 10)
	radius = params.get("radius", 5)

	# Create circle at base then extrude
	circle_id = rs.AddCircle(base, radius)
	if not circle_id:
		return {"status": "error", "message": "Failed to create base circle"}

	start = (0, 0, 0)
	end = (0, 0, height)
	result = surface.extrude_curve_straight(circle_id, start, end)

	return {"status": result["status"], "result": {"id": result.get("id"), "type": "cylinder"}} if result["status"] == "success" else result


def create_cone(params):
	"""Create a cone"""
	base = params.get("base", [0, 0, 0])
	height = params.get("height", 10)
	radius = params.get("radius", 5)

	height_point = [base[0], base[1], base[2] + height]
	result = surface.add_cone(base, height_point, radius)
	return {"status": result["status"], "result": {"id": result.get("id"), "type": "cone"}} if result["status"] == "success" else result


def create_torus(params):
	"""Create a torus"""
	center = params.get("center", [0, 0, 0])
	major_radius = params.get("major_radius", 10)
	minor_radius = params.get("minor_radius", 2)

	p = plane.plane_from_normal(center, (0, 0, 1))
	torus_id = rs.AddTorus(p, major_radius, minor_radius)

	if torus_id:
		document.redraw()
		return {"status": "success", "result": {"id": str(torus_id), "type": "torus"}}
	return {"status": "error", "message": "Failed to create torus"}


# ============================================================================
# TRANSFORMATIONS
# ============================================================================

def move_objects(params):
	"""Move selected objects"""
	displacement = params.get("displacement", [0, 0, 0])
	objects = selection.selected_objects()

	if not objects:
		return {"status": "error", "message": "No objects selected"}

	for obj_id in objects:
		obj.move_object(obj_id, displacement)

	return {"status": "success", "result": {"moved": len(objects)}}


def rotate_objects(params):
	"""Rotate selected objects"""
	center = params.get("center", [0, 0, 0])
	angle = params.get("angle", 90)
	axis = params.get("axis", [0, 0, 1])

	objects = selection.selected_objects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	# Already runs on UI thread via server.py InvokeOnUiThread dispatch
	result = rs.RotateObjects(objects, center, angle, axis)
	if result:
		document.redraw()
		return {"status": "success", "result": {"count": len(result)}}

	return {"status": "error", "message": "Failed to rotate objects"}


def scale_objects(params):
	"""Scale selected objects"""
	center = params.get("center", [0, 0, 0])
	scale_factor = params.get("scale", 1.0)

	objects = selection.selected_objects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	scale = [scale_factor, scale_factor, scale_factor]
	for obj_id in objects:
		obj.scale_object(obj_id, center, scale)

	return {"status": "success", "result": {"scaled": len(objects)}}


def mirror_objects(params):
	"""Mirror selected objects"""
	start = params.get("start", [0, 0, 0])
	end = params.get("end", [10, 0, 0])

	objects = selection.selected_objects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	for obj_id in objects:
		obj.mirror_object(obj_id, start, end)

	return {"status": "success", "result": {"mirrored": len(objects)}}


def copy_objects(params):
	"""Copy selected objects"""
	displacement = params.get("displacement", [10, 0, 0])

	objects = selection.selected_objects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	copied = []
	for obj_id in objects:
		result = obj.copy_object(obj_id, displacement)
		if result["status"] == "success":
			copied.append(result["id"])

	return {"status": "success", "result": {"copied": len(copied), "ids": copied}}


def array_linear(params):
	"""Create linear array"""
	displacement = params.get("displacement", [10, 0, 0])
	count = params.get("count", 3)

	objects = selection.selected_objects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	total_created = 0
	for obj_id in objects:
		for i in range(1, count):
			offset = [displacement[j] * i for j in range(3)]
			result = obj.copy_object(obj_id, offset)
			if result["status"] == "success":
				total_created += 1

	return {"status": "success", "result": {"created": total_created}}


# ============================================================================
# BOOLEAN OPERATIONS
# ============================================================================

def boolean_union(params):
	"""Boolean union on selected objects"""
	objects = selection.selected_objects()
	if not objects or len(objects) < 2:
		return {"status": "error", "message": "Need at least 2 objects selected"}

	# Filter to only polysurfaces and surfaces
	valid_objects = [o for o in objects if surface.is_polysurface(o) or surface.is_surface(o)]
	if len(valid_objects) < 2:
		return {"status": "error", "message": "Need at least 2 surfaces/polysurfaces"}

	result = surface.boolean_union(valid_objects)
	if result["status"] == "success":
		# Select the result for next operation
		selection.unselect_all_objects()
		if "ids" in result:
			selection.select_objects(result["ids"])
		return {"status": "success", "result": {"count": result.get("count", 0)}}
	return result


def boolean_difference(params):
	"""Boolean difference on selected objects"""
	objects = selection.selected_objects()
	if not objects or len(objects) < 2:
		return {"status": "error", "message": "Need at least 2 objects selected"}

	valid_objects = [o for o in objects if surface.is_polysurface(o) or surface.is_surface(o)]
	if len(valid_objects) < 2:
		return {"status": "error", "message": "Need at least 2 surfaces/polysurfaces"}

	result = surface.boolean_difference(valid_objects)
	if result["status"] == "success":
		# Select the result for next operation
		selection.unselect_all_objects()
		if "ids" in result:
			selection.select_objects(result["ids"])
		return {"status": "success", "result": {"count": result.get("count", 0)}}
	return result


def boolean_intersection(params):
	"""Boolean intersection on selected objects"""
	objects = selection.selected_objects()
	if not objects or len(objects) < 2:
		return {"status": "error", "message": "Need at least 2 objects selected"}

	valid_objects = [o for o in objects if surface.is_polysurface(o) or surface.is_surface(o)]
	if len(valid_objects) < 2:
		return {"status": "error", "message": "Need at least 2 surfaces/polysurfaces"}

	result = surface.boolean_intersection(valid_objects)
	if result["status"] == "success":
		# Select the result for next operation
		selection.unselect_all_objects()
		if "ids" in result:
			selection.select_objects(result["ids"])
		return {"status": "success", "result": {"count": result.get("count", 0)}}
	return result


# ============================================================================
# CURVE OPERATIONS
# ============================================================================

def join_curves(params):
	"""Join selected curves"""
	objects = selection.selected_objects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	curves = [o for o in objects if curve.is_curve(o)]
	if len(curves) < 2:
		return {"status": "error", "message": "Need at least 2 curves selected"}

	result = curve.join_curves(curves)
	if result["status"] == "success":
		# Select the joined curves for next operation
		selection.unselect_all_objects()
		if "ids" in result:
			selection.select_objects([result["ids"][i] for i in range(len(result["ids"]))])
		return {"status": "success", "result": {"count": result.get("count", 0)}}
	return result


def explode_curves(params):
	"""Explode selected curves"""
	objects = selection.selected_objects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	total_segments = 0
	exploded_objects = []

	for obj_id in objects:
		if curve.is_curve(obj_id):
			result = curve.explode_curves(obj_id, True)
			if result["status"] == "success":
				total_segments += result["count"]
				if "ids" in result:
					exploded_objects.extend(result["ids"])

	if total_segments > 0:
		# Select the exploded segments for next operation
		selection.unselect_all_objects()
		if exploded_objects:
			selection.select_objects(exploded_objects)
		return {"status": "success", "result": {"count": total_segments}}
	return {"status": "error", "message": "No curves to explode"}


def offset_curve(params):
	"""Offset selected curve"""
	distance = params.get("distance", 5)
	point = params.get("point", None)

	curves = selection.selected_objects()
	if not curves:
		return {"status": "error", "message": "No curve selected"}

	crv = curves[0]

	if point:
		point = tuple(point)
	else:
		bbox = geometry.bounding_box(crv)
		if bbox:
			point = ((bbox[0][0] + bbox[6][0])/2, (bbox[0][1] + bbox[6][1])/2 + distance, bbox[0][2])

	result = curve.offset_curve(crv, point, distance)
	if result["status"] == "success":
		return {"status": "success", "result": {"id": result["id"], "count": 1}}
	return result


def fillet_curves(params):
	"""Fillet two selected curves"""
	radius = params.get("radius", 1)
	objects = selection.selected_objects()

	if not objects:
		return {"status": "error", "message": "No objects selected"}

	curves_list = [o for o in objects if curve.is_curve(o)]
	if len(curves_list) < 2:
		return {"status": "error", "message": "Need 2 curves selected"}

	result = curve.add_fillet_curve(curves_list[0], curves_list[1], radius)
	if result["status"] == "success":
		return {"status": "success", "result": {"id": result["id"]}}
	return result


def extend_curve(params):
	"""Extend selected curve"""
	extension = params.get("extension", 5)
	side = params.get("side", 2)

	curves = selection.selected_objects()
	if not curves:
		return {"status": "error", "message": "No curve selected"}

	result = curve.extend_curve_length(curves[0], 2, side, extension)
	if result["status"] == "success":
		return {"status": "success", "result": {"extended": True, "id": result["id"]}}
	return result


# ============================================================================
# SURFACE OPERATIONS
# ============================================================================

def extrude_curve_straight(params):
	"""Extrude curve straight"""
	height = params.get("height", 10)

	curves = selection.selected_objects()
	if not curves:
		return {"status": "error", "message": "No curve selected"}

	crv = curves[0]
	start = (0, 0, 0)
	end = (0, 0, height)

	result = surface.extrude_curve_straight(crv, start, end)
	if result["status"] == "success":
		return {"status": "success", "result": {"id": result["id"]}}
	return result


def revolve_curve(params):
	"""Revolve curve around axis"""
	axis_start = params.get("axis_start", [0, 0, 0])
	axis_end = params.get("axis_end", [0, 0, 10])
	angle = params.get("angle", 360)

	objects = selection.selected_objects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	curves = [o for o in objects if curve.is_curve(o)]
	if not curves:
		return {"status": "error", "message": "No curve selected"}

	crv = curves[0]
	axis = [tuple(axis_start), tuple(axis_end)]

	result = surface.add_rev_srf(crv, axis, 0, angle)
	if result["status"] == "success":
		return {"status": "success", "result": {"id": result["id"], "count": 1}}
	return result


def loft_curves(params):
	"""Loft surface through selected curves"""
	objects = selection.selected_objects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	curves = [o for o in objects if curve.is_curve(o)]
	if len(curves) < 2:
		return {"status": "error", "message": "Need at least 2 curves"}

	result = surface.add_loft_srf(curves)
	if result["status"] == "success":
		# Select the lofted surface for next operation
		selection.unselect_all_objects()
		if "ids" in result:
			selection.select_objects(result["ids"])
		return {"status": "success", "result": {"count": result.get("count", 0)}}
	return result


# ============================================================================
# LAYER MANAGEMENT
# ============================================================================

def create_layer(params):
	"""Create a new layer"""
	name = params.get("name", "NewLayer")
	color = params.get("color", None)
	result = layer.add_layer(name, color)
	if result["status"] == "success":
		return {"status": "success", "result": {"name": result["name"]}}
	return result


def delete_layer(params):
	"""Delete a layer"""
	name = params.get("name", "")
	result = layer.delete_layer(name)
	if result["status"] == "success":
		return {"status": "success", "result": {"deleted": name}}
	return result


def set_current_layer(params):
	"""Set current layer"""
	name = params.get("name", "")
	result = layer.current_layer(name)
	if result["status"] == "success":
		return {"status": "success", "result": {"current": result["name"]}}
	return result


def set_layer_color(params):
	"""Set layer color"""
	name = params.get("name", "")
	color = params.get("color", [0, 0, 0])
	result = layer.layer_color(name, color)
	if result["status"] == "success":
		return {"status": "success", "result": {"layer": name}}
	return result


def set_layer_visibility(params):
	"""Set layer visibility"""
	name = params.get("name", "")
	visible = params.get("visible", True)
	result = layer.layer_visible(name, visible)
	if result["status"] == "success":
		return {"status": "success", "result": {"layer": name, "visible": visible}}
	return result


def list_layers(params):
	"""List all layers"""
	layers = layer.layer_names()
	layer_info = []

	for lyr in layers:
		info = {
			"name": lyr,
			"visible": layer.layer_visible(lyr),
			"locked": layer.layer_locked(lyr),
			"current": lyr == layer.current_layer()
		}
		layer_info.append(info)

	return {"status": "success", "result": {"layers": layer_info}}


# ============================================================================
# ANALYSIS
# ============================================================================

def measure_distance(params):
	"""Measure distance between two points"""
	point1 = params.get("point1", [0, 0, 0])
	point2 = params.get("point2", [1, 1, 1])
	result = utility.distance(point1, point2)
	if result["status"] == "success":
		return {"status": "success", "result": {"distance": result["distance"]}}
	return result


def measure_curve_length(params):
	"""Measure curve length"""
	curves = selection.selected_objects()
	if not curves:
		return {"status": "error", "message": "No curve selected"}

	result = curve.curve_length(curves[0])
	if result["status"] == "success":
		return {"status": "success", "result": {"length": result["length"]}}
	return result


def measure_area(params):
	"""Measure area of closed planar curve or surface"""
	objects = selection.selected_objects()
	if not objects:
		return {"status": "error", "message": "No object selected"}

	obj_id = objects[0]

	if curve.is_curve(obj_id):
		result = curve.curve_area(obj_id)
		if result["status"] == "success":
			return {"status": "success", "result": {"area": result["area"]}}
		return result
	elif surface.is_surface(obj_id):
		result = surface.surface_area(obj_id)
		if result["status"] == "success":
			return {"status": "success", "result": {"area": result["area"]}}
		return result

	return {"status": "error", "message": "Object must be a closed planar curve or surface"}


def measure_volume(params):
	"""Measure volume of closed surface"""
	objects = selection.selected_objects()
	if not objects:
		return {"status": "error", "message": "No object selected"}

	result = surface.surface_volume(objects[0])
	if result["status"] == "success":
		return {"status": "success", "result": {"volume": result["volume"]}}
	return result


def get_scene_info(params):
	"""Get scene information"""
	all_objs = selection.all_objects()
	layers = layer.layer_names()

	obj_types = {}
	for obj_id in all_objs:
		obj_type = obj.object_type(obj_id)
		obj_types[obj_type] = obj_types.get(obj_type, 0) + 1

	return {
		"status": "success",
		"result": {
			"object_count": len(all_objs),
			"layer_count": len(layers),
			"layers": layers,
			"object_types": obj_types,
			"unit_system": document.unit_system_name()
		}
	}


def get_selected_objects(params):
	"""Get selected objects info"""
	objects = selection.selected_objects()

	if not objects:
		return {"status": "success", "result": {"count": 0, "objects": []}}

	obj_info = []
	for obj_id in objects:
		info = {
			"id": str(obj_id),
			"type": obj.object_type(obj_id),
			"layer": obj.object_layer(obj_id),
			"name": obj.object_name(obj_id)
		}
		bbox = geometry.bounding_box(obj_id)
		if bbox:
			info["bounding_box"] = [[p[0], p[1], p[2]] for p in bbox]
		obj_info.append(info)

	return {"status": "success", "result": {"count": len(objects), "objects": obj_info}}


# ============================================================================
# SELECTION
# ============================================================================

def select_all(params):
	"""Select all objects"""
	all_objs = selection.all_objects()
	if all_objs:
		selection.select_objects(all_objs)
		return {"status": "success", "result": {"count": len(all_objs)}}
	return {"status": "success", "result": {"count": 0}}


def unselect_all(params):
	"""Unselect all objects"""
	selection.unselect_all_objects()
	return {"status": "success", "result": {"message": "All objects unselected"}}


def select_by_type(params):
	"""Select objects by type"""
	obj_type = params.get("type", "curve")

	type_map = {
		"point": 1,
		"curve": 4,
		"surface": 8,
		"polysurface": 16,
		"mesh": 32
	}

	type_id = type_map.get(obj_type, 4)
	objects = selection.objects_by_type(type_id)

	if objects:
		selection.select_objects(objects)
		return {"status": "success", "result": {"count": len(objects)}}
	return {"status": "success", "result": {"count": 0}}


def select_by_layer(params):
	"""Select objects by layer"""
	layer_name = params.get("layer", "")

	if not layer.is_layer(layer_name):
		return {"status": "error", "message": "Layer does not exist"}

	objects = selection.objects_by_layer(layer_name)
	if objects:
		selection.select_objects(objects)
		return {"status": "success", "result": {"count": len(objects)}}
	return {"status": "success", "result": {"count": 0}}


def delete_selected(params):
	"""Delete selected objects"""
	objects = selection.selected_objects()
	if not objects:
		return {"status": "success", "result": {"deleted": 0}}

	count = len(objects)
	result = obj.delete_objects(objects)
	if result["status"] == "success":
		return {"status": "success", "result": {"deleted": count}}
	return result


def set_object_name(params):
	"""Set object name"""
	name = params.get("name", "")
	objects = selection.selected_objects()

	if not objects:
		return {"status": "error", "message": "No objects selected"}

	for obj_id in objects:
		obj.object_name(obj_id, name)

	return {"status": "success", "result": {"count": len(objects)}}


def set_object_color(params):
	"""Set object color"""
	color = params.get("color", [255, 0, 0])
	objects = selection.selected_objects()

	if not objects:
		return {"status": "error", "message": "No objects selected"}

	for obj_id in objects:
		obj.object_color(obj_id, color)

	return {"status": "success", "result": {"count": len(objects)}}


def set_object_layer(params):
	"""Set object layer"""
	layer_name = params.get("layer", "")

	if not layer.is_layer(layer_name):
		return {"status": "error", "message": "Layer does not exist"}

	objects = selection.selected_objects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	for obj_id in objects:
		obj.object_layer(obj_id, layer_name)

	return {"status": "success", "result": {"count": len(objects)}}


# ============================================================================
# NEW SURFACE OPERATIONS (Phase 1)
# ============================================================================

def create_pipe(params):
	"""Create a pipe along a curve"""
	curve_id = params.get("curve_id")
	radius = params.get("radius", 1)
	cap = params.get("cap", 1)
	result = surface.add_pipe(curve_id, [0, 1], [radius, radius], cap)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def sweep1(params):
	"""Sweep shapes along one rail"""
	rail = params.get("rail")
	shapes = params.get("shapes", [])
	result = surface.add_sweep1(rail, shapes)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def sweep2(params):
	"""Sweep shapes along two rails"""
	rails = params.get("rails", [])
	shapes = params.get("shapes", [])
	result = surface.add_sweep2(rails, shapes)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def create_planar_surface(params):
	"""Create planar surface from curves"""
	curve_ids = params.get("curve_ids", [])
	result = surface.add_planar_srf(curve_ids)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def create_edge_surface(params):
	"""Create edge surface"""
	curve_ids = params.get("curve_ids", [])
	result = surface.add_edge_srf(curve_ids)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def create_network_surface(params):
	"""Create network surface"""
	curve_ids = params.get("curve_ids", [])
	continuity = params.get("continuity", 1)
	result = surface.add_network_srf(curve_ids, continuity)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def create_patch(params):
	"""Create patch surface"""
	object_ids = params.get("object_ids", [])
	uspan = params.get("uspan", 10)
	vspan = params.get("vspan", 10)
	result = surface.add_patch(object_ids, uspan, vspan)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def offset_surface(params):
	"""Offset a surface"""
	surface_id = params.get("surface_id")
	distance = params.get("distance", 1)
	result = surface.offset_surface(surface_id, distance)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def split_brep(params):
	"""Split a brep"""
	brep_id = params.get("brep_id")
	cutter_id = params.get("cutter_id")
	result = surface.split_brep(brep_id, cutter_id)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def fillet_surfaces(params):
	"""Fillet between two surfaces"""
	srf1 = params.get("surface1_id")
	srf2 = params.get("surface2_id")
	radius = params.get("radius", 1)
	result = surface.fillet_surfaces(srf1, srf2, radius)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def cap_planar_holes(params):
	"""Cap planar holes"""
	brep_id = params.get("brep_id")
	result = surface.cap_planar_holes(brep_id)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def extrude_curve_along_curve(params):
	"""Extrude curve along another curve"""
	curve_id = params.get("curve_id")
	path_id = params.get("path_id")
	result = surface.extrude_curve_along_curve(curve_id, path_id)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def extrude_curve_to_point(params):
	"""Extrude curve to a point"""
	curve_id = params.get("curve_id")
	point = params.get("point", [0, 0, 10])
	result = surface.extrude_curve_to_point(curve_id, point)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def duplicate_edge_curves(params):
	"""Duplicate edge curves of a brep"""
	brep_id = params.get("brep_id")
	result = surface.duplicate_edge_curves(brep_id)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def duplicate_surface_border(params):
	"""Duplicate surface border"""
	surface_id = params.get("surface_id")
	result = surface.duplicate_surface_border(surface_id)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def join_surfaces(params):
	"""Join surfaces"""
	surface_ids = params.get("surface_ids", [])
	result = surface.join_surfaces(surface_ids)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def explode_polysurfaces(params):
	"""Explode polysurfaces"""
	brep_id = params.get("brep_id")
	result = surface.explode_polysurfaces(brep_id)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def unroll_surface(params):
	"""Unroll a surface"""
	surface_id = params.get("surface_id")
	result = surface.unroll_surface(surface_id)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


# ============================================================================
# NEW CURVE OPERATIONS (Phase 1)
# ============================================================================

def create_rectangle(params):
	"""Create a rectangle"""
	center = params.get("center", [0, 0, 0])
	width = params.get("width", 10)
	height = params.get("height", 10)
	p = plane.plane_from_normal(center, (0, 0, 1))
	result = curve.add_rectangle(p, width, height)
	if result["status"] == "success":
		return {"status": "success", "result": {"id": result["id"], "type": "rectangle"}}
	return result


def create_spiral(params):
	"""Create a spiral"""
	point0 = params.get("point0", [0, 0, 0])
	point1 = params.get("point1", [0, 0, 10])
	pitch = params.get("pitch", 1)
	turns = params.get("turns", 5)
	radius0 = params.get("radius0", 5)
	radius1 = params.get("radius1", 5)
	result = curve.add_spiral(point0, point1, pitch, turns, radius0, radius1)
	if result["status"] == "success":
		return {"status": "success", "result": {"id": result["id"], "type": "spiral"}}
	return result


def create_nurbs_curve(params):
	"""Create a NURBS curve"""
	points = params.get("points", [])
	degree = params.get("degree", 3)
	points_tuple = [tuple(pt) for pt in points]
	# Generate uniform knot vector
	n = len(points_tuple)
	knot_count = n + degree - 1
	knots = [i for i in range(knot_count)]
	result = curve.add_nurbs_curve(points_tuple, knots, degree)
	if result["status"] == "success":
		return {"status": "success", "result": {"id": result["id"], "type": "nurbs_curve"}}
	return result


def create_blend_curve(params):
	"""Create a blend curve"""
	curve1 = params.get("curve1")
	curve2 = params.get("curve2")
	continuity = params.get("continuity", 1)
	result = curve.add_blend_curve(
		[curve1, curve2],
		[rs.CurveDomain(curve1)[1], rs.CurveDomain(curve2)[0]],
		[False, True],
		[continuity, continuity]
	)
	if result["status"] == "success":
		return {"status": "success", "result": {"id": result["id"], "type": "blend_curve"}}
	return result


def divide_curve_cmd(params):
	"""Divide a curve into segments"""
	curve_id = params.get("curve_id")
	segments = params.get("segments", 10)
	create_points = params.get("create_points", True)
	result = curve.divide_curve(curve_id, segments, create_points)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def divide_curve_length_cmd(params):
	"""Divide curve by length"""
	curve_id = params.get("curve_id")
	length = params.get("length", 1)
	create_points = params.get("create_points", True)
	result = curve.divide_curve_length(curve_id, length, create_points)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def split_curve(params):
	"""Split a curve at parameters"""
	curve_id = params.get("curve_id")
	parameters = params.get("parameters", [])
	result = curve.split_curve(curve_id, parameters)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def close_curve(params):
	"""Close an open curve"""
	curve_id = params.get("curve_id")
	result = curve.close_curve(curve_id)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def reverse_curve(params):
	"""Reverse curve direction"""
	curve_id = params.get("curve_id")
	result = curve.reverse_curve(curve_id)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def rebuild_curve(params):
	"""Rebuild a curve"""
	curve_id = params.get("curve_id")
	degree = params.get("degree", 3)
	point_count = params.get("point_count", 10)
	result = curve.rebuild_curve(curve_id, degree, point_count)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def project_curve_to_surface(params):
	"""Project curves onto surfaces"""
	curve_ids = params.get("curve_ids", [])
	surface_ids = params.get("surface_ids", [])
	direction = params.get("direction", [0, 0, -1])
	result = curve.project_curve_to_surface(curve_ids, surface_ids, direction)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


# ============================================================================
# CURVE ANALYSIS (Phase 5)
# ============================================================================

def curve_closest_point(params):
	"""Find closest point on curve"""
	curve_id = params.get("curve_id")
	point = params.get("point", [0, 0, 0])
	result = curve.curve_closest_point(curve_id, point)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def evaluate_curve(params):
	"""Evaluate curve at parameter"""
	curve_id = params.get("curve_id")
	parameter = params.get("parameter", 0)
	result = curve.evaluate_curve(curve_id, parameter)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def curve_start_end_points(params):
	"""Get curve start/end points"""
	curve_id = params.get("curve_id")
	result = curve.curve_start_end_points(curve_id)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def curve_curve_intersection(params):
	"""Find curve-curve intersections"""
	curve1 = params.get("curve1")
	curve2 = params.get("curve2")
	result = curve.curve_curve_intersection(curve1, curve2)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


# ============================================================================
# MESH OPERATIONS (Phase 2)
# ============================================================================

def create_mesh(params):
	"""Create a mesh"""
	vertices = params.get("vertices", [])
	faces = params.get("faces", [])
	result = mesh.add_mesh(vertices, faces)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def create_planar_mesh(params):
	"""Create a planar mesh from a closed curve"""
	curve_id = params.get("curve_id")
	result = mesh.add_planar_mesh(curve_id)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def mesh_from_surface(params):
	"""Mesh brep/surface objects"""
	object_ids = params.get("object_ids", [])
	result = mesh.mesh_objects(object_ids)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def mesh_boolean_union(params):
	"""Mesh boolean union"""
	mesh_ids = params.get("mesh_ids", [])
	result = mesh.mesh_boolean_union(mesh_ids)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def mesh_boolean_difference(params):
	"""Mesh boolean difference"""
	input_ids = params.get("input_ids", [])
	subtract_ids = params.get("subtract_ids", [])
	result = mesh.mesh_boolean_difference(input_ids, subtract_ids)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def mesh_boolean_intersection(params):
	"""Mesh boolean intersection"""
	mesh_ids1 = params.get("mesh_ids1", [])
	mesh_ids2 = params.get("mesh_ids2", [])
	result = mesh.mesh_boolean_intersection(mesh_ids1, mesh_ids2)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def join_meshes(params):
	"""Join meshes"""
	mesh_ids = params.get("mesh_ids", [])
	result = mesh.join_meshes(mesh_ids)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def mesh_to_nurb(params):
	"""Convert mesh to NURBS"""
	mesh_id = params.get("mesh_id")
	result = mesh.mesh_to_nurb(mesh_id)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def mesh_offset(params):
	"""Offset a mesh"""
	mesh_id = params.get("mesh_id")
	distance = params.get("distance", 1)
	result = mesh.mesh_offset(mesh_id, distance)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


# ============================================================================
# GROUP OPERATIONS (Phase 2)
# ============================================================================

def create_group(params):
	"""Create a group"""
	name = params.get("name")
	object_ids = params.get("object_ids", [])
	result = group.add_group(name)
	if result["status"] == "success" and object_ids:
		group.add_objects_to_group(object_ids, result["name"])
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def delete_group(params):
	"""Delete a group"""
	name = params.get("name")
	result = group.delete_group(name)
	if result["status"] == "success":
		return {"status": "success", "result": {"deleted": name}}
	return result


def add_to_group(params):
	"""Add objects to a group"""
	name = params.get("name")
	object_ids = params.get("object_ids", [])
	result = group.add_objects_to_group(object_ids, name)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def remove_from_group(params):
	"""Remove objects from a group"""
	name = params.get("name")
	object_ids = params.get("object_ids", [])
	result = group.remove_objects_from_group(object_ids, name)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def list_groups(params):
	"""List all groups"""
	result = group.group_names()
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def select_by_group(params):
	"""Select objects by group"""
	name = params.get("name")
	result = group.objects_by_group(name)
	if result["status"] == "success" and result["ids"]:
		selection.select_objects(result["ids"])
	return {"status": "success", "result": result}


# ============================================================================
# VIEW OPERATIONS (Phase 3)
# ============================================================================

def set_view_camera(params):
	"""Set view camera"""
	camera = params.get("camera", [0, 0, 50])
	target = params.get("target", [0, 0, 0])
	result = view.set_view_camera(camera, target)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def zoom_extents(params):
	"""Zoom to extents"""
	result = view.zoom_extents()
	return {"status": "success", "result": result}


def zoom_selected(params):
	"""Zoom to selected"""
	result = view.zoom_selected()
	return {"status": "success", "result": result}


def get_view_info(params):
	"""Get view info"""
	result = view.get_view_info()
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def set_display_mode(params):
	"""Set display mode"""
	mode = params.get("mode", "Shaded")
	result = view.set_display_mode(mode)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def add_named_view(params):
	"""Add a named view"""
	name = params.get("name")
	result = view.add_named_view(name)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def restore_named_view(params):
	"""Restore a named view"""
	name = params.get("name")
	result = view.restore_named_view(name)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


# ============================================================================
# BLOCK OPERATIONS (Phase 3)
# ============================================================================

def create_block(params):
	"""Create a block definition"""
	object_ids = params.get("object_ids", [])
	base_point = params.get("base_point", [0, 0, 0])
	name = params.get("name")
	result = block.add_block(object_ids, base_point, name)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def insert_block(params):
	"""Insert a block instance"""
	name = params.get("name")
	point = params.get("point", [0, 0, 0])
	scale = params.get("scale", [1, 1, 1])
	rotation = params.get("rotation", 0)
	result = block.insert_block(name, point, tuple(scale), rotation)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def explode_block(params):
	"""Explode a block instance"""
	block_id = params.get("block_id")
	result = block.explode_block_instance(block_id)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def delete_block(params):
	"""Delete a block definition"""
	name = params.get("name")
	result = block.delete_block(name)
	if result["status"] == "success":
		return {"status": "success", "result": {"deleted": name}}
	return result


def list_blocks(params):
	"""List block definitions"""
	result = block.block_names()
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


# ============================================================================
# MATERIAL OPERATIONS (Phase 3)
# ============================================================================

def add_material_to_object(params):
	"""Add material to object"""
	object_id = params.get("object_id")
	color = params.get("color", [255, 255, 255])
	result = material.add_material_to_object(object_id)
	if result["status"] == "success":
		material.material_color(result["index"], color)
		return {"status": "success", "result": {"index": result["index"]}}
	return result


def add_material_to_layer(params):
	"""Add material to layer"""
	layer_name = params.get("layer_name")
	result = material.add_material_to_layer(layer_name)
	if result["status"] == "success":
		return {"status": "success", "result": {"index": result["index"]}}
	return result


def set_material_color(params):
	"""Set material color"""
	object_id = params.get("object_id")
	color = params.get("color", [255, 255, 255])
	index = rs.ObjectMaterialIndex(object_id)
	if index < 0:
		return {"status": "error", "message": "Object has no material. Add one first."}
	result = material.material_color(index, color)
	return {"status": "success", "result": result}


def set_material_transparency(params):
	"""Set material transparency"""
	object_id = params.get("object_id")
	transparency = params.get("transparency", 0)
	index = rs.ObjectMaterialIndex(object_id)
	if index < 0:
		return {"status": "error", "message": "Object has no material. Add one first."}
	result = material.material_transparency(index, transparency)
	return {"status": "success", "result": result}


def set_material_shine(params):
	"""Set material shine"""
	object_id = params.get("object_id")
	shine = params.get("shine", 0)
	index = rs.ObjectMaterialIndex(object_id)
	if index < 0:
		return {"status": "error", "message": "Object has no material. Add one first."}
	result = material.material_shine(index, shine)
	return {"status": "success", "result": result}


# ============================================================================
# OBJECT OPERATIONS (Phase 4)
# ============================================================================

def hide_objects(params):
	"""Hide selected objects"""
	objects = selection.selected_objects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}
	result = obj.hide_objects(objects)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def show_objects(params):
	"""Show hidden objects"""
	object_ids = params.get("object_ids", [])
	if object_ids:
		result = obj.show_objects(object_ids)
	else:
		# Show all hidden objects
		hidden = rs.HiddenObjects()
		if hidden:
			result = obj.show_objects(hidden)
		else:
			return {"status": "success", "result": {"count": 0}}
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def lock_objects(params):
	"""Lock selected objects"""
	objects = selection.selected_objects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}
	result = obj.lock_objects(objects)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def unlock_objects(params):
	"""Unlock locked objects"""
	object_ids = params.get("object_ids", [])
	if object_ids:
		result = obj.unlock_objects(object_ids)
	else:
		locked = rs.LockedObjects()
		if locked:
			result = obj.unlock_objects(locked)
		else:
			return {"status": "success", "result": {"count": 0}}
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def is_object_solid(params):
	"""Check if object is solid"""
	object_id = params.get("object_id")
	result = obj.is_object_solid(object_id)
	return {"status": "success", "result": result}


# ============================================================================
# SELECTION OPERATIONS (Phase 4)
# ============================================================================

def select_by_name(params):
	"""Select objects by name"""
	name = params.get("name", "")
	objects = selection.objects_by_name(name)
	if objects:
		selection.select_objects(objects)
		return {"status": "success", "result": {"count": len(objects)}}
	return {"status": "success", "result": {"count": 0}}


def last_created_objects(params):
	"""Select last created objects"""
	objects = selection.last_created_objects(select=True)
	return {"status": "success", "result": {"count": len(objects), "ids": objects}}


def invert_selection(params):
	"""Invert selection"""
	count = selection.invert_selected_objects()
	return {"status": "success", "result": {"count": count}}


# ============================================================================
# DOCUMENT OPERATIONS (Phase 4)
# ============================================================================

def get_document_info(params):
	"""Get document info"""
	return {
		"status": "success",
		"result": {
			"name": document.document_name(),
			"path": document.document_path(),
			"units": document.unit_system_name(),
			"unit_system": document.unit_system()
		}
	}


def set_unit_system(params):
	"""Set unit system"""
	system = params.get("system", 4)
	document.unit_system(system)
	return {"status": "success", "result": {"system": system}}


def enable_redraw(params):
	"""Enable/disable redraw"""
	enable = params.get("enable", True)
	document.enable_redraw(enable)
	return {"status": "success", "result": {"enabled": enable}}


# ============================================================================
# TRANSFORM OPERATIONS (Phase 4)
# ============================================================================

def array_polar(params):
	"""Create polar array"""
	center = params.get("center", [0, 0, 0])
	count = params.get("count", 6)
	total_angle = params.get("angle", 360)

	objects = selection.selected_objects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	angle_step = total_angle / count
	total_created = 0

	for obj_id in objects:
		for i in range(1, count):
			new_id = rs.CopyObject(obj_id)
			if new_id:
				rs.RotateObject(new_id, center, angle_step * i)
				total_created += 1

	document.redraw()
	return {"status": "success", "result": {"created": total_created}}


def orient_objects(params):
	"""Orient objects from reference to target (translation)"""
	reference = params.get("reference", [0, 0, 0])
	target = params.get("target", [10, 0, 0])

	objects = selection.selected_objects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	# rs.OrientObject needs at least 2 reference and 2 target points
	ref_pts = [reference, [reference[0] + 1, reference[1], reference[2]]]
	tgt_pts = [target, [target[0] + 1, target[1], target[2]]]

	count = 0
	for obj_id in objects:
		result = obj.orient_object(obj_id, ref_pts, tgt_pts)
		if result and result.get("status") == "success":
			count += 1

	return {"status": "success", "result": {"count": count}}


# ============================================================================
# ANNOTATION OPERATIONS (Phase 4)
# ============================================================================

def add_text(params):
	"""Add text"""
	text = params.get("text", "")
	point = params.get("point", [0, 0, 0])
	height = params.get("height", 1.0)
	font = params.get("font", None)
	result = annotation.add_text(text, point, height, font)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def add_text_dot(params):
	"""Add text dot"""
	text = params.get("text", "")
	point = params.get("point", [0, 0, 0])
	result = annotation.add_text_dot(text, point)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def add_leader(params):
	"""Add leader"""
	points = params.get("points", [])
	text = params.get("text", "")
	points_tuple = [tuple(pt) for pt in points]
	result = annotation.add_leader(points_tuple, text)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


# ============================================================================
# USER DATA OPERATIONS (Phase 5)
# ============================================================================

def set_user_text(params):
	"""Set user text on object"""
	object_id = params.get("object_id")
	key = params.get("key")
	value = params.get("value")
	result = userdata.set_user_text(object_id, key, value)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def get_user_text(params):
	"""Get user text from object"""
	object_id = params.get("object_id")
	key = params.get("key", None)
	result = userdata.get_user_text(object_id, key)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def set_document_user_text(params):
	"""Set document user text"""
	key = params.get("key")
	value = params.get("value")
	result = userdata.set_document_user_text(key, value)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


def get_document_user_text(params):
	"""Get document user text"""
	key = params.get("key", None)
	result = userdata.get_document_user_text(key)
	if result["status"] == "success":
		return {"status": "success", "result": result}
	return result


# ============================================================================
# CODE EXECUTION
# ============================================================================

def execute_python_code(params):
	"""Execute arbitrary Python code with access to rhinoscriptsyntax"""
	code = params.get("code", "")

	if not code:
		return {"status": "error", "message": "No code provided"}

	try:
		import sys

		# Capture stdout
		old_stdout = sys.stdout
		sys.stdout = StringIO()

		# Create namespace with rhinoscriptsyntax and common modules
		namespace = {
			"rs": rs,
			"rhinoscriptsyntax": rs,
			"Rhino": Rhino,
			"System": System,
			"math": math,
			"__builtins__": __builtins__
		}

		# Execute code
		exec(code, namespace)

		# Get output
		output = sys.stdout.getvalue()
		sys.stdout = old_stdout

		# Redraw
		document.redraw()

		return {"status": "success", "result": {"message": "Code executed successfully", "output": output}}

	except Exception as e:
		if 'old_stdout' in locals():
			sys.stdout = old_stdout
		return {"status": "error", "message": "Execution error: {0}".format(str(e))}
