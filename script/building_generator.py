#!/usr/bin/env python3
"""
Building Generator
Creates a complete building with columns and floor slabs organized in layers
"""

import socket
import json
import time

RHINO_HOST = "localhost"
RHINO_PORT = 54321

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
	except Exception as e:
		return {"status": "error", "message": str(e)}


def setup_layers():
	"""Create organized layer structure"""
	print("Setting up layers...")

	layers = [
		{"name": "Columns", "color": [100, 100, 100]},
		{"name": "Floors", "color": [200, 200, 200]},
		{"name": "Walls", "color": [255, 255, 255]}
	]

	for layer in layers:
		result = send_command("create_layer", {
			"name": layer["name"],
			"color": layer["color"]
		})

		if result["status"] == "success":
			print("  Created layer: {}".format(layer["name"]))

		time.sleep(0.1)


def generate_building(floors=5, floor_height=4, width=30, depth=20, column_radius=0.5, slab_thickness=0.3):
	"""
	Generate a complete building with structure and floors

	floors: number of floors
	floor_height: height of each floor
	width: building width (X direction)
	depth: building depth (Y direction)
	column_radius: radius of structural columns
	slab_thickness: thickness of floor slabs
	"""
	print("\nGenerating building: {} floors, {}x{} footprint".format(floors, width, depth))

	# Create columns at corners
	send_command("set_current_layer", {"name": "Columns"})
	time.sleep(0.1)

	column_positions = [
		[0, 0],
		[width, 0],
		[0, depth],
		[width, depth]
	]

	print("\nCreating columns...")
	for x, y in column_positions:
		result = send_command("create_cylinder", {
			"base": [x, y, 0],
			"height": floors * floor_height,
			"radius": column_radius
		})

		if result["status"] == "success":
			print("  Column at ({}, {})".format(x, y))

		time.sleep(0.1)

	# Create floor slabs
	send_command("set_current_layer", {"name": "Floors"})
	time.sleep(0.1)

	print("\nCreating floor slabs...")
	for floor in range(floors + 1):
		z = floor * floor_height
		result = send_command("create_box", {
			"width": width,
			"depth": depth,
			"height": slab_thickness,
			"x": 0,
			"y": 0,
			"z": z
		})

		if result["status"] == "success":
			print("  Floor {} at height {}".format(floor, z))

		time.sleep(0.1)

	print("\nBuilding generation complete!")
	print("Total height: {}".format(floors * floor_height))
	print("Footprint: {} x {}".format(width, depth))


if __name__ == "__main__":
	# Test connection
	print("Testing connection to Rhino...")
	response = send_command("get_scene_info")

	if response["status"] != "success":
		print("ERROR: Cannot connect to Rhino on port {}".format(RHINO_PORT))
		print("Make sure Rhino listener is running!")
		exit(1)

	print("Connection OK\n")

	# Setup layers
	setup_layers()

	# Generate building
	generate_building(
		floors=8,
		floor_height=3.5,
		width=40,
		depth=25,
		column_radius=0.5,
		slab_thickness=0.3
	)
