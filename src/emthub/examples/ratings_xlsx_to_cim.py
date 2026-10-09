# Copyright (C) 2026 Meltran, Inc
"""Branch ratings spreadsheet (xlsx) -> CIM RDF/XML operational limits, with triplets.

Reads *matpower/ieee118ratings.xlsx* (from bus, to bus, kV, MVA rating, length in km),
finds each line's terminals in the IEEE118 network model, and writes a separate
*IEEE118_ratings.xml* holding one OperationalLimitSet + ApparentPowerLimit per line,
referencing the existing Terminal and the existing "Normal" OperationalLimitType.
The pattern — spreadsheet rows -> per-class tables -> triplets -> CIM XML — is the
same for any tabular source.

Command-line Arguments:
  **network** (str): path to the network model XML (default ../../../instances/IEEE118.xml)
  **ratings** (str): path to the workbook (default ../../../matpower/ieee118ratings.xlsx)
  **--serialization**: 552_ED2 (default), 552_ED1 or plain
"""
import argparse
import os

import pandas
from emthub.cim_triplets import REPO, SERIALIZATIONS, full_model, load_rdf_map, model_id, to_triplets, write_cimxml


def line_terminals(network):
    """One row per ACLineSegment: from bus, to bus, terminal 1 id (bus = ConnectivityNode name)."""
    bus = network.type_tableview("ConnectivityNode", string_to_number=False)["IdentifiedObject.name"].astype(int)
    terminals = network.type_tableview("Terminal", string_to_number=False)
    terminals["bus"] = terminals["Terminal.ConnectivityNode"].map(bus)
    lines = network.type_tableview("ACLineSegment", string_to_number=False).index
    ends = terminals[terminals["Terminal.ConductingEquipment"].isin(lines)].reset_index()
    ends = ends.pivot(index="Terminal.ConductingEquipment", columns="ACDCTerminal.sequenceNumber", values=["bus", "ID"])
    return pandas.DataFrame({"from": ends[("bus", "1")], "to": ends[("bus", "2")], "terminal": ends[("ID", "1")]})


def create_cim_ratings(network_path, ratings_path, serialization="552_ED2"):
    network = pandas.read_RDF([network_path])
    ratings = pandas.read_excel(ratings_path, sheet_name=0, names=["from", "to", "kV", "MVA", "km"])
    print("Read", len(ratings), "ratings from", os.path.basename(ratings_path))

    lines = line_terminals(network).reset_index(names="line")
    both_ways = pandas.concat([ratings, ratings.rename(columns={"from": "to", "to": "from"})])
    rated = lines.merge(both_ways, on=["from", "to"]).drop_duplicates("line").set_index("line")
    print("Matched", len(rated), "of", len(lines), "lines")

    limit_types = network.type_tableview("OperationalLimitType", string_to_number=False)
    normal = limit_types.index[limit_types["IdentifiedObject.name"] == "Normal"][0]
    limit_set = rated.index.map(lambda line: model_id(line, "ratingset"))
    limit = rated.index.map(lambda line: model_id(line, "rating"))
    tableviews = {
        "OperationalLimitSet": pandas.DataFrame({"IdentifiedObject.mRID": limit_set,
                                                 "IdentifiedObject.name": (rated["from"].astype(str) + "_" + rated["to"].astype(str) + "_xlsx").values,
                                                 "OperationalLimitSet.Terminal": rated["terminal"].values},
                                                index=pandas.Index(limit_set, name="ID")),
        "ApparentPowerLimit": pandas.DataFrame({"IdentifiedObject.mRID": limit,
                                                "IdentifiedObject.name": (rated["from"].astype(str) + "_" + rated["to"].astype(str) + "_xlsx_Normal").values,
                                                "ApparentPowerLimit.value": 1.0e6 * rated["MVA"].values,
                                                "OperationalLimit.OperationalLimitSet": limit_set,
                                                "OperationalLimit.OperationalLimitType": normal},
                                               index=pandas.Index(limit, name="ID")),
    }

    schema = load_rdf_map(serialization)
    case_id = network.loc[network["KEY"] == "Type"].pipe(lambda d: d.loc[d["VALUE"] == "EquipmentContainer", "ID"]).iloc[0]
    header = full_model(model_id(case_id, "ratings"), "IEEE118 branch ratings from ieee118ratings.xlsx",
                        os.path.getmtime(ratings_path), schema)
    data = to_triplets(tableviews, instance_id=case_id, header=header)
    out = os.path.splitext(os.path.basename(network_path))[0] + "_ratings.xml"
    write_cimxml(data, schema, out)
    print("Wrote", out, f"({serialization}),", len(data), "triplets")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("network", nargs="?", default=str(REPO / "instances" / "IEEE118.xml"))
    parser.add_argument("ratings", nargs="?", default=str(REPO / "matpower" / "ieee118ratings.xlsx"))
    parser.add_argument("--serialization", choices=SERIALIZATIONS, default=SERIALIZATIONS[0])
    args = parser.parse_args()
    create_cim_ratings(args.network, args.ratings, args.serialization)


if __name__ == "__main__":
    main()
