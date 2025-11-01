"""
RhinoScriptSyntax document functions
"""

import rhinoscriptsyntax as rs


def redraw():
	"""Redraw the viewport"""
	rs.Redraw()


def unit_system_name():
	"""Get the document's unit system name"""
	return rs.UnitSystemName()
