# 2. Front-End Feature Walkthrough

## 2.6 Global slice alignment
You can initiate a global slice alignment task by clicking the Global Align button in the lower left corner, and specify the slices and order involved in the alignment in the pop-up window:

![](./_images/1786613377306-c3aa9869-fe9e-4485-bc24-7ccdf100fa63.png)

Note that I exclude adata_2 here to demonstrate the subsequent insertion alignment task. I specified the batch tag as the slicing order. The real slicing order must be selected and the batch column elements should be of numeric type:

![](./_images/1786613452990-e25786d3-8404-4e7b-ad18-2b4a89c85435.png)

The project may take some time to run because it involves data integration and coordinate alignment calculations:

![](./_images/1783329307988-66d205b7-eae4-4f1a-94f7-b7db1c6baf5d.png)

When the task processing is completed, the 3D visualization interface will automatically open:

![](./_images/1786613562664-d53954ea-d832-46d4-bd76-e9cb2800b0c4.png)

