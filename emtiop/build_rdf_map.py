"""Generate the triplets export schemas (rdf_map JSON) from emtiop.owl.

One file per serialization: 552_ED1 (rdf:ID="_<uuid>"), 552_ED2 (rdf:about="urn:uuid:<uuid>",
the default for new exports) and plain (bare identifiers, no header — what the rdflib
pipeline writes today).  Run from this directory after copy_profile.bat updated emtiop.owl.
"""
import json
import logging
from pathlib import Path

from cimtool_owl import SERIALIZATIONS, convert

CIM_NS = "http://www.ucaiug.org/grid18v15#"
EMT_NS = "http://opensource.ieee.org/emtiop01v01#"

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(message)s")
    here = Path(__file__).parent
    for serialization in SERIALIZATIONS:
        schema = convert(here / "emtiop.owl", serialization=serialization, keyword="EMTIOP",
                         namespace_map={"cim": CIM_NS, "emt": EMT_NS})
        target = here / f"emtiop_rdf_map_{serialization}.json"
        target.write_text(json.dumps(schema, indent=2) + "\n")
        print("wrote", target.name, len(schema["EMTIOP"]), "entries")
