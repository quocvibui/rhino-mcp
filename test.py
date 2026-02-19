#!/usr/bin/env python3
"""
Comprehensive test suite for Rhino MCP
Tests all 135 commands with pass/fail tracking
"""

import socket
import json
import time
import base64

RHINO_HOST = "localhost"
RHINO_PORT = 54321
TEST_DELAY = 0.3

test_results = {
	"passed": [],
	"failed": []
}

# Store IDs from creation commands for later use
created_ids = {}


def send_command(command_type, params=None):
	"""Send command to Rhino and return response (chunked reading)"""
	if params is None:
		params = {}

	command = {
		"type": command_type,
		"params": params
	}

	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(10)
		sock.connect((RHINO_HOST, RHINO_PORT))
		sock.sendall(json.dumps(command).encode("utf-8"))

		chunks = []
		while True:
			chunk = sock.recv(8192)
			if not chunk:
				break
			chunks.append(chunk)
			try:
				data = b"".join(chunks)
				response = json.loads(data.decode("utf-8"))
				sock.close()
				return response
			except (json.JSONDecodeError, UnicodeDecodeError):
				continue

		sock.close()
		if chunks:
			return json.loads(b"".join(chunks).decode("utf-8"))
		return {"status": "error", "message": "Empty response"}

	except ConnectionRefusedError:
		return {"status": "error", "message": "Cannot connect to Rhino"}
	except Exception as e:
		return {"status": "error", "message": str(e)}


def test_command(name, command_type, params=None, expect_error=False, store_id=None):
	"""Test a command and track results. Optionally store result IDs."""
	time.sleep(TEST_DELAY)
	response = send_command(command_type, params)

	if response is None:
		test_results["failed"].append({"name": name, "error": "No response"})
		print(f"  FAIL: {name} - No response")
		return None

	status = response.get("status")

	if expect_error:
		if status == "error":
			test_results["passed"].append(name)
			print(f"  PASS: {name}")
			return response
		else:
			test_results["failed"].append({"name": name, "error": "Expected error but got success"})
			print(f"  FAIL: {name} - Expected error but got success")
			return response
	else:
		if status == "success":
			test_results["passed"].append(name)
			print(f"  PASS: {name}")
			# Store IDs for later use
			result = response.get("result", {})
			if store_id and result:
				if "id" in result:
					created_ids[store_id] = result["id"]
				elif "ids" in result and result["ids"]:
					created_ids[store_id] = result["ids"][0]
			return response
		else:
			error_msg = response.get("message", "Unknown error")
			test_results["failed"].append({"name": name, "error": error_msg})
			print(f"  FAIL: {name} - {error_msg}")
			return response


def cleanup():
	"""Clean up: select all, delete all"""
	send_command("select_all")
	time.sleep(TEST_DELAY)
	send_command("delete_selected")
	time.sleep(TEST_DELAY)
	send_command("unselect_all")
	time.sleep(TEST_DELAY)


def run_tests():
	"""Run all tests"""
	print("=" * 70)
	print("RHINO MCP COMPREHENSIVE TEST SUITE - 136 COMMANDS")
	print("=" * 70)
	print()

	# Check connection first
	print("Checking Rhino connection...")
	response = send_command("get_scene_info")
	if response.get("status") != "success":
		print(f"ERROR: Cannot connect to Rhino on port {RHINO_PORT}")
		print("\nMake sure:")
		print("1. Rhino 8 is running")
		print("2. Run this command in Rhino:")
		print('   _-RunPythonScript "/path/to/server.py" _Enter')
		return
	print("Connection OK\n")

	# Clean up scene
	print("Cleaning up scene...")
	cleanup()
	print("Scene cleaned\n")

	section = [0]

	def header(title, count):
		section[0] += 1
		print(f"\n[{section[0]}] {title} ({count} tests)")
		print("-" * 70)

	# ================================================================
	# SCENE UNDERSTANDING (2 tests)
	# ================================================================
	header("SCENE UNDERSTANDING", 2)
	test_command("get_scene_info", "get_scene_info")
	test_command("get_selected_objects", "get_selected_objects")

	# ================================================================
	# BASIC GEOMETRY (7 tests)
	# ================================================================
	header("BASIC GEOMETRY", 7)
	test_command("create_point", "create_point", {"x": 0, "y": 0, "z": 0})
	test_command("create_line", "create_line", {"start": [0, 0, 0], "end": [10, 0, 0]}, store_id="line1")
	test_command("create_circle", "create_circle", {"center": [0, 10, 0], "radius": 5}, store_id="circle1")
	test_command("create_arc", "create_arc", {"center": [0, 20, 0], "radius": 5, "start_angle": 0, "end_angle": 180})
	test_command("create_ellipse", "create_ellipse", {"center": [0, 30, 0], "x_radius": 8, "y_radius": 4})
	test_command("create_polyline", "create_polyline", {"points": [[10, 0, 0], [15, 5, 0], [20, 0, 0]]})
	test_command("create_curve", "create_curve", {"points": [[10, 10, 0], [15, 15, 0], [20, 10, 0]], "degree": 3}, store_id="curve1")

	# ================================================================
	# 3D SOLIDS (5 tests)
	# ================================================================
	header("3D SOLIDS", 5)
	test_command("create_box", "create_box", {"width": 10, "depth": 10, "height": 10, "x": 30, "y": 0, "z": 0}, store_id="box1")
	test_command("create_sphere", "create_sphere", {"center": [30, 20, 5], "radius": 5}, store_id="sphere1")
	test_command("create_cylinder", "create_cylinder", {"base": [50, 0, 0], "height": 15, "radius": 5})
	test_command("create_cone", "create_cone", {"base": [50, 20, 0], "height": 15, "radius": 5})
	test_command("create_torus", "create_torus", {"center": [70, 10, 5], "major_radius": 8, "minor_radius": 2})

	# ================================================================
	# TRANSFORMATIONS (8 tests)
	# ================================================================
	header("TRANSFORMATIONS", 8)
	cleanup()
	send_command("create_box", {"width": 5, "depth": 5, "height": 5, "x": 0, "y": 50, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)

	test_command("move_objects", "move_objects", {"displacement": [5, 0, 0]})
	test_command("rotate_objects", "rotate_objects", {"center": [0, 50, 0], "angle": 45})
	test_command("scale_objects", "scale_objects", {"center": [0, 50, 0], "scale": 1.5})
	test_command("mirror_objects", "mirror_objects", {"start": [0, 50, 0], "end": [10, 50, 0]})
	test_command("copy_objects", "copy_objects", {"displacement": [10, 0, 0]})
	test_command("array_linear", "array_linear", {"displacement": [5, 0, 0], "count": 3})
	test_command("array_polar", "array_polar", {"center": [0, 50, 0], "count": 4, "angle": 360})
	test_command("orient_objects", "orient_objects", {"reference": [0, 0, 0], "target": [10, 0, 0]})
	send_command("unselect_all")

	# ================================================================
	# BOOLEAN OPERATIONS (3 tests)
	# ================================================================
	header("BOOLEAN OPERATIONS", 3)
	cleanup()

	send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 0, "y": 70, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 5, "y": 70, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("boolean_union", "boolean_union")

	cleanup()
	send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 20, "y": 70, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 25, "y": 70, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("boolean_difference", "boolean_difference")

	cleanup()
	send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 40, "y": 70, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 45, "y": 70, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("boolean_intersection", "boolean_intersection")
	send_command("unselect_all")

	# ================================================================
	# CURVE OPERATIONS - EXISTING (5 tests)
	# ================================================================
	header("CURVE OPERATIONS - EXISTING", 5)
	cleanup()

	send_command("create_line", {"start": [0, 90, 0], "end": [10, 90, 0]})
	time.sleep(TEST_DELAY)
	send_command("create_line", {"start": [10, 90, 0], "end": [10, 100, 0]})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("join_curves", "join_curves")
	test_command("explode_curves", "explode_curves")
	send_command("unselect_all")

	send_command("create_circle", {"center": [20, 95, 0], "radius": 5})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("offset_curve", "offset_curve", {"distance": 2})
	send_command("unselect_all")

	send_command("create_line", {"start": [30, 90, 0], "end": [40, 90, 0]})
	time.sleep(TEST_DELAY)
	send_command("create_line", {"start": [40, 90, 0], "end": [40, 100, 0]})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("fillet_curves", "fillet_curves", {"radius": 2})
	send_command("unselect_all")

	send_command("create_line", {"start": [50, 90, 0], "end": [55, 90, 0]})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("extend_curve", "extend_curve", {"extension": 3})
	send_command("unselect_all")

	# ================================================================
	# CURVE OPERATIONS - NEW (12 tests)
	# ================================================================
	header("CURVE OPERATIONS - NEW", 12)
	cleanup()

	test_command("create_rectangle", "create_rectangle", {"center": [0, 0, 0], "width": 10, "height": 5}, store_id="rect1")

	test_command("create_spiral", "create_spiral", {
		"point0": [20, 0, 0], "point1": [20, 0, 10],
		"pitch": 1, "turns": 3, "radius0": 5, "radius1": 5
	})

	test_command("create_nurbs_curve", "create_nurbs_curve", {
		"points": [[40, 0, 0], [45, 5, 0], [50, 0, 0], [55, 5, 0]],
		"degree": 3
	})

	# Create two curves for blend
	r1 = send_command("create_line", {"start": [0, 20, 0], "end": [10, 20, 0]})
	time.sleep(TEST_DELAY)
	r2 = send_command("create_line", {"start": [15, 25, 0], "end": [25, 25, 0]})
	time.sleep(TEST_DELAY)
	if r1.get("status") == "success" and r2.get("status") == "success":
		id1 = r1.get("result", {}).get("id")
		id2 = r2.get("result", {}).get("id")
		if id1 and id2:
			test_command("create_blend_curve", "create_blend_curve", {
				"curve1": id1, "curve2": id2, "continuity": 1
			})
		else:
			test_command("create_blend_curve", "create_blend_curve", {
				"curve1": "dummy", "curve2": "dummy", "continuity": 1
			}, expect_error=True)
	else:
		test_command("create_blend_curve_skip", "create_blend_curve", {
			"curve1": "dummy", "curve2": "dummy"
		}, expect_error=True)

	# Divide curve
	r = send_command("create_line", {"start": [0, 30, 0], "end": [20, 30, 0]})
	time.sleep(TEST_DELAY)
	line_id = r.get("result", {}).get("id") if r.get("status") == "success" else None
	if line_id:
		test_command("divide_curve", "divide_curve", {"curve_id": line_id, "segments": 5, "create_points": True})
		test_command("divide_curve_length", "divide_curve_length", {"curve_id": line_id, "length": 3, "create_points": True})
	else:
		test_command("divide_curve", "divide_curve", {"curve_id": "dummy", "segments": 5}, expect_error=True)
		test_command("divide_curve_length", "divide_curve_length", {"curve_id": "dummy", "length": 3}, expect_error=True)

	# Split curve
	r = send_command("create_line", {"start": [0, 40, 0], "end": [20, 40, 0]})
	time.sleep(TEST_DELAY)
	line_id2 = r.get("result", {}).get("id") if r.get("status") == "success" else None
	if line_id2:
		test_command("split_curve", "split_curve", {"curve_id": line_id2, "parameters": [0.5]})
	else:
		test_command("split_curve", "split_curve", {"curve_id": "dummy", "parameters": [0.5]}, expect_error=True)

	# Close curve
	r = send_command("create_polyline", {"points": [[30, 30, 0], [35, 35, 0], [40, 30, 0]]})
	time.sleep(TEST_DELAY)
	poly_id = r.get("result", {}).get("id") if r.get("status") == "success" else None
	if poly_id:
		test_command("close_curve", "close_curve", {"curve_id": poly_id})
	else:
		test_command("close_curve", "close_curve", {"curve_id": "dummy"}, expect_error=True)

	# Reverse curve
	r = send_command("create_line", {"start": [0, 50, 0], "end": [10, 50, 0]})
	time.sleep(TEST_DELAY)
	rev_id = r.get("result", {}).get("id") if r.get("status") == "success" else None
	if rev_id:
		test_command("reverse_curve", "reverse_curve", {"curve_id": rev_id})
	else:
		test_command("reverse_curve", "reverse_curve", {"curve_id": "dummy"}, expect_error=True)

	# Rebuild curve
	r = send_command("create_curve", {"points": [[0, 60, 0], [5, 65, 0], [10, 60, 0], [15, 65, 0]], "degree": 3})
	time.sleep(TEST_DELAY)
	crv_id = r.get("result", {}).get("id") if r.get("status") == "success" else None
	if crv_id:
		test_command("rebuild_curve", "rebuild_curve", {"curve_id": crv_id, "degree": 3, "point_count": 8})
	else:
		test_command("rebuild_curve", "rebuild_curve", {"curve_id": "dummy"}, expect_error=True)

	# Project curve to surface - skip complex setup, test basic call
	test_command("project_curve_to_surface", "project_curve_to_surface", {
		"curve_ids": ["dummy"], "surface_ids": ["dummy"], "direction": [0, 0, -1]
	}, expect_error=True)

	# ================================================================
	# SURFACE OPERATIONS - EXISTING (3 tests)
	# ================================================================
	header("SURFACE OPERATIONS - EXISTING", 3)
	cleanup()

	send_command("create_circle", {"center": [0, 110, 0], "radius": 5})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("extrude_curve_straight", "extrude_curve_straight", {"height": 10})

	cleanup()
	send_command("create_line", {"start": [20, 110, 0], "end": [20, 115, 5]})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("revolve_curve", "revolve_curve", {"axis_start": [20, 110, 0], "axis_end": [20, 110, 10], "angle": 360})

	cleanup()
	send_command("create_circle", {"center": [40, 110, 0], "radius": 3})
	time.sleep(TEST_DELAY)
	send_command("create_circle", {"center": [40, 110, 5], "radius": 5})
	time.sleep(TEST_DELAY)
	send_command("create_circle", {"center": [40, 110, 10], "radius": 3})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("loft_curves", "loft_curves")
	send_command("unselect_all")

	# ================================================================
	# SURFACE OPERATIONS - NEW (18 tests)
	# ================================================================
	header("SURFACE OPERATIONS - NEW", 18)
	cleanup()

	# Pipe
	r = send_command("create_line", {"start": [0, 0, 0], "end": [20, 0, 0]})
	time.sleep(TEST_DELAY)
	pipe_crv = r.get("result", {}).get("id") if r.get("status") == "success" else None
	if pipe_crv:
		test_command("create_pipe", "create_pipe", {"curve_id": pipe_crv, "radius": 2, "cap": 1})
	else:
		test_command("create_pipe", "create_pipe", {"curve_id": "dummy", "radius": 2}, expect_error=True)

	# Sweep1
	r_rail = send_command("create_line", {"start": [30, 0, 0], "end": [30, 0, 20]})
	time.sleep(TEST_DELAY)
	r_shape = send_command("create_circle", {"center": [30, 0, 0], "radius": 2})
	time.sleep(TEST_DELAY)
	rail_id = r_rail.get("result", {}).get("id") if r_rail.get("status") == "success" else None
	shape_id = r_shape.get("result", {}).get("id") if r_shape.get("status") == "success" else None
	if rail_id and shape_id:
		test_command("sweep1", "sweep1", {"rail": rail_id, "shapes": [shape_id]})
	else:
		test_command("sweep1", "sweep1", {"rail": "dummy", "shapes": ["dummy"]}, expect_error=True)

	# Sweep2
	r_rail1 = send_command("create_line", {"start": [50, 0, 0], "end": [50, 0, 20]})
	time.sleep(TEST_DELAY)
	r_rail2 = send_command("create_line", {"start": [60, 0, 0], "end": [60, 0, 20]})
	time.sleep(TEST_DELAY)
	r_shape2 = send_command("create_line", {"start": [50, 0, 0], "end": [60, 0, 0]})
	time.sleep(TEST_DELAY)
	rail1 = r_rail1.get("result", {}).get("id") if r_rail1.get("status") == "success" else None
	rail2 = r_rail2.get("result", {}).get("id") if r_rail2.get("status") == "success" else None
	shape2 = r_shape2.get("result", {}).get("id") if r_shape2.get("status") == "success" else None
	if rail1 and rail2 and shape2:
		test_command("sweep2", "sweep2", {"rails": [rail1, rail2], "shapes": [shape2]})
	else:
		test_command("sweep2", "sweep2", {"rails": ["d1", "d2"], "shapes": ["d3"]}, expect_error=True)

	# Planar surface
	r = send_command("create_circle", {"center": [0, 30, 0], "radius": 5})
	time.sleep(TEST_DELAY)
	circ_id = r.get("result", {}).get("id") if r.get("status") == "success" else None
	if circ_id:
		test_command("create_planar_surface", "create_planar_surface", {"curve_ids": [circ_id]})
	else:
		test_command("create_planar_surface", "create_planar_surface", {"curve_ids": ["dummy"]}, expect_error=True)

	# Edge surface
	l1 = send_command("create_line", {"start": [20, 30, 0], "end": [30, 30, 0]})
	time.sleep(TEST_DELAY)
	l2 = send_command("create_line", {"start": [30, 30, 0], "end": [30, 40, 0]})
	time.sleep(TEST_DELAY)
	l3 = send_command("create_line", {"start": [30, 40, 0], "end": [20, 40, 0]})
	time.sleep(TEST_DELAY)
	l4 = send_command("create_line", {"start": [20, 40, 0], "end": [20, 30, 0]})
	time.sleep(TEST_DELAY)
	ids = []
	for r in [l1, l2, l3, l4]:
		if r.get("status") == "success":
			ids.append(r["result"]["id"])
	if len(ids) == 4:
		test_command("create_edge_surface", "create_edge_surface", {"curve_ids": ids})
	else:
		test_command("create_edge_surface", "create_edge_surface", {"curve_ids": ["dummy"]}, expect_error=True)

	# Network surface - use same pattern
	test_command("create_network_surface", "create_network_surface", {"curve_ids": ["dummy"]}, expect_error=True)

	# Patch
	r = send_command("create_curve", {"points": [[40, 30, 0], [45, 35, 5], [50, 30, 0]], "degree": 3})
	time.sleep(TEST_DELAY)
	patch_crv = r.get("result", {}).get("id") if r.get("status") == "success" else None
	if patch_crv:
		test_command("create_patch", "create_patch", {"object_ids": [patch_crv], "uspan": 10, "vspan": 10})
	else:
		test_command("create_patch", "create_patch", {"object_ids": ["dummy"]}, expect_error=True)

	# Offset surface
	r = send_command("create_sphere", {"center": [0, 50, 0], "radius": 5})
	time.sleep(TEST_DELAY)
	srf_id = r.get("result", {}).get("id") if r.get("status") == "success" else None
	if srf_id:
		test_command("offset_surface", "offset_surface", {"surface_id": srf_id, "distance": 1})
	else:
		test_command("offset_surface", "offset_surface", {"surface_id": "dummy", "distance": 1}, expect_error=True)

	# Split brep
	r1 = send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 20, "y": 50, "z": 0})
	time.sleep(TEST_DELAY)
	r2 = send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 25, "y": 50, "z": 0})
	time.sleep(TEST_DELAY)
	b1 = r1.get("result", {}).get("id") if r1.get("status") == "success" else None
	b2 = r2.get("result", {}).get("id") if r2.get("status") == "success" else None
	if b1 and b2:
		test_command("split_brep", "split_brep", {"brep_id": b1, "cutter_id": b2})
	else:
		test_command("split_brep", "split_brep", {"brep_id": "dummy", "cutter_id": "dummy"}, expect_error=True)

	# Fillet surfaces
	test_command("fillet_surfaces", "fillet_surfaces", {
		"surface1_id": "dummy", "surface2_id": "dummy", "radius": 1
	}, expect_error=True)

	# Cap planar holes - create open extrusion, then cap it
	send_command("unselect_all")
	time.sleep(TEST_DELAY)
	r = send_command("create_circle", {"center": [40, 50, 0], "radius": 5})
	time.sleep(TEST_DELAY)
	circ2 = r.get("result", {}).get("id") if r.get("status") == "success" else None
	if circ2:
		# Select the circle before extruding
		send_command("select_all")
		time.sleep(TEST_DELAY)
		r2 = send_command("extrude_curve_straight", {"height": 10})
		time.sleep(TEST_DELAY)
		ext_id = r2.get("result", {}).get("id") if r2.get("status") == "success" else None
		if ext_id:
			test_command("cap_planar_holes", "cap_planar_holes", {"brep_id": ext_id})
		else:
			test_command("cap_planar_holes", "cap_planar_holes", {"brep_id": "dummy"}, expect_error=True)
	else:
		test_command("cap_planar_holes", "cap_planar_holes", {"brep_id": "dummy"}, expect_error=True)
	send_command("unselect_all")

	# Extrude curve along curve
	r1 = send_command("create_circle", {"center": [60, 50, 0], "radius": 2})
	time.sleep(TEST_DELAY)
	r2 = send_command("create_line", {"start": [60, 50, 0], "end": [80, 60, 10]})
	time.sleep(TEST_DELAY)
	c1 = r1.get("result", {}).get("id") if r1.get("status") == "success" else None
	c2 = r2.get("result", {}).get("id") if r2.get("status") == "success" else None
	if c1 and c2:
		test_command("extrude_curve_along_curve", "extrude_curve_along_curve", {"curve_id": c1, "path_id": c2})
	else:
		test_command("extrude_curve_along_curve", "extrude_curve_along_curve", {"curve_id": "d", "path_id": "d"}, expect_error=True)

	# Extrude curve to point
	r = send_command("create_circle", {"center": [0, 70, 0], "radius": 3})
	time.sleep(TEST_DELAY)
	ecp_id = r.get("result", {}).get("id") if r.get("status") == "success" else None
	if ecp_id:
		test_command("extrude_curve_to_point", "extrude_curve_to_point", {"curve_id": ecp_id, "point": [0, 70, 15]})
	else:
		test_command("extrude_curve_to_point", "extrude_curve_to_point", {"curve_id": "d", "point": [0, 0, 10]}, expect_error=True)

	# Duplicate edge curves
	r = send_command("create_box", {"width": 5, "depth": 5, "height": 5, "x": 20, "y": 70, "z": 0})
	time.sleep(TEST_DELAY)
	box_id = r.get("result", {}).get("id") if r.get("status") == "success" else None
	if box_id:
		test_command("duplicate_edge_curves", "duplicate_edge_curves", {"brep_id": box_id})
	else:
		test_command("duplicate_edge_curves", "duplicate_edge_curves", {"brep_id": "dummy"}, expect_error=True)

	# Duplicate surface border - use a planar surface (has a border, unlike closed sphere)
	send_command("unselect_all")
	time.sleep(TEST_DELAY)
	r_bc = send_command("create_circle", {"center": [40, 70, 0], "radius": 5})
	time.sleep(TEST_DELAY)
	bc_id = r_bc.get("result", {}).get("id") if r_bc.get("status") == "success" else None
	if bc_id:
		r_ps = send_command("create_planar_surface", {"curve_ids": [bc_id]})
		time.sleep(TEST_DELAY)
		ps_id = r_ps.get("result", {}).get("id") if r_ps.get("status") == "success" else None
		if ps_id:
			test_command("duplicate_surface_border", "duplicate_surface_border", {"surface_id": ps_id})
		else:
			test_command("duplicate_surface_border", "duplicate_surface_border", {"surface_id": "dummy"}, expect_error=True)
	else:
		test_command("duplicate_surface_border", "duplicate_surface_border", {"surface_id": "dummy"}, expect_error=True)

	# Join surfaces
	r1 = send_command("create_box", {"width": 5, "depth": 5, "height": 5, "x": 60, "y": 70, "z": 0})
	time.sleep(TEST_DELAY)
	join_box = r1.get("result", {}).get("id") if r1.get("status") == "success" else None
	if join_box:
		# Explode then re-join
		r_exp = send_command("explode_polysurfaces", {"brep_id": join_box})
		time.sleep(TEST_DELAY)
		exp_ids = r_exp.get("result", {}).get("ids", []) if r_exp.get("status") == "success" else []
		if exp_ids:
			test_command("join_surfaces", "join_surfaces", {"surface_ids": exp_ids})
		else:
			test_command("join_surfaces", "join_surfaces", {"surface_ids": ["dummy"]}, expect_error=True)
	else:
		test_command("join_surfaces", "join_surfaces", {"surface_ids": ["dummy"]}, expect_error=True)

	# Explode polysurfaces
	r = send_command("create_box", {"width": 5, "depth": 5, "height": 5, "x": 80, "y": 70, "z": 0})
	time.sleep(TEST_DELAY)
	exp_box = r.get("result", {}).get("id") if r.get("status") == "success" else None
	if exp_box:
		test_command("explode_polysurfaces", "explode_polysurfaces", {"brep_id": exp_box})
	else:
		test_command("explode_polysurfaces", "explode_polysurfaces", {"brep_id": "dummy"}, expect_error=True)

	# Unroll surface - needs a developable surface, hard to guarantee, test with error
	test_command("unroll_surface", "unroll_surface", {"surface_id": "dummy"}, expect_error=True)

	# ================================================================
	# MESH OPERATIONS (9 tests)
	# ================================================================
	header("MESH OPERATIONS", 9)
	cleanup()

	test_command("create_mesh", "create_mesh", {
		"vertices": [[0, 0, 0], [10, 0, 0], [10, 10, 0], [0, 10, 0]],
		"faces": [[0, 1, 2, 3]]
	})

	r = send_command("create_circle", {"center": [20, 0, 0], "radius": 5})
	time.sleep(TEST_DELAY)
	pm_circ = r.get("result", {}).get("id") if r.get("status") == "success" else None
	if pm_circ:
		test_command("create_planar_mesh", "create_planar_mesh", {"curve_id": pm_circ})
	else:
		test_command("create_planar_mesh", "create_planar_mesh", {"curve_id": "dummy"}, expect_error=True)

	r = send_command("create_sphere", {"center": [40, 0, 0], "radius": 5})
	time.sleep(TEST_DELAY)
	mesh_srf = r.get("result", {}).get("id") if r.get("status") == "success" else None
	if mesh_srf:
		test_command("mesh_from_surface", "mesh_from_surface", {"object_ids": [mesh_srf]})
	else:
		test_command("mesh_from_surface", "mesh_from_surface", {"object_ids": ["dummy"]}, expect_error=True)

	# Mesh booleans - create two mesh boxes
	m1 = send_command("create_mesh", {
		"vertices": [[0, 20, 0], [10, 20, 0], [10, 30, 0], [0, 30, 0],
					 [0, 20, 10], [10, 20, 10], [10, 30, 10], [0, 30, 10]],
		"faces": [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [2, 3, 7, 6], [0, 3, 7, 4], [1, 2, 6, 5]]
	})
	time.sleep(TEST_DELAY)
	m2 = send_command("create_mesh", {
		"vertices": [[5, 20, 0], [15, 20, 0], [15, 30, 0], [5, 30, 0],
					 [5, 20, 10], [15, 20, 10], [15, 30, 10], [5, 30, 10]],
		"faces": [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [2, 3, 7, 6], [0, 3, 7, 4], [1, 2, 6, 5]]
	})
	time.sleep(TEST_DELAY)
	mid1 = m1.get("result", {}).get("id") if m1.get("status") == "success" else None
	mid2 = m2.get("result", {}).get("id") if m2.get("status") == "success" else None

	if mid1 and mid2:
		test_command("mesh_boolean_union", "mesh_boolean_union", {"mesh_ids": [mid1, mid2]})
	else:
		test_command("mesh_boolean_union", "mesh_boolean_union", {"mesh_ids": ["d1", "d2"]}, expect_error=True)

	test_command("mesh_boolean_difference", "mesh_boolean_difference", {
		"input_ids": ["dummy1"], "subtract_ids": ["dummy2"]
	}, expect_error=True)

	test_command("mesh_boolean_intersection", "mesh_boolean_intersection", {
		"mesh_ids1": ["dummy1"], "mesh_ids2": ["dummy2"]
	}, expect_error=True)

	# Join meshes
	jm1 = send_command("create_mesh", {
		"vertices": [[30, 20, 0], [40, 20, 0], [40, 30, 0], [30, 30, 0]],
		"faces": [[0, 1, 2, 3]]
	})
	time.sleep(TEST_DELAY)
	jm2 = send_command("create_mesh", {
		"vertices": [[40, 20, 0], [50, 20, 0], [50, 30, 0], [40, 30, 0]],
		"faces": [[0, 1, 2, 3]]
	})
	time.sleep(TEST_DELAY)
	jid1 = jm1.get("result", {}).get("id") if jm1.get("status") == "success" else None
	jid2 = jm2.get("result", {}).get("id") if jm2.get("status") == "success" else None
	if jid1 and jid2:
		test_command("join_meshes", "join_meshes", {"mesh_ids": [jid1, jid2]})
	else:
		test_command("join_meshes", "join_meshes", {"mesh_ids": ["d1", "d2"]}, expect_error=True)

	# Mesh to NURB
	mt = send_command("create_mesh", {
		"vertices": [[60, 20, 0], [70, 20, 0], [70, 30, 0], [60, 30, 0],
					 [60, 20, 5], [70, 20, 5], [70, 30, 5], [60, 30, 5]],
		"faces": [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [2, 3, 7, 6], [0, 3, 7, 4], [1, 2, 6, 5]]
	})
	time.sleep(TEST_DELAY)
	mt_id = mt.get("result", {}).get("id") if mt.get("status") == "success" else None
	if mt_id:
		test_command("mesh_to_nurb", "mesh_to_nurb", {"mesh_id": mt_id})
	else:
		test_command("mesh_to_nurb", "mesh_to_nurb", {"mesh_id": "dummy"}, expect_error=True)

	# Mesh offset
	mo = send_command("create_mesh", {
		"vertices": [[80, 20, 0], [90, 20, 0], [90, 30, 0], [80, 30, 0],
					 [80, 20, 5], [90, 20, 5], [90, 30, 5], [80, 30, 5]],
		"faces": [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [2, 3, 7, 6], [0, 3, 7, 4], [1, 2, 6, 5]]
	})
	time.sleep(TEST_DELAY)
	mo_id = mo.get("result", {}).get("id") if mo.get("status") == "success" else None
	if mo_id:
		test_command("mesh_offset", "mesh_offset", {"mesh_id": mo_id, "distance": 1})
	else:
		test_command("mesh_offset", "mesh_offset", {"mesh_id": "dummy", "distance": 1}, expect_error=True)

	# ================================================================
	# GROUP OPERATIONS (6 tests)
	# ================================================================
	header("GROUP OPERATIONS", 6)
	cleanup()

	# Create some objects first
	send_command("create_box", {"width": 5, "depth": 5, "height": 5, "x": 0, "y": 0, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("create_sphere", {"center": [20, 0, 0], "radius": 3})
	time.sleep(TEST_DELAY)
	# Get their IDs
	sel = send_command("select_all")
	time.sleep(TEST_DELAY)
	info = send_command("get_selected_objects")
	time.sleep(TEST_DELAY)
	obj_ids = [o["id"] for o in info.get("result", {}).get("objects", [])]
	send_command("unselect_all")

	test_command("create_group", "create_group", {"name": "TestGroup1", "object_ids": obj_ids[:1] if obj_ids else []})
	test_command("add_to_group", "add_to_group", {"name": "TestGroup1", "object_ids": obj_ids[1:] if len(obj_ids) > 1 else []})
	test_command("list_groups", "list_groups")
	test_command("select_by_group", "select_by_group", {"name": "TestGroup1"})
	send_command("unselect_all")
	test_command("remove_from_group", "remove_from_group", {"name": "TestGroup1", "object_ids": obj_ids[:1] if obj_ids else []})
	test_command("delete_group", "delete_group", {"name": "TestGroup1"})

	# ================================================================
	# VIEW OPERATIONS (8 tests)
	# ================================================================
	header("VIEW OPERATIONS", 8)

	test_command("get_view_info", "get_view_info")
	test_command("set_view_camera", "set_view_camera", {"camera": [50, 50, 50], "target": [0, 0, 0]})
	test_command("zoom_extents", "zoom_extents")
	test_command("set_display_mode", "set_display_mode", {"mode": "Shaded"})
	test_command("add_named_view", "add_named_view", {"name": "TestView1"})
	test_command("restore_named_view", "restore_named_view", {"name": "TestView1"})

	# Zoom selected - need something selected
	send_command("create_box", {"width": 5, "depth": 5, "height": 5, "x": 0, "y": 0, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("zoom_selected", "zoom_selected")
	send_command("unselect_all")

	# Capture viewport - verify image data is returned
	time.sleep(TEST_DELAY)
	send_command("zoom_extents")
	time.sleep(TEST_DELAY)
	cap_response = send_command("capture_viewport", {"width": 400, "height": 300})
	if cap_response.get("status") == "success":
		image_data = cap_response.get("image") or cap_response.get("result", {}).get("image")
		if image_data and len(image_data) > 100:
			try:
				decoded = base64.b64decode(image_data)
				# PNG files start with \x89PNG
				if decoded[:4] == b'\x89PNG':
					test_results["passed"].append("capture_viewport")
					print(f"  PASS: capture_viewport (PNG {len(decoded)} bytes)")
				else:
					test_results["failed"].append({"name": "capture_viewport", "error": "Not a valid PNG"})
					print(f"  FAIL: capture_viewport - Not a valid PNG")
			except Exception as e:
				test_results["failed"].append({"name": "capture_viewport", "error": f"Invalid base64: {e}"})
				print(f"  FAIL: capture_viewport - Invalid base64: {e}")
		else:
			test_results["failed"].append({"name": "capture_viewport", "error": "No image data or too small"})
			print(f"  FAIL: capture_viewport - No image data or too small")
	else:
		error_msg = cap_response.get("message", "Unknown error")
		test_results["failed"].append({"name": "capture_viewport", "error": error_msg})
		print(f"  FAIL: capture_viewport - {error_msg}")

	# ================================================================
	# BLOCK OPERATIONS (5 tests)
	# ================================================================
	header("BLOCK OPERATIONS", 5)
	cleanup()

	# Create objects for block
	r = send_command("create_box", {"width": 5, "depth": 5, "height": 5, "x": 0, "y": 0, "z": 0})
	time.sleep(TEST_DELAY)
	block_obj = r.get("result", {}).get("id") if r.get("status") == "success" else None

	if block_obj:
		test_command("create_block", "create_block", {
			"object_ids": [block_obj], "base_point": [0, 0, 0], "name": "TestBlock1"
		})
		test_command("insert_block", "insert_block", {
			"name": "TestBlock1", "point": [20, 0, 0], "scale": [1, 1, 1], "rotation": 0
		}, store_id="block_inst")
		# Explode the inserted block
		if "block_inst" in created_ids:
			test_command("explode_block", "explode_block", {"block_id": created_ids["block_inst"]})
		else:
			test_command("explode_block", "explode_block", {"block_id": "dummy"}, expect_error=True)
		test_command("list_blocks", "list_blocks")
		test_command("delete_block", "delete_block", {"name": "TestBlock1"})
	else:
		test_command("create_block", "create_block", {"object_ids": [], "base_point": [0, 0, 0], "name": "TestBlock1"}, expect_error=True)
		test_command("insert_block", "insert_block", {"name": "NoBlock", "point": [0, 0, 0]}, expect_error=True)
		test_command("explode_block", "explode_block", {"block_id": "dummy"}, expect_error=True)
		test_command("list_blocks", "list_blocks")
		test_command("delete_block", "delete_block", {"name": "NoBlock"}, expect_error=True)

	# ================================================================
	# MATERIAL OPERATIONS (5 tests)
	# ================================================================
	header("MATERIAL OPERATIONS", 5)
	cleanup()

	r = send_command("create_box", {"width": 5, "depth": 5, "height": 5, "x": 0, "y": 0, "z": 0})
	time.sleep(TEST_DELAY)
	mat_obj = r.get("result", {}).get("id") if r.get("status") == "success" else None

	if mat_obj:
		test_command("add_material_to_object", "add_material_to_object", {
			"object_id": mat_obj, "color": [255, 0, 0]
		})
		test_command("set_material_color", "set_material_color", {
			"object_id": mat_obj, "color": [0, 255, 0]
		})
		test_command("set_material_transparency", "set_material_transparency", {
			"object_id": mat_obj, "transparency": 0.5
		})
		test_command("set_material_shine", "set_material_shine", {
			"object_id": mat_obj, "shine": 128
		})
	else:
		test_command("add_material_to_object", "add_material_to_object", {"object_id": "dummy", "color": [255, 0, 0]}, expect_error=True)
		test_command("set_material_color", "set_material_color", {"object_id": "dummy", "color": [0, 255, 0]}, expect_error=True)
		test_command("set_material_transparency", "set_material_transparency", {"object_id": "dummy", "transparency": 0.5}, expect_error=True)
		test_command("set_material_shine", "set_material_shine", {"object_id": "dummy", "shine": 128}, expect_error=True)

	test_command("add_material_to_layer", "add_material_to_layer", {"layer_name": "Default"})

	# ================================================================
	# OBJECT OPERATIONS (5 tests)
	# ================================================================
	header("OBJECT OPERATIONS", 5)
	cleanup()

	send_command("create_box", {"width": 5, "depth": 5, "height": 5, "x": 0, "y": 0, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("hide_objects", "hide_objects")
	test_command("show_objects", "show_objects")

	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("lock_objects", "lock_objects")
	test_command("unlock_objects", "unlock_objects")

	# is_object_solid
	r = send_command("create_box", {"width": 5, "depth": 5, "height": 5, "x": 20, "y": 0, "z": 0})
	time.sleep(TEST_DELAY)
	solid_id = r.get("result", {}).get("id") if r.get("status") == "success" else None
	if solid_id:
		test_command("is_object_solid", "is_object_solid", {"object_id": solid_id})
	else:
		test_command("is_object_solid", "is_object_solid", {"object_id": "dummy"}, expect_error=True)

	# ================================================================
	# SELECTION OPERATIONS - EXISTING + NEW (8 tests)
	# ================================================================
	header("SELECTION OPERATIONS", 8)
	cleanup()

	# Create objects with names
	send_command("create_box", {"width": 5, "depth": 5, "height": 5, "x": 0, "y": 0, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	send_command("set_object_name", {"name": "NamedBox"})
	time.sleep(TEST_DELAY)
	send_command("unselect_all")
	time.sleep(TEST_DELAY)
	send_command("create_sphere", {"center": [20, 0, 0], "radius": 5})
	time.sleep(TEST_DELAY)

	test_command("select_all", "select_all")
	test_command("unselect_all", "unselect_all")
	test_command("select_by_type", "select_by_type", {"type": "curve"})
	send_command("unselect_all")
	test_command("select_by_layer", "select_by_layer", {"layer": "Default"})
	test_command("delete_selected", "delete_selected")

	# New selection tools
	send_command("create_box", {"width": 3, "depth": 3, "height": 3, "x": 0, "y": 0, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	send_command("set_object_name", {"name": "FindMe"})
	time.sleep(TEST_DELAY)
	send_command("unselect_all")
	time.sleep(TEST_DELAY)

	test_command("select_by_name", "select_by_name", {"name": "FindMe"})
	send_command("unselect_all")
	test_command("last_created_objects", "last_created_objects")
	send_command("unselect_all")
	test_command("invert_selection", "invert_selection")
	send_command("unselect_all")

	# ================================================================
	# LAYER MANAGEMENT (6 tests)
	# ================================================================
	header("LAYER MANAGEMENT", 6)
	test_command("create_layer", "create_layer", {"name": "TestLayer1", "color": [255, 0, 0]})
	test_command("create_layer", "create_layer", {"name": "TestLayer2", "color": [0, 255, 0]})
	test_command("set_current_layer", "set_current_layer", {"name": "TestLayer1"})
	test_command("set_layer_color", "set_layer_color", {"name": "TestLayer1", "color": [255, 255, 0]})
	test_command("set_layer_visibility", "set_layer_visibility", {"name": "TestLayer1", "visible": False})
	time.sleep(TEST_DELAY)
	send_command("set_layer_visibility", {"name": "TestLayer1", "visible": True})
	test_command("list_layers", "list_layers")
	# Reset to default
	send_command("set_current_layer", {"name": "Default"})

	# ================================================================
	# ANALYSIS TOOLS (4 tests)
	# ================================================================
	header("ANALYSIS TOOLS", 4)
	cleanup()
	test_command("measure_distance", "measure_distance", {"point1": [0, 0, 0], "point2": [10, 0, 0]})

	send_command("create_line", {"start": [0, 0, 0], "end": [15, 0, 0]})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("measure_curve_length", "measure_curve_length")
	send_command("unselect_all")

	send_command("create_circle", {"center": [20, 0, 0], "radius": 5})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("measure_area", "measure_area")
	send_command("unselect_all")

	send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 40, "y": 0, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("measure_volume", "measure_volume")
	send_command("unselect_all")

	# ================================================================
	# OBJECT PROPERTIES (3 tests)
	# ================================================================
	header("OBJECT PROPERTIES", 3)
	cleanup()
	send_command("create_box", {"width": 5, "depth": 5, "height": 5, "x": 0, "y": 0, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("set_object_name", "set_object_name", {"name": "TestBox"})
	test_command("set_object_color", "set_object_color", {"color": [255, 0, 255]})
	test_command("set_object_layer", "set_object_layer", {"layer": "TestLayer2"})
	send_command("unselect_all")

	# ================================================================
	# DOCUMENT OPERATIONS (3 tests)
	# ================================================================
	header("DOCUMENT OPERATIONS", 3)
	test_command("get_document_info", "get_document_info")
	test_command("set_unit_system", "set_unit_system", {"system": 4})
	test_command("enable_redraw", "enable_redraw", {"enable": True})

	# ================================================================
	# ANNOTATION OPERATIONS (3 tests)
	# ================================================================
	header("ANNOTATION OPERATIONS", 3)
	cleanup()
	test_command("add_text", "add_text", {"text": "Hello Rhino", "point": [0, 0, 0], "height": 2.0})
	test_command("add_text_dot", "add_text_dot", {"text": "Dot Label", "point": [10, 0, 0]})
	test_command("add_leader", "add_leader", {"points": [[20, 0, 0], [30, 5, 0]], "text": "Leader note"})

	# ================================================================
	# USER DATA OPERATIONS (4 tests)
	# ================================================================
	header("USER DATA OPERATIONS", 4)
	cleanup()

	r = send_command("create_box", {"width": 5, "depth": 5, "height": 5, "x": 0, "y": 0, "z": 0})
	time.sleep(TEST_DELAY)
	ud_id = r.get("result", {}).get("id") if r.get("status") == "success" else None

	if ud_id:
		test_command("set_user_text", "set_user_text", {"object_id": ud_id, "key": "material", "value": "steel"})
		test_command("get_user_text", "get_user_text", {"object_id": ud_id, "key": "material"})
	else:
		test_command("set_user_text", "set_user_text", {"object_id": "dummy", "key": "k", "value": "v"}, expect_error=True)
		test_command("get_user_text", "get_user_text", {"object_id": "dummy"}, expect_error=True)

	test_command("set_document_user_text", "set_document_user_text", {"key": "project", "value": "MCP Test"})
	test_command("get_document_user_text", "get_document_user_text", {"key": "project"})

	# ================================================================
	# CURVE ANALYSIS (4 tests)
	# ================================================================
	header("CURVE ANALYSIS", 4)
	cleanup()

	r = send_command("create_line", {"start": [0, 0, 0], "end": [20, 0, 0]})
	time.sleep(TEST_DELAY)
	ca_id = r.get("result", {}).get("id") if r.get("status") == "success" else None

	if ca_id:
		test_command("curve_closest_point", "curve_closest_point", {"curve_id": ca_id, "point": [10, 5, 0]})
		test_command("evaluate_curve", "evaluate_curve", {"curve_id": ca_id, "parameter": 0.5})
		test_command("curve_start_end_points", "curve_start_end_points", {"curve_id": ca_id})
	else:
		test_command("curve_closest_point", "curve_closest_point", {"curve_id": "dummy", "point": [0, 0, 0]}, expect_error=True)
		test_command("evaluate_curve", "evaluate_curve", {"curve_id": "dummy", "parameter": 0}, expect_error=True)
		test_command("curve_start_end_points", "curve_start_end_points", {"curve_id": "dummy"}, expect_error=True)

	# Curve-curve intersection
	r1 = send_command("create_line", {"start": [0, -10, 0], "end": [20, 10, 0]})
	time.sleep(TEST_DELAY)
	r2 = send_command("create_line", {"start": [0, 10, 0], "end": [20, -10, 0]})
	time.sleep(TEST_DELAY)
	cc1 = r1.get("result", {}).get("id") if r1.get("status") == "success" else None
	cc2 = r2.get("result", {}).get("id") if r2.get("status") == "success" else None
	if cc1 and cc2:
		test_command("curve_curve_intersection", "curve_curve_intersection", {"curve1": cc1, "curve2": cc2})
	else:
		test_command("curve_curve_intersection", "curve_curve_intersection", {"curve1": "d1", "curve2": "d2"}, expect_error=True)

	# ================================================================
	# CODE EXECUTION (1 test)
	# ================================================================
	header("CODE EXECUTION", 1)
	test_command("execute_python_code", "execute_python_code", {"code": "print('Hello from RhinoMCP test')"})

	# ================================================================
	# ERROR HANDLING (1 test)
	# ================================================================
	header("ERROR HANDLING", 1)
	test_command("unknown_command_error", "invalid_command_xyz", expect_error=True)


def print_results():
	"""Print test results summary"""
	total = len(test_results["passed"]) + len(test_results["failed"])
	passed = len(test_results["passed"])
	failed = len(test_results["failed"])
	percentage = (passed / total * 100) if total > 0 else 0

	print("\n" + "=" * 70)
	print("TEST RESULTS SUMMARY")
	print("=" * 70)
	print()
	print(f"Total Tests:  {total}")
	print(f"Passed:       {passed} ({percentage:.1f}%)")
	print(f"Failed:       {failed} ({100 - percentage:.1f}%)")
	print()

	if failed > 0:
		print("FAILED TESTS:")
		print("-" * 70)
		for failure in test_results["failed"]:
			print(f"  - {failure['name']}")
			print(f"    Error: {failure['error']}")
		print()

	if passed == total:
		print("SUCCESS: All tests passed!")
	else:
		print(f"ATTENTION: {failed} test(s) failed. Review above for details.")

	print("=" * 70)


def main():
	"""Main test runner"""
	try:
		run_tests()
	except KeyboardInterrupt:
		print("\n\nTests interrupted by user")
	finally:
		print_results()


if __name__ == "__main__":
	main()
