# Rhino Listener for MCP - JSON Protocol
# Compatible with IronPython 2.7 (Rhino 7)

import socket
import threading
import json
import rhinoscriptsyntax as rs

SERVER_HOST = "localhost"
SERVER_PORT = 54321
BUFFER_SIZE = 8192


def create_point(params):
	"""Create a point"""
	x = params.get("x", 0)
	y = params.get("y", 0)
	z = params.get("z", 0)
	point_id = rs.AddPoint(x, y, z)
	if point_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(point_id), "type": "point"}}
	return {"status": "error", "message": "Failed to create point"}


def create_line(params):
	"""Create a line"""
	start = params.get("start", [0, 0, 0])
	end = params.get("end", [1, 1, 1])
	line_id = rs.AddLine(start, end)
	if line_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(line_id), "type": "line"}}
	return {"status": "error", "message": "Failed to create line"}


def create_box(params):
	"""Create a box"""
	width = params.get("width", 10)
	depth = params.get("depth", 10)
	height = params.get("height", 10)
	x = params.get("x", 0)
	y = params.get("y", 0)
	z = params.get("z", 0)

	p0 = (x, y, z)
	p1 = (x + width, y, z)
	p2 = (x + width, y + depth, z)
	p3 = (x, y + depth, z)
	p4 = (x, y, z + height)
	p5 = (x + width, y, z + height)
	p6 = (x + width, y + depth, z + height)
	p7 = (x, y + depth, z + height)

	box_id = rs.AddBox([p0, p1, p2, p3, p4, p5, p6, p7])
	if box_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(box_id), "type": "box"}}
	return {"status": "error", "message": "Failed to create box"}


def create_sphere(params):
	"""Create a sphere"""
	center = params.get("center", [0, 0, 0])
	radius = params.get("radius", 5)
	sphere_id = rs.AddSphere(center, radius)
	if sphere_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(sphere_id), "type": "sphere"}}
	return {"status": "error", "message": "Failed to create sphere"}


def create_circle(params):
	"""Create a circle"""
	center = params.get("center", [0, 0, 0])
	radius = params.get("radius", 5)
	circle_id = rs.AddCircle(center, radius)
	if circle_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(circle_id), "type": "circle"}}
	return {"status": "error", "message": "Failed to create circle"}


def create_cylinder(params):
	"""Create a cylinder"""
	base = params.get("base", [0, 0, 0])
	height = params.get("height", 10)
	radius = params.get("radius", 5)

	base_pt = tuple(base)
	top_pt = (base[0], base[1], base[2] + height)
	plane = rs.PlaneFromNormal(base_pt, (0, 0, 1))
	circle = rs.AddCircle(plane, radius)
	cylinder = rs.ExtrudeCurveStraight(circle, base_pt, top_pt)

	if cylinder:
		rs.DeleteObject(circle)
		rs.Redraw()
		return {"status": "success", "result": {"id": str(cylinder), "type": "cylinder"}}
	return {"status": "error", "message": "Failed to create cylinder"}


def create_cone(params):
	"""Create a cone"""
	base = params.get("base", [0, 0, 0])
	height = params.get("height", 10)
	radius = params.get("radius", 5)

	plane = rs.PlaneFromNormal(base, (0, 0, 1))
	cone_id = rs.AddCone(plane, height, radius)

	if cone_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(cone_id), "type": "cone"}}
	return {"status": "error", "message": "Failed to create cone"}


def create_polyline(params):
	"""Create a polyline"""
	points = params.get("points", [[0, 0, 0], [1, 1, 1], [2, 0, 0]])
	points_tuple = [tuple(pt) for pt in points]
	polyline_id = rs.AddPolyline(points_tuple)

	if polyline_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(polyline_id), "type": "polyline"}}
	return {"status": "error", "message": "Failed to create polyline"}


def create_curve(params):
	"""Create an interpolated curve"""
	points = params.get("points", [[0, 0, 0], [1, 1, 1], [2, 0, 0]])
	degree = params.get("degree", 3)
	points_tuple = [tuple(pt) for pt in points]
	curve_id = rs.AddInterpCurve(points_tuple, degree)

	if curve_id:
		rs.Redraw()
		return {"status": "success", "result": {"id": str(curve_id), "type": "curve"}}
	return {"status": "error", "message": "Failed to create curve"}


def select_all(params):
	"""Select all objects"""
	objects = rs.AllObjects()
	if objects:
		rs.SelectObjects(objects)
		return {"status": "success", "result": {"count": len(objects)}}
	return {"status": "success", "result": {"count": 0}}


def delete_selected(params):
	"""Delete selected objects"""
	objects = rs.SelectedObjects()
	if objects:
		count = len(objects)
		rs.DeleteObjects(objects)
		rs.Redraw()
		return {"status": "success", "result": {"deleted": count}}
	return {"status": "success", "result": {"deleted": 0}}


def get_selected_objects(params):
	"""Get information about selected objects"""
	objects = rs.SelectedObjects()
	type_names = {1: "Point", 2: "PointCloud", 4: "Curve", 8: "Surface", 16: "Polysurface", 32: "Mesh"}

	objects_list = []
	if objects:
		for obj in objects:
			obj_type = rs.ObjectType(obj)
			type_name = type_names.get(obj_type, "Other")

			bbox = rs.BoundingBox(obj)
			if bbox:
				center = [(bbox[0][i] + bbox[6][i]) / 2 for i in range(3)]
			else:
				center = [0, 0, 0]

			objects_list.append({
				"id": str(obj),
				"type": type_name,
				"layer": rs.ObjectLayer(obj),
				"center": center
			})

	return {"status": "success", "result": {"count": len(objects_list), "objects": objects_list}}


def get_scene_info(params):
	"""Get comprehensive scene information"""
	all_objects = rs.AllObjects()
	layers = rs.LayerNames()
	units = rs.UnitSystemName()

	obj_count = len(all_objects) if all_objects else 0
	layer_count = len(layers) if layers else 0

	type_counts = {}
	type_names = {1: "Point", 2: "PointCloud", 4: "Curve", 8: "Surface", 16: "Polysurface", 32: "Mesh"}

	objects_list = []
	if all_objects:
		for obj in all_objects[:30]:
			obj_type = rs.ObjectType(obj)
			type_name = type_names.get(obj_type, "Other")
			type_counts[type_name] = type_counts.get(type_name, 0) + 1

			bbox = rs.BoundingBox(obj)
			if bbox:
				center = [(bbox[0][i] + bbox[6][i]) / 2 for i in range(3)]
			else:
				center = [0, 0, 0]

			objects_list.append({
				"id": str(obj),
				"type": type_name,
				"layer": rs.ObjectLayer(obj),
				"center": center
			})

	result = {
		"total_objects": obj_count,
		"total_layers": layer_count,
		"units": str(units),
		"object_counts": type_counts,
		"objects": objects_list
	}

	return {"status": "success", "result": result}


def execute_command(command_dict):
	"""Execute JSON command and return JSON response"""
	try:
		cmd_type = command_dict.get("type", "")
		params = command_dict.get("params", {})

		command_map = {
			"create_point": create_point,
			"create_line": create_line,
			"create_box": create_box,
			"create_sphere": create_sphere,
			"create_circle": create_circle,
			"create_cylinder": create_cylinder,
			"create_cone": create_cone,
			"create_polyline": create_polyline,
			"create_curve": create_curve,
			"get_scene_info": get_scene_info,
			"select_all": select_all,
			"delete_selected": delete_selected,
			"get_selected_objects": get_selected_objects
		}

		handler = command_map.get(cmd_type)
		if handler:
			return handler(params)
		else:
			return {"status": "error", "message": "Unknown command: " + cmd_type}

	except Exception as e:
		return {"status": "error", "message": "Error: " + str(e)}


def handle_client(client_socket):
	"""Handle incoming client connection"""
	incomplete_data = ""

	try:
		while True:
			data = client_socket.recv(BUFFER_SIZE)
			if not data:
				break

			incomplete_data += data

			try:
				command = json.loads(incomplete_data)
				incomplete_data = ""

				response = execute_command(command)
				response_json = json.dumps(response)
				client_socket.send(response_json)
				break

			except ValueError:
				continue

	except Exception as e:
		error_msg = json.dumps({"status": "error", "message": "Connection error: " + str(e)})
		try:
			client_socket.send(error_msg)
		except:
			pass
	finally:
		try:
			client_socket.close()
		except:
			pass


def socket_server():
	"""Main socket server loop"""
	server_socket = None
	try:
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		server_socket.bind((SERVER_HOST, SERVER_PORT))
		server_socket.listen(5)

		print "RhinoMCP Listener active on " + SERVER_HOST + ":" + str(SERVER_PORT)
		print "Using JSON protocol"
		print "Ready to receive commands"

		while True:
			try:
				client_socket, client_address = server_socket.accept()
				client_thread = threading.Thread(target=handle_client, args=(client_socket,))
				client_thread.daemon = True
				client_thread.start()
			except Exception as e:
				print "Connection error: " + str(e)
				continue

	except Exception as e:
		print "Failed to start listener: " + str(e)
	finally:
		if server_socket:
			try:
				server_socket.close()
			except:
				pass


print "=" * 60
print "RhinoMCP Listener v2.0 - JSON Protocol"
print "=" * 60
print "Starting background listener thread..."

listener_thread = threading.Thread(target=socket_server)
listener_thread.daemon = True
listener_thread.start()

print "Listener started successfully"
print "Commands: create_point, create_line, create_box, create_sphere, get_scene_info"
print "Protocol: JSON"
print "=" * 60
