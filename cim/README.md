# CIM Examples

Scripts and rawfiles for the _XfmrSat_, _IEEE39_, _IEEE118_, and _WECC240_ examples.
Outputs are written to sibling _../../atp/data_ and _../matpower_ directories.

The scripts fully support RDF XML and Turtle (TTL) files via Python's _rdflib_ module.
Support for SQL is partially implemented via Python's _sqlite3_ module.


:construction:**Caveat**: The SPARQL currently implemented uses
*IdentifiedObject.name* as the primary key, but this is not guaranteed to be unique
in the CIM, not even within types. These queries will be changed to use
*IdentifiedObject.mRID* as the primary key. Do not base new Python code or SPARQL
queries on the examples in this repository, until this notice is removed. :construction:

For example, to process the _IEEE39_ network, invoke the following steps in order:

- _python raw_to_emtiop.py 2_, which creates _ieee39.ttl_ and _ieee39.xml_. These don't necessarily have bus locations.
- _python bps_make_graph.py 2_, which creates or updates bus locations.
- _python raw_to_emtiop.py 2_, which recreates _ieee39.ttl_ and _ieee39.xml_ with bus locations.
- _python bps_make_mpow.py 2_, which creates _../matpower/IEEE39.m_. Run this to create or update initial conditions for EMT simulation in ATP.
- _python cim_to_atp.py 2_, which creates _../atp/data/IEEE39_net.atp_ for EMT simulation in ATP.

Files of interest include:

- _emtiop.html_: Documentation of the EMTIOP profile, output from [CIMTOOL](https://cimtool.ucaiug.io/).
- _dynamics_defaults.json_: Specifies the units and default values for dynamic components used in the three IBR system examples.
- _psseraw.json_: Identifies the parameters and columns of interest in three versions of raw file.
- _emtiop.owl_: The EMTIOP profile for [CIMTOOL](https://cimtool.ucaiug.io/).
- _bps_make_graph.py_: Uses the Python _networkx_ package to create auto-layout diagrams for network model visualization. Command-line argument 0..2 selects the case.
- _bps_make_mpow.py_: Creates MATPOWER models to _../matpower_ from input _\*.ttl_ files. Command-line argument 0..2 selects the case.
- _cim_sparql.py_: Tests local SPARQL queries against _xml_ files. Command-line argument 0..3 selects the case.
- _cim_sql.py_:  Tests local SQL queries against _emtiop.db_. Command-line argument 0..1 selects the case.
- _cim_summary.py_: Lists the classes and their instance counts found in four example _\*.ttl_ files.
- _cim_to_atp.py_:  Creates ATP netlist to _../../atp/data/\*_net.atp_ from input _\*.ttl_ files. Command-line argument 0..3 selects the case.
- _create_db.py_: Creates a local SQL database from _emtiop_lite.sql_.
- _plot_bps.py_: Displays a network model visualization from _raw/\*Network.json_ files. Command-line argument 0..2 selects the case.
- _raw_to_emtiop.py_: Creates local Turtle (_\*.ttl_) and XML RDF (_\*.xml_) files from input raw files. Command-line argument 0..3 selects the case.
- _sparql_fragments.py_: Helper file that creates SPARQL query elements from _dynamics_defaults.json_. Use for convenience when adding new dynamics classes from CIM to the profile.
- _sql_to_atp.py_: Partially implemented ATP netlisting from a local SQL database.
- _test_atp_fit.py_: Testing floating-point value output in the strict FORTRAN format used by ATP.
- _emtiop.sql_: SQL statements to create a database, output from [CIMTOOL](https://cimtool.ucaiug.io/).
- _emtiop_lite.sql_: Hand-edited version of _emtiop.sql_ to work with _sqlite3_.
- _\*.ttl_: CIM network models, in Turtle format, output from _raw_to_emtiop.py_, for the four examples. 
- _sparql_queries.txt_: SPARQL queries to run interactively in a web browser with Blazegraph; useful in developing new queries.
- _Emtiop.xmi_: CIM extension UML that complements the CIM Grid model UML.
- _sparql_queries.xml_: SPARQL queries loaded into Python.

In the rawfile subdirectory:

- _raw/\*mrids.dat_: Persistent unique identifiers for CIM data.
- _raw/\*.dyr_: Raw files with dynamics data.
- _raw/\*_Network.json_: Auto-layout bus locations and supplemental data for network model visualization. Created by _bps_make_graph.py_.
- _raw/\*.raw_: Raw files with power flow data.
- _raw/XfmrSat.dat_: Parameter calculations for the transformer saturation example.

Copyright &copy; 2024-26, Meltran, Inc
