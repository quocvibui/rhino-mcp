"""
RhinoScriptSyntax selection functions
"""

import rhinoscriptsyntax as rs


def all_objects():
	"""Get all objects"""
	return rs.AllObjects()


def selected_objects():
	"""Get selected objects"""
	return rs.SelectedObjects()


def unselect_all_objects():
	"""Unselect all objects"""
	rs.UnselectAllObjects()
	return {"status": "success"}


def select_objects(obj_ids):
	"""Select objects by IDs"""
	rs.SelectObjects(obj_ids)
	return {"status": "success"}


def objects_by_type(obj_type):
	"""Get objects by type"""
	return rs.ObjectsByType(obj_type)


def objects_by_layer(layer_name):
	"""Get objects by layer"""
	return rs.ObjectsByLayer(layer_name)


def objects_by_name(name, select=False):
	"""Get objects by name"""
	result = rs.ObjectsByName(name, select)
	if result:
		return [str(x) for x in result]
	return []


def last_created_objects(select=False):
	"""Get the last created objects"""
	result = rs.LastCreatedObjects(select)
	if result:
		return [str(x) for x in result]
	return []


def invert_selected_objects():
	"""Invert the current selection"""
	result = rs.InvertSelectedObjects()
	if result is None:
		return 0
	if isinstance(result, int):
		return result
	# Rhino 8 may return a list of GUIDs
	try:
		return len(result)
	except TypeError:
		return 1
