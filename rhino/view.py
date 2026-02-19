"""
RhinoScriptSyntax view functions
"""

import rhinoscriptsyntax as rs


def set_view_camera(camera, target, view=None):
	"""Set view camera and target"""
	if view:
		rs.ViewCamera(view, camera)
		rs.ViewTarget(view, target)
	else:
		view = rs.CurrentView()
		rs.ViewCamera(view, camera)
		rs.ViewTarget(view, target)
	rs.Redraw()
	return {"status": "success", "view": view}


def zoom_extents(view=None, all_views=False):
	"""Zoom to extents"""
	rs.ZoomExtents(view, all_views)
	return {"status": "success"}


def zoom_selected(view=None, all_views=False):
	"""Zoom to selected objects"""
	rs.ZoomSelected(view, all_views)
	return {"status": "success"}


def get_view_info(view=None):
	"""Get current view information"""
	if not view:
		view = rs.CurrentView()
	camera = rs.ViewCamera(view)
	target = rs.ViewTarget(view)
	mode = rs.ViewDisplayMode(view)
	return {
		"status": "success",
		"view": view,
		"camera": [camera[0], camera[1], camera[2]] if camera else None,
		"target": [target[0], target[1], target[2]] if target else None,
		"display_mode": mode
	}


def set_display_mode(mode, view=None):
	"""Set display mode for a view"""
	if not view:
		view = rs.CurrentView()
	rs.ViewDisplayMode(view, mode)
	rs.Redraw()
	return {"status": "success", "view": view, "mode": mode}


def add_named_view(name, view=None):
	"""Add a named view"""
	if not view:
		view = rs.CurrentView()
	result = rs.AddNamedView(name, view)
	if result:
		return {"status": "success", "name": result}
	return {"status": "error", "message": "Failed to add named view"}


def restore_named_view(name, view=None):
	"""Restore a named view"""
	result = rs.RestoreNamedView(name, view)
	if result:
		rs.Redraw()
		return {"status": "success", "name": name}
	return {"status": "error", "message": "Failed to restore named view"}
