"""
Utility functions for MCP tools
"""

import socket
import json

RHINO_HOST = "localhost"
RHINO_PORT = 54321
SOCKET_TIMEOUT = 30
RECV_CHUNK_SIZE = 8192


def send_to_rhino(command_type, params=None):
	"""
	Send JSON command to Rhino and return response.
	Uses chunked reading to handle large responses.
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

		sock.sendall(json.dumps(command).encode("utf-8"))

		# Chunked reading for large responses
		chunks = []
		while True:
			chunk = sock.recv(RECV_CHUNK_SIZE)
			if not chunk:
				break
			chunks.append(chunk)
			# Try to parse - if valid JSON, we have the full response
			try:
				response_data = b"".join(chunks)
				response = json.loads(response_data.decode("utf-8"))
				break
			except (json.JSONDecodeError, UnicodeDecodeError):
				continue

		sock.close()

		if not chunks:
			raise Exception("Empty response from Rhino")

		response_data = b"".join(chunks)
		response = json.loads(response_data.decode("utf-8"))

		if response.get("status") == "error":
			raise Exception(response.get("message", "Unknown error from Rhino"))

		return response.get("result", {})

	except ConnectionRefusedError:
		raise Exception("Cannot connect to Rhino. Ensure listener is running.")
	except socket.timeout:
		raise Exception("Connection timeout. Rhino may be busy.")
	except json.JSONDecodeError as e:
		raise Exception(f"Invalid response from Rhino: {e}")
	except Exception as e:
		raise Exception(f"Communication error: {e}")
