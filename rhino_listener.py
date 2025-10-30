# Rhino Listener for MCP - COMPREHENSIVE Edition
# Compatible with IronPython 2.7 (Rhino 7)
# Includes 50+ commands for complete Rhino control

import socket
import threading
import json
import rhinoscriptsyntax as rs
import Rhino
import System

SERVER_HOST = "localhost"
SERVER_PORT = 54321
BUFFER_SIZE = 8192


# ============================================================================
# BASIC GEOMETRY CREATION
# ============================================================================

def create_point(params):
	"""Create a point"""
	x = params.get("x", 0)
	y = params.get("y", 0)
	z = params.get("z", 0)
	point_id = rs.AddPoint(x, y, z)
	if point_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(point_id), "type": "point"}}
	return {"status": "error", "message": "Failed to create point"}


def create_line(params):
	"""Create a line"""
	start = params.get("start", [0, 0, 0])
	end = params.get("end", [1, 1, 1])
	line_id = rs.AddLine(start, end)
	if line_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(line_id), "type": "line"}}
	return {"status": "error", "message": "Failed to create line"}


def create_circle(params):
	"""Create a circle"""
	center = params.get("center", [0, 0, 0])
	radius = params.get("radius", 5)
	circle_id = rs.AddCircle(center, radius)
	if circle_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(circle_id), "type": "circle"}}
	return {"status": "error", "message": "Failed to create circle"}


def create_arc(params):
	"""Create an arc through 3 points"""
	start = params.get("start", [0, 0, 0])
	mid = params.get("mid", [1, 1, 0])
	end = params.get("end", [2, 0, 0])
	arc_id = rs.AddArc3Pt(start, mid, end)
	if arc_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(arc_id), "type": "arc"}}
	return {"status": "error", "message": "Failed to create arc"}


def create_ellipse(params):
	"""Create an ellipse"""
	center = params.get("center", [0, 0, 0])
	radius_x = params.get("radius_x", 5)
	radius_y = params.get("radius_y", 3)
	plane = rs.PlaneFromNormal(center, (0, 0, 1))
	ellipse_id = rs.AddEllipse(plane, radius_x, radius_y)
	if ellipse_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(ellipse_id), "type": "ellipse"}}
	return {"status": "error", "message": "Failed to create ellipse"}


def create_polyline(params):
	"""Create a polyline"""
	points = params.get("points", [[0, 0, 0], [1, 1, 1], [2, 0, 0]])
	points_tuple = [tuple(pt) for pt in points]
	polyline_id = rs.AddPolyline(points_tuple)
	if polyline_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(polyline_id), "type": "polyline"}}
	return {"status": "error", "message": "Failed to create polyline"}


def create_curve(params):
	"""Create an interpolated curve"""
	points = params.get("points", [[0, 0, 0], [1, 1, 1], [2, 0, 0]])
	degree = params.get("degree", 3)
	points_tuple = [tuple(pt) for pt in points]
	curve_id = rs.AddInterpCurve(points_tuple, degree)
	if curve_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(curve_id), "type": "curve"}}
	return {"status": "error", "message": "Failed to create curve"}


# ============================================================================
# 3D SOLID CREATION
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

	box_id = rs.AddBox([p0, p1, p2, p3, p4, p5, p6, p7])
	if box_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(box_id), "type": "box"}}
	return {"status": "error", "message": "Failed to create box"}


def create_sphere(params):
	"""Create a sphere"""
	center = params.get("center", [0, 0, 0])
	radius = params.get("radius", 5)
	sphere_id = rs.AddSphere(center, radius)
	if sphere_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(sphere_id), "type": "sphere"}}
	return {"status": "error", "message": "Failed to create sphere"}


def create_cylinder(params):
	"""Create a cylinder"""
	base = params.get("base", [0, 0, 0])
	height = params.get("height", 10)
	radius = params.get("radius", 5)

	base_pt = tuple(base)
	top_pt = (base[0], base[1], base[2] + height)
	plane = rs.PlaneFromNormal(base_pt, (0, 0, 1))
	circle = rs.AddCircle(plane, radius)
	cylinder = rs.ExtrudeCurveStraight(circle, base_pt, top_pt)

	if cylinder:
		rs.DeleteObject(circle)
		rs.Redraw()
		return {"status": "success", "result": {"id": str(cylinder), "type": "cylinder"}}
	return {"status": "error", "message": "Failed to create cylinder"}


def create_cone(params):
	"""Create a cone"""
	base = params.get("base", [0, 0, 0])
	height = params.get("height", 10)
	radius = params.get("radius", 5)

	plane = rs.PlaneFromNormal(base, (0, 0, 1))
	cone_id = rs.AddCone(plane, height, radius)

	if cone_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(cone_id), "type": "cone"}}
	return {"status": "error", "message": "Failed to create cone"}


def create_torus(params):
	"""Create a torus"""
	center = params.get("center", [0, 0, 0])
	major_radius = params.get("major_radius", 10)
	minor_radius = params.get("minor_radius", 2)

	plane = rs.PlaneFromNormal(center, (0, 0, 1))
	torus_id = rs.AddTorus(plane, major_radius, minor_radius)

	if torus_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(torus_id), "type": "torus"}}
	return {"status": "error", "message": "Failed to create torus"}


# ============================================================================
# TRANSFORMATION OPERATIONS
# ============================================================================

def move_objects(params):
	"""Move selected objects by vector"""
	vector = params.get("vector", [0, 0, 0])
	objects = rs.SelectedObjects()

	if not objects:
		return {"status": "error", "message": "No objects selected"}

	for obj in objects:
		rs.MoveObject(obj, vector)

	rs.Redraw()
	return {"status": "success", "result": {"moved": len(objects)}}


def rotate_objects(params):
	"""Rotate selected objects around axis"""
	center = params.get("center", [0, 0, 0])
	angle = params.get("angle", 90)
	axis = params.get("axis", [0, 0, 1])

	objects = rs.SelectedObjects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	result_holder = [None]

	def do_rotate():
		result_holder[0] = rs.RotateObjects(objects, center, angle, axis)
		if result_holder[0]:
			rs.Redraw()

	# Execute on UI thread to avoid macOS threading issues
	Rhino.RhinoApp.InvokeOnUiThread(System.Action(do_rotate))

	if result_holder[0]:
		return {"status": "success", "result": {"count": len(result_holder[0])}}

	return {"status": "error", "message": "Failed to rotate objects"}


def scale_objects(params):
	"""Scale selected objects"""
	origin = params.get("origin", [0, 0, 0])
	factor = params.get("factor", 1.0)

	objects = rs.SelectedObjects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	scale = [factor, factor, factor]
	for obj in objects:
		rs.ScaleObject(obj, origin, scale)

	rs.Redraw()
	return {"status": "success", "result": {"scaled": len(objects)}}


def mirror_objects(params):
	"""Mirror selected objects"""
	plane_origin = params.get("plane_origin", [0, 0, 0])
	plane_normal = params.get("plane_normal", [1, 0, 0])

	objects = rs.SelectedObjects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	for obj in objects:
		rs.MirrorObject(obj, plane_origin, plane_normal)

	rs.Redraw()
	return {"status": "success", "result": {"mirrored": len(objects)}}


def copy_objects(params):
	"""Copy selected objects"""
	vector = params.get("vector", [10, 0, 0])

	objects = rs.SelectedObjects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	copied = []
	for obj in objects:
		new_obj = rs.CopyObject(obj, vector)
		copied.append(str(new_obj))

	rs.Redraw()
	return {"status": "success", "result": {"copied": len(copied), "ids": copied}}


def array_linear(params):
	"""Create linear array of selected objects"""
	vector = params.get("vector", [10, 0, 0])
	count = params.get("count", 3)

	objects = rs.SelectedObjects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	total_created = 0
	for obj in objects:
		for i in range(1, count):
			offset = [vector[j] * i for j in range(3)]
			rs.CopyObject(obj, offset)
			total_created += 1

	rs.Redraw()
	return {"status": "success", "result": {"created": total_created}}


# ============================================================================
# BOOLEAN OPERATIONS
# ============================================================================

def boolean_union(params):
	"""Boolean union of selected objects"""
	objects = rs.SelectedObjects()

	if not objects or len(objects) < 2:
		return {"status": "error", "message": "Need at least 2 objects selected"}

	polysurfaces = [obj for obj in objects if rs.IsPolysurface(obj) or rs.IsSurface(obj)]

	if len(polysurfaces) < 2:
		return {"status": "error", "message": "Need at least 2 solid objects selected"}

	polysurfaces = polysurfaces[-2:]

	try:
		result = rs.BooleanUnion(polysurfaces, True)
		if result:
			rs.UnselectAllObjects()
			rs.SelectObjects(result)
			rs.Redraw()
			return {"status": "success", "result": {"count": len(result)}}
	except Exception as e:
		return {"status": "error", "message": "Boolean union error: " + str(e)}

	return {"status": "error", "message": "Boolean union failed"}


def boolean_difference(params):
	"""Boolean difference - subtract second from first"""
	objects = rs.SelectedObjects()

	if not objects or len(objects) < 2:
		return {"status": "error", "message": "Need at least 2 objects selected"}

	polysurfaces = [obj for obj in objects if (rs.IsPolysurface(obj) or rs.IsSurface(obj)) and not rs.IsCurve(obj)]

	if len(polysurfaces) < 2:
		return {"status": "error", "message": "Need at least 2 solid objects selected"}

	polys_to_use = polysurfaces[-2:] if len(polysurfaces) >= 2 else polysurfaces

	try:
		result = rs.BooleanDifference([polys_to_use[0]], [polys_to_use[1]], True)
		if result and len(result) > 0:
			rs.UnselectAllObjects()
			rs.SelectObjects(result)
			rs.Redraw()
			return {"status": "success", "result": {"count": len(result)}}
		else:
			return {"status": "error", "message": "Boolean difference produced no results"}
	except Exception as e:
		return {"status": "error", "message": "Boolean difference error: " + str(e)}


def boolean_intersection(params):
	"""Boolean intersection of selected objects"""
	objects = rs.SelectedObjects()

	if not objects or len(objects) < 2:
		return {"status": "error", "message": "Need at least 2 objects selected"}

	polysurfaces = [obj for obj in objects if (rs.IsPolysurface(obj) or rs.IsSurface(obj)) and not rs.IsCurve(obj)]

	if len(polysurfaces) < 2:
		return {"status": "error", "message": "Need at least 2 solid objects selected"}

	polys_to_use = polysurfaces[-2:] if len(polysurfaces) >= 2 else polysurfaces

	try:
		result = rs.BooleanIntersection([polys_to_use[0]], [polys_to_use[1]], True)
		if result and len(result) > 0:
			rs.UnselectAllObjects()
			rs.SelectObjects(result)
			rs.Redraw()
			return {"status": "success", "result": {"count": len(result)}}
		else:
			return {"status": "error", "message": "Boolean intersection produced no results"}
	except Exception as e:
		return {"status": "error", "message": "Boolean intersection error: " + str(e)}


# ============================================================================
# CURVE OPERATIONS
# ============================================================================

def join_curves(params):
	"""Join selected curves"""
	objects = rs.SelectedObjects()

	if not objects:
		return {"status": "error", "message": "No objects selected"}

	curves = [obj for obj in objects if rs.IsCurve(obj)]

	if len(curves) < 2:
		return {"status": "error", "message": "Need at least 2 curves selected"}

	result = rs.JoinCurves(curves, True)
	if result:
		rs.UnselectAllObjects()
		rs.SelectObjects(result)
		rs.Redraw()
		return {"status": "success", "result": {"count": len(result)}}

	return {"status": "error", "message": "Failed to join curves"}


def explode_curves(params):
	"""Explode selected curves into segments"""
	objects = rs.SelectedObjects()

	if not objects:
		return {"status": "error", "message": "No objects selected"}

	total_segments = 0
	exploded_objects = []

	for obj in objects:
		if rs.IsCurve(obj):
			segments = rs.ExplodeCurves(obj, True)
			if segments:
				total_segments += len(segments)
				exploded_objects.extend(segments)

	if total_segments > 0:
		rs.UnselectAllObjects()
		if exploded_objects:
			rs.SelectObjects(exploded_objects)
		rs.Redraw()
		return {"status": "success", "result": {"count": total_segments}}

	return {"status": "error", "message": "No curves to explode"}


def offset_curve(params):
	"""Offset selected curve"""
	distance = params.get("distance", 5)
	point = params.get("point", None)

	curves = rs.SelectedObjects()
	if not curves:
		return {"status": "error", "message": "No curve selected"}

	curve = curves[0]

	if point:
		point = tuple(point)
	else:
		bbox = rs.BoundingBox(curve)
		if bbox:
			point = ((bbox[0][0] + bbox[6][0])/2, (bbox[0][1] + bbox[6][1])/2 + distance, bbox[0][2])

	result = rs.OffsetCurve(curve, point, distance)
	if result:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(result)}}

	return {"status": "error", "message": "Failed to offset curve"}


def fillet_curves(params):
	"""Fillet two selected curves"""
	radius = params.get("radius", 1)

	objects = rs.SelectedObjects()

	if not objects:
		return {"status": "error", "message": "No objects selected"}

	curves = [obj for obj in objects if rs.IsCurve(obj)]

	if len(curves) < 2:
		return {"status": "error", "message": "Need 2 curves selected"}

	try:
		if hasattr(rs, 'FilletCurves'):
			result = rs.FilletCurves(curves[0], curves[1], radius)
			if result:
				rs.Redraw()
				return {"status": "success", "result": {"created": True}}
		else:
			return {"status": "success", "result": {"created": False, "message": "FilletCurves not available in RhinoScriptSyntax"}}
	except:
		pass

	return {"status": "error", "message": "Fillet operation not supported"}


def extend_curve(params):
	"""Extend selected curve"""
	length = params.get("length", 5)
	side = params.get("side", 1)

	curves = rs.SelectedObjects()
	if not curves:
		return {"status": "error", "message": "No curve selected"}

	curve = curves[0]
	result = rs.ExtendCurveLength(curve, side, 0, length)

	if result:
		rs.Redraw()
		return {"status": "success", "result": {"extended": True}}

	return {"status": "error", "message": "Failed to extend curve"}


# ============================================================================
# SURFACE OPERATIONS
# ============================================================================

def extrude_curve_straight(params):
	"""Extrude curve straight"""
	direction = params.get("direction", [0, 0, 10])

	curves = rs.SelectedObjects()
	if not curves:
		return {"status": "error", "message": "No curve selected"}

	curve = curves[0]
	start = (0, 0, 0)
	end = tuple(direction)

	result = rs.ExtrudeCurveStraight(curve, start, end)
	if result:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(result)}}

	return {"status": "error", "message": "Failed to extrude curve"}


def revolve_curve(params):
	"""Revolve curve around axis"""
	axis_start = params.get("axis_start", [0, 0, 0])
	axis_end = params.get("axis_end", [0, 0, 10])
	angle = params.get("angle", 360)

	objects = rs.SelectedObjects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	curves = [obj for obj in objects if rs.IsCurve(obj)]

	if not curves:
		return {"status": "error", "message": "No curve selected"}

	curve = curves[0]

	try:
		axis_line = rs.AddLine(tuple(axis_start), tuple(axis_end))
		if not axis_line:
			return {"status": "error", "message": "Failed to create axis line"}

		# rs.AddRevSrf(curve, axis, start_angle, end_angle)
		result = rs.AddRevSrf(curve, axis_line, 0, angle)
		rs.DeleteObject(axis_line)

		if result:
			rs.Redraw()
			return {"status": "success", "result": {"id": str(result)}}
	except Exception as e:
		return {"status": "error", "message": "Revolve error: " + str(e)}

	return {"status": "error", "message": "Failed to revolve curve"}


def loft_curves(params):
	"""Loft surface through selected curves"""
	objects = rs.SelectedObjects()

	if not objects:
		return {"status": "error", "message": "No objects selected"}

	all_curves = [obj for obj in objects if rs.IsCurve(obj)]

	if len(all_curves) < 2:
		return {"status": "error", "message": "Need at least 2 curves selected"}

	# Use ALL curves, not just last 3
	curves = all_curves

	try:
		result = rs.AddLoftSrf(curves)
		if result and len(result) > 0:
			rs.UnselectAllObjects()
			rs.SelectObjects(result)
			rs.Redraw()
			return {"status": "success", "result": {"count": len(result)}}
		else:
			return {"status": "error", "message": "Loft produced no results"}
	except Exception as e:
		return {"status": "error", "message": "Loft error: " + str(e)}


# ============================================================================
# LAYER OPERATIONS
# ============================================================================

def create_layer(params):
	"""Create a new layer"""
	name = params.get("name", "NewLayer")
	color = params.get("color", None)

	if rs.IsLayer(name):
		return {"status": "success", "result": {"name": name, "already_exists": True}}

	if color:
		layer_id = rs.AddLayer(name, color=tuple(color))
	else:
		layer_id = rs.AddLayer(name)

	if layer_id:
		return {"status": "success", "result": {"name": name, "already_exists": False}}

	return {"status": "error", "message": "Failed to create layer"}


def delete_layer(params):
	"""Delete a layer"""
	name = params.get("name", "")

	if not rs.IsLayer(name):
		return {"status": "error", "message": "Layer does not exist: " + name}

	result = rs.DeleteLayer(name)
	if result:
		return {"status": "success", "result": {"deleted": name}}

	return {"status": "error", "message": "Failed to delete layer"}


def set_current_layer(params):
	"""Set the current active layer"""
	name = params.get("name", "")

	if not rs.IsLayer(name):
		return {"status": "error", "message": "Layer does not exist: " + name}

	rs.CurrentLayer(name)
	return {"status": "success", "result": {"current": name}}


def set_layer_color(params):
	"""Set layer color"""
	name = params.get("name", "")
	color = params.get("color", [0, 0, 0])

	if not rs.IsLayer(name):
		return {"status": "error", "message": "Layer does not exist: " + name}

	rs.LayerColor(name, tuple(color))
	rs.Redraw()
	return {"status": "success", "result": {"layer": name}}


def set_layer_visibility(params):
	"""Set layer visibility"""
	name = params.get("name", "")
	visible = params.get("visible", True)

	if not rs.IsLayer(name):
		return {"status": "error", "message": "Layer does not exist: " + name}

	rs.LayerVisible(name, visible)
	rs.Redraw()
	return {"status": "success", "result": {"layer": name, "visible": visible}}


def list_layers(params):
	"""List all layers"""
	layers = rs.LayerNames()
	current = rs.CurrentLayer()

	layers_list = []
	if layers:
		for layer in layers:
			layers_list.append({
				"name": layer,
				"visible": rs.LayerVisible(layer),
				"locked": rs.LayerLocked(layer),
				"current": (layer == current)
			})

	return {"status": "success", "result": {"count": len(layers_list), "layers": layers_list}}


# ============================================================================
# ANALYSIS OPERATIONS
# ============================================================================

def measure_distance(params):
	"""Measure distance between two points"""
	point1 = params.get("point1", [0, 0, 0])
	point2 = params.get("point2", [1, 1, 1])

	distance = rs.Distance(point1, point2)
	return {"status": "success", "result": {"distance": distance}}


def measure_curve_length(params):
	"""Measure length of selected curve"""
	objects = rs.SelectedObjects()

	if not objects:
		return {"status": "error", "message": "No objects selected"}

	curves = [obj for obj in objects if rs.IsCurve(obj)]

	if not curves:
		return {"status": "error", "message": "No curve selected"}

	curve = curves[0]
	length = rs.CurveLength(curve)

	if length is not None:
		return {"status": "success", "result": {"length": length}}

	return {"status": "error", "message": "Failed to measure curve"}


def measure_area(params):
	"""Measure area of selected surface or closed curve"""
	objects = rs.SelectedObjects()

	if not objects:
		return {"status": "error", "message": "No object selected"}

	obj = objects[0]

	try:
		if rs.IsCurve(obj) and rs.IsCurveClosed(obj) and rs.IsCurvePlanar(obj):
			area_result = rs.CurveArea(obj)
			if area_result:
				area_value = float(area_result[0]) if hasattr(area_result[0], '__float__') else area_result[0]
				return {"status": "success", "result": {"area": abs(area_value)}}

		if rs.IsSurface(obj) or rs.IsPolysurface(obj):
			area = rs.SurfaceArea(obj)
			if area:
				return {"status": "success", "result": {"area": area[0]}}
	except Exception as e:
		return {"status": "error", "message": "Error: " + str(e)}

	return {"status": "error", "message": "Failed to measure area"}


def measure_volume(params):
	"""Measure volume of selected solid"""
	objects = rs.SelectedObjects()

	if not objects:
		return {"status": "error", "message": "No object selected"}

	obj = objects[0]
	volume = rs.SurfaceVolume(obj)

	if volume:
		return {"status": "success", "result": {"volume": volume[0]}}

	return {"status": "error", "message": "Failed to measure volume"}


# ============================================================================
# OBJECT PROPERTIES
# ============================================================================

def set_object_name(params):
	"""Set name of selected object"""
	name = params.get("name", "")

	objects = rs.SelectedObjects()
	if not objects:
		return {"status": "error", "message": "No object selected"}

	for obj in objects:
		rs.ObjectName(obj, name)

	return {"status": "success", "result": {"named": len(objects)}}


def set_object_color(params):
	"""Set color of selected objects"""
	color = params.get("color", [255, 0, 0])

	objects = rs.SelectedObjects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	for obj in objects:
		rs.ObjectColor(obj, tuple(color))

	rs.Redraw()
	return {"status": "success", "result": {"colored": len(objects)}}


def set_object_layer(params):
	"""Move selected objects to layer"""
	layer = params.get("layer", "")

	if not rs.IsLayer(layer):
		return {"status": "error", "message": "Layer does not exist: " + layer}

	objects = rs.SelectedObjects()
	if not objects:
		return {"status": "error", "message": "No objects selected"}

	for obj in objects:
		rs.ObjectLayer(obj, layer)

	return {"status": "success", "result": {"moved": len(objects)}}


# ============================================================================
# SELECTION & QUERY OPERATIONS
# ============================================================================

def select_all(params):
	"""Select all objects"""
	objects = rs.AllObjects()
	if objects:
		rs.SelectObjects(objects)
		return {"status": "success", "result": {"count": len(objects)}}
	return {"status": "success", "result": {"count": 0}}


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

	type_filter = type_map.get(obj_type.lower(), 4)
	objects = rs.ObjectsByType(type_filter)

	if objects:
		rs.SelectObjects(objects)
		return {"status": "success", "result": {"count": len(objects)}}

	return {"status": "success", "result": {"count": 0}}


def select_by_layer(params):
	"""Select objects on specific layer"""
	layer = params.get("layer", "")

	if not rs.IsLayer(layer):
		return {"status": "error", "message": "Layer does not exist: " + layer}

	objects = rs.ObjectsByLayer(layer)
	if objects:
		rs.SelectObjects(objects)
		return {"status": "success", "result": {"count": len(objects)}}

	return {"status": "success", "result": {"count": 0}}


def unselect_all(params):
	"""Unselect all objects"""
	rs.UnselectAllObjects()
	return {"status": "success", "result": {"message": "All objects unselected"}}


def delete_selected(params):
	"""Delete selected objects"""
	objects = rs.SelectedObjects()
	if objects:
		count = len(objects)
		rs.DeleteObjects(objects)
		rs.Redraw()
		return {"status": "success", "result": {"deleted": count}}
	return {"status": "success", "result": {"deleted": 0}}


def get_selected_objects(params):
	"""Get information about selected objects"""
	objects = rs.SelectedObjects()
	type_names = {1: "Point", 2: "PointCloud", 4: "Curve", 8: "Surface", 16: "Polysurface", 32: "Mesh"}

	objects_list = []
	if objects:
		for obj in objects:
			obj_type = rs.ObjectType(obj)
			type_name = type_names.get(obj_type, "Other")

			bbox = rs.BoundingBox(obj)
			if bbox:
				center = [(bbox[0][i] + bbox[6][i]) / 2 for i in range(3)]
			else:
				center = [0, 0, 0]

			obj_info = {
				"id": str(obj),
				"type": type_name,
				"layer": rs.ObjectLayer(obj),
				"center": center
			}

			name = rs.ObjectName(obj)
			if name:
				obj_info["name"] = name

			objects_list.append(obj_info)

	return {"status": "success", "result": {"count": len(objects_list), "objects": objects_list}}


def get_scene_info(params):
	"""Get comprehensive scene information"""
	all_objects = rs.AllObjects()
	layers = rs.LayerNames()
	units = rs.UnitSystemName()

	obj_count = len(all_objects) if all_objects else 0
	layer_count = len(layers) if layers else 0

	type_counts = {}
	type_names = {1: "Point", 2: "PointCloud", 4: "Curve", 8: "Surface", 16: "Polysurface", 32: "Mesh"}

	objects_list = []
	if all_objects:
		for obj in all_objects[:30]:
			obj_type = rs.ObjectType(obj)
			type_name = type_names.get(obj_type, "Other")
			type_counts[type_name] = type_counts.get(type_name, 0) + 1

			bbox = rs.BoundingBox(obj)
			if bbox:
				center = [(bbox[0][i] + bbox[6][i]) / 2 for i in range(3)]
			else:
				center = [0, 0, 0]

			objects_list.append({
				"id": str(obj),
				"type": type_name,
				"layer": rs.ObjectLayer(obj),
				"center": center
			})

	result = {
		"total_objects": obj_count,
		"total_layers": layer_count,
		"units": str(units),
		"object_counts": type_counts,
		"objects": objects_list
	}

	return {"status": "success", "result": result}


# ============================================================================
# COMMAND MAPPING AND EXECUTION
# ============================================================================

def execute_command(command_dict):
	"""Execute JSON command and return JSON response"""
	try:
		cmd_type = command_dict.get("type", "")
		params = command_dict.get("params", {})

		command_map = {
			# Basic geometry
			"create_point": create_point,
			"create_line": create_line,
			"create_circle": create_circle,
			"create_arc": create_arc,
			"create_ellipse": create_ellipse,
			"create_polyline": create_polyline,
			"create_curve": create_curve,
			# 3D solids
			"create_box": create_box,
			"create_sphere": create_sphere,
			"create_cylinder": create_cylinder,
			"create_cone": create_cone,
			"create_torus": create_torus,
			# Transformations
			"move_objects": move_objects,
			"rotate_objects": rotate_objects,
			"scale_objects": scale_objects,
			"mirror_objects": mirror_objects,
			"copy_objects": copy_objects,
			"array_linear": array_linear,
			# Boolean operations
			"boolean_union": boolean_union,
			"boolean_difference": boolean_difference,
			"boolean_intersection": boolean_intersection,
			# Curve operations
			"join_curves": join_curves,
			"explode_curves": explode_curves,
			"offset_curve": offset_curve,
			"fillet_curves": fillet_curves,
			"extend_curve": extend_curve,
			# Surface operations
			"extrude_curve_straight": extrude_curve_straight,
			"revolve_curve": revolve_curve,
			"loft_curves": loft_curves,
			# Layer operations
			"create_layer": create_layer,
			"delete_layer": delete_layer,
			"set_current_layer": set_current_layer,
			"set_layer_color": set_layer_color,
			"set_layer_visibility": set_layer_visibility,
			"list_layers": list_layers,
			# Analysis
			"measure_distance": measure_distance,
			"measure_curve_length": measure_curve_length,
			"measure_area": measure_area,
			"measure_volume": measure_volume,
			# Object properties
			"set_object_name": set_object_name,
			"set_object_color": set_object_color,
			"set_object_layer": set_object_layer,
			# Selection
			"select_all": select_all,
			"select_by_type": select_by_type,
			"select_by_layer": select_by_layer,
			"unselect_all": unselect_all,
			"delete_selected": delete_selected,
			"get_selected_objects": get_selected_objects,
			"get_scene_info": get_scene_info
		}

		handler = command_map.get(cmd_type)
		if handler:
			return handler(params)
		else:
			return {"status": "error", "message": "Unknown command: " + cmd_type}

	except Exception as e:
		return {"status": "error", "message": "Error: " + str(e)}


# ============================================================================
# SOCKET SERVER
# ============================================================================

def handle_client(client_socket):
	"""Handle incoming client connection"""
	incomplete_data = ""

	try:
		while True:
			data = client_socket.recv(BUFFER_SIZE)
			if not data:
				break

			incomplete_data += data

			try:
				command = json.loads(incomplete_data)
				incomplete_data = ""

				response = execute_command(command)
				response_json = json.dumps(response)
				client_socket.send(response_json)
				break

			except ValueError:
				continue

	except Exception as e:
		error_msg = json.dumps({"status": "error", "message": "Connection error: " + str(e)})
		try:
			client_socket.send(error_msg)
		except:
			pass
	finally:
		try:
			client_socket.close()
		except:
			pass


def socket_server():
	"""Main socket server loop"""
	server_socket = None
	try:
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		server_socket.bind((SERVER_HOST, SERVER_PORT))
		server_socket.listen(5)

		print "=" * 60
		print "RhinoMCP Listener"
		print "=" * 60
		print "Active on " + SERVER_HOST + ":" + str(SERVER_PORT)
		print "49 commands available"
		print "JSON protocol"
		print "Ready to receive commands"
		print "=" * 60

		while True:
			try:
				client_socket, client_address = server_socket.accept()
				client_thread = threading.Thread(target=handle_client, args=(client_socket,))
				client_thread.daemon = True
				client_thread.start()
			except Exception as e:
				print "Connection error: " + str(e)
				continue

	except Exception as e:
		print "Failed to start listener: " + str(e)
	finally:
		if server_socket:
			try:
				server_socket.close()
			except:
				pass


# ============================================================================
# STARTUP
# ============================================================================

print "=" * 60
print "RhinoMCP Listener"
print "=" * 60
print "Starting background listener thread..."

listener_thread = threading.Thread(target=socket_server)
listener_thread.daemon = True
listener_thread.start()

print "Listener started successfully"
print "49 commands ready"
print "=" * 60
