"""
RhinoScriptSyntax user data functions
"""

import rhinoscriptsyntax as rs


def set_user_text(object_id, key, value, attach_to_geometry=False):
	"""Set user text on an object"""
	result = rs.SetUserText(object_id, key, value, attach_to_geometry)
	if result:
		return {"status": "success"}
	return {"status": "error", "message": "Failed to set user text"}


def get_user_text(object_id, key=None):
	"""Get user text from an object"""
	if key:
		value = rs.GetUserText(object_id, key)
		return {"status": "success", "key": key, "value": value}
	else:
		keys = rs.GetUserText(object_id)
		if keys:
			data = {}
			for k in keys:
				data[k] = rs.GetUserText(object_id, k)
			return {"status": "success", "data": data}
		return {"status": "success", "data": {}}


def set_document_user_text(key, value):
	"""Set document-level user text"""
	result = rs.SetDocumentUserText(key, value)
	if result:
		return {"status": "success"}
	return {"status": "error", "message": "Failed to set document user text"}


def get_document_user_text(key=None):
	"""Get document-level user text"""
	if key:
		value = rs.GetDocumentUserText(key)
		return {"status": "success", "key": key, "value": value}
	else:
		keys = rs.GetDocumentUserText()
		if keys:
			data = {}
			for k in keys:
				data[k] = rs.GetDocumentUserText(k)
			return {"status": "success", "data": data}
		return {"status": "success", "data": {}}
