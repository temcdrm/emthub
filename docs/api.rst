API Reference
=============

.. automodule:: emthub.__init__

First ``import emthub.api as emthub``, then invoke a function like ``emthub.print_cim_summaries([filename_roots])``

api
---

.. automodule:: emthub.api
   :members:
   :special-members:
..   :member-order: bysource
   :exclude-members: __init__, __weakref__, forward

buslists
--------

.. automodule:: emthub.buslists
   :members:
   :special-members:
..   :member-order: bysource
   :exclude-members: __init__, __weakref__, forward

cim_examples
------------

.. autodata:: emthub.cim_examples.CASES
   :no-value:

.. exec_code::

   #hide: start
   import json
   import emthub.api as emthub
   print(json.dumps(emthub.CASES, indent=2))
   #hide: stop

cim_sparql
----------

.. automodule:: emthub.cim_sparql
   :members:
   :special-members:
..   :member-order: bysource
   :exclude-members: __init__, __weakref__, forward

cim_summary
-----------

.. automodule:: emthub.cim_summary
   :members:
   :special-members:
..   :member-order: bysource
   :exclude-members: __init__, __weakref__, forward

cim_support
-----------

.. automodule:: emthub.cim_support
   :members:
   :special-members:
..   :member-order: bysource
   :exclude-members: __init__, __weakref__, forward

create_atp
----------

.. automodule:: emthub.create_atp
   :members:
   :special-members:
..   :member-order: bysource
   :exclude-members: __init__, __weakref__, forward

create_mpow
-----------

.. automodule:: emthub.create_mpow
   :members:
   :special-members:
..   :member-order: bysource
   :exclude-members: __init__, __weakref__, forward

create_rdf
----------

.. automodule:: emthub.create_rdf
   :members:
   :special-members:
..   :member-order: bysource
   :exclude-members: __init__, __weakref__, forward

create_sql
----------

.. automodule:: emthub.create_sql
   :members:
   :special-members:
..   :member-order: bysource
   :exclude-members: __init__, __weakref__, forward

dll_config
----------

Functions to query an IEEE/Cigre DLL through its API.

.. autofunction:: emthub.dll_config.get_dll_interface
.. autofunction:: emthub.dll_config.write_atp_dll_interface

mpow_utilities
--------------

.. automodule:: emthub.mpow_utilities
   :members:
   :special-members:
..   :member-order: bysource
   :exclude-members: __init__, __weakref__, forward

plot_utils
----------

.. automodule:: emthub.plot_utils
   :members:
   :special-members:
..   :member-order: bysource
   :exclude-members: __init__, __weakref__, forward



