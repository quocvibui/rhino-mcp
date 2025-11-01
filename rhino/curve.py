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
