# 2. Front-End Feature Walkthrough

## 2.4 Data processing
The purpose of this step is to improve the efficiency of 2D and 3D visualization. We use a variety of data acceleration methods and need to convert your H5AD files into compressed binary files to ensure smooth loading of visualizations and low memory burden. You first need to click on a file to view its information, then click the Process button in the lower left corner, select the obs label that needs to be saved in the pop-up window, and specify the slice coordinate label (usually in obsm).

![](./_images/1786608088144-e257bb7c-1840-4194-8fa2-2b2dcac24b22.png)

![](./_images/1786608178354-f0556ce6-101d-4dd0-8ed5-837a6be1b4d1.png)

We also provide multi-slice processing function, you can process all slices uniformly:
![](./_images/1786608146548-6c21eae2-a0b4-4a4a-b375-7e5f9306dcc5.png)

Click the Execute button to start the Process. The processing may take a while, depending on the slice size and multi-threading settings you provide (which can be set in the Config interface). After the process ends, it will jump to the 2D visualization interface:

![](./_images/1786608281413-4e7efb45-887a-4bfb-80fa-7450591f3467.png)

