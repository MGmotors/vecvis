VecVis
======
A tool for visualization and filtering of vectors.

Features
--------
- Simple to use API
- Clear visualization of vectors in a starchart.
- Filtering of vectors.
	- Only show Pareto-optimal vectors.
	- Constrain the vectors by valueranges for each dimension.

How to use
----------
After you have installed VecVis you are ready to go.
The only way to start the GUI and add vectors is via API.
The available functions are listed in section :ref:`Availabe Functions`.

Example use:

.. code-block:: python

   from vecvis import API
   
   app = API(3)
   app.add_vector((1,0.4,1.3))

Availabe Functions
------------------
.. autoclass:: vecvis.API
    :members:
   