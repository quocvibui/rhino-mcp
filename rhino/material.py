"""
RhinoScriptSyntax material functions
"""

import rhinoscriptsyntax as rs


def add_material_to_object(object_id):
	"""Add a material to an object and return the material index"""
	index = rs.AddMaterialToObject(object_id)
	if index is not None and index >= 0:
		return {"status": "success", "index": index}
	return {"status": "error", "message": "Failed to add material to object"}


def add_material_to_layer(layer_name):
	"""Add a material to a layer and return the material index"""
	index = rs.AddMaterialToLayer(layer_name)
	if index is not None and index >= 0:
		return {"status": "success", "index": index}
	return {"status": "error", "message": "Failed to add material to layer"}


def material_color(index, color=None):
	"""Get or set material color"""
	if color:
		rs.MaterialColor(index, color)
		rs.Redraw()
		return {"status": "success"}
	c = rs.MaterialColor(index)
	if c is not None:
		return {"status": "success", "color": [int(c.R), int(c.G), int(c.B)]}
	return {"status": "error", "message": "Failed to get material color"}


def material_transparency(index, transparency=None):
	"""Get or set material transparency (0.0 to 1.0)"""
	if transparency is not None:
		rs.MaterialTransparency(index, transparency)
		rs.Redraw()
		return {"status": "success"}
	t = rs.MaterialTransparency(index)
	if t is not None:
		return {"status": "success", "transparency": t}
	return {"status": "error", "message": "Failed to get material transparency"}


def material_shine(index, shine=None):
	"""Get or set material shine (0.0 to 255.0)"""
	if shine is not None:
		rs.MaterialShine(index, shine)
		rs.Redraw()
		return {"status": "success"}
	s = rs.MaterialShine(index)
	if s is not None:
		return {"status": "success", "shine": s}
	return {"status": "error", "message": "Failed to get material shine"}
