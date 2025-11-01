# RhinoScriptSyntax Implementation Status

## Our MCP High-Level Tools (50 total):
1. get_scene_info
2. get_selected_objects
3. create_point
4. create_line
5. create_circle
6. create_arc
7. create_ellipse
8. create_polyline
9. create_curve
10. create_box
11. create_sphere
12. create_cylinder
13. create_cone
14. create_torus
15. move_objects
16. rotate_objects
17. scale_objects
18. mirror_objects
19. copy_objects
20. array_linear
21. boolean_union
22. boolean_difference
23. boolean_intersection
24. join_curves
25. explode_curves
26. offset_curve
27. fillet_curves
28. extend_curve
29. extrude_curve_straight
30. revolve_curve
31. loft_curves
32. create_layer
33. delete_layer
34. set_current_layer
35. set_layer_color
36. set_layer_visibility
37. list_layers
38. measure_distance
39. measure_curve_length
40. measure_area
41. measure_volume
42. set_object_name
43. set_object_color
44. set_object_layer
45. select_all
46. select_by_type
47. select_by_layer
48. unselect_all
49. delete_selected
50. execute_python_code

## application
- [ ] AddAlias
- [ ] AddSearchPath
- [ ] AliasCount
- [ ] AliasMacro
- [ ] AliasNames
- [ ] AppearanceColor
- [ ] AutosaveFile
- [ ] AutosaveInterval
- [ ] BuildDate
- [ ] ClearCommandHistory
- [ ] Command
- [ ] CommandHistory
- [ ] DefaultRenderer
- [ ] DeleteAlias
- [ ] DeleteSearchPath
- [ ] DisplayOleAlerts
- [ ] EdgeAnalysisColor
- [ ] EdgeAnalysisMode
- [ ] EnableAutosave
- [ ] EnablePlugIn
- [ ] ExeFolder
- [ ] ExePlatform
- [ ] ExeServiceRelease
- [ ] ExeVersion
- [ ] Exit
- [ ] FindFile
- [ ] GetPlugInObject
- [ ] InCommand
- [ ] InstallFolder
- [ ] IsAlias
- [ ] IsCommand
- [ ] IsPlugIn
- [ ] IsRunningOnWindows
- [ ] LastCommandName
- [ ] LastCommandResult
- [ ] LocaleID
- [ ] Ortho
- [ ] Osnap
- [ ] OsnapDialog
- [ ] OsnapMode
- [ ] Planar
- [ ] PlugInId
- [ ] PlugIns
- [ ] ProjectOsnaps
- [ ] Prompt
- [ ] ScreenSize
- [ ] SdkVersion
- [ ] SearchPathCount
- [ ] SearchPathList
- [ ] SendKeystrokes
- [ ] Snap
- [ ] StatusBarDistance
- [ ] StatusBarMessage
- [ ] StatusBarPoint
- [ ] StatusBarProgressMeterShow
- [ ] StatusBarProgressMeterUpdate
- [ ] StatusBarProgressMeterHide
- [ ] TemplateFile
- [ ] TemplateFolder
- [ ] WindowHandle
- [ ] WorkingFolder

## block
- [ ] AddBlock
- [ ] BlockContainerCount
- [ ] BlockContainers
- [ ] BlockCount
- [ ] BlockDescription
- [ ] BlockInstanceCount
- [ ] BlockInstanceInsertPoint
- [ ] BlockInstanceName
- [ ] BlockInstances
- [ ] BlockInstanceXform
- [ ] BlockNames
- [ ] BlockObjectCount
- [ ] BlockObjects
- [ ] BlockPath
- [ ] BlockStatus
- [ ] DeleteBlock
- [ ] ExplodeBlockInstance
- [ ] InsertBlock
- [ ] InsertBlock2
- [ ] IsBlock
- [ ] IsBlockEmbedded
- [ ] IsBlockInstance
- [ ] IsBlockInUse
- [ ] IsBlockReference
- [ ] RenameBlock

## curve
- [ ] AddArc
- [x] **AddArc3Pt** (used in create_arc)
- [ ] AddArcPtTanPt
- [ ] AddBlendCurve
- [x] **AddCircle** (used in create_circle)
- [ ] AddCircle3Pt
- [ ] AddCurve
- [x] **AddEllipse** (used in create_ellipse)
- [ ] AddEllipse3Pt
- [ ] AddFilletCurve
- [ ] AddInterpCrvOnSrf
- [ ] AddInterpCrvOnSrfUV
- [x] **AddInterpCurve** (used in create_curve)
- [x] **AddLine** (used in create_line, revolve_curve)
- [ ] AddNurbsCurve
- [x] **AddPolyline** (used in create_polyline)
- [ ] AddRectangle
- [ ] AddSpiral
- [ ] AddSubCrv
- [ ] ArcAngle
- [ ] ArcCenterPoint
- [ ] ArcMidPoint
- [ ] ArcRadius
- [ ] CircleCenterPoint
- [ ] CircleCircumference
- [ ] CircleRadius
- [ ] CloseCurve
- [ ] ClosedCurveOrientation
- [ ] ConvertCurveToPolyline
- [ ] CurveArcLengthPoint
- [x] **CurveArea** (used in measure_area)
- [ ] CurveAreaCentroid
- [ ] CurveArrows
- [ ] CurveBooleanDifference
- [ ] CurveBooleanIntersection
- [ ] CurveBooleanUnion
- [ ] CurveBrepIntersect
- [ ] CurveClosestObject
- [ ] CurveClosestPoint
- [ ] CurveContourPoints
- [ ] CurveCurvature
- [ ] CurveCurveIntersection
- [ ] CurveDegree
- [ ] CurveDeviation
- [ ] CurveDim
- [ ] CurveDirectionsMatch
- [ ] CurveDiscontinuity
- [ ] CurveDomain
- [ ] CurveEditPoints
- [ ] CurveEndPoint
- [ ] CurveFilletPoints
- [ ] CurveFrame
- [ ] CurveKnotCount
- [ ] CurveKnots
- [x] **CurveLength** (used in measure_curve_length)
- [ ] CurveMidPoint
- [ ] CurveNormal
- [ ] CurveNormalizedParameter
- [ ] CurveParameter
- [ ] CurvePerpFrame
- [ ] CurvePlane
- [ ] CurvePointCount
- [ ] CurvePoints
- [ ] CurveRadius
- [ ] CurveSeam
- [ ] CurveStartPoint
- [ ] CurveSurfaceIntersection
- [ ] CurveTangent
- [ ] CurveWeights
- [ ] DivideCurve
- [ ] DivideCurveEquidistant
- [ ] DivideCurveLength
- [ ] EllipseCenterPoint
- [ ] EllipseQuadPoints
- [ ] EvaluateCurve
- [x] **ExplodeCurves** (used in explode_curves)
- [ ] ExtendCurve
- [x] **ExtendCurveLength** (used in extend_curve)
- [ ] ExtendCurvePoint
- [ ] FairCurve
- [ ] FitCurve
- [ ] InsertCurveKnot
- [ ] IsArc
- [ ] IsCircle
- [x] **IsCurve** (used in multiple functions)
- [ ] IsCurveClosable
- [x] **IsCurveClosed** (used in measure_area)
- [ ] IsCurveInPlane
- [ ] IsCurveLinear
- [ ] IsCurvePeriodic
- [x] **IsCurvePlanar** (used in measure_area)
- [ ] IsCurveRational
- [ ] IsEllipse
- [ ] IsLine
- [ ] IsPointOnCurve
- [ ] IsPolyCurve
- [ ] IsPolyline
- [x] **JoinCurves** (used in join_curves)
- [ ] LineFitFromPoints
- [ ] MakeCurveNonPeriodic
- [ ] MeanCurve
- [ ] MeshPolyline
- [x] **OffsetCurve** (used in offset_curve)
- [ ] OffsetCurveOnSurface
- [ ] PlanarClosedCurveContainment
- [ ] PlanarCurveCollision
- [ ] PointInPlanarClosedCurve
- [ ] PolyCurveCount
- [ ] PolylineVertices
- [ ] ProjectCurveToMesh
- [ ] ProjectCurveToSurface
- [ ] RebuildCurve
- [ ] RemoveCurveKnot
- [ ] ReverseCurve
- [ ] SimplifyCurve
- [ ] SplitCurve
- [ ] TrimCurve
- [ ] ChangeCurveDegree
- [ ] AddTweenCurves

## dimension
- [ ] AddAlignedDimension
- [ ] AddDimStyle
- [ ] AddLeader
- [ ] AddLinearDimension
- [ ] CurrentDimStyle
- [ ] DeleteDimStyle
- [ ] DimensionStyle
- [ ] DimensionText
- [ ] DimensionUserText
- [ ] DimensionValue
- [ ] DimStyleAnglePrecision
- [ ] DimStyleArrowSize
- [ ] DimStyleCount
- [ ] DimStyleExtension
- [ ] DimStyleFont
- [ ] DimStyleLeaderArrowSize
- [ ] DimStyleLengthFactor
- [ ] DimStyleLinearPrecision
- [ ] DimStyleNames
- [ ] DimStyleNumberFormat
- [ ] DimStyleOffset
- [ ] DimStylePrefix
- [ ] DimStyleScale
- [ ] DimStyleSuffix
- [ ] DimStyleTextAlignment
- [ ] DimStyleTextGap
- [ ] DimStyleTextHeight
- [ ] IsAlignedDimension
- [ ] IsAngularDimension
- [ ] IsDiameterDimension
- [ ] IsDimension
- [ ] IsDimStyle
- [ ] IsDimStyleReference
- [ ] IsLeader
- [ ] IsLinearDimension
- [ ] IsOrdinateDimension
- [ ] IsRadialDimension
- [ ] LeaderText
- [ ] RenameDimStyle

## document
- [ ] CreatePreviewImage
- [ ] DocumentModified
- [ ] DocumentName
- [ ] DocumentPath
- [ ] EnableRedraw
- [ ] ExtractPreviewImage
- [ ] IsDocumentModified
- [ ] Notes
- [ ] ReadFileVersion
- [x] **Redraw** (used in all creation/modification functions)
- [ ] RenderAntialias
- [ ] RenderColor
- [ ] RenderResolution
- [ ] RenderMeshDensity
- [ ] RenderMeshMaxAngle
- [ ] RenderMeshMaxAspectRatio
- [ ] RenderMeshMaxDistEdgeToSrf
- [ ] RenderMeshMaxEdgeLength
- [ ] RenderMeshMinEdgeLength
- [ ] RenderMeshMinInitialGridQuads
- [ ] RenderMeshQuality
- [ ] RenderMeshSettings
- [ ] RenderSettings
- [ ] UnitAbsoluteTolerance
- [ ] UnitAngleTolerance
- [ ] UnitDistanceDisplayPrecision
- [ ] UnitRelativeTolerance
- [ ] UnitScale
- [ ] UnitSystem
- [x] **UnitSystemName** (used in get_scene_info)

## geometry
- [ ] AddClippingPlane
- [ ] AddPictureFrame
- [x] **AddPoint** (used in create_point)
- [ ] AddPointCloud
- [ ] AddPoints
- [ ] AddText
- [ ] AddTextDot
- [ ] Area
- [x] **BoundingBox** (used in get_selected_objects, get_scene_info, offset_curve)
- [ ] CompareGeometry
- [ ] ExplodeText
- [ ] IsClippingPlane
- [ ] IsPoint
- [ ] IsPointCloud
- [ ] IsText
- [ ] IsTextDot
- [ ] PointCloudCount
- [ ] PointCloudHasHiddenPoints
- [ ] PointCloudHasPointColors
- [ ] PointCloudHidePoints
- [ ] PointCloudPointColors
- [ ] PointCloudPoints
- [ ] PointCloudKNeighbors
- [ ] PointCloudClosestPoints
- [ ] PointCoordinates
- [ ] TextDotFont
- [ ] TextDotHeight
- [ ] TextDotPoint
- [ ] TextDotText
- [ ] TextObjectFont
- [ ] TextObjectHeight
- [ ] TextObjectPlane
- [ ] TextObjectPoint
- [ ] TextObjectStyle
- [ ] TextObjectText

## grips
- [ ] EnableObjectGrips
- [ ] GetObjectGrip
- [ ] GetObjectGrips
- [ ] NextObjectGrip
- [ ] ObjectGripCount
- [ ] ObjectGripLocation
- [ ] ObjectGripLocations
- [ ] ObjectGripsOn
- [ ] ObjectGripsSelected
- [ ] PrevObjectGrip
- [ ] SelectedObjectGrips
- [ ] SelectObjectGrip
- [ ] SelectObjectGrips
- [ ] UnselectObjectGrip
- [ ] UnselectObjectGrips

## group
- [ ] AddGroup
- [ ] AddObjectsToGroup
- [ ] AddObjectToGroup
- [ ] DeleteGroup
- [ ] GroupCount
- [ ] GroupNames
- [ ] HideGroup
- [ ] IsGroup
- [ ] IsGroupEmpty
- [ ] LockGroup
- [ ] RemoveObjectFromAllGroups
- [ ] RemoveObjectFromGroup
- [ ] RemoveObjectsFromGroup
- [ ] RenameGroup
- [ ] ShowGroup
- [ ] UnlockGroup
- [ ] ObjectTopGroup

## hatch
- [ ] AddHatch
- [ ] AddHatches
- [ ] AddHatchPatterns
- [ ] CurrentHatchPattern
- [ ] ExplodeHatch
- [ ] HatchPattern
- [ ] HatchPatternCount
- [ ] HatchPatternDescription
- [ ] HatchPatternFillType
- [ ] HatchPatternNames
- [ ] HatchRotation
- [ ] HatchScale
- [ ] IsHatch
- [ ] IsHatchPattern
- [ ] IsHatchPatternCurrent
- [ ] IsHatchPatternReference

## layer
- [x] **AddLayer** (used in create_layer)
- [x] **CurrentLayer** (used in set_current_layer, list_layers)
- [x] **DeleteLayer** (used in delete_layer)
- [ ] ExpandLayer
- [x] **IsLayer** (used in create_layer, delete_layer, set_current_layer, set_layer_color, set_layer_visibility, set_object_layer)
- [ ] IsLayerChangeable
- [ ] IsLayerChildOf
- [ ] IsLayerCurrent
- [ ] IsLayerEmpty
- [ ] IsLayerExpanded
- [x] **LayerLocked** (used in list_layers)
- [ ] IsLayerOn
- [ ] IsLayerSelectable
- [ ] IsLayerParentOf
- [ ] IsLayerReference
- [ ] IsLayerVisible
- [ ] LayerChildCount
- [ ] LayerChildren
- [x] **LayerColor** (used in set_layer_color)
- [ ] LayerCount
- [ ] LayerIds
- [ ] LayerLinetype
- [ ] LayerMaterialIndex
- [ ] LayerId
- [ ] LayerName
- [x] **LayerNames** (used in list_layers, get_scene_info)
- [ ] LayerOrder
- [ ] LayerPrintColor
- [ ] LayerPrintWidth
- [x] **LayerVisible** (used in set_layer_visibility, list_layers)
- [ ] ParentLayer
- [ ] PurgeLayer
- [ ] RenameLayer

## light
- [ ] AddDirectionalLight
- [ ] AddLinearLight
- [ ] AddPointLight
- [ ] AddRectangularLight
- [ ] AddSpotLight
- [ ] EnableLight
- [ ] IsDirectionalLight
- [ ] IsLight
- [ ] IsLightEnabled
- [ ] IsLightReference
- [ ] IsLinearLight
- [ ] IsPointLight
- [ ] IsRectangularLight
- [ ] IsSpotLight
- [ ] LightColor
- [ ] LightCount
- [ ] LightDirection
- [ ] LightLocation
- [ ] LightName
- [ ] LightObjects
- [ ] RectangularLightPlane
- [ ] SpotLightHardness
- [ ] SpotLightRadius
- [ ] SpotLightShadowIntensity

## line
- [ ] LineClosestPoint
- [ ] LineCylinderIntersection
- [ ] LineIsFartherThan
- [ ] LineLineIntersection
- [ ] LineMaxDistanceTo
- [ ] LineMinDistanceTo
- [ ] LinePlane
- [ ] LinePlaneIntersection
- [ ] LineSphereIntersection
- [ ] LineTransform

## linetype
- [ ] IsLinetype
- [ ] IsLinetypeReference
- [ ] LinetypeCount
- [ ] LinetypeNames

## material
- [ ] AddMaterialToLayer
- [ ] AddMaterialToObject
- [ ] CopyMaterial
- [ ] IsMaterialDefault
- [ ] IsMaterialReference
- [ ] MatchMaterial
- [ ] MaterialBump
- [ ] MaterialColor
- [ ] MaterialEnvironmentMap
- [ ] MaterialName
- [ ] MaterialReflectiveColor
- [ ] MaterialShine
- [ ] MaterialTexture
- [ ] MaterialTransparency
- [ ] MaterialTransparencyMap
- [ ] ResetMaterial

## mesh
- [ ] AddMesh
- [ ] AddPlanarMesh
- [ ] CurveMeshIntersection
- [ ] DisjointMeshCount
- [ ] DuplicateMeshBorder
- [ ] ExplodeMeshes
- [ ] IsMesh
- [ ] IsMeshClosed
- [ ] IsMeshManifold
- [ ] IsPointOnMesh
- [ ] JoinMeshes
- [ ] MeshArea
- [ ] MeshAreaCentroid
- [ ] MeshBooleanDifference
- [ ] MeshBooleanIntersection
- [ ] MeshBooleanSplit
- [ ] MeshBooleanUnion
- [ ] MeshClosestPoint
- [ ] MeshFaceCenters
- [ ] MeshFaceCount
- [ ] MeshFaceNormals
- [ ] MeshFaces
- [ ] MeshFaceVertices
- [ ] MeshHasFaceNormals
- [ ] MeshHasTextureCoordinates
- [ ] MeshHasVertexColors
- [ ] MeshHasVertexNormals
- [ ] MeshMeshIntersection
- [ ] MeshNakedEdgePoints
- [ ] MeshOffset
- [ ] MeshOutline
- [ ] MeshQuadCount
- [ ] MeshQuadsToTriangles
- [ ] MeshToNurb
- [ ] MeshTriangleCount
- [ ] MeshVertexColors
- [ ] MeshVertexCount
- [ ] MeshVertexFaces
- [ ] MeshVertexNormals
- [ ] MeshVertices
- [ ] MeshVolume
- [ ] MeshVolumeCentroid
- [ ] PullCurveToMesh
- [ ] SplitDisjointMesh
- [ ] UnifyMeshNormals

## object
- [x] **CopyObject** (used in copy_objects, array_linear)
- [ ] CopyObjects
- [x] **DeleteObject** (used in revolve_curve - to delete temp axis line)
- [x] **DeleteObjects** (used in delete_selected)
- [ ] FlashObject
- [ ] HideObject
- [ ] HideObjects
- [ ] IsLayoutObject
- [ ] IsObject
- [ ] IsObjectHidden
- [ ] IsObjectInBox
- [ ] IsObjectInGroup
- [ ] IsObjectLocked
- [ ] IsObjectNormal
- [ ] IsObjectReference
- [ ] IsObjectSelectable
- [ ] IsObjectSelected
- [ ] IsObjectSolid
- [ ] IsObjectValid
- [ ] IsVisibleInView
- [ ] LockObject
- [ ] LockObjects
- [ ] MatchObjectAttributes
- [x] **MirrorObject** (used in mirror_objects)
- [ ] MirrorObjects
- [x] **MoveObject** (used in move_objects)
- [ ] MoveObjects
- [x] **ObjectColor** (used in set_object_color)
- [ ] ObjectColorSource
- [ ] ObjectDescription
- [ ] ObjectGroups
- [x] **ObjectLayer** (used in set_object_layer, get_selected_objects, get_scene_info)
- [ ] ObjectLayout
- [ ] ObjectLinetype
- [ ] ObjectLinetypeSource
- [ ] ObjectMaterialIndex
- [ ] ObjectMaterialSource
- [x] **ObjectName** (used in set_object_name, get_selected_objects)
- [ ] ObjectPrintColor
- [ ] ObjectPrintColorSource
- [ ] ObjectPrintWidth
- [ ] ObjectPrintWidthSource
- [x] **ObjectType** (used in get_selected_objects, get_scene_info)
- [ ] OrientObject
- [ ] RotateObject
- [x] **RotateObjects** (used in rotate_objects)
- [x] **ScaleObject** (used in scale_objects)
- [ ] ScaleObjects
- [ ] SelectObject
- [x] **SelectObjects** (used in select_all, select_by_type, select_by_layer)
- [ ] ShearObject
- [ ] ShearObjects
- [ ] ShowObject
- [ ] ShowObjects
- [ ] TransformObject
- [ ] TransformObjects
- [ ] UnlockObject
- [ ] UnlockObjects
- [ ] UnselectObject
- [ ] UnselectObjects

## plane
- [ ] DistanceToPlane
- [ ] EvaluatePlane
- [ ] IntersectPlanes
- [ ] MovePlane
- [ ] PlaneClosestPoint
- [ ] PlaneCurveIntersection
- [ ] PlaneEquation
- [ ] PlaneFitFromPoints
- [ ] PlaneFromFrame
- [x] **PlaneFromNormal** (used in create_ellipse, create_cylinder, create_cone, create_torus, create_arc)
- [ ] PlaneFromPoints
- [ ] PlanePlaneIntersection
- [ ] PlaneSphereIntersection
- [ ] PlaneTransform
- [ ] RotatePlane
- [ ] WorldXYPlane
- [ ] WorldYZPlane
- [ ] WorldZXPlane

## pointvector
- [ ] IsVectorParallelTo
- [ ] IsVectorPerpendicularTo
- [ ] IsVectorTiny
- [ ] IsVectorZero
- [ ] PointAdd
- [ ] PointArrayClosestPoint
- [ ] PointArrayTransform
- [ ] PointClosestObject
- [ ] PointCompare
- [ ] PointDivide
- [ ] PointsAreCoplanar
- [ ] PointScale
- [ ] PointSubtract
- [ ] PointTransform
- [ ] ProjectPointToMesh
- [ ] ProjectPointToSurface
- [ ] PullPoints
- [ ] VectorAdd
- [ ] VectorAngle
- [ ] VectorCompare
- [ ] VectorCreate
- [ ] VectorCrossProduct
- [ ] VectorDivide
- [ ] VectorDotProduct
- [ ] VectorLength
- [ ] VectorMultiply
- [ ] VectorReverse
- [ ] VectorRotate
- [ ] VectorScale
- [ ] VectorSubtract
- [ ] VectorTransform
- [ ] VectorUnitize
- [ ] PointArrayBoundingBox

## selection
- [x] **AllObjects** (used in get_scene_info, select_all)
- [ ] FirstObject
- [ ] GetCurveObject
- [ ] GetObject
- [ ] GetObjectEx
- [ ] GetObjects
- [ ] GetObjectsEx
- [ ] GetPointCoordinates
- [ ] GetSurfaceObject
- [ ] LockedObjects
- [ ] HiddenObjects
- [ ] InvertSelectedObjects
- [ ] LastCreatedObjects
- [ ] LastObject
- [ ] NextObject
- [ ] NormalObjects
- [ ] ObjectsByColor
- [ ] ObjectsByGroup
- [x] **ObjectsByLayer** (used in select_by_layer)
- [ ] ObjectsByName
- [x] **ObjectsByType** (used in select_by_type)
- [x] **SelectedObjects** (used in all transformation, boolean, curve, surface operations)
- [x] **UnselectAllObjects** (used in unselect_all)
- [ ] VisibleObjects
- [ ] WindowPick

## surface
- [x] **AddBox** (used in create_box)
- [x] **AddCone** (used in create_cone)
- [ ] AddCutPlane
- [ ] AddCylinder
- [ ] AddEdgeSrf
- [ ] AddNetworkSrf
- [ ] AddNurbsSurface
- [ ] AddPatch
- [ ] AddPipe
- [ ] AddPlanarSrf
- [ ] AddPlaneSurface
- [x] **AddLoftSrf** (used in loft_curves)
- [x] **AddRevSrf** (used in revolve_curve)
- [x] **AddSphere** (used in create_sphere)
- [ ] AddSrfContourCrvs
- [ ] AddSrfControlPtGrid
- [ ] AddSrfPt
- [ ] AddSrfPtGrid
- [ ] AddSweep1
- [ ] AddSweep2
- [ ] AddRailRevSrf
- [x] **AddTorus** (used in create_torus)
- [x] **BooleanDifference** (used in boolean_difference)
- [x] **BooleanIntersection** (used in boolean_intersection)
- [x] **BooleanUnion** (used in boolean_union)
- [ ] BrepClosestPoint
- [ ] CapPlanarHoles
- [ ] DuplicateEdgeCurves
- [ ] DuplicateSurfaceBorder
- [ ] EvaluateSurface
- [ ] ExtendSurface
- [ ] ExplodePolysurfaces
- [ ] ExtractIsoCurve
- [ ] ExtractSurface
- [ ] ExtrudeCurve
- [ ] ExtrudeCurvePoint
- [x] **ExtrudeCurveStraight** (used in extrude_curve_straight, create_cylinder)
- [ ] ExtrudeSurface
- [ ] FilletSurfaces
- [ ] FlipSurface
- [ ] IntersectBreps
- [ ] IntersectSpheres
- [ ] IsBrep
- [ ] IsCone
- [ ] IsCylinder
- [ ] IsPlaneSurface
- [ ] IsPointInSurface
- [ ] IsPointOnSurface
- [x] **IsPolysurface** (used in boolean operations)
- [ ] IsPolysurfaceClosed
- [ ] IsSphere
- [x] **IsSurface** (used in boolean operations)
- [ ] IsSurfaceClosed
- [ ] IsSurfacePeriodic
- [ ] IsSurfacePlanar
- [ ] IsSurfaceRational
- [ ] IsSurfaceSingular
- [ ] IsSurfaceTrimmed
- [ ] IsTorus
- [ ] SurfaceSphere
- [ ] JoinSurfaces
- [ ] MakeSurfacePeriodic
- [ ] OffsetSurface
- [ ] PullCurve
- [ ] RebuildSurface
- [ ] RemoveSurfaceKnot
- [ ] ReverseSurface
- [ ] ShootRay
- [ ] ShortPath
- [ ] ShrinkTrimmedSurface
- [ ] SplitBrep
- [x] **SurfaceArea** (used in measure_area)
- [ ] SurfaceAreaCentroid
- [ ] SurfaceAreaMoments
- [ ] SurfaceClosestPoint
- [ ] SurfaceCone
- [ ] SurfaceCurvature
- [ ] SurfaceCylinder
- [ ] SurfaceDegree
- [ ] SurfaceDomain
- [ ] SurfaceEditPoints
- [ ] SurfaceEvaluate
- [ ] SurfaceFrame
- [ ] SurfaceIsocurveDensity
- [ ] SurfaceKnotCount
- [ ] SurfaceKnots
- [ ] SurfaceNormal
- [ ] SurfaceNormalizedParameter
- [ ] SurfaceParameter
- [ ] SurfacePointCount
- [ ] SurfacePoints
- [ ] SurfaceTorus
- [x] **SurfaceVolume** (used in measure_volume)
- [ ] SurfaceVolumeCentroid
- [ ] SurfaceVolumeMoments
- [ ] SurfaceWeights
- [ ] TrimBrep
- [ ] TrimSurface
- [ ] UnrollSurface
- [ ] ChangeSurfaceDegree

## toolbar
- [ ] CloseToolbarCollection
- [ ] HideToolbar
- [ ] IsToolbar
- [ ] IsToolbarCollection
- [ ] IsToolbarDocked
- [ ] IsToolbarVisible
- [ ] OpenToolbarCollection
- [ ] SaveToolbarCollection
- [ ] SaveToolbarCollectionAs
- [ ] ShowToolbar
- [ ] ToolbarCollectionCount
- [ ] ToolbarCollectionNames
- [ ] ToolbarCollectionPath
- [ ] ToolbarCount
- [ ] ToolbarNames

## transformation
- [ ] IsXformIdentity
- [ ] IsXformSimilarity
- [ ] IsXformZero
- [ ] XformChangeBasis
- [ ] XformChangeBasis2
- [ ] XformCompare
- [ ] XformCPlaneToWorld
- [ ] XformDeterminant
- [ ] XformDiagonal
- [ ] XformIdentity
- [ ] XformInverse
- [ ] XformMirror
- [ ] XformMultiply
- [ ] XformPlanarProjection
- [ ] XformRotation1
- [ ] XformRotation2
- [ ] XformRotation3
- [ ] XformRotation4
- [ ] XformScale
- [ ] XformScreenToWorld
- [ ] XformShear
- [ ] XformTranslation
- [ ] XformWorldToCPlane
- [ ] XformWorldToScreen
- [ ] XformZero

## userdata
- [ ] DeleteDocumentData
- [ ] DocumentDataCount
- [ ] DocumentUserTextCount
- [ ] GetDocumentData
- [ ] GetDocumentUserText
- [ ] GetUserText
- [ ] IsDocumentData
- [ ] IsDocumentUserText
- [ ] IsUserText
- [ ] SetDocumentData
- [ ] SetDocumentUserText
- [ ] SetUserText

## userinterface
- [ ] BrowseForFolder
- [ ] CheckListBox
- [ ] ComboListBox
- [ ] EditBox
- [ ] GetAngle
- [ ] GetBoolean
- [ ] GetBox
- [ ] GetColor
- [ ] GetCursorPos
- [ ] GetDistance
- [ ] GetEdgeCurves
- [ ] GetInteger
- [ ] GetLayer
- [ ] GetLayers
- [ ] GetLine
- [ ] GetLinetype
- [ ] GetMeshFaces
- [ ] GetMeshVertices
- [ ] GetPoint
- [ ] GetPointOnCurve
- [ ] GetPointOnMesh
- [ ] GetPointOnSurface
- [ ] GetPoints
- [ ] GetPolyline
- [ ] GetReal
- [ ] GetRectangle
- [ ] GetString
- [ ] ListBox
- [ ] MessageBox
- [ ] PropertyListBox
- [ ] MultiListBox
- [ ] OpenFileName
- [ ] OpenFileNames
- [ ] PopupMenu
- [ ] RealBox
- [ ] SaveFileName
- [ ] StringBox
- [ ] TextOut

## utility
- [ ] ContextIsRhino
- [ ] ContextIsGrasshopper
- [ ] Angle
- [ ] Angle2
- [ ] ClipboardText
- [ ] ColorAdjustLuma
- [ ] ColorBlueValue
- [ ] ColorGreenValue
- [ ] ColorHLSToRGB
- [ ] ColorRedValue
- [ ] ColorRGBToHLS
- [ ] CullDuplicateNumbers
- [ ] CullDuplicatePoints
- [x] **Distance** (used in measure_distance)
- [ ] GetSettings
- [ ] Polar
- [ ] SimplifyArray
- [ ] Sleep
- [ ] SortPointList
- [ ] SortPoints
- [ ] Str2Pt
- [ ] CreatePoint
- [ ] CreateVector
- [ ] CreatePlane
- [ ] CreateXform
- [ ] CreateColor
- [ ] CreateInterval

## view
- [ ] AddDetail
- [ ] AddLayout
- [ ] AddNamedCPlane
- [ ] AddNamedView
- [ ] CurrentDetail
- [ ] CurrentView
- [ ] DeleteNamedCPlane
- [ ] DeleteNamedView
- [ ] DetailLock
- [ ] DetailScale
- [ ] IsDetail
- [ ] IsLayout
- [ ] IsView
- [ ] IsViewCurrent
- [ ] IsViewMaximized
- [ ] IsViewPerspective
- [ ] IsViewTitleVisible
- [ ] IsWallpaper
- [ ] MaximizeRestoreView
- [ ] NamedCPlane
- [ ] NamedCPlanes
- [ ] NamedViews
- [ ] RenameView
- [ ] RestoreNamedCPlane
- [ ] RestoreNamedView
- [ ] RotateCamera
- [ ] RotateView
- [ ] ShowGrid
- [ ] ShowGridAxes
- [ ] ShowViewTitle
- [ ] ShowWorldAxes
- [ ] TiltView
- [ ] ViewCamera
- [ ] ViewCameraLens
- [ ] ViewCameraPlane
- [ ] ViewCameraTarget
- [ ] ViewCameraUp
- [ ] ViewCPlane
- [ ] ViewDisplayMode
- [ ] ViewDisplayModeId
- [ ] ViewDisplayModeName
- [ ] ViewDisplayModes
- [ ] ViewNames
- [ ] ViewNearCorners
- [ ] ViewProjection
- [ ] ViewRadius
- [ ] ViewSize
- [ ] ViewSpeedTest
- [ ] ViewTarget
- [ ] ViewTitle
- [ ] Wallpaper
- [ ] WallpaperGrayScale
- [ ] WallpaperHidden
- [ ] ZoomBoundingBox
- [ ] ZoomExtents
- [ ] ZoomSelected

---