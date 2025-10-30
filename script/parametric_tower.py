#!/usr/bin/env python3
"""
Parametric Tower
Creates a twisting tower with varying radius using lofted circles
"""

import socket
import json
import time
import math

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


def create_parametric_tower(floors=10, base_radius=20, height_per_floor=5, taper_rate=0.05, twist_rate=10):
	"""
	Create a twisting parametric tower

	floors: number of floor levels
	base_radius: radius at ground level
	height_per_floor: vertical spacing between floors
	taper_rate: how much to reduce radius per floor (0.05 = 5% per floor)
	twist_rate: degrees of twist per floor
	"""
	print("Creating parametric tower with {} floors...".format(floors))

	# Create circles at each floor
	for floor in range(floors):
		z_height = floor * height_per_floor
		floor_radius = base_radius * (1 - floor * taper_rate)

		# Calculate position (can add twist offset if desired)
		twist_angle = math.radians(floor * twist_rate)
		x_offset = 0  # Could add: floor_radius * 0.1 * math.cos(twist_angle) for eccentric twist
		y_offset = 0  # Could add: floor_radius * 0.1 * math.sin(twist_angle) for eccentric twist

		result = send_command("create_circle", {
			"center": [x_offset, y_offset, z_height],
			"radius": floor_radius
		})

		if result["status"] == "success":
			print("  Floor {} - radius: {:.2f}, height: {:.2f}".format(floor + 1, floor_radius, z_height))
		else:
			print("  Failed at floor {}: {}".format(floor + 1, result.get("message", "")))

		time.sleep(0.1)

	# Select all circles and loft into surface
	print("\nLofting circles into tower surface...")
	send_command("select_by_type", {"type": "curve"})
	time.sleep(0.2)

	result = send_command("loft_curves")
	if result["status"] == "success":
		print("Tower lofted successfully!")
	else:
		print("Failed to loft tower: {}".format(result.get("message", "")))


if __name__ == "__main__":
	# Test connection
	print("Testing connection to Rhino...")
	response = send_command("get_scene_info")

	if response["status"] != "success":
		print("ERROR: Cannot connect to Rhino on port {}".format(RHINO_PORT))
		print("Make sure Rhino listener is running!")
		exit(1)

	print("Connection OK\n")

	# Create parametric tower
	create_parametric_tower(
		floors=15,
		base_radius=25,
		height_per_floor=4,
		taper_rate=0.05,
		twist_rate=10
	)
