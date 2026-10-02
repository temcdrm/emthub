.. _target-triplets:

Tabular Workflow with triplets
==============================

`triplets <https://pypi.org/project/triplets/>`_ is a Python package that
holds a CIM RDF model as one pandas DataFrame of ``ID, KEY, VALUE,
INSTANCE_ID`` rows and moves it between CIM RDF/XML, spreadsheets, SPARQL
and SHACL. This page shows how it is used with the EMTHub examples. The
scripts live next to the rdflib-based ones in ``src/emthub/examples`` and
do not replace them.

Install the optional dependencies with::

    pip install "triplets[validation,excel]"

or ``pip install emthub[triplets]``.

Reading and writing CIM RDF/XML
-------------------------------

.. code-block:: python

    import pandas
    import triplets                       # registers pandas.read_RDF and the export methods

    data = pandas.read_RDF(["IEEE118.xml", "IEEE118_ic.xml"])
    data.type_tableview("ACLineSegment")  # one wide table per class, index = mRID
    data.export_to_cimxml(rdf_map=schema["EMTIOP"], export_type="xml_per_instance")

``schema`` is the export schema described below. Every attribute is written
under the namespace and identifier convention the schema prescribes, so the
data itself carries only bare identifiers and plain values.

Typed values (``rdf:datatype``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

IEC 61970-552 files carry no ``rdf:datatype``: the type of each value comes
from the profile, and CIMTool and the CGMES tools read it from there.
``validate_cim.py`` checks every value against the profile's ``xsd:type``
either way. Generic RDF tools can use typed literals (numeric comparisons in
SPARQL, for example); ``datatypes=True`` writes them from the schema:

.. code-block:: python

    from triplets.export import export_to_cimxml
    from emthub.cim_triplets import load_rdf_map

    schema = load_rdf_map("552_ED2")            # data with a FullModel header
    export_to_cimxml(data, rdf_map=schema, export_type="xml_per_instance",
                     datatypes=True)

    plain = load_rdf_map("plain")["EMTIOP"]     # header-less data
    export_to_cimxml(data, rdf_map=plain, export_type="xml_per_instance",
                     datatypes=True)

.. code-block:: xml

    <cim:SvVoltage.v rdf:datatype="http://www.w3.org/2001/XMLSchema#float">135979.818</cim:SvVoltage.v>
    <cim:IdentifiedObject.name>BUS1</cim:IdentifiedObject.name>

``xsd:string`` values stay untyped. Without ``datatypes=True`` the output is
unchanged. The option uses the lxml engine of triplets (``engine="auto"``
picks it).

Element order is kept
^^^^^^^^^^^^^^^^^^^^^

triplets writes objects in the order of the rows it holds and attributes in
the order of their rows within the object. Nothing is sorted or hashed on the
way out. Consequences:

* a file read with ``pandas.read_RDF`` and written back comes out with the
  same object and attribute order it had, for all nine files in
  ``instances/`` (checked on this repository);
* two runs on the same inputs produce byte-identical output, so the
  post-sorting step in ``instances/sort_xml.py`` is not needed for files
  written this way;
* the order of a spreadsheet or CSV row set becomes the order of the objects
  in the XML, which keeps diffs between model versions readable.

Export schema from the EMTIOP profile
-------------------------------------

*emtiop/emtiop.owl* is the CIMTool profile. ``emtiop/cimtool_owl.py``
converts it to the JSON export schema triplets uses (classes with their
inherited properties, cardinalities, datatypes, enumeration values and
association ranges; namespaces are taken from the base model URIs, i.e.
``cim:`` and ``emt:``, not from the profile namespace). Run
``python build_rdf_map.py`` in ``emtiop/`` after updating the profile. Three
files are generated, one per serialization:

==============================  ================================================================
File                            Identifiers
==============================  ================================================================
emtiop_rdf_map_552_ED2.json     ``rdf:about="urn:uuid:…"``, ``rdf:resource="urn:uuid:…"``, with an
                                ``md:FullModel`` header (IEC 61970-552 Ed. 2). **Default** for new files.
emtiop_rdf_map_552_ED1.json     ``rdf:ID="_…"``, ``rdf:resource="#_…"``, with header (IEC 61970-552 Ed. 1).
emtiop_rdf_map_plain.json       Bare identifiers, no header — what ``ic_to_rdf.py`` and ``create_rdf.py`` write today.
==============================  ================================================================

Each file holds one section, ``{"EMTIOP": {...}}``. Pass ``schema["EMTIOP"]``
to the exporter for header-less data and the whole ``schema`` to the
validator (``profiles=["EMTIOP"]``); ``emthub.cim_triplets.write_cimxml``
picks the right one. The plain schema's section also holds
``AttributeDatatypes``, the attribute types once more, nested: triplets reads
the types for ``datatypes=True`` one level below the map it is given, and
header-less data is exported with the section itself. It is never a class or
KEY, so exports without ``datatypes=True`` are unchanged.

Four restrictions in *emtiop.owl* carry a cardinality but no
``owl:allValuesFrom`` (``ns#IdentifiedObject.Name`` and the
``ConductingEquipment.From/ToConnectivityNode`` pair in the old
``emtiop#`` namespace); the converter skips them with a warning. The
profile also refers to CIM datatypes in two namespaces
(``http://www.ucaiug.org/ns#Voltage`` and ``grid18v15#Voltage``); both are
mapped by local name.

RAW to CIM RDF/XML
------------------

``raw_to_rdf_triplets.py`` writes the same model as ``raw_to_rdf.py`` from
the same inputs (``<case>.raw``, ``<case>.dyr``, ``<case>_mRIDs.dat`` and
``<case>_Network.json`` for the bus diagram), built as one table per class:

* the network equipment: container, limit types, base voltages, nodes and
  bus diagram, lines, series compensators, switches, loads, shunts and
  two-winding transformers, with their terminals and ratings;
* generators with their generating units, an EnergySource at the swing bus
  when there are none;
* the dyr dynamics: machine models, detailed models with their parameter
  values, and the model types with their parameter descriptors;
* an IBR or rotating machine plant with its point of common coupling per
  generator that has a step-up transformer; rotating machine GSUs become
  ``Yd1``.

Run it in ``test/`` after ``emthub-extract-case``::

    python raw_to_rdf_triplets.py 1                        # IEEE118.xml, 552 Ed. 2
    python raw_to_rdf_triplets.py 1 --serialization plain  # bare identifiers, as raw_to_rdf.py

With ``--serialization plain`` the output holds exactly the triples
``raw_to_rdf.py`` writes, which are the committed ``instances/<case>.xml``
(cases 0–3, compared triple by triple). Only CIM RDF/XML is written, no TTL or
JSON-LD. Enumeration values are given by local name
(``WindingConnection.D``); the schema adds the namespace.

mRIDs come from ``<case>_mRIDs.dat``. ``raw_to_rdf.py`` gives any object the
map lacks a new uuid4 and rewrites the map; this script stops and lists them
instead. ``--new-mrids`` accepts them: each gets a new uuid4, appended to
the map, so the existing entries never change.

CSV to CIM RDF/XML
------------------

``ic_to_rdf_triplets.py`` reads the same three MATPOWER result files as
``ic_to_rdf.py`` (``<case>mb.txt``, ``<case>mg.txt``, ``<case>mbr.txt``)
and writes the same state variables. Instead of adding one rdflib triple
at a time it builds one wide table per class, index = identifier, columns =
``Class.attribute``, and hands the dictionary of tables to triplets:

.. code-block:: python

    tableviews = {
        "TopologicalNode":  pandas.DataFrame(index=pandas.Index(tn, name="ID")),
        "ConnectivityNode": pandas.DataFrame({"ConnectivityNode.TopologicalNode": tn.values},
                                             index=pandas.Index(cn, name="ID")),
        "SvVoltage":        pandas.DataFrame({"SvVoltage.TopologicalNode": tn.values,
                                              "SvVoltage.v": (1000.0 * buses["kVbase"] * buses["Vpu"]).values,
                                              "SvVoltage.angle": buses["Vdeg"].values},
                                             index=pandas.Index(cn + "_SvV", name="ID")),
        "SvPowerFlow":      power_flows(branches, generators),
    }
    data = to_triplets(tableviews, instance_id=case["id"], header=full_model(...))
    write_cimxml(data, schema, f"{case['name']}_ic.xml")

Run it in ``test/`` after ``mpow.py``::

    python ic_to_rdf_triplets.py 1                        # IEEE118_ic.xml, 552 Ed. 2
    python ic_to_rdf_triplets.py 1 --serialization plain  # same content as ic_to_rdf.py writes

With ``--serialization plain`` the output holds exactly the triples of the
committed ``instances/IEEE118_ic.xml``; with the default it adds the
``md:FullModel`` header and ``urn:uuid:`` identifiers.

Excel to CIM RDF/XML
--------------------

``ratings_xlsx_to_cim.py`` turns *matpower/ieee118ratings.xlsx* (from bus,
to bus, kV, MVA, km) into an ``OperationalLimitSet`` with one
``ApparentPowerLimit`` per line, attached to the line's first ``Terminal``
found in *instances/IEEE118.xml* and to the existing ``Normal``
``OperationalLimitType``::

    python ratings_xlsx_to_cim.py           # writes IEEE118_ratings.xml

The spreadsheet rows are joined to the network with pandas (bus numbers come
from the ``ConnectivityNode`` names, terminals from their
``sequenceNumber``), then converted like the CSV case. Any other tabular
source follows the same three steps: read into pandas, shape one table per
class, export.

CIM RDF/XML to CSV and back
---------------------------

A model can be edited as one CSV file per class and written back:

.. code-block:: python

    import glob
    import pandas
    import triplets
    from triplets.tools import tableviews_to_triplets
    from emthub.cim_triplets import load_rdf_map, write_cimxml

    data = pandas.read_RDF(["IEEE39.xml"])          # CIM RDF/XML -> csv/<Class>.csv
    for cls in data.query("KEY == 'Type'").VALUE.unique():
        data.type_tableview(cls, string_to_number=False, multivalue=True).to_csv(f"csv/{cls}.csv")

    tables = {path.split("/")[-1][:-4]: pandas.read_csv(path, index_col="ID", dtype=str)
              for path in glob.glob("csv/*.csv")}   # csv/<Class>.csv -> CIM RDF/XML
    back = tableviews_to_triplets(tables, multivalue=True)
    back["INSTANCE_ID"] = data.INSTANCE_ID.iloc[0]
    write_cimxml(back, load_rdf_map("552_ED2"), "IEEE39_from_csv.xml")

``string_to_number=False`` and ``dtype=str`` keep every value as written,
and ``multivalue=True`` keeps properties with several values (e.g.
``ConnectedFacility.Equipments``) as one list cell. On IEEE39 the file
written back holds the same triples, except empty strings: CSV cannot tell
an empty value from a missing one.

``cim-spreadsheet -i IEEE39.xml -o IEEE39.xlsx`` writes one sheet per class
for viewing, with numbers as numeric cells. Its way back
(``--direction to-cim``) fails in triplets 0.2.0
(https://github.com/Haigutus/triplets/issues/125).

Validation
----------

``validate_cim.py`` checks CIM RDF/XML files in two passes and writes the
findings as CSV and `SARIF <https://sarifweb.azurewebsites.net/>`_::

    python validate_cim.py ../instances/*.xml        # or a list of files

#. **Profile conformance** from the export schema: cardinality, datatypes,
   enumeration membership and association targets (subclass-aware). This is
   the scripted counterpart of importing an instance into CIMTool and
   checking it against *emtiop.owl* (see :ref:`target-roadmap-profile`).
#. **SHACL rules** from *emtiop/emtiop_shapes.ttl*: value ranges and
   structural rules the profile cannot express, such as positive base
   voltages, voltage angles within ±180°, terminal sequence numbers 1–3,
   and every ``ConnectivityNode`` having a ``Terminal``. Add rules there as
   plain SHACL.

Files ``<case>.xml``, ``<case>_ic.xml`` and ``<case>_ratings.xml`` are
validated together as one model. On the committed instance files the only
finding is ``ShuntCompensator.sections`` written as an integer where the
profile declares a float.
