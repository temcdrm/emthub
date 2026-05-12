.. _target-queries:

Queries to CIM RDF
==================

The package invokes SPARQL queries against a CIM RDF (ttl, xml, or json) 
file to load Python dictionaries. The dictionary keys and field names use 
CIM attribute names, which are fully qualified with the CIM class name 
only as needed to resolve ambiguities. The tables in this section document 
the keys and field names for each Python dictionary, along with the 
corresponding CIM fully qualified attribute names. Each dictionary is 
briefly described, with links to the main CIM classes that the dictionary 
is based on.
 
The **CIM Attribute** begins with a CIM namespace as follows:
 
- **c:** denotes the prefix for base CIM
- **e:** denotes the prefix for an *Emtiop* extension
 
Some queries may return multiple rows for each dictionary key. These queries
are indicated with an asterisk, e.g., `EMTIEEECigreDLLParameters*`. Those
dictionaries must be iterated using the Python *.items()* construct.
 
.. include:: query_doc.rst
 
