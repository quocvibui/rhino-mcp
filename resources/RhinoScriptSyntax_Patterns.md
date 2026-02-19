# RhinoScriptSyntax Patterns & Recipes

Common workflows for `rhinoscriptsyntax` (rs) in Rhino 8 / CPython 3.

---

## 1. Rhino 8 / CPython 3 Notes

**Type strictness** — PythonNET 3.0 is stricter than IronPython:
```python
# Use float literals for numeric params (radius, angle, tolerance)
rs.AddCircle([0,0,0], 5.0)      # good
rs.AddCircle([0,0,0], 5)        # may cause issues in some contexts

# Tuples for points, not lists, when passing to .NET methods directly
Rhino.Geometry.Point3d(0.0, 0.0, 0.0)  # use floats
```

**Import pattern:**
```python
import rhinoscriptsyntax as rs
import Rhino                     # .NET bridge to RhinoCommon
import System                    # .NET System namespace
```

**Running Rhino commands from script:**
```python
rs.Command("_Circle 0,0,0 5 ", False)  # trailing space = Enter, echo=False
```

---

## 2. Common Types

```python
guid    = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"  # object ID string
point   = [0.0, 5.0, 0.0]    # or (0, 5, 0) tuple
vector  = [0.0, 0.0, 1.0]    # direction, same format as point
plane   = rs.PlaneFromNormal([0,0,0], [0,0,1])  # origin + normal
color   = [255, 0, 0]        # RGB, 0-255
xform   = rs.XformScale(2.0) # 4x4 transformation matrix
```

---

## 3. Creating Geometry

### Points & Curves
```python
pt = rs.AddPoint([0, 0, 0])
line = rs.AddLine([0,0,0], [10,0,0])
circle = rs.AddCircle([0,0,0], 5.0)
arc = rs.AddArc3Pt([0,0,0], [10,0,0], [5,5,0])
ellipse = rs.AddEllipse(rs.WorldXYPlane(), 10.0, 5.0)
rect = rs.AddRectangle(rs.WorldXYPlane(), 20.0, 10.0)
pline = rs.AddPolyline([[0,0,0], [5,0,0], [5,5,0], [0,5,0], [0,0,0]])
curve = rs.AddInterpCurve([[0,0,0], [3,4,0], [6,2,0], [10,5,0]])
nurbs = rs.AddCurve([[0,0,0], [2,4,0], [5,3,0], [8,6,0]], degree=3)
```

### 3D Primitives
```python
box = rs.AddBox([[0,0,0],[10,0,0],[10,10,0],[0,10,0],
                 [0,0,10],[10,0,10],[10,10,10],[0,10,10]])
sphere = rs.AddSphere([0,0,0], 5.0)
cone = rs.AddCone([0,0,0], [0,0,10], 5.0)
cyl = rs.AddCylinder([0,0,0], 10.0, 5.0)
torus = rs.AddTorus(rs.WorldXYPlane(), 10.0, 2.0)
```

### Surfaces from Curves
```python
# Extrude
srf = rs.ExtrudeCurveStraight(curve_id, [0,0,0], [0,0,10])

# Revolve (axis = [start, end])
srf = rs.AddRevSrf(profile_id, [[0,0,0], [0,0,10]])

# Loft through curves
srf = rs.AddLoftSrf([crv1, crv2, crv3])

# Sweep along rail
srf = rs.AddSweep1(rail_id, [shape1, shape2])

# Planar surface from closed curve
srf = rs.AddPlanarSrf([closed_curve_id])

# Edge surface from 2-4 boundary curves
srf = rs.AddEdgeSrf([crv1, crv2, crv3, crv4])

# Pipe along curve
pipes = rs.AddPipe(curve_id, [0, 1], [2.0, 2.0], cap=1)

# Surface from 3-4 corner points
srf = rs.AddSrfPt([[0,0,0], [10,0,0], [10,10,5], [0,10,5]])
```

---

## 4. Modifying Geometry

### Boolean Operations (surfaces/polysurfaces)
```python
result = rs.BooleanUnion([brep1, brep2])
result = rs.BooleanDifference([brep1], [brep2])  # subtract brep2 from brep1
result = rs.BooleanIntersection([brep1], [brep2])
```

### Curve Operations
```python
# Join curves into polycurve
joined = rs.JoinCurves([crv1, crv2, crv3], delete_input=True)

# Offset curve
offset = rs.OffsetCurve(crv, direction_point, 5.0)

# Fillet between two curves
fillet = rs.AddFilletCurve(crv1, crv2, radius=2.0)

# Split curve at parameter
domain = rs.CurveDomain(crv)
mid_t = (domain[0] + domain[1]) / 2.0
pieces = rs.SplitCurve(crv, mid_t)

# Trim curve to interval
trimmed = rs.TrimCurve(crv, [t0, t1])

# Extend curve
extended = rs.ExtendCurveLength(crv, 2, 2, 5.0)  # type=smooth, side=both, length=5

# Explode polycurve into segments
segments = rs.ExplodeCurves([polycurve_id])

# Boolean on closed planar curves
union = rs.CurveBooleanUnion([crv1, crv2])
diff = rs.CurveBooleanDifference(crv1, crv2)
```

### Surface Operations
```python
# Offset surface
offset_srf = rs.OffsetSurface(srf_id, 2.0)

# Split brep with cutter
pieces = rs.SplitBrep(brep_id, cutter_id)

# Fillet between surfaces
fillets = rs.FilletSurfaces(srf1, srf2, radius=1.0)

# Cap planar holes
rs.CapPlanarHoles(open_brep_id)

# Join surfaces into polysurface
joined = rs.JoinSurfaces([srf1, srf2, srf3])

# Explode polysurface
faces = rs.ExplodePolysurfaces([polysrf_id])

# Duplicate edge curves from brep
edges = rs.DuplicateEdgeCurves(brep_id)
```

---

## 5. Transformations

### Basic Transforms
```python
rs.MoveObject(obj, [10, 0, 0])      # translate by vector
rs.MoveObjects(obj_list, [0, 5, 0])

rs.RotateObject(obj, [0,0,0], 45.0)              # 2D rotation (degrees)
rs.RotateObject(obj, [0,0,0], 90.0, [1,0,0])     # 3D: rotate around X axis

rs.ScaleObject(obj, [0,0,0], [2, 2, 2])          # uniform scale 2x
rs.ScaleObject(obj, [0,0,0], [1, 1, 3])          # non-uniform: stretch Z

rs.MirrorObject(obj, [0,0,0], [0,10,0])          # mirror across line

copy = rs.CopyObject(obj, [10, 0, 0])            # copy + translate
copies = rs.CopyObjects(obj_list, [10, 0, 0])
```

### Transform Matrices (for complex operations)
```python
# Compose transforms
t1 = rs.XformTranslation([10, 0, 0])
r1 = rs.XformRotation2(45.0, [0,0,1], [0,0,0])
combined = rs.XformMultiply(t1, r1)
rs.TransformObject(obj, combined)

# Mirror via matrix
mirror = rs.XformMirror([0,0,0], [1,0,0])  # mirror across YZ plane
rs.TransformObject(obj, mirror, copy=True)

# Scale via matrix
scale = rs.XformScale([2.0, 1.0, 0.5])
rs.TransformObject(obj, scale)
```

### Arrays
```python
# Linear array
for i in range(1, count):
    copy = rs.CopyObject(obj, [spacing * i, 0, 0])

# Polar array
for i in range(1, count):
    copy = rs.CopyObject(obj)
    rs.RotateObject(copy, center, 360.0 / count * i)
```

---

## 6. Querying & Analysis

### Object Properties
```python
obj_type = rs.ObjectType(obj)      # 4=curve, 8=surface, 16=polysurface, 32=mesh
bbox = rs.BoundingBox(obj)         # 8 corner points
name = rs.ObjectName(obj)          # get name
rs.ObjectName(obj, "MyObject")     # set name
layer = rs.ObjectLayer(obj)        # get layer
rs.ObjectLayer(obj, "Layer01")     # set layer
color = rs.ObjectColor(obj)        # get color
rs.ObjectColor(obj, [255, 0, 0])   # set color
solid = rs.IsObjectSolid(obj)      # closed volume?
```

### Measurements
```python
length = rs.CurveLength(crv_id)
area = rs.CurveArea(crv_id)                # [area, error]
area = rs.SurfaceArea(srf_id)              # [area, error]
volume = rs.SurfaceVolume(brep_id)         # [volume, error]
dist = rs.Distance([0,0,0], [10,10,10])
```

### Curve Analysis
```python
start = rs.CurveStartPoint(crv)
end = rs.CurveEndPoint(crv)
mid = rs.CurveMidPoint(crv)
domain = rs.CurveDomain(crv)           # [t_min, t_max]
pt = rs.EvaluateCurve(crv, t)          # point at parameter
tan = rs.CurveTangent(crv, t)          # tangent vector at parameter
frame = rs.CurveFrame(crv, t)          # plane at parameter
closed = rs.IsCurveClosed(crv)
planar = rs.IsCurvePlanar(crv)
degree = rs.CurveDegree(crv)
pts = rs.CurvePoints(crv)              # control points
t = rs.CurveClosestPoint(crv, test_pt) # closest parameter
```

### Surface Analysis
```python
uv = rs.SurfaceClosestPoint(srf, test_pt)  # [u, v]
pt = rs.EvaluateSurface(srf, uv[0], uv[1])
nrm = rs.SurfaceNormal(srf, uv)
frame = rs.SurfaceFrame(srf, uv)
domain_u = rs.SurfaceDomain(srf, 0)        # [u_min, u_max]
domain_v = rs.SurfaceDomain(srf, 1)        # [v_min, v_max]
```

### Intersections
```python
# Curve-curve
events = rs.CurveCurveIntersection(crv1, crv2)

# Curve-surface
events = rs.CurveSurfaceIntersection(crv, srf)

# Brep-brep
curves, pts = rs.IntersectBreps(brep1, brep2)

# Point containment
inside = rs.PointInPlanarClosedCurve(pt, crv)  # 0=out, 1=in, 2=on
inside = rs.IsPointInSurface(brep, pt)
```

---

## 7. Organization

### Layers
```python
rs.AddLayer("Walls", color=[255,0,0])
rs.AddLayer("Walls::Interior", parent="Walls")     # sublayer
rs.CurrentLayer("Walls")
rs.LayerVisible("Walls", False)                     # hide
rs.LayerLocked("Walls", True)                       # lock
rs.LayerColor("Walls", [0, 128, 255])
names = rs.LayerNames()
rs.DeleteLayer("EmptyLayer")
rs.PurgeLayer("LayerWithObjects")                   # force delete
```

### Groups
```python
rs.AddGroup("MyGroup")
rs.AddObjectsToGroup(object_ids, "MyGroup")
rs.RemoveObjectsFromGroup(object_ids, "MyGroup")
members = rs.ObjectsByGroup("MyGroup")
rs.DeleteGroup("MyGroup")                           # removes group, not objects
```

### Object Naming & User Data
```python
rs.ObjectName(obj, "Part_001")
objs = rs.ObjectsByName("Part_001")

rs.SetUserText(obj, "material", "steel")
val = rs.GetUserText(obj, "material")               # "steel"
keys = rs.GetUserText(obj)                           # all keys

rs.SetDocumentUserText("project", "Bridge Design")
val = rs.GetDocumentUserText("project")
```

### Materials
```python
idx = rs.AddMaterialToObject(obj)
rs.MaterialColor(idx, [200, 50, 50])
rs.MaterialTransparency(idx, 0.3)
rs.MaterialShine(idx, 128.0)
rs.MaterialTexture(idx, "C:/textures/wood.jpg")
```

---

## 8. Selection

```python
all_objs = rs.AllObjects()
selected = rs.SelectedObjects()
rs.SelectObjects(obj_list)
rs.UnselectAllObjects()

# Filter by type
curves = rs.ObjectsByType(4)       # 4=curve
surfaces = rs.ObjectsByType(8)     # 8=surface
polysrfs = rs.ObjectsByType(16)    # 16=polysurface
meshes = rs.ObjectsByType(32)      # 32=mesh

# Filter by layer
objs = rs.ObjectsByLayer("Walls")

# Filter by name
objs = rs.ObjectsByName("Part_*")

# Last created
recent = rs.LastCreatedObjects()

# Visibility/state
hidden = rs.HiddenObjects()
locked = rs.LockedObjects()
```

---

## 9. Multi-step Recipes

### Solid from Profile (extrude + cap)
```python
profile = rs.AddRectangle(rs.WorldXYPlane(), 10.0, 5.0)
solid = rs.ExtrudeCurveStraight(profile, [0,0,0], [0,0,8])
rs.CapPlanarHoles(solid)
```

### Revolved Vase
```python
pts = [[5,0,0], [4,0,3], [6,0,6], [3,0,9], [4,0,12]]
profile = rs.AddInterpCurve(pts)
vase = rs.AddRevSrf(profile, [[0,0,0], [0,0,12]])
rs.DeleteObject(profile)
```

### Rounded Box (box + fillet edges)
```python
# Create box, fillet with Rhino command
box = rs.AddBox([[0,0,0],[10,0,0],[10,10,0],[0,10,0],
                 [0,0,5],[10,0,5],[10,10,5],[0,10,5]])
rs.SelectObject(box)
rs.Command("_FilletEdge _Radius 1 _Enter _Enter", False)
result = rs.LastCreatedObjects()
```

### Pattern of Objects on Surface
```python
srf = rs.AddSphere([0,0,0], 20.0)
for u in range(0, 10):
    for v in range(0, 10):
        uv = [u/9.0, v/9.0]
        # Convert normalized to surface domain
        dom_u = rs.SurfaceDomain(srf, 0)
        dom_v = rs.SurfaceDomain(srf, 1)
        u_val = dom_u[0] + uv[0] * (dom_u[1] - dom_u[0])
        v_val = dom_v[0] + uv[1] * (dom_v[1] - dom_v[0])
        pt = rs.EvaluateSurface(srf, u_val, v_val)
        rs.AddPoint(pt)
```

### Divide Curve and Place Objects
```python
pts = rs.DivideCurve(curve_id, 20, create_points=False, return_points=True)
for pt in pts:
    rs.AddSphere(pt, 0.5)
```

### Profile Sweep (pipe-like)
```python
rail = rs.AddInterpCurve([[0,0,0], [10,0,5], [20,0,0]])
plane = rs.CurveFrame(rail, rs.CurveDomain(rail)[0])
circle = rs.AddCircle(plane, 2.0)
srf = rs.AddSweep1(rail, [circle])
```

### Boolean Subtract Holes
```python
base = rs.AddBox([[0,0,0],[20,0,0],[20,20,0],[0,20,0],
                  [0,0,5],[20,0,5],[20,20,5],[0,20,5]])
hole1 = rs.AddCylinder([5,5,-1], 7.0, 2.0)
hole2 = rs.AddCylinder([15,15,-1], 7.0, 2.0)
result = rs.BooleanDifference([base], [hole1, hole2])
```

### Move Objects to Layer by Type
```python
for obj in rs.AllObjects():
    t = rs.ObjectType(obj)
    if t == 4:
        rs.ObjectLayer(obj, "Curves")
    elif t in (8, 16):
        rs.ObjectLayer(obj, "Surfaces")
    elif t == 32:
        rs.ObjectLayer(obj, "Meshes")
```
