# EMTIOP Profile

CIM extensions and profile for EMT model portability. Files of interest include:

- _copy_profile.bat_: Copies the [CIMTOOL](https://cimtool.ucaiug.io/) output into this repository.
- _emtiop.html_: Documentation of the EMTIOP profile, output from CIMTOOL.
- _emtiop.owl_: The EMTIOP profile for CIMTOOL.
- _emtiop.sql_: SQL statements to create a database, output from CIMTOOL.
- _emtiop_lite.sql_: Hand-edited version of _emtiop.sql_ to work with _sqlite3_.
- _Emtiop.xmi_: CIM extension UML that complements the CIM Grid model UML.
- _merge_dynamics_defaults.py_: Combines new types and default values from _profile_attributes.json_ into the base file of _dynamics_defaults.json_.
- _process_html.py_: Corrects the HTML coding in profile documentation output from CIMTOOL.
- _profile_attributes.json_: CIM attribute names, types, and default values found in _emtiop.html_.

Copyright &copy; 2024-26, Meltran, Inc
