# Rhino Listener for MCP - Socket Server
# Compatible with IronPython 2.7 (Rhino 7)
# Handles socket communication and routes commands to rhino module

import sys
import os

# Add the script directory to Python path to enable imports
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
	sys.path.insert(0, script_dir)

import socket
import threading
import json
import rhinoscriptsyntax as rs

# Import all command functions from rhino.commands
from rhino.commands import (
	# Basic geometry
	create_point,
	create_line,
	create_circle,
	create_arc,
	create_ellipse,
	create_polyline,
	create_curve,
	# 3D solids
	create_box,
	create_sphere,
	create_cylinder,
	create_cone,
	create_torus,
	# Transformations
	move_objects,
	rotate_objects,
	scale_objects,
	mirror_objects,
	copy_objects,
	array_linear,
	# Boolean operations
	boolean_union,
	boolean_difference,
	boolean_intersection,
	# Curve operations
	join_curves,
	explode_curves,
	offset_curve,
	fillet_curves,
	extend_curve,
	# Surface operations
	extrude_curve_straight,
	revolve_curve,
	loft_curves,
	# Layer operations
	create_layer,
	delete_layer,
	set_current_layer,
	set_layer_color,
	set_layer_visibility,
	list_layers,
	# Analysis
	measure_distance,
	measure_curve_length,
	measure_area,
	measure_volume,
	# Object properties
	set_object_name,
	set_object_color,
	set_object_layer,
	# Selection
	select_all,
	select_by_type,
	select_by_layer,
	unselect_all,
	delete_selected,
	get_selected_objects,
	get_scene_info,
	# Code execution
	execute_python_code
)

SERVER_HOST = "localhost"
SERVER_PORT = 54321
BUFFER_SIZE = 8192


# ============================================================================
# COMMAND MAPPING AND EXECUTION
# ============================================================================

def execute_command(command_dict):
	"""Execute JSON command and return JSON response"""
	try:
		cmd_type = command_dict.get("type", "")
		params = command_dict.get("params", {})

		command_map = {
			# Basic geometry
			"create_point": create_point,
			"create_line": create_line,
			"create_circle": create_circle,
			"create_arc": create_arc,
			"create_ellipse": create_ellipse,
			"create_polyline": create_polyline,
			"create_curve": create_curve,
			# 3D solids
			"create_box": create_box,
			"create_sphere": create_sphere,
			"create_cylinder": create_cylinder,
			"create_cone": create_cone,
			"create_torus": create_torus,
			# Transformations
			"move_objects": move_objects,
			"rotate_objects": rotate_objects,
			"scale_objects": scale_objects,
			"mirror_objects": mirror_objects,
			"copy_objects": copy_objects,
			"array_linear": array_linear,
			# Boolean operations
			"boolean_union": boolean_union,
			"boolean_difference": boolean_difference,
			"boolean_intersection": boolean_intersection,
			# Curve operations
			"join_curves": join_curves,
			"explode_curves": explode_curves,
			"offset_curve": offset_curve,
			"fillet_curves": fillet_curves,
			"extend_curve": extend_curve,
			# Surface operations
			"extrude_curve_straight": extrude_curve_straight,
			"revolve_curve": revolve_curve,
			"loft_curves": loft_curves,
			# Layer operations
			"create_layer": create_layer,
			"delete_layer": delete_layer,
			"set_current_layer": set_current_layer,
			"set_layer_color": set_layer_color,
			"set_layer_visibility": set_layer_visibility,
			"list_layers": list_layers,
			# Analysis
			"measure_distance": measure_distance,
			"measure_curve_length": measure_curve_length,
			"measure_area": measure_area,
			"measure_volume": measure_volume,
			# Object properties
			"set_object_name": set_object_name,
			"set_object_color": set_object_color,
			"set_object_layer": set_object_layer,
			# Selection
			"select_all": select_all,
			"select_by_type": select_by_type,
			"select_by_layer": select_by_layer,
			"unselect_all": unselect_all,
			"delete_selected": delete_selected,
			"get_selected_objects": get_selected_objects,
			"get_scene_info": get_scene_info,
			# Code execution
			"execute_python_code": execute_python_code
		}

		handler = command_map.get(cmd_type)
		if handler:
			return handler(params)
		else:
			return {"status": "error", "message": "Unknown command: " + cmd_type}

	except Exception as e:
		return {"status": "error", "message": "Error: " + str(e)}


# ============================================================================
# SOCKET SERVER
# ============================================================================

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

		print "=" * 60
		print "RhinoMCP Listener"
		print "=" * 60
		print "Active on " + SERVER_HOST + ":" + str(SERVER_PORT)
		print "50 commands available"
		print "JSON protocol"
		print "Ready to receive commands"
		print "=" * 60

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


# ============================================================================
# STARTUP
# ============================================================================

print "=" * 60
print "RhinoMCP Listener"
print "=" * 60
print "Starting background listener thread..."

listener_thread = threading.Thread(target=socket_server)
listener_thread.daemon = True
listener_thread.start()

print "Listener started successfully"
print "50 commands ready"
print "=" * 60
