"""
RhinoScriptSyntax curve functions
Direct wrappers around rs.Add*, rs.Curve*, etc.
"""

import rhinoscriptsyntax as rs


def add_line(start, end):
	"""Add a line curve"""
	line_id = rs.AddLine(start, end)
	if line_id:
		rs.Redraw()
		return {"status": "success", "id": str(line_id)}
	return {"status": "error", "message": "Failed to add line"}


def add_circle(center, radius):
	"""Add a circle curve"""
	circle_id = rs.AddCircle(center, radius)
	if circle_id:
		rs.Redraw()
		return {"status": "success", "id": str(circle_id)}
	return {"status": "error", "message": "Failed to add circle"}


def add_arc_3pt(start, mid, end):
	"""Add arc through 3 points"""
	arc_id = rs.AddArc3Pt(start, mid, end)
	if arc_id:
		rs.Redraw()
		return {"status": "success", "id": str(arc_id)}
	return {"status": "error", "message": "Failed to add arc"}


def add_ellipse(plane, x_radius, y_radius):
	"""Add an ellipse"""
	ellipse_id = rs.AddEllipse(plane, x_radius, y_radius)
	if ellipse_id:
		rs.Redraw()
		return {"status": "success", "id": str(ellipse_id)}
	return {"status": "error", "message": "Failed to add ellipse"}


def add_polyline(points):
	"""Add a polyline"""
	points_tuple = [tuple(pt) for pt in points]
	polyline_id = rs.AddPolyline(points_tuple)
	if polyline_id:
		rs.Redraw()
		return {"status": "success", "id": str(polyline_id)}
	return {"status": "error", "message": "Failed to add polyline"}


def add_interp_curve(points, degree=3):
	"""Add interpolated curve"""
	points_tuple = [tuple(pt) for pt in points]
	curve_id = rs.AddInterpCurve(points_tuple, degree)
	if curve_id:
		rs.Redraw()
		return {"status": "success", "id": str(curve_id)}
	return {"status": "error", "message": "Failed to add curve"}


def join_curves(curve_ids):
	"""Join curves"""
	result = rs.JoinCurves(curve_ids, delete_input=True)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to join curves"}


def explode_curves(curve_id, delete_input=True):
	"""Explode curve into segments"""
	segments = rs.ExplodeCurves(curve_id, delete_input)
	if segments:
		rs.Redraw()
		return {"status": "success", "count": len(segments), "ids": [str(x) for x in segments]}
	return {"status": "error", "message": "Failed to explode curve"}


def offset_curve(curve_id, point, distance):
	"""Offset curve"""
	result = rs.OffsetCurve(curve_id, point, distance)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to offset curve"}


def extend_curve_length(curve_id, curve_type, side, length):
	"""Extend curve length"""
	result = rs.ExtendCurveLength(curve_id, curve_type, side, length)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to extend curve"}


def curve_length(curve_id):
	"""Get curve length"""
	length = rs.CurveLength(curve_id)
	if length is not None:
		return {"status": "success", "length": length}
	return {"status": "error", "message": "Failed to get curve length"}


def curve_area(curve_id):
	"""Get curve area (for closed planar curves)"""
	if rs.IsCurveClosed(curve_id) and rs.IsCurvePlanar(curve_id):
		area = rs.CurveArea(curve_id)
		if area:
			return {"status": "success", "area": area[0]}
	return {"status": "error", "message": "Curve must be closed and planar"}


def is_curve(obj_id):
	"""Check if object is a curve"""
	return rs.IsCurve(obj_id)


def is_curve_closed(curve_id):
	"""Check if curve is closed"""
	return rs.IsCurveClosed(curve_id)


def is_curve_planar(curve_id):
	"""Check if curve is planar"""
	return rs.IsCurvePlanar(curve_id)


def add_rectangle(plane, width, height):
	"""Add a rectangle"""
	rect_id = rs.AddRectangle(plane, width, height)
	if rect_id:
		rs.Redraw()
		return {"status": "success", "id": str(rect_id)}
	return {"status": "error", "message": "Failed to add rectangle"}


def add_spiral(point0, point1, pitch, turns, radius0, radius1=None):
	"""Add a spiral curve"""
	if radius1 is None:
		radius1 = radius0
	spiral_id = rs.AddSpiral(point0, point1, pitch, turns, radius0, radius1)
	if spiral_id:
		rs.Redraw()
		return {"status": "success", "id": str(spiral_id)}
	return {"status": "error", "message": "Failed to add spiral"}


def add_nurbs_curve(points, knots, degree, weights=None):
	"""Add a NURBS curve"""
	curve_id = rs.AddNurbsCurve(points, knots, degree, weights)
	if curve_id:
		rs.Redraw()
		return {"status": "success", "id": str(curve_id)}
	return {"status": "error", "message": "Failed to add NURBS curve"}


def add_blend_curve(curves, parameters, reverses, continuities):
	"""Add a blend curve between two curves"""
	curve_id = rs.AddBlendCurve(curves, parameters, reverses, continuities)
	if curve_id:
		rs.Redraw()
		return {"status": "success", "id": str(curve_id)}
	return {"status": "error", "message": "Failed to add blend curve"}


def add_fillet_curve(curve0, curve1, radius=1.0, base_point0=None, base_point1=None):
	"""Add a fillet curve between two curves"""
	curve_id = rs.AddFilletCurve(curve0, curve1, radius, base_point0, base_point1)
	if curve_id:
		rs.Redraw()
		return {"status": "success", "id": str(curve_id)}
	return {"status": "error", "message": "Failed to add fillet curve"}


def divide_curve(curve_id, segments, create_points=True):
	"""Divide a curve into segments"""
	points = rs.DivideCurve(curve_id, segments, create_points)
	if points:
		rs.Redraw()
		return {"status": "success", "count": len(points), "points": [[p[0], p[1], p[2]] for p in points]}
	return {"status": "error", "message": "Failed to divide curve"}


def divide_curve_length(curve_id, length, create_points=True):
	"""Divide a curve by arc length"""
	points = rs.DivideCurveLength(curve_id, length, create_points)
	if points:
		rs.Redraw()
		return {"status": "success", "count": len(points), "points": [[p[0], p[1], p[2]] for p in points]}
	return {"status": "error", "message": "Failed to divide curve by length"}


def split_curve(curve_id, parameters):
	"""Split a curve at parameters"""
	result = rs.SplitCurve(curve_id, parameters)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to split curve"}


def close_curve(curve_id, tolerance=-1):
	"""Close an open curve"""
	import scriptcontext
	import Rhino
	curve_obj = rs.coercerhinoobject(curve_id)
	if not curve_obj:
		return {"status": "error", "message": "Curve not found"}
	curve_geom = curve_obj.Geometry
	if curve_geom.IsClosed:
		return {"status": "success", "id": str(curve_id)}
	if tolerance < 0:
		tolerance = scriptcontext.doc.ModelAbsoluteTolerance
	# Try MakeClosed (works when endpoints are near each other)
	dup = curve_geom.DuplicateCurve()
	if dup.MakeClosed(tolerance):
		scriptcontext.doc.Objects.Replace(curve_obj.Id, dup)
		rs.Redraw()
		return {"status": "success", "id": str(curve_id)}
	# Fallback: add a line segment from end to start and join
	line = Rhino.Geometry.LineCurve(curve_geom.PointAtEnd, curve_geom.PointAtStart)
	joined = Rhino.Geometry.Curve.JoinCurves([curve_geom, line], tolerance)
	if joined and len(joined) == 1:
		scriptcontext.doc.Objects.Replace(curve_obj.Id, joined[0])
		rs.Redraw()
		return {"status": "success", "id": str(curve_id)}
	return {"status": "error", "message": "Failed to close curve"}


def reverse_curve(curve_id):
	"""Reverse curve direction"""
	result = rs.ReverseCurve(curve_id)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(curve_id)}
	return {"status": "error", "message": "Failed to reverse curve"}


def rebuild_curve(curve_id, degree=3, point_count=10):
	"""Rebuild a curve with specified degree and point count"""
	import scriptcontext
	curve_obj = rs.coercerhinoobject(curve_id)
	if not curve_obj:
		return {"status": "error", "message": "Curve not found"}
	curve_geom = curve_obj.Geometry
	nurbs = curve_geom.Rebuild(point_count, degree, True)
	if nurbs:
		scriptcontext.doc.Objects.Replace(curve_obj.Id, nurbs)
		rs.Redraw()
		return {"status": "success", "id": str(curve_id)}
	return {"status": "error", "message": "Failed to rebuild curve"}


def project_curve_to_surface(curve_ids, surface_ids, direction):
	"""Project curves onto surfaces"""
	result = rs.ProjectCurveToSurface(curve_ids, surface_ids, direction)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to project curve to surface"}


# Curve analysis functions

def curve_closest_point(curve_id, point):
	"""Find the closest point on a curve to a test point"""
	param = rs.CurveClosestPoint(curve_id, point)
	if param is not None:
		pt = rs.EvaluateCurve(curve_id, param)
		return {"status": "success", "parameter": param, "point": [pt[0], pt[1], pt[2]]}
	return {"status": "error", "message": "Failed to find closest point"}


def evaluate_curve(curve_id, parameter):
	"""Evaluate a curve at a parameter"""
	pt = rs.EvaluateCurve(curve_id, parameter)
	if pt:
		tangent = rs.CurveTangent(curve_id, parameter)
		result = {"status": "success", "point": [pt[0], pt[1], pt[2]]}
		if tangent:
			result["tangent"] = [tangent[0], tangent[1], tangent[2]]
		return result
	return {"status": "error", "message": "Failed to evaluate curve"}


def curve_start_end_points(curve_id):
	"""Get start and end points of a curve"""
	start = rs.CurveStartPoint(curve_id)
	end = rs.CurveEndPoint(curve_id)
	if start and end:
		return {
			"status": "success",
			"start": [start[0], start[1], start[2]],
			"end": [end[0], end[1], end[2]]
		}
	return {"status": "error", "message": "Failed to get curve endpoints"}


def curve_curve_intersection(curve1, curve2, tolerance=-1):
	"""Find intersections between two curves"""
	result = rs.CurveCurveIntersection(curve1, curve2, tolerance)
	if result:
		intersections = []
		for i in range(len(result)):
			event = result[i]
			inter = {"type": event[0], "point1": [event[1][0], event[1][1], event[1][2]]}
			if event[0] == 2:  # overlap
				inter["point2"] = [event[5][0], event[5][1], event[5][2]]
			intersections.append(inter)
		return {"status": "success", "count": len(intersections), "intersections": intersections}
	return {"status": "success", "count": 0, "intersections": []}
