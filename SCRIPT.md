# Scripting Direct Control of Rhino

This guide explains how to write standalone Python scripts that control Rhino algorithmically without using Claude or MCP.

## Overview

The Rhino listener (server.py) is a standalone JSON API server that any program can connect to. You don't need the MCP server or Claude Desktop to use it.

## Architecture

```
Your Python Script <--> Rhino Listener <--> Rhino 8
    (algorithm)      (localhost:54321)   (3D modeling)
```

Your script sends JSON commands directly to Rhino over TCP socket on port 54321.

## Basic Template

```python
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
		sock.settimeout(10)
		sock.connect((RHINO_HOST, RHINO_PORT))
		sock.sendall(json.dumps(command).encode("utf-8"))

		# Chunked reading for large responses
		chunks = []
		while True:
			chunk = sock.recv(8192)
			if not chunk:
				break
			chunks.append(chunk)
			try:
				data = b"".join(chunks)
				response = json.loads(data.decode("utf-8"))
				sock.close()
				return response
			except (json.JSONDecodeError, UnicodeDecodeError):
				continue

		sock.close()
		return {"status": "error", "message": "No response received"}
	except Exception as e:
		return {"status": "error", "message": str(e)}

# Your algorithmic code here
```

## Simple Examples

### Linear Array

```python
# Create a line of spheres
for i in range(10):
	send_command("create_sphere", {
		"center": [i * 20, 0, 0],
		"radius": 5
	})
	time.sleep(0.1)  # Small delay to avoid overwhelming Rhino
```

### Grid Pattern

```python
# Create a grid of boxes
for x in range(5):
	for y in range(5):
		send_command("create_box", {
			"width": 8,
			"depth": 8,
			"height": 8,
			"x": x * 15,
			"y": y * 15,
			"z": 0
		})
		time.sleep(0.1)
```

### Spiral

```python
import math

# Create a spiral of points
num_points = 50
for i in range(num_points):
	angle = i * 0.5
	radius = i * 2
	x = radius * math.cos(angle)
	y = radius * math.sin(angle)
	z = i * 1.5

	send_command("create_point", {"x": x, "y": y, "z": z})
	time.sleep(0.1)
```

## Complex Examples

### Parametric Tower

```python
import math

def create_parametric_tower(floors=10, radius=20, height_per_floor=5):
	"""Create a twisting tower with varying radius"""

	for floor in range(floors):
		z_height = floor * height_per_floor
		floor_radius = radius * (1 - floor * 0.05)  # Taper inward

		send_command("create_circle", {
			"center": [0, 0, z_height],
			"radius": floor_radius
		})
		time.sleep(0.1)

	# Select all circles and loft
	send_command("select_by_type", {"type": "curve"})
	time.sleep(0.1)
	send_command("loft_curves")

# Run it
create_parametric_tower(floors=15, radius=25, height_per_floor=4)
```

### Fractal Tree

```python
import math
import random

def create_branch(start_x, start_y, start_z, length, angle, depth):
	"""Recursively create tree branches"""
	if depth == 0:
		return

	# Calculate end point
	end_x = start_x + length * math.cos(math.radians(angle))
	end_y = start_y + length * math.sin(math.radians(angle))
	end_z = start_z + length * 0.5

	# Create branch
	send_command("create_line", {
		"start": [start_x, start_y, start_z],
		"end": [end_x, end_y, end_z]
	})
	time.sleep(0.05)

	# Create sub-branches with variation
	angle_variation = random.uniform(-30, 30)
	new_length = length * 0.7

	create_branch(end_x, end_y, end_z, new_length, angle + 25 + angle_variation, depth - 1)
	create_branch(end_x, end_y, end_z, new_length, angle - 25 + angle_variation, depth - 1)

# Create a fractal tree
create_branch(0, 0, 0, length=30, angle=90, depth=5)
```

### Wave Surface

```python
import math

def create_wave_surface(width=50, depth=50, resolution=10):
	"""Create a surface from a sine wave"""

	for x in range(resolution):
		for y in range(resolution):
			x_pos = (x / resolution) * width
			y_pos = (y / resolution) * depth
			z_height = 5 * math.sin(x * 0.5) * math.cos(y * 0.5)

			send_command("create_circle", {
				"center": [x_pos, y_pos, z_height],
				"radius": 2
			})
			time.sleep(0.05)

	# Loft into surface
	send_command("select_all")
	time.sleep(0.2)
	send_command("loft_curves")

create_wave_surface(width=100, depth=100, resolution=20)
```

## Advanced Techniques

### Object Selection and Manipulation

```python
# Create objects
send_command("create_box", {"width": 10, "depth": 10, "height": 10, "x": 0, "y": 0, "z": 0})
send_command("create_sphere", {"center": [0, 0, 5], "radius": 7})

# Select all and perform boolean union
send_command("select_all")
time.sleep(0.1)
result = send_command("boolean_union")

if result["status"] == "success":
	print("Boolean union successful")
```

### Layer Organization

```python
def setup_layers():
	"""Create organized layer structure"""
	layers = [
		{"name": "Structure", "color": [100, 100, 100]},
		{"name": "Walls", "color": [255, 255, 255]},
		{"name": "Floors", "color": [200, 150, 100]},
		{"name": "Roof", "color": [150, 50, 50]}
	]

	for layer in layers:
		send_command("create_layer", {
			"name": layer["name"],
			"color": layer["color"]
		})
		time.sleep(0.1)

def create_on_layer(layer_name, create_func):
	"""Create geometry on specific layer"""
	send_command("set_current_layer", {"name": layer_name})
	create_func()

# Use it
setup_layers()
create_on_layer("Structure", lambda: send_command("create_box", {...}))
```

### Error Handling

```python
def safe_command(command_type, params=None, retries=3):
	"""Send command with retry logic"""
	for attempt in range(retries):
		response = send_command(command_type, params)

		if response["status"] == "success":
			return response

		print(f"Attempt {attempt + 1} failed: {response.get('message', 'Unknown error')}")
		time.sleep(0.5)

	return {"status": "error", "message": "Max retries exceeded"}

# Use it
result = safe_command("create_sphere", {"center": [0, 0, 0], "radius": 10})
```

## Tips

### Performance

- Add small delays (0.05-0.1s) between commands to avoid overwhelming Rhino
- Use `select_all` sparingly - be specific with selections when possible
- Clear selection with `unselect_all` between operations

### Debugging

- Check response status: `if response["status"] == "success"`
- Print error messages: `print(response.get("message", ""))`
- Test commands individually before chaining them

### Organization

- Use functions to encapsulate common patterns
- Create reusable building blocks (towers, columns, walls, etc.)
- Organize code into modules for complex projects

## Example: Complete Building Generator

```python
def generate_building(floors=5, floor_height=4, width=30, depth=20):
	"""Generate a complete building with structure and floors"""

	# Setup layers
	send_command("create_layer", {"name": "Columns", "color": [100, 100, 100]})
	send_command("create_layer", {"name": "Floors", "color": [200, 200, 200]})

	# Create columns at corners
	send_command("set_current_layer", {"name": "Columns"})
	column_positions = [
		[0, 0], [width, 0], [0, depth], [width, depth]
	]

	for x, y in column_positions:
		send_command("create_cylinder", {
			"base": [x, y, 0],
			"height": floors * floor_height,
			"radius": 0.5
		})
		time.sleep(0.1)

	# Create floor slabs
	send_command("set_current_layer", {"name": "Floors"})

	for floor in range(floors + 1):
		z = floor * floor_height
		send_command("create_box", {
			"width": width,
			"depth": depth,
			"height": 0.3,
			"x": 0,
			"y": 0,
			"z": z
		})
		time.sleep(0.1)

# Generate building
generate_building(floors=8, floor_height=3.5, width=40, depth=25)
```

## See Also

- **[MCP.md](MCP.md)** - Using with Claude Desktop
- **[README.md](README.md)** - Full project documentation
- **[IMPLEMENTED.md](IMPLEMENTED.md)** - Implemented features
- **[TESTING.md](TESTING.md)** - Testing guide
