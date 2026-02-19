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


def document_name():
	"""Get the document name"""
	return rs.DocumentName()


def document_path():
	"""Get the document path"""
	return rs.DocumentPath()


def unit_system(system=None):
	"""Get or set the unit system (0=None,1=Microns,2=mm,3=cm,4=m,8=inches,9=feet)"""
	if system is not None:
		rs.UnitSystem(system)
		return {"status": "success"}
	return rs.UnitSystem()


def enable_redraw(enable=True):
	"""Enable or disable viewport redraw"""
	rs.EnableRedraw(enable)
	return {"status": "success"}
