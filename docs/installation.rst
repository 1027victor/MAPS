Installation
=======================

Download
--------

Clone the MAPS repository from `GitHub <https://github.com/dbjzs/MAPS>`_:

.. code-block:: bash

    git clone https://github.com/dbjzs/MAPS.git
    cd MAPS

Environment
-----------

MAPS requires Python 3.10. We recommend training MAPS models on a device
with GPU support.

Create and activate a Conda environment:

.. code-block:: bash

    conda create -n MAPS -c conda-forge python=3.10.13 libopenblas=0.3.25 -y
    conda activate MAPS

Package installation
--------------------

Install the required dependencies:

.. code-block:: bash

    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

Then install MAPS from the local repository:

.. code-block:: bash

    pip install .