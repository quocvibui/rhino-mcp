"""
RhinoScriptSyntax layer functions
"""

import rhinoscriptsyntax as rs


def add_layer(name, color=None):
	"""Add a new layer"""
	if rs.IsLayer(name):
		return {"status": "error", "message": "Layer already exists"}
	layer = rs.AddLayer(name, color) if color else rs.AddLayer(name)
	if layer:
		return {"status": "success", "name": layer}
	return {"status": "error", "message": "Failed to create layer"}


def delete_layer(name):
	"""Delete a layer"""
	if not rs.IsLayer(name):
		return {"status": "error", "message": "Layer does not exist"}
	if rs.DeleteLayer(name):
		return {"status": "success"}
	return {"status": "error", "message": "Failed to delete layer"}


def current_layer(name=None):
	"""Get or set current layer"""
	if name:
		if not rs.IsLayer(name):
			return {"status": "error", "message": "Layer does not exist"}
		rs.CurrentLayer(name)
		return {"status": "success", "name": name}
	else:
		return rs.CurrentLayer()


def layer_color(name, color=None):
	"""Get or set layer color"""
	if not rs.IsLayer(name):
		return {"status": "error", "message": "Layer does not exist"}
	if color:
		rs.LayerColor(name, color)
		return {"status": "success"}
	return rs.LayerColor(name)


def layer_visible(name, visible=None):
	"""Get or set layer visibility"""
	if not rs.IsLayer(name):
		return {"status": "error", "message": "Layer does not exist"}
	if visible is not None:
		rs.LayerVisible(name, visible)
		return {"status": "success"}
	return rs.LayerVisible(name)


def layer_names():
	"""Get all layer names"""
	return rs.LayerNames()


def layer_locked(name):
	"""Check if layer is locked"""
	return rs.LayerLocked(name)


def is_layer(name):
	"""Check if layer exists"""
	return rs.IsLayer(name)
