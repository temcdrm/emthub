# Copyright (C) 2017-2023 Battelle Memorial Institute
# Copyright (C) 2025-2026 Meltran, Inc.
# file: api.py
"""Functions intended for public access.

Example:
    To show print CIM summaries interface::

        import emthub.api as emthub
        emthub.print_cim_summaries(['XfmrSat','IEEE39','IEEE118','WECC240'])

Public Functions:
    :print_cim_summaries: Print class names and counts found in list of Turtle files.
    :summarize_graph: Count the class instances by namespace in an RDF graph.
    :load_emt_dict: Load an RDF graph into Python dictionary using packaged SPARQL queries.
    :load_ic_dict: Load an RDF graph into Python dictionary from standalone power flow solution file.
    :list_dict_table: Print the fields and attributes of a Python dictionary loaded from SPARQL.
    :adhoc_sparql_dict: Load the result of a user-written SPARQL query into a Python dictionary.
    :build_bus_lists: Order the buses (connectivity nodes) sequentially.
    :get_swingbus_id: Find the CIM ConnectivityNode ID by matching the Name/Number from the original raw file.
"""

from __future__ import absolute_import

from .cim_summary import print_cim_summaries

from .cim_sparql import summarize_graph
from .cim_sparql import load_emt_dict
from .cim_sparql import load_ic_dict
from .cim_sparql import list_dict_table
from .cim_sparql import adhoc_sparql_dict

from .buslists import build_bus_lists
from .buslists import get_swingbus_id

from .version import __version__


