Tutorials
=========

.. raw:: html

   <style>
     .maps-tutorial-grid {
       display: grid;
       grid-template-columns: repeat(3, minmax(0, 1fr));
       gap: 1.25rem;
       margin-top: 1.5rem;
     }
     .maps-tutorial-card {
       display: block;
       color: inherit;
       text-decoration: none;
       border: 1px solid var(--color-background-border);
       border-radius: 8px;
       overflow: hidden;
       background: var(--color-background-primary);
       transition: transform 120ms ease, border-color 120ms ease, box-shadow 120ms ease;
     }
     .maps-tutorial-card:hover {
       transform: translateY(-2px);
       border-color: var(--color-brand-primary);
       box-shadow: 0 8px 24px rgba(0, 0, 0, 0.10);
       text-decoration: none;
     }
     .maps-tutorial-card img {
       display: block;
       width: 100%;
       aspect-ratio: 16 / 9;
       object-fit: cover;
       background: var(--color-background-secondary);
     }
     .maps-tutorial-card span {
       display: block;
       padding: 0.75rem 0.9rem;
       font-weight: 600;
       line-height: 1.3;
     }
     @media (max-width: 900px) {
       .maps-tutorial-grid {
         grid-template-columns: repeat(2, minmax(0, 1fr));
       }
     }
     @media (max-width: 560px) {
       .maps-tutorial-grid {
         grid-template-columns: 1fr;
       }
     }
   </style>

   <div class="maps-tutorial-grid">
     <a class="maps-tutorial-card" href="Cross_modal_alignment/index.html">
       <img src="../../_static/img/Cross_modal_alignment.jpg" alt="Cross modal alignment">
       <span>Cross Modal Alignment</span>
     </a>
     <a class="maps-tutorial-card" href="Cross_platform_alignment/index.html">
       <img src="../../_static/img/Cross_platforms_alignment.jpg" alt="Cross platform alignment">
       <span>Cross Platform Alignment</span>
     </a>
     <a class="maps-tutorial-card" href="Diagonal_integration/index.html">
       <img src="../../_static/img/Diagonal_integration.jpg" alt="Diagonal integration">
       <span>Diagonal Integration</span>
     </a>
     <a class="maps-tutorial-card" href="Partial_alignment/index.html">
       <img src="../../_static/img/Partial_alignment.jpg" alt="Partial alignment">
       <span>Partial Alignment</span>
     </a>
     <a class="maps-tutorial-card" href="Reference_and_sequential_alignment/index.html">
       <img src="../../_static/img/Reference%20and%20sequential%20alignment.jpg" alt="Reference and sequential alignment">
       <span>Reference and Sequential Alignment</span>
     </a>
     <a class="maps-tutorial-card" href="3D_reconstruction/index.html">
       <img src="../../_static/img/3D_reconstruction.jpg" alt="3D reconstruction">
       <span>3D Reconstruction</span>
     </a>
     <a class="maps-tutorial-card" href="MAPS_Explore/README.html">
       <img src="../../_static/img/MAPS_Explorer.jpg" alt="MAPS Explore">
       <span>MAPS Explore</span>
     </a>
   </div>

.. toctree::
   :maxdepth: 2
   :hidden:

   Cross_modal_alignment/index
   Cross_platform_alignment/index
   Diagonal_integration/index
   Partial_alignment/index
   Reference_and_sequential_alignment/index
   3D_reconstruction/index
   MAPS_Explore/README
