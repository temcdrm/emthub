# Copyright (C) 2026 Meltran, Inc

import sys
import rdflib
from otsrdflib import OrderedTurtleSerializer

CIM_NS = 'http://www.ucaiug.org/grid18v15#'
EMT_NS = 'http://opensource.ieee.org/emtiop01v01#'

if __name__ == '__main__':
  CIM = rdflib.Namespace (CIM_NS)
  EMT = rdflib.Namespace (EMT_NS)
  g = rdflib.Graph(store='Oxigraph')
  g.bind('cim', CIM)
  g.bind('emt', EMT)

  froot = 'XfmrSat'
  if len(sys.argv) > 1:
    froot = sys.argv[1]

  fnetwork = froot + '.ttl'
  fic = froot + '_ic.ttl'
  fttl = froot + '_merged.ttl'
  fxml = froot + '_merged.xml'
  print ('Combining', fnetwork, 'and', fic, 'to form', fttl, 'and', fxml)

  g.parse (fnetwork, publicID="")
  print ('Read', len(g), 'network statements from', fnetwork)
  g.parse (fic, publicID="")
  print ('Total', len(g), 'statements after merging from', fic)

  g.serialize (destination=fxml, format='pretty-xml', max_depth=1)

  serializer = OrderedTurtleSerializer(g)
  serializer.class_order = [
    CIM.EquipmentContainer,
    CIM.BaseVoltage,
    CIM.ConnectivityNode,
    CIM.Terminal,
    CIM.ACLineSegment,
    CIM.DisconnectingCircuitBreaker,
    CIM.LinearShuntCompensator,
    CIM.SeriesCompensator,
    CIM.EnergyConsumer,
    CIM.LoadResponseCharacteristic,
    CIM.EnergySource,
    CIM.SynchronousMachine,
    CIM.HydroGeneratingUnit,
    CIM.NuclearGeneratingUnit,
    CIM.ThermalGeneratingUnit,
    CIM.SynchronousMachineSimplified,
    CIM.SynchronousMachineTimeConstantReactance,
    CIM.DetailedModelDynamics,
    EMT.NthAmDynamicModel,
    CIM.ParameterDescriptor,
    CIM.PowerElectronicsConnection,
    CIM.PhotoVoltaicUnit,
    CIM.PowerElectronicsWindUnit,
    CIM.PowerTransformer,
    CIM.PowerTransformerEnd,
    CIM.RatioTapChanger,
    CIM.TransformerMeshImpedance,
    CIM.TransformerCoreAdmittance,
    EMT.TransformerSaturationCurve,
    EMT.IBRPlant,
    EMT.RotatingMachinePlant,
    CIM.ACPointOfCommonCoupling,
    EMT.IEEECigreDLL,
    EMT.IEEECigreDLLParameter,
    EMT.IEEECigreDLLInput,
    EMT.IEEECigreDLLOutput,
    CIM.OperationalLimitType,
    CIM.OperationalLimitSet,
    CIM.ApparentPowerLimit,
    CIM.TextDiagramObject,
    CIM.DiagramObjectPoint,
    CIM.CurveData,
    CIM.ParameterValue,
    CIM.DCEquipmentContainer,
    CIM.DCNode,
    EMT.PowerElectronicsConnectionDCTerminal,
    CIM.DCShunt,
    CIM.DCLineSegment, 
    CIM.DCSeriesDevice, 
    CIM.DCGround, 
    CIM.DCBreaker, 
    CIM.DCDisconnector,
    EMT.DCEnergySource,
    CIM.SvVoltage,
    CIM.SvPowerFlow,
    CIM.TopologicalNode
  ]
  with open(fttl, 'wb') as fp:
    serializer.serialize(fp, base='')


