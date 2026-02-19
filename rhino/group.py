"""
RhinoScriptSyntax group functions
"""

import rhinoscriptsyntax as rs


def add_group(name=None):
	"""Create a new group"""
	group = rs.AddGroup(name)
	if group:
		return {"status": "success", "name": group}
	return {"status": "error", "message": "Failed to create group"}


def delete_group(name):
	"""Delete a group"""
	if rs.DeleteGroup(name):
		return {"status": "success"}
	return {"status": "error", "message": "Failed to delete group"}


def add_objects_to_group(object_ids, group_name):
	"""Add objects to a group"""
	count = rs.AddObjectsToGroup(object_ids, group_name)
	if count:
		return {"status": "success", "count": count}
	return {"status": "error", "message": "Failed to add objects to group"}


def remove_objects_from_group(object_ids, group_name):
	"""Remove objects from a group"""
	count = rs.RemoveObjectsFromGroup(object_ids, group_name)
	if count:
		return {"status": "success", "count": count}
	return {"status": "error", "message": "Failed to remove objects from group"}


def group_names():
	"""Get all group names"""
	names = rs.GroupNames()
	if names:
		return {"status": "success", "groups": list(names)}
	return {"status": "success", "groups": []}


def objects_by_group(group_name):
	"""Get objects in a group"""
	objects = rs.ObjectsByGroup(group_name)
	if objects:
		return {"status": "success", "count": len(objects), "ids": [str(x) for x in objects]}
	return {"status": "success", "count": 0, "ids": []}
