# RhinoScriptSyntax Implementation Status

## Our MCP High-Level Tools (135 total):

### Scene Understanding (2)
1. get_scene_info
2. get_selected_objects

### Basic Geometry (7)
3. create_point
4. create_line
5. create_circle
6. create_arc
7. create_ellipse
8. create_polyline
9. create_curve

### 3D Solids (5)
10. create_box
11. create_sphere
12. create_cylinder
13. create_cone
14. create_torus

### Transformations (8)
15. move_objects
16. rotate_objects
17. scale_objects
18. mirror_objects
19. copy_objects
20. array_linear
21. array_polar
22. orient_objects

### Boolean Operations (3)
23. boolean_union
24. boolean_difference
25. boolean_intersection

### Curve Operations (17)
26. join_curves
27. explode_curves
28. offset_curve
29. fillet_curves
30. extend_curve
31. create_rectangle
32. create_spiral
33. create_nurbs_curve
34. create_blend_curve
35. divide_curve
36. divide_curve_length
37. split_curve
38. close_curve
39. reverse_curve
40. rebuild_curve
41. project_curve_to_surface
42. execute_python_code

### Surface Operations (21)
43. extrude_curve_straight
44. revolve_curve
45. loft_curves
46. create_pipe
47. sweep1
48. sweep2
49. create_planar_surface
50. create_edge_surface
51. create_network_surface
52. create_patch
53. offset_surface
54. split_brep
55. fillet_surfaces
56. cap_planar_holes
57. extrude_curve_along_curve
58. extrude_curve_to_point
59. duplicate_edge_curves
60. duplicate_surface_border
61. join_surfaces
62. explode_polysurfaces
63. unroll_surface

### Mesh Operations (9)
64. create_mesh
65. create_planar_mesh
66. mesh_from_surface
67. mesh_boolean_union
68. mesh_boolean_difference
69. mesh_boolean_intersection
70. join_meshes
71. mesh_to_nurb
72. mesh_offset

### Group Operations (6)
73. create_group
74. delete_group
75. add_to_group
76. remove_from_group
77. list_groups
78. select_by_group

### View Operations (7)
79. set_view_camera
80. zoom_extents
81. zoom_selected
82. get_view_info
83. set_display_mode
84. add_named_view
85. restore_named_view

### Block Operations (5)
86. create_block
87. insert_block
88. explode_block
89. delete_block
90. list_blocks

### Material Operations (5)
91. add_material_to_object
92. add_material_to_layer
93. set_material_color
94. set_material_transparency
95. set_material_shine

### Layer Management (6)
96. create_layer
97. delete_layer
98. set_current_layer
99. set_layer_color
100. set_layer_visibility
101. list_layers

### Analysis (4)
102. measure_distance
103. measure_curve_length
104. measure_area
105. measure_volume

### Object Properties (8)
106. set_object_name
107. set_object_color
108. set_object_layer
109. hide_objects
110. show_objects
111. lock_objects
112. unlock_objects
113. is_object_solid

### Selection (8)
114. select_all
115. select_by_type
116. select_by_layer
117. unselect_all
118. delete_selected
119. select_by_name
120. last_created_objects
121. invert_selection

### Document (3)
122. get_document_info
123. set_unit_system
124. enable_redraw

### Annotations (3)
125. add_text
126. add_text_dot
127. add_leader

### User Data (4)
128. set_user_text
129. get_user_text
130. set_document_user_text
131. get_document_user_text

### Curve Analysis (4)
132. curve_closest_point
133. evaluate_curve
134. curve_start_end_points
135. curve_curve_intersection

---

## RhinoScriptSyntax API Coverage

### application
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

### block
- [x] **AddBlock** (used in create_block)
- [ ] BlockContainerCount
- [ ] BlockContainers
- [ ] BlockCount
- [ ] BlockDescription
- [ ] BlockInstanceCount
- [ ] BlockInstanceInsertPoint
- [ ] BlockInstanceName
- [ ] BlockInstances
- [ ] BlockInstanceXform
- [x] **BlockNames** (used in list_blocks)
- [ ] BlockObjectCount
- [ ] BlockObjects
- [ ] BlockPath
- [ ] BlockStatus
- [x] **DeleteBlock** (used in delete_block)
- [x] **ExplodeBlockInstance** (used in explode_block)
- [x] **InsertBlock** (used in insert_block)
- [ ] InsertBlock2
- [ ] IsBlock
- [ ] IsBlockEmbedded
- [ ] IsBlockInstance
- [ ] IsBlockInUse
- [ ] IsBlockReference
- [ ] RenameBlock

### curve
- [ ] AddArc
- [x] **AddArc3Pt** (used in create_arc)
- [ ] AddArcPtTanPt
- [x] **AddBlendCurve** (used in create_blend_curve)
- [x] **AddCircle** (used in create_circle)
- [ ] AddCircle3Pt
- [ ] AddCurve
- [x] **AddEllipse** (used in create_ellipse)
- [ ] AddEllipse3Pt
- [x] **AddFilletCurve** (used in fillet_curves)
- [ ] AddInterpCrvOnSrf
- [ ] AddInterpCrvOnSrfUV
- [x] **AddInterpCurve** (used in create_curve)
- [x] **AddLine** (used in create_line)
- [x] **AddNurbsCurve** (used in create_nurbs_curve)
- [x] **AddPolyline** (used in create_polyline)
- [x] **AddRectangle** (used in create_rectangle)
- [x] **AddSpiral** (used in create_spiral)
- [ ] AddSubCrv
- [ ] ArcAngle
- [ ] ArcCenterPoint
- [ ] ArcMidPoint
- [ ] ArcRadius
- [ ] CircleCenterPoint
- [ ] CircleCircumference
- [ ] CircleRadius
- [x] **CloseCurve** (used in close_curve)
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
- [x] **CurveClosestPoint** (used in curve_closest_point)
- [ ] CurveContourPoints
- [ ] CurveCurvature
- [x] **CurveCurveIntersection** (used in curve_curve_intersection)
- [ ] CurveDegree
- [ ] CurveDeviation
- [ ] CurveDim
- [ ] CurveDirectionsMatch
- [ ] CurveDiscontinuity
- [x] **CurveDomain** (used in create_blend_curve)
- [ ] CurveEditPoints
- [x] **CurveEndPoint** (used in curve_start_end_points)
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
- [x] **CurveStartPoint** (used in curve_start_end_points)
- [ ] CurveSurfaceIntersection
- [x] **CurveTangent** (used in evaluate_curve)
- [ ] CurveWeights
- [x] **DivideCurve** (used in divide_curve)
- [ ] DivideCurveEquidistant
- [x] **DivideCurveLength** (used in divide_curve_length)
- [ ] EllipseCenterPoint
- [ ] EllipseQuadPoints
- [x] **EvaluateCurve** (used in evaluate_curve, curve_closest_point)
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
- [x] **ProjectCurveToSurface** (used in project_curve_to_surface)
- [x] **RebuildCurve** (used in rebuild_curve)
- [ ] RemoveCurveKnot
- [x] **ReverseCurve** (used in reverse_curve)
- [ ] SimplifyCurve
- [x] **SplitCurve** (used in split_curve)
- [ ] TrimCurve
- [ ] ChangeCurveDegree
- [ ] AddTweenCurves

### dimension
- [ ] AddAlignedDimension
- [ ] AddDimStyle
- [x] **AddLeader** (used in add_leader)
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

### document
- [ ] CreatePreviewImage
- [ ] DocumentModified
- [x] **DocumentName** (used in get_document_info)
- [x] **DocumentPath** (used in get_document_info)
- [x] **EnableRedraw** (used in enable_redraw)
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
- [x] **UnitSystem** (used in set_unit_system, get_document_info)
- [x] **UnitSystemName** (used in get_scene_info, get_document_info)

### geometry
- [ ] AddClippingPlane
- [ ] AddPictureFrame
- [x] **AddPoint** (used in create_point)
- [ ] AddPointCloud
- [ ] AddPoints
- [x] **AddText** (used in add_text)
- [x] **AddTextDot** (used in add_text_dot)
- [ ] Area
- [x] **BoundingBox** (used in get_selected_objects, offset_curve)
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

### grips
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

### group
- [x] **AddGroup** (used in create_group)
- [x] **AddObjectsToGroup** (used in create_group, add_to_group)
- [ ] AddObjectToGroup
- [x] **DeleteGroup** (used in delete_group)
- [ ] GroupCount
- [x] **GroupNames** (used in list_groups)
- [ ] HideGroup
- [ ] IsGroup
- [ ] IsGroupEmpty
- [ ] LockGroup
- [ ] RemoveObjectFromAllGroups
- [ ] RemoveObjectFromGroup
- [x] **RemoveObjectsFromGroup** (used in remove_from_group)
- [ ] RenameGroup
- [ ] ShowGroup
- [ ] UnlockGroup
- [x] **ObjectsByGroup** (used in select_by_group)
- [ ] ObjectTopGroup

### hatch
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

### layer
- [x] **AddLayer** (used in create_layer)
- [x] **CurrentLayer** (used in set_current_layer, list_layers)
- [x] **DeleteLayer** (used in delete_layer)
- [ ] ExpandLayer
- [x] **IsLayer** (used in multiple functions)
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

### light
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

### line
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

### linetype
- [ ] IsLinetype
- [ ] IsLinetypeReference
- [ ] LinetypeCount
- [ ] LinetypeNames

### material
- [x] **AddMaterialToLayer** (used in add_material_to_layer)
- [x] **AddMaterialToObject** (used in add_material_to_object)
- [ ] CopyMaterial
- [ ] IsMaterialDefault
- [ ] IsMaterialReference
- [ ] MatchMaterial
- [ ] MaterialBump
- [x] **MaterialColor** (used in set_material_color, add_material_to_object)
- [ ] MaterialEnvironmentMap
- [ ] MaterialName
- [ ] MaterialReflectiveColor
- [x] **MaterialShine** (used in set_material_shine)
- [ ] MaterialTexture
- [x] **MaterialTransparency** (used in set_material_transparency)
- [ ] MaterialTransparencyMap
- [ ] ResetMaterial

### mesh
- [x] **AddMesh** (used in create_mesh)
- [x] **AddPlanarMesh** (used in create_planar_mesh)
- [ ] CurveMeshIntersection
- [ ] DisjointMeshCount
- [ ] DuplicateMeshBorder
- [ ] ExplodeMeshes
- [ ] IsMesh
- [ ] IsMeshClosed
- [ ] IsMeshManifold
- [ ] IsPointOnMesh
- [x] **JoinMeshes** (used in join_meshes)
- [ ] MeshArea
- [ ] MeshAreaCentroid
- [x] **MeshBooleanDifference** (used in mesh_boolean_difference)
- [x] **MeshBooleanIntersection** (used in mesh_boolean_intersection)
- [ ] MeshBooleanSplit
- [x] **MeshBooleanUnion** (used in mesh_boolean_union)
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
- [x] **MeshOffset** (used in mesh_offset)
- [ ] MeshOutline
- [ ] MeshQuadCount
- [ ] MeshQuadsToTriangles
- [x] **MeshToNurb** (used in mesh_to_nurb)
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
- [x] **MeshObjects** (used in mesh_from_surface)

### object
- [x] **CopyObject** (used in copy_objects, array_linear, array_polar)
- [ ] CopyObjects
- [x] **DeleteObject** (used internally)
- [x] **DeleteObjects** (used in delete_selected)
- [ ] FlashObject
- [ ] HideObject
- [x] **HideObjects** (used in hide_objects)
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
- [x] **IsObjectSolid** (used in is_object_solid)
- [ ] IsObjectValid
- [ ] IsVisibleInView
- [ ] LockObject
- [x] **LockObjects** (used in lock_objects)
- [ ] MatchObjectAttributes
- [x] **MirrorObject** (used in mirror_objects)
- [ ] MirrorObjects
- [x] **MoveObject** (used in move_objects)
- [ ] MoveObjects
- [x] **ObjectColor** (used in set_object_color)
- [ ] ObjectColorSource
- [ ] ObjectDescription
- [ ] ObjectGroups
- [x] **ObjectLayer** (used in set_object_layer, get_selected_objects)
- [ ] ObjectLayout
- [ ] ObjectLinetype
- [ ] ObjectLinetypeSource
- [x] **ObjectMaterialIndex** (used in set_material_color/transparency/shine)
- [ ] ObjectMaterialSource
- [x] **ObjectName** (used in set_object_name, get_selected_objects)
- [ ] ObjectPrintColor
- [ ] ObjectPrintColorSource
- [ ] ObjectPrintWidth
- [ ] ObjectPrintWidthSource
- [x] **ObjectType** (used in get_selected_objects, get_scene_info)
- [x] **OrientObject** (used in orient_objects)
- [x] **RotateObject** (used in array_polar)
- [x] **RotateObjects** (used in rotate_objects)
- [x] **ScaleObject** (used in scale_objects)
- [ ] ScaleObjects
- [ ] SelectObject
- [x] **SelectObjects** (used in select_all, select_by_type, select_by_layer)
- [ ] ShearObject
- [ ] ShearObjects
- [ ] ShowObject
- [x] **ShowObjects** (used in show_objects)
- [ ] TransformObject
- [ ] TransformObjects
- [ ] UnlockObject
- [x] **UnlockObjects** (used in unlock_objects)
- [ ] UnselectObject
- [ ] UnselectObjects

### plane
- [ ] DistanceToPlane
- [ ] EvaluatePlane
- [ ] IntersectPlanes
- [ ] MovePlane
- [ ] PlaneClosestPoint
- [ ] PlaneCurveIntersection
- [ ] PlaneEquation
- [ ] PlaneFitFromPoints
- [ ] PlaneFromFrame
- [x] **PlaneFromNormal** (used in create_ellipse, create_torus, create_arc, create_rectangle)
- [ ] PlaneFromPoints
- [ ] PlanePlaneIntersection
- [ ] PlaneSphereIntersection
- [ ] PlaneTransform
- [ ] RotatePlane
- [ ] WorldXYPlane
- [ ] WorldYZPlane
- [ ] WorldZXPlane

### pointvector
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

### selection
- [x] **AllObjects** (used in get_scene_info, select_all)
- [ ] FirstObject
- [ ] GetCurveObject
- [ ] GetObject
- [ ] GetObjectEx
- [ ] GetObjects
- [ ] GetObjectsEx
- [ ] GetPointCoordinates
- [ ] GetSurfaceObject
- [x] **HiddenObjects** (used in show_objects)
- [x] **InvertSelectedObjects** (used in invert_selection)
- [x] **LastCreatedObjects** (used in last_created_objects)
- [ ] LastObject
- [x] **LockedObjects** (used in unlock_objects)
- [ ] NextObject
- [ ] NormalObjects
- [ ] ObjectsByColor
- [x] **ObjectsByGroup** (used in select_by_group)
- [x] **ObjectsByLayer** (used in select_by_layer)
- [x] **ObjectsByName** (used in select_by_name)
- [x] **ObjectsByType** (used in select_by_type)
- [x] **SelectedObjects** (used in all transformation, boolean, curve, surface operations)
- [x] **UnselectAllObjects** (used in unselect_all)
- [ ] VisibleObjects
- [ ] WindowPick

### surface
- [x] **AddBox** (used in create_box)
- [x] **AddCone** (used in create_cone)
- [ ] AddCutPlane
- [ ] AddCylinder
- [x] **AddEdgeSrf** (used in create_edge_surface)
- [x] **AddNetworkSrf** (used in create_network_surface)
- [ ] AddNurbsSurface
- [x] **AddPatch** (used in create_patch)
- [x] **AddPipe** (used in create_pipe)
- [x] **AddPlanarSrf** (used in create_planar_surface)
- [ ] AddPlaneSurface
- [x] **AddLoftSrf** (used in loft_curves)
- [x] **AddRevSrf** (used in revolve_curve)
- [x] **AddSphere** (used in create_sphere)
- [ ] AddSrfContourCrvs
- [ ] AddSrfControlPtGrid
- [ ] AddSrfPt
- [ ] AddSrfPtGrid
- [x] **AddSweep1** (used in sweep1)
- [x] **AddSweep2** (used in sweep2)
- [ ] AddRailRevSrf
- [x] **AddTorus** (used in create_torus)
- [x] **BooleanDifference** (used in boolean_difference)
- [x] **BooleanIntersection** (used in boolean_intersection)
- [x] **BooleanUnion** (used in boolean_union)
- [ ] BrepClosestPoint
- [x] **CapPlanarHoles** (used in cap_planar_holes)
- [x] **DuplicateEdgeCurves** (used in duplicate_edge_curves)
- [x] **DuplicateSurfaceBorder** (used in duplicate_surface_border)
- [ ] EvaluateSurface
- [ ] ExtendSurface
- [x] **ExplodePolysurfaces** (used in explode_polysurfaces)
- [ ] ExtractIsoCurve
- [ ] ExtractSurface
- [x] **ExtrudeCurve** (used in extrude_curve_along_curve)
- [x] **ExtrudeCurvePoint** (used in extrude_curve_to_point)
- [x] **ExtrudeCurveStraight** (used in extrude_curve_straight, create_cylinder)
- [ ] ExtrudeSurface
- [x] **FilletSurfaces** (used in fillet_surfaces)
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
- [x] **IsSurface** (used in boolean operations, measure_area)
- [ ] IsSurfaceClosed
- [ ] IsSurfacePeriodic
- [ ] IsSurfacePlanar
- [ ] IsSurfaceRational
- [ ] IsSurfaceSingular
- [ ] IsSurfaceTrimmed
- [ ] IsTorus
- [ ] SurfaceSphere
- [x] **JoinSurfaces** (used in join_surfaces)
- [ ] MakeSurfacePeriodic
- [x] **OffsetSurface** (used in offset_surface)
- [ ] PullCurve
- [ ] RebuildSurface
- [ ] RemoveSurfaceKnot
- [ ] ReverseSurface
- [ ] ShootRay
- [ ] ShortPath
- [ ] ShrinkTrimmedSurface
- [x] **SplitBrep** (used in split_brep)
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
- [x] **UnrollSurface** (used in unroll_surface)
- [ ] ChangeSurfaceDegree

### toolbar
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

### transformation
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

### userdata
- [ ] DeleteDocumentData
- [ ] DocumentDataCount
- [ ] DocumentUserTextCount
- [ ] GetDocumentData
- [x] **GetDocumentUserText** (used in get_document_user_text)
- [x] **GetUserText** (used in get_user_text)
- [ ] IsDocumentData
- [ ] IsDocumentUserText
- [ ] IsUserText
- [ ] SetDocumentData
- [x] **SetDocumentUserText** (used in set_document_user_text)
- [x] **SetUserText** (used in set_user_text)

### userinterface
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

### utility
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

### view
- [ ] AddDetail
- [ ] AddLayout
- [ ] AddNamedCPlane
- [x] **AddNamedView** (used in add_named_view)
- [ ] CurrentDetail
- [x] **CurrentView** (used in get_view_info, set_view_camera, set_display_mode)
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
- [x] **RestoreNamedView** (used in restore_named_view)
- [ ] RotateCamera
- [ ] RotateView
- [ ] ShowGrid
- [ ] ShowGridAxes
- [ ] ShowViewTitle
- [ ] ShowWorldAxes
- [ ] TiltView
- [x] **ViewCamera** (used in set_view_camera, get_view_info)
- [ ] ViewCameraLens
- [ ] ViewCameraPlane
- [ ] ViewCameraTarget
- [ ] ViewCameraUp
- [ ] ViewCPlane
- [x] **ViewDisplayMode** (used in set_display_mode, get_view_info)
- [ ] ViewDisplayModeId
- [ ] ViewDisplayModeName
- [ ] ViewDisplayModes
- [ ] ViewNames
- [ ] ViewNearCorners
- [ ] ViewProjection
- [ ] ViewRadius
- [ ] ViewSize
- [ ] ViewSpeedTest
- [x] **ViewTarget** (used in set_view_camera, get_view_info)
- [ ] ViewTitle
- [ ] Wallpaper
- [ ] WallpaperGrayScale
- [ ] WallpaperHidden
- [ ] ZoomBoundingBox
- [x] **ZoomExtents** (used in zoom_extents)
- [x] **ZoomSelected** (used in zoom_selected)

---
