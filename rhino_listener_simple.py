# Rhino Listener - Simplified for IronPython 2.7
# Test version to isolate syntax issues

import socket
import threading
import rhinoscriptsyntax as rs

print "Starting Rhino MCP Listener..."
print "Version: Simple Test"

SERVER_HOST = "localhost"
SERVER_PORT = 54321

def handle_client(client_socket):
	try:
		data = client_socket.recv(4096)
		print "Received request"

		# Try to execute
		try:
			exec data
			client_socket.send("SUCCESS")
		except Exception as e:
			msg = "ERROR: " + str(e)
			client_socket.send(msg)
	except Exception as e:
		print "Connection error: " + str(e)
	finally:
		try:
			client_socket.close()
		except:
			pass

def run_server():
	server = None
	try:
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		server.bind((SERVER_HOST, SERVER_PORT))
		server.listen(5)
		print "Listener active on port " + str(SERVER_PORT)

		while True:
			try:
				client, addr = server.accept()
				t = threading.Thread(target=handle_client, args=(client,))
				t.daemon = True
				t.start()
			except Exception as e:
				print "Accept error: " + str(e)
	except Exception as e:
		print "Server error: " + str(e)
	finally:
		if server:
			try:
				server.close()
			except:
				pass

# Start server thread
thread = threading.Thread(target=run_server)
thread.daemon = True
thread.start()

print "Listener started in background"
print "Ready to receive commands"
