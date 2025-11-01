"""
RhinoScriptSyntax plane functions
"""

import rhinoscriptsyntax as rs


def plane_from_normal(origin, normal):
	"""Create a plane from origin and normal"""
	return rs.PlaneFromNormal(origin, normal)
