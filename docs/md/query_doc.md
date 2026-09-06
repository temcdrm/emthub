# EMTBaseVoltage

List all (preferred) base voltages found in a transmission system.

**CIM Class:** [BaseVoltage](profile.html#BaseVoltage)

**Python Key:** nominalVoltage

  -----------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------
  nominalVoltage                      c:BaseVoltage.nominalVoltage

  -----------------------------------------------------------------------

  : EMTBaseVoltage Query Dictionary

# EMTBranchFlow

Branch power flows in a merged instance, keyed on *Equipment*.
*Equipment_type* may be *ACLineSegment*, *DisconnectingCircuitBreaker*,
etc. Use the *EMTXfmrFlow* query for transformer winding flows.

**CIM Classes:** [SvPowerFlow](profile.html#SvPowerFlow),
[ConductingEquipment](profile.html#ConductingEquipment)

**Python Key:** mRID:sequenceNumber

  -------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -------------------------------------
  Equipment_type                      class name of associated
                                      [Equipment](profile.html#Equipment)

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name

  p                                   c:SvPowerFlow.p

  q                                   c:SvPowerFlow.q

  sequenceNumber                      c:ACDCTerminal.sequenceNumber
  -------------------------------------------------------------------------

  : EMTBranchFlow Query Dictionary

# EMTBranchFlowIC

Branch power flows in a standalone file. Don\'t select the system. Keyed
on *Equipment*. Filtering on *EquipmentContainer* is not supported in
standalone IC files. Includes PowerTransformers.

**CIM Classes:** [SvPowerFlow](profile.html#SvPowerFlow),
[ConductingEquipment](profile.html#ConductingEquipment)

**Python Key:** mRID:sequenceNumber

  -----------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------
  mRID                                c:IdentifiedObject.mRID

  p                                   c:SvPowerFlow.p

  q                                   c:SvPowerFlow.q

  sequenceNumber                      c:ACDCTerminal.sequenceNumber
  -----------------------------------------------------------------------

  : EMTBranchFlowIC Query Dictionary

# EMTBranchLimit

Operational limits for conducting equipment. *Equipment_type* may be
*ACLineSegment*, *DisconnectingCircuitBreaker*, etc. Use the
*EMTXfmrLimit* query for transformer winding limits.

**CIM Classes:** [ApparentPowerLimit](profile.html#ApparentPowerLimit),
[ConductingEquipment](profile.html#ConductingEquipment)

**Python Key:** mRID

  -----------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------------------------------
  Equipment_mRID                      mRID for [Equipment](profile.html#Equipment)

  Equipment_type                      class name of associated
                                      [Equipment](profile.html#Equipment)

  OperationalLimitType_name           name for
                                      [OperationalLimitType](profile.html#OperationalLimitType)

  acceptableDuration                  c:OperationalLimitType.acceptableDuration

  direction                           c:OperationalLimitType.direction

  isInfiniteDuration                  c:OperationalLimitType.isInfiniteDuration

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name

  value                               c:ApparentPowerLimit.value
  -----------------------------------------------------------------------------------------------

  : EMTBranchLimit Query Dictionary

# EMTBus

Buses and their base voltages.

**CIM Classes:** [ConnectivityNode](profile.html#ConnectivityNode),
[BaseVoltage](profile.html#BaseVoltage)

**Python Key:** mRID

  -----------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------
  BaseVoltage_nominalVoltage          c:BaseVoltage.nominalVoltage

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name
  -----------------------------------------------------------------------

  : EMTBus Query Dictionary

# EMTBusVoltage

Bus voltages from power flow in a merged instance, keyed on
*ConnectivityNode*.

**CIM Classes:** [SvVoltage](profile.html#SvVoltage),
[ConnectivityNode](profile.html#ConnectivityNode),
[TopologicalNode](profile.html#TopologicalNode)

**Python Key:** mRID

  -----------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------
  angle                               c:SvVoltage.angle

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name

  v                                   c:SvVoltage.v
  -----------------------------------------------------------------------

  : EMTBusVoltage Query Dictionary

# EMTBusVoltageIC

Bus voltages from power flow in a standalone file. Keyed on
*ConnectivityNode*. Filtering on *EquipmentContainer* is not supported
in standalone IC files.

**CIM Classes:** [SvVoltage](profile.html#SvVoltage),
[ConnectivityNode](profile.html#ConnectivityNode),
[TopologicalNode](profile.html#TopologicalNode)

**Python Key:** mRID

  -----------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------
  angle                               c:SvVoltage.angle

  mRID                                c:IdentifiedObject.mRID

  v                                   c:SvVoltage.v
  -----------------------------------------------------------------------

  : EMTBusVoltageIC Query Dictionary

# EMTBusXY

XY bus coordinates for graphical layouts.

**CIM Classes:** [TextDiagramObject](profile.html#TextDiagramObject),
[DiagramObjectPoint](profile.html#DiagramObjectPoint)

**Python Key:** mRID

  ---------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- ---------------------------------------------------
  ConnectivityNode_mRID               mRID for
                                      [ConnectivityNode](profile.html#ConnectivityNode)

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name

  sequenceNumber                      c:DiagramObjectPoint.sequenceNumber

  text                                c:TextDiagramObject.text

  xPosition                           c:DiagramObjectPoint.xPosition

  yPosition                           c:DiagramObjectPoint.yPosition
  ---------------------------------------------------------------------------------------

  : EMTBusXY Query Dictionary

# EMTCompSeries

Series capacitor or reactor.

**CIM Class:** [SeriesCompensator](profile.html#SeriesCompensator)

**Python Key:** mRID

  -------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -------------------------------------------------------
  BaseVoltage_nominalVoltage          c:BaseVoltage.nominalVoltage

  ConnectivityNode1_mRID              mRID for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **1**

  ConnectivityNode1_name              name for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **1**

  ConnectivityNode2_mRID              mRID for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **2**

  ConnectivityNode2_name              name for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **2**

  EquipmentContainer_mRID             mRID for
                                      [EquipmentContainer](profile.html#EquipmentContainer)

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name

  r                                   c:SeriesCompensator.r

  r0                                  c:SeriesCompensator.r0

  x                                   c:SeriesCompensator.x

  x0                                  c:SeriesCompensator.x0
  -------------------------------------------------------------------------------------------

  : EMTCompSeries Query Dictionary

# EMTCompShunt

Shunt reactor or capacitor.

**CIM Class:**
[LinearShuntCompensator](profile.html#LinearShuntCompensator)

**Python Key:** mRID

  -------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -------------------------------------------------------
  BaseVoltage_nominalVoltage          c:BaseVoltage.nominalVoltage

  ConnectivityNode1_mRID              mRID for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **1**

  ConnectivityNode1_name              name for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **1**

  EquipmentContainer_mRID             mRID for
                                      [EquipmentContainer](profile.html#EquipmentContainer)

  bPerSection                         c:LinearShuntCompensator.bPerSection

  gPerSection                         c:LinearShuntCompensator.gPerSection

  mRID                                c:IdentifiedObject.mRID

  maximumSections                     c:ShuntCompensator.maximumSections

  name                                c:IdentifiedObject.name

  nomU                                c:ShuntCompensator.nomU

  sections                            c:ShuntCompensator.sections
  -------------------------------------------------------------------------------------------

  : EMTCompShunt Query Dictionary

# EMTContainer

Lists all the transmission systems found in a CIM RDF file. The *mRID*
can be used to filter on the system, when constructing a network model
from a CIM RDF file that contains multiple transmission systems.

**CIM Class:** [EquipmentContainer](profile.html#EquipmentContainer)

**Python Key:** mRID

  -----------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------
  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name
  -----------------------------------------------------------------------

  : EMTContainer Query Dictionary

# EMTCountAPIInputs

Counts the number of input signals in each CIGRE TB 958 API model.

**CIM Classes:** [IEEECigreAPIInput](profile.html#IEEECigreAPIInput),
[IEEECigreAPI](profile.html#IEEECigreAPI)

**Python Key:** mRID

  -----------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------
  count                               number of instances matching mRID

  mRID                                c:IdentifiedObject.mRID
  -----------------------------------------------------------------------

  : EMTCountAPIInputs Query Dictionary

# EMTCountAPIOutputs

Counts the number of output signals in each CIGRE TB 958 API model\'s
interface.

**CIM Classes:** [IEEECigreAPIOutput](profile.html#IEEECigreAPIOutput),
[IEEECigreAPI](profile.html#IEEECigreAPI)

**Python Key:** mRID

  -----------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------
  count                               number of instances matching mRID

  mRID                                c:IdentifiedObject.mRID
  -----------------------------------------------------------------------

  : EMTCountAPIOutputs Query Dictionary

# EMTCountAPIParameters

Counts the number of parameters in each CIGRE TB 958 API model.

**CIM Classes:**
[IEEECigreAPIParameter](profile.html#IEEECigreAPIParameter),
[IEEECigreAPI](profile.html#IEEECigreAPI)

**Python Key:** mRID

  -----------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------
  count                               number of instances matching mRID

  mRID                                c:IdentifiedObject.mRID
  -----------------------------------------------------------------------

  : EMTCountAPIParameters Query Dictionary

# EMTCountPowerXfmrWindings

Count the number of windings in each *PowerTransformer*.

**CIM Class:** [PowerTransformerEnd](profile.html#PowerTransformerEnd)

**Python Key:** mRID

  -----------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------
  count                               number of instances matching mRID

  mRID                                c:IdentifiedObject.mRID
  -----------------------------------------------------------------------

  : EMTCountPowerXfmrWindings Query Dictionary

# EMTDCEnergySource

Solar panels, batteries, and other DC sources that don\'t rely on
primary AC power.

**CIM Class:** [DCEnergySource](profile.html#DCEnergySource)

**Python Key:** mRID

  -------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -------------------------------------------------------
  DCNode1_mRID                        mRID for [DCNode1](profile.html#DCNode1)

  EquipmentContainer_mRID             mRID for
                                      [EquipmentContainer](profile.html#EquipmentContainer)

  kind                                e:DCEnergySource.kind

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name

  ratedUdc                            c:DCConductingEquipment.ratedUdc
  -------------------------------------------------------------------------------------------

  : EMTDCEnergySource Query Dictionary

# EMTDCEquipmentContainer

A container just for the DC nodes in the transmission system.

**CIM Class:** [DCEquipmentContainer](profile.html#DCEquipmentContainer)

**Python Key:** mRID

  -----------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------
  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name
  -----------------------------------------------------------------------

  : EMTDCEquipmentContainer Query Dictionary

# EMTDCNode

DC buses.

**CIM Class:** [DCNode](profile.html#DCNode)

**Python Key:** mRID

  -----------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------------------------------
  DCEquipmentContainer_mRID           mRID for
                                      [DCEquipmentContainer](profile.html#DCEquipmentContainer)

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name
  -----------------------------------------------------------------------------------------------

  : EMTDCNode Query Dictionary

# EMTDCShunt

DC shunt capacitors and resistive loads.

**CIM Class:** [DCShunt](profile.html#DCShunt)

**Python Key:** mRID

  -------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -------------------------------------------------------
  DCNode1_mRID                        mRID for [DCNode1](profile.html#DCNode1)

  EquipmentContainer_mRID             mRID for
                                      [EquipmentContainer](profile.html#EquipmentContainer)

  capacitance                         c:DCShunt.capacitance

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name

  ratedUdc                            c:DCConductingEquipment.ratedUdc

  resistance                          c:DCShunt.resistance
  -------------------------------------------------------------------------------------------

  : EMTDCShunt Query Dictionary

# EMTDisconnectingCircuitBreaker

A three-phase breaker with disconnect switches.

**CIM Class:**
[DisconnectingCircuitBreaker](profile.html#DisconnectingCircuitBreaker)

**Python Key:** mRID

  -------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -------------------------------------------------------
  BaseVoltage_nominalVoltage          c:BaseVoltage.nominalVoltage

  ConnectivityNode1_mRID              mRID for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **1**

  ConnectivityNode1_name              name for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **1**

  ConnectivityNode2_mRID              mRID for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **2**

  ConnectivityNode2_name              name for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **2**

  EquipmentContainer_mRID             mRID for
                                      [EquipmentContainer](profile.html#EquipmentContainer)

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name
  -------------------------------------------------------------------------------------------

  : EMTDisconnectingCircuitBreaker Query Dictionary

# EMTDynamicsModel

A controller for machines or power electronics.

**CIM Class:**
[DetailedModelDynamics](profile.html#DetailedModelDynamics)

**Python Key:** mRID

  ---------------------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- ---------------------------------------------------------------------
  DetailedModelTypeDynamics_mRID      mRID for
                                      [DetailedModelTypeDynamics](profile.html#DetailedModelTypeDynamics)

  DetailedModelTypeDynamics_name      name for
                                      [DetailedModelTypeDynamics](profile.html#DetailedModelTypeDynamics)

  Equipment_mRID                      mRID for [Equipment](profile.html#Equipment)

  Equipment_name                      name for [Equipment](profile.html#Equipment)

  Equipment_type                      class name of associated [Equipment](profile.html#Equipment)

  mRID                                c:IdentifiedObject.mRID

  modelKind                           e:NthAmDynamicModel.modelKind

  name                                c:IdentifiedObject.name
  ---------------------------------------------------------------------------------------------------------

  : EMTDynamicsModel Query Dictionary

# EMTDynamicsModelType

A type of controller defined from proprietary file formats.

**CIM Class:** [NthAmDynamicModel](profile.html#NthAmDynamicModel)

**Python Key:** mRID

  ------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- ------------------------------------------
  closestStandardModel                e:NthAmDynamicModel.closestStandardModel

  mRID                                c:IdentifiedObject.mRID

  modelKind                           e:NthAmDynamicModel.modelKind

  name                                c:IdentifiedObject.name

  nameKind                            c:IdentifiedObject.name

  statusKind                          e:NthAmDynamicModel.statusKind
  ------------------------------------------------------------------------------

  : EMTDynamicsModelType Query Dictionary

# EMTDynamicsParameter

Parameter value for a controller instance.

**CIM Class:** [ParameterValue](profile.html#ParameterValue)

**Python Key:** Equipment_mRID:DetailedModelTypeDynamics_mRID:name

  ---------------------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- ---------------------------------------------------------------------
  DetailedModelTypeDynamics_mRID      mRID for
                                      [DetailedModelTypeDynamics](profile.html#DetailedModelTypeDynamics)

  DetailedModelTypeDynamics_name      name for
                                      [DetailedModelTypeDynamics](profile.html#DetailedModelTypeDynamics)

  Equipment_mRID                      mRID for [Equipment](profile.html#Equipment)

  Equipment_name                      name for [Equipment](profile.html#Equipment)

  Equipment_type                      class name of associated [Equipment](profile.html#Equipment)

  ParameterDescriptor_mRID            mRID for [ParameterDescriptor](profile.html#ParameterDescriptor)

  name                                c:IdentifiedObject.name

  sequenceNumber                      c:ParameterDescriptor.sequenceNumber

  value                               c:ParameterValue.value
  ---------------------------------------------------------------------------------------------------------

  : EMTDynamicsParameter Query Dictionary

# EMTDynamicsParameterDescriptor

Describes the name and other metadata for a dynamics parameter.

**CIM Class:** [ParameterDescriptor](profile.html#ParameterDescriptor)

**Python Key:** mRID

  ---------------------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- ---------------------------------------------------------------------
  DetailedModelTypeDynamics_mRID      mRID for
                                      [DetailedModelTypeDynamics](profile.html#DetailedModelTypeDynamics)

  DetailedModelTypeDynamics_name      name for
                                      [DetailedModelTypeDynamics](profile.html#DetailedModelTypeDynamics)

  engineeringUnit                     c:ParameterDescriptor.engineeringUnit

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name

  sequenceNumber                      c:ParameterDescriptor.sequenceNumber

  typicalValue                        c:ParameterDescriptor.typicalValue
  ---------------------------------------------------------------------------------------------------------

  : EMTDynamicsParameterDescriptor Query Dictionary

# EMTEnergySource

A Thevenin equivalent source.

**CIM Classes:** [EnergySource](profile.html#EnergySource),
[BaseVoltage](profile.html#BaseVoltage)

**Python Key:** mRID

  -------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -------------------------------------------------------
  BaseVoltage_nominalVoltage          c:BaseVoltage.nominalVoltage

  ConnectivityNode1_mRID              mRID for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **1**

  ConnectivityNode1_name              name for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **1**

  EnergySource_nominalVoltage         c:EnergySource.nominalVoltage

  EquipmentContainer_mRID             mRID for
                                      [EquipmentContainer](profile.html#EquipmentContainer)

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name

  r                                   c:EnergySource.r

  r0                                  c:EnergySource.r0

  voltageAngle                        c:EnergySource.voltageAngle

  voltageMagnitude                    c:EnergySource.voltageMagnitude

  x                                   c:EnergySource.x

  x0                                  c:EnergySource.x0
  -------------------------------------------------------------------------------------------

  : EMTEnergySource Query Dictionary

# EMTEquipmentContainer

An equipment container represents the whole transmission system.

**CIM Class:** [EquipmentContainer](profile.html#EquipmentContainer)

**Python Key:** mRID

  -----------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------
  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name
  -----------------------------------------------------------------------

  : EMTEquipmentContainer Query Dictionary

# EMTIBRPlant\*

Collection of equipment comprising an inverter-based resource plant. May
return multiple rows for the same plant *mRID*. Use the
*EMTIBRPlantAttributes* query to retrieve the plant-level attributes.
*Equipment_type* is typically *ACLineSegment*, *PowerTransformer*,
*PowerElectronicsConnection*, or *DisconnectingCircuitBreaker* but may
include other types.

**CIM Class:** [IBRPlant](profile.html#IBRPlant)

**Python Multi-Key:** mRID\*

  -------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -------------------------------------
  Equipment_mRID                      mRID for
                                      [Equipment](profile.html#Equipment)

  Equipment_type                      class name of associated
                                      [Equipment](profile.html#Equipment)

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name
  -------------------------------------------------------------------------

  : EMTIBRPlant\* Query Dictionary

# EMTIBRPlantAttributes

IBR plant attributes, keyed on the inverter ID for convenience.

**CIM Class:** [IBRPlant](profile.html#IBRPlant)

**Python Key:** PowerElectronicsConnection_mRID

  -----------------------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------------------------------------------
  IEEECigreAPI_mRID                   mRID for [IEEECigreAPI](profile.html#IEEECigreAPI)

  PowerElectronicsConnection_mRID     mRID for
                                      [PowerElectronicsConnection](profile.html#PowerElectronicsConnection)

  dcLinkVoltage                       e:IBRPlant.dcLinkVoltage

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name

  switchingFrequency                  e:IBRPlant.switchingFrequency
  -----------------------------------------------------------------------------------------------------------

  : EMTIBRPlantAttributes Query Dictionary

# EMTIEEECigreAPI

CIGRE TB 958 API model attached to an inverter.

**CIM Class:** [IEEECigreAPI](profile.html#IEEECigreAPI)

**Python Key:** mRID

  -----------------------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------------------------------------------
  PowerElectronicsConnection_mRID     mRID for
                                      [PowerElectronicsConnection](profile.html#PowerElectronicsConnection)

  apiDLLInterfaceVersion              e:IEEECigreAPI.apiDLLInterfaceVersion

  apiEmtRmsMode                       e:IEEECigreAPI.apiEmtRmsMode

  apiFixedStepBaseSampleTime          e:IEEECigreAPI.apiFixedStepBaseSampleTime

  apiModelName                        e:IEEECigreAPI.apiModelName

  apiModelVersion                     e:IEEECigreAPI.apiModelVersion

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name

  shareable                           e:IEEECigreAPI.shareable

  snapshotUri                         e:IEEECigreAPI.snapshotUri

  uri                                 e:IEEECigreAPI.uri
  -----------------------------------------------------------------------------------------------------------

  : EMTIEEECigreAPI Query Dictionary

# EMTIEEECigreAPIInfo

Supplemental information from the CIGRE TB 958 API about a model\'s
interface.

**CIM Classes:** [IEEECigreAPI](profile.html#IEEECigreAPI),
[IEEECigreAPIInfo](profile.html#IEEECigreAPIInfo)

**Python Key:** mRID

  ---------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- ---------------------------------------------
  apiGeneralInformation               e:IEEECigreAPIInfo.apiGeneralInformation

  apiModelCreated                     e:IEEECigreAPIInfo.apiModelCreated

  apiModelCreator                     e:IEEECigreAPIInfo.apiModelCreator

  apiModelDescription                 e:IEEECigreAPIInfo.apiModelDescription

  apiModelLastModifiedBy              e:IEEECigreAPIInfo.apiModelLastModifiedBy

  apiModelLastModifiedDate            e:IEEECigreAPIInfo.apiModelLastModifiedDate

  apiModelModifiedComment             e:IEEECigreAPIInfo.apiModelModifiedComment

  apiModelModifiedHistory             e:IEEECigreAPIInfo.apiModelModifiedHistory

  apiNumDoubleStates                  e:IEEECigreAPIInfo.apiNumDoubleStates

  apiNumFloatStates                   e:IEEECigreAPIInfo.apiNumFloatStates

  apiNumInputPorts                    e:IEEECigreAPIInfo.apiNumInputPorts

  apiNumIntStates                     e:IEEECigreAPIInfo.apiNumIntStates

  apiNumOutputPorts                   e:IEEECigreAPIInfo.apiNumOutputPorts

  apiNumParameters                    e:IEEECigreAPIInfo.apiNumParameters

  mRID                                c:IdentifiedObject.mRID
  ---------------------------------------------------------------------------------

  : EMTIEEECigreAPIInfo Query Dictionary

# EMTIEEECigreAPIInputSignalInfos\*

Supplemental information from the CIGRE TB 958 API about a model\'s
input ports (signals). May return multiple rows for the same API *mRID*.

**CIM Classes:** [IEEECigreAPIInput](profile.html#IEEECigreAPIInput),
[IEEECigreAPISignalInfo](profile.html#IEEECigreAPISignalInfo),
[IEEECigreAPI](profile.html#IEEECigreAPI)

**Python Multi-Key:** mRID\*

  -----------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------------
  apiDescription                      e:IEEECigreAPISignalInfo.apiDescription

  apiSequenceNumber                   e:IEEECigreAPISignal.apiSequenceNumber

  apiUnit                             e:IEEECigreAPISignalInfo.apiUnit

  mRID                                c:IdentifiedObject.mRID
  -----------------------------------------------------------------------------

  : EMTIEEECigreAPIInputSignalInfos\* Query Dictionary

# EMTIEEECigreAPIInputs\*

List the metadata of input signals for the CIGRE TB 958 API models. May
return multiple rows for the same API *mRID*.

**CIM Classes:** [IEEECigreAPIInput](profile.html#IEEECigreAPIInput),
[IEEECigreAPI](profile.html#IEEECigreAPI)

**Python Multi-Key:** mRID\*

  ---------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- ---------------------------------------------------
  ACDCTerminal_mRID                   mRID for [ACDCTerminal](profile.html#ACDCTerminal)

  ConnectivityNode_mRID               mRID for
                                      [ConnectivityNode](profile.html#ConnectivityNode)

  DCNode_mRID                         mRID for [DCNode](profile.html#DCNode)

  apiName                             e:IEEECigreAPISignal.apiName

  apiParameterKind                    e:IEEECigreAPISignal.apiParameterKind

  apiSequenceNumber                   e:IEEECigreAPISignal.apiSequenceNumber

  apiWidth                            e:IEEECigreAPISignal.apiWidth

  kind                                e:IEEECigreAPIInput.kind

  mRID                                c:IdentifiedObject.mRID

  multiplier                          e:IEEECigreAPISignal.multiplier

  phase                               e:IEEECigreAPISignal.phase

  sensorRatio                         e:IEEECigreAPIInput.sensorRatio

  unit                                e:IEEECigreAPISignal.unit
  ---------------------------------------------------------------------------------------

  : EMTIEEECigreAPIInputs\* Query Dictionary

# EMTIEEECigreAPIOutputSignalInfos\*

Supplemental information from the CIGRE TB 958 API about a model\'s
output ports (signals). May return multiple rows for the same API
*mRID*.

**CIM Classes:** [IEEECigreAPIOutput](profile.html#IEEECigreAPIOutput),
[IEEECigreAPISignalInfo](profile.html#IEEECigreAPISignalInfo),
[IEEECigreAPI](profile.html#IEEECigreAPI)

**Python Multi-Key:** mRID\*

  -----------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------------
  apiDescription                      e:IEEECigreAPISignalInfo.apiDescription

  apiSequenceNumber                   e:IEEECigreAPISignal.apiSequenceNumber

  apiUnit                             e:IEEECigreAPISignalInfo.apiUnit

  mRID                                c:IdentifiedObject.mRID
  -----------------------------------------------------------------------------

  : EMTIEEECigreAPIOutputSignalInfos\* Query Dictionary

# EMTIEEECigreAPIOutputs\*

List the metadata of output signals for the CIGRE TB 958 API models. May
return multiple rows for the same API *mRID*.

**CIM Classes:** [IEEECigreAPIOutput](profile.html#IEEECigreAPIOutput),
[IEEECigreAPI](profile.html#IEEECigreAPI)

**Python Multi-Key:** mRID\*

  ---------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- ---------------------------------------------------
  ACDCTerminal_mRID                   mRID for [ACDCTerminal](profile.html#ACDCTerminal)

  ConnectivityNode_mRID               mRID for
                                      [ConnectivityNode](profile.html#ConnectivityNode)

  DCNode_mRID                         mRID for [DCNode](profile.html#DCNode)

  apiName                             e:IEEECigreAPISignal.apiName

  apiParameterKind                    e:IEEECigreAPISignal.apiParameterKind

  apiSequenceNumber                   e:IEEECigreAPISignal.apiSequenceNumber

  apiWidth                            e:IEEECigreAPISignal.apiWidth

  kind                                e:IEEECigreAPIOutput.kind

  mRID                                c:IdentifiedObject.mRID

  multiplier                          e:IEEECigreAPISignal.multiplier

  phase                               e:IEEECigreAPISignal.phase

  scalingRatio                        e:IEEECigreAPIOutput.scalingRatio

  unit                                e:IEEECigreAPISignal.unit
  ---------------------------------------------------------------------------------------

  : EMTIEEECigreAPIOutputs\* Query Dictionary

# EMTIEEECigreAPIParameterInfos\*

Supplemental information from the CIGRE TB 958 API about a model\'s
parameters. May return multiple rows for the same API *mRID*.

**CIM Classes:**
[IEEECigreAPIParameter](profile.html#IEEECigreAPIParameter),
[IEEECigreAPIParameterInfo](profile.html#IEEECigreAPIParameterInfo),
[IEEECigreAPI](profile.html#IEEECigreAPI)

**Python Multi-Key:** mRID\*

  ---------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- ---------------------------------------------
  apiDefaultValue                     e:IEEECigreAPIParameterInfo.apiDefaultValue

  apiDescription                      e:IEEECigreAPIParameterInfo.apiDescription

  apiFixedValue                       e:IEEECigreAPIParameterInfo.apiFixedValue

  apiGroupName                        e:IEEECigreAPIParameterInfo.apiGroupName

  apiMaxValue                         e:IEEECigreAPIParameterInfo.apiMaxValue

  apiMinValue                         e:IEEECigreAPIParameterInfo.apiMinValue

  apiName                             e:IEEECigreAPIParameterInfo.apiName

  apiSequenceNumber                   e:IEEECigreAPIParameter.apiSequenceNumber

  apiUnit                             e:IEEECigreAPIParameterInfo.apiUnit

  mRID                                c:IdentifiedObject.mRID
  ---------------------------------------------------------------------------------

  : EMTIEEECigreAPIParameterInfos\* Query Dictionary

# EMTIEEECigreAPIParameters\*

List the values and sizes of parameters for the CIGRE TB 958 API models.
May return multiple rows for the same API *mRID*.

**CIM Classes:**
[IEEECigreAPIParameter](profile.html#IEEECigreAPIParameter),
[IEEECigreAPI](profile.html#IEEECigreAPI)

**Python Multi-Key:** mRID\*

  -------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -------------------------------------------
  apiParameterKind                    e:IEEECigreAPIParameter.apiParameterKind

  apiSequenceNumber                   e:IEEECigreAPIParameter.apiSequenceNumber

  mRID                                c:IdentifiedObject.mRID

  value                               e:IEEECigreAPIParameter.value
  -------------------------------------------------------------------------------

  : EMTIEEECigreAPIParameters\* Query Dictionary

# EMTLine

A three-phase transposed line, overhead or underground.

**CIM Class:** [ACLineSegment](profile.html#ACLineSegment)

**Python Key:** mRID

  -------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -------------------------------------------------------
  BaseVoltage_nominalVoltage          c:BaseVoltage.nominalVoltage

  ConnectivityNode1_mRID              mRID for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **1**

  ConnectivityNode1_name              name for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **1**

  ConnectivityNode2_mRID              mRID for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **2**

  ConnectivityNode2_name              name for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **2**

  EquipmentContainer_mRID             mRID for
                                      [EquipmentContainer](profile.html#EquipmentContainer)

  b0ch                                c:ACLineSegment.b0ch

  bch                                 c:ACLineSegment.bch

  length                              c:Conductor.length

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name

  r                                   c:ACLineSegment.r

  r0                                  c:ACLineSegment.r0

  x                                   c:ACLineSegment.x

  x0                                  c:ACLineSegment.x0
  -------------------------------------------------------------------------------------------

  : EMTLine Query Dictionary

# EMTLoad

Balanced three-phase ZIP load.

**CIM Classes:** [EnergyConsumer](profile.html#EnergyConsumer),
[LoadResponseCharacteristic](profile.html#LoadResponseCharacteristic)

**Python Key:** mRID

  -------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -------------------------------------------------------
  BaseVoltage_nominalVoltage          c:BaseVoltage.nominalVoltage

  ConnectivityNode1_mRID              mRID for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **1**

  ConnectivityNode1_name              name for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **1**

  EquipmentContainer_mRID             mRID for
                                      [EquipmentContainer](profile.html#EquipmentContainer)

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name

  p                                   c:EnergyConsumer.p

  pConstantCurrent                    c:LoadResponseCharacteristic.pConstantCurrent

  pConstantImpedance                  c:LoadResponseCharacteristic.pConstantImpedance

  pConstantPower                      c:LoadResponseCharacteristic.pConstantPower

  pVoltageExponent                    c:LoadResponseCharacteristic.pVoltageExponent

  q                                   c:EnergyConsumer.q

  qConstantCurrent                    c:LoadResponseCharacteristic.qConstantCurrent

  qConstantImpedance                  c:LoadResponseCharacteristic.qConstantImpedance

  qConstantPower                      c:LoadResponseCharacteristic.qConstantPower

  qVoltageExponent                    c:LoadResponseCharacteristic.qVoltageExponent
  -------------------------------------------------------------------------------------------

  : EMTLoad Query Dictionary

# EMTPowerXfmrCore

Linear exciting current branch for a transformer.

**CIM Class:**
[TransformerCoreAdmittance](profile.html#TransformerCoreAdmittance)

**Python Key:** PowerTransformer_mRID

  ---------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- ---------------------------------------------------------
  PowerTransformerEnd_mRID            mRID for
                                      [PowerTransformerEnd](profile.html#PowerTransformerEnd)

  PowerTransformer_mRID               mRID for
                                      [PowerTransformer](profile.html#PowerTransformer)

  PowerTransformer_name               name for
                                      [PowerTransformer](profile.html#PowerTransformer)

  b                                   c:TransformerCoreAdmittance.b

  endNumber                           c:TransformerEnd.endNumber

  g                                   c:TransformerCoreAdmittance.g

  mRID                                c:IdentifiedObject.mRID
  ---------------------------------------------------------------------------------------------

  : EMTPowerXfmrCore Query Dictionary

# EMTPowerXfmrMesh

Mesh impedances between pairs of transformer windings. Note that SI
units are used, referred to the highest voltage winding in the pair.

**CIM Class:**
[TransformerMeshImpedance](profile.html#TransformerMeshImpedance)

**Python Key:** FromTransformerEnd_mRID:ToTransformerEnd_mRID

  ---------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- ---------------------------------------------------
  FromTransformerEnd_endNumber        endNumber of the **From**
                                      [TransformerEnd](profile.html#TransformerEnd)

  FromTransformerEnd_mRID             mRID for **From**
                                      [TransformerEnd](profile.html#TransformerEnd)

  PowerTransformer_mRID               mRID for
                                      [PowerTransformer](profile.html#PowerTransformer)

  PowerTransformer_name               name for
                                      [PowerTransformer](profile.html#PowerTransformer)

  ToTransformerEnd_endNumber          endNumber of the **To**
                                      [TransformerEnd](profile.html#TransformerEnd)

  ToTransformerEnd_mRID               mRID for **To**
                                      [TransformerEnd](profile.html#TransformerEnd)

  mRID                                c:IdentifiedObject.mRID

  r                                   c:TransformerMeshImpedance.r

  x                                   c:TransformerMeshImpedance.x
  ---------------------------------------------------------------------------------------

  : EMTPowerXfmrMesh Query Dictionary

# EMTPowerXfmrWinding

Three-phase, balanced, multi-winding power transformers defined by data
for windings, mesh impedances, and core admittance. The datasheet option
is not supported in this query. The query returns one row for each
winding of a transformer.

**CIM Class:** [PowerTransformerEnd](profile.html#PowerTransformerEnd)

**Python Key:** PowerTransformer_mRID:endNumber

  ---------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- ---------------------------------------------------
  BaseVoltage_nominalVoltage          c:BaseVoltage.nominalVoltage

  ConnectivityNode1_mRID              mRID for
                                      [ConnectivityNode](profile.html#ConnectivityNode)
                                      **1**

  ConnectivityNode1_name              name for
                                      [ConnectivityNode](profile.html#ConnectivityNode)
                                      **1**

  PowerTransformer_mRID               mRID for
                                      [PowerTransformer](profile.html#PowerTransformer)

  PowerTransformer_name               name for
                                      [PowerTransformer](profile.html#PowerTransformer)

  connectionKind                      c:PowerTransformerEnd.connectionKind

  endNumber                           c:TransformerEnd.endNumber

  grounded                            c:TransformerEnd.grounded

  mRID                                c:IdentifiedObject.mRID

  phaseAngleClock                     c:PowerTransformerEnd.phaseAngleClock

  ratedS                              c:PowerTransformerEnd.ratedS

  ratedU                              c:PowerTransformerEnd.ratedU

  rground                             c:TransformerEnd.rground

  vectorGroup                         c:PowerTransformer.vectorGroup

  xground                             c:TransformerEnd.xground
  ---------------------------------------------------------------------------------------

  : EMTPowerXfmrWinding Query Dictionary

# EMTRotatingMachinePlant\*

Collection of equipment comprising a conventional generating plant. May
return multiple rows for the same plant *mRID*. *Equipment_type* is
typically *SynchronousMachine*, *PowerTransformer*, or
*DisconnectingCircuitBreaker* but may include other types.

**CIM Class:** [RotatingMachinePlant](profile.html#RotatingMachinePlant)

**Python Multi-Key:** mRID\*

  -------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -------------------------------------
  Equipment_mRID                      mRID for
                                      [Equipment](profile.html#Equipment)

  Equipment_type                      class name of associated
                                      [Equipment](profile.html#Equipment)

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name
  -------------------------------------------------------------------------

  : EMTRotatingMachinePlant\* Query Dictionary

# EMTSolar

An inverter with associated solar generation. Keyed on the
*PowerElectronicsConnection*.

**CIM Class:**
[PowerElectronicsConnection](profile.html#PowerElectronicsConnection)

**Python Key:** mRID

  -------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -------------------------------------------------------
  ConnectivityNode1_mRID              mRID for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **1**

  ConnectivityNode1_name              name for
                                      [ConnectivityNode](profile.html#ConnectivityNode) **1**

  EquipmentContainer_mRID             mRID for
                                      [EquipmentContainer](profile.html#EquipmentContainer)

  PhotoVoltaicUnit_mRID               mRID for
                                      [PhotoVoltaicUnit](profile.html#PhotoVoltaicUnit)

  mRID                                c:IdentifiedObject.mRID

  maxIFault                           c:PowerElectronicsConnection.maxIFault

  maxP                                c:PowerElectronicsUnit.maxP

  maxQ                                c:PowerElectronicsConnection.maxQ

  minP                                c:PowerElectronicsUnit.minP

  minQ                                c:PowerElectronicsConnection.minQ

  name                                c:IdentifiedObject.name

  p                                   c:PowerElectronicsConnection.p

  q                                   c:PowerElectronicsConnection.q

  ratedS                              c:PowerElectronicsConnection.ratedS

  ratedU                              c:PowerElectronicsConnection.ratedU
  -------------------------------------------------------------------------------------------

  : EMTSolar Query Dictionary

# EMTSyncMachine

A *SynchronousMachine* with dynamic parameters. The
*GeneratingUnit_type* is typically *HydroGeneratingUnit*,
*NuclearGeneratingUnit*, or *ThermalGeneratingUnit*.

**CIM Classes:** [SynchronousMachine](profile.html#SynchronousMachine),
[SynchronousMachineTimeConstantReactance](profile.html#SynchronousMachineTimeConstantReactance)

**Python Key:** mRID

  -----------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------------------------------
  ConnectivityNode1_mRID              mRID for [ConnectivityNode](profile.html#ConnectivityNode)
                                      **1**

  ConnectivityNode1_name              name for [ConnectivityNode](profile.html#ConnectivityNode)
                                      **1**

  EquipmentContainer_mRID             mRID for
                                      [EquipmentContainer](profile.html#EquipmentContainer)

  GeneratingUnit_mRID                 mRID for [GeneratingUnit](profile.html#GeneratingUnit)

  GeneratingUnit_type                 class name of associated
                                      [GeneratingUnit](profile.html#GeneratingUnit)

  inertia                             c:RotatingMachineDynamics.inertia

  mRID                                c:IdentifiedObject.mRID

  maxOperatingP                       c:GeneratingUnit.maxOperatingP

  maxQ                                c:SynchronousMachine.maxQ

  minOperatingP                       c:GeneratingUnit.minOperatingP

  minQ                                c:SynchronousMachine.minQ

  name                                c:IdentifiedObject.name

  p                                   c:RotatingMachine.p

  q                                   c:RotatingMachine.q

  ratedS                              c:RotatingMachine.ratedS

  ratedU                              c:RotatingMachine.ratedU

  statorLeakageReactance              c:RotatingMachineDynamics.statorLeakageReactance

  statorResistance                    c:RotatingMachineDynamics.statorResistance

  tpdo                                c:SynchronousMachineTimeConstantReactance.tpdo

  tppdo                               c:SynchronousMachineTimeConstantReactance.tppdo

  tppqo                               c:SynchronousMachineTimeConstantReactance.tppqo

  tpqo                                c:SynchronousMachineTimeConstantReactance.tpqo

  xDirectSubtrans                     c:SynchronousMachineTimeConstantReactance.xDirectSubtrans

  xDirectSync                         c:SynchronousMachineTimeConstantReactance.xDirectSync

  xDirectTrans                        c:SynchronousMachineTimeConstantReactance.xDirectTrans

  xQuadSubtrans                       c:SynchronousMachineTimeConstantReactance.xQuadSubtrans

  xQuadSync                           c:SynchronousMachineTimeConstantReactance.xQuadSync

  xQuadTrans                          c:SynchronousMachineTimeConstantReactance.xQuadTrans
  -----------------------------------------------------------------------------------------------

  : EMTSyncMachine Query Dictionary

# EMTWind

An inverter with associated wind generation. Keyed on the
*PowerElectronicsConnection*.

**CIM Class:**
[PowerElectronicsConnection](profile.html#PowerElectronicsConnection)

**Python Key:** mRID

  -------------------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -------------------------------------------------------------------
  ConnectivityNode1_mRID              mRID for [ConnectivityNode](profile.html#ConnectivityNode) **1**

  ConnectivityNode1_name              name for [ConnectivityNode](profile.html#ConnectivityNode) **1**

  EquipmentContainer_mRID             mRID for [EquipmentContainer](profile.html#EquipmentContainer)

  PowerElectronicsWindUnit_mRID       mRID for
                                      [PowerElectronicsWindUnit](profile.html#PowerElectronicsWindUnit)

  mRID                                c:IdentifiedObject.mRID

  maxIFault                           c:PowerElectronicsConnection.maxIFault

  maxP                                c:PowerElectronicsUnit.maxP

  maxQ                                c:PowerElectronicsConnection.maxQ

  minP                                c:PowerElectronicsUnit.minP

  minQ                                c:PowerElectronicsConnection.minQ

  name                                c:IdentifiedObject.name

  p                                   c:PowerElectronicsConnection.p

  q                                   c:PowerElectronicsConnection.q

  ratedS                              c:PowerElectronicsConnection.ratedS

  ratedU                              c:PowerElectronicsConnection.ratedU
  -------------------------------------------------------------------------------------------------------

  : EMTWind Query Dictionary

# EMTXfmrFlow

Transformer winding (end) power flows in a merged instance, keyed on
*TransformerEnd*.

**CIM Classes:** [SvPowerFlow](profile.html#SvPowerFlow),
[PowerTransformerEnd](profile.html#PowerTransformerEnd)

**Python Key:** mRID

  ---------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- ---------------------------------------------------
  PowerTransformer_mRID               mRID for
                                      [PowerTransformer](profile.html#PowerTransformer)

  endNumber                           c:TransformerEnd.endNumber

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name

  p                                   c:SvPowerFlow.p

  q                                   c:SvPowerFlow.q

  sequenceNumber                      c:ACDCTerminal.sequenceNumber
  ---------------------------------------------------------------------------------------

  : EMTXfmrFlow Query Dictionary

# EMTXfmrFlowIC

Transformer winding (end) power flows in a standalone file. WARNING: no
longer works with CIM Terminals in a standalone file; the IC and network
model should be merged first. Don\'t select the system. Keyed on
*TransformerEnd*. Filtering on *EquipmentContainer* is not supported in
standalone IC files.

**CIM Classes:** [SvPowerFlow](profile.html#SvPowerFlow),
[PowerTransformerEnd](profile.html#PowerTransformerEnd)

**Python Key:** mRID

  -----------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------
  mRID                                c:IdentifiedObject.mRID

  p                                   c:SvPowerFlow.p

  q                                   c:SvPowerFlow.q
  -----------------------------------------------------------------------

  : EMTXfmrFlowIC Query Dictionary

# EMTXfmrLimit

Operational limits for transformer windings.

**CIM Classes:** [ApparentPowerLimit](profile.html#ApparentPowerLimit),
[PowerTransformerEnd](profile.html#PowerTransformerEnd)

**Python Key:** mRID

  -----------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- -----------------------------------------------------------
  OperationalLimitType_name           name for
                                      [OperationalLimitType](profile.html#OperationalLimitType)

  PowerTransformerEnd_mRID            mRID for
                                      [PowerTransformerEnd](profile.html#PowerTransformerEnd)

  acceptableDuration                  c:OperationalLimitType.acceptableDuration

  direction                           c:OperationalLimitType.direction

  isInfiniteDuration                  c:OperationalLimitType.isInfiniteDuration

  mRID                                c:IdentifiedObject.mRID

  name                                c:IdentifiedObject.name

  value                               c:ApparentPowerLimit.value
  -----------------------------------------------------------------------------------------------

  : EMTXfmrLimit Query Dictionary

# EMTXfmrSaturation

Non-linear transformer saturation data. Does not include hysteresis, so
the resistive portion of *TransformerCoreAdmittance* should still be
included, but this replaces the inductive portion of
*TransformerCoreAdmittance*.

**CIM Classes:**
[TransformerSaturationCurve](profile.html#TransformerSaturationCurve),
[CurveData](profile.html#CurveData)

**Python Key:** PowerTransformer_mRID:amps

  ---------------------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- ---------------------------------------------------------------------
  PowerTransformer_mRID               mRID for [PowerTransformer](profile.html#PowerTransformer)

  PowerTransformer_name               name for [PowerTransformer](profile.html#PowerTransformer)

  TransformerCoreAdmittance_mRID      mRID for
                                      [TransformerCoreAdmittance](profile.html#TransformerCoreAdmittance)

  amps                                c:CurveData.xvalue

  vs                                  c:CurveData.y1value
  ---------------------------------------------------------------------------------------------------------

  : EMTXfmrSaturation Query Dictionary

# EMTXfmrTap

Off-nominal transformer tap in percent. The query returns one row for
each winding that has an off-nominal tap.

**CIM Class:** [RatioTapChanger](profile.html#RatioTapChanger)

**Python Key:** PowerTransformerEnd_mRID

  ---------------------------------------------------------------------------------------------
  Python Field                        CIM Attribute
  ----------------------------------- ---------------------------------------------------------
  PowerTransformerEnd_mRID            mRID for
                                      [PowerTransformerEnd](profile.html#PowerTransformerEnd)

  PowerTransformer_name               name for
                                      [PowerTransformer](profile.html#PowerTransformer)

  endNumber                           c:TransformerEnd.endNumber

  step                                c:TapChanger.step

  stepVoltageIncrement                c:RatioTapChanger.stepVoltageIncrement
  ---------------------------------------------------------------------------------------------

  : EMTXfmrTap Query Dictionary
