# Save this file as rhino_listener.py
# Run once in Rhino with: _-RunPythonScript "/Users/quocbui/desktop/rhino_mcp/rhino_listener.py" _Enter

import socket
import threading
import rhinoscriptsyntax as rs

def socket_server():
    """Socket server that runs in background"""
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("localhost", 54321))
        server.listen(1)
        
        print("Rhino MCP listener started on port 54321")
        print("Ready to receive commands from Claude!")
        
        while True:
            try:
                client, addr = server.accept()
                
                # Receive script
                script = client.recv(4096).decode('utf-8')
                
                # Execute script in Rhino's context
                try:
                    exec(script, globals())
                    client.send("SUCCESS: Command executed".encode('utf-8'))
                except Exception as e:
                    error_msg = "ERROR: " + str(e)
                    print("Error: " + error_msg)
                    client.send(error_msg.encode('utf-8'))
                
                client.close()
                
            except Exception as e:
                print("Connection error:", e)
                continue
                
    except Exception as e:
        print("Failed to start server:", e)

# Start server in background thread
print("Starting Rhino MCP listener...")
thread = threading.Thread(target=socket_server)
thread.daemon = True
thread.start()

print("Listener started! Script complete.")