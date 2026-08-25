Installation
============

Installation via GitHub
-----------------------

Download
~~~~~~~~

.. code-block:: bash

    git clone https://github.com/dbjzs/MAPS.git
    cd MAPS

Environment
~~~~~~~~~~~

MAPS is available for Python 3.10. We recommend training MAPS models on a
device with GPU support.

Create and activate the Conda environment:

.. code-block:: bash

    conda create -n MAPS -c conda-forge python==3.10.13 libopenblas=0.3.25 -y
    conda activate MAPS

Package installation
~~~~~~~~~~~~~~~~~~~~

Install the requirements and then install MAPS from the local repository:

.. code-block:: bash

    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
    pip install .

Installation via PyPI
---------------------

Environment
~~~~~~~~~~~

MAPS is available for Python 3.10. We recommend training MAPS models on a
device with GPU support.

Create and activate the Conda environment:

.. code-block:: bash

    conda create -n MAPS -c conda-forge python==3.10.13 libopenblas=0.3.25 -y
    conda activate MAPS

Package installation
~~~~~~~~~~~~~~~~~~~~

Install MAPS from PyPI:

.. code-block:: bash

    pip install mapspatial
