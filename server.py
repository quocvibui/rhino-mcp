# Rhino Listener for MCP - Socket Server
# Compatible with CPython 3 (Rhino 8)
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
import Rhino
import System

# Import all command functions from rhino.commands
import rhino.commands as commands

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
			"create_point": commands.create_point,
			"create_line": commands.create_line,
			"create_circle": commands.create_circle,
			"create_arc": commands.create_arc,
			"create_ellipse": commands.create_ellipse,
			"create_polyline": commands.create_polyline,
			"create_curve": commands.create_curve,
			# 3D solids
			"create_box": commands.create_box,
			"create_sphere": commands.create_sphere,
			"create_cylinder": commands.create_cylinder,
			"create_cone": commands.create_cone,
			"create_torus": commands.create_torus,
			# Transformations
			"move_objects": commands.move_objects,
			"rotate_objects": commands.rotate_objects,
			"scale_objects": commands.scale_objects,
			"mirror_objects": commands.mirror_objects,
			"copy_objects": commands.copy_objects,
			"array_linear": commands.array_linear,
			"array_polar": commands.array_polar,
			"orient_objects": commands.orient_objects,
			# Boolean operations
			"boolean_union": commands.boolean_union,
			"boolean_difference": commands.boolean_difference,
			"boolean_intersection": commands.boolean_intersection,
			# Curve operations
			"join_curves": commands.join_curves,
			"explode_curves": commands.explode_curves,
			"offset_curve": commands.offset_curve,
			"fillet_curves": commands.fillet_curves,
			"extend_curve": commands.extend_curve,
			"create_rectangle": commands.create_rectangle,
			"create_spiral": commands.create_spiral,
			"create_nurbs_curve": commands.create_nurbs_curve,
			"create_blend_curve": commands.create_blend_curve,
			"divide_curve": commands.divide_curve_cmd,
			"divide_curve_length": commands.divide_curve_length_cmd,
			"split_curve": commands.split_curve,
			"close_curve": commands.close_curve,
			"reverse_curve": commands.reverse_curve,
			"rebuild_curve": commands.rebuild_curve,
			"project_curve_to_surface": commands.project_curve_to_surface,
			# Curve analysis
			"curve_closest_point": commands.curve_closest_point,
			"evaluate_curve": commands.evaluate_curve,
			"curve_start_end_points": commands.curve_start_end_points,
			"curve_curve_intersection": commands.curve_curve_intersection,
			# Surface operations
			"extrude_curve_straight": commands.extrude_curve_straight,
			"revolve_curve": commands.revolve_curve,
			"loft_curves": commands.loft_curves,
			"create_pipe": commands.create_pipe,
			"sweep1": commands.sweep1,
			"sweep2": commands.sweep2,
			"create_planar_surface": commands.create_planar_surface,
			"create_edge_surface": commands.create_edge_surface,
			"create_network_surface": commands.create_network_surface,
			"create_patch": commands.create_patch,
			"offset_surface": commands.offset_surface,
			"split_brep": commands.split_brep,
			"fillet_surfaces": commands.fillet_surfaces,
			"cap_planar_holes": commands.cap_planar_holes,
			"extrude_curve_along_curve": commands.extrude_curve_along_curve,
			"extrude_curve_to_point": commands.extrude_curve_to_point,
			"duplicate_edge_curves": commands.duplicate_edge_curves,
			"duplicate_surface_border": commands.duplicate_surface_border,
			"join_surfaces": commands.join_surfaces,
			"explode_polysurfaces": commands.explode_polysurfaces,
			"unroll_surface": commands.unroll_surface,
			# Mesh operations
			"create_mesh": commands.create_mesh,
			"create_planar_mesh": commands.create_planar_mesh,
			"mesh_from_surface": commands.mesh_from_surface,
			"mesh_boolean_union": commands.mesh_boolean_union,
			"mesh_boolean_difference": commands.mesh_boolean_difference,
			"mesh_boolean_intersection": commands.mesh_boolean_intersection,
			"join_meshes": commands.join_meshes,
			"mesh_to_nurb": commands.mesh_to_nurb,
			"mesh_offset": commands.mesh_offset,
			# Group operations
			"create_group": commands.create_group,
			"delete_group": commands.delete_group,
			"add_to_group": commands.add_to_group,
			"remove_from_group": commands.remove_from_group,
			"list_groups": commands.list_groups,
			"select_by_group": commands.select_by_group,
			# View operations
			"set_view_camera": commands.set_view_camera,
			"zoom_extents": commands.zoom_extents,
			"zoom_selected": commands.zoom_selected,
			"get_view_info": commands.get_view_info,
			"set_display_mode": commands.set_display_mode,
			"add_named_view": commands.add_named_view,
			"restore_named_view": commands.restore_named_view,
			# Block operations
			"create_block": commands.create_block,
			"insert_block": commands.insert_block,
			"explode_block": commands.explode_block,
			"delete_block": commands.delete_block,
			"list_blocks": commands.list_blocks,
			# Material operations
			"add_material_to_object": commands.add_material_to_object,
			"add_material_to_layer": commands.add_material_to_layer,
			"set_material_color": commands.set_material_color,
			"set_material_transparency": commands.set_material_transparency,
			"set_material_shine": commands.set_material_shine,
			# Object operations
			"hide_objects": commands.hide_objects,
			"show_objects": commands.show_objects,
			"lock_objects": commands.lock_objects,
			"unlock_objects": commands.unlock_objects,
			"is_object_solid": commands.is_object_solid,
			# Selection operations
			"select_by_name": commands.select_by_name,
			"last_created_objects": commands.last_created_objects,
			"invert_selection": commands.invert_selection,
			# Document operations
			"get_document_info": commands.get_document_info,
			"set_unit_system": commands.set_unit_system,
			"enable_redraw": commands.enable_redraw,
			# Annotation operations
			"add_text": commands.add_text,
			"add_text_dot": commands.add_text_dot,
			"add_leader": commands.add_leader,
			# User data operations
			"set_user_text": commands.set_user_text,
			"get_user_text": commands.get_user_text,
			"set_document_user_text": commands.set_document_user_text,
			"get_document_user_text": commands.get_document_user_text,
			# Layer operations
			"create_layer": commands.create_layer,
			"delete_layer": commands.delete_layer,
			"set_current_layer": commands.set_current_layer,
			"set_layer_color": commands.set_layer_color,
			"set_layer_visibility": commands.set_layer_visibility,
			"list_layers": commands.list_layers,
			# Analysis
			"measure_distance": commands.measure_distance,
			"measure_curve_length": commands.measure_curve_length,
			"measure_area": commands.measure_area,
			"measure_volume": commands.measure_volume,
			# Object properties
			"set_object_name": commands.set_object_name,
			"set_object_color": commands.set_object_color,
			"set_object_layer": commands.set_object_layer,
			# Selection
			"select_all": commands.select_all,
			"select_by_type": commands.select_by_type,
			"select_by_layer": commands.select_by_layer,
			"unselect_all": commands.unselect_all,
			"delete_selected": commands.delete_selected,
			"get_selected_objects": commands.get_selected_objects,
			"get_scene_info": commands.get_scene_info,
			# Code execution
			"execute_python_code": commands.execute_python_code,
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
	incomplete_data = b""

	try:
		while True:
			data = client_socket.recv(BUFFER_SIZE)
			if not data:
				break

			incomplete_data += data

			try:
				command = json.loads(incomplete_data.decode("utf-8"))
				incomplete_data = b""

				# Execute command on UI thread to avoid macOS threading crashes
				# Rhino requires all object modifications to happen on the main thread
				result_holder = [None]
				done_event = threading.Event()

				def run_on_ui():
					try:
						result_holder[0] = execute_command(command)
					except Exception as e:
						result_holder[0] = {"status": "error", "message": "Error: " + str(e)}
					finally:
						done_event.set()

				Rhino.RhinoApp.InvokeOnUiThread(System.Action(run_on_ui))
				done_event.wait(timeout=30)

				if result_holder[0] is None:
					response = {"status": "error", "message": "Command timed out waiting for UI thread"}
				else:
					response = result_holder[0]

				response_json = json.dumps(response)
				client_socket.send(response_json.encode("utf-8"))
				break

			except ValueError:
				continue

	except Exception as e:
		error_msg = json.dumps({"status": "error", "message": "Connection error: " + str(e)})
		try:
			client_socket.send(error_msg.encode("utf-8"))
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

		print("=" * 60)
		print("RhinoMCP Listener")
		print("=" * 60)
		print("Active on " + SERVER_HOST + ":" + str(SERVER_PORT))
		print("135 commands available")
		print("JSON protocol")
		print("Ready to receive commands")
		print("=" * 60)

		while True:
			try:
				client_socket, client_address = server_socket.accept()
				client_thread = threading.Thread(target=handle_client, args=(client_socket,))
				client_thread.daemon = True
				client_thread.start()
			except Exception as e:
				print("Connection error: " + str(e))
				continue

	except Exception as e:
		print("Failed to start listener: " + str(e))
	finally:
		if server_socket:
			try:
				server_socket.close()
			except:
				pass


# ============================================================================
# STARTUP
# ============================================================================

print("=" * 60)
print("RhinoMCP Listener")
print("=" * 60)
print("Starting background listener thread...")

listener_thread = threading.Thread(target=socket_server)
listener_thread.daemon = True
listener_thread.start()

print("Listener started successfully")
print("135 commands ready")
print("=" * 60)
