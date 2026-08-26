# 2. Front-End Feature Walkthrough

## 2.7 3D Visualization
![](./_images/1787625173370-7b46ceaf-f01c-4b19-be52-4852e4531a60.png)

The 3D visualization interface contains richer visualization functions, for the top navigation bar:

### (1) ALIGN drop-down menu
+ ALIGN drop-down menu: used to switch the alignment mode. If you have not performed a certain alignment mode and want to access it, it will fall back to the processed mode.
+ ![](./_images/1786613960320-75bc2b2c-8384-4de6-ad7f-c7c68a04d15d.png)

### (2) GENE input box
+ GENE input box: Same as 2D visualization, for 3D visualization effect, we recommend enlarging the point size and turning on the Dark Min Alpha switch of the color map card.
+ ![](./_images/1786614004868-06bb4a2f-cf9d-4641-b8eb-2d17186a2415.png)

### (3) LABEL drop-down menu
+ LABEL drop-down menu: same as 2D visualization.
+ ![](./_images/1786614103746-6a208372-b9da-46d7-8fcd-82befc7df678.png)

### (4) dark/light button
+ dark/light button: same as 2D visualization.
+ ![](./_images/1786614130796-10756da4-68ea-4493-b36e-2cb31a77c4e9.png)

### (5) statistics button
+ statistics button: used to expand additional sidebars to display statistical information.
+ ![](./_images/1786614164255-ef5e36c2-e794-4fe6-8a07-01d1154c94f6.png)

### (6) reset button
+ reset button: used to reset the view. The user can rotate the space with the left mouse button, drag the slice with the right mouse button, or zoom in and out through the mouse wheel. This button can restore the initial view and zoom ratio.

### (7) Model Frame button
+ Model Frame button: used to add borders and scales, and can indicate the physical dimensions of the slice.
+ ![](./_images/1786614247885-f8abeae4-f115-4794-8e51-3f446933c7f9.png)

### (8) Window shape button
+ Window shape button: same as 2D visualization.
+ ![](./_images/1786614268364-d1c11508-52fe-40e1-bc35-f89aaff73391.png)

### (9) Download button
+ Download button: same as 2D visualization.
+ ![](./_images/1786614318809-49783f10-262e-473f-b0e8-906e1e730fb7.png)

For the right sidebar:

### (10) VIEW Card
+ VIEW Card: Define the screen center, rotation angle and viewing distance. These settings can be pre-set and loaded through the "config" page.

### (11) POINT Card
+ POINT Card: Same as 2D visualization.

### (12) LABELS Card
+ LABELS Card: Same as 2D visualization, we provide users with 5 preset color panels and color mapping JSON quick copy button.
+ ![](./_images/1786614364945-daa2f11d-793e-407d-a380-b850988ab4ad.png)

### (13) ADVANCED FILTER Card
+ ADVANCED FILTER Card: same as 2D visualization.

### (14) FILES Card
+ FILES Card: used to control whether the points of the corresponding slice are displayed.
+ ![](./_images/1786614456769-76807f3f-cb28-45f1-9297-f5a93d02ff89.png)

### (14) X Slice Panel
+ X Slice Panel: X-axis slab slicer, the controls are the same as described above.
+ ![](./_images/1786620419692-4ff3d3f0-f4a8-4e95-9e40-75b41524f0ea.png)

### (16) Y Slice Panel
+ Y Slice Panel: Y-axis slab slicer, the controls are the same as described above.
+ ![](./_images/1786620457354-dcc1bdf1-41c6-42e4-ac67-c9b81688a242.png)

### (17) Z Slice Panel
+ Z Slice Panel: Z-axis slab slicer, the controls are the same as described above. Note that the default Z-axis scaling of all projects is 0.3. This setting is to make the slices compact and easy to visualize, and can be set in the Config interface.
+ ![](./_images/1786620518242-5065145e-f70d-477e-aade-30d909fd8850.png)

### (18) Global Voxelization Panel
+ Shell Panel: Global voxelization panel, when selected, will generate a closed, smooth, translucent shell outside the entire point cloud. This shell is calculated entirely from the front end and is affected by slice spacing. Users can modify the shell transparency, extension distance, outline stroke, and lighting rendering effects through the panel. Note that we have provided a model download button on the right side to facilitate you to export the shell for more customized rendering for scientific research or other scenarios.
+ ![](./_images/1786614542569-3346aa95-0294-4277-9f76-1d3764ddfc8c.png)

### (19) Label Voxelization Panel
+ Label Shell Panel: Label voxelization panel, when selected, will generate a closed, smooth, opaque shell outside the visible point cloud. This shell is calculated entirely by the front end and is affected by slice spacing and point density. Users can modify the smoothness and filtering range of the shell through the panel. We also provide a model download button on the right.
+ ![](./_images/1786614686257-1649bff3-7e7f-40d4-bc2d-38a7dffb4162.png)

### (20) SURFACE DYNAMICS panel
+ SURFACE DYNAMICS panel: used for surface molecular heterogeneity analysis and gradient analysis of closed surfaces. Note that this analysis module must first use Label Shell to calculate the label voxelization model. This computation may take some time to complete.
+ ![](./_images/1786624987128-23ed0beb-0235-4b49-a529-32f68c9651cc.png)
+ ![](./_images/1786625011211-56b36869-9663-4131-82e8-eb73d23e715e.png)

### (21) Surface region analysis panel
+ Surface region analysis panel: used to isolate a specified surface region for subsequent analysis, provided that at least one of the selection boxes in the X/Y/Z slab slicer is used.
+ ![](./_images/1786625130284-e98d4ec2-859d-47d9-862b-ba1cee82cff0.png)
+ ![](./_images/1786625248873-74133358-cd48-4b2c-952d-36728eca77fc.png)

### (22) Axial analysis panel
+ Axial analysis panel: Used for selecting and performing advanced analysis on axial cylindrical regions. Users can define the axial cylindrical space in two ways: either by specifying two points to determine the cylinder's ends, or by defining a single point as the cylinder's center, then setting its length via extension and adjusting the angle using XYZ rotation. After establishing the axial cylindrical selection, three analysis modules below allow interpretation of axial cell type distribution, gene expression gradients, and multi-component colocalization analysis. All analyses provide thumbnail previews, full-screen display, and data export options, and the current rendering effects can be cleared using the reset button.
+ ![](./_images/1787623305854-0ce760df-2dc4-4bdc-9628-0f16e6c1722d.png)
+ ![](./_images/1787623369119-df2f4a96-5d78-4dbc-8ef8-8760fd0464a9.png)
+ ![](./_images/1787623651473-65cf55fe-a3fc-4675-966d-feb1f9fa0368.png)
+ ![](./_images/1787623930956-e6265f8d-d21c-42bb-a670-e15def9386bc.png)
+ ![](./_images/1787623950182-0e2c6c89-69b9-451b-baa7-d243556abc08.png)
+ ![](./_images/1787624005765-498f8809-feaf-472c-a80c-220498819c5a.png)
+ ![](./_images/1787624045934-d3540171-276f-4b16-b498-4c3b903c5b21.png)
+ ![](./_images/1787624077970-c57cec9c-44c3-45f0-a4d8-e153f8f6d431.png)

### (23) CELL DENSITY VIEWER panel
+ CELL DENSITY VIEWER panel: for spatial cell density analysis of a specified range.
+ ![](./_images/1786625363397-b6bfd6c2-4105-42ce-b7e9-e8347ff70b8e.png)
+ ![](./_images/1786625380670-9947cc1e-298d-4552-bcab-ce1c691dd3fc.png)

### (24) Auto Rotate Panel
+ Auto Rotate Panel: Automatically rotate the panel. Once selected, you can start the rotation and adjust the rotation speed and direction.
+ ![](./_images/1786620365820-f29bec3c-dd7a-4b22-83c4-bffcf4df4bd4.png)

### (25) X Slice Panel
+ X Slice Panel: an X-axis slab slicer. When enabled, it displays a cubic selection volume and renders only the points inside that volume. Use the CENTER slider to move the cube, the THICKNESS slider to adjust its depth, and the X-COMPRESSION slider to scale the global X axis. Quick controls on the right side of the panel title flip the X-axis coordinates, rotate the view clockwise, or automatically sweep the slab through the dataset.

### (26) 3D co-localization panel
+ 3D co-localization panel: performs gene coexpression analysis and supports custom expression filters and colors for three gene-interaction groups.
+ ![](./_images/1786624410503-262ca15c-49c9-4108-acbe-9737b0f8b857.png)

### (27) SPATIALLY VARIABLE GENES (SVG) panel
+ SPATIALLY VARIABLE GENES (SVG) panel: identifies spatially variable genes using a custom algorithm optimized for high-speed computation in the front-end visualization environment.

### (28) MARKER GENE STATISTICS panel
+ MARKER GENE STATISTICS panel: identifies marker genes for a specified cell label using a custom algorithm optimized for high-speed computation in the front-end visualization environment.
+ ![](./_images/1786624558751-3a8b9403-e5ce-4e6e-82fd-dd0ba3f1ccfa.png)
