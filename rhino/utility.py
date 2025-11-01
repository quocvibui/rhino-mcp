"""
RhinoScriptSyntax utility functions
"""

import rhinoscriptsyntax as rs


def distance(point1, point2):
	"""Calculate distance between two points"""
	dist = rs.Distance(point1, point2)
	if dist is not None:
		return {"status": "success", "distance": dist}
	return {"status": "error", "message": "Failed to calculate distance"}
