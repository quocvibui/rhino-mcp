"""
RhinoScriptSyntax geometry functions
"""

import rhinoscriptsyntax as rs


def add_point(x, y, z):
	"""Add a point"""
	point_id = rs.AddPoint(x, y, z)
	if point_id:
		rs.Redraw()
		return {"status": "success", "id": str(point_id)}
	return {"status": "error", "message": "Failed to add point"}


def bounding_box(obj_id):
	"""Get object bounding box"""
	return rs.BoundingBox(obj_id)
