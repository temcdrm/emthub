CIM Extension and Profile
=========================

The CIM extensions and profile for EMT are in the `emthub/emtiop` repository folder:

1) *emtiop.html* contains the class and attribute documentation built from CIMTool
2) *emtiop.owl* contains the profile for CIMTool
3) *emtiop.sql* contains the CIMTool-generated statements to build a SQL database; these don't work with Pythons _sqlite_ package
4) *Emtiop.xmi* contains the CIM extensions, for importing into a UML editor that has the core CIM UML
5) *emtiop_sqlite.sql* contains hand-edits to *emtiop.sql* that work with _sqlite_

.. raw:: html
   :file: ../emtiop/emtiop.html
