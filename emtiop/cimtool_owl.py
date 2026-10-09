"""CIMTool OWL profile -> triplets export schema (rdf_map).

CIMTool writes a profile as OWL: every named class is an ``owl:Class`` whose
``rdfs:subClassOf`` points at blank ``owl:Restriction`` nodes, one per property
constraint (``owl:onProperty`` + ``owl:minCardinality`` / ``owl:maxCardinality``
/ ``owl:allValuesFrom``).  triplets' export and schema validation want the
flat JSON "rdf_map" that ``triplets.rdfs_tools.cim_rdfs_to_json`` produces
from ENTSO-E RDFS.  This module produces the same shape from CIMTool OWL.

Namespaces of classes, properties, enumeration values and datatypes come from
the base model URIs the profile refers to (``grid18v15#``, ``emtiop01v01#``),
never from the profile namespace itself.

Vendored in emthub until it moves into ``triplets.rdfs_tools``.
Works with triplets >= 0.2.0.

Usage::

    python cimtool_owl.py emtiop.owl --keyword EMTIOP --serialization 552_ED2 \
        --ns cim=http://www.ucaiug.org/grid18v15# --ns emt=http://opensource.ieee.org/emtiop01v01# \
        -o emtiop_rdf_map_552_ED2.json
"""
import argparse
import io
import json
import logging
from pathlib import Path

from triplets.parser import parse
from triplets.rdfs_tools.cim_rdfs_to_json import cgmes_data_types_map

logger = logging.getLogger(__name__)

RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
OWL = "http://www.w3.org/2002/07/owl#"
RDFS = "http://www.w3.org/2000/01/rdf-schema#"
XSD = "http://www.w3.org/2001/XMLSchema#"
MD = "http://iec.ch/TC57/61970-552/ModelDescription/1#"
RDF_NIL = f"{RDF}nil"

# CIM datatype local name -> xsd type; the profile only names the datatype
XSD_TYPES = {**cgmes_data_types_map, "RealEnergy": "xsd:float"}

# IEC 61970-552 serialization flavours + "plain" (bare identifiers, no header —
# what emthub's rdflib pipeline writes today)
SERIALIZATIONS = {
    "552_ED1": {"conformsTo": "urn:iso:std:iec:61970-552:2013",
                "id": (f"{{{RDF}}}ID", "_"), "resource": "#_", "header": True},
    "552_ED2": {"conformsTo": "urn:iso:std:iec:61970-552:2016",
                "id": (f"{{{RDF}}}about", "urn:uuid:"), "resource": "urn:uuid:", "header": True},
    "plain":   {"conformsTo": None,
                "id": (f"{{{RDF}}}about", ""), "resource": "", "header": False},
}

_ABOUT = {"attribute": f"{{{RDF}}}about", "value_prefix": "urn:uuid:"}
_RESOURCE_UUID = {"attribute": f"{{{RDF}}}resource", "value_prefix": "urn:uuid:"}


def header_entries():
    """md:FullModel header (IEC 61970-552) — the same in Ed1 and Ed2."""
    attribute = {"type": "Attribute", "namespace": MD, "xsd:minOccours": "0", "xsd:maxOccours": "1",
                 "xsd:type": "xsd:string"}
    reference = {"type": "Association", "namespace": MD, "xsd:minOccours": "0", "xsd:maxOccours": "n",
                 "xsd:type": "xsd:anyURI", "range": "FullModel", "attrib": _RESOURCE_UUID}
    entries = {
        "Model.created": {**attribute, "xsd:type": "xsd:dateTime"},
        "Model.scenarioTime": {**attribute, "xsd:type": "xsd:dateTime"},
        "Model.description": attribute,
        "Model.version": attribute,
        "Model.modelingAuthoritySet": {**attribute, "xsd:type": "xsd:anyURI"},
        "Model.profile": {**attribute, "xsd:maxOccours": "n", "xsd:type": "xsd:anyURI"},
        "Model.DependentOn": reference,
        "Model.Supersedes": reference,
    }
    entries["FullModel"] = {"attrib": _ABOUT, "type": "Class", "inheritance": ["FullModel", "Model"],
                            "stereotyped": False, "namespace": MD, "parameters": list(entries)}
    return entries


def load(path):
    """Parse an OWL profile losslessly (full URIs kept).

    triplets 0.2.0 only accepts .xml/.rdf names, so the file is handed over
    under an .rdf alias.
    """
    buffer = io.BytesIO(Path(path).read_bytes())
    buffer.name = f"{Path(path).stem}.rdf"
    return parse([buffer], engine="python_lxml_pandas", shorten_resources=False)


def _namespace(uri):
    return uri.rsplit("#", 1)[0] + "#"


def _local(uri):
    return uri.rsplit("#", 1)[-1]


def _as_xsd(uri):
    return "xsd:" + _local(uri) if uri.startswith(XSD) else None


def convert_profile(data, serialization="552_ED2", keyword="PROFILE", namespace_map=None):
    """OWL profile frame -> ``{keyword: section}`` export schema."""
    ser = SERIALIZATIONS[serialization]
    rows = {ID: list(zip(group["KEY"], group["VALUE"])) for ID, group in data.groupby("ID", sort=False)}

    def values(ID, key):
        return [value for k, value in rows.get(ID, ()) if k == key]

    def first(ID, key):
        found = values(ID, key)
        return found[0] if found else None

    def stereotypes(ID):
        return {_local(value) for value in values(ID, "hasStereotype")}

    def rdf_list(head):
        while head and head != RDF_NIL:
            yield first(head, "first")
            head = first(head, "rest")

    def ancestors(cls):
        """Class and its profile ancestors, nearest first (CIMTool does not flatten inheritance)."""
        chain, pending = [], [cls]
        while pending:
            current = pending.pop(0)
            if current in chain:
                continue
            chain.append(current)
            pending += [value for value in values(current, "subClassOf") if value.startswith("#")]
        return chain

    def base_uri(cls):
        """The base-model class this profile class restricts — source of its namespace."""
        for value in values(cls, "subClassOf"):
            if value.startswith("http") and _local(value) == cls[1:]:
                return value
        raise ValueError(f"{cls}: no base-model class among rdfs:subClassOf")

    def restrictions(cls):
        """property URI -> merged {minCardinality, maxCardinality, allValuesFrom} across ancestors."""
        merged = {}
        for ancestor in ancestors(cls):
            for node in values(ancestor, "subClassOf"):
                if node.startswith(("#", "http")) or f"{OWL}Restriction" not in values(node, "type"):
                    continue
                constraint = merged.setdefault(first(node, "onProperty"), {})
                for key in ("minCardinality", "maxCardinality", "allValuesFrom"):
                    if constraint.get(key) is None:
                        constraint[key] = first(node, key)
        return merged

    profile, skipped = {}, set()

    def property_entry(uri, constraint):
        target = constraint["allValuesFrom"]
        if target is None:
            if uri not in skipped:
                logger.warning("%s: cardinality without owl:allValuesFrom — skipped", uri)
            skipped.add(uri)
            return None
        entry = {"namespace": _namespace(uri), "xsd:minOccours": constraint["minCardinality"] or "0",
                 "xsd:maxOccours": constraint["maxCardinality"] or "1"}
        if f"{RDFS}Datatype" in values(target, "type"):
            equivalent = first(target, "equivalentClass")
            xsd = _as_xsd(equivalent) or XSD_TYPES.get(_local(equivalent))
            entry["type"] = "Attribute"
            if not _as_xsd(equivalent):
                entry["dataType"] = _local(equivalent)
                profile.setdefault(_local(equivalent), {"type": "CIMDatatype", "namespace": _namespace(equivalent),
                                                        **({"xsd:type": xsd} if xsd else {})})
            if xsd:
                entry["xsd:type"] = xsd
            return entry
        declared = next(value for value in values(target, "subClassOf") if value.startswith("http"))
        entry.update({"xsd:type": "xsd:anyURI", "range": _local(declared)})
        if "enumeration" in stereotypes(target):
            members = [_local(member) for member in rdf_list(first(f"#{_local(declared)}", "oneOf"))]
            entry.update({"type": "Enumeration", "values": members,
                          "attrib": {"attribute": f"{{{RDF}}}resource", "value_prefix": _namespace(declared)}})
            for member in members:
                profile.setdefault(member, {"type": "EnumerationValue", "namespace": _namespace(declared)})
        else:
            entry.update({"type": "Association", "xsd:maxOccours": constraint["maxCardinality"] or "n",
                          "attrib": {"attribute": f"{{{RDF}}}resource", "value_prefix": ser["resource"]}})
        return entry

    named = [ID for ID in rows if ID.startswith("#") and f"{OWL}Class" in values(ID, "type")]
    for cls in named:
        if "concrete" not in stereotypes(cls):
            continue
        parameters = []
        for uri, constraint in restrictions(cls).items():
            name = _local(uri)
            if name not in profile:
                entry = property_entry(uri, constraint)
                if entry is None:
                    continue
                profile[name] = entry
            parameters.append(name)
        profile[cls[1:]] = {"attrib": {"attribute": ser["id"][0], "value_prefix": ser["id"][1]},
                            "type": "Class", "inheritance": [ancestor[1:] for ancestor in ancestors(cls)],
                            "stereotyped": False, "namespace": _namespace(base_uri(cls)),
                            "parameters": parameters}

    namespace_map = {"rdf": RDF, **(namespace_map or {})}
    if ser["header"]:
        profile.update(header_entries())
        namespace_map["md"] = MD

    ontology = next(ID for ID in rows if f"{OWL}Ontology" in values(ID, "type"))
    xml_base = first(next(ID for ID in rows if "NamespaceMap" in values(ID, "Type")), "xml_base") or ""
    profile["ProfileMetadata"] = {"keyword": keyword, "title": first(ontology, "label"),
                                  "versionIRI": xml_base + "#", "imports": values(ontology, "imports"),
                                  "serialization": serialization, "conformsTo": ser["conformsTo"]}
    serialized = {"Class", "Attribute", "Association", "Enumeration", "EnumerationValue"}
    used = {entry["namespace"] for entry in profile.values()
            if isinstance(entry, dict) and entry.get("type") in serialized}
    for uri in sorted(used - set(namespace_map.values())):
        namespace_map[uri.rstrip("#").rsplit("/", 1)[-1]] = uri
    profile["ProfileNamespaceMap"] = namespace_map
    return {keyword: profile}


def convert(path, **kwargs):
    return convert_profile(load(path), **kwargs)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("owl")
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("--keyword", default="PROFILE")
    parser.add_argument("--serialization", choices=SERIALIZATIONS, default="552_ED2")
    parser.add_argument("--ns", action="append", default=[], metavar="PREFIX=URI")
    args = parser.parse_args(argv)
    namespace_map = dict(item.split("=", 1) for item in args.ns)
    schema = convert(args.owl, serialization=args.serialization, keyword=args.keyword, namespace_map=namespace_map)
    Path(args.output).write_text(json.dumps(schema, indent=2) + "\n")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    main()
