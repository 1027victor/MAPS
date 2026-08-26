# 2. Front-End Feature Walkthrough

## 2.5 2D Visualization
![](./_images/1786608674140-53c85fc2-2023-4d2c-986f-3b3aa2fd9f18.png)

The 2D visualization interface contains multiple visualization functions, for the top navigation bar:

### (1) SLICE drop-down menu
+ SLICE drop-down menu: used to switch slice files
+ ![](./_images/1786608724668-88c5dc7e-94a4-4293-8af7-4bdce6b12ada.png)

### (2) GENE input box
+ GENE input box: used to search the gene list, click the Apply button to refresh, data loading will take a certain amount of time, depending on the data size
+ ![](./_images/1786608809216-525d9192-3f6d-40cf-a9bb-ce7fe8e7bd18.png)

### (3) LABEL drop-down menu
+ LABEL drop-down menu: used to switch cell labels. Click the Apply button to refresh. Data loading will take a certain amount of time, depending on the size of the data.
+ ![](./_images/1786608855255-e2bbc8d1-7e9c-4ea7-9bf3-058518db2933.png)

### (4) dark/light button
+ dark/light button: used to switch the background color. The black background is loaded by default and can be set in the Config interface.
+ ![](./_images/1786608941486-28731a48-5721-4d9a-b1d5-d8294b0d6d17.png)

### (5) reset button
+ reset button: used to reset the view. The user can drag the slice with the right mouse button, or zoom in and out with the mouse wheel. This button can restore the initial view and zoom ratio.

### (6) Model Frame button
+ Model Frame button: used to add borders and scales, and can indicate the physical dimensions of the slice
+ ![](./_images/1786613272863-5f4cb150-39e2-4f73-821a-68f976b0bf81.png)

### (7) Window shape button
+ Window shape button: used to switch the window shape, the default is rectangular, click to switch to square, click again to restore the rectangular window
+ ![](./_images/1786608978878-626d2f3e-7e57-4a37-8570-3521393c5705.png)

### (8) Save figure button
+ Save figure button: Click to save the current window to a PNG image. The resolution is affected by the screen size and magnification (HD parameters can be set in the Config interface, the default is 2X)
+ ![](./_images/1786609162470-5650fc72-7dd3-4cec-9c2a-0bc36d104167.png)

For the right sidebar:

### (9) POINT Card
+ POINT Card: can change the size and transparency of points
+ ![](./_images/1786609313522-301e4932-405d-4e9f-a540-24c8dce0b69d.png)

### (10) LABELS Card
+ LABELS Card: used to set color mapping (only for categorical labels, invalid for numerical labels such as gene expression values). The drop-down menu on the right side of the title can switch color palettes (we provide 5 sets of color palettes, which can be set in the Config interface). The three buttons on the right are used for "Export Palette", "Select All" and "Deselect All", which are shortcut operations for the multi-select box below. The multi-select box on the left side of the color entry below can be used to control whether the points of the corresponding label are displayed. Clicking the color rectangle can also switch the mapping color. The Apply button below needs to be clicked to confirm after modifying the color to refresh the color mapping. The Reset button is used to restore the default color mapping.
+ ![](./_images/1786609366594-05ea5c22-bffe-498d-adfd-d8fb39345455.png)
+ ![](./_images/1786609395623-555520a5-362c-4aa8-a45e-8785ce0b804d.png)

### (11) ADVANCED FILTER Card
+ ADVANCED FILTER Card: For hierarchical label filtering, you can select another label (perhaps a more dominant cell type or region) from the drop-down menu, thereby displaying only the cell types in that region
+ ![](./_images/1786609503908-bb43e127-e032-4b12-9ee9-ba5eb8fc5009.png)

### (12) FLIP Card
+ FLIP Card: used to mirror the X- and Y-axis coordinates
+ ![](./_images/1786609537147-02358b35-e36b-4c55-84cb-f45eaab76d6a.png)

### (13) CELL DENSITY VIEWER
+ CELL DENSITY VIEWER: for visualizing cell density
+ ![](./_images/1786609625871-df99ece3-92a2-4079-9f40-ebe7578b25f2.png)

