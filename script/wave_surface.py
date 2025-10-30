#!/usr/bin/env python3
"""
Wave Surface
Creates a surface from a mathematical sine wave pattern
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


def create_wave_surface(width=60, depth=60, num_curves=8, amplitude=8):
	"""
	Create a surface from a sine wave using polylines (more reliable than curves)

	width: total width of surface
	depth: total depth of surface
	num_curves: number of profile curves (6-10 recommended)
	amplitude: height of wave peaks
	"""
	print("Creating wave surface {}x{} with {} profile curves...".format(width, depth, num_curves))
	print("Using polylines for reliable lofting\n")

	count = 0
	points_per_curve = 20  # More points = smoother wave

	# Create polylines along Y direction at different X positions
	for x_idx in range(num_curves):
		x_pos = (x_idx / float(num_curves - 1)) * width - (width / 2.0)  # Center at origin

		# Create points along this polyline (going in Y direction)
		points = []
		for y_idx in range(points_per_curve):
			y_pos = (y_idx / float(points_per_curve - 1)) * depth - (depth / 2.0)  # Center at origin

			# Calculate wave height
			x_normalized = (x_pos + width/2.0) / width  # 0 to 1
			y_normalized = (y_pos + depth/2.0) / depth  # 0 to 1

			# Two complete sine waves
			z_height = amplitude * math.sin(x_normalized * 4 * math.pi) * math.cos(y_normalized * 4 * math.pi)

			points.append([x_pos, y_pos, z_height])

		# Create polyline through these points
		result = send_command("create_polyline", {
			"points": points
		})

		if result["status"] == "success":
			count += 1
			print("  Created polyline {} of {} at x={:.1f}".format(count, num_curves, x_pos))
		else:
			print("  FAILED to create polyline at x={:.1f}: {}".format(x_pos, result.get("message", "")))
			# Try with create_curve as fallback
			result2 = send_command("create_curve", {
				"points": points,
				"degree": 3
			})
			if result2["status"] == "success":
				count += 1
				print("  Created curve {} of {} at x={:.1f} (fallback)".format(count, num_curves, x_pos))

		time.sleep(0.15)

	print("\nCreated {} profile curves successfully".format(count))

	if count < 3:
		print("ERROR: Need at least 3 curves to loft. Only created {}.".format(count))
		return

	# Loft curves into surface
	print("Lofting {} curves into surface...".format(count))
	send_command("select_by_type", {"type": "curve"})
	time.sleep(0.3)

	result = send_command("loft_curves")
	if result["status"] == "success":
		print("\n=== SUCCESS! ===")
		print("Wave surface created successfully!")
		print("Surface shows smooth flowing wave pattern with multiple undulations!")
	else:
		print("Loft failed: {}".format(result.get("message", "")))
		print("The curves are visible - try selecting them in order and using 'Loft' command in Rhino.")


if __name__ == "__main__":
	# Test connection
	print("Testing connection to Rhino...")
	response = send_command("get_scene_info")

	if response["status"] != "success":
		print("ERROR: Cannot connect to Rhino on port {}".format(RHINO_PORT))
		print("Make sure Rhino listener is running!")
		exit(1)

	print("Connection OK\n")

	# Create wave surface
	create_wave_surface(
		width=60,
		depth=60,
		num_curves=8,
		amplitude=8
	)
