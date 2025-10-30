#!/usr/bin/env python3
"""
Spiral Pattern
Creates a 3D spiral of points
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


def create_spiral(num_points=50, radius_increment=2, height_increment=1.5, angle_increment=0.5):
	"""Create a 3D spiral of points"""
	print("Creating spiral with {} points...".format(num_points))

	count = 0
	for i in range(num_points):
		angle = i * angle_increment
		radius = i * radius_increment
		x = radius * math.cos(angle)
		y = radius * math.sin(angle)
		z = i * height_increment

		result = send_command("create_point", {"x": x, "y": y, "z": z})

		if result["status"] == "success":
			count += 1
		else:
			print("  Failed at point {}: {}".format(i, result.get("message", "")))

		time.sleep(0.1)

	print("Spiral complete! Created {} points".format(count))


if __name__ == "__main__":
	# Test connection
	print("Testing connection to Rhino...")
	response = send_command("get_scene_info")

	if response["status"] != "success":
		print("ERROR: Cannot connect to Rhino on port {}".format(RHINO_PORT))
		print("Make sure Rhino listener is running!")
		exit(1)

	print("Connection OK\n")

	# Create spiral
	create_spiral(num_points=50, radius_increment=2, height_increment=1.5, angle_increment=0.5)
