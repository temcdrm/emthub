# Copyright (C) 2025-2026 Meltran, Inc

"""CIM RDF/XML from PSS/E RAW and DYR files, built as tables with triplets.

Writes the same model as *raw_to_rdf.py* (*create_rdf.create_cim_rdf*): the network
equipment, generators with their generating units, the dyr dynamics (machine models and
detailed models with their model types and parameter descriptors), an EnergySource at
the swing bus when there are no generators, and the IBR and rotating machine plants with
their points of common coupling (GSU transformers of rotating machines become Yd1).
Only CIM RDF/XML is written, as *<case>.xml*.

Identifiers come from *<case>_mRIDs.dat*. Objects the map does not hold stop the script,
unless **--new-mrids** is given: then each gets a new uuid4, appended to the map.

Command-line Arguments:
  **index** (int): case number, 0 to 3 (as *raw_to_rdf.py*)
  **--serialization**: 552_ED2 (default, rdf:about="urn:uuid:..."), 552_ED1 (rdf:ID="_...") or plain
  **--new-mrids**: append new mRIDs to *<case>_mRIDs.dat* for objects it does not hold
"""
import argparse
import math
import os
import re
import uuid

import numpy
import pandas

import emthub.api as emthub
from emthub.cim_support import (
    load_detailed_model_types,
    load_dynamics_defaults,
    load_dynamics_mapping,
    load_dyrfile,
    match_dyr_generators,
)
from emthub.cim_triplets import (
    SERIALIZATIONS,
    full_model,
    load_rdf_map,
    model_id,
    to_triplets,
    write_cimxml,
)
from emthub.create_rdf import (
    HIGH_STEP,
    IBR_IFAULT,
    LOW_STEP,
    M_PER_MILE,
    OFAF_SCALE,
    ONAF_SCALE,
    PU_WAVE_SPEED,
    SHORT_TERM_SCALE,
    SHORT_TERM_SECONDS,
    SQRT2,
    SQRT3,
    STEP_VOLTAGE_INCREMENT,
    WFREQ,
    XFMR_AIRCORE,
    XFMR_IMAG_PU,
    XFMR_INLL_PU,
    XFMR_VSAT_PU,
    load_bus_coordinates,
)

UNIT_CLASSES = (("wind_units", "PowerElectronicsWindUnit"), ("solar_units", "PhotoVoltaicUnit"),
                ("hydro_units", "HydroGeneratingUnit"), ("nuclear_units", "NuclearGeneratingUnit"))
IBR_UNITS = ("PowerElectronicsWindUnit", "PhotoVoltaicUnit")
MACHINE_SECTIONS = ("SynchronousMachineDetailed", "RotatingMachineDynamics", "DynamicsFunctionBlock")


def load_mrids(name):
    """``{"Class:name": mRID}`` from *<case>_mRIDs.dat* (the map *create_rdf.py* keeps)."""
    uuids = {}
    if os.path.exists(f"{name}_mRIDs.dat"):
        with open(f"{name}_mRIDs.dat") as file:
            for line in file:
                tokens = re.split(r"[,\s]+", line)
                if len(tokens) > 2 and not tokens[0].startswith("//"):
                    uuids[f"{tokens[0]}:{tokens[1]}"] = tokens[2]
    return uuids


def lexical(value):
    """Value as rdflib writes it: xsd:boolean lexical form, numpy scalars as Python numbers."""
    if isinstance(value, (bool, numpy.bool_)):
        return "true" if value else "false"
    return value.item() if isinstance(value, numpy.generic) else value


class Tables:
    """Rows per class, collected in creation order, then one DataFrame per class."""

    def __init__(self, uuids):
        self.uuids = uuids
        self.added = {}       # map entries the file does not hold yet, in creation order
        self.generated = []   # of which new uuid4s
        self.rows = {}
        self.index = {}

    def mrid(self, cls, name):
        key = f"{cls}:{name}"
        if key not in self.uuids:
            self.uuids[key] = self.added[key] = str(uuid.uuid4()).upper()
            self.generated.append(key)
        return self.uuids[key]

    def keep(self, cls, name, ID):
        """A fixed mRID (container, model library) recorded in the map, as *create_rdf.py* does."""
        key = f"{cls}:{name}"
        if key not in self.uuids:
            self.uuids[key] = self.added[key] = ID

    def add(self, cls, ID, **attributes):
        row = self.index[ID] = {"ID": ID, **attributes}
        self.rows.setdefault(cls, []).append(row)
        return ID

    def identified(self, cls, ID, name, **attributes):
        return self.add(cls, ID, **{"IdentifiedObject.name": name, "IdentifiedObject.mRID": ID}, **attributes)

    def named(self, cls, name, **attributes):
        """An IdentifiedObject whose mRID comes from the map; returns the mRID."""
        return self.identified(cls, self.mrid(cls, name), name, **attributes)

    def terminal(self, eq_id, cn_id, sequence):
        return self.add("Terminal", f"{eq_id}_{sequence}", **{"Terminal.ConnectivityNode": cn_id,
                                                              "Terminal.ConductingEquipment": eq_id,
                                                              "ACDCTerminal.sequenceNumber": sequence})

    def tableviews(self):
        # dtype=object keeps each value as given: no int -> float upcast within a column
        return {cls: pandas.DataFrame([{key: lexical(value) for key, value in row.items()} for row in rows],
                                      dtype=object).set_index("ID")
                for cls, rows in self.rows.items()}


def limits(t, key, terminal_id, ol_type, ratings):
    """OperationalLimitSet on *terminal_id* with one ApparentPowerLimit per (suffix, type, VA)."""
    ols = t.named("OperationalLimitSet", key, **{"OperationalLimitSet.Terminal": terminal_id})
    for suffix, limit_type, value in ratings:
        t.named("ApparentPowerLimit", f"{key}_{suffix}", **{"OperationalLimit.OperationalLimitSet": ols,
                                                            "OperationalLimit.OperationalLimitType": ol_type[limit_type],
                                                            "ApparentPowerLimit.value": value})


def equipment(t, cls, key, eq, kv_id, buses, **attributes):
    """A ConductingEquipment in *eq* with a Terminal per connected bus."""
    ID = t.named(cls, key, **{"Equipment.EquipmentContainer": eq, "Equipment.inService": True}, **attributes)
    for sequence, cn_id in enumerate(buses, start=1):
        t.terminal(ID, cn_id, sequence)
    t.index[ID]["ConductingEquipment.BaseVoltage"] = kv_id
    return ID


def model_tables(tables, kvbases, bus_kvbases, baseMVA, case):
    name = case["name"]
    t = Tables(load_mrids(name))
    emergency = case.get("emergency_ratings") is True

    t.keep("EquipmentContainer", name, case["id"])
    eq = t.identified("EquipmentContainer", case["id"], name)
    absolute = "OperationalLimitDirectionKind.absoluteValue"
    ol_type = {
        "Normal": t.named("OperationalLimitType", "Normal", **{"OperationalLimitType.isInfiniteDuration": True,
                                                               "OperationalLimitType.direction": absolute}),
        "ShortTerm": t.named("OperationalLimitType", "ShortTerm", **{"OperationalLimitType.isInfiniteDuration": False,
                                                                     "OperationalLimitType.acceptableDuration": SHORT_TERM_SECONDS,
                                                                     "OperationalLimitType.direction": absolute}),
    }

    kv_ids = {str(kv): t.named("BaseVoltage", kvname, **{"BaseVoltage.nominalVoltage": kv * 1000.0})
              for kvname, kv in kvbases.items()}
    bus_ids = {str(row[0]): t.named("ConnectivityNode", str(row[0]), **{"ConnectivityNode.ConnectivityNodeContainer": eq})
               for row in tables["BUS"]["data"]}

    if os.path.exists(f"{name}_Network.json"):
        xy = load_bus_coordinates(f"{name}_Network.json")
        for row in tables["BUS"]["data"]:
            key = str(row[0])
            td = t.named("TextDiagramObject", key, **{"DiagramObject.IdentifiedObject": bus_ids[key],
                                                      "DiagramObject.drawingOrder": 1, "DiagramObject.isPolygon": False,
                                                      "TextDiagramObject.text": f"{row[0]:d} {row[1]:s} {row[2]:.2f} kV"})
            t.add("DiagramObjectPoint", f"{td}_pt1", **{"DiagramObjectPoint.DiagramObject": td,
                                                        "DiagramObjectPoint.sequenceNumber": 1,
                                                        "DiagramObjectPoint.xPosition": xy[key][0],
                                                        "DiagramObjectPoint.yPosition": xy[key][1]})

    for row in tables["BRANCH"]["data"]:
        key = f"{row[0]:d}_{row[1]:d}_{int(row[2]):d}"
        kvbase = bus_kvbases[row[0]]
        zbase = kvbase * kvbase / baseMVA
        r1, x1, bpu, rate1mva = row[3] * zbase, row[4] * zbase, row[5], row[6]
        buses = (bus_ids[str(row[0])], bus_ids[str(row[1])])
        if x1 < 0.0:
            ID = equipment(t, "SeriesCompensator", key, eq, kv_ids[str(kvbase)], buses,
                           **{"SeriesCompensator.r": r1, "SeriesCompensator.x": x1,
                              "SeriesCompensator.r0": r1, "SeriesCompensator.x0": x1})
        else:
            l1 = x1 / WFREQ
            if bpu > 0.0:
                c1 = bpu / WFREQ / zbase
                z1 = math.sqrt(l1 / c1)
            else:
                z1 = 400.0
                c1 = l1 / z1 / z1
            b1ch = c1 * WFREQ
            if z1 >= 100.0:          # overhead
                r0, x0, b0ch = 2.0 * r1, 3.0 * x1, 0.6 * b1ch
                length = math.sqrt(x1 * b1ch) / WFREQ * 3.0e8 * PU_WAVE_SPEED
            else:                    # underground
                r0, x0, b0ch = r1, x1, b1ch
                length = M_PER_MILE * x1 / 0.2
            ID = equipment(t, "ACLineSegment", key, eq, kv_ids[str(kvbase)], buses,
                           **{"Conductor.length": length, "ACLineSegment.r": r1, "ACLineSegment.x": x1,
                              "ACLineSegment.bch": b1ch, "ACLineSegment.r0": r0, "ACLineSegment.x0": x0,
                              "ACLineSegment.b0ch": b0ch})
        ratings = [("Normal", "Normal", rate1mva * 1.0e6)]
        if emergency:
            ratings.append(("ShortTerm", "ShortTerm", rate1mva * 1.0e6 * SHORT_TERM_SCALE))
        limits(t, key, f"{ID}_1", ol_type, ratings)

    for row in tables.get("SYSTEM SWITCHING DEVICE", {}).get("data", []):
        key = f"{row[0]:d}_{row[1]:d}_{int(row[2]):d}"
        ID = equipment(t, "DisconnectingCircuitBreaker", key, eq, kv_ids[str(bus_kvbases[row[0]])],
                       (bus_ids[str(row[0])], bus_ids[str(row[1])]))
        limits(t, key, f"{ID}_1", ol_type, [("Normal", "Normal", row[4] * 1.0e6)])

    responses = {}
    for row in tables["LOAD"]["data"]:
        if row[2] < 1:
            continue
        scale = row[9] * 1.0e6
        Pp, Ip, Zp, Pq, Iq, Zq = 0.0, 100.0, 0.0, 0.0, 0.0, 100.0    # defaults match WECC 240
        Pmag = abs(row[3]) + abs(row[5]) + abs(row[7])
        if Pmag > 0.0:
            Pp, Ip, Zp = (100.0 * abs(row[i]) / Pmag for i in (3, 5, 7))
        Qmag = abs(row[4]) + abs(row[6]) + abs(row[8])
        if Qmag > 0.0:
            Pq, Iq, Zq = (100.0 * abs(row[i]) / Qmag for i in (4, 6, 8))
        lr_key = f"LoadResp_Zp={Zp:.3f}_Ip={Ip:.3f}_Pp={Pp:.3f}_Zq={Zq:.3f}_Iq={Iq:.3f}_Pq={Pq:.3f}"
        responses.setdefault(lr_key, (Zp, Ip, Pp, Zq, Iq, Pq))
        equipment(t, "EnergyConsumer", f"{row[0]:d}_{int(row[1]):d}", eq, kv_ids[str(bus_kvbases[row[0]])],
                  (bus_ids[str(row[0])],),
                  **{"EnergyConsumer.LoadResponse": t.mrid("LoadResponseCharacteristic", lr_key),
                     "EnergyConsumer.p": (row[3] + row[5] + row[7]) * scale,
                     "EnergyConsumer.q": (row[4] + row[6] + row[8]) * scale})
    for lr_key, (Zp, Ip, Pp, Zq, Iq, Pq) in responses.items():
        t.named("LoadResponseCharacteristic", lr_key, **{
            "LoadResponseCharacteristic.exponentModel": False,
            "LoadResponseCharacteristic.pFrequencyExponent": 0.0, "LoadResponseCharacteristic.qFrequencyExponent": 0.0,
            "LoadResponseCharacteristic.pVoltageExponent": 0.0, "LoadResponseCharacteristic.qVoltageExponent": 0.0,
            "LoadResponseCharacteristic.pConstantImpedance": Zp, "LoadResponseCharacteristic.pConstantCurrent": Ip,
            "LoadResponseCharacteristic.pConstantPower": Pp, "LoadResponseCharacteristic.qConstantImpedance": Zq,
            "LoadResponseCharacteristic.qConstantCurrent": Iq, "LoadResponseCharacteristic.qConstantPower": Pq})

    def shunt(key, row, kvbase, count, maximum, b, g):
        equipment(t, "LinearShuntCompensator", key, eq, kv_ids[str(kvbase)], (bus_ids[str(row[0])],),
                  **{"ShuntCompensator.nomU": kvbase * 1000.0, "ShuntCompensator.sections": count,
                     "ShuntCompensator.maximumSections": maximum, "ShuntCompensator.grounded": True,
                     "LinearShuntCompensator.bPerSection": b, "LinearShuntCompensator.gPerSection": g})

    for row in tables["FIXED SHUNT"]["data"]:
        if row[2] >= 1:
            kvbase = bus_kvbases[row[0]]
            shunt(f"{row[0]:d}_{int(row[1]):d}", row, kvbase, 1, 1, row[4] / kvbase / kvbase, row[3] / kvbase / kvbase)
    for row in tables["SWITCHED SHUNT"]["data"]:
        if row[1] >= 1:
            kvbase = bus_kvbases[row[0]]
            shunt(f"{row[0]:d}", row, kvbase, int((row[2] + 0.1 * row[4]) / row[4]), row[3],
                  row[4] / kvbase / kvbase, 0.0)

    transformers(t, tables, bus_kvbases, kv_ids, bus_ids, eq, ol_type, emergency)
    machines = generators(t, tables, case, bus_kvbases, kv_ids, bus_ids, eq)
    if not machines and "swingbus" in case:
        swing = int(case["swingbus"])
        kvbase = bus_kvbases[swing]
        print("No generators, writing an EnergySource at swing bus", swing)
        equipment(t, "EnergySource", f"{swing:d}_1", eq, kv_ids[str(kvbase)], (bus_ids[case["swingbus"]],),
                  **{"EnergySource.nominalVoltage": 1000.0 * kvbase, "EnergySource.voltageMagnitude": 1000.0 * kvbase,
                     "EnergySource.voltageAngle": 0.0, "EnergySource.r": 0.0, "EnergySource.x": 0.001,
                     "EnergySource.r0": 0.0, "EnergySource.x0": 0.001})
    plants(t, machines)
    return t


def transformers(t, tables, bus_kvbases, kv_ids, bus_ids, eq, ol_type, emergency):
    """Two-winding transformers, as *create_rdf.py* writes them (Yy0, ends by RAW order)."""
    for row, wdg in zip(tables["TRANSFORMER"]["data"], tables["TRANSFORMER"]["winding_data"]):
        if row[4] < 1:
            continue
        key = f"{row[0]:d}_{row[1]:d}_{row[2]:d}_{int(row[3]):d}"
        mva = max(wdg["mvas"]) if max(wdg["mvas"]) > 0.0 else wdg["s12"]
        kvs = [kv if kv > 0.0 else bus_kvbases[row[i]] for i, kv in enumerate(wdg["kvs"][:wdg["nwdgs"]])]
        pt = t.named("PowerTransformer", key, **{"Equipment.EquipmentContainer": eq, "Equipment.inService": True,
                                                 "PowerTransformer.vectorGroup": "Yy"})
        ends = []
        for i in range(2):
            end_key = f"{key}_End_{i + 1}"
            terminal = t.terminal(pt, bus_ids[str(row[i])], i + 1)
            end = t.named("PowerTransformerEnd", end_key, **{
                "PowerTransformerEnd.PowerTransformer": pt, "PowerTransformerEnd.ratedS": mva * 1.0e6,
                "PowerTransformerEnd.ratedU": kvs[i] * 1.0e3, "PowerTransformerEnd.phaseAngleClock": 0,
                "TransformerEnd.endNumber": i + 1, "PowerTransformerEnd.connectionKind": "WindingConnection.Y",
                "TransformerEnd.grounded": True, "TransformerEnd.rground": 0.0, "TransformerEnd.xground": 0.0,
                "TransformerEnd.BaseVoltage": kv_ids[str(kvs[i])], "TransformerEnd.Terminal": terminal})
            ends.append(end)
            tap = wdg["taps"][i]
            if abs(1.0 - tap) > 1.0e-8:
                step = min(max((tap - 1.0) * 100.0 / STEP_VOLTAGE_INCREMENT, LOW_STEP), HIGH_STEP)
                t.named("RatioTapChanger", end_key, **{
                    "TapChanger.highStep": HIGH_STEP, "TapChanger.lowStep": LOW_STEP, "TapChanger.neutralStep": 0,
                    "TapChanger.neutralU": kvs[i] * 1.0e3, "TapChanger.normalStep": round(step), "TapChanger.step": step,
                    "RatioTapChanger.stepVoltageIncrement": STEP_VOLTAGE_INCREMENT, "RatioTapChanger.TransformerEnd": end})
            ratings = [("ONAN", "Normal", mva * 1.0e6)]
            if emergency:
                ratings += [("ONAN_ShortTerm", "ShortTerm", mva * 1.0e6 * SHORT_TERM_SCALE),
                            ("ONAF", "Normal", mva * 1.0e6 * ONAF_SCALE),
                            ("ONAF_ShortTerm", "ShortTerm", mva * 1.0e6 * ONAF_SCALE * SHORT_TERM_SCALE),
                            ("OFAF", "Normal", mva * 1.0e6 * OFAF_SCALE),
                            ("OFAF_ShortTerm", "ShortTerm", mva * 1.0e6 * OFAF_SCALE * SHORT_TERM_SCALE)]
            limits(t, end_key, terminal, ol_type, ratings)

        zbase = kvs[0] * kvs[0] / wdg["s12"]
        rmesh, xmesh = zbase * wdg["r12"], zbase * wdg["x12"]
        t.named("TransformerMeshImpedance", f"{key}_Mesh", **{
            "TransformerMeshImpedance.FromTransformerEnd": ends[0], "TransformerMeshImpedance.ToTransformerEnd": ends[1],
            "TransformerMeshImpedance.r": rmesh, "TransformerMeshImpedance.r0": rmesh,
            "TransformerMeshImpedance.x": xmesh, "TransformerMeshImpedance.x0": xmesh})
        kvbase = kvs[1]
        ybase = mva / kvbase / kvbase
        bcore, gcore = XFMR_IMAG_PU * ybase, XFMR_INLL_PU * ybase
        core = t.named("TransformerCoreAdmittance", f"{key}_Core", **{
            "TransformerCoreAdmittance.TransformerEnd": ends[1], "TransformerCoreAdmittance.g": gcore,
            "TransformerCoreAdmittance.g0": gcore, "TransformerCoreAdmittance.b": bcore,
            "TransformerCoreAdmittance.b0": bcore})
        sat = t.named("TransformerSaturationCurve", f"{key}_Sat", **{
            "TransformerSaturationCurve.TransformerCoreAdmittance": core,
            "Curve.curveStyle": "CurveStyle.straightLineYValues", "Curve.xUnit": "UnitSymbol.A",
            "Curve.y1Unit": "UnitSymbol.Vs", "Curve.xMultiplier": "UnitMultiplier.none",
            "Curve.y1Multiplier": "UnitMultiplier.none"})
        ibase_peak = 1.0e3 * XFMR_IMAG_PU * SQRT2 * mva / kvbase / SQRT3
        fbase_peak = 1.0e3 * SQRT2 * kvbase / SQRT3 / WFREQ
        i1, f1 = XFMR_VSAT_PU * ibase_peak, XFMR_VSAT_PU * fbase_peak
        aircore = XFMR_AIRCORE * wdg["x12"] * kvbase * kvbase / wdg["s12"] / WFREQ
        for n, (x, y) in enumerate(((i1, f1), (i1 + 100.0, f1 + 100.0 * aircore)), start=1):
            t.add("CurveData", f"{sat}_pt{n}", **{"CurveData.Curve": sat, "CurveData.xvalue": x, "CurveData.y1value": y})


def generators(t, tables, case, bus_kvbases, kv_ids, bus_ids, eq):
    """Generators with their units and dyr dynamics; returns ``[(mRID, name, unit class)]``."""
    dyr_df = load_dyrfile(case)
    dyr = match_dyr_generators(dyr_df) if dyr_df is not None else {}
    defaults, mapping = load_dynamics_defaults(), load_dynamics_mapping()
    models = load_detailed_model_types()["DYR"]
    used = {}       # detailed model types, in first-use order
    machines = []
    for row in tables["GENERATOR"]["data"]:
        if row[7] < 1:
            continue
        bus, kvbase, mvabase = bus_ids[str(row[0])], bus_kvbases[row[0]], row[6]
        key = f"{row[0]:d}_{row[1].strip():s}"
        unit_class = next((cls for field, cls in UNIT_CLASSES if key in case.get(field, ())), "ThermalGeneratingUnit")
        if unit_class in IBR_UNITS:
            maxQ = row[4] if row[4] > 0.0 else mvabase
            minQ = row[5] if row[5] < 0.0 else -mvabase
            ID = equipment(t, "PowerElectronicsConnection", key, eq, kv_ids[str(kvbase)], (bus,), **{
                "PowerElectronicsConnection.maxIFault": IBR_IFAULT,
                "PowerElectronicsConnection.maxQ": 1.0e6 * maxQ, "PowerElectronicsConnection.minQ": 1.0e6 * minQ,
                "PowerElectronicsConnection.p": 1.0e6 * row[2], "PowerElectronicsConnection.q": 1.0e6 * row[3],
                "PowerElectronicsConnection.ratedS": 1.0e6 * mvabase, "PowerElectronicsConnection.ratedU": 1.0e3 * kvbase})
            t.named(unit_class, key, **{"Equipment.EquipmentContainer": eq, "Equipment.inService": True,
                                        "PowerElectronicsUnit.PowerElectronicsConnection": ID,
                                        "PowerElectronicsUnit.maxP": 1.0e6 * row[6], "PowerElectronicsUnit.minP": 0.0})
        else:
            unit = t.named(unit_class, key, **{"Equipment.EquipmentContainer": eq, "Equipment.inService": True,
                                               "GeneratingUnit.minOperatingP": 0.0,
                                               "GeneratingUnit.maxOperatingP": 1.0e6 * mvabase})
            maxQ = row[4] if row[4] > 0.0 else 0.3122 * mvabase    # 0.95 pf
            minQ = row[5] if row[5] < 0.0 else -0.3122 * mvabase
            ID = equipment(t, "SynchronousMachine", key, eq, kv_ids[str(kvbase)], (bus,), **{
                "RotatingMachine.GeneratingUnit": unit,
                "RotatingMachine.p": 1.0e6 * row[2], "RotatingMachine.q": 1.0e6 * row[3],
                "RotatingMachine.ratedS": 1.0e6 * mvabase, "RotatingMachine.ratedU": 1.0e3 * kvbase,
                "SynchronousMachine.earthing": False, "SynchronousMachine.earthingStarPointR": 0.0,
                "SynchronousMachine.earthingStarPointX": 0.0,
                "SynchronousMachine.maxQ": 1.0e6 * maxQ, "SynchronousMachine.minQ": 1.0e6 * minQ,
                "SynchronousMachine.operatingMode": "SynchronousMachineOperatingMode.generator",
                "SynchronousMachine.type": "SynchronousMachineKind.generator"})
        machines.append((ID, key, unit_class))

        if key not in dyr:
            print("no dynamics found for", key, unit_class)
        for model_name, values in dyr.get(key, {}).items():
            model = models[model_name]
            cls = model["closestStandardModel"]
            if unit_class not in IBR_UNITS and cls.startswith("SynchronousMachine"):
                machine_dynamics(t, cls, key, ID, defaults, mapping[model_name]["AttMap"], values)
            else:
                used[model_name] = model
                detailed_model(t, key, ID, model_name, model, values)

    unused = [key for key in dyr if key not in {name for _, name, _ in machines}]
    if unused:
        print("dyr entries for these generators were not used (off-line in the raw file?):", unused)
    for model_name, model in used.items():
        model_type(t, model_name, model)
    return machines


def machine_dynamics(t, cls, key, machine, defaults, attmap, values):
    """A SynchronousMachineDynamics leaf: profile defaults, overridden by the dyr row where mapped."""
    attributes = {}
    for section in (cls, *MACHINE_SECTIONS):
        for tag, (value, unit, *_) in defaults[section].items():
            if value is None:
                continue
            attribute = f"{section}.{tag}"
            if attribute in attmap:
                value = values[attmap[attribute]]
                value = {"Boolean": bool, "Integer": int}.get(unit, lambda v: v)(value)
                if unit == "InputSignalKind":
                    value = "rotorAngularFrequencyDeviation"
            attributes[attribute] = f"{unit}.{value}" if unit.endswith("Kind") else value
    t.named(cls, key, **attributes, **{"SynchronousMachineDynamics.SynchronousMachine": machine})


def detailed_model(t, root_key, equipment_id, model_name, model, values):
    """DetailedModelDynamics on *equipment_id* with one ParameterValue per dyr value."""
    key = f"{root_key}_{model['modelKind']}"
    if "renewableEnergyResource" in key:
        key = f"{key}_{model_name}"
    ID = t.named("DetailedModelDynamics", key, **{"DynamicsFunctionBlock.enabled": True,
                                                  "DetailedModelDynamics.Equipment": equipment_id,
                                                  "DetailedModelDynamics.DetailedModelTypeDynamics": model["mRID"]})
    descriptors = model["parameterDescriptors"]
    for index, value in enumerate(values):
        descriptor = descriptors[index + 3]     # the dyr bus, model and ID are not parameters
        t.add("ParameterValue", f"{ID}_seq{descriptor['sequenceNumber']:d}", **{
            "ParameterValue.DetailedModelDynamics": ID, "ParameterValue.ParameterDescriptor": descriptor["mRID"],
            "ParameterValue.value": value})


def model_type(t, model_name, model):
    """NthAmDynamicModel from the library, with its ParameterDescriptors."""
    ID = model["mRID"]
    t.keep("NthAmDynamicModel", model_name, ID)
    t.identified("NthAmDynamicModel", ID, model_name, **{
        "NthAmDynamicModel.modelKind": f"NthAmModelKind.{model['modelKind']}",
        "NthAmDynamicModel.nameKind": f"NthAmModelNameKind.{model['nameKind']}",
        "NthAmDynamicModel.statusKind": f"NthAmModelStatusKind.{model['statusKind']}",
        "NthAmDynamicModel.closestStandardModel": model["closestStandardModel"]})
    for descriptor in model["parameterDescriptors"][3:]:
        t.keep("ParameterDescriptor", f"{model_name}_{descriptor['name']}", descriptor["mRID"])
        t.identified("ParameterDescriptor", descriptor["mRID"], descriptor["name"], **{
            "DetailedModelDescriptor.DetailedModelTypeDynamics": ID,
            "ParameterDescriptor.typicalValue": descriptor["typicalValue"],
            "ParameterDescriptor.engineeringUnit": descriptor["engineeringUnit"],
            "ParameterDescriptor.sequenceNumber": descriptor["sequenceNumber"]})


def plants(t, machines):
    """A plant per generator with a step-up transformer at its bus; rotating machine GSUs become Yd1."""
    node_of = {row["ID"]: row["Terminal.ConnectivityNode"] for row in t.rows["Terminal"]}
    ends = t.rows.get("PowerTransformerEnd", [])
    first_end = {end["PowerTransformerEnd.PowerTransformer"]: end for end in ends if end["TransformerEnd.endNumber"] == 1}
    ends_at = {}
    for end in ends:
        ends_at.setdefault(node_of[end["TransformerEnd.Terminal"]], []).append(end)
    for machine, key, unit_class in machines:
        gsu = ends_at.get(node_of[f"{machine}_1"], [])
        if not gsu:
            continue
        if len(gsu) > 1:
            print("more than one transformer at generator", key, "- using the first for its plant")
        end = gsu[0]
        pt = end["PowerTransformerEnd.PowerTransformer"]
        if unit_class in IBR_UNITS:     # the GSU stays Yy
            plant_class = "IBRPlant"
        else:
            plant_class = "RotatingMachinePlant"
            t.index[pt]["PowerTransformer.vectorGroup"] = "Yd1"
            end.update({"PowerTransformerEnd.phaseAngleClock": 1,
                        "PowerTransformerEnd.connectionKind": "WindingConnection.D",
                        "TransformerEnd.grounded": False})
        t.mrid(plant_class, key)
        poc = t.named("ACPointOfCommonCoupling", key, **{
            "ACPointOfCommonCoupling.ConnectivityNode": node_of[first_end[pt]["TransformerEnd.Terminal"]]})
        t.named(plant_class, key, **{"ConnectedFacility.Equipments": [machine, pt],
                                     "ConnectedFacility.ACPointOfCommonCoupling": poc})


def create_cim_model(case, serialization="552_ED2", new_mrids=False):
    name = case["name"]
    tables, kvbases, bus_kvbases, baseMVA = emthub.load_rawfile(f"{name}.raw")
    t = model_tables(tables, kvbases, bus_kvbases, baseMVA, case)
    if t.generated and not new_mrids:
        raise SystemExit(f"{len(t.generated)} objects have no mRID in {name}_mRIDs.dat "
                         f"(e.g. {', '.join(t.generated[:5])}); rerun with --new-mrids to append new ones")
    if t.added and new_mrids:
        with open(f"{name}_mRIDs.dat", "a") as file:
            file.writelines(f"{key.replace(':', ',', 1)},{ID}\n" for key, ID in t.added.items())
        print("Appended", len(t.added), "mRIDs to", f"{name}_mRIDs.dat,", len(t.generated), "of them new")

    tableviews = t.tableviews()
    schema = load_rdf_map(serialization)
    header = full_model(model_id(case["id"], "network"), f"{name} network, generators and dynamics",
                        os.path.getmtime(f"{name}.raw"), schema)
    data = to_triplets(tableviews, instance_id=case["id"], header=header, multivalue=True)
    write_cimxml(data, schema, f"{name}.xml")
    print("Wrote", f"{name}.xml", f"({serialization}),", len(data), "triplets,",
          sum(len(table) for table in tableviews.values()), "objects")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("index", type=int, nargs="?", default=0)
    parser.add_argument("--serialization", choices=SERIALIZATIONS, default=SERIALIZATIONS[0])
    parser.add_argument("--new-mrids", action="store_true",
                        help="append a new uuid4 to <case>_mRIDs.dat for each object it does not hold")
    args = parser.parse_args()
    create_cim_model(emthub.CASES[args.index], args.serialization, args.new_mrids)


if __name__ == "__main__":
    main()
