# 2. Front-End Feature Walkthrough

## 2.9 Insert slice alignment
This mode integrates one or more slices excluded from Global Align into an existing aligned reference atlas. Click Impute Align in the lower-left corner, then select the slices and their insertion positions in the dialog box:

![](./_images/1786620628766-1a98956c-fb42-46a2-80a9-f9e7a2cfd947.png)

Several insertion-position methods are available. Auto-match position identifies the most similar reference slice and places the new slice next to it at the target slice's Z coordinate plus 0.5. UNS_atlas_match-First reads the selected slice's `uns` metadata and obtains the target slice from `atlas_match.best_atlas_slice_idx`; populate this field to define insertion positions in batches. Auto-match position also writes its result to this field. For a single slice, you may specify the target directly; the same Z-axis offset of +0.5 is applied:

![](./_images/1786620671879-a4af7421-308b-4436-bdff-56cc7c1887c2.png)

Processing time depends on slice size and the multithreading threshold configured in Config.

![](./_images/1783335490175-6b9d3baf-0e62-4c26-bdc9-089142bea0c3.png)

When insertion is complete, MAPS-Explore opens the 3D visualization interface. Click the adjustment button in the top toolbar to open the list of inserted slices.

![](./_images/1786620739304-821bb280-af09-44b4-8bd8-ebf75efef288.png)

From this list, you can search for slices, adjust and save their positions, or delete multiple inserted slices at once.
