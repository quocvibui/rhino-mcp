# Rhino MCP Testing Guide

Test your Rhino MCP server step-by-step by pasting these prompts into Claude Desktop.

## Prerequisites

1. Rhino 7 is running
2. Run this in Rhino's Python editor:
   ```
   _-RunPythonScript "/path/to/rhino_listener.py" _Enter
   ```
3. MCP server is configured in Claude Desktop

## Test Sequence

### 1. Initial Setup & Scene Understanding

```
Get the current scene info from Rhino
```

**Expected**: Claude should return details about objects, layers, and units in your Rhino scene.

---

### 2. Basic Geometry Creation

```
Create a sphere at position (0, 0, 0) with radius 5
```

**Expected**: A sphere appears in Rhino at the origin.

```
Create a box at position (20, 0, 0) with width 10, depth 10, and height 10
```

**Expected**: A box appears at x=20.

```
Create a circle at (0, 20, 0) with radius 7
```

**Expected**: A circle appears at y=20.

---

### 3. Curve Creation

```
Create a polyline through these points: [0,40,0], [10,40,0], [10,50,0], [0,50,0]
```

**Expected**: A polyline appears forming an L-shape.

```
Create an arc at center (20,40,0) with radius 5, starting at 0 degrees and ending at 180 degrees
```

**Expected**: A semicircular arc appears.

```
Create an ellipse at center (40,40,0) with x_radius 8 and y_radius 4
```

**Expected**: An ellipse appears.

---

### 4. Transformation Tests

First, select objects for transformation:

```
Select all objects in Rhino
```

**Expected**: All objects are selected.

Now test move:

```
Move the selected objects by displacement vector (-5, 0, 0)
```

**Expected**: Selected objects move 5 units in negative X direction.

```
Select all objects again
```

```
Rotate the selected objects around point (0, 0, 0) by 45 degrees
```

**Expected**: Objects rotate 45 degrees around the origin.

```
Select all objects
```

```
Scale the selected objects from center point (0, 0, 0) by a factor of 1.5
```

**Expected**: Objects grow 1.5x larger.

```
Select the sphere at origin
```

```
Copy the selected objects with displacement (15, 0, 0)
```

**Expected**: A copy of the sphere appears 15 units to the right.

```
Select the box
```

```
Create a linear array of the selected objects with displacement (5, 0, 0) and count 3
```

**Expected**: 2 additional boxes appear, spaced 5 units apart.

---

### 5. Boolean Operations

```
Unselect all objects
```

```
Create a box at (0, 60, 0) with dimensions 10x10x10
```

```
Create another box at (5, 60, 0) with dimensions 10x10x10
```

```
Select all objects
```

```
Perform a boolean union on the selected objects
```

**Expected**: The two boxes merge into one object.

---

### 6. Curve Operations

```
Create a circle at (0, 80, 0) with radius 5
```

```
Select all objects
```

```
Offset the selected curve by distance 2
```

**Expected**: A larger concentric circle appears.

```
Unselect all
```

```
Create a line from (20, 80, 0) to (30, 80, 0)
```

```
Select the line
```

```
Extend the curve by extension length 3
```

**Expected**: The line extends on both ends.

---

### 7. Surface Operations

```
Unselect all objects
```

```
Create a circle at (0, 100, 0) with radius 5
```

```
Select the circle
```

```
Extrude the curve straight up with height 10
```

**Expected**: A cylinder surface is created.

```
Unselect all
```

```
Create 3 circles: one at (20,100,0) radius 3, one at (20,100,5) radius 5, and one at (20,100,10) radius 3
```

```
Select all objects
```

```
Create a lofted surface through the selected curves
```

**Expected**: A smooth surface connects the three circles.

---

### 8. Layer Management

```
Create a new layer named "TestLayer" with color RGB(255, 0, 0)
```

**Expected**: A new red layer is created.

```
Set the current layer to "TestLayer"
```

**Expected**: TestLayer becomes active.

```
List all layers in the document
```

**Expected**: All layers shown including TestLayer.

```
Set layer "Default" visibility to false
```

**Expected**: Objects on Default become hidden.

```
Set layer "Default" visibility to true
```

**Expected**: Objects on Default become visible again.

---

### 9. Object Properties

```
Create a box at (0, 120, 0) with dimensions 5x5x5
```

```
Select the box
```

```
Set the object name to "MyBox"
```

**Expected**: The box is named "MyBox".

```
Set the object color to RGB(0, 255, 0)
```

**Expected**: The box turns green.

```
Move the object to layer "TestLayer"
```

**Expected**: The box moves to TestLayer.

---

### 10. Analysis Tools

```
Measure the distance between point (0,0,0) and point (10,0,0)
```

**Expected**: Distance = 10.

```
Create a line from (0, 140, 0) to (15, 140, 0)
```

```
Select the line
```

```
Measure the length of the selected curve
```

**Expected**: Length = 15.

```
Create a circle at (20, 140, 0) with radius 5
```

```
Select the circle
```

```
Measure the area of the selected object
```

**Expected**: Area ≈ 78.54 (π × 5²).

```
Create a sphere at (40, 140, 0) with radius 5
```

```
Select the sphere
```

```
Measure the volume of the selected object
```

**Expected**: Volume ≈ 523.6 (4/3 × π × 5³).

---

### 11. Selection Operations

```
Select all objects of type "curve"
```

**Expected**: All curves are selected.

```
Select all objects on layer "TestLayer"
```

**Expected**: All objects on TestLayer are selected.

```
Delete the selected objects
```

**Expected**: TestLayer objects are deleted.

```
Unselect all objects
```

---

### 12. Mirror Test

```
Create a sphere at (0, 0, 5) with radius 3
```

```
Select the sphere
```

```
Mirror the selected objects across a line from (0, 0, 0) to (10, 0, 0)
```

**Expected**: A mirrored copy appears on the opposite side of the mirror line.

---

## Troubleshooting

If a command fails:

1. **Check Rhino listener**: Ensure `rhino_listener.py` is still running in Rhino
2. **Check selection**: Some operations require objects to be selected first
3. **Check object types**: Boolean operations require solid objects, not curves
4. **Review error message**: Claude will explain what went wrong

## Success Criteria

All commands should:
- Execute without errors
- Create/modify geometry as described
- Return success messages with relevant details
- Show immediate visual feedback in Rhino
