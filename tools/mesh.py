"""
MCP tools for mesh operations
"""

import json
from .utils import send_to_rhino


def register_tools(mcp):
	"""Register all mesh tools with the MCP server"""

	@mcp.tool()
	def create_mesh(vertices: str, faces: str) -> str:
		"""
		Create a mesh from vertices and face definitions
		vertices: Semicolon-separated vertices, each as 'x,y,z' (e.g. '0,0,0;10,0,0;10,10,0;0,10,0')
		faces: Semicolon-separated face vertex indices, each as 'i,j,k' or 'i,j,k,l' (e.g. '0,1,2;0,2,3')
		"""
		try:
			verts = [[float(c) for c in v.split(",")] for v in vertices.split(";")]
			face_list = [[int(i) for i in f.split(",")] for f in faces.split(";")]
			result = send_to_rhino("create_mesh", {"vertices": verts, "faces": face_list})
			return f"Created mesh with {len(verts)} vertices and {len(face_list)} faces"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def create_planar_mesh(curve_id: str) -> str:
		"""
		Create a planar mesh from a closed planar curve
		curve_id: ID of the closed planar curve
		"""
		try:
			result = send_to_rhino("create_planar_mesh", {"curve_id": curve_id})
			return f"Created planar mesh"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def mesh_from_surface(object_ids: str) -> str:
		"""
		Create meshes from brep/surface objects
		object_ids: Comma-separated IDs of brep/surface objects
		"""
		try:
			ids = [s.strip() for s in object_ids.split(",")]
			result = send_to_rhino("mesh_from_surface", {"object_ids": ids})
			count = result.get("count", 0)
			return f"Created {count} mesh(es) from surfaces"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def mesh_boolean_union(mesh_ids: str) -> str:
		"""
		Boolean union of meshes
		mesh_ids: Comma-separated IDs of meshes to union
		"""
		try:
			ids = [s.strip() for s in mesh_ids.split(",")]
			result = send_to_rhino("mesh_boolean_union", {"mesh_ids": ids})
			count = result.get("count", 0)
			return f"Mesh boolean union created {count} result(s)"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def mesh_boolean_difference(input_ids: str, subtract_ids: str) -> str:
		"""
		Boolean difference of meshes
		input_ids: Comma-separated IDs of input meshes
		subtract_ids: Comma-separated IDs of meshes to subtract
		"""
		try:
			inputs = [s.strip() for s in input_ids.split(",")]
			subtracts = [s.strip() for s in subtract_ids.split(",")]
			result = send_to_rhino("mesh_boolean_difference", {"input_ids": inputs, "subtract_ids": subtracts})
			count = result.get("count", 0)
			return f"Mesh boolean difference created {count} result(s)"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def mesh_boolean_intersection(mesh_ids1: str, mesh_ids2: str) -> str:
		"""
		Boolean intersection of meshes
		mesh_ids1: Comma-separated IDs of first set of meshes
		mesh_ids2: Comma-separated IDs of second set of meshes
		"""
		try:
			ids1 = [s.strip() for s in mesh_ids1.split(",")]
			ids2 = [s.strip() for s in mesh_ids2.split(",")]
			result = send_to_rhino("mesh_boolean_intersection", {"mesh_ids1": ids1, "mesh_ids2": ids2})
			count = result.get("count", 0)
			return f"Mesh boolean intersection created {count} result(s)"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def join_meshes(mesh_ids: str) -> str:
		"""
		Join multiple meshes into a single mesh
		mesh_ids: Comma-separated IDs of meshes to join
		"""
		try:
			ids = [s.strip() for s in mesh_ids.split(",")]
			result = send_to_rhino("join_meshes", {"mesh_ids": ids})
			return f"Joined meshes"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def mesh_to_nurb(mesh_id: str) -> str:
		"""
		Convert a mesh to a NURBS polysurface
		mesh_id: ID of the mesh to convert
		"""
		try:
			result = send_to_rhino("mesh_to_nurb", {"mesh_id": mesh_id})
			return f"Converted mesh to NURBS"
		except Exception as e:
			return f"Error: {e}"

	@mcp.tool()
	def mesh_offset(mesh_id: str, distance: float) -> str:
		"""
		Offset a mesh by a distance
		mesh_id: ID of the mesh to offset
		distance: Offset distance
		"""
		try:
			result = send_to_rhino("mesh_offset", {"mesh_id": mesh_id, "distance": distance})
			return f"Offset mesh by {distance}"
		except Exception as e:
			return f"Error: {e}"
