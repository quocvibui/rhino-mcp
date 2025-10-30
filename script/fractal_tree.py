#!/usr/bin/env python3
"""
Fractal Tree
Creates a 3D fractal tree structure using recursive branching
"""

import socket
import json
import time
import math
import random

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


def create_branch(start_x, start_y, start_z, length, angle, depth, branch_count):
	"""
	Recursively create tree branches

	Returns the total number of branches created
	"""
	if depth == 0:
		return branch_count

	# Calculate end point
	end_x = start_x + length * math.cos(math.radians(angle))
	end_y = start_y + length * math.sin(math.radians(angle))
	end_z = start_z + length * 0.5

	# Create branch
	result = send_command("create_line", {
		"start": [start_x, start_y, start_z],
		"end": [end_x, end_y, end_z]
	})

	if result["status"] == "success":
		branch_count += 1

	time.sleep(0.05)

	# Create sub-branches with variation
	angle_variation = random.uniform(-30, 30)
	new_length = length * 0.7

	# Left branch
	branch_count = create_branch(
		end_x, end_y, end_z,
		new_length,
		angle + 25 + angle_variation,
		depth - 1,
		branch_count
	)

	# Right branch
	branch_count = create_branch(
		end_x, end_y, end_z,
		new_length,
		angle - 25 + angle_variation,
		depth - 1,
		branch_count
	)

	return branch_count


def create_fractal_tree(trunk_length=30, depth=5, seed=None):
	"""
	Create a fractal tree

	trunk_length: length of initial trunk
	depth: recursion depth (number of branch generations)
	seed: random seed for reproducible results
	"""
	if seed is not None:
		random.seed(seed)

	print("Creating fractal tree with depth {}...".format(depth))
	print("This will create approximately {} branches".format(2 ** (depth + 1) - 1))

	# Start from origin, pointing upward (90 degrees)
	total_branches = create_branch(
		start_x=0,
		start_y=0,
		start_z=0,
		length=trunk_length,
		angle=90,
		depth=depth,
		branch_count=0
	)

	print("Fractal tree complete! Created {} branches".format(total_branches))


if __name__ == "__main__":
	# Test connection
	print("Testing connection to Rhino...")
	response = send_command("get_scene_info")

	if response["status"] != "success":
		print("ERROR: Cannot connect to Rhino on port {}".format(RHINO_PORT))
		print("Make sure Rhino listener is running!")
		exit(1)

	print("Connection OK\n")

	# Create fractal tree
	create_fractal_tree(trunk_length=30, depth=5, seed=42)
