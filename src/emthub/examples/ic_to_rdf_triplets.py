# Copyright (C) 2026 Meltran, Inc
"""MATPOWER initial conditions (CSV) -> CIM RDF/XML state variables, with triplets.

Same inputs and output objects as *ic_to_rdf.py*, built as per-class tables
instead of one rdflib triple at a time, and written in a fixed order — two
runs on the same inputs give byte-identical files, so no post-sorting step.

Command-line Arguments:
  **index** (int): case number from 0 to **3**.
  **--serialization**: 552_ED2 (default, rdf:about="urn:uuid:..."), 552_ED1 (rdf:ID="_...") or plain
  (bare identifiers, no header, as *ic_to_rdf.py* writes).
"""
import argparse
import os

import numpy
import pandas
import emthub.api as emthub
from emthub.cim_triplets import SERIALIZATIONS, full_model, load_rdf_map, model_id, to_triplets, write_cimxml


def power_flows(branches, generators):
    """SvPowerFlow rows: both ends of every branch, then generator terminals (load convention)."""
    eq = branches["t1_id"].str.split("_").str[0]
    kind = numpy.where(branches["Ratio"] > 0.0, "_SvXfmrPF_", "_SvLinePF_")
    ends = [pandas.DataFrame({"SvPowerFlow.Terminal": branches[f"t{n}_id"].values,
                              "SvPowerFlow.p": 1.0e6 * branches[f"P{end}"].values,
                              "SvPowerFlow.q": 1.0e6 * branches[f"Q{end}"].values},
                             index=pandas.Index(eq + kind + str(n), name="ID"))
            for n, end in ((1, "from"), (2, "to"))]
    gen_eq = generators["CEQ t1_id"].str.split("_").str[0]
    ends.append(pandas.DataFrame({"SvPowerFlow.Terminal": generators["CEQ t1_id"].values,
                                  "SvPowerFlow.p": -1.0e6 * generators["Pg"].values,
                                  "SvPowerFlow.q": -1.0e6 * generators["Qg"].values},
                                 index=pandas.Index(gen_eq + "_SvGenPF", name="ID")))
    return pandas.concat(ends)


def create_cim_ic(case, serialization="552_ED2"):
    name = case["name"]
    buses = pandas.read_csv(f"{name}mb.txt", skipinitialspace=True)
    generators = pandas.read_csv(f"{name}mg.txt", skipinitialspace=True)
    branches = pandas.read_csv(f"{name}mbr.txt", skipinitialspace=True)
    print("Read", len(buses), "buses,", len(generators), "generators,", len(branches), "branches")

    cn = buses["CN id"]
    tn = cn + "_TN"   # temporary TopologicalNode for compliance with base CIM
    tableviews = {
        "TopologicalNode": pandas.DataFrame(index=pandas.Index(tn, name="ID")),
        "ConnectivityNode": pandas.DataFrame({"ConnectivityNode.TopologicalNode": tn.values},
                                             index=pandas.Index(cn, name="ID")),
        "SvVoltage": pandas.DataFrame({"SvVoltage.TopologicalNode": tn.values,
                                       "SvVoltage.v": (1000.0 * buses["kVbase"] * buses["Vpu"]).values,
                                       "SvVoltage.angle": buses["Vdeg"].values},
                                      index=pandas.Index(cn + "_SvV", name="ID")),
        "SvPowerFlow": power_flows(branches, generators),
    }

    schema = load_rdf_map(serialization)
    header = full_model(model_id(case["id"], "ic"), f"{name} initial conditions",
                        os.path.getmtime(f"{name}mb.txt"), schema)
    data = to_triplets(tableviews, instance_id=case["id"], header=header)
    write_cimxml(data, schema, f"{name}_ic.xml")
    print("Wrote", f"{name}_ic.xml", f"({serialization}),", len(data), "triplets")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("index", type=int, nargs="?", default=0)
    parser.add_argument("--serialization", choices=SERIALIZATIONS, default=SERIALIZATIONS[0])
    args = parser.parse_args()
    create_cim_ic(emthub.CASES[args.index], args.serialization)


if __name__ == "__main__":
    main()
