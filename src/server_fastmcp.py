#!/usr/bin/env python3
"""
Rhino MCP Server using FastMCP
Production-ready implementation with comprehensive tools
"""

from mcp.server.fastmcp import FastMCP
import socket
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("RhinoMCP")

mcp = FastMCP("rhino-mcp")

RHINO_HOST = "localhost"
RHINO_PORT = 54321
SOCKET_TIMEOUT = 10


def send_to_rhino(command_type, params=None):
	"""
	Send JSON command to Rhino and return response
	command_type: Command type string
	params: Parameters dictionary
	return: Response dictionary from Rhino
	"""
	if params is None:
		params = {}

	command = {
		"type": command_type,
		"params": params
	}

	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(SOCKET_TIMEOUT)
		sock.connect((RHINO_HOST, RHINO_PORT))

		sock.sendall(json.dumps(command).encode('utf-8'))

		response_data = sock.recv(8192)
		sock.close()

		response = json.loads(response_data.decode('utf-8'))

		if response.get("status") == "error":
			raise Exception(response.get("message", "Unknown error from Rhino"))

		return response.get("result", {})

	except ConnectionRefusedError:
		raise Exception("Cannot connect to Rhino. Ensure listener is running.")
	except socket.timeout:
		raise Exception("Connection timeout. Rhino may be busy.")
	except json.JSONDecodeError as e:
		raise Exception("Invalid response from Rhino: {0}".format(str(e)))
	except Exception as e:
		raise Exception("Communication error: {0}".format(str(e)))


@mcp.tool()
def get_scene_info() -> str:
	"""
	Get comprehensive information about the current Rhino scene.
	Returns details about all objects, layers, units, and object counts.
	This should be called first to understand what's already in the scene.
	"""
	try:
		result = send_to_rhino("get_scene_info")
		return json.dumps(result, indent=2)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def get_selected_objects() -> str:
	"""
	Get information about currently selected objects in Rhino.
	Returns details about each selected object including type, layer, and location.
	"""
	try:
		result = send_to_rhino("get_selected_objects")
		return json.dumps(result, indent=2)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def create_point(x: float, y: float, z: float = 0) -> str:
	"""
	Create a point in Rhino
	x: X coordinate
	y: Y coordinate
	z: Z coordinate (default 0)
	"""
	try:
		result = send_to_rhino("create_point", {"x": x, "y": y, "z": z})
		return "Created point at ({0}, {1}, {2})".format(x, y, z)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def create_line(start_x: float, start_y: float, start_z: float,
				end_x: float, end_y: float, end_z: float) -> str:
	"""
	Create a line in Rhino between two points
	start_x, start_y, start_z: Start point coordinates
	end_x, end_y, end_z: End point coordinates
	"""
	try:
		params = {
			"start": [start_x, start_y, start_z],
			"end": [end_x, end_y, end_z]
		}
		result = send_to_rhino("create_line", params)
		return "Created line from ({0}, {1}, {2}) to ({3}, {4}, {5})".format(
			start_x, start_y, start_z, end_x, end_y, end_z)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def create_polyline(points: list[list[float]]) -> str:
	"""
	Create a polyline through multiple points
	points: List of points, each point is [x, y, z]
	Example: [[0,0,0], [10,0,0], [10,10,0], [0,10,0]]
	"""
	try:
		result = send_to_rhino("create_polyline", {"points": points})
		return "Created polyline with {0} points".format(len(points))
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def create_curve(points: list[list[float]], degree: int = 3) -> str:
	"""
	Create a smooth interpolated curve through points
	points: List of points, each point is [x, y, z]
	degree: Curve degree (3 for cubic, higher for smoother)
	"""
	try:
		result = send_to_rhino("create_curve", {"points": points, "degree": degree})
		return "Created curve with {0} points, degree {1}".format(len(points), degree)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def create_circle(center_x: float, center_y: float, center_z: float, radius: float) -> str:
	"""
	Create a circle in Rhino
	center_x, center_y, center_z: Center point coordinates
	radius: Circle radius
	"""
	try:
		params = {
			"center": [center_x, center_y, center_z],
			"radius": radius
		}
		result = send_to_rhino("create_circle", params)
		return "Created circle with radius {0} at ({1}, {2}, {3})".format(
			radius, center_x, center_y, center_z)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def create_box(width: float = 10, depth: float = 10, height: float = 10,
			   x: float = 0, y: float = 0, z: float = 0) -> str:
	"""
	Create a box in Rhino
	width: Box width (X direction)
	depth: Box depth (Y direction)
	height: Box height (Z direction)
	x, y, z: Position coordinates (default 0, 0, 0)
	"""
	try:
		params = {
			"width": width,
			"depth": depth,
			"height": height,
			"x": x,
			"y": y,
			"z": z
		}
		result = send_to_rhino("create_box", params)
		return "Created box {0}x{1}x{2} at ({3}, {4}, {5})".format(
			width, depth, height, x, y, z)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def create_sphere(center_x: float, center_y: float, center_z: float,
				  radius: float) -> str:
	"""
	Create a sphere in Rhino
	center_x, center_y, center_z: Center point coordinates
	radius: Sphere radius
	"""
	try:
		params = {
			"center": [center_x, center_y, center_z],
			"radius": radius
		}
		result = send_to_rhino("create_sphere", params)
		return "Created sphere with radius {0} at ({1}, {2}, {3})".format(
			radius, center_x, center_y, center_z)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def create_cylinder(base_x: float, base_y: float, base_z: float,
					height: float, radius: float) -> str:
	"""
	Create a cylinder in Rhino
	base_x, base_y, base_z: Base center point coordinates
	height: Cylinder height
	radius: Cylinder radius
	"""
	try:
		params = {
			"base": [base_x, base_y, base_z],
			"height": height,
			"radius": radius
		}
		result = send_to_rhino("create_cylinder", params)
		return "Created cylinder with radius {0}, height {1} at ({2}, {3}, {4})".format(
			radius, height, base_x, base_y, base_z)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def create_cone(base_x: float, base_y: float, base_z: float,
				height: float, radius: float) -> str:
	"""
	Create a cone in Rhino
	base_x, base_y, base_z: Base center point coordinates
	height: Cone height
	radius: Base radius
	"""
	try:
		params = {
			"base": [base_x, base_y, base_z],
			"height": height,
			"radius": radius
		}
		result = send_to_rhino("create_cone", params)
		return "Created cone with base radius {0}, height {1} at ({2}, {3}, {4})".format(
			radius, height, base_x, base_y, base_z)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def select_all() -> str:
	"""
	Select all objects in the Rhino document
	"""
	try:
		result = send_to_rhino("select_all")
		count = result.get("count", 0)
		return "Selected {0} objects".format(count)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def delete_selected() -> str:
	"""
	Delete all currently selected objects in Rhino.
	Use select_all first if you want to delete everything.
	"""
	try:
		result = send_to_rhino("delete_selected")
		deleted = result.get("deleted", 0)
		return "Deleted {0} objects".format(deleted)
	except Exception as e:
		return "Error: {0}".format(str(e))


def main():
	"""Run the MCP server"""
	mcp.run()


if __name__ == "__main__":
	main()
