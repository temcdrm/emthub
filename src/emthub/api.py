# Copyright (C) 2017-2023 Battelle Memorial Institute
# Copyright (C) 2025-2026 Meltran, Inc.
# file: api.py
"""Functions intended for public access.

Example:
    To show print CIM summaries interface::

        import emthub.api as emthub
        emthub.print_cim_summaries(['XfmrSat','IEEE39','IEEE118','WECC240'])

Public Functions:
    :create_cim_rdf: Create RDF in TTL/XML formats from results of load_psse_rawfile
    :create_cim_sql: Create SQL db from results of load_psse_rawfile
    :create_atp: Write an ATP netlist from CIM loaded into a Python dictionary.
    :create_matpower: Write a MATPOWER netlist from CIM loaded into a Python dictionary.
    :print_cim_summaries: Print class names and counts found in list of Turtle files.
    :load_dynamics_defaults: Load example default settings for dynamics into a Python dictionary.
    :load_psse_meta: Load PSSE rawfile metadata into a Python dictionary.
    :load_psse_dyrfile: Load contents of a PSSE dyrfile into a Pandas dataframe.
    :summarize_psse_dyrfile: Enumerate contents of a loaded PSSE dyrfile dataframe.
    :match_dyr_generators: Collect dyrfile modeels from Pandas dataframe into a Python dictionary by generator name/id.
    :load_dynamics_mapping: Load a dictionary of CIM classes and attributes corresponding to dyr file contents.
    :load_psse_rawfile: Load contents of a PSSE rawfile into a Python dictionary.
    :summarize_graph: Count the class instances by namespace in an RDF graph.
    :load_emt_dict: Load an RDF graph into Python dictionary using packaged SPARQL queries.
    :load_ic_dict: Load an RDF graph into Python dictionary from standalone power flow solution file.
    :list_dict_table: Print the fields and attributes of a Python dictionary loaded from SPARQL.
    :adhoc_sparql_dict: Load the result of a user-written SPARQL query into a Python dictionary.
    :build_bus_lists: Order the buses (connectivity nodes) sequentially.
    :get_swingbus_id: Find the CIM ConnectivityNode ID by matching the Name/Number from the original raw file.
    :build_system_graph: Auto-layout a diagram of the CIM network, returning a networkx graph.
    :load_system_graph: Load the networkx layout (graph) from a JSON file.
    :plot_system_graph: Plot the transmission system topology from a networkx layout (graph).
    :save_system_graph: Save the networkx layout (graph) to a JSON file.
"""

from __future__ import absolute_import

from .create_rdf import create_cim_rdf
from .create_sql import create_cim_sql
from .create_atp import create_atp
from .create_mpow import create_matpower

from .cim_summary import print_cim_summaries

from .cim_support import load_dynamics_defaults
from .cim_support import load_psse_meta
from .cim_support import load_psse_rawfile
from .cim_support import print_psse_table
from .cim_support import load_psse_dyrfile
from .cim_support import summarize_psse_dyrfile
from .cim_support import match_dyr_generators
from .cim_support import load_dynamics_mapping

from .cim_sparql import summarize_graph
from .cim_sparql import load_emt_dict
from .cim_sparql import load_ic_dict
from .cim_sparql import list_dict_table
from .cim_sparql import adhoc_sparql_dict

from .buslists import build_bus_lists
from .buslists import get_swingbus_id

from .plot_utils import build_system_graph
from .plot_utils import load_system_graph
from .plot_utils import plot_system_graph
from .plot_utils import save_system_graph

from .version import __version__


