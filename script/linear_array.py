#!/usr/bin/env python3
"""
Linear Array Pattern
Creates a line of spheres with even spacing
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


def create_linear_array(count=10, spacing=20, radius=5):
	"""Create a linear array of spheres"""
	print("Creating linear array of {} spheres...".format(count))

	for i in range(count):
		x = i * spacing
		result = send_command("create_sphere", {
			"center": [x, 0, 0],
			"radius": radius
		})

		if result["status"] == "success":
			print("  Created sphere {} at x={}".format(i + 1, x))
		else:
			print("  Failed to create sphere {}: {}".format(i + 1, result.get("message", "")))

		time.sleep(0.1)

	print("Linear array complete!")


if __name__ == "__main__":
	# Test connection
	print("Testing connection to Rhino...")
	response = send_command("get_scene_info")

	if response["status"] != "success":
		print("ERROR: Cannot connect to Rhino on port {}".format(RHINO_PORT))
		print("Make sure Rhino listener is running!")
		exit(1)

	print("Connection OK\n")

	# Create linear array
	create_linear_array(count=10, spacing=20, radius=5)
