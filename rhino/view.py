"""
RhinoScriptSyntax view functions
"""

import os
import tempfile
import base64
import rhinoscriptsyntax as rs
import Rhino
import System.Drawing


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


def capture_viewport(width=800, height=600):
	"""Capture viewport to base64 PNG image"""
	view = Rhino.RhinoDoc.ActiveDoc.Views.ActiveView
	if not view:
		return {"status": "error", "message": "No active view found"}
	filepath = os.path.join(tempfile.gettempdir(), "rhino_mcp_capture.png")
	size = System.Drawing.Size(width, height)
	bitmap = view.CaptureToBitmap(size)
	if not bitmap:
		return {"status": "error", "message": "Failed to capture viewport"}
	bitmap.Save(filepath)
	bitmap.Dispose()
	with open(filepath, "rb") as f:
		b64 = base64.b64encode(f.read()).decode("utf-8")
	return {"status": "success", "image": b64}
