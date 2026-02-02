# Copyright (C) 2026 Meltran, Inc

import rdflib
import os
import sys
import re
import uuid
import pandas as pd
from rdflib.namespace import XSD
from otsrdflib import OrderedTurtleSerializer
import cim_examples 
import emthub.api as emthub

CIM_NS = 'http://www.ucaiug.org/ns#'
EMT_NS = 'http://opensource.ieee.org/emtiop#'

def create_cim_ic (case):
  bus_ic = None
  if 'bus_ic' in case and os.path.exists(case['bus_ic']):
    bus_ic = pd.read_csv (case['bus_ic'])
    print ('Initial bus numbers, base kV, Vpus, angles, and CN ids from', case['bus_ic'], 'read', bus_ic.shape)
    #print (bus_ic)
  gen_ic = None
  if 'gen_ic' in case and os.path.exists(case['gen_ic']):
    gen_ic = pd.read_csv (case['gen_ic'])
    print ('Generator bus, p, q, types, and EQ ids from', case['gen_ic'], 'read', gen_ic.shape)
    #print (gen_ic)
  br_ic = None
  if 'br_ic' in case and os.path.exists(case['br_ic']):
    br_ic = pd.read_csv (case['br_ic'])
    print ('Branch from, to, tap, pf, qf, pt, qt and EQ/XfEnd ids from', case['br_ic'], 'read', br_ic.shape)
    print (br_ic)

  g = rdflib.Graph()
  CIM = rdflib.Namespace (CIM_NS)
  g.bind('cim', CIM)
  EMT = rdflib.Namespace (EMT_NS)
  g.bind('emt', EMT)
  
  for i in range(len(bus_ic)):
    bus = bus_ic.iloc[i,0]
    nomv = 1000.0 * bus_ic.iloc[i,1]
    vpu = bus_ic.iloc[i,2]
    deg = bus_ic.iloc[i,3]
    cnid = bus_ic.iloc[i,4]
    vmag = vpu * nomv
    sv = rdflib.URIRef (cnid+'_SvV') #rdflib.BNode()
    g.add ((sv, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'SvVoltage')))
    g.add ((sv, rdflib.URIRef (EMT_NS + 'SvVoltage.ConnectivityNode'), rdflib.URIRef(cnid)))
    g.add ((sv, rdflib.URIRef (CIM_NS + 'SvVoltage.v'), rdflib.Literal (vmag, datatype=CIM.Voltage)))
    g.add ((sv, rdflib.URIRef (CIM_NS + 'SvVoltage.angle'), rdflib.Literal (deg, datatype=CIM.AngleDegrees)))

  for i in range(len(br_ic)):
    tap = br_ic.iloc[i,2]
    pf = 1.0e6 * br_ic.iloc[i,3]
    qf = 1.0e6 * br_ic.iloc[i,4]
    brid = br_ic.iloc[i,7]
    sv = rdflib.URIRef (brid+'_SvPF') #rdflib.BNode()
    g.add ((sv, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'SvPowerFlow')))
    if tap > 0.0:
      g.add ((sv, rdflib.URIRef (EMT_NS + 'SvPowerFlow.TransformerEnd'), rdflib.URIRef(brid)))
    else:
      g.add ((sv, rdflib.URIRef (EMT_NS + 'SvPowerFlow.ConductingEquipment'), rdflib.URIRef(brid)))
    g.add ((sv, rdflib.URIRef (CIM_NS + 'SvPowerFlow.p'), rdflib.Literal (pf, datatype=CIM.ActivePower)))
    g.add ((sv, rdflib.URIRef (CIM_NS + 'SvPowerFlow.q'), rdflib.Literal (qf, datatype=CIM.ReactivePower)))

  # positive generation sign changes to follow load convention, into the From bus
  for i in range(len(gen_ic)):
    pf = -1.0e6 * gen_ic.iloc[i,1]
    qf = -1.0e6 * gen_ic.iloc[i,2]
    eqid = gen_ic.iloc[i,4]
    sv = rdflib.URIRef (eqid+'_SvPF') #rdflib.BNode()
    g.add ((sv, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'SvPowerFlow')))
    g.add ((sv, rdflib.URIRef (EMT_NS + 'SvPowerFlow.ConductingEquipment'), rdflib.URIRef(eqid)))
    g.add ((sv, rdflib.URIRef (CIM_NS + 'SvPowerFlow.p'), rdflib.Literal (pf, datatype=CIM.ActivePower)))
    g.add ((sv, rdflib.URIRef (CIM_NS + 'SvPowerFlow.q'), rdflib.Literal (qf, datatype=CIM.ReactivePower)))

  serializer = OrderedTurtleSerializer(g)
  serializer.class_order = [
    CIM.SvPowerFlow,
    CIM.SvVoltage
  ]
  with open(case['ttl_ic'], 'wb') as fp:
    serializer.serialize(fp)
  print ('wrote initial conditions to', case['ttl_ic'])

if __name__ == '__main__':
  idx = 3
  if len(sys.argv) > 1:
    idx = int(sys.argv[1])
  case = cim_examples.CASES[idx]
  create_cim_ic (case)

