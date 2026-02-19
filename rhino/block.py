"""
RhinoScriptSyntax block functions
"""

import rhinoscriptsyntax as rs


def add_block(object_ids, base_point, name, delete_input=True):
	"""Create a block definition"""
	result = rs.AddBlock(object_ids, base_point, name, delete_input)
	if result:
		return {"status": "success", "name": result}
	return {"status": "error", "message": "Failed to create block"}


def insert_block(name, insertion_point, scale=None, rotation=0):
	"""Insert a block instance"""
	if scale is None:
		scale = (1, 1, 1)
	result = rs.InsertBlock(name, insertion_point, scale, rotation)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to insert block"}


def explode_block_instance(block_id):
	"""Explode a block instance into its component objects"""
	result = rs.ExplodeBlockInstance(block_id)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to explode block"}


def delete_block(name):
	"""Delete a block definition"""
	if rs.DeleteBlock(name):
		return {"status": "success"}
	return {"status": "error", "message": "Failed to delete block"}


def block_names():
	"""Get all block definition names"""
	names = rs.BlockNames()
	if names:
		return {"status": "success", "blocks": list(names)}
	return {"status": "success", "blocks": []}
