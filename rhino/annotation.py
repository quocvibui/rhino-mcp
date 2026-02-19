"""
RhinoScriptSyntax annotation functions
"""

import rhinoscriptsyntax as rs


def add_text(text, point, height=1.0, font=None):
	"""Add a text object"""
	if font:
		text_id = rs.AddText(text, point, height, font)
	else:
		text_id = rs.AddText(text, point, height)
	if text_id:
		rs.Redraw()
		return {"status": "success", "id": str(text_id)}
	return {"status": "error", "message": "Failed to add text"}


def add_text_dot(text, point):
	"""Add a text dot"""
	dot_id = rs.AddTextDot(text, point)
	if dot_id:
		rs.Redraw()
		return {"status": "success", "id": str(dot_id)}
	return {"status": "error", "message": "Failed to add text dot"}


def add_leader(points, text=""):
	"""Add a leader annotation"""
	if text:
		leader_id = rs.AddLeader(points, text=text)
	else:
		leader_id = rs.AddLeader(points)
	if leader_id:
		rs.Redraw()
		return {"status": "success", "id": str(leader_id)}
	return {"status": "error", "message": "Failed to add leader"}
