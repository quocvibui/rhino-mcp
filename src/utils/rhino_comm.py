"""
Communication utilities for Rhino socket connection
"""

import socket

RHINO_HOST = "localhost"
RHINO_PORT = 54321
SOCKET_TIMEOUT = 10


def send_to_rhino(script):
	"""
	Send Python script to Rhino via socket connection
	script: Python script string to execute in Rhino
	return: Response string from Rhino or error message
	"""
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(SOCKET_TIMEOUT)
		sock.connect((RHINO_HOST, RHINO_PORT))

		sock.send(script.encode('utf-8'))

		response = sock.recv(8192).decode('utf-8')
		sock.close()

		return response

	except ConnectionRefusedError:
		return "ERROR: Cannot connect to Rhino. Ensure Rhino is running with listener script active."
	except socket.timeout:
		return "ERROR: Connection timeout. Rhino may be busy or listener not responding."
	except Exception as e:
		return f"ERROR: {str(e)}"
