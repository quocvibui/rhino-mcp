# Example Pattern Scripts

These scripts demonstrate algorithmic pattern generation in Rhino without using Claude or MCP.

## Prerequisites

1. Rhino 7 must be running
2. Rhino listener must be active (run in Rhino):
   ```
   _-RunPythonScript "/path/to/rhino-mcp/server.py" _Enter
   ```

## Running Scripts

All scripts are standalone and can be run directly:

```bash
cd script/
python3 linear_array.py
```

Each script will:
1. Test connection to Rhino
2. Generate the pattern algorithmically
3. Display progress in terminal

## Available Scripts

### linear_array.py
Creates a line of spheres with even spacing.

**Parameters:**
- `count`: Number of spheres (default: 10)
- `spacing`: Distance between spheres (default: 20)
- `radius`: Sphere radius (default: 5)

**Output:** 10 spheres in a line along X-axis

---

### grid_pattern.py
Creates a 2D grid of boxes.

**Parameters:**
- `rows`: Number of rows (default: 5)
- `cols`: Number of columns (default: 5)
- `spacing`: Distance between boxes (default: 15)
- `box_size`: Size of each box (default: 8)

**Output:** 5x5 grid of boxes (25 total)

---

### spiral.py
Creates a 3D spiral of points.

**Parameters:**
- `num_points`: Number of points (default: 50)
- `radius_increment`: How much radius grows per point (default: 2)
- `height_increment`: Vertical spacing (default: 1.5)
- `angle_increment`: Rotation per point in radians (default: 0.5)

**Output:** Ascending spiral of 50 points

---

### parametric_tower.py
Creates a twisting tower with tapering radius using lofted circles.

**Parameters:**
- `floors`: Number of floor levels (default: 15)
- `base_radius`: Radius at ground level (default: 25)
- `height_per_floor`: Vertical spacing (default: 4)
- `taper_rate`: Radius reduction per floor (default: 0.05 = 5%)
- `twist_rate`: Degrees of rotation per floor (default: 10)

**Output:** Lofted tower surface with 15 floors

---

### wave_surface.py
Creates a surface from a mathematical sine wave pattern using curves.

**Parameters:**
- `width`: Total surface width (default: 50)
- `depth`: Total surface depth (default: 50)
- `resolution`: Number of curves (default: 8, use 6-8 for best results)
- `amplitude`: Height of wave peaks (default: 5)

**Output:** Lofted surface with smooth sine wave undulation

**Note:** Uses curves instead of circles for reliable lofting. Creates curves in one direction and lofts them into a smooth surface.

---

### fractal_tree.py
Creates a 3D fractal tree structure using recursive branching.

**Parameters:**
- `trunk_length`: Length of initial trunk (default: 30)
- `depth`: Recursion depth / branch generations (default: 5)
- `seed`: Random seed for reproducible results (default: 42)

**Output:** Recursive branching tree structure with approximately 63 branches at depth 5

**Note:** Each generation creates 2 branches from each previous branch. Depth 5 creates a nice balanced tree.

---

### building_generator.py
Generates a complete building with columns, floor slabs, and organized layers.

**Parameters:**
- `floors`: Number of floors (default: 8)
- `floor_height`: Height of each floor (default: 3.5)
- `width`: Building width in X (default: 40)
- `depth`: Building depth in Y (default: 25)
- `column_radius`: Structural column radius (default: 0.5)
- `slab_thickness`: Floor slab thickness (default: 0.3)

**Output:**
- 4 corner columns extending full height
- 9 floor slabs (ground + 8 floors)
- Organized in "Columns" and "Floors" layers

---

## Customization

Edit the script parameters in the `if __name__ == "__main__":` section:

```python
# Example: Create a larger grid
create_grid_pattern(rows=10, cols=10, spacing=20, box_size=10)
```

## Tips

### Performance
- Scripts include 0.05-0.1s delays between commands to avoid overwhelming Rhino
- Watch Rhino viewport to see objects appear in real-time

### Clean Scene
Before running a script, clear the scene in Rhino:
- Command: `SelAll` then `Delete`
- Or run: `python3 ../test_rhino_listener.py` (includes cleanup)

### Modify for Your Needs
All scripts follow the same template:
1. Connection function
2. Pattern generation function
3. Main execution block

Copy any script as a starting point for your own patterns.

## Troubleshooting

### "Cannot connect to Rhino"
- Ensure Rhino 7 is running
- Verify listener is active (check Rhino command line for status message)
- Port 54321 must not be blocked

### Script runs but nothing appears
- Check Rhino command line for errors
- Verify objects are being created (run `SelAll` in Rhino)
- Some operations may create objects outside the current view

### Lofting fails
- Loft operations require compatible curves
- Try reducing the number of curves
- Ensure curves are properly ordered

## See Also

- **[SCRIPT.md](../SCRIPT.md)** - Full scripting guide with more examples
- **[MCP.md](../MCP.md)** - Using with Claude Desktop
- **[test_rhino_listener.py](../test_rhino_listener.py)** - All 49 commands demonstrated
