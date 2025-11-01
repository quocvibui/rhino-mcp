"""
Utility functions for MCP tools
"""

import socket
import json

RHINO_HOST = "localhost"
RHINO_PORT = 54321
SOCKET_TIMEOUT = 10


def send_to_rhino(command_type, params=None):
	"""
	Send JSON command to Rhino and return response
	command_type: Command type string
	params: Parameters dictionary
	return: Response dictionary from Rhino
	"""
	if params is None:
		params = {}

	command = {
		"type": command_type,
		"params": params
	}

	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(SOCKET_TIMEOUT)
		sock.connect((RHINO_HOST, RHINO_PORT))

		sock.sendall(json.dumps(command).encode('utf-8'))

		response_data = sock.recv(8192)
		sock.close()

		response = json.loads(response_data.decode('utf-8'))

		if response.get("status") == "error":
			raise Exception(response.get("message", "Unknown error from Rhino"))

		return response.get("result", {})

	except ConnectionRefusedError:
		raise Exception("Cannot connect to Rhino. Ensure listener is running.")
	except socket.timeout:
		raise Exception("Connection timeout. Rhino may be busy.")
	except json.JSONDecodeError as e:
		raise Exception("Invalid response from Rhino: {0}".format(str(e)))
	except Exception as e:
		raise Exception("Communication error: {0}".format(str(e)))
