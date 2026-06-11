# Copyright (C) 2026 Meltran, Inc

import rdflib
import os
import sys
import pandas as pd
from rdflib.namespace import XSD
from otsrdflib import OrderedTurtleSerializer
import emthub.api as emthub

CIM_NS = 'http://www.ucaiug.org/ns#'
EMT_NS = 'http://opensource.ieee.org/emtiop#'

def create_cim_ic (case):
  bus_ic = None
  bus_name = case['name']+'mb.txt'
  if os.path.exists(bus_name):
    bus_ic = pd.read_csv (bus_name)
    print ('Initial bus numbers, base kV, Vpus, angles, and CN ids from', bus_name, 'read', bus_ic.shape)
    #print (bus_ic)
  gen_ic = None
  gen_name = case['name']+'mg.txt'
  if os.path.exists(gen_name):
    gen_ic = pd.read_csv (gen_name)
    print ('Generator bus, p, q, types, and EQ ids from', gen_name, 'read', gen_ic.shape)
    #print (gen_ic)
  br_ic = None
  br_name = case['name']+'mbr.txt'
  if os.path.exists(br_name):
    br_ic = pd.read_csv (br_name)
    print ('Branch from, to, tap, pf, qf, pt, qt and EQ/XfEnd ids from', br_name, 'read', br_ic.shape)
    #print (br_ic)

  g = rdflib.Graph() # (store='Oxigraph')
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
    # temporary TopologicalNode for compliance with base CIM
    tnid = cnid+'_TN'
    tn = rdflib.URIRef (tnid)
    g.add ((tn, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'TopologicalNode')))
    cn = rdflib.URIRef (cnid)
    g.add ((cn, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'ConnectivityNode')))
    g.add ((cn, rdflib.URIRef (CIM_NS + 'ConnectivityNode.TopologicalNode'), rdflib.URIRef(tnid)))
    sv = rdflib.URIRef (cnid+'_SvV')
    g.add ((sv, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'SvVoltage')))
    g.add ((sv, rdflib.URIRef (CIM_NS + 'SvVoltage.TopologicalNode'), rdflib.URIRef(tnid)))
    g.add ((sv, rdflib.URIRef (CIM_NS + 'SvVoltage.v'), rdflib.Literal (vmag, datatype=CIM.Voltage)))
    g.add ((sv, rdflib.URIRef (CIM_NS + 'SvVoltage.angle'), rdflib.Literal (deg, datatype=CIM.AngleDegrees)))

  for i in range(len(br_ic)):
    tap = br_ic.iloc[i,2]
    p1 = 1.0e6 * br_ic.iloc[i,3]
    q1 = 1.0e6 * br_ic.iloc[i,4]
    p2 = 1.0e6 * br_ic.iloc[i,5]
    q2 = 1.0e6 * br_ic.iloc[i,6]
    t1id = br_ic.iloc[i,7]
    t2id = br_ic.iloc[i,8]
    eqid = t1id.split('_')[0]
    if tap > 0.0:
      sv1 = rdflib.URIRef (eqid+'_SvXfmrPF_1')
      sv2 = rdflib.URIRef (eqid+'_SvXfmrPF_2')
    else:
      sv1 = rdflib.URIRef (eqid+'_SvLinePF_1')
      sv2 = rdflib.URIRef (eqid+'_SvLinePF_2')
    g.add ((sv1, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'SvPowerFlow')))
    g.add ((sv1, rdflib.URIRef (CIM_NS + 'SvPowerFlow.Terminal'), rdflib.URIRef(t1id)))
    g.add ((sv1, rdflib.URIRef (CIM_NS + 'SvPowerFlow.p'), rdflib.Literal (p1, datatype=CIM.ActivePower)))
    g.add ((sv1, rdflib.URIRef (CIM_NS + 'SvPowerFlow.q'), rdflib.Literal (q1, datatype=CIM.ReactivePower)))
    g.add ((sv2, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'SvPowerFlow')))
    g.add ((sv2, rdflib.URIRef (CIM_NS + 'SvPowerFlow.Terminal'), rdflib.URIRef(t2id)))
    g.add ((sv2, rdflib.URIRef (CIM_NS + 'SvPowerFlow.p'), rdflib.Literal (p2, datatype=CIM.ActivePower)))
    g.add ((sv2, rdflib.URIRef (CIM_NS + 'SvPowerFlow.q'), rdflib.Literal (q2, datatype=CIM.ReactivePower)))

  # positive generation sign changes to follow load convention, into the From bus
  for i in range(len(gen_ic)):
    p1 = -1.0e6 * gen_ic.iloc[i,1]
    q1 = -1.0e6 * gen_ic.iloc[i,2]
    t1id = gen_ic.iloc[i,4]
    eqid = t1id.split('_')[0]
    sv = rdflib.URIRef (eqid+'_SvGenPF')
    g.add ((sv, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'SvPowerFlow')))
    g.add ((sv, rdflib.URIRef (CIM_NS + 'SvPowerFlow.Terminal'), rdflib.URIRef(t1id)))
    g.add ((sv, rdflib.URIRef (CIM_NS + 'SvPowerFlow.p'), rdflib.Literal (p1, datatype=CIM.ActivePower)))
    g.add ((sv, rdflib.URIRef (CIM_NS + 'SvPowerFlow.q'), rdflib.Literal (q1, datatype=CIM.ReactivePower)))

  serializer = OrderedTurtleSerializer(g)
  serializer.class_order = [
    CIM.SvPowerFlow,
    CIM.SvVoltage,
    CIM.TopologicalNode
  ]
  ic_name = case['name']+'_ic.ttl'
  with open(ic_name, 'wb') as fp:
    serializer.serialize(fp)
  print ('wrote initial conditions to', ic_name)

def main():
  """Converts initial conditions from MATPOWER to CIM RDF (TTL file).

  Command-line Arguments:
    **index** (int): case number from 0 to 4
  """
  idx = 0
  if len(sys.argv) > 1:
    idx = int(sys.argv[1])
  case = emthub.CASES[idx]
  if not case['UseMATPOWER']:
    print ('{:s} does not use MATPOWER'.format(case['name']))
    quit()
  create_cim_ic (case)

if __name__ == '__main__':
  main()

