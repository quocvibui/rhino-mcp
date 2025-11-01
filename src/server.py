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


@mcp.tool()
def create_arc(center_x: float, center_y: float, center_z: float,
			   radius: float, start_angle: float, end_angle: float) -> str:
	"""
	Create an arc in Rhino
	center_x, center_y, center_z: Center point coordinates
	radius: Arc radius
	start_angle: Start angle in degrees
	end_angle: End angle in degrees
	"""
	try:
		params = {
			"center": [center_x, center_y, center_z],
			"radius": radius,
			"start_angle": start_angle,
			"end_angle": end_angle
		}
		result = send_to_rhino("create_arc", params)
		return "Created arc with radius {0} from {1} to {2} degrees".format(
			radius, start_angle, end_angle)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def create_ellipse(center_x: float, center_y: float, center_z: float,
				   x_radius: float, y_radius: float) -> str:
	"""
	Create an ellipse in Rhino
	center_x, center_y, center_z: Center point coordinates
	x_radius: Radius in X direction
	y_radius: Radius in Y direction
	"""
	try:
		params = {
			"center": [center_x, center_y, center_z],
			"x_radius": x_radius,
			"y_radius": y_radius
		}
		result = send_to_rhino("create_ellipse", params)
		return "Created ellipse with radii {0}x{1}".format(x_radius, y_radius)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def create_torus(center_x: float, center_y: float, center_z: float,
				 major_radius: float, minor_radius: float) -> str:
	"""
	Create a torus in Rhino
	center_x, center_y, center_z: Center point coordinates
	major_radius: Major radius (distance from center to tube center)
	minor_radius: Minor radius (tube radius)
	"""
	try:
		params = {
			"center": [center_x, center_y, center_z],
			"major_radius": major_radius,
			"minor_radius": minor_radius
		}
		result = send_to_rhino("create_torus", params)
		return "Created torus with radii {0}/{1}".format(major_radius, minor_radius)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def move_objects(dx: float, dy: float, dz: float) -> str:
	"""
	Move selected objects by a displacement vector
	dx: Displacement in X direction
	dy: Displacement in Y direction
	dz: Displacement in Z direction
	Objects must be selected in Rhino first
	"""
	try:
		params = {"displacement": [dx, dy, dz]}
		result = send_to_rhino("move_objects", params)
		moved = result.get("moved", 0)
		return "Moved {0} objects by ({1}, {2}, {3})".format(moved, dx, dy, dz)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def rotate_objects(center_x: float, center_y: float, center_z: float,
				   angle: float) -> str:
	"""
	Rotate selected objects around Z-axis
	center_x, center_y, center_z: Rotation center point
	angle: Rotation angle in degrees
	Objects must be selected in Rhino first
	"""
	try:
		params = {
			"center": [center_x, center_y, center_z],
			"angle": angle
		}
		result = send_to_rhino("rotate_objects", params)
		count = result.get("count", 0)
		return "Rotated {0} objects by {1} degrees".format(count, angle)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def scale_objects(center_x: float, center_y: float, center_z: float,
				  scale_factor: float) -> str:
	"""
	Scale selected objects uniformly from a center point
	center_x, center_y, center_z: Scale center point
	scale_factor: Scale factor (2.0 = double size, 0.5 = half size)
	Objects must be selected in Rhino first
	"""
	try:
		params = {
			"center": [center_x, center_y, center_z],
			"scale": scale_factor
		}
		result = send_to_rhino("scale_objects", params)
		scaled = result.get("scaled", 0)
		return "Scaled {0} objects by factor {1}".format(scaled, scale_factor)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def mirror_objects(start_x: float, start_y: float, start_z: float,
				   end_x: float, end_y: float, end_z: float) -> str:
	"""
	Mirror selected objects across a line
	start_x, start_y, start_z: Start point of mirror line
	end_x, end_y, end_z: End point of mirror line
	Objects must be selected in Rhino first
	"""
	try:
		params = {
			"start": [start_x, start_y, start_z],
			"end": [end_x, end_y, end_z]
		}
		result = send_to_rhino("mirror_objects", params)
		mirrored = result.get("mirrored", 0)
		return "Mirrored {0} objects".format(mirrored)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def copy_objects(dx: float, dy: float, dz: float) -> str:
	"""
	Copy selected objects to a new location
	dx: Displacement in X direction
	dy: Displacement in Y direction
	dz: Displacement in Z direction
	Objects must be selected in Rhino first
	"""
	try:
		params = {"displacement": [dx, dy, dz]}
		result = send_to_rhino("copy_objects", params)
		copied = result.get("copied", 0)
		return "Copied {0} objects".format(copied)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def array_linear(dx: float, dy: float, dz: float, count: int) -> str:
	"""
	Create a linear array of selected objects
	dx, dy, dz: Spacing between copies
	count: Number of copies to create
	Objects must be selected in Rhino first
	"""
	try:
		params = {
			"displacement": [dx, dy, dz],
			"count": count
		}
		result = send_to_rhino("array_linear", params)
		created = result.get("created", 0)
		return "Created linear array with {0} new objects".format(created)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def boolean_union() -> str:
	"""
	Perform boolean union on selected objects
	Combines multiple solids into one
	At least 2 objects must be selected in Rhino first
	"""
	try:
		result = send_to_rhino("boolean_union")
		count = result.get("count", 0)
		return "Boolean union created {0} result(s)".format(count)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def boolean_difference() -> str:
	"""
	Perform boolean difference on selected objects
	Subtracts all objects after the first from the first object
	At least 2 objects must be selected in Rhino first
	"""
	try:
		result = send_to_rhino("boolean_difference")
		count = result.get("count", 0)
		return "Boolean difference created {0} result(s)".format(count)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def boolean_intersection() -> str:
	"""
	Perform boolean intersection on selected objects
	Keeps only the overlapping volume
	At least 2 objects must be selected in Rhino first
	"""
	try:
		result = send_to_rhino("boolean_intersection")
		count = result.get("count", 0)
		return "Boolean intersection created {0} result(s)".format(count)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def join_curves() -> str:
	"""
	Join selected curves into a single curve
	Curves must be selected in Rhino first and should be connected
	"""
	try:
		result = send_to_rhino("join_curves")
		count = result.get("count", 0)
		return "Joined curves into {0} result(s)".format(count)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def explode_curves() -> str:
	"""
	Explode selected curves into segments
	Breaks polylines and polycurves into individual segments
	Curves must be selected in Rhino first
	"""
	try:
		result = send_to_rhino("explode_curves")
		count = result.get("count", 0)
		return "Exploded curves into {0} segments".format(count)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def offset_curve(distance: float) -> str:
	"""
	Offset selected curves by a distance
	distance: Offset distance (positive or negative)
	Curves must be selected in Rhino first
	"""
	try:
		params = {"distance": distance}
		result = send_to_rhino("offset_curve", params)
		count = result.get("count", 0)
		return "Offset {0} curves by distance {1}".format(count, distance)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def fillet_curves(radius: float) -> str:
	"""
	Fillet two selected curves with a radius
	radius: Fillet radius
	Exactly 2 curves must be selected in Rhino first
	"""
	try:
		params = {"radius": radius}
		result = send_to_rhino("fillet_curves", params)
		return "Created fillet with radius {0}".format(radius)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def extend_curve(extension: float) -> str:
	"""
	Extend selected curves by a length
	extension: Extension length
	Curves must be selected in Rhino first
	"""
	try:
		params = {"extension": extension}
		result = send_to_rhino("extend_curve", params)
		return "Extended curve by {0}".format(extension)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def extrude_curve_straight(height: float) -> str:
	"""
	Extrude selected curves straight up to create surfaces
	height: Extrusion height in Z direction
	Closed curves will create solids, open curves will create surfaces
	Curves must be selected in Rhino first
	"""
	try:
		params = {"height": height}
		result = send_to_rhino("extrude_curve_straight", params)
		return "Extruded curves with height {0}".format(height)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def revolve_curve(axis_start_x: float, axis_start_y: float, axis_start_z: float,
				  axis_end_x: float, axis_end_y: float, axis_end_z: float,
				  angle: float = 360) -> str:
	"""
	Revolve selected curves around an axis to create surfaces
	axis_start_x, axis_start_y, axis_start_z: Axis start point
	axis_end_x, axis_end_y, axis_end_z: Axis end point
	angle: Rotation angle in degrees (default 360 for full revolution)
	Curves must be selected in Rhino first
	"""
	try:
		params = {
			"axis_start": [axis_start_x, axis_start_y, axis_start_z],
			"axis_end": [axis_end_x, axis_end_y, axis_end_z],
			"angle": angle
		}
		result = send_to_rhino("revolve_curve", params)
		count = result.get("count", 0)
		return "Revolved {0} curves by {1} degrees".format(count, angle)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def loft_curves() -> str:
	"""
	Create a lofted surface through selected curves
	Creates smooth surface transitioning between curves
	At least 2 curves must be selected in Rhino first
	"""
	try:
		result = send_to_rhino("loft_curves")
		return "Created lofted surface"
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def create_layer(name: str, color_r: int = 0, color_g: int = 0, color_b: int = 0) -> str:
	"""
	Create a new layer in Rhino
	name: Layer name
	color_r, color_g, color_b: RGB color values (0-255), default black
	"""
	try:
		params = {
			"name": name,
			"color": [color_r, color_g, color_b]
		}
		result = send_to_rhino("create_layer", params)
		return "Created layer '{0}'".format(name)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def delete_layer(name: str) -> str:
	"""
	Delete a layer from Rhino
	name: Layer name to delete
	Layer must be empty (no objects on it)
	"""
	try:
		params = {"name": name}
		result = send_to_rhino("delete_layer", params)
		return "Deleted layer '{0}'".format(name)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def set_current_layer(name: str) -> str:
	"""
	Set the current active layer in Rhino
	name: Layer name to make current
	New objects will be created on this layer
	"""
	try:
		params = {"name": name}
		result = send_to_rhino("set_current_layer", params)
		return "Set current layer to '{0}'".format(name)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def set_layer_color(name: str, color_r: int, color_g: int, color_b: int) -> str:
	"""
	Set the color of a layer
	name: Layer name
	color_r, color_g, color_b: RGB color values (0-255)
	"""
	try:
		params = {
			"name": name,
			"color": [color_r, color_g, color_b]
		}
		result = send_to_rhino("set_layer_color", params)
		return "Set layer '{0}' color to RGB({1}, {2}, {3})".format(
			name, color_r, color_g, color_b)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def set_layer_visibility(name: str, visible: bool) -> str:
	"""
	Set layer visibility (show/hide)
	name: Layer name
	visible: True to show, False to hide
	"""
	try:
		params = {
			"name": name,
			"visible": visible
		}
		result = send_to_rhino("set_layer_visibility", params)
		status = "visible" if visible else "hidden"
		return "Set layer '{0}' to {1}".format(name, status)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def list_layers() -> str:
	"""
	Get list of all layers in the document
	Returns layer names and their properties
	"""
	try:
		result = send_to_rhino("list_layers")
		return json.dumps(result, indent=2)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def measure_distance(point1_x: float, point1_y: float, point1_z: float,
					 point2_x: float, point2_y: float, point2_z: float) -> str:
	"""
	Measure distance between two points
	point1_x, point1_y, point1_z: First point coordinates
	point2_x, point2_y, point2_z: Second point coordinates
	"""
	try:
		params = {
			"point1": [point1_x, point1_y, point1_z],
			"point2": [point2_x, point2_y, point2_z]
		}
		result = send_to_rhino("measure_distance", params)
		distance = result.get("distance", 0)
		return "Distance: {0}".format(distance)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def measure_curve_length() -> str:
	"""
	Measure length of selected curve
	One curve must be selected in Rhino first
	"""
	try:
		result = send_to_rhino("measure_curve_length")
		length = result.get("length", 0)
		return "Curve length: {0}".format(length)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def measure_area() -> str:
	"""
	Measure area of selected surface or closed curve
	One surface or closed planar curve must be selected in Rhino first
	"""
	try:
		result = send_to_rhino("measure_area")
		area = result.get("area", 0)
		return "Area: {0}".format(area)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def measure_volume() -> str:
	"""
	Measure volume of selected solid
	One closed solid must be selected in Rhino first
	"""
	try:
		result = send_to_rhino("measure_volume")
		volume = result.get("volume", 0)
		return "Volume: {0}".format(volume)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def set_object_name(name: str) -> str:
	"""
	Set name for selected object
	name: Object name to set
	One object must be selected in Rhino first
	"""
	try:
		params = {"name": name}
		result = send_to_rhino("set_object_name", params)
		return "Set object name to '{0}'".format(name)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def set_object_color(color_r: int, color_g: int, color_b: int) -> str:
	"""
	Set color for selected objects
	color_r, color_g, color_b: RGB color values (0-255)
	Objects must be selected in Rhino first
	"""
	try:
		params = {"color": [color_r, color_g, color_b]}
		result = send_to_rhino("set_object_color", params)
		count = result.get("count", 0)
		return "Set color for {0} objects to RGB({1}, {2}, {3})".format(
			count, color_r, color_g, color_b)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def set_object_layer(layer_name: str) -> str:
	"""
	Move selected objects to a different layer
	layer_name: Target layer name
	Objects must be selected in Rhino first
	"""
	try:
		params = {"layer": layer_name}
		result = send_to_rhino("set_object_layer", params)
		count = result.get("count", 0)
		return "Moved {0} objects to layer '{1}'".format(count, layer_name)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def select_by_type(object_type: str) -> str:
	"""
	Select objects by type
	object_type: Type to select - 'point', 'curve', 'surface', 'polysurface', 'mesh'
	"""
	try:
		params = {"type": object_type}
		result = send_to_rhino("select_by_type", params)
		count = result.get("count", 0)
		return "Selected {0} {1} objects".format(count, object_type)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def select_by_layer(layer_name: str) -> str:
	"""
	Select all objects on a specific layer
	layer_name: Layer name to select objects from
	"""
	try:
		params = {"layer": layer_name}
		result = send_to_rhino("select_by_layer", params)
		count = result.get("count", 0)
		return "Selected {0} objects on layer '{1}'".format(count, layer_name)
	except Exception as e:
		return "Error: {0}".format(str(e))


@mcp.tool()
def unselect_all() -> str:
	"""
	Deselect all objects in Rhino
	Clears the current selection
	"""
	try:
		result = send_to_rhino("unselect_all")
		return "Deselected all objects"
	except Exception as e:
		return "Error: {0}".format(str(e))


def main():
	"""Run the MCP server"""
	mcp.run()


if __name__ == "__main__":
	main()
