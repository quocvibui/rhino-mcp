#!/usr/bin/env python3
"""
Test script to verify rhino_listener.py works with IronPython 2.7 syntax
"""

import socket
import json
import time

RHINO_HOST = "localhost"
RHINO_PORT = 54321


def test_command(command_type, params=None):
	"""Test sending a command to Rhino"""
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

		print("Sending command: {0}".format(command_type))
		sock.sendall(json.dumps(command).encode('utf-8'))

		response_data = sock.recv(8192)
		sock.close()

		response = json.loads(response_data.decode('utf-8'))
		print("Response: {0}".format(json.dumps(response, indent=2)))
		return response

	except ConnectionRefusedError:
		print("ERROR: Cannot connect to Rhino on port {0}".format(RHINO_PORT))
		print("Make sure:")
		print("1. Rhino 7 is running")
		print("2. You've run the rhino_listener.py script in Rhino")
		return None
	except Exception as e:
		print("ERROR: {0}".format(str(e)))
		return None


def main():
	"""Run tests"""
	print("=" * 60)
	print("Testing Rhino Listener JSON Protocol")
	print("=" * 60)
	print()

	print("Test 1: Get scene info")
	test_command("get_scene_info")
	print()

	print("Test 2: Create point")
	test_command("create_point", {"x": 5, "y": 5, "z": 0})
	print()

	print("Test 3: Create box")
	test_command("create_box", {"width": 10, "depth": 10, "height": 10})
	print()

	print("Test 4: Create sphere")
	test_command("create_sphere", {"center": [20, 0, 0], "radius": 5})
	print()

	print("Test 5: Unknown command (should fail)")
	test_command("unknown_command")
	print()

	print("=" * 60)
	print("Tests complete")
	print("=" * 60)


if __name__ == "__main__":
	main()
