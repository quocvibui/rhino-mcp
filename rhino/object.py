"""
RhinoScriptSyntax object functions
"""

import rhinoscriptsyntax as rs


def copy_object(obj_id, translation):
	"""Copy an object"""
	new_obj = rs.CopyObject(obj_id, translation)
	if new_obj:
		rs.Redraw()
		return {"status": "success", "id": str(new_obj)}
	return {"status": "error", "message": "Failed to copy object"}


def delete_object(obj_id):
	"""Delete an object"""
	if rs.DeleteObject(obj_id):
		rs.Redraw()
		return {"status": "success"}
	return {"status": "error", "message": "Failed to delete object"}


def delete_objects(obj_ids):
	"""Delete multiple objects"""
	if rs.DeleteObjects(obj_ids):
		rs.Redraw()
		return {"status": "success", "count": len(obj_ids)}
	return {"status": "error", "message": "Failed to delete objects"}


def move_object(obj_id, translation):
	"""Move an object"""
	result = rs.MoveObject(obj_id, translation)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to move object"}


def rotate_objects(obj_ids, center, angle, axis=None):
	"""Rotate objects"""
	result = rs.RotateObjects(obj_ids, center, angle, axis)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result)}
	return {"status": "error", "message": "Failed to rotate objects"}


def scale_object(obj_id, origin, scale):
	"""Scale an object"""
	result = rs.ScaleObject(obj_id, origin, scale)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to scale object"}


def mirror_object(obj_id, start, end):
	"""Mirror an object"""
	result = rs.MirrorObject(obj_id, start, end)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to mirror object"}


def object_name(obj_id, name=None):
	"""Get or set object name"""
	if name:
		rs.ObjectName(obj_id, name)
		return {"status": "success"}
	return rs.ObjectName(obj_id)


def object_layer(obj_id, layer=None):
	"""Get or set object layer"""
	if layer:
		rs.ObjectLayer(obj_id, layer)
		return {"status": "success"}
	return rs.ObjectLayer(obj_id)


def object_color(obj_id, color=None):
	"""Get or set object color"""
	if color:
		rs.ObjectColor(obj_id, color)
		return {"status": "success"}
	return rs.ObjectColor(obj_id)


def object_type(obj_id):
	"""Get object type"""
	return rs.ObjectType(obj_id)


def select_objects(obj_ids):
	"""Select objects"""
	rs.SelectObjects(obj_ids)
	return {"status": "success", "count": len(obj_ids)}


def hide_objects(obj_ids):
	"""Hide objects"""
	count = rs.HideObjects(obj_ids)
	if count:
		rs.Redraw()
		return {"status": "success", "count": count}
	return {"status": "error", "message": "Failed to hide objects"}


def show_objects(obj_ids):
	"""Show hidden objects"""
	count = rs.ShowObjects(obj_ids)
	if count:
		rs.Redraw()
		return {"status": "success", "count": count}
	return {"status": "error", "message": "Failed to show objects"}


def lock_objects(obj_ids):
	"""Lock objects"""
	count = rs.LockObjects(obj_ids)
	if count:
		rs.Redraw()
		return {"status": "success", "count": count}
	return {"status": "error", "message": "Failed to lock objects"}


def unlock_objects(obj_ids):
	"""Unlock objects"""
	count = rs.UnlockObjects(obj_ids)
	if count:
		rs.Redraw()
		return {"status": "success", "count": count}
	return {"status": "error", "message": "Failed to unlock objects"}


def is_object_solid(obj_id):
	"""Check if an object is a solid (closed polysurface or mesh)"""
	result = rs.IsObjectSolid(obj_id)
	return {"status": "success", "solid": bool(result)}


def orient_object(obj_id, reference, target):
	"""Orient an object from reference to target planes"""
	result = rs.OrientObject(obj_id, reference, target)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to orient object"}
