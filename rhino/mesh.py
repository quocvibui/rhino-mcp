"""
RhinoScriptSyntax mesh functions
"""

import rhinoscriptsyntax as rs


def add_mesh(vertices, face_vertices):
	"""Add a mesh from vertices and face vertex indices"""
	mesh_id = rs.AddMesh(vertices, face_vertices)
	if mesh_id:
		rs.Redraw()
		return {"status": "success", "id": str(mesh_id)}
	return {"status": "error", "message": "Failed to create mesh"}


def add_planar_mesh(object_id):
	"""Create a planar mesh from a closed planar curve"""
	mesh_id = rs.AddPlanarMesh(object_id)
	if mesh_id:
		rs.Redraw()
		return {"status": "success", "id": str(mesh_id)}
	return {"status": "error", "message": "Failed to create planar mesh"}


def mesh_objects(object_ids):
	"""Create meshes from brep objects"""
	import Rhino
	import scriptcontext
	mesh_ids = []
	for obj_id in object_ids:
		brep = rs.coercebrep(obj_id)
		if brep:
			meshes = Rhino.Geometry.Mesh.CreateFromBrep(brep, Rhino.Geometry.MeshingParameters.Default)
			if meshes:
				for m in meshes:
					added = scriptcontext.doc.Objects.AddMesh(m)
					if added:
						mesh_ids.append(str(added))
	if mesh_ids:
		rs.Redraw()
		return {"status": "success", "count": len(mesh_ids), "ids": mesh_ids}
	return {"status": "error", "message": "Failed to mesh objects"}


def mesh_boolean_union(mesh_ids):
	"""Boolean union of meshes"""
	result = rs.MeshBooleanUnion(mesh_ids)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to perform mesh boolean union"}


def mesh_boolean_difference(input_meshes, subtract_meshes):
	"""Boolean difference of meshes"""
	result = rs.MeshBooleanDifference(input_meshes, subtract_meshes)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to perform mesh boolean difference"}


def mesh_boolean_intersection(mesh_ids1, mesh_ids2):
	"""Boolean intersection of meshes"""
	result = rs.MeshBooleanIntersection(mesh_ids1, mesh_ids2)
	if result:
		rs.Redraw()
		return {"status": "success", "count": len(result), "ids": [str(x) for x in result]}
	return {"status": "error", "message": "Failed to perform mesh boolean intersection"}


def join_meshes(mesh_ids, delete_input=True):
	"""Join meshes into a single mesh"""
	result = rs.JoinMeshes(mesh_ids, delete_input)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to join meshes"}


def mesh_to_nurb(mesh_id):
	"""Convert a mesh to a NURBS polysurface"""
	result = rs.MeshToNurb(mesh_id)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to convert mesh to NURBS"}


def mesh_offset(mesh_id, distance):
	"""Offset a mesh"""
	result = rs.MeshOffset(mesh_id, distance)
	if result:
		rs.Redraw()
		return {"status": "success", "id": str(result)}
	return {"status": "error", "message": "Failed to offset mesh"}
