# Copyright (C) 2026 Meltran, Inc
"""Validate CIM RDF/XML files against the EMTIOP profile and the EMTIOP SHACL shapes.

Two checks, both from triplets.validation:

* schema conformance from *emtiop/emtiop_rdf_map_552_ED2.json* — cardinality,
  datatypes, enumeration membership, association targets — the scripted
  counterpart of importing an instance into CIMTool and checking it against
  *emtiop.owl*;
* SHACL rules from *emtiop/emtiop_shapes.ttl* — value ranges and structure the
  profile cannot express.

Files named ``<case>.xml``, ``<case>_ic.xml`` and ``<case>_ratings.xml`` are
validated together as one model (the state variables reference the network).
Findings are printed and written as ``<name>_violations.csv`` and
``<name>.sarif``; the exit code is 1 when any finding has severity Violation.

Command-line Arguments:
  **files** (str): CIM XML files; default ../../../instances/*.xml
"""
import argparse
import glob
import os
import re
from collections import defaultdict

import pandas
from triplets.validation import validate, validate_schema
from triplets.validation.sarif import export_to_sarif
from triplets.validation.shacl_report import violations_to_csv
from emthub.cim_triplets import EMTIOP, REPO, load_rdf_map

SHAPES = EMTIOP / "emtiop_shapes.ttl"


def group_by_case(files):
    """{'IEEE118': ['.../IEEE118.xml', '.../IEEE118_ic.xml'], ...}"""
    groups = defaultdict(list)
    for path in sorted(files):
        groups[re.sub(r"_(ic|ratings)$", "", os.path.splitext(os.path.basename(path))[0])].append(path)
    return groups


def check_mrid(data):
    """IdentifiedObject.mRID must repeat the object's own identifier (not expressible in core SHACL)."""
    mrid = data[data["KEY"] == "IdentifiedObject.mRID"]
    bad = mrid[mrid["ID"].str.upper() != mrid["VALUE"].str.upper()]
    return pandas.DataFrame({"ID": bad["ID"], "KEY": "IdentifiedObject.mRID", "VALUE": bad["VALUE"],
                             "VIOLATION_TYPE": "emthub:mRID", "MESSAGE": "mRID differs from rdf:about",
                             "SEVERITY": "Violation", "SOURCE_SHAPE": "validate_cim.check_mrid"})


def validate_case(name, files, schema):
    data = pandas.read_RDF(files)
    data["INSTANCE_ID"] = name   # one model, even when split over network + state variable files
    schema_violations = validate_schema(data, schema, profiles=["EMTIOP"])
    shacl_violations = validate(data, str(SHAPES), rdf_map=schema)
    violations = pandas.concat([schema_violations, shacl_violations, check_mrid(data)], ignore_index=True)
    print(f"{name}: {len(files)} file(s), {(data['KEY'] == 'Type').sum()} objects, {len(violations)} violation(s)")
    if len(violations):
        print(violations.groupby(["VIOLATION_TYPE", "KEY"], dropna=False).size().to_string(), "\n")
        violations_to_csv(violations, f"{name}_violations.csv")
        export_to_sarif(violations, data=data, rdf_map=schema, path=f"{name}.sarif")
    return violations


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("files", nargs="*", default=glob.glob(str(REPO / "instances" / "*.xml")))
    args = parser.parse_args()
    schema = load_rdf_map("552_ED2")
    findings = [validate_case(name, files, schema) for name, files in group_by_case(args.files).items()]
    errors = sum((frame["SEVERITY"] == "Violation").sum() for frame in findings)
    raise SystemExit(1 if errors else 0)   # warnings (e.g. lexical form) do not fail the run


if __name__ == "__main__":
    main()
