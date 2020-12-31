Cerebellum Value Map
====================

This package can show values as colors on top of a cerebellum
illustration:

.. image:: _static/example_lobe.svg
.. image:: _static/example_lobules.svg

It is used in the paper `Longitudinal analysis of regional cerebellum volumes
during normal aging <https://www.sciencedirect.com/science/article/pii/S1053811920305486?via%3Dihub>`_.


.. toctree::
   :maxdepth: 3
   :caption: Contents
    
   api
   examples

Install
-------

Install from GitHub:

.. code-block:: bash

   pip install git+https://github.com/shuohan/cerebellum-value-map


Install from PyPI:

.. code-block:: bash

   pip install cerebellum-value-map

Use the source code:

.. code-block:: bash

   git clone https://github.com/shuohan/cerebellum-value-map
   # see https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH
   export PYTHONPATH=$(realpath cerebellum-value-map):$PYTHONPATH
   cd cerebellum-value-map/scripts
   ./show_cerebellum.py -h

Index
-----

* :ref:`genindex`
