# RhinoScriptSyntax API Reference

Compact reference for all 898 `rhinoscriptsyntax` (rs) functions. Rhino 8 / CPython 3.

`*` = used in MCP codebase

## Rhino 8 Notes
- CPython 3 via PythonNET 3.0 — use `float` literals (1.0 not 1) for radius, angle, tolerance params
- `import rhinoscriptsyntax as rs` still works; `import Rhino`, `import System` for .NET bridge
- Enum values may need `int()` cast in some contexts
- `rs.Command("_Line 0,0,0 10,10,0 ", False)` — trailing space needed, echo=False for scripts

## Types
- `guid` — object identifier string (from rs.Add*, rs.CopyObject, etc.)
- `point` — [x, y, z] list or tuple
- `vector` — [x, y, z] list or tuple (direction)
- `plane` — Rhino.Geometry.Plane (origin + x/y/z axes). Create with rs.PlaneFromNormal, rs.WorldXYPlane
- `color` — [r, g, b] or (r, g, b) tuple, 0-255
- `xform` — 4x4 transformation matrix

---

## Application (61)
AddAlias(alias, macro) -> str
AddSearchPath(folder, index=-1) -> int
AliasCount() -> int
AliasMacro(alias, macro=None) -> str
AliasNames() -> list[str]
AppearanceColor(item, color=None) -> color
AutosaveFile(filename=None) -> str
AutosaveInterval(minutes=None) -> int
BuildDate() -> str
ClearCommandHistory() -> None
Command(commandString, echo=True) -> bool  # Run any Rhino command
CommandHistory() -> str
DefaultRenderer(renderer=None) -> str
DeleteAlias(alias) -> bool
DeleteSearchPath(folder) -> bool
DisplayOleAlerts(enable) -> None
EdgeAnalysisColor(color=None) -> color
EdgeAnalysisMode(mode=None) -> int
EnableAutosave(enable=True) -> None
EnablePlugIn(plugin, enable=None) -> bool
ExeFolder() -> str
ExePlatform() -> int
ExeServiceRelease() -> int
ExeVersion() -> int
Exit() -> None
FindFile(filename) -> str
GetPlugInObject(plug_in) -> object
InCommand(ignore_runners=True) -> bool
InstallFolder() -> str
IsAlias(alias) -> bool
IsCommand(command_name) -> bool
IsPlugIn(plugin) -> bool
IsRunningOnWindows() -> bool
LastCommandName() -> str
LastCommandResult() -> int
LocaleID() -> int
Ortho(enable=None) -> bool
Osnap(enable=None) -> bool
OsnapDialog(visible=None) -> bool
OsnapMode(mode=None) -> int
Planar(enable=None) -> bool
PlugInId(plugin) -> guid
PlugIns(types=0, status=0) -> list[str]
ProjectOsnaps(enable=None) -> bool
Prompt(message=None) -> None
ScreenSize() -> [int, int]
SdkVersion() -> int
SearchPathCount() -> int
SearchPathList() -> list[str]
SendKeystrokes(keys=None, add_return=True) -> None
Snap(enable=None) -> bool
StatusBarDistance(distance=0) -> None
StatusBarMessage(message=None) -> None
StatusBarPoint(point=None) -> None
StatusBarProgressMeterHide() -> None
StatusBarProgressMeterShow(label, lower, upper, embed_label=True, show_percent=True) -> bool
StatusBarProgressMeterUpdate(position, absolute=True) -> int
TemplateFile(filename=None) -> str
TemplateFolder(folder=None) -> str
WindowHandle() -> int
WorkingFolder(folder=None) -> str

---

## Block (25)
AddBlock(object_ids, base_point, name=None, delete_input=False) -> str  # block name
BlockContainerCount(block_name) -> int
BlockContainers(block_name) -> list[str]
BlockCount() -> int
BlockDescription(block_name, description=None) -> str
BlockInstanceCount(block_name, where_to_look=0) -> int
BlockInstanceInsertPoint(object_id) -> point
BlockInstanceName(object_id) -> str
BlockInstanceXform(object_id) -> xform
BlockInstances(block_name, where_to_look=0) -> list[guid]
BlockNames(sort=False) -> list[str]
BlockObjectCount(block_name) -> int
BlockObjects(block_name) -> list[guid]
BlockPath(block_name) -> str
BlockStatus(block_name) -> int  # -1=linked not found, 0=ok, 1=linked newer
DeleteBlock(block_name) -> bool
ExplodeBlockInstance(object_id, explode_nested_instances=False) -> list[guid]
InsertBlock(block_name, insertion_point, scale=(1,1,1), angle_degrees=0, rotation_normal=(0,0,1)) -> guid
InsertBlock2(block_name, xform) -> guid
IsBlock(block_name) -> bool
IsBlockEmbedded(block_name) -> bool
IsBlockInUse(block_name, where_to_look=0) -> bool
IsBlockInstance(object_id) -> bool
IsBlockReference(block_name) -> bool
RenameBlock(block_name, new_name) -> str

---

## Curve (119)
*AddArc3Pt(start, end, point_on_arc) -> guid
AddArc(plane, radius, angle_degrees) -> guid
AddArcPtTanPt(start, direction, end) -> guid
AddBlendCurve(curves, parameters, reverses, continuities) -> guid  # tangent-matched blend
*AddCircle(plane_or_center, radius) -> guid
AddCircle3Pt(first, second, third) -> guid
AddCurve(points, degree=3) -> guid  # control-point curve
*AddEllipse(plane, radiusX, radiusY) -> guid
AddEllipse3Pt(center, second, third) -> guid
AddFilletCurve(curve0id, curve1id, radius=1.0, base_point0=None, base_point1=None) -> guid
*AddInterpCurve(points, degree=3, knotstyle=0, start_tangent=None, end_tangent=None) -> guid
AddInterpCrvOnSrf(surface_id, points) -> guid
AddInterpCrvOnSrfUV(surface_id, points) -> guid
*AddLine(start, end) -> guid
AddNurbsCurve(points, knots, degree, weights=None) -> guid
*AddPolyline(points, replace_id=None) -> guid
AddRectangle(plane, width, height) -> guid
AddSpiral(point0, point1, pitch, turns, radius0, radius1=None) -> guid
AddSubCrv(curve_id, param0, param1) -> guid  # extract sub-curve by params
AddTweenCurves(from_curve_id, to_curve_id, number_of_curves=1, method=0, sample_number=10) -> list[guid]
ArcAngle(curve_id, segment_index=-1) -> float
ArcCenterPoint(curve_id, segment_index=-1) -> point
ArcMidPoint(curve_id, segment_index=-1) -> point
ArcRadius(curve_id, segment_index=-1) -> float
ChangeCurveDegree(object_id, degree) -> bool
CircleCenterPoint(curve_id, segment_index=-1, return_plane=False) -> point|plane
CircleCircumference(curve_id, segment_index=-1) -> float
CircleRadius(curve_id, segment_index=-1) -> float
CloseCurve(curve_id, tolerance=-1.0) -> guid
ClosedCurveOrientation(curve_id, direction=(0,0,1)) -> int  # 1=CCW, -1=CW, 0=error
ConvertCurveToPolyline(curve_id, angle_tolerance=5.0, tolerance=0.01, delete_input=False, min_edge_length=0, max_edge_length=0) -> guid
*CurveArea(curve_id) -> [float, float]  # [area, error_bound]
CurveArcLengthPoint(curve_id, length, from_start=True) -> point
CurveAreaCentroid(curve_id) -> [point, [float, float, float]]
CurveArrows(curve_id, arrow_style=None) -> int
CurveBooleanDifference(curve_id_0, curve_id_1, tolerance=None) -> list[guid]
CurveBooleanIntersection(curve_id_0, curve_id_1, tolerance=None) -> list[guid]
CurveBooleanUnion(curve_id, tolerance=None) -> list[guid]
CurveBrepIntersect(curve_id, brep_id, tolerance=None) -> [list[guid], list[point]]
CurveClosestObject(curve_id, object_ids) -> [guid, point, point]
CurveClosestPoint(curve_id, test_point, segment_index=-1) -> float  # parameter
CurveContourPoints(curve_id, start_point, end_point, interval=None) -> list[point]
CurveCurvature(curve_id, parameter) -> [point, vector, point, float, float]
CurveCurveIntersection(curveA, curveB=None, tolerance=-1) -> list  # intersect events
CurveDegree(curve_id, segment_index=-1) -> int
CurveDeviation(curve_a, curve_b) -> [float, float, float, float, float, float]
CurveDim(curve_id, segment_index=-1) -> int
CurveDirectionsMatch(curve_id_0, curve_id_1) -> bool
CurveDiscontinuity(curve_id, style) -> list[point]
CurveDomain(curve_id, segment_index=-1) -> [float, float]
CurveEditPoints(curve_id, return_parameters=False, segment_index=-1) -> list[point]|list[float]
CurveEndPoint(curve_id, segment_index=-1) -> point
CurveFilletPoints(curve_id_0, curve_id_1, radius=1.0, base_point_0=None, base_point_1=None, return_points=True) -> [point, point, point, vector, vector]
CurveFrame(curve_id, parameter, segment_index=-1) -> plane
CurveKnotCount(curve_id, segment_index=-1) -> int
CurveKnots(curve_id, segment_index=-1) -> list[float]
*CurveLength(curve_id, segment_index=-1, sub_domain=None) -> float
CurveMidPoint(curve_id, segment_index=-1) -> point
CurveNormal(curve_id, segment_index=-1) -> vector
CurveNormalizedParameter(curve_id, parameter) -> float  # convert to 0-1 range
CurveParameter(curve_id, parameter) -> float  # normalized to domain
CurvePerpFrame(curve_id, parameter) -> plane
CurvePlane(curve_id, segment_index=-1) -> plane  # planar curves only
CurvePointCount(curve_id, segment_index=-1) -> int
CurvePoints(curve_id, segment_index=-1) -> list[point]  # control points
CurveRadius(curve_id, test_point, segment_index=-1) -> float
CurveSeam(curve_id, parameter) -> bool  # adjust seam of closed curve
CurveStartPoint(curve_id, segment_index=-1, point=None) -> point
CurveSurfaceIntersection(curve_id, surface_id, tolerance=-1, angle_tolerance=-1) -> list
CurveTangent(curve_id, parameter, segment_index=-1) -> vector
CurveWeights(curve_id, segment_index=-1) -> list[float]
DivideCurve(curve_id, segments, create_points=False, return_points=True) -> list[point]|list[float]
DivideCurveEquidistant(curve_id, distance, create_points=False, return_points=True) -> list[point]
DivideCurveLength(curve_id, length, create_points=False, return_points=True) -> list[point]|list[float]
EllipseCenterPoint(curve_id) -> point
EllipseQuadPoints(curve_id) -> [point, point, point, point]
EvaluateCurve(curve_id, t, segment_index=-1) -> point
*ExplodeCurves(curve_ids, delete_input=False) -> list[guid]
*ExtendCurveLength(curve_id, extension_type, side, length) -> guid  # type: 0=line,1=arc,2=smooth; side: 0=start,1=end,2=both
ExtendCurve(curve_id, extension_type, side, boundary_object_ids) -> guid
ExtendCurvePoint(curve_id, side, point, extension_type=2) -> guid
FairCurve(curve_id, tolerance=1.0) -> bool
FitCurve(curve_id, degree=3, distance_tolerance=-1, angle_tolerance=-1) -> guid
InsertCurveKnot(curve_id, parameter, symmetrical=False) -> bool
IsArc(curve_id, segment_index=-1) -> bool
IsCircle(curve_id, tolerance=None) -> bool
*IsCurve(object_id) -> bool
IsCurveClosable(curve_id, tolerance=None) -> bool
*IsCurveClosed(object_id) -> bool
IsCurveInPlane(object_id, plane=None) -> bool
IsCurveLinear(object_id, segment_index=-1) -> bool
*IsCurvePeriodic(curve_id, segment_index=-1) -> bool
*IsCurvePlanar(curve_id, segment_index=-1) -> bool
IsCurveRational(curve_id, segment_index=-1) -> bool
IsEllipse(object_id, segment_index=-1) -> bool
IsLine(object_id, segment_index=-1) -> bool
IsPointOnCurve(object_id, point, segment_index=-1) -> bool
IsPolyCurve(object_id, segment_index=-1) -> bool
IsPolyline(object_id, segment_index=-1) -> bool
*JoinCurves(object_ids, delete_input=False, tolerance=None) -> list[guid]
LineFitFromPoints(points) -> [point, point]
MakeCurveNonPeriodic(curve_id, delete_input=False) -> guid
MeanCurve(curve0, curve1, tolerance=None) -> guid
MeshPolyline(polyline_id) -> guid  # polygon mesh from closed polyline
*OffsetCurve(object_id, direction, distance, normal=None, style=1) -> list[guid]
OffsetCurveOnSurface(curve_id, surface_id, distance_or_parameter) -> guid|list[guid]
PlanarClosedCurveContainment(curve_a, curve_b, plane=None, tolerance=None) -> int  # 0=disjoint,1=a_in_b,2=b_in_a,3=both
PlanarCurveCollision(curve_a, curve_b, plane=None, tolerance=None) -> bool
PointInPlanarClosedCurve(point, curve, plane=None, tolerance=None) -> int  # 0=outside,1=inside,2=on
PolyCurveCount(curve_id, segment_index=-1) -> int
PolylineVertices(curve_id, segment_index=-1) -> list[point]
ProjectCurveToMesh(curve_ids, mesh_ids, direction) -> list[guid]
ProjectCurveToSurface(curve_ids, surface_ids, direction) -> list[guid]
RebuildCurve(curve_id, degree=3, point_count=10) -> bool
RemoveCurveKnot(curve, parameter) -> bool
ReverseCurve(curve_id) -> bool
SimplifyCurve(curve_id, flags=0) -> guid
SplitCurve(curve_id, parameter, delete_input=True) -> list[guid]  # param can be float or list
TrimCurve(curve_id, interval, delete_input=True) -> guid  # interval=[t0, t1]

---

## Dimension (39)
AddAlignedDimension(start_point, end_point, point_on_dimension_line, style=None) -> guid
AddDimStyle(dimstyle_name=None) -> str
AddLeader(points, view_or_plane=None, text=None) -> guid
AddLinearDimension(plane, start_point, end_point, point_on_dimension_line) -> guid
CurrentDimStyle(dimstyle_name=None) -> str
DeleteDimStyle(dimstyle_name) -> str
DimStyleAnglePrecision(dimstyle, precision=None) -> int
DimStyleArrowSize(dimstyle, size=None) -> float
DimStyleCount() -> int
DimStyleExtension(dimstyle, extension=None) -> float
DimStyleFont(dimstyle, font=None) -> str
DimStyleLeaderArrowSize(dimstyle, size=None) -> float
DimStyleLengthFactor(dimstyle, factor=None) -> float
DimStyleLinearPrecision(dimstyle, precision=None) -> int
DimStyleNames(sort=False) -> list[str]
DimStyleNumberFormat(dimstyle, format=None) -> int
DimStyleOffset(dimstyle, offset=None) -> float
DimStylePrefix(dimstyle, prefix=None) -> str
DimStyleScale(dimstyle, scale=None) -> float
DimStyleSuffix(dimstyle, suffix=None) -> str
DimStyleTextAlignment(dimstyle, alignment=None) -> int
DimStyleTextGap(dimstyle, gap=None) -> float
DimStyleTextHeight(dimstyle, height=None) -> float
DimensionStyle(object_id, dimstyle_name=None) -> str
DimensionText(object_id) -> str
DimensionUserText(object_id, usertext=None) -> str
DimensionValue(object_id) -> float
IsAlignedDimension(object_id) -> bool
IsAngularDimension(object_id) -> bool
IsDiameterDimension(object_id) -> bool
IsDimStyle(dimstyle) -> bool
IsDimStyleReference(dimstyle) -> bool
IsDimension(object_id) -> bool
IsLeader(object_id) -> bool
IsLinearDimension(object_id) -> bool
IsOrdinateDimension(object_id) -> bool
IsRadialDimension(object_id) -> bool
LeaderText(object_id, text=None) -> str
RenameDimStyle(oldstyle, newstyle) -> str

---

## Document (30)
CreatePreviewImage(filename, view=None, size=None, flags=0, wireframe=False) -> str
DocumentModified(modified=None) -> bool
DocumentName() -> str
DocumentPath() -> str
EnableRedraw(enable=True) -> bool
ExtractPreviewImage(filename, modelname=None) -> bool
IsDocumentModified() -> bool
Notes(newnotes=None) -> str
ReadFileVersion() -> str
*Redraw() -> None
RenderAntialias(style=None) -> int
RenderColor(item, color=None) -> color
RenderMeshDensity(density=None) -> float
RenderMeshMaxAngle(angle_degrees=None) -> float
RenderMeshMaxAspectRatio(ratio=None) -> float
RenderMeshMaxDistEdgeToSrf(distance=None) -> float
RenderMeshMaxEdgeLength(distance=None) -> float
RenderMeshMinEdgeLength(distance=None) -> float
RenderMeshMinInitialGridQuads(quads=None) -> int
RenderMeshQuality(quality=None) -> int
RenderMeshSettings(settings=None) -> int
RenderResolution(resolution=None) -> [int, int]
RenderSettings(settings=None) -> int
UnitAbsoluteTolerance(tolerance=None, in_model_units=True) -> float
UnitAngleTolerance(angle_tolerance_degrees=None, in_model_units=True) -> float
UnitDistanceDisplayPrecision(precision=None, model_units=True) -> int
UnitRelativeTolerance(relative_tolerance=None, in_model_units=True) -> float
UnitScale(to_system, from_system=None) -> float
UnitSystem(unit_system=None, scale=False, in_model_units=True) -> int  # 0=none,1=micron,2=mm,3=cm,4=m,8=in,9=ft
*UnitSystemName(capitalize=False, singular=True, abbreviate=False, model_units=True) -> str

---

## Geometry (35)
AddClippingPlane(plane, u_magnitude, v_magnitude, views=None) -> guid
AddPictureFrame(plane, filename, width=0.0, height=0.0, self_illumination=True, embed=False, use_alpha=False, make_mesh=False) -> guid
*AddPoint(point, y=None, z=None) -> guid
AddPointCloud(points, colors=None) -> guid
AddPoints(points) -> list[guid]
AddText(text, point_or_plane, height=1.0, font=None, font_style=0, justification=None) -> guid
AddTextDot(text, point) -> guid
Area(object_id) -> float  # works on curves, hatches, surfaces, meshes
*BoundingBox(objects, view_or_plane=None, in_world_coords=True) -> [point x 8]  # 8 corners
CompareGeometry(first, second) -> bool
ExplodeText(text_id, delete=False) -> list[guid]
IsClippingPlane(object_id) -> bool
IsPoint(object_id) -> bool
IsPointCloud(object_id) -> bool
IsText(object_id) -> bool
IsTextDot(object_id) -> bool
PointCloudClosestPoints(pt_cloud, needle_points, distance) -> list[list[int]]
PointCloudCount(object_id) -> int
PointCloudHasHiddenPoints(object_id) -> bool
PointCloudHasPointColors(object_id) -> bool
PointCloudHidePoints(object_id, hidden=[]) -> list[bool]
PointCloudKNeighbors(pt_cloud, needle_points, amount=1) -> list[list[int]]
PointCloudPointColors(object_id, colors=[]) -> list[color]
PointCloudPoints(object_id) -> list[point]
PointCoordinates(object_id, point=None) -> point
TextDotFont(object_id, fontface=None) -> str
TextDotHeight(object_id, height=None) -> int
TextDotPoint(object_id, point=None) -> point
TextDotText(object_id, text=None) -> str
TextObjectFont(object_id, font=None) -> str
TextObjectHeight(object_id, height=None) -> float
TextObjectPlane(object_id, plane=None) -> plane
TextObjectPoint(object_id, point=None) -> point
TextObjectStyle(object_id, style=None) -> int
TextObjectText(object_id, text=None) -> str

---

## Grips (15)
EnableObjectGrips(object_id, enable=True) -> bool
GetObjectGrip(message=None, preselect=False, select=False) -> [guid, int, point]
GetObjectGrips(message=None, preselect=False, select=False) -> list[[guid, int, point]]
NextObjectGrip(object_id, index, direction=0, enable=True) -> int
ObjectGripCount(object_id) -> int
ObjectGripLocation(object_id, index, point=None) -> point
ObjectGripLocations(object_id, points=None) -> list[point]
ObjectGripsOn(object_id) -> bool
ObjectGripsSelected(object_id) -> bool
PrevObjectGrip(object_id, index, direction=0, enable=True) -> int
SelectObjectGrip(object_id, index) -> bool
SelectObjectGrips(object_id) -> int
SelectedObjectGrips(object_id) -> list[int]
UnselectObjectGrip(object_id, index) -> bool
UnselectObjectGrips(object_id) -> int

---

## Group (17)
AddGroup(group_name=None) -> str
AddObjectToGroup(object_id, group_name) -> bool
AddObjectsToGroup(object_ids, group_name) -> int
DeleteGroup(group_name) -> bool
GroupCount() -> int
GroupNames() -> list[str]
HideGroup(group_name) -> int
IsGroup(group_name) -> bool
IsGroupEmpty(group_name) -> bool
LockGroup(group_name) -> int
ObjectTopGroup(object_id) -> str
RemoveObjectFromAllGroups(object_id) -> bool
RemoveObjectFromGroup(object_id, group_name) -> bool
RemoveObjectsFromGroup(object_ids, group_name) -> int
RenameGroup(old_name, new_name) -> str
ShowGroup(group_name) -> int
UnlockGroup(group_name) -> int

---

## Hatch (16)
AddHatch(curve_id, hatch_pattern=None, scale=1.0, rotation=0.0) -> guid
AddHatchPatterns(filename, replace=False) -> int
AddHatches(curve_ids, hatch_pattern=None, scale=1.0, rotation=0.0, tolerance=None) -> list[guid]
CurrentHatchPattern(hatch_pattern=None) -> str
ExplodeHatch(hatch_id, delete=False) -> list[guid]
HatchPattern(hatch_id, hatch_pattern=None) -> str
HatchPatternCount() -> int
HatchPatternDescription(hatch_pattern) -> str
HatchPatternFillType(hatch_pattern) -> int
HatchPatternNames() -> list[str]
HatchRotation(hatch_id, rotation=None) -> float
HatchScale(hatch_id, scale=None) -> float
IsHatch(object_id) -> bool
IsHatchPattern(name) -> bool
IsHatchPatternCurrent(hatch_pattern) -> bool
IsHatchPatternReference(hatch_pattern) -> bool

---

## Layer (33)
*AddLayer(name=None, color=None, visible=True, locked=False, parent=None) -> str
*CurrentLayer(layer=None) -> str
*DeleteLayer(layer) -> bool
ExpandLayer(layer, expand) -> bool
*IsLayer(layer) -> bool
IsLayerChangeable(layer) -> bool
IsLayerChildOf(layer, test) -> bool
IsLayerCurrent(layer) -> bool
IsLayerEmpty(layer) -> bool
IsLayerExpanded(layer) -> bool
IsLayerOn(layer) -> bool
IsLayerParentOf(layer, test) -> bool
IsLayerReference(layer) -> bool
IsLayerSelectable(layer) -> bool
IsLayerVisible(layer) -> bool
LayerChildCount(layer) -> int
LayerChildren(layer) -> list[str]
*LayerColor(layer, color=None) -> color
LayerCount() -> int
LayerId(layer) -> guid
LayerIds() -> list[guid]
LayerLinetype(layer, linetype=None) -> str
LayerMaterialIndex(layer, index=None) -> int
LayerName(layer_id, fullpath=True) -> str
*LayerNames(sort=False) -> list[str]
LayerOrder(layer) -> int
LayerPrintColor(layer, color=None) -> color
LayerPrintWidth(layer, width=None) -> float
*LayerLocked(layer, locked=None) -> bool
*LayerVisible(layer, visible=None, forcevisible_or_donotpersist=False) -> bool
ParentLayer(layer, parent=None) -> str
PurgeLayer(layer) -> bool  # removes layer even with objects
RenameLayer(oldname, newname) -> str

---

## Light (24)
AddDirectionalLight(start_point, end_point) -> guid
AddLinearLight(start_point, end_point, width=None) -> guid
AddPointLight(point) -> guid
AddRectangularLight(origin, width_point, height_point) -> guid
AddSpotLight(origin, radius, apex_point) -> guid
EnableLight(object_id, enable=None) -> bool
IsDirectionalLight(object_id) -> bool
IsLight(object_id) -> bool
IsLightEnabled(object_id) -> bool
IsLightReference(object_id) -> bool
IsLinearLight(object_id) -> bool
IsPointLight(object_id) -> bool
IsRectangularLight(object_id) -> bool
IsSpotLight(object_id) -> bool
LightColor(object_id, color=None) -> color
LightCount() -> int
LightDirection(object_id, direction=None) -> vector
LightLocation(object_id, location=None) -> point
LightName(object_id, name=None) -> str
LightObjects() -> list[guid]
RectangularLightPlane(object_id) -> plane
SpotLightHardness(object_id, hardness=None) -> float
SpotLightRadius(object_id, radius=None) -> float
SpotLightShadowIntensity(object_id, intensity=None) -> float

---

## Line (10)
LineClosestPoint(line, testpoint) -> point
LineCylinderIntersection(line, cylinder_plane, cylinder_height, cylinder_radius) -> list[point]
LineIsFartherThan(line, distance, point_or_line) -> bool
LineLineIntersection(lineA, lineB) -> [point, point]  # closest points on each line
LineMaxDistanceTo(line, point_or_line) -> float
LineMinDistanceTo(line, point_or_line) -> float
LinePlane(line) -> plane
LinePlaneIntersection(line, plane) -> float  # parameter on line
LineSphereIntersection(line, sphere_center, sphere_radius) -> list[point]
LineTransform(line, xform) -> [point, point]

---

## Linetype (4)
IsLinetype(name_or_id) -> bool
IsLinetypeReference(name_or_id) -> bool
LinetypeCount() -> int
LinetypeNames(sort=False) -> list[str]

---

## Material (16)
AddMaterialToLayer(layer) -> int  # material index
AddMaterialToObject(object_id) -> int
CopyMaterial(source_index, destination_index) -> bool
IsMaterialDefault(material_index) -> bool
IsMaterialReference(material_index) -> bool
MatchMaterial(source, destination) -> int
MaterialBump(material_index, filename=None) -> str
MaterialColor(material_index, color=None) -> color
MaterialEnvironmentMap(material_index, filename=None) -> str
MaterialName(material_index, name=None) -> str
MaterialReflectiveColor(material_index, color=None) -> color
MaterialShine(material_index, shine=None) -> float  # 0.0 to MaxShine
MaterialTexture(material_index, filename=None) -> str
MaterialTransparency(material_index, transparency=None) -> float  # 0.0 to 1.0
MaterialTransparencyMap(material_index, filename=None) -> str
ResetMaterial(material_index) -> bool

---

## Mesh (45)
AddMesh(vertices, face_vertices, vertex_normals=None, texture_coordinates=None, vertex_colors=None) -> guid
AddPlanarMesh(object_id, delete_input=False) -> guid  # from closed planar curve
CurveMeshIntersection(curve_id, mesh_id, return_faces=False) -> list[point]|list[int]
DisjointMeshCount(object_id) -> int
DuplicateMeshBorder(mesh_id) -> list[guid]
ExplodeMeshes(mesh_ids, delete=False) -> list[guid]
IsMesh(object_id) -> bool
IsMeshClosed(object_id) -> bool
IsMeshManifold(object_id) -> bool
IsPointOnMesh(object_id, point) -> bool
JoinMeshes(object_ids, delete_input=False) -> guid
MeshArea(object_ids) -> [float, float, float]  # [area, +error, -error]
MeshAreaCentroid(object_id) -> point
MeshBooleanDifference(input0, input1, delete_input=True, tolerance=None) -> list[guid]
MeshBooleanIntersection(input0, input1, delete_input=True) -> list[guid]
MeshBooleanSplit(input0, input1, delete_input=True) -> list[guid]
MeshBooleanUnion(mesh_ids, delete_input=True) -> list[guid]
MeshClosestPoint(object_id, point, maximum_distance=None) -> [point, int]
MeshFaceCenters(mesh_id) -> list[point]
MeshFaceCount(object_id) -> int
MeshFaceNormals(mesh_id) -> list[vector]
MeshFaceVertices(object_id) -> list[[int, int, int, int]]
MeshFaces(object_id, face_type=True) -> list[point]
MeshHasFaceNormals(object_id) -> bool
MeshHasTextureCoordinates(object_id) -> bool
MeshHasVertexColors(object_id) -> bool
MeshHasVertexNormals(object_id) -> bool
MeshMeshIntersection(mesh1, mesh2, tolerance=None) -> list[list[point]]
MeshNakedEdgePoints(object_id) -> list[bool]
MeshOffset(mesh_id, distance) -> guid
MeshOutline(object_ids, view=None) -> list[guid]
MeshQuadCount(object_id) -> int
MeshQuadsToTriangles(object_id) -> bool
MeshToNurb(object_id, trimmed_triangles=True, delete_input=False) -> guid
MeshTriangleCount(object_id) -> int
MeshVertexColors(mesh_id, colors=0) -> list[color]
MeshVertexCount(object_id) -> int
MeshVertexFaces(mesh_id, vertex_index) -> list[int]
MeshVertexNormals(mesh_id) -> list[vector]
MeshVertices(object_id) -> list[point]
MeshVolume(object_ids) -> [float, float, float]
MeshVolumeCentroid(object_id) -> point
PullCurveToMesh(mesh_id, curve_id) -> guid
SplitDisjointMesh(object_id, delete_input=False) -> list[guid]
UnifyMeshNormals(object_id) -> int  # num flipped faces

---

## Object (60)
*CopyObject(object_id, translation=None) -> guid
CopyObjects(object_ids, translation=None) -> list[guid]
*DeleteObject(object_id) -> bool
*DeleteObjects(object_ids) -> int
FlashObject(object_ids, style=True) -> None
HideObject(object_id) -> bool
HideObjects(object_ids) -> int
IsLayoutObject(object_id) -> bool
IsObject(object_id) -> bool
IsObjectHidden(object_id) -> bool
IsObjectInBox(object_id, box, test_mode=True) -> bool
IsObjectInGroup(object_id, group_name=None) -> bool
IsObjectLocked(object_id) -> bool
IsObjectNormal(object_id) -> bool
IsObjectReference(object_id) -> bool
IsObjectSelectable(object_id) -> bool
IsObjectSelected(object_id) -> bool
IsObjectSolid(object_id) -> bool
IsObjectValid(object_id) -> bool
IsVisibleInView(object_id, view=None) -> bool
LockObject(object_id) -> bool
LockObjects(object_ids) -> int
MatchObjectAttributes(target_ids, source_id=None) -> int
*MirrorObject(object_id, start_point, end_point, copy=False) -> guid
MirrorObjects(object_ids, start_point, end_point, copy=False) -> list[guid]
*MoveObject(object_id, translation) -> guid
MoveObjects(object_ids, translation) -> list[guid]
*ObjectColor(object_ids, color=None) -> color|int
ObjectColorSource(object_ids, source=None) -> int  # 0=layer,1=object,2=material,3=parent
ObjectDescription(object_id) -> str
ObjectGroups(object_id) -> list[str]
ObjectLayout(object_id, layout=None, return_name=True) -> str
*ObjectLayer(object_id, layer=None) -> str
ObjectLinetype(object_ids, linetype=None) -> str
ObjectLinetypeSource(object_ids, source=None) -> int
ObjectMaterialIndex(object_id, material_index=None) -> int
ObjectMaterialSource(object_ids, source=None) -> int
*ObjectName(object_id, name=None) -> str
ObjectPrintColor(object_ids, color=None) -> color
ObjectPrintColorSource(object_ids, source=None) -> int
ObjectPrintWidth(object_ids, width=None) -> float
ObjectPrintWidthSource(object_ids, source=None) -> int
OrientObject(object_id, reference, target, flags=0) -> guid  # map ref points to target points
*ObjectType(object_id) -> int  # 1=point,2=pointcloud,4=curve,8=surface,16=polysurface,32=mesh,256=light,512=annotation,4096=block,8192=textdot
RotateObject(object_id, center_point, rotation_angle, axis=None, copy=False) -> guid
*RotateObjects(object_ids, center_point, rotation_angle, axis=None, copy=False) -> list[guid]
*ScaleObject(object_id, origin, scale, copy=False) -> guid  # scale=[sx,sy,sz]
ScaleObjects(object_ids, origin, scale, copy=False) -> list[guid]
SelectObject(object_id, redraw=True) -> bool
*SelectObjects(object_ids) -> int
ShearObject(object_id, origin, reference_point, angle_degrees, copy=False) -> guid
ShearObjects(object_ids, origin, reference_point, angle_degrees, copy=False) -> list[guid]
ShowObject(object_id) -> bool
ShowObjects(object_ids) -> int
TransformObject(object_id, matrix, copy=False) -> guid
TransformObjects(object_ids, matrix, copy=False) -> list[guid]
UnlockObject(object_id) -> bool
UnlockObjects(object_ids) -> int
UnselectObject(object_id) -> bool
UnselectObjects(object_ids) -> int

---

## Plane (18)
DistanceToPlane(plane, point) -> float
EvaluatePlane(plane, parameter) -> point  # parameter=[u,v]
IntersectPlanes(plane1, plane2, plane3) -> point
MovePlane(plane, origin) -> plane
PlaneClosestPoint(plane, point, return_point=True) -> point|[float, float]
PlaneCurveIntersection(plane, curve, tolerance=None) -> list  # intersection events
PlaneEquation(plane) -> [float, float, float, float]  # [a,b,c,d]
PlaneFitFromPoints(points) -> plane
PlaneFromFrame(origin, x_axis, y_axis) -> plane
*PlaneFromNormal(origin, normal, xaxis=None) -> plane
PlaneFromPoints(origin, x, y) -> plane
PlanePlaneIntersection(plane1, plane2) -> [point, point]  # line
PlaneSphereIntersection(plane, sphere_plane, sphere_radius) -> [int, plane, float]  # type, circle_plane, radius
PlaneTransform(plane, xform) -> plane
RotatePlane(plane, angle_degrees, axis) -> plane
WorldXYPlane() -> plane
WorldYZPlane() -> plane
WorldZXPlane() -> plane

---

## Pointvector (33)
IsVectorParallelTo(vector1, vector2) -> int  # 1=parallel,-1=anti-parallel,0=not
IsVectorPerpendicularTo(vector1, vector2) -> bool
IsVectorTiny(vector) -> bool
IsVectorZero(vector) -> bool
PointAdd(point1, point2) -> point
PointArrayBoundingBox(points, view_or_plane=None, in_world_coords=True) -> [point x 8]
PointArrayClosestPoint(points, test_point) -> int  # index
PointArrayTransform(points, xform) -> list[point]
PointClosestObject(point, object_ids) -> [guid, point]
PointCompare(point1, point2, tolerance=None) -> bool
PointDivide(point, divide) -> point
PointScale(point, scale) -> point
PointSubtract(point1, point2) -> point
PointTransform(point, xform) -> point
PointsAreCoplanar(points, tolerance=1.0e-12) -> bool
ProjectPointToMesh(points, mesh_ids, direction) -> list[point]
ProjectPointToSurface(points, surface_ids, direction) -> list[point]
PullPoints(object_id, points) -> list[point]
VectorAdd(vector1, vector2) -> vector
VectorAngle(vector1, vector2) -> float  # degrees
VectorCompare(vector1, vector2) -> bool
VectorCreate(to_point, from_point) -> vector
VectorCrossProduct(vector1, vector2) -> vector
VectorDivide(vector, divide) -> vector
VectorDotProduct(vector1, vector2) -> float
VectorLength(vector) -> float
VectorMultiply(vector1, vector2) -> float  # dot product
VectorReverse(vector) -> vector
VectorRotate(vector, angle_degrees, axis) -> vector
VectorScale(vector, scale) -> vector
VectorSubtract(vector1, vector2) -> vector
VectorTransform(vector, xform) -> vector
VectorUnitize(vector) -> vector

---

## Selection (25)
*AllObjects(select=False, include_lights=False, include_grips=False, include_references=False) -> list[guid]
FirstObject(select=False, include_lights=False, include_grips=False) -> guid
GetCurveObject(message=None, preselect=False, select=False) -> [guid, bool, int, point, str]
GetObject(message=None, filter=0, preselect=False, select=False, custom_filter=None, subobjects=False) -> guid
GetObjectEx(message=None, filter=0, preselect=False, select=False, objects=None) -> [guid, bool, int, point]
GetObjects(message=None, filter=0, group=True, preselect=False, select=False, objects=None, minimum_count=1, maximum_count=0, custom_filter=None) -> list[guid]
GetObjectsEx(message=None, filter=0, group=True, preselect=False, select=False, objects=None) -> list[[guid, bool, int, point]]
GetPointCoordinates(message="Select points", preselect=False) -> list[point]
GetSurfaceObject(message="Select surface", preselect=False, select=False) -> [guid, bool, int, point, [float, float]]
HiddenObjects(include_lights=False, include_grips=False, include_references=False) -> list[guid]
InvertSelectedObjects(include_lights=False, include_grips=False, include_references=False) -> int
LastCreatedObjects(select=False) -> list[guid]
LastObject(select=False, include_lights=False, include_grips=False) -> guid
LockedObjects(include_lights=False, include_grips=False, include_references=False) -> list[guid]
NextObject(object_id, select=False, include_lights=False, include_grips=False) -> guid
NormalObjects(include_lights=False, include_grips=False) -> list[guid]
ObjectsByColor(color, select=False, include_lights=False) -> list[guid]
ObjectsByGroup(group_name, select=False) -> list[guid]
*ObjectsByLayer(layer_name, select=False) -> list[guid]
ObjectsByName(name, select=False, include_lights=False, include_references=False) -> list[guid]
*ObjectsByType(geometry_type, select=False, state=0) -> list[guid]  # type: 0=all,4=curve,8=surface,16=polysrf,32=mesh
*SelectedObjects(include_lights=False, include_grips=False) -> list[guid]
*UnselectAllObjects() -> int
VisibleObjects(view=None, select=False, include_lights=False, include_grips=False) -> list[guid]
WindowPick(corner1, corner2, view=None, select=False, in_window=True) -> list[guid]

---

## Surface (100)
*AddBox(corners) -> guid  # 8 corner points
*AddCone(base, height, radius, cap=True) -> guid  # height can be point or float
AddCutPlane(object_ids, start_point, end_point, normal=None) -> guid
*AddCylinder(base, height, radius, cap=True) -> guid
AddEdgeSrf(curve_ids) -> guid  # 2-4 edge curves
*AddLoftSrf(object_ids, start=None, end=None, loft_type=0, simplify_method=0, value=0, closed=False) -> list[guid]  # loft_type: 0=normal,1=loose,2=tight,3=straight,4=developable
AddNetworkSrf(curves, continuity=1, edge_tolerance=0, interior_tolerance=0, angle_tolerance=0) -> guid
AddNurbsSurface(point_count, points, knots_u, knots_v, degree, weights=None) -> guid
AddPatch(object_ids, uv_spans_OR_surface_id, tolerance=None, trim=True, point_spacing=0.1, flexibility=1.0, surface_pull=1.0, fix_edges=False) -> guid
AddPipe(curve_id, parameters, radii, blend_type=0, cap=0, fit=False) -> list[guid]
AddPlanarSrf(object_ids) -> list[guid]  # from closed planar curves
AddPlaneSurface(plane, u_dir, v_dir) -> guid
AddRailRevSrf(profile, rail, axis, scale_height=False) -> guid
*AddRevSrf(curve_id, axis, start_angle=0.0, end_angle=360.0) -> guid  # axis=[point, point]
AddSrfContourCrvs(object_id, points_or_plane, interval=None) -> list[guid]
AddSrfControlPtGrid(count, points, degree=(3,3)) -> guid
AddSrfPt(points) -> guid  # 3 or 4 corner points
AddSrfPtGrid(count, points, degree=(3,3), closed=(False,False)) -> guid
AddSweep1(rail, shapes, closed=False) -> list[guid]
AddSweep2(rails, shapes, closed=False) -> list[guid]
*AddSphere(center_or_plane, radius) -> guid
*AddTorus(base, major_radius, minor_radius, direction=None) -> guid
*BooleanDifference(input0, input1, delete_input=True) -> list[guid]
*BooleanIntersection(input0, input1, delete_input=True) -> list[guid]
*BooleanUnion(input, delete_input=True) -> list[guid]
BrepClosestPoint(object_id, point) -> [point, [float, float], int, vector]
CapPlanarHoles(surface_id) -> bool
ChangeSurfaceDegree(object_id, degree) -> bool  # degree=[u,v]
DuplicateEdgeCurves(object_id, select=False) -> list[guid]
DuplicateSurfaceBorder(surface_id, type=0) -> list[guid]
EvaluateSurface(surface_id, u, v) -> point
ExplodePolysurfaces(object_ids, delete_input=False) -> list[guid]
ExtendSurface(surface_id, parameter, length, smooth=True) -> guid
ExtractIsoCurve(surface_id, parameter, direction) -> list[guid]  # dir: 0=u, 1=v, 2=both
ExtractSurface(object_id, face_indices, copy=False) -> guid
ExtrudeCurve(curve_id, path_id) -> guid  # extrude along a curve
ExtrudeCurvePoint(curve_id, point) -> guid  # extrude to a point
*ExtrudeCurveStraight(curve_id, start_point, end_point) -> guid
ExtrudeSurface(surface, curve, cap=True) -> guid
FilletSurfaces(surface0, surface1, radius, uvparam0=None, uvparam1=None) -> list[guid]
FlipSurface(surface_id, flip=None) -> bool
IntersectBreps(brep1, brep2, tolerance=None) -> [list[guid], list[point]]
IntersectSpheres(sphere_plane0, sphere_radius0, sphere_plane1, sphere_radius1) -> [int, plane, float]
IsBrep(object_id) -> bool
IsCone(object_id) -> bool
IsCylinder(object_id) -> bool
IsPlaneSurface(object_id) -> bool
IsPointInSurface(object_id, point, strictly_in=False, tolerance=None) -> bool
IsPointOnSurface(object_id, point) -> bool
IsPolysurfaceClosed(object_id) -> bool
*IsPolysurface(object_id) -> bool
IsSphere(object_id) -> bool
*IsSurface(object_id) -> bool
IsSurfaceClosed(surface_id, direction) -> bool  # dir: 0=u, 1=v
IsSurfacePeriodic(surface_id, direction) -> bool
IsSurfacePlanar(surface_id, tolerance=None) -> bool
IsSurfaceRational(surface_id) -> bool
IsSurfaceSingular(surface_id, direction) -> bool
IsSurfaceTrimmed(surface_id) -> bool
IsTorus(surface_id) -> bool
JoinSurfaces(object_ids, delete_input=False, return_all=False) -> guid|list[guid]
MakeSurfacePeriodic(surface_id, direction, delete_input=False) -> guid
OffsetSurface(surface_id, distance, tolerance=None, both_sides=False, create_solid=False) -> guid
PullCurve(surface, curve, delete_input=False) -> list[guid]
RebuildSurface(object_id, degree=(3,3), pointcount=(10,10)) -> bool
RemoveSurfaceKnot(surface, uv_parameter, v_direction) -> bool
ReverseSurface(surface_id, direction) -> bool  # dir: 0=u, 1=v, 2=swap
ShootRay(surface_ids, start_point, direction, reflections=10) -> list[point]
ShortPath(surface_id, start_point, end_point) -> guid  # geodesic curve
ShrinkTrimmedSurface(object_id, create_copy=False) -> bool
SplitBrep(brep_id, cutter_id, delete_input=False) -> list[guid]
*SurfaceArea(object_id) -> [float, float]  # [area, error_bound]
SurfaceAreaCentroid(object_id) -> [point, [float, float, float]]
SurfaceAreaMoments(surface_id) -> list  # moments of inertia
SurfaceClosestPoint(surface_id, test_point) -> [float, float]  # [u, v] params
SurfaceCone(surface_id) -> [plane, float, float]  # plane, height, radius
SurfaceCurvature(surface_id, parameter) -> [point, vector, float, float, float, float, float]
SurfaceCylinder(surface_id) -> [plane, float, float]  # plane, height, radius
SurfaceDegree(surface_id, direction=2) -> int|[int, int]  # 2=both
SurfaceDomain(surface_id, direction) -> [float, float]  # dir: 0=u, 1=v
SurfaceEditPoints(surface_id, return_parameters=False, return_all=True) -> list[point]|list[[float, float]]
SurfaceEvaluate(surface_id, parameter, derivative) -> list[vector]
SurfaceFrame(surface_id, uv_parameter) -> plane
SurfaceIsocurveDensity(surface_id, density=None) -> int
SurfaceKnotCount(surface_id) -> [int, int]  # [u_count, v_count]
SurfaceKnots(surface_id) -> [list[float], list[float]]
SurfaceNormal(surface_id, uv_parameter) -> vector
SurfaceNormalizedParameter(surface_id, parameter) -> [float, float]
SurfaceParameter(surface_id, parameter) -> [float, float]
SurfacePointCount(surface_id) -> [int, int]
SurfacePoints(surface_id, return_all=True) -> list[point]
SurfaceSphere(surface_id) -> [plane, float]
SurfaceTorus(surface_id) -> [plane, float, float]
*SurfaceVolume(object_id) -> [float, float]  # [volume, error_bound]
SurfaceVolumeCentroid(object_id) -> [point, [float, float, float]]
SurfaceVolumeMoments(surface_id) -> list
SurfaceWeights(object_id) -> list[float]
TrimBrep(object_id, cutter, tolerance=None) -> list[guid]
TrimSurface(surface_id, direction, interval, delete_input=False) -> guid
UnrollSurface(surface_id, explode=False, following_geometry=None, absolute_tolerance=None, relative_tolerance=None) -> list[guid]

---

## Toolbar (15)
CloseToolbarCollection(name, prompt=False) -> bool
HideToolbar(name, toolbar_group) -> bool
IsToolbar(name, toolbar, group=False) -> bool
IsToolbarCollection(file) -> bool
IsToolbarDocked(name, toolbar_group) -> bool
IsToolbarVisible(name, toolbar_group) -> bool
OpenToolbarCollection(file) -> bool
SaveToolbarCollection(name) -> bool
SaveToolbarCollectionAs(name, file) -> bool
ShowToolbar(name, toolbar_group) -> bool
ToolbarCollectionCount() -> int
ToolbarCollectionNames() -> list[str]
ToolbarCollectionPath(name) -> str
ToolbarCount(name, groups=False) -> int
ToolbarNames(name, groups=False) -> list[str]

---

## Transformation (25)
IsXformIdentity(xform) -> bool
IsXformSimilarity(xform) -> int  # 0=IsNot,1=IsOrient,2=IsSimilar
IsXformZero(xform) -> bool
XformCPlaneToWorld(point, plane) -> point
XformChangeBasis(initial_plane, final_plane) -> xform
XformChangeBasis2(x0, y0, z0, x1, y1, z1) -> xform
XformCompare(xform1, xform2) -> int
XformDeterminant(xform) -> float
XformDiagonal(diagonal_value) -> xform
XformIdentity() -> xform
XformInverse(xform) -> xform
XformMirror(mirror_plane_point, mirror_plane_normal) -> xform
XformMultiply(xform1, xform2) -> xform
XformPlanarProjection(plane) -> xform
XformRotation1(initial_plane, final_plane) -> xform
XformRotation2(angle_degrees, rotation_axis, center_point) -> xform
XformRotation3(start_direction, end_direction, center_point) -> xform
XformRotation4(x0, y0, z0, x1, y1, z1) -> xform
XformScale(scale, point=None) -> xform  # scale=[sx,sy,sz] or float
XformScreenToWorld(point, view=None, screen_coordinates=False) -> point
XformShear(plane, x, y, z) -> xform
XformTranslation(vector) -> xform
XformWorldToCPlane(point, plane) -> point
XformWorldToScreen(point, view=None, screen_coordinates=False) -> point
XformZero() -> xform

---

## Userdata (12)
DeleteDocumentData(section=None, entry=None) -> bool
DocumentDataCount() -> int
DocumentUserTextCount() -> int
GetDocumentData(section=None, entry=None) -> list[str]|str
GetDocumentUserText(key=None) -> str|list[str]
GetUserText(object_id, key=None, attached_to_geometry=False) -> str|list[str]
IsDocumentData() -> bool
IsDocumentUserText() -> bool
IsUserText(object_id) -> bool
SetDocumentData(section, entry, value) -> bool
SetDocumentUserText(key, value=None) -> bool
SetUserText(object_id, key, value=None, attach_to_geometry=False) -> bool

---

## Userinterface (38)
BrowseForFolder(folder=None, message=None, title=None) -> str
CheckListBox(items, message=None, title=None) -> list[bool]
ComboListBox(items, message=None, title=None) -> str
EditBox(default_string=None, message=None, title=None) -> str
GetAngle(point=None, reference_point=None, default_angle_degrees=0, message=None) -> float
GetBoolean(message, items, defaults) -> list[bool]
GetBox(mode=0, base_point=None, prompt1=None, prompt2=None, prompt3=None) -> list[point]
GetColor(color=[0,0,0]) -> color
GetCursorPos() -> point
GetDistance(first_pt=None, distance=None, first_pt_msg='First distance point', second_pt_msg='Second distance point') -> float
GetEdgeCurves(message=None, min_count=1, max_count=0, select=False) -> list[[guid, bool, int, point]]
GetInteger(message=None, number=None, minimum=None, maximum=None) -> int
GetLayer(title="Select Layer", layer=None, show_new_button=False, show_set_current=False) -> str
GetLayers(title="Select Layers", show_new_button=False) -> list[str]
GetLine(mode=0, point=None, message1=None, message2=None, message3=None) -> [point, point]
GetLinetype(default_linetype=None, show_by_layer=False) -> str
GetMeshFaces(object_id, message="", min_count=1, max_count=0) -> list[int]
GetMeshVertices(object_id, message="", min_count=1, max_count=0) -> list[int]
GetPoint(message=None, base_point=None, distance=None, in_plane=False) -> point
GetPointOnCurve(curve_id, message=None) -> point
GetPointOnMesh(mesh_id, message=None) -> point
GetPointOnSurface(surface_id, message=None) -> point
GetPoints(draw_lines=False, in_plane=False, message1=None, message2=None, max_points=None, base_point=None) -> list[point]
GetPolyline(flags=3, message1=None, message2=None, message3=None, message4=None, min=2, max=0) -> list[point]
GetReal(message="Number", number=None, minimum=None, maximum=None) -> float
GetRectangle(mode=0, base_point=None, prompt1=None, prompt2=None, prompt3=None) -> [point, point, point, point]
GetString(message=None, defaultString=None, strings=None) -> str
ListBox(items, message=None, title=None, default=None) -> str
MessageBox(message, buttons=0, title="") -> int
MultiListBox(items, message=None, title=None, defaults=None) -> list[str]
OpenFileName(title=None, filter=None, folder=None, filename=None, extension=None) -> str
OpenFileNames(title=None, filter=None, folder=None, filename=None, extension=None) -> list[str]
PopupMenu(items, modes=None, point=None, view=None) -> int
PropertyListBox(items, values, message=None, title=None) -> list[str]
RealBox(message="", default_number=None, title="", minimum=None, maximum=None) -> float
SaveFileName(title=None, filter=None, folder=None, filename=None, extension=None) -> str
StringBox(message=None, default_value=None, title=None) -> str
TextOut(message=None, title=None) -> None

---

## Utility (27)
Angle(point1, point2, plane=True) -> float  # degrees
Angle2(line1, line2) -> [float, float]  # [acute, reflex]
ClipboardText(text=None) -> str
ColorAdjustLuma(rgb, luma, scale=False) -> color
ColorBlueValue(rgb) -> int
ColorGreenValue(rgb) -> int
ColorHLSToRGB(hls) -> color
ColorRGBToHLS(rgb) -> [float, float, float]
ColorRedValue(rgb) -> int
ContextIsGrasshopper() -> bool
ContextIsRhino() -> bool
CreateColor(color, g=None, b=None, a=None) -> color
CreateInterval(interval, y=None) -> interval
CreatePlane(plane_or_origin, x_axis=None, y_axis=None, ignored=None) -> plane
CreatePoint(point, y=None, z=None) -> point
CreateVector(vector, y=None, z=None) -> vector
CreateXform(xform) -> xform
CullDuplicateNumbers(numbers, tolerance=None) -> list[float]
CullDuplicatePoints(points, tolerance=-1) -> list[point]
*Distance(point1, point2) -> float|list[float]
GetSettings(filename, section=None, entry=None) -> str
Polar(point, angle_degrees, distance, plane=None) -> point
SimplifyArray(points) -> list[float]  # flatten [point,...] to [x,y,z,x,y,z,...]
Sleep(milliseconds) -> None
SortPointList(points, tolerance=None) -> list[point]
SortPoints(points, ascending=True, order=0) -> list[point]
Str2Pt(point) -> point

---

## View (56)
AddDetail(layout_id, corner1, corner2, title=None, projection=1) -> guid
AddLayout(title=None, size=None) -> str
AddNamedCPlane(cplane_name, view=None) -> str
AddNamedView(name, view=None) -> str
CurrentDetail(layout, detail=None, return_name=True) -> str
CurrentView(view=None, return_name=True) -> str
DeleteNamedCPlane(name) -> bool
DeleteNamedView(name) -> bool
DetailLock(detail_id, lock=None) -> bool
DetailScale(detail_id, model_length=None, page_length=None) -> float
IsDetail(layout, detail) -> bool
IsLayout(layout) -> bool
IsView(view) -> bool
IsViewCurrent(view) -> bool
IsViewMaximized(view=None) -> bool
IsViewPerspective(view) -> bool
IsViewTitleVisible(view=None) -> bool
IsWallpaper(view) -> bool
MaximizeRestoreView(view=None) -> None
NamedCPlane(name) -> plane
NamedCPlanes() -> list[str]
NamedViews() -> list[str]
RenameView(old_title, new_title) -> str
RestoreNamedCPlane(cplane_name, view=None) -> str
RestoreNamedView(named_view, view=None, restore_bitmap=False) -> str
RotateCamera(view=None, direction=0, angle=None) -> None
RotateView(view=None, direction=0, angle=None) -> None
ShowGrid(view=None, show=None) -> bool
ShowGridAxes(view=None, show=None) -> bool
ShowViewTitle(view=None, show=True) -> None
ShowWorldAxes(view=None, show=None) -> bool
TiltView(view=None, direction=0, angle=None) -> None
ViewCPlane(view=None, plane=None) -> plane
ViewCamera(view=None, camera_location=None) -> point
ViewCameraLens(view=None, length=None) -> float
ViewCameraPlane(view=None) -> plane
ViewCameraTarget(view=None, camera=None, target=None) -> [point, point]
ViewCameraUp(view=None, up_vector=None) -> vector
ViewDisplayMode(view=None, mode=None, return_name=True) -> str
ViewDisplayModeId(name) -> str
ViewDisplayModeName(mode_id) -> str
ViewDisplayModes(return_names=True) -> list[str]
ViewNames(return_names=True, view_type=0) -> list[str]
ViewNearCorners(view=None) -> [point, point, point, point]
ViewProjection(view=None, mode=None) -> int  # 1=parallel, 2=perspective
ViewRadius(view=None, radius=None, mode=False) -> float
ViewSize(view=None) -> [int, int]
ViewSpeedTest(view=None, frames=100, freeze=True, direction=0, angle_degrees=5) -> str
ViewTarget(view=None, target=None) -> point
ViewTitle(view_id) -> str
Wallpaper(view=None, filename=None) -> str
WallpaperGrayScale(view=None, grayscale=None) -> bool
WallpaperHidden(view=None, hidden=None) -> bool
ZoomBoundingBox(bounding_box, view=None, all=False) -> None
ZoomExtents(view=None, all=False) -> None
ZoomSelected(view=None, all=False) -> None

---

*Source: https://developer.rhino3d.com/api/RhinoScriptSyntax/*
