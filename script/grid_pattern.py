#!/usr/bin/env python3
"""
Grid Pattern
Creates a grid of boxes with even spacing
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


def create_grid_pattern(rows=5, cols=5, spacing=15, box_size=8):
	"""Create a grid of boxes"""
	print("Creating {}x{} grid of boxes...".format(rows, cols))

	count = 0
	for x in range(rows):
		for y in range(cols):
			x_pos = x * spacing
			y_pos = y * spacing

			result = send_command("create_box", {
				"width": box_size,
				"depth": box_size,
				"height": box_size,
				"x": x_pos,
				"y": y_pos,
				"z": 0
			})

			if result["status"] == "success":
				count += 1
			else:
				print("  Failed at ({}, {}): {}".format(x, y, result.get("message", "")))

			time.sleep(0.1)

	print("Grid pattern complete! Created {} boxes".format(count))


if __name__ == "__main__":
	# Test connection
	print("Testing connection to Rhino...")
	response = send_command("get_scene_info")

	if response["status"] != "success":
		print("ERROR: Cannot connect to Rhino on port {}".format(RHINO_PORT))
		print("Make sure Rhino listener is running!")
		exit(1)

	print("Connection OK\n")

	# Create grid pattern
	create_grid_pattern(rows=5, cols=5, spacing=15, box_size=8)
