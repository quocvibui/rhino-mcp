#!/usr/bin/env python3
"""
Comprehensive test suite for Rhino MCP
Tests all 51 commands with pass/fail tracking
"""

import socket
import json
import time

RHINO_HOST = "localhost"
RHINO_PORT = 54321
TEST_DELAY = 0.3

test_results = {
	"passed": [],
	"failed": []
}


def send_command(command_type, params=None):
	"""Send command to Rhino and return response"""
	if params is None:
		params = {}

	command = {
		"type": command_type,
		"params": params
	}

	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(5)
		sock.connect((RHINO_HOST, RHINO_PORT))
		sock.sendall(json.dumps(command).encode('utf-8'))
		response_data = sock.recv(8192)
		sock.close()
		response = json.loads(response_data.decode('utf-8'))
		return response

	except ConnectionRefusedError:
		return {"status": "error", "message": "Cannot connect to Rhino"}
	except Exception as e:
		return {"status": "error", "message": str(e)}


def test_command(name, command_type, params=None, expect_error=False):
	"""Test a command and track results"""
	response = send_command(command_type, params)

	if response is None:
		test_results["failed"].append({"name": name, "error": "No response"})
		print("  FAIL: {0} - No response".format(name))
		return False

	status = response.get("status")

	if expect_error:
		if status == "error":
			test_results["passed"].append(name)
			print("  PASS: {0}".format(name))
			return True
		else:
			test_results["failed"].append({"name": name, "error": "Expected error but got success"})
			print("  FAIL: {0} - Expected error but got success".format(name))
			return False
	else:
		if status == "success":
			test_results["passed"].append(name)
			print("  PASS: {0}".format(name))
			return True
		else:
			error_msg = response.get("message", "Unknown error")
			test_results["failed"].append({"name": name, "error": error_msg})
			print("  FAIL: {0} - {1}".format(name, error_msg))
			return False


def run_tests():
	"""Run all tests"""
	print("=" * 70)
	print("RHINO MCP COMPREHENSIVE TEST SUITE")
	print("=" * 70)
	print()

	# Check connection first
	print("Checking Rhino connection...")
	response = send_command("get_scene_info")
	if response.get("status") != "success":
		print("ERROR: Cannot connect to Rhino on port {0}".format(RHINO_PORT))
		print("\nMake sure:")
		print("1. Rhino 7 is running")
		print("2. Run this command in Rhino:")
		print("   _-RunPythonScript \"/path/to/server.py\" _Enter")
		return
	print("Connection OK\n")
	time.sleep(TEST_DELAY)

	# Clean up scene from previous test runs
	print("Cleaning up scene from previous test runs...")
	send_command("select_all")
	time.sleep(TEST_DELAY)
	send_command("delete_selected")
	time.sleep(TEST_DELAY)
	print("Scene cleaned\n")

	# Scene Understanding (2 tests)
	print("\n[1/11] SCENE UNDERSTANDING (2 tests)")
	print("-" * 70)
	test_command("get_scene_info", "get_scene_info")
	time.sleep(TEST_DELAY)
	test_command("get_selected_objects", "get_selected_objects")
	time.sleep(TEST_DELAY)

	# Basic Geometry (7 tests)
	print("\n[2/11] BASIC GEOMETRY (7 tests)")
	print("-" * 70)
	test_command("create_point", "create_point", {"x": 0, "y": 0, "z": 0})
	time.sleep(TEST_DELAY)
	test_command("create_line", "create_line", {"start": [0, 0, 0], "end": [10, 0, 0]})
	time.sleep(TEST_DELAY)
	test_command("create_circle", "create_circle", {"center": [0, 10, 0], "radius": 5})
	time.sleep(TEST_DELAY)
	test_command("create_arc", "create_arc", {"center": [0, 20, 0], "radius": 5, "start_angle": 0, "end_angle": 180})
	time.sleep(TEST_DELAY)
	test_command("create_ellipse", "create_ellipse", {"center": [0, 30, 0], "x_radius": 8, "y_radius": 4})
	time.sleep(TEST_DELAY)
	test_command("create_polyline", "create_polyline", {"points": [[10, 0, 0], [15, 5, 0], [20, 0, 0]]})
	time.sleep(TEST_DELAY)
	test_command("create_curve", "create_curve", {"points": [[10, 10, 0], [15, 15, 0], [20, 10, 0]], "degree": 3})
	time.sleep(TEST_DELAY)

	# 3D Solids (5 tests)
	print("\n[3/11] 3D SOLIDS (5 tests)")
	print("-" * 70)
	test_command("create_box", "create_box", {"width": 10, "depth": 10, "height": 10, "x": 30, "y": 0, "z": 0})
	time.sleep(TEST_DELAY)
	test_command("create_sphere", "create_sphere", {"center": [30, 20, 5], "radius": 5})
	time.sleep(TEST_DELAY)
	test_command("create_cylinder", "create_cylinder", {"base": [50, 0, 0], "height": 15, "radius": 5})
	time.sleep(TEST_DELAY)
	test_command("create_cone", "create_cone", {"base": [50, 20, 0], "height": 15, "radius": 5})
	time.sleep(TEST_DELAY)
	test_command("create_torus", "create_torus", {"center": [70, 10, 5], "major_radius": 8, "minor_radius": 2})
	time.sleep(TEST_DELAY)

	# Transformations (6 tests)
	print("\n[4/11] TRANSFORMATIONS (6 tests)")
	print("-" * 70)

	# Create and select a box for transformation tests
	send_command("create_box", {"width": 5, "depth": 5, "height": 5, "x": 0, "y": 50, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)

	test_command("move_objects", "move_objects", {"displacement": [5, 0, 0]})
	time.sleep(TEST_DELAY)
	test_command("rotate_objects", "rotate_objects", {"center": [0, 50, 0], "angle": 45})
	time.sleep(TEST_DELAY)
	test_command("scale_objects", "scale_objects", {"center": [0, 50, 0], "scale": 1.5})
	time.sleep(TEST_DELAY)
	test_command("mirror_objects", "mirror_objects", {"start": [0, 50, 0], "end": [10, 50, 0]})
	time.sleep(TEST_DELAY)
	test_command("copy_objects", "copy_objects", {"displacement": [10, 0, 0]})
	time.sleep(TEST_DELAY)
	test_command("array_linear", "array_linear", {"displacement": [5, 0, 0], "count": 3})
	time.sleep(TEST_DELAY)

	send_command("unselect_all")
	time.sleep(TEST_DELAY)

	# Boolean Operations (3 tests)
	print("\n[5/11] BOOLEAN OPERATIONS (3 tests)")
	print("-" * 70)

	# Create overlapping boxes for boolean union
	send_command("unselect_all")
	time.sleep(TEST_DELAY)
	send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 0, "y": 70, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 5, "y": 70, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("boolean_union", "boolean_union")
	time.sleep(TEST_DELAY)

	# Clean up and create boxes for boolean difference
	send_command("select_all")
	time.sleep(TEST_DELAY)
	send_command("delete_selected")
	time.sleep(TEST_DELAY)
	send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 20, "y": 70, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 25, "y": 70, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("boolean_difference", "boolean_difference")
	time.sleep(TEST_DELAY)

	# Clean up and create boxes for boolean intersection
	send_command("select_all")
	time.sleep(TEST_DELAY)
	send_command("delete_selected")
	time.sleep(TEST_DELAY)
	send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 40, "y": 70, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 45, "y": 70, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("boolean_intersection", "boolean_intersection")
	time.sleep(TEST_DELAY)
	send_command("unselect_all")
	time.sleep(TEST_DELAY)

	# Curve Operations (5 tests)
	print("\n[6/11] CURVE OPERATIONS (5 tests)")
	print("-" * 70)

	# Create curves for testing
	send_command("create_line", {"start": [0, 90, 0], "end": [10, 90, 0]})
	time.sleep(TEST_DELAY)
	send_command("create_line", {"start": [10, 90, 0], "end": [10, 100, 0]})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("join_curves", "join_curves")
	time.sleep(TEST_DELAY)
	test_command("explode_curves", "explode_curves")
	time.sleep(TEST_DELAY)
	send_command("unselect_all")
	time.sleep(TEST_DELAY)

	send_command("create_circle", {"center": [20, 95, 0], "radius": 5})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("offset_curve", "offset_curve", {"distance": 2})
	time.sleep(TEST_DELAY)
	send_command("unselect_all")
	time.sleep(TEST_DELAY)

	send_command("create_line", {"start": [30, 90, 0], "end": [40, 90, 0]})
	time.sleep(TEST_DELAY)
	send_command("create_line", {"start": [40, 90, 0], "end": [40, 100, 0]})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("fillet_curves", "fillet_curves", {"radius": 2})
	time.sleep(TEST_DELAY)
	send_command("unselect_all")
	time.sleep(TEST_DELAY)

	send_command("create_line", {"start": [50, 90, 0], "end": [55, 90, 0]})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("extend_curve", "extend_curve", {"extension": 3})
	time.sleep(TEST_DELAY)
	send_command("unselect_all")
	time.sleep(TEST_DELAY)

	# Surface Operations (3 tests)
	print("\n[7/11] SURFACE OPERATIONS (3 tests)")
	print("-" * 70)

	# Clean up before surface operations
	send_command("select_all")
	time.sleep(TEST_DELAY)
	send_command("delete_selected")
	time.sleep(TEST_DELAY)

	send_command("create_circle", {"center": [0, 110, 0], "radius": 5})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("extrude_curve_straight", "extrude_curve_straight", {"height": 10})
	time.sleep(TEST_DELAY)

	# Clean up before revolve
	send_command("select_all")
	time.sleep(TEST_DELAY)
	send_command("delete_selected")
	time.sleep(TEST_DELAY)

	send_command("create_line", {"start": [20, 110, 0], "end": [20, 115, 5]})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("revolve_curve", "revolve_curve", {"axis_start": [20, 110, 0], "axis_end": [20, 110, 10], "angle": 360})
	time.sleep(TEST_DELAY)

	# Clean up before loft
	send_command("select_all")
	time.sleep(TEST_DELAY)
	send_command("delete_selected")
	time.sleep(TEST_DELAY)

	send_command("create_circle", {"center": [40, 110, 0], "radius": 3})
	time.sleep(TEST_DELAY)
	send_command("create_circle", {"center": [40, 110, 5], "radius": 5})
	time.sleep(TEST_DELAY)
	send_command("create_circle", {"center": [40, 110, 10], "radius": 3})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("loft_curves", "loft_curves")
	time.sleep(TEST_DELAY)
	send_command("unselect_all")
	time.sleep(TEST_DELAY)

	# Layer Management (6 tests)
	print("\n[8/11] LAYER MANAGEMENT (6 tests)")
	print("-" * 70)
	test_command("create_layer", "create_layer", {"name": "TestLayer1", "color": [255, 0, 0]})
	time.sleep(TEST_DELAY)
	test_command("create_layer", "create_layer", {"name": "TestLayer2", "color": [0, 255, 0]})
	time.sleep(TEST_DELAY)
	test_command("set_current_layer", "set_current_layer", {"name": "TestLayer1"})
	time.sleep(TEST_DELAY)
	test_command("set_layer_color", "set_layer_color", {"name": "TestLayer1", "color": [255, 255, 0]})
	time.sleep(TEST_DELAY)
	test_command("set_layer_visibility", "set_layer_visibility", {"name": "TestLayer1", "visible": False})
	time.sleep(TEST_DELAY)
	test_command("set_layer_visibility", "set_layer_visibility", {"name": "TestLayer1", "visible": True})
	time.sleep(TEST_DELAY)
	test_command("list_layers", "list_layers")
	time.sleep(TEST_DELAY)

	# Analysis Tools (4 tests)
	print("\n[9/11] ANALYSIS TOOLS (4 tests)")
	print("-" * 70)
	test_command("measure_distance", "measure_distance", {"point1": [0, 0, 0], "point2": [10, 0, 0]})
	time.sleep(TEST_DELAY)

	send_command("create_line", {"start": [0, 130, 0], "end": [15, 130, 0]})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("measure_curve_length", "measure_curve_length")
	time.sleep(TEST_DELAY)
	send_command("unselect_all")
	time.sleep(TEST_DELAY)

	send_command("create_circle", {"center": [20, 130, 0], "radius": 5})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("measure_area", "measure_area")
	time.sleep(TEST_DELAY)
	send_command("unselect_all")
	time.sleep(TEST_DELAY)

	send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 40, "y": 130, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("measure_volume", "measure_volume")
	time.sleep(TEST_DELAY)
	send_command("unselect_all")
	time.sleep(TEST_DELAY)

	# Object Properties (3 tests)
	print("\n[10/11] OBJECT PROPERTIES (3 tests)")
	print("-" * 70)

	send_command("create_box", {"width": 5, "depth": 5, "height": 5, "x": 0, "y": 150, "z": 0})
	time.sleep(TEST_DELAY)
	send_command("select_all")
	time.sleep(TEST_DELAY)
	test_command("set_object_name", "set_object_name", {"name": "TestBox"})
	time.sleep(TEST_DELAY)
	test_command("set_object_color", "set_object_color", {"color": [255, 0, 255]})
	time.sleep(TEST_DELAY)
	test_command("set_object_layer", "set_object_layer", {"layer": "TestLayer2"})
	time.sleep(TEST_DELAY)
	send_command("unselect_all")
	time.sleep(TEST_DELAY)

	# Selection & Management (5 tests)
	print("\n[11/11] SELECTION & MANAGEMENT (5 tests)")
	print("-" * 70)
	test_command("select_all", "select_all")
	time.sleep(TEST_DELAY)
	test_command("unselect_all", "unselect_all")
	time.sleep(TEST_DELAY)
	test_command("select_by_type", "select_by_type", {"type": "curve"})
	time.sleep(TEST_DELAY)
	send_command("unselect_all")
	time.sleep(TEST_DELAY)
	test_command("select_by_layer", "select_by_layer", {"layer": "TestLayer2"})
	time.sleep(TEST_DELAY)
	test_command("delete_selected", "delete_selected")
	time.sleep(TEST_DELAY)

	# Error Handling Test
	print("\n[BONUS] ERROR HANDLING (1 test)")
	print("-" * 70)
	test_command("unknown_command_error", "invalid_command_xyz", expect_error=True)
	time.sleep(TEST_DELAY)


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
	print("Total Tests:  {0}".format(total))
	print("Passed:       {0} ({1:.1f}%)".format(passed, percentage))
	print("Failed:       {0} ({1:.1f}%)".format(failed, 100 - percentage))
	print()

	if failed > 0:
		print("FAILED TESTS:")
		print("-" * 70)
		for failure in test_results["failed"]:
			print("  - {0}".format(failure["name"]))
			print("    Error: {0}".format(failure["error"]))
		print()

	if passed == total:
		print("SUCCESS: All tests passed!")
	else:
		print("ATTENTION: {0} test(s) failed. Review above for details.".format(failed))

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
