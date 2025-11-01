# RhinoScriptSyntax - Quick Reference

Fast lookup for function signatures and parameters.

**Statistics:**
- Total Functions: 898
- Currently in Use: 60
- Available: 838

**Legend:** [IN USE] = Function currently used in code

---

## Table of Contents

- [Application](#application)
- [Block](#block)
- [Curve](#curve)
- [Dimension](#dimension)
- [Document](#document)
- [Geometry](#geometry)
- [Grips](#grips)
- [Group](#group)
- [Hatch](#hatch)
- [Layer](#layer)
- [Light](#light)
- [Line](#line)
- [Linetype](#linetype)
- [Material](#material)
- [Mesh](#mesh)
- [Object](#object)
- [Plane](#plane)
- [Pointvector](#pointvector)
- [Selection](#selection)
- [Surface](#surface)
- [Toolbar](#toolbar)
- [Transformation](#transformation)
- [Userdata](#userdata)
- [Userinterface](#userinterface)
- [Utility](#utility)
- [View](#view)

---

## Application

**`AddAlias(alias, macro)`** - Add new command alias to Rhino. Command aliases can be added manually by using Rhino's Options co...
**`AddSearchPath(folder, index=-1)`** - Add new path to Rhino's search path list. Search paths can be added by using Rhino's Options comm...
**`AliasCount()`** - Returns number of command aliases in Rhino.
**`AliasMacro(alias, macro=None)`** - Returns or modifies the macro of a command alias.
**`AliasNames()`** - Returns a list of command alias names.
**`AppearanceColor(item, color=None)`** - Returns or modifies an application interface item's color.
**`AutosaveFile(filename=None)`** - Returns or changes the file name used by Rhino's automatic file saving
**`AutosaveInterval(minutes=None)`** - Returns or changes how often the document will be saved when Rhino's automatic file saving mechan...
**`BuildDate()`** - Returns the build date of Rhino
**`ClearCommandHistory()`** - Clears contents of Rhino's command history window. You can view the command history window by usi...
**`Command(commandString, echo=True)`** - Runs a Rhino command script. All Rhino commands can be used in command scripts. The command can b...
**`CommandHistory()`** - Returns the contents of Rhino's command history window
**`DefaultRenderer(renderer=None)`** - Returns or changes the default render plug-in
**`DeleteAlias(alias)`** - Delete an existing alias from Rhino.
**`DeleteSearchPath(folder)`** - Removes existing path from Rhino's search path list. Search path items can be removed manually by...
**`DisplayOleAlerts(enable)`** - Enables/disables OLE Server Busy/Not Responding dialog boxes
**`EdgeAnalysisColor(color=None)`** - Returns or modifies edge analysis color displayed by the ShowEdges command
**`EdgeAnalysisMode(mode=None)`** - Returns or modifies edge analysis mode displayed by the ShowEdges command
**`EnableAutosave(enable=True)`** - Enables or disables Rhino's automatic file saving mechanism
**`EnablePlugIn(plugin, enable=None)`** - Enables or disables a Rhino plug-in
**`ExeFolder()`** - Returns the full path to Rhino's executable folder.
**`ExePlatform()`** - Returns the platform of the Rhino executable
**`ExeServiceRelease()`** - Returns the service release number of the Rhino executable
**`ExeVersion()`** - Returns the major version number of the Rhino executable
**`Exit()`** - Closes the rhino application
**`FindFile(filename)`** - Searches for a file using Rhino's search path. Rhino will look for a file in the following locati...
**`GetPlugInObject(plug_in)`** - Returns a scriptable object from a specified plug-in. Not all plug-ins contain scriptable objects...
**`InCommand(ignore_runners=True)`** - Determines if Rhino is currently running a command. Because Rhino allows for transparent commands...
**`InstallFolder()`** - The full path to Rhino's installation folder
**`IsAlias(alias)`** - Verifies that a command alias exists in Rhino
**`IsCommand(command_name)`** - Verifies that a command exists in Rhino. Useful when scripting commands found in 3rd party plug-ins.
**`IsPlugIn(plugin)`** - Verifies that a plug-in is registered
**`IsRunningOnWindows()`** - Returns True if this script is being executed on a Windows platform
**`LastCommandName()`** - Returns the name of the last executed command
**`LastCommandResult()`** - Returns the result code for the last executed command
**`LocaleID()`** - Returns the current language used for the Rhino interface. The current language is returned as a ...
**`Ortho(enable=None)`** - Enables or disables Rhino's ortho modeling aid.
**`Osnap(enable=None)`** - Enables or disables Rhino's object snap modeling aid. Object snaps are tools for specifying point...
**`OsnapDialog(visible=None)`** - Shows or hides Rhino's dockable object snap bar
**`OsnapMode(mode=None)`** - Returns or sets the object snap mode. Object snaps are tools for specifying points on existing ob...
**`Planar(enable=None)`** - Enables or disables Rhino's planar modeling aid
**`PlugInId(plugin)`** - Returns the identifier of a plug-in given the plug-in name
**`PlugIns(types=0, status=0)`** - Returns a list of registered Rhino plug-ins
**`ProjectOsnaps(enable=None)`** - Enables or disables object snap projection
**`Prompt(message=None)`** - Change Rhino's command window prompt
**`ScreenSize()`** - Returns current width and height, of the screen of the primary monitor.
**`SdkVersion()`** - Returns version of the Rhino SDK supported by the executing Rhino.
**`SearchPathCount()`** - Returns the number of path items in Rhino's search path list. See "Options Files settings" in the...
**`SearchPathList()`** - Returns all of the path items in Rhino's search path list. See "Options Files settings" in the Rh...
**`SendKeystrokes(keys=None, add_return=True)`** - Sends a string of printable characters to Rhino's command line
**`Snap(enable=None)`** - Enables or disables Rhino's grid snap modeling aid
**`StatusBarDistance(distance=0)`** - Sets Rhino's status bar distance pane
**`StatusBarMessage(message=None)`** - Sets Rhino's status bar message pane
**`StatusBarPoint(point=None)`** - Sets Rhino's status bar point coordinate pane
**`StatusBarProgressMeterHide()`** - Hide the progress meter
**`StatusBarProgressMeterShow(label, lower, upper, embed_label=True, show_percent=True)`** - Start the Rhino status bar progress meter
**`StatusBarProgressMeterUpdate(position, absolute=True)`** - Set the current position of the progress meter
**`TemplateFile(filename=None)`** - Returns or sets Rhino's default template file. This is the file used when Rhino starts.
**`TemplateFolder(folder=None)`** - Returns or sets the location of Rhino's template folder
**`WindowHandle()`** - Returns the windows handle of Rhino's main window
**`WorkingFolder(folder=None)`** - Returns or sets Rhino's working folder (directory). The working folder is the default folder for ...

---

## Block

**`AddBlock(object_ids, base_point, name=None, delete_input=False)`** - Adds a new block definition to the document
**`BlockContainerCount(block_name)`** - Returns number of block definitions that contain a specified block definition
**`BlockContainers(block_name)`** - Returns names of the block definitions that contain a specified block definition.
**`BlockCount()`** - Returns the number of block definitions in the document
**`BlockDescription(block_name, description=None)`** - Returns or sets the description of a block definition
**`BlockInstanceCount(block_name,where_to_look=0)`** - Counts number of instances of the block in the document. Nested instances are not included in the...
**`BlockInstanceInsertPoint(object_id)`** - Returns the insertion point of a block instance.
**`BlockInstanceName(object_id)`** - Returns the block name of a block instance
**`BlockInstanceXform(object_id)`** - Returns the location of a block instance relative to the world coordinate system origin (0,0,0). ...
**`BlockInstances(block_name,where_to_look=0)`** - Returns the identifiers of the inserted instances of a block.
**`BlockNames( sort=False )`** - Returns the names of all block definitions in the document
**`BlockObjectCount(block_name)`** - Returns number of objects that make up a block definition
**`BlockObjects(block_name)`** - Returns identifiers of the objects that make up a block definition
**`BlockPath(block_name)`** - Returns path to the source of a linked or embedded block definition. A linked or embedded block d...
**`BlockStatus(block_name)`** - Returns the status of a linked block
**`DeleteBlock(block_name)`** - Deletes a block definition and all of it's inserted instances.
**`ExplodeBlockInstance(object_id, explode_nested_instances=False)`** - Explodes a block instance into it's geometric components. The exploded objects are added to the d...
**`InsertBlock( block_name, insertion_point, scale=(1,1,1), angle_degrees=0, rotation_normal=(0,0,1) )`** - Inserts a block whose definition already exists in the document
**`InsertBlock2(block_name, xform)`** - Inserts a block whose definition already exists in the document
**`IsBlock(block_name)`** - Verifies the existence of a block definition in the document.
**`IsBlockEmbedded(block_name)`** - Verifies a block definition is embedded, or linked, from an external file.
**`IsBlockInUse(block_name, where_to_look=0)`** - Verifies that a block definition is being used by an inserted instance
**`IsBlockInstance(object_id)`** - Verifies an object is a block instance
**`IsBlockReference(block_name)`** - Verifies that a block definition is from a reference file.
**`RenameBlock( block_name, new_name )`** - Renames an existing block definition

---

## Curve

### Currently Used

#### `AddArc3Pt(start, end, point_on_arc)`
**Adds a 3-point arc curve to the document**
*Returns:* guid: id of the new curve object

#### `AddCircle(plane_or_center, radius)`
**Adds a circle curve to the document**
*Returns:* guid: id of the new curve object

#### `AddEllipse(plane, radiusX, radiusY)`
**Adds an elliptical curve to the document**
*Returns:* guid: id of the new curve object if successful

#### `AddInterpCurve(points, degree=3, knotstyle=0, start_tangent=None, end_tangent=None)`
**Adds an interpolated curve object to the document. Options exist to make a periodic curve or to specify the tangent at the endpoints. The resulting curve is a non-rational NURBS curve of the specified degree.**
*Returns:* guid: id of the new curve object if successful

#### `AddLine(start, end)`
**Adds a line curve to the current model.**
*Returns:* guid: id of the new curve object

#### `AddPolyline(points, replace_id=None)`
**Adds a polyline curve to the current model**
*Returns:* guid: id of the new curve object if successful

#### `CurveArea(curve_id)`
**Returns area of closed planar curves. The results are based on the current drawing units.**
*Returns:* list[number, number]: List of area information. The list will contain the following information: Element Description [0] The area. If more than one curve was specified, the value will be the cumulative area. [1] The absolute (+/-) error bound for the area.

#### `CurveLength(curve_id, segment_index=-1, sub_domain=None)`
**Returns the length of a curve object.**
*Returns:* number: The length of the curve if successful. None: if not successful, or on error.

#### `ExplodeCurves(curve_ids, delete_input=False)`
**Explodes, or un-joins, one curves. Polycurves will be exploded into curve segments. Polylines will be exploded into line segments. ExplodeCurves will return the curves in topological order.**
*Returns:* list(guid, ...): identifying the newly created curve objects

#### `ExtendCurveLength(curve_id, extension_type, side, length)`
**Extends a non-closed curve by a line, arc, or smooth extension for a specified distance**
*Returns:* guid: The identifier of the new object None: if not successful

#### `IsCurve(object_id)`
**Verifies an object is a curve**
*Returns:* bool: True or False

#### `IsCurveClosed(object_id)`
**Verifies an object is a closed curve object**
*Returns:* bool: True if successful otherwise False. None on error

#### `IsCurvePlanar(curve_id, segment_index=-1)`
**Verifies an object is a planar curve**
*Returns:* bool: True or False indicating success or failure

#### `JoinCurves(object_ids, delete_input=False, tolerance=None)`
**Joins multiple curves together to form one or more curves or polycurves**
*Returns:* list(guid, ...): Object id representing the new curves

#### `OffsetCurve(object_id, direction, distance, normal=None, style=1)`
**Offsets a curve by a distance. The offset curve will be added to Rhino**
*Returns:* list(guid, ...): list of ids for the new curves on success None: on error

### Available Functions

**`AddArc(plane, radius, angle_degrees)`** - Adds an arc curve to the document
**`AddArcPtTanPt(start, direction, end)`** - Adds an arc curve, created from a start point, a start direction, and an end point, to the document
**`AddBlendCurve(curves, parameters, reverses, continuities)`** - Makes a curve blend between two curves
**`AddCircle3Pt(first, second, third)`** - Adds a 3-point circle curve to the document
**`AddCurve(points, degree=3)`** - Adds a control points curve object to the document
**`AddEllipse3Pt(center, second, third)`** - Adds a 3-point elliptical curve to the document
**`AddFilletCurve(curve0id, curve1id, radius=1.0, base_point0=None, base_point1=None)`** - Adds a fillet curve between two curve objects
**`AddInterpCrvOnSrf(surface_id, points)`** - Adds an interpolated curve object that lies on a specified surface. Note, this function will not ...
**`AddInterpCrvOnSrfUV(surface_id, points)`** - Adds an interpolated curve object based on surface parameters, that lies on a specified surface. ...
**`AddNurbsCurve(points, knots, degree, weights=None)`** - Adds a NURBS curve object to the document
**`AddRectangle(plane, width, height)`** - Add a rectangular curve to the document
**`AddSpiral(point0, point1, pitch, turns, radius0, radius1=None)`** - Adds a spiral or helical curve to the document
**`AddSubCrv(curve_id, param0, param1)`** - Add a curve object based on a portion, or interval of an existing curve object. Similar in operat...
**`AddTweenCurves(from_curve_id, to_curve_id, number_of_curves = 1, method = 0, sample_number = 10)`** - Creates curves between two open or closed input curves.
**`ArcAngle(curve_id, segment_index=-1)`** - Returns the angle of an arc curve object.
**`ArcCenterPoint(curve_id, segment_index=-1)`** - Returns the center point of an arc curve object
**`ArcMidPoint(curve_id, segment_index=-1)`** - Returns the mid point of an arc curve object
**`ArcRadius(curve_id, segment_index=-1)`** - Returns the radius of an arc curve object
**`ChangeCurveDegree(object_id, degree)`** - Changes the degree of a curve object. For more information see the Rhino help file for the Change...
**`CircleCenterPoint(curve_id, segment_index=-1, return_plane=False)`** - Returns the center point of a circle curve object
**`CircleCircumference(curve_id, segment_index=-1)`** - Returns the circumference of a circle curve object
**`CircleRadius(curve_id, segment_index=-1)`** - Returns the radius of a circle curve object
**`CloseCurve(curve_id, tolerance=-1.0)`** - Closes an open curve object by making adjustments to the end points so they meet at a point
**`ClosedCurveOrientation(curve_id, direction=(0,0,1))`** - Determine the orientation (counter-clockwise or clockwise) of a closed, planar curve
**`ConvertCurveToPolyline(curve_id, angle_tolerance=5.0, tolerance=0.01, delete_input=False, min_edge_length=0, max_edge_length=0)`** - Convert curve to a polyline curve
**`CurveArcLengthPoint(curve_id, length, from_start=True)`** - Returns the point on the curve that is a specified arc length from the start of the curve.
**`CurveAreaCentroid(curve_id)`** - Returns area centroid of closed, planar curves. The results are based on the current drawing units.
**`CurveArrows(curve_id, arrow_style=None)`** - Enables or disables a curve object's annotation arrows
**`CurveBooleanDifference(curve_id_0, curve_id_1, tolerance=None)`** - Calculates the difference between two closed, planar curves and adds the results to the document....
**`CurveBooleanIntersection(curve_id_0, curve_id_1, tolerance=None)`** - Calculates the intersection of two closed, planar curves and adds the results to the document. No...
**`CurveBooleanUnion(curve_id, tolerance=None)`** - Calculate the union of two or more closed, planar curves and add the results to the document. Not...
**`CurveBrepIntersect(curve_id, brep_id, tolerance=None)`** - Intersects a curve object with a brep object. Note, unlike the CurveSurfaceIntersection function,...
**`CurveClosestObject(curve_id, object_ids)`** - Returns the 3D point locations on two objects where they are closest to each other. Note, this fu...
**`CurveClosestPoint(curve_id, test_point, segment_index=-1 )`** - Returns parameter of the point on a curve that is closest to a test point.
**`CurveContourPoints(curve_id, start_point, end_point, interval=None)`** - Returns the 3D point locations calculated by contouring a curve object.
**`CurveCurvature(curve_id, parameter)`** - Returns the curvature of a curve at a parameter. See the Rhino help for details on curve curvature
**`CurveCurveIntersection(curveA, curveB=None, tolerance=-1)`** - Calculates intersection of two curve objects.
**`CurveDegree(curve_id, segment_index=-1)`** - Returns the degree of a curve object.
**`CurveDeviation(curve_a, curve_b)`** - Returns the minimum and maximum deviation between two curve objects
**`CurveDim(curve_id, segment_index=-1)`** - Returns the dimension of a curve object
**`CurveDirectionsMatch(curve_id_0, curve_id_1)`** - Tests if two curve objects are generally in the same direction or if they would be more in the sa...
**`CurveDiscontinuity(curve_id, style)`** - Search for a derivatitive, tangent, or curvature discontinuity in a curve object.
**`CurveDomain(curve_id, segment_index=-1)`** - Returns the domain of a curve object as an indexable object with two elements.
**`CurveEditPoints(curve_id, return_parameters=False, segment_index=-1)`** - Returns the edit, or Greville, points of a curve object. For each curve control point, there is a...
**`CurveEndPoint(curve_id, segment_index=-1)`** - Returns the end point of a curve object
**`CurveFilletPoints(curve_id_0, curve_id_1, radius=1.0, base_point_0=None, base_point_1=None, return_points=True)`** - Find points at which to cut a pair of curves so that a fillet of a specified radius fits. A fille...
**`CurveFrame(curve_id, parameter, segment_index=-1)`** - Returns the plane at a parameter of a curve. The plane is based on the tangent and curvature vect...
**`CurveKnotCount(curve_id, segment_index=-1)`** - Returns the knot count of a curve object.
**`CurveKnots(curve_id, segment_index=-1)`** - Returns the knots, or knot vector, of a curve object
**`CurveMidPoint(curve_id, segment_index=-1)`** - Returns the mid point of a curve object.
**`CurveNormal(curve_id, segment_index=-1)`** - Returns the normal direction of the plane in which a planar curve object lies.
**`CurveNormalizedParameter(curve_id, parameter)`** - Converts a curve parameter to a normalized curve parameter; one that ranges between 0-1
**`CurveParameter(curve_id, parameter)`** - Converts a normalized curve parameter to a curve parameter; one within the curve's domain
**`CurvePerpFrame(curve_id, parameter)`** - Returns the perpendicular plane at a parameter of a curve. The result is relatively parallel (zer...
**`CurvePlane(curve_id, segment_index=-1)`** - Returns the plane in which a planar curve lies. Note, this function works only on planar curves.
**`CurvePointCount(curve_id, segment_index=-1)`** - Returns the control points count of a curve object.
**`CurvePoints(curve_id, segment_index=-1)`** - Returns the control points, or control vertices, of a curve object. If the curve is a rational NU...
**`CurveRadius(curve_id, test_point, segment_index=-1)`** - Returns the radius of curvature at a point on a curve.
**`CurveSeam(curve_id, parameter)`** - Adjusts the seam, or start/end, point of a closed curve.
**`CurveStartPoint(curve_id, segment_index=-1, point=None)`** - Returns the start point of a curve object
**`CurveSurfaceIntersection(curve_id, surface_id, tolerance=-1, angle_tolerance=-1)`** - Calculates intersection of a curve object with a surface object. Note, this function works on the...
**`CurveTangent(curve_id, parameter, segment_index=-1)`** - Returns a 3D vector that is the tangent to a curve at a parameter.
**`CurveWeights(curve_id, segment_index=-1)`** - Returns list of weights that are assigned to the control points of a curve
**`DivideCurve(curve_id, segments, create_points=False, return_points=True)`** - Divides a curve object into a specified number of segments.
**`DivideCurveEquidistant(curve_id, distance, create_points=False, return_points=True)`** - Divides a curve such that the linear distance between the points is equal.
**`DivideCurveLength(curve_id, length, create_points=False, return_points=True)`** - Divides a curve object into segments of a specified length.
**`EllipseCenterPoint(curve_id)`** - Returns the center point of an elliptical-shaped curve object.
**`EllipseQuadPoints(curve_id)`** - Returns the quadrant points of an elliptical-shaped curve object.
**`EvaluateCurve(curve_id, t, segment_index=-1)`** - Evaluates a curve at a parameter and returns a 3D point
**`ExtendCurve(curve_id, extension_type, side, boundary_object_ids)`** - Extends a non-closed curve object by a line, arc, or smooth extension until it intersects a colle...
**`ExtendCurvePoint(curve_id, side, point, extension_type=2)`** - Extends a non-closed curve by smooth extension to a point
**`FairCurve(curve_id, tolerance=1.0)`** - Fairs a curve. Fair works best on degree 3 (cubic) curves. Fair attempts to remove large curvatur...
**`FitCurve(curve_id, degree=3, distance_tolerance=-1, angle_tolerance=-1)`** - Reduces number of curve control points while maintaining the curve's same general shape. Use this...
**`InsertCurveKnot(curve_id, parameter, symmetrical=False )`** - Inserts a knot into a curve object
**`IsArc(curve_id, segment_index=-1)`** - Verifies an object is an open arc curve
**`IsCircle(curve_id, tolerance=None)`** - Verifies an object is a circle curve
**`IsCurveClosable(curve_id, tolerance=None)`** - Decide if it makes sense to close off the curve by moving the end point to the start point based ...
**`IsCurveInPlane(object_id, plane=None)`** - Test a curve to see if it lies in a specific plane
**`IsCurveLinear(object_id, segment_index=-1)`** - Verifies an object is a linear curve
**`IsCurvePeriodic(curve_id, segment_index=-1)`** - Verifies an object is a periodic curve object
**`IsCurveRational(curve_id, segment_index=-1)`** - Verifies an object is a rational NURBS curve
**`IsEllipse(object_id, segment_index=-1)`** - Verifies an object is an elliptical-shaped curve
**`IsLine(object_id, segment_index=-1)`** - Verifies an object is a line curve
**`IsPointOnCurve(object_id, point, segment_index=-1)`** - Verifies that a point is on a curve
**`IsPolyCurve(object_id, segment_index=-1)`** - Verifies an object is a PolyCurve curve
**`IsPolyline( object_id, segment_index=-1 )`** - Verifies an object is a Polyline curve object
**`LineFitFromPoints(points)`** - Returns a line that was fit through an array of 3D points
**`MakeCurveNonPeriodic(curve_id, delete_input=False)`** - Makes a periodic curve non-periodic. Non-periodic curves can develop kinks when deformed
**`MeanCurve(curve0, curve1, tolerance=None)`** - Creates an average curve from two curves
**`MeshPolyline(polyline_id)`** - Creates a polygon mesh object based on a closed polyline curve object. The created mesh object is...
**`OffsetCurveOnSurface(curve_id, surface_id, distance_or_parameter)`** - Offset a curve on a surface. The source curve must lie on the surface. The offset curve or curves...
**`PlanarClosedCurveContainment(curve_a, curve_b, plane=None, tolerance=None)`** - Determines the relationship between the regions bounded by two coplanar simple closed curves
**`PlanarCurveCollision(curve_a, curve_b, plane=None, tolerance=None)`** - Determines if two coplanar curves intersect
**`PointInPlanarClosedCurve(point, curve, plane=None, tolerance=None)`** - Determines if a point is inside of a closed curve, on a closed curve, or outside of a closed curve
**`PolyCurveCount(curve_id, segment_index=-1)`** - Returns the number of curve segments that make up a polycurve
**`PolylineVertices(curve_id, segment_index=-1)`** - Returns the vertices of a polyline curve on success
**`ProjectCurveToMesh(curve_ids, mesh_ids, direction)`** - Projects one or more curves onto one or more surfaces or meshes
**`ProjectCurveToSurface(curve_ids, surface_ids, direction)`** - Projects one or more curves onto one or more surfaces or polysurfaces
**`RebuildCurve(curve_id, degree=3, point_count=10)`** - Rebuilds a curve to a given degree and control point count. For more information, see the Rhino h...
**`RemoveCurveKnot(curve, parameter)`** - Deletes a knot from a curve object.
**`ReverseCurve(curve_id)`** - Reverses the direction of a curve object. Same as Rhino's Dir command
**`SimplifyCurve(curve_id, flags=0)`** - Replace a curve with a geometrically equivalent polycurve. The polycurve will have the following ...
**`SplitCurve(curve_id, parameter, delete_input=True)`** - Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of th...
**`TrimCurve(curve_id, interval, delete_input=True)`** - Trims a curve by removing portions of the curve outside a specified interval

---

## Dimension

### Available Functions

**`AddAlignedDimension(start_point, end_point, point_on_dimension_line, style=None)`** - Adds an aligned dimension object to the document. An aligned dimension is a linear dimension line...
**`AddDimStyle(dimstyle_name=None)`** - Adds a new dimension style to the document. The new dimension style will be initialized with the ...
**`AddLeader(points, view_or_plane=None, text=None)`** - Adds a leader to the document. Leader objects are planar. The 3D points passed to this function s...
**`AddLinearDimension(plane, start_point, end_point, point_on_dimension_line)`** - Adds a linear dimension to the document
**`CurrentDimStyle(dimstyle_name=None)`** - Returns or changes the current default dimension style
**`DeleteDimStyle(dimstyle_name)`** - Removes an existing dimension style from the document. The dimension style to be removed cannot b...
**`DimStyleAnglePrecision(dimstyle, precision=None)`** - Returns or changes the angle display precision of a dimension style
**`DimStyleArrowSize(dimstyle, size=None)`** - Returns or changes the arrow size of a dimension style
**`DimStyleCount()`** - Returns the number of dimension styles in the document
**`DimStyleExtension(dimstyle, extension=None)`** - Returns or changes the extension line extension of a dimension style
**`DimStyleFont(dimstyle, font=None)`** - Returns or changes the font used by a dimension style
**`DimStyleLeaderArrowSize(dimstyle, size=None)`** - Returns or changes the leader arrow size of a dimension style
**`DimStyleLengthFactor(dimstyle, factor=None)`** - Returns or changes the length factor of a dimension style. Length factor is the conversion betwee...
**`DimStyleLinearPrecision(dimstyle, precision=None)`** - Returns or changes the linear display precision of a dimension style
**`DimStyleNames(sort=False)`** - Returns the names of all dimension styles in the document
**`DimStyleNumberFormat(dimstyle, format=None)`** - Returns or changes the number display format of a dimension style
**`DimStyleOffset(dimstyle, offset=None)`** - Returns or changes the extension line offset of a dimension style
**`DimStylePrefix(dimstyle, prefix=None)`** - Returns or changes the prefix of a dimension style - the text to prefix to the dimension text.
**`DimStyleScale(dimstyle, scale=None)`** - Returns or modifies the scale of a dimension style.
**`DimStyleSuffix(dimstyle, suffix=None)`** - Returns or changes the suffix of a dimension style - the text to append to the dimension text.
**`DimStyleTextAlignment(dimstyle, alignment=None)`** - Returns or changes the text alignment mode of a dimension style
**`DimStyleTextGap(dimstyle, gap=None)`** - Returns or changes the text gap used by a dimension style
**`DimStyleTextHeight(dimstyle, height=None)`** - Returns or changes the text height used by a dimension style
**`DimensionStyle(object_id, dimstyle_name=None)`** - Returns or modifies the dimension style of a dimension object
**`DimensionText(object_id)`** - Returns the text displayed by a dimension object
**`DimensionUserText(object_id, usertext=None)`** - Returns of modifies the user text string of a dimension object. The user text is the string that ...
**`DimensionValue(object_id)`** - Returns the value of a dimension object
**`IsAlignedDimension(object_id)`** - Verifies an object is an aligned dimension object
**`IsAngularDimension(object_id)`** - Verifies an object is an angular dimension object
**`IsDiameterDimension(object_id)`** - Verifies an object is a diameter dimension object
**`IsDimStyle(dimstyle)`** - Verifies the existance of a dimension style in the document
**`IsDimStyleReference(dimstyle)`** - Verifies that an existing dimension style is from a reference file
**`IsDimension(object_id)`** - Verifies an object is a dimension object
**`IsLeader(object_id)`** - Verifies an object is a dimension leader object
**`IsLinearDimension(object_id)`** - Verifies an object is a linear dimension object
**`IsOrdinateDimension(object_id)`** - Verifies an object is an ordinate dimension object
**`IsRadialDimension(object_id)`** - Verifies an object is a radial dimension object
**`LeaderText(object_id, text=None)`** - Returns or modifies the text string of a dimension leader object
**`RenameDimStyle(oldstyle, newstyle)`** - Renames an existing dimension style

---

## Document

### Currently Used

#### `Redraw()`
**Redraws all views**
*Returns:* None

#### `UnitSystemName(capitalize=False, singular=True, abbreviate=False, model_units=True)`
**Returns the name of the current unit system**
*Returns:* str: The name of the current units system if successful.

### Available Functions

**`CreatePreviewImage(filename, view=None, size=None, flags=0, wireframe=False)`** - Create a bitmap preview image of the current model
**`DocumentModified(modified=None)`** - Returns or sets the document's modified flag. This flag indicates whether or not any changes to t...
**`DocumentName()`** - Returns the name of the currently loaded Rhino document (3DM file)
**`DocumentPath()`** - Returns path of the currently loaded Rhino document (3DM file)
**`EnableRedraw(enable=True)`** - Enables or disables screen redrawing
**`ExtractPreviewImage(filename, modelname=None)`** - Extracts the bitmap preview image from the specified model (.3dm)
**`IsDocumentModified()`** - Verifies that the current document has been modified in some way
**`Notes(newnotes=None)`** - Returns or sets the document's notes. Notes are generally created using Rhino's Notes command
**`ReadFileVersion()`** - Returns the file version of the current document. Use this function to determine which version of...
**`RenderAntialias(style=None)`** - Returns or sets render antialiasing style
**`RenderColor(item, color=None)`** - Returns or sets the render ambient light or background color
**`RenderMeshDensity(density=None)`** - Returns or sets the render mesh density property of the active document. For more information on ...
**`RenderMeshMaxAngle(angle_degrees=None)`** - Returns or sets the render mesh maximum angle property of the active document. For more informati...
**`RenderMeshMaxAspectRatio(ratio=None)`** - Returns or sets the render mesh maximum aspect ratio property of the active document. For more in...
**`RenderMeshMaxDistEdgeToSrf(distance=None)`** - Returns or sets the render mesh maximum distance, edge to surface parameter of the active documen...
**`RenderMeshMaxEdgeLength(distance=None)`** - Returns or sets the render mesh maximum edge length parameter of the active document. For more in...
**`RenderMeshMinEdgeLength(distance=None)`** - Returns or sets the render mesh minimum edge length parameter of the active document. For more in...
**`RenderMeshMinInitialGridQuads(quads=None)`** - Returns or sets the render mesh minimum initial grid quads parameter of the active document. For ...
**`RenderMeshQuality(quality=None)`** - Returns or sets the render mesh quality of the active document. For more information on render me...
**`RenderMeshSettings(settings=None)`** - Returns or sets the render mesh settings of the active document. For more information on render m...
**`RenderResolution(resolution=None)`** - Returns or sets the render resolution
**`RenderSettings(settings=None)`** - Returns or sets render settings
**`UnitAbsoluteTolerance(tolerance=None, in_model_units=True)`** - Resturns or sets the document's absolute tolerance. Absolute tolerance is measured in drawing uni...
**`UnitAngleTolerance(angle_tolerance_degrees=None, in_model_units=True)`** - Return or set the document's angle tolerance. Angle tolerance is measured in degrees. See Rhino's...
**`UnitDistanceDisplayPrecision(precision=None, model_units=True)`** - Return or set the document's distance display precision
**`UnitRelativeTolerance(relative_tolerance=None, in_model_units=True)`** - Return or set the document's relative tolerance. Relative tolerance is measured in percent. See R...
**`UnitScale(to_system, from_system=None)`** - Return the scale factor for changing between unit systems.
**`UnitSystem(unit_system=None, scale=False, in_model_units=True)`** - Return or set the document's unit system. See Rhino's DocumentProperties command (Units and Page ...

---

## Geometry

### Currently Used

#### `AddPoint(point, y=None, z=None)`
**Adds point object to the document.**
*Returns:* guid: identifier for the object that was added to the doc

#### `BoundingBox(objects, view_or_plane=None, in_world_coords=True)`
**Returns either world axis-aligned or a construction plane axis-aligned bounding box of an object or of several objects**
*Returns:* list(point, point, point, point, point, point, point, point): Eight 3D points that define the bounding box. Points returned in counter-clockwise order starting with the bottom rectangle of the box. None: on error

### Available Functions

**`AddClippingPlane(plane, u_magnitude, v_magnitude, views=None)`** - Create a clipping plane for visibly clipping away geometry in a specific view. Note, clipping pla...
**`AddPictureFrame(plane, filename, width=0.0, height=0.0, self_illumination=True, embed=False, use_alpha=False, make_mesh=False)`** - Creates a picture frame and adds it to the document.
**`AddPointCloud(points, colors=None)`** - Adds point cloud object to the document
**`AddPoints(points)`** - Adds one or more point objects to the document
**`AddText(text, point_or_plane, height=1.0, font=None, font_style=0, justification=None)`** - Adds a text string to the document
**`AddTextDot(text, point)`** - Add a text dot to the document.
**`Area(object_id)`** - Compute the area of a closed curve, hatch, surface, polysurface, or mesh
**`CompareGeometry(first, second)`** - Compares two objects to determine if they are geometrically identical.
**`ExplodeText(text_id, delete=False)`** - Creates outline curves for a given text entity
**`IsClippingPlane(object_id)`** - Verifies that an object is a clipping plane object
**`IsPoint(object_id)`** - Verifies an object is a point object.
**`IsPointCloud(object_id)`** - Verifies an object is a point cloud object.
**`IsText(object_id)`** - Verifies an object is a text object.
**`IsTextDot(object_id)`** - Verifies an object is a text dot object.
**`PointCloudClosestPoints(pt_cloud, needle_points, distance)`** - Returns a list of lists of point indices in a point cloud that are closest to needle_points. Each...
**`PointCloudCount(object_id)`** - Returns the point count of a point cloud object
**`PointCloudHasHiddenPoints(object_id)`** - Verifies that a point cloud has hidden points
**`PointCloudHasPointColors(object_id)`** - Verifies that a point cloud has point colors
**`PointCloudHidePoints(object_id, hidden=[])`** - Returns or modifies the hidden points of a point cloud object
**`PointCloudKNeighbors(pt_cloud, needle_points, amount=1)`** - Returns amount indices of points in a point cloud that are near needle_points.
**`PointCloudPointColors(object_id, colors=[])`** - Returns or modifies the point colors of a point cloud object
**`PointCloudPoints(object_id)`** - Returns the points of a point cloud object
**`PointCoordinates(object_id, point=None)`** - Returns or modifies the X, Y, and Z coordinates of a point object
**`TextDotFont(object_id, fontface=None)`** - Returns or modified the font of a text dot
**`TextDotHeight(object_id, height=None)`** - Returns or modified the font height of a text dot
**`TextDotPoint(object_id, point=None)`** - Returns or modifies the location, or insertion point, on a text dot object
**`TextDotText(object_id, text=None)`** - Returns or modifies the text on a text dot object
**`TextObjectFont(object_id, font=None)`** - Returns of modifies the font used by a text object
**`TextObjectHeight(object_id, height=None)`** - Returns or modifies the height of a text object
**`TextObjectPlane(object_id, plane=None)`** - Returns or modifies the plane used by a text object
**`TextObjectPoint(object_id, point=None)`** - Returns or modifies the location of a text object
**`TextObjectStyle(object_id, style=None)`** - Returns or modifies the font style of a text object
**`TextObjectText(object_id, text=None)`** - Returns or modifies the text string of a text object.

---

## Grips

### Available Functions

**`EnableObjectGrips(object_id, enable=True)`** - Enables or disables an object's grips. For curves and surfaces, these are also called control poi...
**`GetObjectGrip(message=None, preselect=False, select=False)`** - Prompts the user to pick a single object grip
**`GetObjectGrips(message=None, preselect=False, select=False)`** - Prompts user to pick one or more object grips from one or more objects.
**`NextObjectGrip(object_id, index, direction=0, enable=True)`** - Returns the next grip index from a specified grip index of an object
**`ObjectGripCount(object_id)`** - Returns number of grips owned by an object
**`ObjectGripLocation(object_id, index, point=None)`** - Returns or modifies the location of an object's grip
**`ObjectGripLocations(object_id, points=None)`** - Returns or modifies the location of all grips owned by an object. The locations of the grips are ...
**`ObjectGripsOn(object_id)`** - Verifies that an object's grips are turned on
**`ObjectGripsSelected(object_id)`** - Verifies that an object's grips are turned on and at least one grip is selected
**`PrevObjectGrip(object_id, index, direction=0, enable=True)`** - Returns the previous grip index from a specified grip index of an object
**`SelectObjectGrip(object_id, index)`** - Selects a single grip owned by an object. If the object's grips are not turned on, the grips will...
**`SelectObjectGrips(object_id)`** - Selects an object's grips. If the object's grips are not turned on, they will not be selected
**`SelectedObjectGrips(object_id)`** - Returns a list of grip indices indentifying an object's selected grips
**`UnselectObjectGrip(object_id, index)`** - Unselects a single grip owned by an object. If the object's grips are not turned on, the grips wi...
**`UnselectObjectGrips(object_id)`** - Unselects an object's grips. Note, the grips will not be turned off.

---

## Group

### Available Functions

**`AddGroup(group_name=None)`** - Adds a new empty group to the document
**`AddObjectToGroup(object_id, group_name)`** - Adds a single object to an existing group.
**`AddObjectsToGroup(object_ids, group_name)`** - Adds one or more objects to an existing group.
**`DeleteGroup(group_name)`** - Removes an existing group from the document. Reference groups cannot be removed. Deleting a group...
**`GroupCount()`** - Returns the number of groups in the document
**`GroupNames()`** - Returns the names of all the groups in the document None if no names exist in the document
**`HideGroup(group_name)`** - Hides a group of objects. Hidden objects are not visible, cannot be snapped to, and cannot be sel...
**`IsGroup(group_name)`** - Verifies the existance of a group
**`IsGroupEmpty(group_name)`** - Verifies that an existing group is empty, or contains no object members
**`LockGroup(group_name)`** - Locks a group of objects. Locked objects are visible and they can be snapped to. But, they cannot...
**`ObjectTopGroup(object_id)`** - Returns the top most group name that an object is assigned. This function primarily applies to ob...
**`RemoveObjectFromAllGroups(object_id)`** - Removes a single object from any and all groups that it is a member. Neither the object nor the g...
**`RemoveObjectFromGroup(object_id, group_name)`** - Remove a single object from an existing group
**`RemoveObjectsFromGroup(object_ids, group_name)`** - Removes one or more objects from an existing group
**`RenameGroup(old_name, new_name)`** - Renames an existing group
**`ShowGroup(group_name)`** - Shows a group of previously hidden objects. Hidden objects are not visible, cannot be snapped to,...
**`UnlockGroup(group_name)`** - Unlocks a group of previously locked objects. Lockes objects are visible, can be snapped to, but ...

---

## Hatch

**`AddHatch(curve_id, hatch_pattern=None, scale=1.0, rotation=0.0)`** - Creates a new hatch object from a closed planar curve object
**`AddHatchPatterns(filename, replace=False)`** - Adds hatch patterns to the document by importing hatch pattern definitions from a pattern file.
**`AddHatches(curve_ids, hatch_pattern=None, scale=1.0, rotation=0.0, tolerance=None)`** - Creates one or more new hatch objects a list of closed planar curves
**`CurrentHatchPattern(hatch_pattern=None)`** - Returns or sets the current hatch pattern file
**`ExplodeHatch(hatch_id, delete=False)`** - Explodes a hatch object into its component objects. The exploded objects will be added to the doc...
**`HatchPattern(hatch_id, hatch_pattern=None)`** - Returns or changes a hatch object's hatch pattern
**`HatchPatternCount()`** - Returns the number of hatch patterns in the document
**`HatchPatternDescription(hatch_pattern)`** - Returns the description of a hatch pattern. Note, not all hatch patterns have descriptions
**`HatchPatternFillType(hatch_pattern)`** - Returns the fill type of a hatch pattern.
**`HatchPatternNames()`** - Returns the names of all of the hatch patterns in the document
**`HatchRotation(hatch_id, rotation=None)`** - Returns or modifies the rotation applied to the hatch pattern when it is mapped to the hatch's plane
**`HatchScale(hatch_id, scale=None)`** - Returns or modifies the scale applied to the hatch pattern when it is mapped to the hatch's plane
**`IsHatch(object_id)`** - Verifies the existence of a hatch object in the document
**`IsHatchPattern(name)`** - Verifies the existence of a hatch pattern in the document
**`IsHatchPatternCurrent(hatch_pattern)`** - Verifies that a hatch pattern is the current hatch pattern
**`IsHatchPatternReference(hatch_pattern)`** - Verifies that a hatch pattern is from a reference file

---

## Layer

#### `AddLayer(name=None, color=None, visible=True, locked=False, parent=None)`
**Add a new layer to the document**
*Returns:* str: The full name of the new layer if successful.

#### `CurrentLayer(layer=None)`
**Returns or changes the current layer**
*Returns:* str: If a layer name is not specified, the full name of the current layer str: If a layer name is specified, the full name of the previous current layer

#### `DeleteLayer(layer)`
**Removes an existing layer from the document. The layer to be removed cannot be the current layer. Unlike the PurgeLayer method, the layer must be empty, or contain no objects, before it can be removed. Any layers that are children of the specified layer will also be removed if they are also empty.**
*Returns:* bool: True or False indicating success or failure

#### `IsLayer(layer)`
**Verifies the existance of a layer in the document**
*Returns:* bool: True on success otherwise False

#### `LayerColor(layer, color=None)`
**Returns or changes the color of a layer.**
*Returns:* color: If a color value is not specified, the current color value on success color: If a color value is specified, the previous color value on success

#### `LayerLocked(layer, locked=None)`
**Returns or changes the locked mode of a layer**
*Returns:* bool: If locked is not specified, the current layer locked mode bool: If locked is specified, the previous layer locked mode

#### `LayerNames(sort=False)`
**Returns the names of all layers in the document.**
*Returns:* list(str, ...): list of layer names

#### `LayerVisible(layer, visible=None, forcevisible_or_donotpersist=False)`
**Returns or changes the visible property of a layer.**
*Returns:* bool: if visible is not specified, the current layer visibility bool: if visible is specified, the previous layer visibility

### Available Functions

**`ExpandLayer( layer, expand )`** - Expands a layer. Expanded layers can be viewed in Rhino's layer dialog
**`IsLayerChangeable(layer)`** - Verifies that the objects on a layer can be changed (normal)
**`IsLayerChildOf(layer, test)`** - Verifies that a layer is a child of another layer
**`IsLayerCurrent(layer)`** - Verifies that a layer is the current layer
**`IsLayerEmpty(layer)`** - Verifies that an existing layer is empty, or contains no objects
**`IsLayerExpanded(layer)`** - Verifies that a layer is expanded. Expanded layers can be viewed in Rhino's layer dialog
**`IsLayerOn(layer)`** - Verifies that a layer is on.
**`IsLayerParentOf(layer, test)`** - Verifies that a layer is a parent of another layer
**`IsLayerReference(layer)`** - Verifies that a layer is from a reference file.
**`IsLayerSelectable(layer)`** - Verifies that an existing layer is selectable (normal and reference)
**`IsLayerVisible(layer)`** - Verifies that a layer is visible (normal, locked, and reference)
**`LayerChildCount(layer)`** - Returns the number of immediate child layers of a layer
**`LayerChildren(layer)`** - Returns the immediate child layers of a layer
**`LayerCount()`** - Returns the number of layers in the document
**`LayerId(layer)`** - Returns the identifier of a layer given the layer's name.
**`LayerIds()`** - Return identifiers of all layers in the document
**`LayerLinetype(layer, linetype=None)`** - Returns or changes the linetype of a layer
**`LayerMaterialIndex(layer,index=None)`** - Returns or changes the material index of a layer. A material index of -1 indicates that no materi...
**`LayerName(layer_id, fullpath=True)`** - Return the name of a layer given it's identifier
**`LayerOrder(layer)`** - Returns the current display order index of a layer as displayed in Rhino's layer dialog box. A di...
**`LayerPrintColor(layer, color=None)`** - Returns or changes the print color of a layer. Layer print colors are represented as RGB colors.
**`LayerPrintWidth(layer, width=None)`** - Returns or changes the print width of a layer. Print width is specified in millimeters. A print w...
**`ParentLayer(layer, parent=None)`** - Return or modify the parent layer of a layer
**`PurgeLayer(layer)`** - Removes an existing layer from the document. The layer will be removed even if it contains geomet...
**`RenameLayer(oldname, newname)`** - Renames an existing layer

---

## Light

**`AddDirectionalLight(start_point, end_point)`** - Adds a new directional light object to the document
**`AddLinearLight(start_point, end_point, width=None)`** - Adds a new linear light object to the document
**`AddPointLight(point)`** - Adds a new point light object to the document
**`AddRectangularLight(origin, width_point, height_point)`** - Adds a new rectangular light object to the document
**`AddSpotLight(origin, radius, apex_point)`** - Adds a new spot light object to the document
**`EnableLight(object_id, enable=None)`** - Enables or disables a light object
**`IsDirectionalLight(object_id)`** - Verifies a light object is a directional light
**`IsLight(object_id)`** - Verifies an object is a light object
**`IsLightEnabled(object_id)`** - Verifies a light object is enabled
**`IsLightReference(object_id)`** - Verifies a light object is referenced from another file
**`IsLinearLight(object_id)`** - Verifies a light object is a linear light
**`IsPointLight(object_id)`** - Verifies a light object is a point light
**`IsRectangularLight(object_id)`** - Verifies a light object is a rectangular light
**`IsSpotLight(object_id)`** - Verifies a light object is a spot light
**`LightColor(object_id, color=None)`** - Returns or changes the color of a light
**`LightCount()`** - Returns the number of light objects in the document
**`LightDirection(object_id, direction=None)`** - Returns or changes the direction of a light object
**`LightLocation(object_id, location=None)`** - Returns or changes the location of a light object
**`LightName(object_id, name=None)`** - Returns or changes the name of a light object
**`LightObjects()`** - Returns list of identifiers of light objects in the document
**`RectangularLightPlane(object_id)`** - Returns the plane of a rectangular light object
**`SpotLightHardness(object_id, hardness=None)`** - Returns or changes the hardness of a spot light. Spotlight hardness controls the fully illuminate...
**`SpotLightRadius(object_id, radius=None)`** - Returns or changes the radius of a spot light.
**`SpotLightShadowIntensity(object_id, intensity=None)`** - Returns or changes the shadow intensity of a spot light.

---

## Line

### Available Functions

**`LineClosestPoint(line, testpoint)`** - Finds the point on an infinite line that is closest to a test point
**`LineCylinderIntersection(line, cylinder_plane, cylinder_height, cylinder_radius)`** - Calculates the intersection of a line and a cylinder
**`LineIsFartherThan(line, distance, point_or_line)`** - Determines if the shortest distance from a line to a point or another line is greater than a spec...
**`LineLineIntersection(lineA, lineB)`** - Calculates the intersection of two non-parallel lines. Note, the two lines do not have to interse...
**`LineMaxDistanceTo(line, point_or_line)`** - Finds the longest distance between a line as a finite chord, and a point or another line
**`LineMinDistanceTo(line, point_or_line)`** - Finds the shortest distance between a line as a finite chord, and a point or another line
**`LinePlane(line)`** - Returns a plane that contains the line. The origin of the plane is at the start of the line. If p...
**`LinePlaneIntersection(line, plane)`** - Calculates the intersection of a line and a plane.
**`LineSphereIntersection(line, sphere_center, sphere_radius)`** - Calculates the intersection of a line and a sphere
**`LineTransform(line, xform)`** - Transforms a line

---

## Linetype

**`IsLinetype(name_or_id)`** - Verifies the existance of a linetype in the document
**`IsLinetypeReference(name_or_id)`** - Verifies that an existing linetype is from a reference file
**`LinetypeCount()`** - Returns number of linetypes in the document
**`LinetypeNames(sort=False)`** - Returns names of all linetypes in the document

---

## Material

**`AddMaterialToLayer(layer)`** - Add material to a layer and returns the new material's index. If the layer already has a material...
**`AddMaterialToObject(object_id)`** - Adds material to an object and returns the new material's index. If the object already has a mate...
**`CopyMaterial(source_index, destination_index)`** - Copies definition of a source material to a destination material
**`IsMaterialDefault(material_index)`** - Verifies a material is a copy of Rhino's built-in "default" material. The default material is use...
**`IsMaterialReference(material_index)`** - Verifies a material is referenced from another file
**`MatchMaterial(source, destination)`** - Copies the material definition from one material to one or more objects
**`MaterialBump(material_index, filename=None)`** - Returns or modifies a material's bump bitmap filename
**`MaterialColor(material_index, color=None)`** - Returns or modifies a material's diffuse color.
**`MaterialEnvironmentMap(material_index, filename=None)`** - Returns or modifies a material's environment bitmap filename.
**`MaterialName(material_index, name=None)`** - Returns or modifies a material's user defined name
**`MaterialReflectiveColor(material_index, color=None)`** - Returns or modifies a material's reflective color.
**`MaterialShine(material_index, shine=None)`** - Returns or modifies a material's shine value
**`MaterialTexture(material_index, filename=None)`** - Returns or modifies a material's texture bitmap filename
**`MaterialTransparency(material_index, transparency=None)`** - Returns or modifies a material's transparency value
**`MaterialTransparencyMap(material_index, filename=None)`** - Returns or modifies a material's transparency bitmap filename
**`ResetMaterial(material_index)`** - Resets a material to Rhino's default material

---

## Mesh

**`AddMesh(vertices, face_vertices, vertex_normals=None, texture_coordinates=None, vertex_colors=None)`** - Add a mesh object to the document
**`AddPlanarMesh(object_id, delete_input=False)`** - Creates a planar mesh from a closed, planar curve
**`CurveMeshIntersection(curve_id, mesh_id, return_faces=False)`** - Calculates the intersection of a curve object and a mesh object
**`DisjointMeshCount(object_id)`** - Returns number of meshes that could be created by calling SplitDisjointMesh
**`DuplicateMeshBorder(mesh_id)`** - Creates curves that duplicates a mesh border
**`ExplodeMeshes(mesh_ids, delete=False)`** - Explodes a mesh object, or mesh objects int submeshes. A submesh is a collection of mesh faces th...
**`IsMesh(object_id)`** - Verifies if an object is a mesh
**`IsMeshClosed(object_id)`** - Verifies a mesh object is closed
**`IsMeshManifold(object_id)`** - Verifies a mesh object is manifold. A mesh for which every edge is shared by at most two faces is...
**`IsPointOnMesh(object_id, point)`** - Verifies a point is on a mesh
**`JoinMeshes(object_ids, delete_input=False)`** - Joins two or or more mesh objects together
**`MeshArea(object_ids)`** - Returns approximate area of one or more mesh objects
**`MeshAreaCentroid(object_id)`** - Calculates the area centroid of a mesh object
**`MeshBooleanDifference(input0, input1, delete_input=True, tolerance=None)`** - Performs boolean difference operation on two sets of input meshes
**`MeshBooleanIntersection(input0, input1, delete_input=True)`** - Performs boolean intersection operation on two sets of input meshes
**`MeshBooleanSplit(input0, input1, delete_input=True)`** - Performs boolean split operation on two sets of input meshes
**`MeshBooleanUnion(mesh_ids, delete_input=True)`** - Performs boolean union operation on a set of input meshes
**`MeshClosestPoint(object_id, point, maximum_distance=None)`** - Returns the point on a mesh that is closest to a test point
**`MeshFaceCenters(mesh_id)`** - Returns the center of each face of the mesh object
**`MeshFaceCount(object_id)`** - Returns total face count of a mesh object
**`MeshFaceNormals(mesh_id)`** - Returns the face unit normal for each face of a mesh object
**`MeshFaceVertices(object_id)`** - Returns the vertex indices of all faces of a mesh object
**`MeshFaces(object_id, face_type=True)`** - Returns face vertices of a mesh
**`MeshHasFaceNormals(object_id)`** - Verifies a mesh object has face normals
**`MeshHasTextureCoordinates(object_id)`** - Verifies a mesh object has texture coordinates
**`MeshHasVertexColors(object_id)`** - Verifies a mesh object has vertex colors
**`MeshHasVertexNormals(object_id)`** - Verifies a mesh object has vertex normals
**`MeshMeshIntersection(mesh1, mesh2, tolerance=None)`** - Calculates the intersections of a mesh object with another mesh object
**`MeshNakedEdgePoints(object_id)`** - Identifies the naked edge points of a mesh object. This function shows where mesh vertices are no...
**`MeshOffset(mesh_id, distance)`** - Makes a new mesh with vertices offset at a distance in the opposite direction of the existing ver...
**`MeshOutline(object_ids, view=None)`** - Creates polyline curve outlines of mesh objects
**`MeshQuadCount(object_id)`** - Returns the number of quad faces of a mesh object
**`MeshQuadsToTriangles(object_id)`** - Converts a mesh object's quad faces to triangles
**`MeshToNurb(object_id, trimmed_triangles=True, delete_input=False)`** - Duplicates each polygon in a mesh with a NURBS surface. The resulting surfaces are then joined in...
**`MeshTriangleCount(object_id)`** - Returns number of triangular faces of a mesh
**`MeshVertexColors(mesh_id, colors=0)`** - Returns of modifies vertex colors of a mesh
**`MeshVertexCount(object_id)`** - Returns the vertex count of a mesh
**`MeshVertexFaces(mesh_id, vertex_index)`** - Returns the mesh faces that share a specified mesh vertex
**`MeshVertexNormals(mesh_id)`** - Returns the vertex unit normal for each vertex of a mesh
**`MeshVertices(object_id)`** - Returns the vertices of a mesh
**`MeshVolume(object_ids)`** - Returns the approximate volume of one or more closed meshes
**`MeshVolumeCentroid(object_id)`** - Calculates the volume centroid of a mesh
**`PullCurveToMesh(mesh_id, curve_id)`** - Pulls a curve to a mesh. The function makes a polyline approximation of the input curve and gets ...
**`SplitDisjointMesh(object_id, delete_input=False)`** - Splits up a mesh into its unconnected pieces
**`UnifyMeshNormals(object_id)`** - Fixes inconsistencies in the directions of faces of a mesh

---

## Object

#### `CopyObject(object_id, translation=None)`
**Copies object from one location to another, or in-place.**
*Returns:* guid: id for the copy if successful None: if not able to copy

#### `DeleteObject(object_id)`
**Deletes a single object from the document**
*Returns:* bool: True of False indicating success or failure

#### `DeleteObjects(object_ids)`
**Deletes one or more objects from the document**
*Returns:* number: Number of objects deleted

#### `MirrorObject(object_id, start_point, end_point, copy=False)`
**Mirrors a single object**
*Returns:* guid: Identifier of the mirrored object if successful None: on error

#### `MoveObject(object_id, translation)`
**Moves a single object**
*Returns:* guid: Identifier of the moved object if successful None: on error

#### `ObjectColor(object_ids, color=None)`
**Returns of modifies the color of an object. Object colors are represented as RGB colors. An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed**
*Returns:* color: If color value is not specified, the current color value color: If color value is specified, the previous color value number: If object_ids is a list, then the number of objects modified

#### `ObjectLayer(object_id, layer=None)`
**Returns or modifies the layer of an object**
*Returns:* str: If a layer is not specified, the object's current layer str: If a layer is specified, the object's previous layer number: If object_id is a list or tuple, the number of objects modified

#### `ObjectName(object_id, name=None)`
**Returns or modifies the name of an object**
*Returns:* str: If name is not specified, the current object name str: If name is specified, the previous object name number: If object_id is a list, the number of objects changed

#### `ObjectType(object_id)`
**Returns the object type**
*Returns:* number: The object type if successful. The valid object types are as follows: Value Description 0 Unknown object 1 Point 2 Point cloud 4 Curve 8 Surface or single-face brep 16 Polysurface or multiple-face 32 Mesh 256 Light 512 Annotation 4096 Instance or block reference 8192 Text dot object 16384 Grip object 32768 Detail 65536 Hatch 131072 Morph control 134217728 Cage 268435456 Phantom 536870912 Clipping plane 1073741824 Extrusion

#### `RotateObjects( object_ids, center_point, rotation_angle, axis=None, copy=False)`
**Rotates multiple objects**
*Returns:* list(guid, ...): identifiers of the rotated objects if successful

#### `ScaleObject(object_id, origin, scale, copy=False)`
**Scales a single object. Can be used to perform a uniform or non-uniform scale transformation. Scaling is based on the active construction plane.**
*Returns:* guid: Identifier of the scaled object if successful None: on error

#### `SelectObjects( object_ids)`
**Selects one or more objects**
*Returns:* number: number of selected objects

**`CopyObjects(object_ids, translation=None)`** - Copies one or more objects from one location to another, or in-place.
**`FlashObject(object_ids, style=True)`** - Causes the selection state of one or more objects to change momentarily so the object appears to ...
**`HideObject(object_id)`** - Hides a single object
**`HideObjects(object_ids)`** - Hides one or more objects
**`IsLayoutObject(object_id)`** - Verifies that an object is in either page layout space or model space
**`IsObject(object_id)`** - Verifies the existence of an object
**`IsObjectHidden(object_id)`** - Verifies that an object is hidden. Hidden objects are not visible, cannot be snapped to, and cann...
**`IsObjectInBox(object_id, box, test_mode=True)`** - Verifies an object's bounding box is inside of another bounding box
**`IsObjectInGroup(object_id, group_name=None)`** - Verifies that an object is a member of a group
**`IsObjectLocked(object_id)`** - Verifies that an object is locked. Locked objects are visible, and can be snapped to, but cannot ...
**`IsObjectNormal(object_id)`** - Verifies that an object is normal. Normal objects are visible, can be snapped to, and can be sele...
**`IsObjectReference(object_id)`** - Verifies that an object is a reference object. Reference objects are objects that are not part of...
**`IsObjectSelectable(object_id)`** - Verifies that an object can be selected
**`IsObjectSelected(object_id)`** - Verifies that an object is currently selected.
**`IsObjectSolid(object_id)`** - Determines if an object is closed, solid
**`IsObjectValid(object_id)`** - Verifies an object's geometry is valid and without error
**`IsVisibleInView(object_id, view=None)`** - Verifies an object is visible in a view
**`LockObject(object_id)`** - Locks a single object. Locked objects are visible, and they can be snapped to. But, they cannot b...
**`LockObjects(object_ids)`** - Locks one or more objects. Locked objects are visible, and they can be snapped to. But, they cann...
**`MatchObjectAttributes(target_ids, source_id=None)`** - Matches, or copies the attributes of a source object to a target object
**`MirrorObjects(object_ids, start_point, end_point, copy=False)`** - Mirrors a list of objects
**`MoveObjects(object_ids, translation)`** - Moves one or more objects
**`ObjectColorSource(object_ids, source=None)`** - Returns of modifies the color source of an object.
**`ObjectDescription(object_id)`** - Returns a short text description of an object
**`ObjectGroups(object_id)`** - Returns all of the group names that an object is assigned to
**`ObjectLayout(object_id, layout=None, return_name=True)`** - Returns or changes the layout or model space of an object
**`ObjectLinetype(object_ids, linetype=None)`** - Returns of modifies the linetype of an object
**`ObjectLinetypeSource(object_ids, source=None)`** - Returns of modifies the linetype source of an object
**`ObjectMaterialIndex(object_id, material_index=None)`** - Returns or changes the material index of an object. Rendering materials are stored in Rhino's ren...
**`ObjectMaterialSource(object_ids, source=None)`** - Returns or modifies the rendering material source of an object.
**`ObjectPrintColor(object_ids, color=None)`** - Returns or modifies the print color of an object
**`ObjectPrintColorSource(object_ids, source=None)`** - Returns or modifies the print color source of an object
**`ObjectPrintWidth(object_ids, width=None)`** - Returns or modifies the print width of an object
**`ObjectPrintWidthSource(object_ids, source=None)`** - Returns or modifies the print width source of an object
**`OrientObject(object_id, reference, target, flags=0)`** - Orients a single object based on input points. If two 3-D points are specified, then this method ...
**`RotateObject(object_id, center_point, rotation_angle, axis=None, copy=False)`** - Rotates a single object
**`ScaleObjects(object_ids, origin, scale, copy=False)`** - Scales one or more objects. Can be used to perform a uniform or non- uniform scale transformation...
**`SelectObject(object_id, redraw=True)`** - Selects a single object
**`ShearObject(object_id, origin, reference_point, angle_degrees, copy=False)`** - Perform a shear transformation on a single object
**`ShearObjects(object_ids, origin, reference_point, angle_degrees, copy=False)`** - Shears one or more objects
**`ShowObject(object_id)`** - Shows a previously hidden object. Hidden objects are not visible, cannot be snapped to and cannot...
**`ShowObjects(object_ids)`** - Shows one or more objects. Hidden objects are not visible, cannot be snapped to and cannot be sel...
**`TransformObject(object_id, matrix, copy=False)`** - Moves, scales, or rotates an object given a 4x4 transformation matrix. The matrix acts on the left.
**`TransformObjects(object_ids, matrix, copy=False)`** - Moves, scales, or rotates a list of objects given a 4x4 transformation matrix. The matrix acts on...
**`UnlockObject(object_id)`** - Unlocks an object. Locked objects are visible, and can be snapped to, but they cannot be selected.
**`UnlockObjects(object_ids)`** - Unlocks one or more objects. Locked objects are visible, and can be snapped to, but they cannot b...
**`UnselectObject(object_id)`** - Unselects a single selected object
**`UnselectObjects(object_ids)`** - Unselects one or more selected objects.

---

## Plane

#### `PlaneFromNormal(origin, normal, xaxis=None)`
**Creates a plane from an origin point and a normal direction vector.**
*Returns:* plane: The plane if successful.
**`DistanceToPlane(plane, point)`** - Returns the distance from a 3D point to a plane
**`EvaluatePlane(plane, parameter)`** - Evaluates a plane at a U,V parameter
**`IntersectPlanes(plane1, plane2, plane3)`** - Calculates the intersection of three planes
**`MovePlane(plane, origin)`** - Moves the origin of a plane
**`PlaneClosestPoint(plane, point, return_point=True)`** - Returns the point on a plane that is closest to a test point.
**`PlaneCurveIntersection(plane, curve, tolerance=None)`** - Intersect an infinite plane and a curve object
**`PlaneEquation(plane)`** - Returns the equation of a plane as a tuple of four numbers. The standard equation of a plane with...
**`PlaneFitFromPoints(points)`** - Returns a plane that was fit through an array of 3D points.
**`PlaneFromFrame(origin, x_axis, y_axis)`** - Construct a plane from a point, and two vectors in the plane.
**`PlaneFromPoints(origin, x, y)`** - Creates a plane from three non-colinear points
**`PlanePlaneIntersection(plane1, plane2)`** - Calculates the intersection of two planes
**`PlaneSphereIntersection(plane, sphere_plane, sphere_radius)`** - Calculates the intersection of a plane and a sphere
**`PlaneTransform(plane, xform)`** - Transforms a plane
**`RotatePlane(plane, angle_degrees, axis)`** - Rotates a plane
**`WorldXYPlane()`** - Returns Rhino's world XY plane
**`WorldYZPlane()`** - Returns Rhino's world YZ plane
**`WorldZXPlane()`** - Returns Rhino's world ZX plane

---

## Pointvector

**`IsVectorParallelTo(vector1, vector2)`** - Compares two vectors to see if they are parallel
**`IsVectorPerpendicularTo(vector1, vector2)`** - Compares two vectors to see if they are perpendicular
**`IsVectorTiny(vector)`** - Verifies that a vector is very short. The X,Y,Z elements are <= 1.0e-12
**`IsVectorZero(vector)`** - Verifies that a vector is zero, or tiny. The X,Y,Z elements are equal to 0.0
**`PointAdd(point1, point2)`** - Adds a 3D point or a 3D vector to a 3D point
**`PointArrayBoundingBox(points, view_or_plane=None, in_world_coords=True)`** - Returns either a world axis-aligned or a construction plane axis-aligned bounding box of an array...
**`PointArrayClosestPoint(points, test_point)`** - Finds the point in a list of 3D points that is closest to a test point
**`PointArrayTransform(points, xform)`** - Transforms a list of 3D points
**`PointClosestObject(point, object_ids)`** - Finds the object that is closest to a test point
**`PointCompare(point1, point2, tolerance=None)`** - Compares two 3D points
**`PointDivide(point, divide)`** - Divides a 3D point by a value
**`PointScale(point, scale)`** - Scales a 3D point by a value
**`PointSubtract(point1, point2)`** - Subtracts a 3D point or a 3D vector from a 3D point
**`PointTransform(point, xform)`** - Transforms a 3D point
**`PointsAreCoplanar(points, tolerance=1.0e-12)`** - Verifies that a list of 3D points are coplanar
**`ProjectPointToMesh(points, mesh_ids, direction)`** - Projects one or more points onto one or more meshes
**`ProjectPointToSurface(points, surface_ids, direction)`** - Projects one or more points onto one or more surfaces or polysurfaces
**`PullPoints(object_id, points)`** - Pulls an array of points to a surface or mesh object. For more information, see the Rhino help fi...
**`VectorAdd(vector1, vector2)`** - Adds two 3D vectors
**`VectorAngle(vector1, vector2)`** - Returns the angle, in degrees, between two 3-D vectors
**`VectorCompare(vector1, vector2)`** - Compares two 3D vectors
**`VectorCreate(to_point, from_point)`** - Creates a vector from two 3D points
**`VectorCrossProduct(vector1, vector2)`** - Calculates the cross product of two 3D vectors
**`VectorDivide(vector, divide)`** - Divides a 3D vector by a value
**`VectorDotProduct(vector1, vector2)`** - Calculates the dot product of two 3D vectors
**`VectorLength(vector)`** - Returns the length of a 3D vector
**`VectorMultiply(vector1, vector2)`** - Multiplies two 3D vectors
**`VectorReverse(vector)`** - Reverses the direction of a 3D vector
**`VectorRotate(vector, angle_degrees, axis)`** - Rotates a 3D vector
**`VectorScale(vector, scale)`** - Scales a 3-D vector
**`VectorSubtract(vector1, vector2)`** - Subtracts two 3D vectors
**`VectorTransform(vector, xform)`** - Transforms a 3D vector
**`VectorUnitize(vector)`** - Unitizes, or normalizes a 3D vector. Note, zero vectors cannot be unitized

---

## Selection

#### `AllObjects(select=False, include_lights=False, include_grips=False, include_references=False)`
**Returns identifiers of all objects in the document.**
*Returns:* list(guid, ...): identifiers for all the objects in the document

#### `ObjectsByLayer(layer_name, select=False)`
**Returns identifiers of all objects based on the objects' layer name**
*Returns:* list(guid, ...): identifiers for objects in the specified layer

#### `ObjectsByType(geometry_type, select=False, state=0)`
**Returns identifiers of all objects based on the objects' geometry type.**
*Returns:* list(guid, ...): identifiers of object that fit the specified type(s).

#### `SelectedObjects(include_lights=False, include_grips=False)`
**Returns the identifiers of all objects that are currently selected**
*Returns:* list(guid, ...) identifiers of selected objects

#### `UnselectAllObjects()`
**Unselects all objects in the document**
*Returns:* number: the number of objects that were unselected

**`FirstObject(select=False, include_lights=False, include_grips=False)`** - Returns identifier of the first object in the document. The first object is the last object creat...
**`GetCurveObject(message=None, preselect=False, select=False)`** - Prompts user to pick or select a single curve object
**`GetObject(message=None, filter=0, preselect=False, select=False, custom_filter=None, subobjects=False)`** - Prompts user to pick, or select, a single object.
**`GetObjectEx(message=None, filter=0, preselect=False, select=False, objects=None)`** - Prompts user to pick, or select a single object
**`GetObjects(message=None, filter=0, group=True, preselect=False, select=False, objects=None, minimum_count=1, maximum_count=0, custom_filter=None)`** - Prompts user to pick or select one or more objects.
**`GetObjectsEx(message=None, filter=0, group=True, preselect=False, select=False, objects=None)`** - Prompts user to pick, or select one or more objects
**`GetPointCoordinates(message="Select points", preselect=False)`** - Prompts the user to select one or more point objects.
**`GetSurfaceObject(message="Select surface", preselect=False, select=False)`** - Prompts the user to select a single surface
**`HiddenObjects(include_lights=False, include_grips=False, include_references=False)`** - Returns identifiers of all hidden objects in the document. Hidden objects are not visible, cannot...
**`InvertSelectedObjects(include_lights=False, include_grips=False, include_references=False)`** - Inverts the current object selection. The identifiers of the newly selected objects are returned
**`LastCreatedObjects(select=False)`** - Returns identifiers of the objects that were most recently created or changed by scripting a Rhin...
**`LastObject(select=False, include_lights=False, include_grips=False)`** - Returns the identifier of the last object in the document. The last object in the document is the...
**`LockedObjects(include_lights=False, include_grips=False, include_references=False)`** - Returns identifiers of all locked objects in the document. Locked objects cannot be snapped to, a...
**`NextObject(object_id, select=False, include_lights=False, include_grips=False)`** - Returns the identifier of the next object in the document
**`NormalObjects(include_lights=False, include_grips=False)`** - Returns identifiers of all normal objects in the document. Normal objects are visible, can be sna...
**`ObjectsByColor(color, select=False, include_lights=False)`** - Returns identifiers of all objects based on color
**`ObjectsByGroup(group_name, select=False)`** - Returns identifiers of all objects based on the objects' group name
**`ObjectsByName(name, select=False, include_lights=False, include_references=False)`** - Returns identifiers of all objects based on user-assigned name
**`VisibleObjects(view=None, select=False, include_lights=False, include_grips=False)`** - Return identifiers of all objects that are visible in a specified view
**`WindowPick(corner1, corner2, view=None, select=False, in_window=True)`** - Picks objects using either a window or crossing selection

---

## Surface

#### `AddBox(corners)`
**Adds a box shaped polysurface to the document**
*Returns:* guid: identifier of the new object on success

#### `AddCone(base, height, radius, cap=True)`
**Adds a cone shaped polysurface to the document**
*Returns:* guid: identifier of the new object on success

#### `AddLoftSrf(object_ids, start=None, end=None, loft_type=0, simplify_method=0, value=0, closed=False)`
**Adds a surface created by lofting curves to the document. - no curve sorting performed. pass in curves in the order you want them sorted - directions of open curves not adjusted. Use CurveDirectionsMatch and ReverseCurve to adjust the directions of open curves - seams of closed curves are not adjusted. Use CurveSeam to adjust the seam of closed curves**
*Returns:* list(guid, ...):Array containing the identifiers of the new surface objects if successful None: on error

#### `AddRevSrf(curve_id, axis, start_angle=0.0, end_angle=360.0)`
**Create a surface by revolving a curve around an axis**
*Returns:* guid: identifier of new object if successful None: on error

#### `AddSphere(center_or_plane, radius)`
**Add a spherical surface to the document**
*Returns:* guid: identifier of the new object on success None: on error

#### `AddTorus(base, major_radius, minor_radius, direction=None)`
**Adds a torus shaped revolved surface to the document**
*Returns:* guid: The identifier of the new object if successful. None: if not successful, or on error.

#### `BooleanDifference(input0, input1, delete_input=True)`
**Performs a boolean difference operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanDifference command in the Rhino help file**
*Returns:* list(guid, ...): of identifiers of newly created objects on success None: on error

#### `BooleanIntersection(input0, input1, delete_input=True)`
**Performs a boolean intersection operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanIntersection command in the Rhino help file**
*Returns:* list(guid, ...): of identifiers of newly created objects on success None: on error

#### `BooleanUnion(input, delete_input=True)`
**Performs a boolean union operation on a set of input surfaces and polysurfaces. For more details, see the BooleanUnion command in the Rhino help file**
*Returns:* list(guid, ...): of identifiers of newly created objects on success None on error

#### `ExtrudeCurveStraight(curve_id, start_point, end_point)`
**Create surface by extruding a curve along two points that define a line**
*Returns:* guid: identifier of new surface on success None: on error

#### `IsPolysurface(object_id)`
**Verifies an object is a polysurface. Polysurfaces consist of two or more surfaces joined together. If the polysurface fully encloses a volume, it is considered a solid.**
*Returns:* bool: True is successful, otherwise False

#### `IsSurface(object_id)`
**Verifies an object is a surface. Brep objects with only one face are also considered surfaces.**
*Returns:* bool: True if successful, otherwise False.

#### `SurfaceArea(object_id)`
**Calculate the area of a surface or polysurface object. The results are based on the current drawing units**
*Returns:* list(number, number): of area information on success (area, absolute error bound) None: on error

#### `SurfaceVolume(object_id)`
**Calculates volume of a closed surface or polysurface**
*Returns:* list(number, tuple(X, Y, Z): volume data returned (Volume, Error bound) on success None: on error

**`AddCutPlane(object_ids, start_point, end_point, normal=None)`** - Adds a planar surface through objects at a designated location. For more information, see the Rhi...
**`AddCylinder(base, height, radius, cap=True)`** - Adds a cylinder-shaped polysurface to the document
**`AddEdgeSrf(curve_ids)`** - Creates a surface from 2, 3, or 4 edge curves
**`AddNetworkSrf(curves, continuity=1, edge_tolerance=0, interior_tolerance=0, angle_tolerance=0)`** - Creates a surface from a network of crossing curves
**`AddNurbsSurface(point_count, points, knots_u, knots_v, degree, weights=None)`** - Adds a NURBS surface object to the document
**`AddPatch(object_ids, uv_spans_tuple_OR_surface_object_id, tolerance=None, trim=True, point_spacing=0.1, flexibility=1.0, surface_pull=1.0, fix_edges=False)`** - Fits a surface through curve, point, point cloud, and mesh objects.
**`AddPipe(curve_id, parameters, radii, blend_type=0, cap=0, fit=False)`** - Creates a single walled surface with a circular profile around a curve
**`AddPlanarSrf(object_ids)`** - Creates one or more surfaces from planar curves
**`AddPlaneSurface(plane, u_dir, v_dir)`** - Create a plane surface and add it to the document.
**`AddRailRevSrf(profile, rail, axis, scale_height=False)`** - Adds a surface created through profile curves that define the surface shape and two curves that d...
**`AddSrfContourCrvs(object_id, points_or_plane, interval=None)`** - Adds a spaced series of planar curves resulting from the intersection of defined cutting planes t...
**`AddSrfControlPtGrid(count, points, degree=(3,3))`** - Creates a surface from a grid of points
**`AddSrfPt(points)`** - Creates a new surface from either 3 or 4 corner points.
**`AddSrfPtGrid(count, points, degree=(3,3), closed=(False,False))`** - Creates a surface from a grid of points
**`AddSweep1(rail, shapes, closed=False)`** - Adds a surface created through profile curves that define the surface shape and one curve that de...
**`AddSweep2(rails, shapes, closed=False)`** - Adds a surface created through profile curves that define the surface shape and two curves that d...
**`BrepClosestPoint(object_id, point)`** - Returns the point on a surface or polysurface that is closest to a test point. This function work...
**`CapPlanarHoles(surface_id)`** - Caps planar holes in a surface or polysurface
**`ChangeSurfaceDegree(object_id, degree)`** - Changes the degree of a surface object. For more information see the Rhino help file for the Chan...
**`DuplicateEdgeCurves(object_id, select=False)`** - Duplicates the edge curves of a surface or polysurface. For more information, see the Rhino help ...
**`DuplicateSurfaceBorder(surface_id, type=0)`** - Create curves that duplicate a surface or polysurface border
**`EvaluateSurface(surface_id, u, v)`** - Evaluates a surface at a U,V parameter
**`ExplodePolysurfaces(object_ids, delete_input=False)`** - Explodes, or unjoins, one or more polysurface objects. Polysurfaces will be exploded into separat...
**`ExtendSurface(surface_id, parameter, length, smooth=True)`** - Lengthens an untrimmed surface object
**`ExtractIsoCurve(surface_id, parameter, direction)`** - Extracts isoparametric curves from a surface
**`ExtractSurface(object_id, face_indices, copy=False)`** - Separates or copies a surface or a copy of a surface from a polysurface
**`ExtrudeCurve(curve_id, path_id)`** - Creates a surface by extruding a curve along a path
**`ExtrudeCurvePoint(curve_id, point)`** - Creates a surface by extruding a curve to a point
**`ExtrudeSurface(surface, curve, cap=True)`** - Create surface by extruding along a path curve
**`FilletSurfaces(surface0, surface1, radius, uvparam0=None, uvparam1=None)`** - Create constant radius rolling ball fillets between two surfaces. Note, this function does not tr...
**`FlipSurface(surface_id, flip=None)`** - Returns or changes the normal direction of a surface. This feature can also be found in Rhino's D...
**`IntersectBreps(brep1, brep2, tolerance=None)`** - Intersects a brep object with another brep object. Note, unlike the SurfaceSurfaceIntersection fu...
**`IntersectSpheres(sphere_plane0, sphere_radius0, sphere_plane1, sphere_radius1)`** - Calculates intersections of two spheres
**`IsBrep(object_id)`** - Verifies an object is a Brep, or a boundary representation model, object.
**`IsCone(object_id)`** - Determines if a surface is a portion of a cone
**`IsCylinder(object_id)`** - Determines if a surface is a portion of a cone
**`IsPlaneSurface(object_id)`** - Verifies an object is a plane surface. Plane surfaces can be created by the Plane command. Note, ...
**`IsPointInSurface(object_id, point, strictly_in=False, tolerance=None)`** - Verifies that a point is inside a closed surface or polysurface
**`IsPointOnSurface(object_id, point)`** - Verifies that a point lies on a surface
**`IsPolysurfaceClosed(object_id)`** - Verifies a polysurface object is closed. If the polysurface fully encloses a volume, it is consid...
**`IsSphere(object_id)`** - Determines if a surface is a portion of a sphere
**`IsSurfaceClosed( surface_id, direction )`** - Verifies a surface object is closed in the specified direction. If the surface fully encloses a v...
**`IsSurfacePeriodic(surface_id, direction)`** - Verifies a surface object is periodic in the specified direction.
**`IsSurfacePlanar(surface_id, tolerance=None)`** - Verifies a surface object is planar
**`IsSurfaceRational(surface_id)`** - Verifies a surface object is rational
**`IsSurfaceSingular(surface_id, direction)`** - Verifies a surface object is singular in the specified direction. Surfaces are considered singula...
**`IsSurfaceTrimmed(surface_id)`** - Verifies a surface object has been trimmed
**`IsTorus(surface_id)`** - Determines if a surface is a portion of a torus
**`JoinSurfaces(object_ids, delete_input=False, return_all=False)`** - Joins two or more surface or polysurface objects together to form one polysurface object
**`MakeSurfacePeriodic(surface_id, direction, delete_input=False)`** - Makes an existing surface a periodic NURBS surface
**`OffsetSurface(surface_id, distance, tolerance=None, both_sides=False, create_solid=False)`** - Offsets a trimmed or untrimmed surface by a distance. The offset surface will be added to Rhino.
**`PullCurve(surface, curve, delete_input=False)`** - Pulls a curve object to a surface object
**`RebuildSurface(object_id, degree=(3,3), pointcount=(10,10))`** - Rebuilds a surface to a given degree and control point count. For more information see the Rhino ...
**`RemoveSurfaceKnot(surface, uv_parameter, v_direction)`** - Deletes a knot from a surface object.
**`ReverseSurface(surface_id, direction)`** - Reverses U or V directions of a surface, or swaps (transposes) U and V directions.
**`ShootRay(surface_ids, start_point, direction, reflections=10)`** - Shoots a ray at a collection of surfaces
**`ShortPath(surface_id, start_point, end_point)`** - Creates the shortest possible curve(geodesic) between two points on a surface. For more details, ...
**`ShrinkTrimmedSurface(object_id, create_copy=False)`** - Shrinks the underlying untrimmed surfaces near to the trimming boundaries. See the ShrinkTrimmedS...
**`SplitBrep(brep_id, cutter_id, delete_input=False)`** - Splits a brep
**`SurfaceAreaCentroid(object_id)`** - Calculates the area centroid of a surface or polysurface
**`SurfaceAreaMoments(surface_id)`** - Calculates area moments of inertia of a surface or polysurface object. See the Rhino help for "Ma...
**`SurfaceClosestPoint(surface_id, test_point)`** - Returns U,V parameters of point on a surface that is closest to a test point
**`SurfaceCone(surface_id)`** - Returns the definition of a surface cone
**`SurfaceCurvature(surface_id, parameter)`** - Returns the curvature of a surface at a U,V parameter. See Rhino help for details of surface curv...
**`SurfaceCylinder(surface_id)`** - Returns the definition of a cylinder surface
**`SurfaceDegree(surface_id, direction=2)`** - Returns the degree of a surface object in the specified direction
**`SurfaceDomain(surface_id, direction)`** - Returns the domain of a surface object in the specified direction.
**`SurfaceEditPoints(surface_id, return_parameters=False, return_all=True)`** - Returns the edit, or Greville points of a surface object. For each surface control point, there i...
**`SurfaceEvaluate(surface_id, parameter, derivative)`** - A general purpose surface evaluator
**`SurfaceFrame(surface_id, uv_parameter)`** - Returns a plane based on the normal, u, and v directions at a surface U,V parameter
**`SurfaceIsocurveDensity(surface_id, density=None)`** - Returns or sets the isocurve density of a surface or polysurface object. An isoparametric curve i...
**`SurfaceKnotCount(surface_id)`** - Returns the control point count of a surface surface_id = the surface's identifier
**`SurfaceKnots(surface_id)`** - Returns the knots, or knot vector, of a surface object.
**`SurfaceNormal(surface_id, uv_parameter)`** - Returns 3D vector that is the normal to a surface at a parameter
**`SurfaceNormalizedParameter(surface_id, parameter)`** - Converts surface parameter to a normalized surface parameter; one that ranges between 0.0 and 1.0...
**`SurfaceParameter(surface_id, parameter)`** - Converts normalized surface parameter to a surface parameter; or within the surface's domain
**`SurfacePointCount(surface_id)`** - Returns the control point count of a surface surface_id = the surface's identifier
**`SurfacePoints(surface_id, return_all=True)`** - Returns the control points, or control vertices, of a surface object
**`SurfaceSphere(surface_id)`** - Gets the sphere definition from a surface, if possible.
**`SurfaceTorus(surface_id)`** - Returns the definition of a surface torus
**`SurfaceVolumeCentroid(object_id)`** - Calculates volume centroid of a closed surface or polysurface
**`SurfaceVolumeMoments(surface_id)`** - Calculates volume moments of inertia of a surface or polysurface object. For more information, se...
**`SurfaceWeights(object_id)`** - Returns list of weight values assigned to the control points of a surface. The number of weights ...
**`TrimBrep(object_id, cutter, tolerance=None)`** - Trims a surface using an oriented cutter
**`TrimSurface( surface_id, direction, interval, delete_input=False)`** - Remove portions of the surface outside of the specified interval
**`UnrollSurface(surface_id, explode=False, following_geometry=None, absolute_tolerance=None, relative_tolerance=None)`** - Flattens a developable surface or polysurface

---

## Toolbar

**`CloseToolbarCollection(name, prompt=False)`** - Closes a currently open toolbar collection
**`HideToolbar(name, toolbar_group)`** - Hides a previously visible toolbar group in an open toolbar collection
**`IsToolbar(name, toolbar, group=False)`** - Verifies a toolbar (or toolbar group) exists in an open collection file
**`IsToolbarCollection(file)`** - Verifies that a toolbar collection is open
**`IsToolbarDocked(name, toolbar_group)`** - Verifies that a toolbar group in an open toolbar collection is visible
**`IsToolbarVisible(name, toolbar_group)`** - Verifies that a toolbar group in an open toolbar collection is visible
**`OpenToolbarCollection(file)`** - Opens a toolbar collection file
**`SaveToolbarCollection(name)`** - Saves an open toolbar collection to disk
**`SaveToolbarCollectionAs(name, file)`** - Saves an open toolbar collection to a different disk file
**`ShowToolbar(name, toolbar_group)`** - Shows a previously hidden toolbar group in an open toolbar collection
**`ToolbarCollectionCount()`** - Returns number of currently open toolbar collections
**`ToolbarCollectionNames()`** - Returns names of all currently open toolbar collections
**`ToolbarCollectionPath(name)`** - Returns full path to a currently open toolbar collection file
**`ToolbarCount(name, groups=False)`** - Returns the number of toolbars or groups in a currently open toolbar file
**`ToolbarNames(name, groups=False)`** - Returns the names of all toolbars (or toolbar groups) found in a currently open toolbar file

---

## Transformation

**`IsXformIdentity(xform)`** - Verifies a matrix is the identity matrix
**`IsXformSimilarity(xform)`** - Verifies a matrix is a similarity transformation. A similarity transformation can be broken into ...
**`IsXformZero(xform)`** - verifies that a matrix is a zero transformation matrix
**`XformCPlaneToWorld(point, plane)`** - Transform point from construction plane coordinates to world coordinates
**`XformChangeBasis(initial_plane, final_plane)`** - Returns a change of basis transformation matrix or None on error
**`XformChangeBasis2(x0,y0,z0,x1,y1,z1)`** - Returns a change of basis transformation matrix of None on error
**`XformCompare(xform1, xform2)`** - Compares two transformation matrices
**`XformDeterminant(xform)`** - Returns the determinant of a transformation matrix. If the determinant of a transformation matrix...
**`XformDiagonal(diagonal_value)`** - Returns a diagonal transformation matrix. Diagonal matrices are 3x3 with the bottom row [0,0,0,1]
**`XformIdentity()`** - returns the identity transformation matrix
**`XformInverse(xform)`** - Returns the inverse of a non-singular transformation matrix
**`XformMirror(mirror_plane_point, mirror_plane_normal)`** - Creates a mirror transformation matrix
**`XformMultiply(xform1, xform2)`** - Multiplies two transformation matrices, where result = xform1 * xform2
**`XformPlanarProjection(plane)`** - Returns a transformation matrix that projects to a plane.
**`XformRotation1(initial_plane, final_plane)`** - Returns a rotation transformation that maps initial_plane to final_plane. The planes should be ri...
**`XformRotation2(angle_degrees, rotation_axis, center_point)`** - Returns a rotation transformation around an axis
**`XformRotation3( start_direction, end_direction, center_point )`** - Calculate the minimal transformation that rotates start_direction to end_direction while fixing c...
**`XformRotation4(x0, y0, z0, x1, y1, z1)`** - Returns a rotation transformation.
**`XformScale(scale, point=None)`** - Creates a scale transformation
**`XformScreenToWorld(point, view=None, screen_coordinates=False)`** - Transforms a point from either client-area coordinates of the specified view or screen coordinate...
**`XformShear(plane, x, y, z)`** - Returns a shear transformation matrix
**`XformTranslation(vector)`** - Creates a translation transformation matrix
**`XformWorldToCPlane(point, plane)`** - Transforms a point from world coordinates to construction plane coordinates.
**`XformWorldToScreen(point, view=None, screen_coordinates=False)`** - Transforms a point from world coordinates to either client-area coordinates of the specified view...
**`XformZero()`** - Returns a zero transformation matrix

---

## Userdata

### Available Functions

**`DeleteDocumentData(section=None, entry=None)`** - Removes user data strings from the current document
**`DocumentDataCount()`** - Returns the number of user data strings in the current document
**`DocumentUserTextCount()`** - Returns the number of user text strings in the current document
**`GetDocumentData(section=None, entry=None)`** - Returns a user data item from the current document
**`GetDocumentUserText(key=None)`** - Returns user text stored in the document
**`GetUserText(object_id, key=None, attached_to_geometry=False)`** - Returns user text stored on an object.
**`IsDocumentData()`** - Verifies the current document contains user data
**`IsDocumentUserText()`** - Verifies the current document contains user text
**`IsUserText(object_id)`** - Verifies that an object contains user text
**`SetDocumentData(section, entry, value)`** - Adds or sets a user data string to the current document
**`SetDocumentUserText(key, value=None)`** - Sets or removes user text stored in the document
**`SetUserText(object_id, key, value=None, attach_to_geometry=False)`** - Sets or removes user text stored on an object.

---

## Userinterface

**`BrowseForFolder(folder=None, message=None, title=None)`** - Display browse-for-folder dialog allowing the user to select a folder
**`CheckListBox(items, message=None, title=None)`** - Displays a list of items in a checkable-style list dialog box
**`ComboListBox(items, message=None, title=None)`** - Displays a list of items in a combo-style list box dialog.
**`EditBox(default_string=None, message=None, title=None)`** - Display dialog prompting the user to enter a string. The string value may span multiple lines
**`GetAngle(point=None, reference_point=None, default_angle_degrees=0, message=None)`** - Pause for user input of an angle
**`GetBoolean(message, items, defaults)`** - Pauses for user input of one or more boolean values. Boolean values are displayed as click-able c...
**`GetBox(mode=0, base_point=None, prompt1=None, prompt2=None, prompt3=None)`** - Pauses for user input of a box
**`GetColor(color=[0,0,0])`** - Display the Rhino color picker dialog allowing the user to select an RGB color
**`GetCursorPos()`** - Retrieves the cursor's position
**`GetDistance(first_pt=None, distance=None, first_pt_msg='First distance point', second_pt_msg='Second distance point')`** - Pauses for user input of a distance.
**`GetEdgeCurves(message=None, min_count=1, max_count=0, select=False)`** - Prompt the user to pick one or more surface or polysurface edge curves
**`GetInteger(message=None, number=None, minimum=None, maximum=None)`** - Pauses for user input of a whole number.
**`GetLayer(title="Select Layer", layer=None, show_new_button=False, show_set_current=False)`** - Displays dialog box prompting the user to select a layer
**`GetLayers(title="Select Layers", show_new_button=False)`** - Displays a dialog box prompting the user to select one or more layers
**`GetLine(mode=0, point=None, message1=None, message2=None, message3=None)`** - Prompts the user to pick points that define a line
**`GetLinetype(default_linetype=None, show_by_layer=False)`** - Displays a dialog box prompting the user to select one linetype
**`GetMeshFaces(object_id, message="", min_count=1, max_count=0)`** - Prompts the user to pick one or more mesh faces
**`GetMeshVertices(object_id, message="", min_count=1, max_count=0)`** - Prompts the user to pick one or more mesh vertices
**`GetPoint(message=None, base_point=None, distance=None, in_plane=False)`** - Pauses for user input of a point.
**`GetPointOnCurve(curve_id, message=None)`** - Pauses for user input of a point constrainted to a curve object
**`GetPointOnMesh(mesh_id, message=None)`** - Pauses for user input of a point constrained to a mesh object
**`GetPointOnSurface(surface_id, message=None)`** - Pauses for user input of a point constrained to a surface or polysurface object
**`GetPoints(draw_lines=False, in_plane=False, message1=None, message2=None, max_points=None, base_point=None)`** - Pauses for user input of one or more points
**`GetPolyline(flags=3, message1=None, message2=None, message3=None, message4=None, min=2, max=0)`** - Prompts the user to pick points that define a polyline.
**`GetReal(message="Number", number=None, minimum=None, maximum=None)`** - Pauses for user input of a number.
**`GetRectangle(mode=0, base_point=None, prompt1=None, prompt2=None, prompt3=None)`** - Pauses for user input of a rectangle
**`GetString(message=None, defaultString=None, strings=None)`** - Pauses for user input of a string value
**`ListBox(items, message=None, title=None, default=None)`** - Display a list of items in a list box dialog.
**`MessageBox(message, buttons=0, title="")`** - Displays a message box. A message box contains a message and title, plus any combination of prede...
**`MultiListBox(items, message=None, title=None, defaults=None)`** - Displays a list of items in a multiple-selection list box dialog
**`OpenFileName(title=None, filter=None, folder=None, filename=None, extension=None)`** - Displays file open dialog box allowing the user to enter a file name. Note, this function does no...
**`OpenFileNames(title=None, filter=None, folder=None, filename=None, extension=None)`** - Displays file open dialog box allowing the user to select one or more file names. Note, this func...
**`PopupMenu(items, modes=None, point=None, view=None)`** - Display a context-style popup menu. The popup menu can appear almost anywhere, and can be dismiss...
**`PropertyListBox(items, values, message=None, title=None)`** - Displays list of items and their values in a property-style list box dialog
**`RealBox(message="", default_number=None, title="", minimum=None, maximum=None)`** - Display a dialog box prompting the user to enter a number
**`SaveFileName(title=None, filter=None, folder=None, filename=None, extension=None)`** - Display a save dialog box allowing the user to enter a file name. Note, this function does not sa...
**`StringBox(message=None, default_value=None, title=None)`** - Display a dialog box prompting the user to enter a string value.
**`TextOut(message=None, title=None)`** - Display a text dialog box similar to the one used by the _What command.
---

## Utility

#### `Distance(point1, point2)`
**Measures distance between two 3D points, or between a 3D point and an array of 3D points.**
*Returns:* point: If point2 is a 3D point then the distance if successful. point: If point2 is a list of points, then an list of distances if successful. None: if not successful

**`Angle(point1, point2, plane=True)`** - Measures the angle between two points
**`Angle2(line1, line2)`** - Measures the angle between two lines
**`ClipboardText(text=None)`** - Returns or sets a text string to the Windows clipboard
**`ColorAdjustLuma(rgb, luma, scale=False)`** - Changes the luminance of a red-green-blue value. Hue and saturation are not affected
**`ColorBlueValue(rgb)`** - Retrieves intensity value for the blue component of an RGB color
**`ColorGreenValue(rgb)`** - Retrieves intensity value for the green component of an RGB color
**`ColorHLSToRGB(hls)`** - Converts colors from hue-lumanence-saturation to RGB
**`ColorRGBToHLS(rgb)`** - Convert colors from RGB to HLS
**`ColorRedValue(rgb)`** - Retrieves intensity value for the red component of an RGB color
**`ContextIsGrasshopper()`** - Return True if the script is being executed in a grasshopper component
**`ContextIsRhino()`** - Return True if the script is being executed in the context of Rhino
**`CreateColor(color, g=None, b=None, a=None)`** - Converts 'color' into a native color object if possible. The returned data is accessible by index...
**`CreateInterval(interval, y=None)`** - Converts 'interval' into a Rhino.Geometry.Interval. If the provided object is already an interval...
**`CreatePlane(plane_or_origin, x_axis=None, y_axis=None, ignored=None)`** - Converts input into a Rhino.Geometry.Plane object if possible. If the provided object is already ...
**`CreatePoint(point, y=None, z=None)`** - Converts 'point' into a Rhino.Geometry.Point3d if possible. If the provided object is already a p...
**`CreateVector(vector, y=None, z=None)`** - Converts 'vector' into a Rhino.Geometry.Vector3d if possible. If the provided object is already a...
**`CreateXform(xform)`** - Converts input into a Rhino.Geometry.Transform object if possible. If the provided object is alre...
**`CullDuplicateNumbers(numbers, tolerance=None)`** - Removes duplicates from an array of numbers.
**`CullDuplicatePoints(points, tolerance=-1)`** - Removes duplicates from a list of 3D points.
**`GetSettings(filename, section=None, entry=None)`** - Returns string from a specified section in a initialization file.
**`Polar(point, angle_degrees, distance, plane=None)`** - Returns 3D point that is a specified angle and distance from a 3D point
**`SimplifyArray(points)`** - Flattens an array of 3-D points into a one-dimensional list of real numbers. For example, if you ...
**`Sleep(milliseconds)`** - Suspends execution of a running script for the specified interval
**`SortPointList(points, tolerance=None)`** - Sorts list of points so they will be connected in a "reasonable" polyline order
**`SortPoints(points, ascending=True, order=0)`** - Sorts the components of an array of 3D points
**`Str2Pt(point)`** - convert a formatted string value into a 3D point value

---

## View

**`AddDetail(layout_id, corner1, corner2, title=None, projection=1)`** - Add new detail view to an existing layout view
**`AddLayout(title=None, size=None)`** - Adds a new page layout view
**`AddNamedCPlane(cplane_name, view=None)`** - Adds new named construction plane to the document
**`AddNamedView(name, view=None)`** - Adds a new named view to the document
**`CurrentDetail(layout, detail=None, return_name=True)`** - Returns or changes the current detail view in a page layout view
**`CurrentView(view=None, return_name=True)`** - Returns or sets the currently active view
**`DeleteNamedCPlane(name)`** - Removes a named construction plane from the document
**`DeleteNamedView(name)`** - Removes a named view from the document
**`DetailLock(detail_id, lock=None)`** - Returns or modifies the projection locked state of a detail
**`DetailScale(detail_id, model_length=None, page_length=None)`** - Returns or modifies the scale of a detail object
**`IsDetail(layout, detail)`** - Verifies that a detail view exists on a page layout view
**`IsLayout(layout)`** - Verifies that a view is a page layout view
**`IsView(view)`** - Verifies that the specified view exists
**`IsViewCurrent(view)`** - Verifies that the specified view is the current, or active view
**`IsViewMaximized(view=None)`** - Verifies that the specified view is maximized (enlarged so as to fill the entire Rhino window)
**`IsViewPerspective(view)`** - Verifies that the specified view's projection is set to perspective
**`IsViewTitleVisible(view=None)`** - Verifies that the specified view's title window is visible
**`IsWallpaper(view)`** - Verifies that the specified view contains a wallpaper image
**`MaximizeRestoreView(view=None)`** - Toggles a view's maximized/restore window state of the specified view
**`NamedCPlane(name)`** - Returns the plane geometry of the specified named construction plane
**`NamedCPlanes()`** - Returns the names of all named construction planes in the document
**`NamedViews()`** - Returns the names of all named views in the document
**`RenameView(old_title, new_title)`** - Changes the title of the specified view
**`RestoreNamedCPlane(cplane_name, view=None)`** - Restores a named construction plane to the specified view.
**`RestoreNamedView(named_view, view=None, restore_bitmap=False)`** - Restores a named view to the specified view
**`RotateCamera(view=None, direction=0, angle=None)`** - Rotates a perspective-projection view's camera. See the RotateCamera command in the Rhino help fi...
**`RotateView(view=None, direction=0, angle=None)`** - Rotates a view. See RotateView command in Rhino help for more information
**`ShowGrid(view=None, show=None)`** - Shows or hides a view's construction plane grid
**`ShowGridAxes(view=None, show=None)`** - Shows or hides a view's construction plane grid axes.
**`ShowViewTitle(view=None, show=True)`** - Shows or hides the title window of a view
**`ShowWorldAxes(view=None, show=None)`** - Shows or hides a view's world axis icon
**`TiltView(view=None, direction=0, angle=None)`** - Tilts a view by rotating the camera up vector. See the TiltView command in the Rhino help file fo...
**`ViewCPlane(view=None, plane=None)`** - Return or set a view's construction plane
**`ViewCamera(view=None, camera_location=None)`** - Returns or sets the camera location of the specified view
**`ViewCameraLens(view=None, length=None)`** - Returns or sets the 35mm camera lens length of the specified perspective projection view.
**`ViewCameraPlane(view=None)`** - Returns the orientation of a view's camera.
**`ViewCameraTarget(view=None, camera=None, target=None)`** - Returns or sets the camera and target positions of the specified view
**`ViewCameraUp(view=None, up_vector=None)`** - Returns or sets the camera up direction of a specified
**`ViewDisplayMode(view=None, mode=None, return_name=True)`** - Return or set a view display mode
**`ViewDisplayModeId(name)`** - Return id of a display mode given it's name
**`ViewDisplayModeName(mode_id)`** - Return name of a display mode given it's id
**`ViewDisplayModes(return_names=True)`** - Return list of display modes
**`ViewNames(return_names=True, view_type=0)`** - Return the names, titles, or identifiers of all views in the document
**`ViewNearCorners(view=None)`** - Return 3d corners of a view's near clipping plane rectangle. Useful in determining the "real worl...
**`ViewProjection(view=None, mode=None)`** - Return or set a view's projection mode.
**`ViewRadius(view=None, radius=None, mode=False)`** - Returns or sets the radius of a parallel-projected view. Useful when you need an absolute zoom fa...
**`ViewSize(view=None)`** - Returns the width and height in pixels of the specified view
**`ViewSpeedTest(view=None, frames=100, freeze=True, direction=0, angle_degrees=5)`** - Test's Rhino's display performance
**`ViewTarget(view=None, target=None)`** - Returns or sets the target location of the specified view
**`ViewTitle(view_id)`** - Returns the name, or title, of a given view's identifier
**`Wallpaper(view=None, filename=None)`** - Returns or sets the wallpaper bitmap of the specified view. To remove a wallpaper bitmap, pass an...
**`WallpaperGrayScale(view=None, grayscale=None)`** - Returns or sets the grayscale display option of the wallpaper bitmap in a specified view
**`WallpaperHidden(view=None, hidden=None)`** - Returns or sets the visibility of the wallpaper bitmap in a specified view
**`ZoomBoundingBox(bounding_box, view=None, all=False)`** - Zooms to the extents of a specified bounding box in the specified view
**`ZoomExtents(view=None, all=False)`** - Zooms to extents of visible objects in the specified view
**`ZoomSelected(view=None, all=False)`** - Zoom to extents of selected objects in a view

---

*Source: https://developer.rhino3d.com/api/RhinoScriptSyntax/*
