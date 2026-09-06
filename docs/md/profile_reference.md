# Profile Documentation

Profile namespace: <http://opensource.ieee.org/emtiop01p01#>

# Concrete Classes

::: {#ACDCConverterDCTerminal .container .group}
[#ACDCConverterDCTerminal](#ACDCConverterDCTerminal)

**ACDCConverterDCTerminal**

DC

A DC electrical connection point at the AC/DC converter. The AC/DC
converter is electrically connected also to the AC side. The AC
connection is inherited from the AC conducting equipment in the same way
as any other AC equipment. The AC/DC converter DC terminal is separate
from generic DC terminal to restrict the connection with the AC side to
AC/DC converter and so that no other DC conducting equipment can be
connected to the AC side.

**Native Members**

+----------------+----------------+----------------+----------------+
| polarity       | 0..1           | [DC Polarity   | Represents the |
|                |                | Kind           | normal network |
|                |                | \<#%20DCPo     | polarity       |
|                |                | l              | condition.     |
|                |                | arityKind\>]{. | Depending on   |
|                |                | title-ref}\_\_ | the converter  |
|                |                |                | configuration  |
|                |                |                | the value      |
|                |                |                | shall be set   |
|                |                |                | as follows:    |
|                |                |                |                |
|                |                |                | \- For a       |
|                |                |                | monopole with  |
|                |                |                | two converter  |
|                |                |                | terminals use  |
|                |                |                | DCPolarityKind |
|                |                |                | \"positive\"   |
|                |                |                | and            |
|                |                |                | \"negative\".  |
|                |                |                |                |
|                |                |                | \- For a       |
|                |                |                | bi-pole or     |
|                |                |                | symmetric      |
|                |                |                | monopole with  |
|                |                |                | three          |
|                |                |                | converter      |
|                |                |                | terminals use  |
|                |                |                | DCPolarityKind |
|                |                |                | \"positive\",  |
|                |                |                | \"middle\" and |
|                |                |                | \"negative\".  |
+----------------+----------------+----------------+----------------+
| DCCond u       | 0..1           | [ACDCC         | A DC converter |
| ctingEquipment |                | onverter       | terminal       |
|                |                | \<#ACD         | belong to an   |
|                |                | C              | DC converter.  |
|                |                | Converter\>]{. |                |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  -------- ------ ---------------------- ----------------------------------------
  DCNode   1..1   [DCNode](#DCNode)      see [DCBaseTerminal \<#DC
                                         BaseTerminal.DCNode\>]{.title-ref}\_\_

  -------- ------ ---------------------- ----------------------------------------

  ---------------- ------ ------------------- ----------------------------------
  sequenceNumber   1..1   [Inte               see [ACDCTerminal
                          ger](#Integer)      \<#ACDCTerminal.s
                                              equenceNumber\>]{.title-ref}\_\_

  ---------------- ------ ------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#ACLineSegment .container .group}
[#ACLineSegment](#ACLineSegment)

**ACLineSegment**

Wires

A line segment is a conductor or combination of conductors, with
consistent electrical characteristics along its length, building a
single electrical system that carries alternating current between two
points in the power system.

The BaseVoltage at the two ends of a line segment shall have the same
BaseVoltage.nominalVoltage. However, boundary lines may have slightly
different BaseVoltage.nominalVoltages and variation is allowed. Larger
voltage difference in general requires use of an equivalent branch.

Line segment impedances can be either directly described in electrical
terms or physical line detail can be provided from which impedances can
be calculated.

**Directly described impedances**

For symmetrical, transposed three phase line segments, it is sufficient
to use attributes of the line segment, which describe impedances and
admittances for the entire length of the line segment. Additionally,
line segment impedances can be computed by using line segment length and
associated per length impedances.

Unbalanced modeling of impedances is supported by the per length phase
impedance matrix (PerLengthPhaseImpedance) in conjunction with
phase-to-sequence number mapping supplied by either ACLineSegmentPhase
or WirePosition. The sequence numbers are referenced by the row and
column attributes of the per length phase impedance matrix. This method
enables single-phase and two-phase line segments, and transpositions of
phases, to be described using the same per length phase impedance
matrix. The length of the line segment is used in the computation of
total impedance values for the line segment.

**Line detail characteristics**

There are three approaches to providing line detail and all use
WireAssembly to supply line positions:

-   Option 1 - WireAssembly supplies only line positions.
    ACLineSegmentPhase points to wire type and intraphase spacing and
    supplies the phase-to-sequence number mapping.
-   Option 2 - WireAssembly supplies line position and, for each
    position, also supplies wire type and intraphase spacing.
    ACLineSegmentPhase supplies the phase-to-sequence number mapping.
-   Option 3 - WireAssembly supplies line position and, for each
    position, also supplies wire type and intraphase spacing and phase.
    WireAssembly therefore supplies the phase-to-sequence number mapping
    and ACLineSegmentPhase is not needed.

**Native Members**

  ------ ------ -------------------------- --------------------------
  b0ch   1..1   [Susce                     Zero sequence shunt
                ptance](#Susceptance)      (charging) susceptance,
                                           uniformly distributed, of
                                           the entire line segment.

  bch    1..1   [Susce                     Positive sequence shunt
                ptance](#Susceptance)      (charging) susceptance,
                                           uniformly distributed, of
                                           the entire line segment.
                                           This value represents the
                                           full charging over the
                                           full length of the line
                                           segment.

  r      1..1   [Res istance](#Resistance) Positive sequence series
                                           resistance of the entire
                                           line segment.

  r0     1..1   [Res istance](#Resistance) Zero sequence series
                                           resistance of the entire
                                           line segment.

  x      1..1   [R eactance](#Reactance)   Positive sequence series
                                           reactance of the entire
                                           line segment.

  x0     1..1   [R eactance](#Reactance)   Zero sequence series
                                           reactance of the entire
                                           line segment.
  ------ ------ -------------------------- --------------------------

**Inherited Members**

  -------- ------ ------------------- ------------------------------------
  length   1..1   [Length](#Length)   see [Conductor](#Conductor.length)
  -------- ------ ------------------- ------------------------------------

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#ACPointOfCommonCoupling .container .group}
[#ACPointOfCommonCoupling](#ACPointOfCommonCoupling)

**ACPointOfCommonCoupling**

Core

Point of interconnection of the DC converter station to the adjacent AC
system (IEC 60633).

**Native Members**

  ------------------ ------ ---------------------------------- -------------------
  ConnectivityNode   0..1   [Conne ctivityNode \<#Con          Connectivity node
                            nectivityNode\>]{.title-ref}\_\_   which is a point of
                                                               common coupling AC.

  ------------------ ------ ---------------------------------- -------------------

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [PointO fCommonCoupling \<#PointO
                                       fCommonCoupling.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [PointO fCommonCoupling \<#PointO
                                       fCommonCoupling.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#ApparentPowerLimit .container .group}
[#ApparentPowerLimit](#ApparentPowerLimit)

**ApparentPowerLimit**

OperationalLimits

Apparent power limit.

**Native Members**

  ------- ------ ------------------------- -------------------------
  value   0..1   [ApparentPo               The apparent power limit.
                 wer](#ApparentPower)      The attribute shall be a
                                           positive value or zero.

  ------- ------ ------------------------- -------------------------

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  mRID                1..1   [St ring](#String)                 see [Operationa lLimit \<#Operatio
                                                                nalLimit.mRID\>]{.title-ref}\_\_

  name                1..1   [St ring](#String)                 see [Operationa lLimit \<#Operatio
                                                                nalLimit.name\>]{.title-ref}\_\_

  Op                  0..1   [Operational LimitSet \<#Operat    see [Operatio nalLimit \<#Operat
  erationalLimitSet          ionalLimitSet\>]{.title-ref}\_\_   ionalLimit.Operat
                                                                ionalLimitSet\>]{.title-ref}\_\_

  Ope                 0..1   [OperationalLi mitType \<#Operati  see [Operation alLimit \<#Operati
  rationalLimitType          onalLimitType\>]{.title-ref}\_\_   onalLimit.Operati
                                                                onalLimitType\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#AsynchronousMachine .container .group}
[#AsynchronousMachine](#AsynchronousMachine)

**AsynchronousMachine**

Wires

A rotating machine whose shaft rotates asynchronously with the
electrical field. Also known as an induction machine with no external
connection to the rotor windings, e.g. squirrel-cage induction machine.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  asynch              0..1   [As ynchronousMachine Kind         Indicates the type
  ronousMachineType          \<#Asynchrono                      of Asynchronous
                             usMachineKind\>]{.title-ref}\_\_   Machine (motor or
                                                                generator).

  converterFedDrive   0..1   [Bool ean](#Boolean)               Indicates whether
                                                                the machine is a
                                                                converter fed
                                                                drive. Used for
                                                                short circuit data
                                                                exchange according
                                                                to IEC 60909.

  efficiency          0..1   [PerC ent](#PerCent)               Efficiency of the
                                                                asynchronous
                                                                machine at nominal
                                                                operation as a
                                                                percentage.
                                                                Indicator for
                                                                converter drive
                                                                motors. Used for
                                                                short circuit data
                                                                exchange according
                                                                to IEC 60909.

  iaIrRatio           0..1   [Float](#Float)                    Ratio of
                                                                locked-rotor
                                                                current to the
                                                                rated current of
                                                                the motor (Ia/Ir).
                                                                Used for short
                                                                circuit data
                                                                exchange according
                                                                to IEC 60909.

  nominalFrequency    0..1   [Frequenc y](#Frequency)           Nameplate data
                                                                indicates if the
                                                                machine is 50 Hz or
                                                                60 Hz.

  nominalSpeed        0..1   [RotationSpeed \<#                 Nameplate data.
                             RotationSpeed\>]{.title-ref}\_\_   Depends on the slip
                                                                and number of pole
                                                                pairs.

  polePairNumber      0..1   [Inte ger](#Integer)               Number of pole
                                                                pairs of stator.
                                                                Used for short
                                                                circuit data
                                                                exchange according
                                                                to IEC 60909.

  rat                 0..1   [ActivePower](#ActivePower)        Rated mechanical
  edMechanicalPower                                             power (Pr in IEC
                                                                60909-0). Used for
                                                                short circuit data
                                                                exchange according
                                                                to IEC 60909.

  reversible          0..1   [Bool ean](#Boolean)               Indicates for
                                                                converter drive
                                                                motors if the power
                                                                can be reversible.
                                                                Used for short
                                                                circuit data
                                                                exchange according
                                                                to IEC 60909.

  rr1                 0..1   [Resistance](#Resistance)          Damper 1 winding
                                                                resistance.

  rr2                 0..1   [Resistance](#Resistance)          Damper 2 winding
                                                                resistance.

  r xLockedRotorRatio 0..1   [Float](#Float)                    Locked rotor ratio
                                                                (R/X). Used for
                                                                short circuit data
                                                                exchange according
                                                                to IEC 60909.

  tpo                 0..1   [Seco nds](#Seconds)               Transient rotor
                                                                time constant
                                                                (greater than
                                                                tppo).

  tppo                0..1   [Seco nds](#Seconds)               Sub-transient rotor
                                                                time constant
                                                                (greater than 0).

  xlr1                0..1   [Reactanc e](#Reactance)           Damper 1 winding
                                                                leakage reactance.

  xlr2                0..1   [Reactanc e](#Reactance)           Damper 2 winding
                                                                leakage reactance.

  xm                  0..1   [Reactanc e](#Reactance)           Magnetizing
                                                                reactance.

  xp                  0..1   [Reactanc e](#Reactance)           Transient reactance
                                                                (unsaturated)
                                                                (greater than or
                                                                equal to xpp).

  xpp                 0..1   [Reactanc e](#Reactance)           Sub-transient
                                                                reactance
                                                                (unsaturated).

  xs                  0..1   [Reactanc e](#Reactance)           Synchronous
                                                                reactance (greater
                                                                than xp).
  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**

  ---------------- ------ ---------------------------------- ----------------------------------
  p                1..1   [ActivePower](#ActivePower)        see [Rotat ingMachine \<#Rota
                                                             tingMachine.p\>]{.title-ref}\_\_

  q                1..1   [ReactivePower \<#                 see [Rotat ingMachine \<#Rota
                          ReactivePower\>]{.title-ref}\_\_   tingMachine.q\>]{.title-ref}\_\_

  ratedS           1..1   [ApparentPower \<#                 see [RotatingMa chine \<#RotatingM
                          ApparentPower\>]{.title-ref}\_\_   achine.ratedS\>]{.title-ref}\_\_

  ratedU           1..1   [Volt age](#Voltage)               see [RotatingMa chine \<#RotatingM
                                                             achine.ratedU\>]{.title-ref}\_\_

  GeneratingUnit   1..1   [G eneratingUnit \<#G              see [R otatingMachine \<#
                          eneratingUnit\>]{.title-ref}\_\_   RotatingMachine.G
                                                             eneratingUnit\>]{.title-ref}\_\_
  ---------------- ------ ---------------------------------- ----------------------------------

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#AsynchronousMachineTimeConstantReactance .container .group}
[#AsynchronousMachineTimeConstantReactance](#AsynchronousMachineTimeConstantReactance)

**AsynchronousMachineTimeConstantReactance**

AsynchronousMachineDynamics

Parameter details:

1.  If *X\'\'* = *X\'*, a single cage (one equivalent rotor winding per
    axis) is modelled.
2.  The "*p*" in the attribute names is a substitution for a "prime" in
    the usual parameter notation, e.g. \*tpo\* refers to *T\'o*.

The parameters used for models expressed in time constant reactance form
include:

-   RotatingMachine.ratedS (*MVAbase*);
-   RotatingMachineDynamics.damping (*D*);
-   RotatingMachineDynamics.inertia (*H*);
-   RotatingMachineDynamics.saturationFactor (*S1*);
-   RotatingMachineDynamics.saturationFactor120 (*S12*);
-   RotatingMachineDynamics.statorLeakageReactance (*Xl*);
-   RotatingMachineDynamics.statorResistance (*Rs*);
-   .xs (*Xs*);
-   .xp (*X\'*);
-   .xpp (*X\'\'*);
-   .tpo (*T\'o*);
-   .tppo (*T\'\'o*).

**Native Members**

  ------ ------ ------------------------ --------------------------
  tpo    0..1   [Seconds](#Seconds)      Transient rotor time
                                         constant (*T\'o*) (\>
                                         AsynchronousMachineTime
                                         ConstantReactance.tppo).
                                         Typical value = 5.

  tppo   0..1   [Seconds](#Seconds)      Subtransient rotor time
                                         constant (*T\'\'o*) (\>
                                         0). Typical value = 0,03.

  xp     0..1   [PU](#PU)                Transient reactance
                                         (unsaturated) (*X\'*) (\>=
                                         AsynchronousMachineTim
                                         eConstantReactance.xpp).
                                         Typical value = 0,5.

  xpp    0..1   [PU](#PU)                Subtransient reactance
                                         (unsaturated) (*X\'\'*)
                                         (\>
                                         RotatingMachineDynamics.
                                         statorLeakageReactance).
                                         Typical value = 0,2.

  xs     0..1   [PU](#PU)                Synchronous reactance
                                         (*Xs*) (\>=
                                         AsynchronousMachineTi
                                         meConstantReactance.xp).
                                         Typical value = 1,8.
  ------ ------ ------------------------ --------------------------

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  As                  0..1   [Asynchronou sMachine \<#Asynch    see [AsynchronousM achineDynamics
  ynchronousMachine          ronousMachine\>]{.title-ref}\_\_   \<# AsynchronousMachi
                                                                neDynamics.Asynch
                                                                ronousMachine\>]{.title-ref}\_\_

  ------------------- ------ ---------------------------------- ----------------------------------

  ------------------- ------ ------------------- ----------------------------------
  damping             1..1   [Float](#Float)     see [RotatingMa chineDynamics \<#R
                                                 otatingMachineDyn
                                                 amics.damping\>]{.title-ref}\_\_

  inertia             1..1   [Seco               see [RotatingMa chineDynamics \<#R
                             nds](#Seconds)      otatingMachineDyn
                                                 amics.inertia\>]{.title-ref}\_\_

  stato               1..1   [PU](#PU)           see [Rotating MachineDynamics \<
  rLeakageReactance                              #RotatingMachineD
                                                 ynamics.statorLea
                                                 kageReactance\>]{.title-ref}\_\_

  statorResistance    1..1   [PU](#PU)           see [Ro tatingMachineDyna mics
                                                 \<#RotatingMa chineDynamics.sta
                                                 torResistance\>]{.title-ref}\_\_
  ------------------- ------ ------------------- ----------------------------------

  --------- ------ ------------------------ ---------------------------------------
  mRID      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.mRID\>]{.title-ref}\_\_

  enabled   1..1   [Boolean](#Boolean)      see [DynamicsFunct ionBlock
                                            \<#DynamicsFun
                                            ctionBlock.enabled\>]{.title-ref}\_\_

  name      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.name\>]{.title-ref}\_\_
  --------- ------ ------------------------ ---------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#BaseVoltage .container .group}
[#BaseVoltage](#BaseVoltage)

**BaseVoltage**

Core

Defines a system base voltage which is referenced. This may be different
than the rated voltage.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 1..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| name           | 1..1           | [S trin        | The name is    |
|                |                | g](#String)    | any free human |
|                |                |                | readable and   |
|                |                |                | possibly non   |
|                |                |                | unique text    |
|                |                |                | naming the     |
|                |                |                | object.        |
+----------------+----------------+----------------+----------------+
| nominalVoltage | 1..1           | [Vol           | The power      |
|                |                | t              | system         |
|                |                | age](#Voltage) | resource\'s    |
|                |                |                | base voltage,  |
|                |                |                | expressed on a |
|                |                |                | phase-to-phase |
|                |                |                | (line-to-line) |
|                |                |                | basis. Shall   |
|                |                |                | be a positive  |
|                |                |                | value and not  |
|                |                |                | zero.          |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#BatteryUnit .container .group}
[#BatteryUnit](#BatteryUnit)

**BatteryUnit**

Production

An electrochemical energy storage device.

**Native Members**

  -------------- ------ ------------------------------------- ----------------------
  batteryState   1..1   [BatteryStateKind \<#                 The current state of
                        BatteryStateKind\>]{.title-ref}\_\_   the battery (charging,
                                                              full, etc.).

  ratedE         1..1   [RealEne rgy](#RealEnergy)            Full energy storage
                                                              capacity of the
                                                              battery. The attribute
                                                              shall be a positive
                                                              value.

  storedE        1..1   [RealEne rgy](#RealEnergy)            Amount of energy
                                                              currently stored. The
                                                              attribute shall be a
                                                              positive value or zero
                                                              and lower than
                                                              BatteryUnit.ratedE.
  -------------- ------ ------------------------------------- ----------------------

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  maxP                1..1   [ActivePower](#ActivePower)        see [P owerElectronicsUn it
                                                                \<#PowerElectro
                                                                nicsUnit.maxP\>]{.title-ref}\_\_

  minP                1..1   [ActivePower](#ActivePower)        see [P owerElectronicsUn it
                                                                \<#PowerElectro
                                                                nicsUnit.minP\>]{.title-ref}\_\_

  PowerElec           1..1   [PowerEle ctronicsConnectio n      see [PowerE lectronicsUnit \<#
  tronicsConnection          \<#PowerElectron                   PowerElectronicsU
                             icsConnection\>]{.title-ref}\_\_   nit.PowerElectron
                                                                icsConnection\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#ConnectivityNode .container .group}
[#ConnectivityNode](#ConnectivityNode)

**ConnectivityNode**

Core

Connectivity nodes are points where terminals of AC conducting equipment
are connected together with zero impedance.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 1..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| name           | 1..1           | [S trin        | The name is    |
|                |                | g](#String)    | any free human |
|                |                |                | readable and   |
|                |                |                | possibly non   |
|                |                |                | unique text    |
|                |                |                | naming the     |
|                |                |                | object.        |
+----------------+----------------+----------------+----------------+
| Connectivi t   | 1..1           | [Connectiv i   | Container of   |
| yNodeContainer |                | tyNodeContaine | this           |
|                |                | r \<#Conn      | connectivity   |
|                |                | ectivit%20yNod | node.          |
|                |                | e              |                |
|                |                | Container\>]{. |                |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+
| T              | 0..1           | [Topo logicalN | The            |
| opologicalNode |                | ode            | topological    |
|                |                | \<#T%20opol    | node to which  |
|                |                | o              | this           |
|                |                | gicalNode\>]{. | connectivity   |
|                |                | title-ref}\_\_ | node is        |
|                |                |                | assigned. May  |
|                |                |                | depend on the  |
|                |                |                | current state  |
|                |                |                | of switches in |
|                |                |                | the network.   |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#CsConverter .container .group}
[#CsConverter](#CsConverter)

**CsConverter**

DC

DC side of the current source converter (CSC).

The firing angle controls the dc voltage at the converter, both for
rectifier and inverter. The difference between the dc voltages of the
rectifier and inverter determines the dc current. The extinction angle
is used to limit the dc voltage at the inverter, if needed, and is not
used in active power control. The firing angle, transformer tap position
and number of connected filters are the primary means to control a
current source dc line. Higher level controls are built on top, e.g. DC
voltage, dc current and active power. From a steady state perspective it
is sufficient to specify the desired active power transfer
(ACDCConverter.targetPpcc) and the control functions will set the dc
voltage, dc current, firing angle, transformer tap position and number
of connected filters to meet this. Therefore attributes targetAlpha and
targetGamma are not applicable in this case.

Attributes targetAlpha and targetGamma are mutually exclusive therefore
only one of them can be defined to describe an operating target.

The reactive power consumed by the converter is a function of the firing
angle, transformer tap position and number of connected filter, which
can be approximated with half of the active power. The losses are a
function of the dc voltage and dc current.

The attributes minAlpha and maxAlpha define the range of firing angles
for rectifier operation between which no discrete tap changer action
takes place. The range is typically 10 to 18 degrees.

The attributes minGamma and maxGamma define the range of extinction
angles for inverter operation between which no discrete tap changer
action takes place. The range is typically 17 to 20 degrees.

**Native Members**

  --------------- ------ ------------------------------------ ----------------------
  alpha           0..1   [AngleDegrees](#AngleDegrees)        Firing angle that
                                                              determines the DC
                                                              voltage at the
                                                              converter DC terminal.
                                                              Typical value between
                                                              10 degrees and 18
                                                              degrees for a
                                                              rectifier. It is
                                                              converter\'s state
                                                              variable, result from
                                                              power flow. The
                                                              attribute shall be a
                                                              positive value.

  gamma           0..1   [AngleDegrees](#AngleDegrees)        Extinction angle. It
                                                              is used to limit the
                                                              DC voltage at the
                                                              inverter if needed.
                                                              Typical value between
                                                              17 degrees and 20
                                                              degrees for an
                                                              inverter. It is
                                                              converter\'s state
                                                              variable, result from
                                                              power flow. The
                                                              attribute shall be a
                                                              positive value.

  maxAlpha        0..1   [AngleDegrees](#AngleDegrees)        Maximum firing angle.
                                                              It is the converter\'s
                                                              configuration data
                                                              used in power flow.
                                                              The attribute shall be
                                                              a positive value.

  maxGamma        0..1   [AngleDegrees](#AngleDegrees)        Maximum extinction
                                                              angle. It is the
                                                              converter\'s
                                                              configuration data
                                                              used in power flow.
                                                              The attribute shall be
                                                              a positive value.

  maxIdc          0..1   [CurrentFlo w](#CurrentFlow)         The maximum direct
                                                              current (Id) on the DC
                                                              side at which the
                                                              converter should
                                                              operate. It is the
                                                              converter\'s
                                                              configuration data use
                                                              in power flow. The
                                                              attribute shall be a
                                                              positive value.

  minAlpha        0..1   [AngleDegrees](#AngleDegrees)        Minimum firing angle.
                                                              It is the converter\'s
                                                              configuration data
                                                              used in power flow.
                                                              The attribute shall be
                                                              a positive value.

  minGamma        0..1   [AngleDegrees](#AngleDegrees)        Minimum extinction
                                                              angle. It is the
                                                              converter\'s
                                                              configuration data
                                                              used in power flow.
                                                              The attribute shall be
                                                              a positive value.

  minIdc          0..1   [CurrentFlo w](#CurrentFlow)         The minimum direct
                                                              current (Id) on the DC
                                                              side at which the
                                                              converter should
                                                              operate. It is the
                                                              converter\'s
                                                              configuration data
                                                              used in power flow.
                                                              The attribute shall be
                                                              a positive value.

  operatingMode   0..1   [CsOpera tingModeKind \<#CsOp        Indicates whether the
                         eratingModeKind\>]{.title-ref}\_\_   DC pole is operating
                                                              as an inverter or as a
                                                              rectifier. It is
                                                              converter\'s control
                                                              variable used in power
                                                              flow.

  pPccControl     0..1   [CsP pccControlKind \<#Cs            Kind of active power
                         PpccControlKind\>]{.title-ref}\_\_   control.

  ratedIdc        0..1   [CurrentFlo w](#CurrentFlow)         Rated converter DC
                                                              current, also called
                                                              IdN. The attribute
                                                              shall be a positive
                                                              value. It is the
                                                              converter\'s
                                                              configuration data
                                                              used in power flow.

  targetAlpha     0..1   [AngleDegrees](#AngleDegrees)        Target firing angle.
                                                              It is converter\'s
                                                              control variable used
                                                              in power flow. It is
                                                              only applicable for
                                                              rectifier control.
                                                              Allowed values are
                                                              within the range
                                                              minAlpha\<=tar
                                                              getAlpha\<=maxAlpha.
                                                              The attribute shall be
                                                              a positive value.

  targetGamma     0..1   [AngleDegrees](#AngleDegrees)        Target extinction
                                                              angle. It is
                                                              converter\'s control
                                                              variable used in power
                                                              flow. It is only
                                                              applicable for
                                                              inverter control.
                                                              Allowed values are
                                                              within the range
                                                              minGamma\<=tar
                                                              getGamma\<=maxGamma.
                                                              The attribute shall be
                                                              a positive value.

  targetIdc       0..1   [CurrentFlo w](#CurrentFlow)         DC current target
                                                              value. It is
                                                              converter\'s control
                                                              variable used in power
                                                              flow. The attribute
                                                              shall be a positive
                                                              value.
  --------------- ------ ------------------------------------ ----------------------

**Inherited Members**

  ---------------- ------ ---------------------------------- ----------------------------------
  baseS            0..1   [ApparentPower \<#                 see [ACDCC onverter \<#ACDCCo
                          ApparentPower\>]{.title-ref}\_\_   nverter.baseS\>]{.title-ref}\_\_

  idc              0..1   [CurrentFlow](#CurrentFlow)        see [ACD CConverter \<#ACDC
                                                             Converter.idc\>]{.title-ref}\_\_

  idleLoss         0..1   [ActivePower](#ActivePower)        see [ACDCConv erter \<#ACDCConve
                                                             rter.idleLoss\>]{.title-ref}\_\_

  maxP             0..1   [ActivePower](#ActivePower)        see [ACDC Converter \<#ACDCC
                                                             onverter.maxP\>]{.title-ref}\_\_

  maxUdc           0..1   [Volt age](#Voltage)               see [ACDCCo nverter \<#ACDCCon
                                                             verter.maxUdc\>]{.title-ref}\_\_

  minP             0..1   [ActivePower](#ActivePower)        see [ACDC Converter \<#ACDCC
                                                             onverter.minP\>]{.title-ref}\_\_

  minUdc           0..1   [Volt age](#Voltage)               see [ACDCCo nverter \<#ACDCCon
                                                             verter.minUdc\>]{.title-ref}\_\_

  numberOfValves   0..1   [Inte ger](#Integer)               see [ACDCConverter
                                                             \<#ACDCConverter.n
                                                             umberOfValves\>]{.title-ref}\_\_

  p                0..1   [ActivePower](#ActivePower)        see [A CDCConverter \<#AC
                                                             DCConverter.p\>]{.title-ref}\_\_

  poleLossP        0..1   [ActivePower](#ActivePower)        see [ACDCConve rter \<#ACDCConver
                                                             ter.poleLossP\>]{.title-ref}\_\_

  q                0..1   [ReactivePower \<#                 see [A CDCConverter \<#AC
                          ReactivePower\>]{.title-ref}\_\_   DCConverter.q\>]{.title-ref}\_\_

  ratedUdc         0..1   [Volt age](#Voltage)               see [ACDCConv erter \<#ACDCConve
                                                             rter.ratedUdc\>]{.title-ref}\_\_

  resistiveLoss    0..1   [Resistance](#Resistance)          see [ACDCConverter
                                                             \<#ACDCConverter.
                                                             resistiveLoss\>]{.title-ref}\_\_

  switchingLoss    0..1   [Active PowerPerCurrentFl ow       see [ACDCConverter
                          \<#ActivePowerP                    \<#ACDCConverter.
                          erCurrentFlow\>]{.title-ref}\_\_   switchingLoss\>]{.title-ref}\_\_

  targetPpcc       0..1   [ActivePower](#ActivePower)        see [ACDCConver ter \<#ACDCConvert
                                                             er.targetPpcc\>]{.title-ref}\_\_

  targetUdc        0..1   [Volt age](#Voltage)               see [ACDCConve rter \<#ACDCConver
                                                             ter.targetUdc\>]{.title-ref}\_\_

  uc               0..1   [Volt age](#Voltage)               see [AC DCConverter \<#ACD
                                                             CConverter.uc\>]{.title-ref}\_\_

  udc              0..1   [Volt age](#Voltage)               see [ACD CConverter \<#ACDC
                                                             Converter.udc\>]{.title-ref}\_\_

  valveU0          0..1   [Volt age](#Voltage)               see [ACDCCon verter \<#ACDCConv
                                                             erter.valveU0\>]{.title-ref}\_\_
  ---------------- ------ ---------------------------------- ----------------------------------

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#CurveData .container .group}
[#CurveData](#CurveData)

**CurveData**

Core

Multi-purpose data points for defining a curve. The use of this generic
class is discouraged if a more specific class can be used to specify the
X and Y axis values along with their specific data types.

**Native Members**

  --------- ------ -------------------- ------------------------
  xvalue    1..1   [Float](#Float)      The data value of the
                                        X-axis variable,
                                        depending on the X-axis
                                        units.

  y1value   1..1   [Float](#Float)      The data value of the
                                        first Y-axis variable,
                                        depending on the Y-axis
                                        units.

  Curve     1..1   [Curve](#Curve)      The curve of this curve
                                        data point.
  --------- ------ -------------------- ------------------------
:::

::: {#DCBreaker .container .group}
[#DCBreaker](#DCBreaker)

**DCBreaker**

DC

A breaker within a DC system.

**Inherited Members**

  ------------ ------ ----------------------- --------------------------------------
  locked       0..1   [Boolean](#Boolean)     see [DCSwitch](#DCSwitch.locked)

  normalOpen   0..1   [Boolean](#Boolean)     see [DCSwitch \<#DC
                                              Switch.normalOpen\>]{.title-ref}\_\_

  open         0..1   [Boolean](#Boolean)     see [DCSwitc h](#DCSwitch.open)

  retained     0..1   [Boolean](#Boolean)     see [DCSwitch \<#
                                              DCSwitch.retained\>]{.title-ref}\_\_
  ------------ ------ ----------------------- --------------------------------------

  -------------- ------ ---------------------- -------------------------------------
  ratedCurrent   0..1   [CurrentFl             see [DC ConductingEquipment
                        ow](#CurrentFlow)      \<#DCConductingEquipm
                                               ent.ratedCurrent\>]{.title-ref}\_\_

  ratedUdc       0..1   [V oltage](#Voltage)   see [DCConductingEquipm ent
                                               \<#DCConductingEq
                                               uipment.ratedUdc\>]{.title-ref}\_\_
  -------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DCDisconnector .container .group}
[#DCDisconnector](#DCDisconnector)

**DCDisconnector**

DC

A disconnector within a DC system.

**Inherited Members**

  ------------ ------ ----------------------- --------------------------------------
  locked       0..1   [Boolean](#Boolean)     see [DCSwitch](#DCSwitch.locked)

  normalOpen   0..1   [Boolean](#Boolean)     see [DCSwitch \<#DC
                                              Switch.normalOpen\>]{.title-ref}\_\_

  open         0..1   [Boolean](#Boolean)     see [DCSwitc h](#DCSwitch.open)

  retained     0..1   [Boolean](#Boolean)     see [DCSwitch \<#
                                              DCSwitch.retained\>]{.title-ref}\_\_
  ------------ ------ ----------------------- --------------------------------------

  -------------- ------ ---------------------- -------------------------------------
  ratedCurrent   0..1   [CurrentFl             see [DC ConductingEquipment
                        ow](#CurrentFlow)      \<#DCConductingEquipm
                                               ent.ratedCurrent\>]{.title-ref}\_\_

  ratedUdc       0..1   [V oltage](#Voltage)   see [DCConductingEquipm ent
                                               \<#DCConductingEq
                                               uipment.ratedUdc\>]{.title-ref}\_\_
  -------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DCEnergySource .container .group}
[#DCEnergySource](#DCEnergySource)

**DCEnergySource**

Emtiop

A source of DC power that is independent of the AC system, e.g., a
battery or solar panel. The internal representation may include current
sources, voltage sources, diodes, etc. Use DCSourceKind to provide
guidance on the internal representation.

**Native Members**

  ---------- ------ ------------------------ ------------------------
  kind       0..1   [DCSourceK               
                    ind](#DCSourceKind)      

  p          0..1   [ActiveP                 The power output,
                    ower](#ActivePower)      negative for load or
                                             charging.

  pMax       0..1   [ActiveP                 Maximum power available
                    ower](#ActivePower)      from the primary source,
                                             e.g., photovoltaic
                                             panels or a battery.

  pMaxLoad   0..1   [ActiveP                 Maximum load or battery
                    ower](#ActivePower)      charging power.

  pMin       0..1   [ActiveP                 Minimum power available
                    ower](#ActivePower)      from the supply.

  pMinLoad   0..1   [ActiveP                 Minimum load or battery
                    ower](#ActivePower)      charging power.

  rSeries    0..1   [Resis                   Series source
                    tance](#Resistance)      resistance.

  rShunt     0..1   [Resis                   Shunt source resistance.
                    tance](#Resistance)      
  ---------- ------ ------------------------ ------------------------

**Inherited Members**

  -------------- ------ ---------------------- -------------------------------------
  ratedCurrent   0..1   [CurrentFl             see [DC ConductingEquipment
                        ow](#CurrentFlow)      \<#DCConductingEquipm
                                               ent.ratedCurrent\>]{.title-ref}\_\_

  ratedUdc       0..1   [V oltage](#Voltage)   see [DCConductingEquipm ent
                                               \<#DCConductingEq
                                               uipment.ratedUdc\>]{.title-ref}\_\_
  -------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DCEquipmentContainer .container .group}
[#DCEquipmentContainer](#DCEquipmentContainer)

**DCEquipmentContainer**

DC

A modelling construct to provide a root class for containment of DC as
well as AC equipment. The class differ from the EquipmentContainer for
AC in that it may also contain DCNode(-s). Hence it can contain both AC
and DC equipment.

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DCGround .container .group}
[#DCGround](#DCGround)

**DCGround**

DC

A ground within a DC system.

**Native Members**

  ------------ ------ --------------------------- -----------------------
  inductance   0..1   [Inductance](#Inductance)   Inductance to ground.
  r            0..1   [Resistance](#Resistance)   Resistance to ground.
  ------------ ------ --------------------------- -----------------------

**Inherited Members**

  -------------- ------ ---------------------- -------------------------------------
  ratedCurrent   0..1   [CurrentFl             see [DC ConductingEquipment
                        ow](#CurrentFlow)      \<#DCConductingEquipm
                                               ent.ratedCurrent\>]{.title-ref}\_\_

  ratedUdc       0..1   [V oltage](#Voltage)   see [DCConductingEquipm ent
                                               \<#DCConductingEq
                                               uipment.ratedUdc\>]{.title-ref}\_\_
  -------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DCLineSegment .container .group}
[#DCLineSegment](#DCLineSegment)

**DCLineSegment**

DC

A wire or combination of wires not insulated from one another, with
consistent electrical characteristics, used to carry direct current
between points in the DC region of the power system.

**Native Members**

  ------------- ------ ---------------------- ----------------------
  capacitance   0..1   [Capacitan             Capacitance of the DC
                       ce](#Capacitance)      line segment.
                                              Significant for cables
                                              only.

  inductance    0..1   [Inducta               Inductance of the DC
                       nce](#Inductance)      line segment.
                                              Negligible compared
                                              with DCSeriesDevice
                                              used for smoothing.

  length        0..1   [Length](#Length)      Segment length for
                                              calculating line
                                              section capabilities.

  resistance    0..1   [Resista               Resistance of the DC
                       nce](#Resistance)      line segment.
  ------------- ------ ---------------------- ----------------------

**Inherited Members**

  -------------- ------ ---------------------- -------------------------------------
  ratedCurrent   0..1   [CurrentFl             see [DC ConductingEquipment
                        ow](#CurrentFlow)      \<#DCConductingEquipm
                                               ent.ratedCurrent\>]{.title-ref}\_\_

  ratedUdc       0..1   [V oltage](#Voltage)   see [DCConductingEquipm ent
                                               \<#DCConductingEq
                                               uipment.ratedUdc\>]{.title-ref}\_\_
  -------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DCNode .container .group}
[#DCNode](#DCNode)

**DCNode**

DC

DC nodes are points where terminals of DC conducting equipment are
connected together with zero impedance.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 1..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| name           | 1..1           | [S trin        | The name is    |
|                |                | g](#String)    | any free human |
|                |                |                | readable and   |
|                |                |                | possibly non   |
|                |                |                | unique text    |
|                |                |                | naming the     |
|                |                |                | object.        |
+----------------+----------------+----------------+----------------+
| DCEqu i        | 0..1           | [              | The DC         |
| pmentContainer |                | DCEquipmentCon | container for  |
|                |                | tainer \<      | the DC nodes.  |
|                |                | #DCEqui%20pmen |                |
|                |                | t              |                |
|                |                | Container\>]{. |                |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+
| DC T           | 0..1           | [DCTopolo      | The DC         |
| opologicalNode |                | gicalNod e     | topological    |
|                |                | \<#DCT%20opol  | node to which  |
|                |                | o              | this DC        |
|                |                | gicalNode\>]{. | connectivity   |
|                |                | title-ref}\_\_ | node is        |
|                |                |                | assigned. May  |
|                |                |                | depend on the  |
|                |                |                | current state  |
|                |                |                | of switches in |
|                |                |                | the network.   |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DCSeriesDevice .container .group}
[#DCSeriesDevice](#DCSeriesDevice)

**DCSeriesDevice**

DC

A series device within the DC system, typically a reactor used for
filtering or smoothing. Needed for transient and short circuit studies.

**Native Members**

  ------------ ------ --------------------------- --------------------------
  inductance   0..1   [Inductance](#Inductance)   Inductance of the device.

  resistance   0..1   [Resistance](#Resistance)   Resistance of the DC
                                                  device.
  ------------ ------ --------------------------- --------------------------

**Inherited Members**

  -------------- ------ ---------------------- -------------------------------------
  ratedCurrent   0..1   [CurrentFl             see [DC ConductingEquipment
                        ow](#CurrentFlow)      \<#DCConductingEquipm
                                               ent.ratedCurrent\>]{.title-ref}\_\_

  ratedUdc       0..1   [V oltage](#Voltage)   see [DCConductingEquipm ent
                                               \<#DCConductingEq
                                               uipment.ratedUdc\>]{.title-ref}\_\_
  -------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DCShunt .container .group}
[#DCShunt](#DCShunt)

**DCShunt**

DC

A shunt device within the DC system, typically used for filtering.
Needed for transient and short circuit studies.

**Native Members**

  ------------- ------ ---------------------- ----------------------
  capacitance   0..1   [Capacitan             Capacitance of the DC
                       ce](#Capacitance)      shunt.

  resistance    0..1   [Resista               Resistance of the DC
                       nce](#Resistance)      device.
  ------------- ------ ---------------------- ----------------------

**Inherited Members**

  -------------- ------ ---------------------- -------------------------------------
  ratedCurrent   0..1   [CurrentFl             see [DC ConductingEquipment
                        ow](#CurrentFlow)      \<#DCConductingEquipm
                                               ent.ratedCurrent\>]{.title-ref}\_\_

  ratedUdc       0..1   [V oltage](#Voltage)   see [DCConductingEquipm ent
                                               \<#DCConductingEq
                                               uipment.ratedUdc\>]{.title-ref}\_\_
  -------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DCTerminal .container .group}
[#DCTerminal](#DCTerminal)

**DCTerminal**

DC

An electrical connection point to generic DC conducting equipment.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  polarity            0..1   [ DCTerminalPolarit yKind          Represents the
                             \<#DCTermina                       normal network
                             lPolarityKind\>]{.title-ref}\_\_   polarity condition.
                                                                Used in DC system
                                                                configurations that
                                                                have explicit
                                                                polarity of the
                                                                terminals, e.g.,
                                                                voltage source
                                                                converter (VSC)
                                                                technology.

  DCCo                0..1   [DCConductingEqu ipment            An DC terminal
  nductingEquipment          \<#DCConduc                        belong to a DC
                             tingEquipment\>]{.title-ref}\_\_   conducting
                                                                equipment.
  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**

  -------- ------ ---------------------- ----------------------------------------
  DCNode   1..1   [DCNode](#DCNode)      see [DCBaseTerminal \<#DC
                                         BaseTerminal.DCNode\>]{.title-ref}\_\_

  -------- ------ ---------------------- ----------------------------------------

  ---------------- ------ ------------------- ----------------------------------
  sequenceNumber   1..1   [Inte               see [ACDCTerminal
                          ger](#Integer)      \<#ACDCTerminal.s
                                              equenceNumber\>]{.title-ref}\_\_

  ---------------- ------ ------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DCTopologicalNode .container .group}
[#DCTopologicalNode](#DCTopologicalNode)

**DCTopologicalNode**

DC

DC bus.

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DetailedModelDynamics .container .group}
[#DetailedModelDynamics](#DetailedModelDynamics)

**DetailedModelDynamics**

DetailedModelDescription

The main class that packages all related to this detailed model. This
includes all parameters, functions, signals, etc.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  Detailed            0..1   [Detail edModelTypeDynami cs       The type of
  ModelTypeDynamics          \<#DetailedMode                    detailed model
                             lTypeDynamics\>]{.title-ref}\_\_   dynamics that is
                                                                applied to the
                                                                detailed model
                                                                dynamics.

  Dyna                0..1   [DynamicsFunctio nBlock            The dynamics
  micsFunctionBlock          \<#Dynamics                        function block for
                             FunctionBlock\>]{.title-ref}\_\_   this detailed model
                                                                dynamics.

  Equipment           0..1   [Equipmen t](#Equipment)           The equipment which
                                                                behaviour this
                                                                detailed model
                                                                dynamics
                                                                represents.
  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**

  --------- ------ ------------------------ ---------------------------------------
  mRID      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.mRID\>]{.title-ref}\_\_

  enabled   1..1   [Boolean](#Boolean)      see [DynamicsFunct ionBlock
                                            \<#DynamicsFun
                                            ctionBlock.enabled\>]{.title-ref}\_\_

  name      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.name\>]{.title-ref}\_\_
  --------- ------ ------------------------ ---------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DiagramObjectPoint .container .group}
[#DiagramObjectPoint](#DiagramObjectPoint)

**DiagramObjectPoint**

DiagramLayout

A point in a given space defined by 3 coordinates and associated to a
diagram object. The coordinates may be positive or negative as the
origin does not have to be in the corner of a diagram.

**Native Members**

  ---------------- ------ ---------------------------------- -------------------
  sequenceNumber   1..1   [Inte ger](#Integer)               The sequence
                                                             position of the
                                                             point, used for
                                                             defining the order
                                                             of points for
                                                             diagram objects
                                                             acting as a
                                                             polyline or polygon
                                                             with more than one
                                                             point. The
                                                             attribute shall be
                                                             a positive value.

  xPosition        1..1   [Float](#Float)                    The X coordinate of
                                                             this point.

  yPosition        1..1   [Float](#Float)                    The Y coordinate of
                                                             this point.

  DiagramObject    1..1   [DiagramObject \<#                 The diagram object
                          DiagramObject\>]{.title-ref}\_\_   with which the
                                                             points are
                                                             associated.
  ---------------- ------ ---------------------------------- -------------------
:::

::: {#DisconnectingCircuitBreaker .container .group}
[#DisconnectingCircuitBreaker](#DisconnectingCircuitBreaker)

**DisconnectingCircuitBreaker**

Wires

A circuit breaking device including disconnecting function, eliminating
the need for separate disconnectors.

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#EnergyConsumer .container .group}
[#EnergyConsumer](#EnergyConsumer)

**EnergyConsumer**

Wires

Generic user of energy - a point of consumption on the power system
model.

EnergyConsumer.pfixed, .qfixed, .pfixedPct and .qfixedPct have meaning
only if there is no LoadResponseCharacteristic associated with
EnergyConsumer or if LoadResponseCharacteristic.exponentModel is set to
False.

**Native Members**

+----------------+----------------+----------------+----------------+
| p              | 1..1           | [A ctivePower  | Active power   |
|                |                | \<#A           | of the load.   |
|                |                | c              | Load sign      |
|                |                | tivePower\>]{. | convention is  |
|                |                | title-ref}\_\_ | used, i.e.     |
|                |                |                | positive sign  |
|                |                |                | means flow out |
|                |                |                | from a node.   |
|                |                |                |                |
|                |                |                | For voltage    |
|                |                |                | dependent      |
|                |                |                | loads the      |
|                |                |                | value is at    |
|                |                |                | rated voltage. |
|                |                |                |                |
|                |                |                | Starting value |
|                |                |                | for a steady   |
|                |                |                | state          |
|                |                |                | solution.      |
+----------------+----------------+----------------+----------------+
| q              | 1..1           | [React         | Reactive power |
|                |                | ivePower       | of the load.   |
|                |                | \<#Rea         | Load sign      |
|                |                | c              | convention is  |
|                |                | tivePower\>]{. | used, i.e.     |
|                |                | title-ref}\_\_ | positive sign  |
|                |                |                | means flow out |
|                |                |                | from a node.   |
|                |                |                |                |
|                |                |                | For voltage    |
|                |                |                | dependent      |
|                |                |                | loads the      |
|                |                |                | value is at    |
|                |                |                | rated voltage. |
|                |                |                |                |
|                |                |                | Starting value |
|                |                |                | for a steady   |
|                |                |                | state          |
|                |                |                | solution.      |
+----------------+----------------+----------------+----------------+
| LoadResponse   | 1..1           | [LoadRespons   | The load       |
|                |                | eCharacte      | response       |
|                |                | ristic         | characteristic |
|                |                | \<#LoadR       | of this load.  |
|                |                | esponse%20Char | If missing,    |
|                |                | a              | this load is   |
|                |                | cteristic\>]{. | assumed to be  |
|                |                | title-ref}\_\_ | constant       |
|                |                |                | power.         |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#EnergySource .container .group}
[#EnergySource](#EnergySource)

**EnergySource**

Wires

A generic equivalent for an energy supplier on a transmission or
distribution voltage level.

**Native Members**

  ------------------ ------ ---------------------------------- -------------------
  nominalVoltage     1..1   [Volt age](#Voltage)               Phase-to-phase
                                                               nominal voltage.

  r                  1..1   [Resistance](#Resistance)          Positive sequence
                                                               Thevenin
                                                               resistance.

  r0                 1..1   [Resistance](#Resistance)          Zero sequence
                                                               Thevenin
                                                               resistance.

  voltageAngle       1..1   [AngleRadians \<                   Phase angle of
                            #AngleRadians\>]{.title-ref}\_\_   a-phase open
                                                               circuit used when
                                                               voltage
                                                               characteristics
                                                               need to be imposed
                                                               at the node
                                                               associated with the
                                                               terminal of the
                                                               energy source, such
                                                               as when voltages
                                                               and angles from the
                                                               transmission level
                                                               are used as input
                                                               to the distribution
                                                               network. The
                                                               attribute shall be
                                                               a positive value or
                                                               zero.

  voltageMagnitude   1..1   [Volt age](#Voltage)               Phase-to-phase open
                                                               circuit voltage
                                                               magnitude used when
                                                               voltage
                                                               characteristics
                                                               need to be imposed
                                                               at the node
                                                               associated with the
                                                               terminal of the
                                                               energy source, such
                                                               as when voltages
                                                               and angles from the
                                                               transmission level
                                                               are used as input
                                                               to the distribution
                                                               network. The
                                                               attribute shall be
                                                               a positive value or
                                                               zero.

  x                  1..1   [Reactanc e](#Reactance)           Positive sequence
                                                               Thevenin reactance.

  x0                 1..1   [Reactanc e](#Reactance)           Zero sequence
                                                               Thevenin reactance.
  ------------------ ------ ---------------------------------- -------------------

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#EquipmentContainer .container .group}
[#EquipmentContainer](#EquipmentContainer)

**EquipmentContainer**

Core

A modelling construct to provide a root class for containing equipment.

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#HydroGeneratingUnit .container .group}
[#HydroGeneratingUnit](#HydroGeneratingUnit)

**HydroGeneratingUnit**

Production

A generating unit whose prime mover is a hydraulic turbine (e.g.
Francis, Pelton, Kaplan).

**Inherited Members**

  --------------- ------ --------------------- ------------------------------------
  maxOperatingP   1..1   [ActivePowe           see [GeneratingU nit
                         r](#ActivePower)      \<#GeneratingUni
                                               t.maxOperatingP\>]{.title-ref}\_\_

  minOperatingP   1..1   [ActivePowe           see [GeneratingU nit
                         r](#ActivePower)      \<#GeneratingUni
                                               t.minOperatingP\>]{.title-ref}\_\_
  --------------- ------ --------------------- ------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#IBRPlant .container .group}
[#IBRPlant](#IBRPlant)

**IBRPlant**

Emtiop

An inverter-based resource (IBR) plant comprising a collection of
components, e.g., a PowerElectronicsConnection with associated controls
and GeneratingUnit, one or more PowerTransformers, one or more
DisconnectingCircuitBreakers, and one or more ACLineSegments. The
components may also include AC filter and DC bus modeling.

**Native Members**

  ------------------- ------ ------------------- -------------------
  dcLinkVoltage       0..1   [Volt               Voltage of the DC
                             age](#Voltage)      bus, used to scale
                                                 average source
                                                 models or to supply
                                                 switching models of
                                                 the converter.

  s witchingFrequency 0..1   [Frequenc           Pulse width
                             y](#Frequency)      modulation (PWM)
                                                 switching frequency
                                                 of the firing
                                                 pulses in a
                                                 switching model of
                                                 the converter.
  ------------------- ------ ------------------- -------------------

**Inherited Members**

  ---------------- -------------- ------------------------------- -------------------------------
  ACPointOf        0..1           [ACPointOfCo mmonCoupling \<    see [Connected Facility \<#Con
  CommonCoupling                  #ACPointOfComm                  nectedFacility .ACPointOfComm
                                  onCoupling\>]{.title-ref}\_\_   onCoupling\>]{.title-ref}\_\_

  Equipments       0..unbounded   [Equipment \<                   see [ConnectedF acility \<#Conn
                                  #Equipment\>]{.title-ref}\_\_   ectedFacility.
                                                                  Equipments\>]{.title-ref}\_\_
  ---------------- -------------- ------------------------------- -------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#IEEECigreAPI .container .group}
[#IEEECigreAPI](#IEEECigreAPI)

**IEEECigreAPI**

Emtiop

A dynamic link library (DLL) or other application programming interface
(API) for inverter-based resource (IBR) control and other control
applications, as defined in CIGRE Technical Brochure TB 958 and IEEE
Standards Association P3597. Attributes prefixed by **api** correspond
to members of the IEEE_Cigre_DLLInterface_Model_Info header file
structure that was documented in TB 958; they should be obtained and
verified using the API.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  apiDL               0..1   [St ring](#String)                 Codifies a
  LInterfaceVersion                                             four-number version
                                                                of the CIGRE TB 958
                                                                interface standard
                                                                supported by this
                                                                model, in string
                                                                format, as returned
                                                                from the API.

  apiEmtRmsMode       0..1   [IEEECigreAPIM odeKind \<#IEEECig  Identify whether
                             reAPIModeKind\>]{.title-ref}\_\_   the model runs in
                                                                EMT, RMS, or both
                                                                kinds of
                                                                simulation, as
                                                                returned from the
                                                                CIGRE TB 958 API.

  apiFixedS           0..1   [Seco nds](#Seconds)               Hard-coded
  tepBaseSampleTime                                             simulation time
                                                                step for this
                                                                model, as returned
                                                                from the CIGRE TB
                                                                958 API.

  apiModelName        0..1   [St ring](#String)                 The ModelName as
                                                                returned from the
                                                                CIGRE TB 958 API.
                                                                Not necessarily
                                                                equal to the
                                                                inherited Ident
                                                                ifiedObject.name.

  apiModelVersion     0..1   [St ring](#String)                 Version of this
                                                                model instance, as
                                                                returned from the
                                                                CIGRE TB 958 API.

  shareable           0..1   [Bool ean](#Boolean)               True if this DLL
                                                                can be loaded and
                                                                used by different
                                                                instances of
                                                                Equipment in the
                                                                same simulation.
                                                                This information is
                                                                not available from
                                                                the DLL API; it
                                                                must be determined
                                                                from careful review
                                                                of the DLL
                                                                documentation.

  snapshotUri         0..1   [St ring](#String)                 Location of the
                                                                optional snapshot
                                                                file for
                                                                initializing the
                                                                DLL from a saved
                                                                state. Either a
                                                                universal resource
                                                                identifier or n
                                                                etwork-accessible
                                                                filename. It is not
                                                                obtainable from the
                                                                DLL API.

  uri                 0..1   [St ring](#String)                 Location of the
                                                                DLL, e.g., a
                                                                universal resource
                                                                identifier or n
                                                                etwork-accessible
                                                                filename. It is not
                                                                obtainable from the
                                                                DLL API.

  IEEECigreAPIInfo    0..1   [IEEEC igreAPIInfo \<#IEE          Expanded set of
                             ECigreAPIInfo\>]{.title-ref}\_\_   attributes
                                                                available from the
                                                                CIGRE TB 958 API.
  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  Detailed            0..1   [Detail edModelTypeDynami cs       see [Detaile dModelDynamics \<#
  ModelTypeDynamics          \<#DetailedMode                    DetailedModelDyna
                             lTypeDynamics\>]{.title-ref}\_\_   mics.DetailedMode
                                                                lTypeDynamics\>]{.title-ref}\_\_

  Dyna                0..1   [DynamicsFunctio nBlock            see [Det ailedModelDynamic s
  micsFunctionBlock          \<#Dynamics                        \<#DetailedModel Dynamics.Dynamics
                             FunctionBlock\>]{.title-ref}\_\_   FunctionBlock\>]{.title-ref}\_\_

  Equipment           0..1   [Equipmen t](#Equipment)           see [Detailed ModelDynamics \<#D
                                                                etailedModelDynam
                                                                ics.Equipment\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  --------- ------ ------------------------ ---------------------------------------
  mRID      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.mRID\>]{.title-ref}\_\_

  enabled   1..1   [Boolean](#Boolean)      see [DynamicsFunct ionBlock
                                            \<#DynamicsFun
                                            ctionBlock.enabled\>]{.title-ref}\_\_

  name      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.name\>]{.title-ref}\_\_
  --------- ------ ------------------------ ---------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#IEEECigreAPIInfo .container .group}
[#IEEECigreAPIInfo](#IEEECigreAPIInfo)

**IEEECigreAPIInfo**

Emtiop

Supplemental information about this interface from the CIGRE TB 958 API.

**Native Members**

  ------------------- ------- ---------------------------------- -------------------
  apiG                0..1    [St ring](#String)                 One of two general
  eneralInformation                                              description fields;
                                                                 also see the ap
                                                                 iModelDescription
                                                                 attribute.

  apiModelCreated     0..1    [DateTi me](#DateTime)             Date and time of
                                                                 the first model
                                                                 (not API) version.

  apiModelCreator     0..1    [St ring](#String)                 Identifies the
                                                                 person or the
                                                                 organization who
                                                                 first created the
                                                                 model.

  ap                  0..1    [St ring](#String)                 One of two general
  iModelDescription                                              description fields;
                                                                 also see the apiG
                                                                 eneralDescription
                                                                 attribute.

  apiMo               0..1    [St ring](#String)                 Identifies the
  delLastModifiedBy                                              person or the
                                                                 organization who
                                                                 first created the
                                                                 model.

  apiMode             0..1    [DateTi me](#DateTime)             Date and time of
  lLastModifiedDate                                              the latest model
                                                                 version.

  apiMod              0..1    [St ring](#String)                 A description of
  elModifiedComment                                              the latest model
                                                                 update.

  apiMod              0..1    [St ring](#String)                 A history of model
  elModifiedHistory                                              updates; may be a
                                                                 change log or other
                                                                 multi-paragraph
                                                                 text.

  a piNumDoubleStates 0..1    [Inte ger](#Integer)               Size of internal
                                                                 double-precision
                                                                 array storage
                                                                 needed by the model
                                                                 instance for state
                                                                 variables. These
                                                                 are not represented
                                                                 in CIM, but the
                                                                 information could
                                                                 help identify
                                                                 different versions
                                                                 of this model. The
                                                                 EMT/RMS simulator
                                                                 manages this
                                                                 memory.

  apiNumFloatStates   0..1    [Inte ger](#Integer)               Size of internal
                                                                 single-precision
                                                                 array storage
                                                                 needed by this
                                                                 model for state
                                                                 variables. These
                                                                 are not represented
                                                                 in CIM, but the
                                                                 information could
                                                                 help identify
                                                                 different versions
                                                                 of this model. The
                                                                 EMT/RMS simulator
                                                                 manages this
                                                                 memory.

  apiNumInputPorts    0..1    [Inte ger](#Integer)               The number of input
                                                                 ports expected by
                                                                 this model, which
                                                                 should match
                                                                 cardinality of the
                                                                 associated
                                                                 IEEECigreAPI -\>
                                                                 IEEECigr
                                                                 eAPIInputSignals.

  apiNumIntStates     0..1    [Inte ger](#Integer)               Size of internal
                                                                 integer array
                                                                 storage needed by
                                                                 this model for
                                                                 state variables.
                                                                 These are not
                                                                 represented in CIM,
                                                                 but the information
                                                                 could help identify
                                                                 different versions
                                                                 of this model. The
                                                                 EMT/RMS simulator
                                                                 manages this
                                                                 memory.

  apiNumOutputPorts   0..1    [Inte ger](#Integer)               The number of
                                                                 output ports
                                                                 expected by this
                                                                 model, which should
                                                                 match cardinality
                                                                 of the associated
                                                                 IEEECigreAPI -\>
                                                                 IEEECigre
                                                                 APIOutputSignals.

  apiNumParameters    0..1    [Inte ger](#Integer)               The number of input
                                                                 parameters expected
                                                                 by this model,
                                                                 which should match
                                                                 cardinality of the
                                                                 associated
                                                                 IEEECigreAPI -\>
                                                                 IEEECi
                                                                 greAPIParameters.

  IEEECigreAPIs       0..\*   [IEEECigreAPI \<                   Minimum set of
                              #IEEECigreAPI\>]{.title-ref}\_\_   attributes required
                                                                 to use this model.
  ------------------- ------- ---------------------------------- -------------------
:::

::: {#IEEECigreAPIInput .container .group}
[#IEEECigreAPIInput](#IEEECigreAPIInput)

**IEEECigreAPIInput**

Emtiop

Connects the set of CIGRE TB 958 API input signals, for this instance,
to points in the network model or to external references, like other
controllers.

**Native Members**

  ------------- ------ ------------------------------------- ----------------------
  kind          0..1   [IEEECigre APIInputKind \<#IEEEC      The type of input
                       igreAPIInputKind\>]{.title-ref}\_\_   signal. If
                                                             remoteInputSignal,
                                                             supply the
                                                             RemoteInputSignal
                                                             association. The phase
                                                             attribute is required
                                                             for acTerminalVoltage,
                                                             acCurrentVsc, and
                                                             acCurrentGrid. If
                                                             apiDefined, the model
                                                             must be queried
                                                             through its API for
                                                             more information.

  sensorRatio   0..1   [Float](#Float)                       Ratio between measured
                                                             quantity on the power
                                                             network and signal
                                                             quantity in the
                                                             control system, e.g.,
                                                             a current transformer
                                                             (CT) or voltage
                                                             transformer (VT)
                                                             ratio. Should be
                                                             greater than or equal
                                                             to 1.
  ------------- ------ ------------------------------------- ----------------------

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  apiName             0..1   [St ring](#String)                 see [ IEEECigreAPISigna l
                                                                \<#IEEECigreAPIS
                                                                ignal.apiName\>]{.title-ref}\_\_

  apiParameterKind    0..1   [IEEECi greAPIParameterKi nd       see [IEEECigre APISignal \<#IEEEC
                             \<#IEEECigreAPI                    igreAPISignal.api
                             ParameterKind\>]{.title-ref}\_\_   ParameterKind\>]{.title-ref}\_\_

  apiSequenceNumber   0..1   [Inte ger](#Integer)               see [IEEECigreA PISignal \<#IEEECi
                                                                greAPISignal.apiS
                                                                equenceNumber\>]{.title-ref}\_\_

  apiWidth            0..1   [Inte ger](#Integer)               see [I EEECigreAPISignal
                                                                \<#IEEECigreAPISi
                                                                gnal.apiWidth\>]{.title-ref}\_\_

  multiplier          0..1   [U nitMultiplier \<#U              see [IEE ECigreAPISignal \<
                             nitMultiplier\>]{.title-ref}\_\_   #IEEECigreAPISign
                                                                al.multiplier\>]{.title-ref}\_\_

  phase               0..1   [Sin glePhaseKind \<#Si            see [IEEECigreAPISig nal
                             nglePhaseKind\>]{.title-ref}\_\_   \<#IEEECigreAP
                                                                ISignal.phase\>]{.title-ref}\_\_

  unit                0..1   [UnitSymbol](#UnitSymbol)          see [IEEECigreAPISi gnal
                                                                \<#IEEECigreA
                                                                PISignal.unit\>]{.title-ref}\_\_

  ConnectivityNode    0..1   [Conne ctivityNode \<#Con          see [IEEECigre APISignal \<#IEEEC
                             nectivityNode\>]{.title-ref}\_\_   igreAPISignal.Con
                                                                nectivityNode\>]{.title-ref}\_\_

  DCNode              0..1   [DC Node](#DCNode)                 see [IEEECigreAPISign al
                                                                \<#IEEECigreAPI
                                                                Signal.DCNode\>]{.title-ref}\_\_

  IEEEC               0..1   [ IEEECigreAPISigna lInfo          see [IEEECigreAPISig nal
  igreAPISignalInfo          \<#IEEECigre                       \<#IEEECigreAP ISignal.IEEECigre
                             APISignalInfo\>]{.title-ref}\_\_   APISignalInfo\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  ACDCTerminal        0..1   [ACDCTerminal \<                   see [S ignalDescriptor \<
                             #ACDCTerminal\>]{.title-ref}\_\_   #SignalDescriptor
                                                                .ACDCTerminal\>]{.title-ref}\_\_

  Dyna                0..1   [DynamicsFunctio nBlock            see [SignalDesc riptor \<#SignalDe
  micsFunctionBlock          \<#Dynamics                        scriptor.Dynamics
                             FunctionBlock\>]{.title-ref}\_\_   FunctionBlock\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  mRID                0..1   [St ring](#String)                 see [Detaile dModelDescriptor
                                                                \<#DetailedModelDe
                                                                scriptor.mRID\>]{.title-ref}\_\_

  Detailed            0..1   [Detail edModelTypeDynami cs       see [DetailedMod elDescriptor
  ModelTypeDynamics          \<#DetailedMode                    \<#De tailedModelDescri
                             lTypeDynamics\>]{.title-ref}\_\_   ptor.DetailedMode
                                                                lTypeDynamics\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#IEEECigreAPIOutput .container .group}
[#IEEECigreAPIOutput](#IEEECigreAPIOutput)

**IEEECigreAPIOutput**

Emtiop

Connects the set of CIGRE TB 958 API output signals, for this instance,
to points in the network model.

**Native Members**

  -------------- ------ ------------------------------------- ----------------------
  kind           0..1   [IEEECigreAP IOutputKind \<#IEEECi    The type of output
                        greAPIOutputKind\>]{.title-ref}\_\_   signal. The phase
                                                              attribute must be
                                                              supplied with
                                                              modulationIndex and
                                                              vscVoltage. If
                                                              apiDefined, obtain
                                                              more information from
                                                              the CIGRE TB 958 API.

  scalingRatio   0..1   [Float](#Float)                       Ratio between the
                                                              controller output and
                                                              the power system
                                                              connection point. For
                                                              example, a modulation
                                                              index output could be
                                                              multiplied by 50% of
                                                              the DC link voltage of
                                                              a converter to create
                                                              a controlled voltage
                                                              source connected to
                                                              the AC power network.
                                                              If the DC link voltage
                                                              is 1200 V, the
                                                              scalingRatio should
                                                              then be 600. May be
                                                              any value, noting that
                                                              a value of zero has no
                                                              effect on the power
                                                              network.
  -------------- ------ ------------------------------------- ----------------------

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  apiName             0..1   [St ring](#String)                 see [ IEEECigreAPISigna l
                                                                \<#IEEECigreAPIS
                                                                ignal.apiName\>]{.title-ref}\_\_

  apiParameterKind    0..1   [IEEECi greAPIParameterKi nd       see [IEEECigre APISignal \<#IEEEC
                             \<#IEEECigreAPI                    igreAPISignal.api
                             ParameterKind\>]{.title-ref}\_\_   ParameterKind\>]{.title-ref}\_\_

  apiSequenceNumber   0..1   [Inte ger](#Integer)               see [IEEECigreA PISignal \<#IEEECi
                                                                greAPISignal.apiS
                                                                equenceNumber\>]{.title-ref}\_\_

  apiWidth            0..1   [Inte ger](#Integer)               see [I EEECigreAPISignal
                                                                \<#IEEECigreAPISi
                                                                gnal.apiWidth\>]{.title-ref}\_\_

  multiplier          0..1   [U nitMultiplier \<#U              see [IEE ECigreAPISignal \<
                             nitMultiplier\>]{.title-ref}\_\_   #IEEECigreAPISign
                                                                al.multiplier\>]{.title-ref}\_\_

  phase               0..1   [Sin glePhaseKind \<#Si            see [IEEECigreAPISig nal
                             nglePhaseKind\>]{.title-ref}\_\_   \<#IEEECigreAP
                                                                ISignal.phase\>]{.title-ref}\_\_

  unit                0..1   [UnitSymbol](#UnitSymbol)          see [IEEECigreAPISi gnal
                                                                \<#IEEECigreA
                                                                PISignal.unit\>]{.title-ref}\_\_

  ConnectivityNode    0..1   [Conne ctivityNode \<#Con          see [IEEECigre APISignal \<#IEEEC
                             nectivityNode\>]{.title-ref}\_\_   igreAPISignal.Con
                                                                nectivityNode\>]{.title-ref}\_\_

  DCNode              0..1   [DC Node](#DCNode)                 see [IEEECigreAPISign al
                                                                \<#IEEECigreAPI
                                                                Signal.DCNode\>]{.title-ref}\_\_

  IEEEC               0..1   [ IEEECigreAPISigna lInfo          see [IEEECigreAPISig nal
  igreAPISignalInfo          \<#IEEECigre                       \<#IEEECigreAP ISignal.IEEECigre
                             APISignalInfo\>]{.title-ref}\_\_   APISignalInfo\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  ACDCTerminal        0..1   [ACDCTerminal \<                   see [S ignalDescriptor \<
                             #ACDCTerminal\>]{.title-ref}\_\_   #SignalDescriptor
                                                                .ACDCTerminal\>]{.title-ref}\_\_

  Dyna                0..1   [DynamicsFunctio nBlock            see [SignalDesc riptor \<#SignalDe
  micsFunctionBlock          \<#Dynamics                        scriptor.Dynamics
                             FunctionBlock\>]{.title-ref}\_\_   FunctionBlock\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  mRID                0..1   [St ring](#String)                 see [Detaile dModelDescriptor
                                                                \<#DetailedModelDe
                                                                scriptor.mRID\>]{.title-ref}\_\_

  Detailed            0..1   [Detail edModelTypeDynami cs       see [DetailedMod elDescriptor
  ModelTypeDynamics          \<#DetailedMode                    \<#De tailedModelDescri
                             lTypeDynamics\>]{.title-ref}\_\_   ptor.DetailedMode
                                                                lTypeDynamics\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#IEEECigreAPIParameter .container .group}
[#IEEECigreAPIParameter](#IEEECigreAPIParameter)

**IEEECigreAPIParameter**

Emtiop

A single value in the array of CIGRE TB 958 API input values. The
meaning of this parameter is discoverable through the API for an
implementation, like a DLL, and/or documentation provided with the
model. This CIM class maintains only the essential parameter setting and
location/size in the array of API inputs.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  apiParameterKind    0..1   [IEEECi greAPIParameterKi nd       The C type of this
                             \<#IEEECigreAPI                    parameter as
                             ParameterKind\>]{.title-ref}\_\_   expected by the
                                                                CIGRE TB 958 API.
                                                                This also
                                                                determines the
                                                                memory size of this
                                                                parameter in the
                                                                array of model
                                                                inputs. It
                                                                indicates whether
                                                                the value attribute
                                                                should be
                                                                considered a
                                                                string, integer, or
                                                                floating point
                                                                value.

  apiSequenceNumber   0..1   [Inte ger](#Integer)               The zero-based
                                                                array index for
                                                                this parameter, as
                                                                expected in the
                                                                CIGRE TB 958 API.

  value               0..1   [St ring](#String)                 The parameter
                                                                value, to be parsed
                                                                from string format
                                                                according to the
                                                                apiParameterKind.

  IEEECigreAPI        0..1   [IEEECigreAPI \<                   The API model
                             #IEEECigreAPI\>]{.title-ref}\_\_   instance associated
                                                                with this
                                                                parameter.

  IEEECigr            0..1   [IEEECi greAPIParameterIn fo       Expanded set of
  eAPIParameterInfo          \<#IEEECigreAPI                    attributes
                             ParameterInfo\>]{.title-ref}\_\_   available from the
                                                                CIGRE TB 958 API.
  ------------------- ------ ---------------------------------- -------------------
:::

::: {#IEEECigreAPIParameterInfo .container .group}
[#IEEECigreAPIParameterInfo](#IEEECigreAPIParameterInfo)

**IEEECigreAPIParameterInfo**

Emtiop

Supplemental information about this parameter from the CIGRE TB 958 API.

**Native Members**

  ------------------- ------- ---------------------------------- -------------------
  apiDefaultValue     0..1    [St ring](#String)                 Default value
                                                                 internally assigned
                                                                 by the model
                                                                 implementation.

  apiDescription      0..1    [St ring](#String)                 General
                                                                 description.

  apiFixedValue       0..1    [Bool ean](#Boolean)               True if the
                                                                 parameter can be
                                                                 changed any time
                                                                 during simulation,
                                                                 False if the
                                                                 parameter value
                                                                 must be set and
                                                                 time zero and not
                                                                 changed thereafter.

  apiGroupName        0..1    [St ring](#String)                 A group name, if
                                                                 applicable.

  apiMaxValue         0..1    [St ring](#String)                 Maximum value
                                                                 allowed, for
                                                                 numerical
                                                                 parameters.

  apiMinValue         0..1    [St ring](#String)                 Minimum value
                                                                 allowed, for
                                                                 numerical
                                                                 parameters.

  apiName             0..1    [St ring](#String)                 The name of this
                                                                 parameter, as
                                                                 returned by the
                                                                 CIGRE TB 958 API.
                                                                 If there is an
                                                                 inherited Iden
                                                                 tifiedObject.name
                                                                 attribute, it may
                                                                 not necessarily
                                                                 match this name.

  apiUnit             0..1    [St ring](#String)                 The parameter units
                                                                 expected by the
                                                                 CIGRE TB 958 API.
                                                                 This may not
                                                                 correspond to CIM
                                                                 units, so
                                                                 interpretation may
                                                                 be required.

  IEEEC               0..\*   [IEEECigreAPIPar ameter            Minimum set of
  igreAPIParameters           \<#IEEECigr                        attributes required
                              eAPIParameter\>]{.title-ref}\_\_   to use this
                                                                 parameter.
  ------------------- ------- ---------------------------------- -------------------
:::

::: {#IEEECigreAPISignalInfo .container .group}
[#IEEECigreAPISignalInfo](#IEEECigreAPISignalInfo)

**IEEECigreAPISignalInfo**

Emtiop

Supplemental information about the signal from the CIGRE TB 958 API.

**Native Members**

  ------------------- ------- ---------------------------------- -------------------
  apiDescription      0..1    [St ring](#String)                 A description of
                                                                 the signal as
                                                                 written by the
                                                                 model\'s developer.

  apiUnit             0..1    [St ring](#String)                 The signal units
                                                                 expected by the
                                                                 CIGRE TB 958 API.
                                                                 This may not
                                                                 correspond to CIM
                                                                 units, so
                                                                 interpretation may
                                                                 be required.

  IE                  0..\*   [IEEECigre APISignal \<#IEEEC      Minimum set of
  EECigreAPISignals           igreAPISignal\>]{.title-ref}\_\_   attributes required
                                                                 to use this signal.
  ------------------- ------- ---------------------------------- -------------------
:::

::: {#LinearShuntCompensator .container .group}
[#LinearShuntCompensator](#LinearShuntCompensator)

**LinearShuntCompensator**

Wires

A linear shunt compensator has banks or sections with equal admittance
values.

**Native Members**

  ------------- ------ ---------------------- ----------------------
  bPerSection   1..1   [Susceptan             Positive sequence
                       ce](#Susceptance)      shunt (charging)
                                              susceptance per
                                              section.

  gPerSection   1..1   [Conductan             Positive sequence
                       ce](#Conductance)      shunt (charging)
                                              conductance per
                                              section.
  ------------- ------ ---------------------- ----------------------

**Inherited Members**

  ----------------- ------ ---------------------------------- ----------------------------------
  grounded          1..1   [Bool ean](#Boolean)               see [ShuntCompensat or
                                                              \<#ShuntCompens
                                                              ator.grounded\>]{.title-ref}\_\_

  maximumSections   1..1   [Inte ger](#Integer)               see [Shun tCompensator \<#Sh
                                                              untCompensator.ma
                                                              ximumSections\>]{.title-ref}\_\_

  nomU              1..1   [Volt age](#Voltage)               see [ShuntCompe nsator \<#ShuntCom
                                                              pensator.nomU\>]{.title-ref}\_\_

  phaseConnection   0..1   [Phas eShuntConnectionK ind        see [Shun tCompensator \<#Sh
                           \<#PhaseShuntC                     untCompensator.ph
                           onnectionKind\>]{.title-ref}\_\_   aseConnection\>]{.title-ref}\_\_

  sections          1..1   [Float](#Float)                    see [ShuntCompensat or
                                                              \<#ShuntCompens
                                                              ator.sections\>]{.title-ref}\_\_
  ----------------- ------ ---------------------------------- ----------------------------------

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#LoadResponseCharacteristic .container .group}
[#LoadResponseCharacteristic](#LoadResponseCharacteristic)

**LoadResponseCharacteristic**

LoadModel

Models the characteristic response of the load demand due to changes in
system conditions such as voltage and frequency. It is not related to
demand response.

If LoadResponseCharacteristic.exponentModel is True, the exponential
voltage or frequency dependent models are specified and used as to
calculate active and reactive power components of the load model.

The equations to calculate active and reactive power components of the
load model are internal to the power flow calculation, hence they use
different quantities depending on the use case of the data exchange.

The equations for exponential voltage dependent load model injected
power are:

pInjection= Pnominal\* (Voltage/cim:BaseVoltage.nominalVoltage) \*\*
cim:LoadResponseCharacteristic.pVoltageExponent

qInjection= Qnominal\* (Voltage/cim:BaseVoltage.nominalVoltage) \*\*
cim:LoadResponseCharacteristic.qVoltageExponent

pInjection = Pnominal\* (Frequency/(Nominal
frequency))\*\*cim:LoadResponseCharacteristic.pFrequencyExponent

qInjection = Qnominal\* (Frequency/(Nominal
frequency))\*\*cim:LoadResponseCharacteristic.qFrequencyExponent

Note that both voltage and frequency exponents could be used together so
the full equation would be:

pInjection = Pnominal\*
(Voltage/(cim:BaseVoltage.nominalVoltage))**cim:LoadResponseCharacteristic.pVoltageExponent
\* (Frequency/(base
frequency))**cim:LoadResponseCharacteristic.pFrequencyExponent

qInjection = Qnominal\*
(Voltage/(cim:BaseVoltage.nominalVoltage))**cim:LoadResponseCharacteristic.qVoltageExponent
\* (Frequency/(base
frequency))**cim:LoadResponseCharacteristic.qFrequencyExponent

The voltage and frequency expressed in the equation are values obtained
from solved power flow. Base voltage and base frequency are those
derived from the connectivity of the static network model.

Where:

1)  \* means \"multiply\" and \*\* is \"raised to the power of\";

2\) Pnominal and Qnominal represent the active power and reactive power
at nominal voltage as any load described by the voltage exponential
model shall be given at nominal voltage. This means that
EnergyConsumer.p and EnergyConsumer.q are at nominal voltage.

3)  After power flow is solved:

-pInjection and qInjection correspond to SvPowerflow.p and SvPowerflow.q
respectively.

\- Voltage corresponds to SvVoltage.v at the TopologicalNode where the
load is connected.

**Native Members**

+----------------+----------------+----------------+----------------+
| exponentModel  | 1..1           | [Boo           | Indicates the  |
|                |                | l              | exponential    |
|                |                | ean](#Boolean) | voltage        |
|                |                |                | dependency     |
|                |                |                | model is to be |
|                |                |                | used. If       |
|                |                |                | false, the     |
|                |                |                | coefficient    |
|                |                |                | model is to be |
|                |                |                | used.          |
|                |                |                |                |
|                |                |                | The            |
|                |                |                | exponential    |
|                |                |                | voltage        |
|                |                |                | dependency     |
|                |                |                | model consist  |
|                |                |                | of the         |
|                |                |                | attributes:    |
|                |                |                |                |
|                |                |                | \- p V         |
|                |                |                | oltageExponent |
|                |                |                |                |
|                |                |                | \- q V         |
|                |                |                | oltageExponent |
|                |                |                |                |
|                |                |                | \- pFr e       |
|                |                |                | quencyExponent |
|                |                |                |                |
|                |                |                | \- qFre q      |
|                |                |                | uencyExponent. |
|                |                |                |                |
|                |                |                | The            |
|                |                |                | coefficient    |
|                |                |                | model consist  |
|                |                |                | of the         |
|                |                |                | attributes:    |
|                |                |                |                |
|                |                |                | \- pCo n       |
|                |                |                | stantImpedance |
|                |                |                |                |
|                |                |                | \- p C         |
|                |                |                | onstantCurrent |
|                |                |                |                |
|                |                |                | -              |
|                |                |                | pConstantPower |
|                |                |                |                |
|                |                |                | \- qCo n       |
|                |                |                | stantImpedance |
|                |                |                |                |
|                |                |                | \- q C         |
|                |                |                | onstantCurrent |
|                |                |                |                |
|                |                |                | -q             |
|                |                |                | ConstantPower. |
|                |                |                |                |
|                |                |                | The sum of     |
|                |                |                | pCon s         |
|                |                |                | tantImpedance, |
|                |                |                | p C            |
|                |                |                | onstantCurrent |
|                |                |                | and            |
|                |                |                | pConstantPower |
|                |                |                | shall equal 1. |
|                |                |                |                |
|                |                |                | The sum of     |
|                |                |                | qCon s         |
|                |                |                | tantImpedance, |
|                |                |                | q C            |
|                |                |                | onstantCurrent |
|                |                |                | and            |
|                |                |                | qConstantPower |
|                |                |                | shall equal 1. |
+----------------+----------------+----------------+----------------+
| p C            | 1..1           | [Flo           | Portion of     |
| onstantCurrent |                | at](#Float)    | active power   |
|                |                |                | load modelled  |
|                |                |                | as constant    |
|                |                |                | current.       |
+----------------+----------------+----------------+----------------+
| pCo n          | 1..1           | [Flo           | Portion of     |
| stantImpedance |                | at](#Float)    | active power   |
|                |                |                | load modelled  |
|                |                |                | as constant    |
|                |                |                | impedance.     |
+----------------+----------------+----------------+----------------+
| pConstantPower | 1..1           | [Flo           | Portion of     |
|                |                | at](#Float)    | active power   |
|                |                |                | load modelled  |
|                |                |                | as constant    |
|                |                |                | power.         |
+----------------+----------------+----------------+----------------+
| pFr e          | 1..1           | [Flo           | Exponent of    |
| quencyExponent |                | at](#Float)    | per unit       |
|                |                |                | frequency      |
|                |                |                | effecting      |
|                |                |                | active power.  |
+----------------+----------------+----------------+----------------+
| p V            | 1..1           | [Flo           | Exponent of    |
| oltageExponent |                | at](#Float)    | per unit       |
|                |                |                | voltage        |
|                |                |                | effecting real |
|                |                |                | power.         |
+----------------+----------------+----------------+----------------+
| q C            | 1..1           | [Flo           | Portion of     |
| onstantCurrent |                | at](#Float)    | reactive power |
|                |                |                | load modelled  |
|                |                |                | as constant    |
|                |                |                | current.       |
+----------------+----------------+----------------+----------------+
| qCo n          | 1..1           | [Flo           | Portion of     |
| stantImpedance |                | at](#Float)    | reactive power |
|                |                |                | load modelled  |
|                |                |                | as constant    |
|                |                |                | impedance.     |
+----------------+----------------+----------------+----------------+
| qConstantPower | 1..1           | [Flo           | Portion of     |
|                |                | at](#Float)    | reactive power |
|                |                |                | load modelled  |
|                |                |                | as constant    |
|                |                |                | power.         |
+----------------+----------------+----------------+----------------+
| qFr e          | 1..1           | [Flo           | Exponent of    |
| quencyExponent |                | at](#Float)    | per unit       |
|                |                |                | frequency      |
|                |                |                | effecting      |
|                |                |                | reactive       |
|                |                |                | power.         |
+----------------+----------------+----------------+----------------+
| q V            | 1..1           | [Flo           | Exponent of    |
| oltageExponent |                | at](#Float)    | per unit       |
|                |                |                | voltage        |
|                |                |                | effecting      |
|                |                |                | reactive       |
|                |                |                | power.         |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#MachineSaturationCurve .container .group}
[#MachineSaturationCurve](#MachineSaturationCurve)

**MachineSaturationCurve**

Emtiop

Use to define machine saturation with more than two points. xUnit is A
(RMS current) and y1Unit is none (per-unit voltage).

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  Synchrono           0..1   [Synchron ousMachineDetaile d      The synchronous
  usMachineDetailed          \<#SynchronousMa                   machine this
                             chineDetailed\>]{.title-ref}\_\_   saturation
                                                                characteristic
                                                                applies to.

  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**

  -------------- ------ ----------------------------------- -------------------------------------
  mRID           1..1   [String](#String)                   see [Cu rve](#Curve.mRID)

  curveStyle     0..1   [CurveSt yle](#CurveStyle)          see [Curve \<#
                                                            Curve.curveStyle\>]{.title-ref}\_\_

  name           1..1   [String](#String)                   see [Cu rve](#Curve.name)

  xMultiplier    0..1   [UnitMultiplier](#UnitMultiplier)   see [Curve \<#C
                                                            urve.xMultiplier\>]{.title-ref}\_\_

  xUnit          0..1   [UnitSym bol](#UnitSymbol)          see [Cur ve](#Curve.xUnit)

  y1Multiplier   0..1   [UnitMultiplier](#UnitMultiplier)   see [Curve \<#Cu
                                                            rve.y1Multiplier\>]{.title-ref}\_\_

  y1Unit         0..1   [UnitSym bol](#UnitSymbol)          see [Curv e](#Curve.y1Unit)
  -------------- ------ ----------------------------------- -------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#NthAmDynamicModel .container .group}
[#NthAmDynamicModel](#NthAmDynamicModel)

**NthAmDynamicModel**

Emtiop

Parameterized models from software libraries or user code that rely on
documentation provided elsewhere, e.g., software documentation. The
model is named within the domain of nameKind, e.g., ST6B for DYR or
esst6b for DYD. Parameters are maintained by name and sequence number in
the ParameterDescriptor class.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  clo                 0..1   [St ring](#String)                 Name of the closest
  sestStandardModel                                             match from Dynamics
                                                                / StandardModels,
                                                                if such a match
                                                                exists.

  modelKind           0..1   [N thAmModelKind \<#N              Suggested
                             thAmModelKind\>]{.title-ref}\_\_   application of this
                                                                dynamic model.

  nameKind            0..1   [NthAmMode lNameKind \<#NthAm      
                             ModelNameKind\>]{.title-ref}\_\_   

  statusKind          0..1   [NthAmModelSta tusKind \<#NthAmMo  
                             delStatusKind\>]{.title-ref}\_\_   
  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**
:::

::: {#NuclearGeneratingUnit .container .group}
[#NuclearGeneratingUnit](#NuclearGeneratingUnit)

**NuclearGeneratingUnit**

Production

A nuclear generating unit.

**Inherited Members**

  --------------- ------ --------------------- ------------------------------------
  maxOperatingP   1..1   [ActivePowe           see [GeneratingU nit
                         r](#ActivePower)      \<#GeneratingUni
                                               t.maxOperatingP\>]{.title-ref}\_\_

  minOperatingP   1..1   [ActivePowe           see [GeneratingU nit
                         r](#ActivePower)      \<#GeneratingUni
                                               t.minOperatingP\>]{.title-ref}\_\_
  --------------- ------ --------------------- ------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#OperationalLimitSet .container .group}
[#OperationalLimitSet](#OperationalLimitSet)

**OperationalLimitSet**

OperationalLimits

A set of limits associated with equipment. Sets of limits might apply to
a specific temperature, or season for example. A set of limits may
contain different severities of limit levels that would apply to the
same equipment. The set may contain limits of different types such as
apparent power and current limits or high and low voltage limits that
are logically applied together as a set.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 1..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| name           | 1..1           | [S trin        | The name is    |
|                |                | g](#String)    | any free human |
|                |                |                | readable and   |
|                |                |                | possibly non   |
|                |                |                | unique text    |
|                |                |                | naming the     |
|                |                |                | object.        |
+----------------+----------------+----------------+----------------+
| Terminal       | 1..1           | [ACD CTerminal | The terminal   |
|                |                | \<#ac          | where the      |
|                |                | d              | operational    |
|                |                | cterminal\>]{. | limit set      |
|                |                | title-ref}\_\_ | apply.         |
|                |                | (              |                |
|                |                | #ACDCTerminal) |                |
+----------------+----------------+----------------+----------------+
:::

::: {#OperationalLimitType .container .group}
[#OperationalLimitType](#OperationalLimitType)

**OperationalLimitType**

OperationalLimits

The operational meaning of a category of limits.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 1..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| acc e          | 0..1           | [Sec           | The nominal    |
| ptableDuration |                | o              | acceptable     |
|                |                | nds](#Seconds) | duration of    |
|                |                |                | the limit.     |
|                |                |                | Limits are     |
|                |                |                | commonly       |
|                |                |                | expressed in   |
|                |                |                | terms of the   |
|                |                |                | time limit for |
|                |                |                | which the      |
|                |                |                | limit is       |
|                |                |                | normally       |
|                |                |                | acceptable.    |
|                |                |                | The actual     |
|                |                |                | acceptable     |
|                |                |                | duration of a  |
|                |                |                | specific limit |
|                |                |                | may depend on  |
|                |                |                | other local    |
|                |                |                | factors such   |
|                |                |                | as temperature |
|                |                |                | or wind speed. |
|                |                |                | The attribute  |
|                |                |                | has meaning    |
|                |                |                | only if the    |
|                |                |                | flag isI n     |
|                |                |                | finiteDuration |
|                |                |                | is set to      |
|                |                |                | false, hence   |
|                |                |                | it shall not   |
|                |                |                | be exchanged   |
|                |                |                | when isI n     |
|                |                |                | finiteDuration |
|                |                |                | is set to      |
|                |                |                | true.          |
+----------------+----------------+----------------+----------------+
| direction      | 0..1           | [Op e          | The direction  |
|                |                | rationalLimitD | of the limit.  |
|                |                | irectionKind   |                |
|                |                | \<#%20Operatio |                |
|                |                | nalLimi%20tDir |                |
|                |                | e              |                |
|                |                | ctionKind\>]{. |                |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+
| isI n          | 0..1           | [Boo           | Defines if the |
| finiteDuration |                | l              | operational    |
|                |                | ean](#Boolean) | limit type has |
|                |                |                | infinite       |
|                |                |                | duration. If   |
|                |                |                | true, the      |
|                |                |                | limit has      |
|                |                |                | infinite       |
|                |                |                | duration. If   |
|                |                |                | false, the     |
|                |                |                | limit has      |
|                |                |                | definite       |
|                |                |                | duration which |
|                |                |                | is defined by  |
|                |                |                | the attribute  |
|                |                |                | acce p         |
|                |                |                | tableDuration. |
+----------------+----------------+----------------+----------------+
| name           | 1..1           | [S trin        | The name is    |
|                |                | g](#String)    | any free human |
|                |                |                | readable and   |
|                |                |                | possibly non   |
|                |                |                | unique text    |
|                |                |                | naming the     |
|                |                |                | object.        |
+----------------+----------------+----------------+----------------+
:::

::: {#ParameterDescriptor .container .group}
[#ParameterDescriptor](#ParameterDescriptor)

**ParameterDescriptor**

DetailedModelDescription

Supports definition of one or more parameters of several different
datatypes for use by the detailed model. It describes the parameters
used in the equations of the detailed model.

The name of the parameter shall be the same as the name used in the
equations of the detailed model.

**Native Members**

  ----------------- ------ ------------------- -------------------
  engineeringUnit   0..1   [St ring](#String)  The engineering
                                               unit of the value.

  sequenceNumber    0..1   [Inte               Sequence number of
                           ger](#Integer)      the parameter among
                                               the set of
                                               parameters
                                               associated with the
                                               related proprietary
                                               user-defined model.

  typicalValue      0..1   [St ring](#String)  Typical value for
                                               the parameter. The
                                               datatype is as
                                               specified in
                                               attribute
                                               valueXSDdatatype.
  ----------------- ------ ------------------- -------------------

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  mRID                0..1   [St ring](#String)                 see [Detaile dModelDescriptor
                                                                \<#DetailedModelDe
                                                                scriptor.mRID\>]{.title-ref}\_\_

  Detailed            0..1   [Detail edModelTypeDynami cs       see [DetailedMod elDescriptor
  ModelTypeDynamics          \<#DetailedMode                    \<#De tailedModelDescri
                             lTypeDynamics\>]{.title-ref}\_\_   ptor.DetailedMode
                                                                lTypeDynamics\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#ParameterValue .container .group}
[#ParameterValue](#ParameterValue)

**ParameterValue**

DetailedModelDescription

Provides the value of a given parameter of a detailed model dynamics.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  value               0..1   [St ring](#String)                 The value of the
                                                                parameter.

  Deta                0..1   [DetailedModelDy namics            The detailed model
  iledModelDynamics          \<#Detailed                        to which this
                             ModelDynamics\>]{.title-ref}\_\_   parameter value
                                                                applies.

  Pa                  0..1   [ParameterDe scriptor \<#Parame    The parameter
  rameterDescriptor          terDescriptor\>]{.title-ref}\_\_   descriptor that has
                                                                this value.
  ------------------- ------ ---------------------------------- -------------------
:::

::: {#PhaseTapChangerLinear .container .group}
[#PhaseTapChangerLinear](#PhaseTapChangerLinear)

**PhaseTapChangerLinear**

Wires

Describes a tap changer with a linear relation between the tap step and
the phase angle difference across the transformer. This is a
mathematical model that is an approximation of a real phase tap changer.

The phase angle is computed as stepPhaseShiftIncrement times the tap
position.

The voltage magnitude of both sides is the same.

**Native Members**

+----------------+----------------+----------------+----------------+
| stepPhas e     | 0..1           | [Ang leDegrees | Phase shift    |
| ShiftIncrement |                | \<#an          | per step       |
|                |                | g              | position. A    |
|                |                | ledegrees\>]{. | positive value |
|                |                | title-ref}\_\_ | indicates a    |
|                |                | (              | positive angle |
|                |                | #AngleDegrees) | variation from |
|                |                |                | the Terminal   |
|                |                |                | at the Power T |
|                |                |                | ransformerEnd, |
|                |                |                | where the      |
|                |                |                | TapChanger is  |
|                |                |                | located, into  |
|                |                |                | the            |
|                |                |                | transformer.   |
|                |                |                |                |
|                |                |                | The actual     |
|                |                |                | phase shift    |
|                |                |                | increment      |
|                |                |                | might be more  |
|                |                |                | accurately     |
|                |                |                | computed from  |
|                |                |                | the            |
|                |                |                | symmetrical or |
|                |                |                | asymmetrical   |
|                |                |                | models or a    |
|                |                |                | tap step table |
|                |                |                | lookup if      |
|                |                |                | those are      |
|                |                |                | available.     |
+----------------+----------------+----------------+----------------+
| xMax           | 0..1           | [Reactan ce \< | The reactance  |
|                |                | #              | depends on the |
|                |                | Reactance\>]{. | tap position   |
|                |                | title-ref}\_\_ | according to a |
|                |                |                | \"u\" shaped   |
|                |                |                | curve. The     |
|                |                |                | maximum        |
|                |                |                | reactance      |
|                |                |                | (xMax) appears |
|                |                |                | at the low and |
|                |                |                | high tap       |
|                |                |                | positions.     |
|                |                |                | Depending on   |
|                |                |                | the \"u\"      |
|                |                |                | curve the      |
|                |                |                | attribute can  |
|                |                |                | be either      |
|                |                |                | higher or      |
|                |                |                | lower than     |
|                |                |                | PowerTr a      |
|                |                |                | nsformerEnd.x. |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ---------------- ------ ---------------------------------- ----------------------------------
  TransformerEnd   0..1   [T ransformerEnd \<#T              see [P haseTapChanger \<#
                          ransformerEnd\>]{.title-ref}\_\_   PhaseTapChanger.T
                                                             ransformerEnd\>]{.title-ref}\_\_

  ---------------- ------ ---------------------------------- ----------------------------------

  ------------- ------ ---------------------- -------------------------------------
  highStep      0..1   [I nteger](#Integer)   see [TapChanger \<#Tap
                                              Changer.highStep\>]{.title-ref}\_\_

  lowStep       0..1   [I nteger](#Integer)   see [TapChanger \<#Ta
                                              pChanger.lowStep\>]{.title-ref}\_\_

  neutralStep   0..1   [I nteger](#Integer)   see [TapChanger \<#TapCha
                                              nger.neutralStep\>]{.title-ref}\_\_

  neutralU      0..1   [V oltage](#Voltage)   see [TapChanger \<#Tap
                                              Changer.neutralU\>]{.title-ref}\_\_

  normalStep    0..1   [I nteger](#Integer)   see [TapChanger \<#TapCh
                                              anger.normalStep\>]{.title-ref}\_\_

  step          1..1   [Float](#Float)        see [TapChanger \<
                                              #TapChanger.step\>]{.title-ref}\_\_
  ------------- ------ ---------------------- -------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#PhotoVoltaicUnit .container .group}
[#PhotoVoltaicUnit](#PhotoVoltaicUnit)

**PhotoVoltaicUnit**

Production

A photovoltaic device or an aggregation of such devices.

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  maxP                1..1   [ActivePower](#ActivePower)        see [P owerElectronicsUn it
                                                                \<#PowerElectro
                                                                nicsUnit.maxP\>]{.title-ref}\_\_

  minP                1..1   [ActivePower](#ActivePower)        see [P owerElectronicsUn it
                                                                \<#PowerElectro
                                                                nicsUnit.minP\>]{.title-ref}\_\_

  PowerElec           1..1   [PowerEle ctronicsConnectio n      see [PowerE lectronicsUnit \<#
  tronicsConnection          \<#PowerElectron                   PowerElectronicsU
                             icsConnection\>]{.title-ref}\_\_   nit.PowerElectron
                                                                icsConnection\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#PowerElectronicsConnection .container .group}
[#PowerElectronicsConnection](#PowerElectronicsConnection)

**PowerElectronicsConnection**

Wires

A connection to the AC network for energy production or consumption that
uses power electronics rather than rotating machines.

**Native Members**

+----------------+----------------+----------------+----------------+
| maxIFault      | 1..1           | [PU](#PU)      | Maximum fault  |
|                |                |                | current this   |
|                |                |                | device will    |
|                |                |                | contribute, in |
|                |                |                | per-unit of    |
|                |                |                | rated current, |
|                |                |                | before the     |
|                |                |                | converter      |
|                |                |                | protection     |
|                |                |                | will trip or   |
|                |                |                | bypass.        |
+----------------+----------------+----------------+----------------+
| maxQ           | 1..1           | [React         | Maximum        |
|                |                | ivePower       | reactive power |
|                |                | \<#Rea         | limit. This is |
|                |                | c              | the maximum    |
|                |                | tivePower\>]{. | (nameplate)    |
|                |                | title-ref}\_\_ | limit for the  |
|                |                |                | unit.          |
+----------------+----------------+----------------+----------------+
| minQ           | 1..1           | [React         | Minimum        |
|                |                | ivePower       | reactive power |
|                |                | \<#Rea         | limit for the  |
|                |                | c              | unit. This is  |
|                |                | tivePower\>]{. | the minimum    |
|                |                | title-ref}\_\_ | (nameplate)    |
|                |                |                | limit for the  |
|                |                |                | unit.          |
+----------------+----------------+----------------+----------------+
| p              | 1..1           | [A ctivePower  | Active power   |
|                |                | \<#A           | injection.     |
|                |                | c              | Load sign      |
|                |                | tivePower\>]{. | convention is  |
|                |                | title-ref}\_\_ | used, i.e.     |
|                |                |                | positive sign  |
|                |                |                | means flow out |
|                |                |                | from a node.   |
|                |                |                |                |
|                |                |                | Starting value |
|                |                |                | for a steady   |
|                |                |                | state          |
|                |                |                | solution.      |
+----------------+----------------+----------------+----------------+
| q              | 1..1           | [React         | Reactive power |
|                |                | ivePower       | injection.     |
|                |                | \<#Rea         | Load sign      |
|                |                | c              | convention is  |
|                |                | tivePower\>]{. | used, i.e.     |
|                |                | title-ref}\_\_ | positive sign  |
|                |                |                | means flow out |
|                |                |                | from a node.   |
|                |                |                |                |
|                |                |                | Starting value |
|                |                |                | for a steady   |
|                |                |                | state          |
|                |                |                | solution.      |
+----------------+----------------+----------------+----------------+
| ratedS         | 1..1           | [Appar         | Nameplate      |
|                |                | entPower       | apparent power |
|                |                | \<#App         | rating for the |
|                |                | a              | unit.          |
|                |                | rentPower\>]{. |                |
|                |                | title-ref}\_\_ | The attribute  |
|                |                |                | shall have a   |
|                |                |                | positive       |
|                |                |                | value.         |
+----------------+----------------+----------------+----------------+
| ratedU         | 1..1           | [Vol           | Rated voltage  |
|                |                | t              | (nameplate     |
|                |                | age](#Voltage) | data, Ur in    |
|                |                |                | IEC 60909-0).  |
|                |                |                | It is          |
|                |                |                | primarily used |
|                |                |                | for short      |
|                |                |                | circuit data   |
|                |                |                | exchange       |
|                |                |                | according to   |
|                |                |                | IEC 60909.     |
|                |                |                |                |
|                |                |                | The attribute  |
|                |                |                | shall be a     |
|                |                |                | positive       |
|                |                |                | value.         |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#PowerElectronicsConnectionDCTerminal .container .group}
[#PowerElectronicsConnectionDCTerminal](#PowerElectronicsConnectionDCTerminal)

**PowerElectronicsConnectionDCTerminal**

Emtiop

A DC connection point at the converter, which is also connected on the
AC side as any other AC ConductingEquipment. This special terminal is
separate from the regular DCTerminal to restrict the connection, such
that no other DC conducting equipment can be connected to the AC side.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  polarity            0..1   [ DCTerminalPolarit yKind          Use to indicated
                             \<#DCTermina                       positive or
                             lPolarityKind\>]{.title-ref}\_\_   negative polarity
                                                                on the DC side.

  PowerElec           0..1   [PowerEle ctronicsConnectio n      The PowerElec
  tronicsConnection          \<#PowerElectron                   tronicsConnection
                             icsConnection\>]{.title-ref}\_\_   for this terminal.
  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**

  -------- ------ ---------------------- ----------------------------------------
  DCNode   1..1   [DCNode](#DCNode)      see [DCBaseTerminal \<#DC
                                         BaseTerminal.DCNode\>]{.title-ref}\_\_

  -------- ------ ---------------------- ----------------------------------------

  ---------------- ------ ------------------- ----------------------------------
  sequenceNumber   1..1   [Inte               see [ACDCTerminal
                          ger](#Integer)      \<#ACDCTerminal.s
                                              equenceNumber\>]{.title-ref}\_\_

  ---------------- ------ ------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#PowerElectronicsWindUnit .container .group}
[#PowerElectronicsWindUnit](#PowerElectronicsWindUnit)

**PowerElectronicsWindUnit**

Production

A wind generating unit that connects to the AC network with power
electronics rather than rotating machines or an aggregation of such
units.

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  maxP                1..1   [ActivePower](#ActivePower)        see [P owerElectronicsUn it
                                                                \<#PowerElectro
                                                                nicsUnit.maxP\>]{.title-ref}\_\_

  minP                1..1   [ActivePower](#ActivePower)        see [P owerElectronicsUn it
                                                                \<#PowerElectro
                                                                nicsUnit.minP\>]{.title-ref}\_\_

  PowerElec           1..1   [PowerEle ctronicsConnectio n      see [PowerE lectronicsUnit \<#
  tronicsConnection          \<#PowerElectron                   PowerElectronicsU
                             icsConnection\>]{.title-ref}\_\_   nit.PowerElectron
                                                                icsConnection\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#PowerTransformer .container .group}
[#PowerTransformer](#PowerTransformer)

**PowerTransformer**

Wires

An electrical device consisting of two or more coupled windings, with or
without a magnetic core, for introducing mutual coupling between
electric circuits. Transformers can be used to control voltage and phase
shift (active power flow).

A power transformer may be composed of separate transformer tanks that
need not be identical.

A power transformer can be modelled with or without tanks and is
intended for use in both balanced and unbalanced representations. A
power transformer typically has two terminals, but may have one
(grounding), three or more terminals.

The inherited association ConductingEquipment.BaseVoltage should not be
used. The association from TransformerEnd to BaseVoltage should be used
instead.

**Native Members**

+----------------+----------------+----------------+----------------+
| vectorGroup    | 1..1           | [S trin        | Vector group   |
|                |                | g](#String)    | of the         |
|                |                |                | transformer    |
|                |                |                | for protective |
|                |                |                | relaying,      |
|                |                |                | e.g., Dyn1.    |
|                |                |                | For unbalanced |
|                |                |                | transformers,  |
|                |                |                | this may not   |
|                |                |                | be simply      |
|                |                |                | determined     |
|                |                |                | from the       |
|                |                |                | constituent    |
|                |                |                | winding        |
|                |                |                | connections    |
|                |                |                | and phase      |
|                |                |                | angle          |
|                |                |                | displacements. |
|                |                |                |                |
|                |                |                | The            |
|                |                |                | vectorGroup    |
|                |                |                | string         |
|                |                |                | consists of    |
|                |                |                | the following  |
|                |                |                | components in  |
|                |                |                | the order      |
|                |                |                | listed: high   |
|                |                |                | voltage        |
|                |                |                | winding        |
|                |                |                | connection,    |
|                |                |                | mid voltage    |
|                |                |                | winding        |
|                |                |                | connection     |
|                |                |                | (for three     |
|                |                |                | winding        |
|                |                |                | transformers), |
|                |                |                | phase          |
|                |                |                | displacement   |
|                |                |                | clock number   |
|                |                |                | from 0 to 11,  |
|                |                |                | low voltage    |
|                |                |                | winding        |
|                |                |                | connection     |
|                |                |                |                |
|                |                |                | phase          |
|                |                |                | displacement   |
|                |                |                | clock number   |
|                |                |                | from 0 to 11.  |
|                |                |                | The winding    |
|                |                |                | connections    |
|                |                |                | are D (delta), |
|                |                |                | Y (wye), YN    |
|                |                |                | (wye with      |
|                |                |                | neutral), Z    |
|                |                |                | (zigzag), ZN   |
|                |                |                | (zigzag with   |
|                |                |                | neutral), A    |
|                |                |                | (auto          |
|                |                |                | transformer).  |
|                |                |                | Upper case     |
|                |                |                | means the high |
|                |                |                | voltage, lower |
|                |                |                | case mid or    |
|                |                |                | low. The high  |
|                |                |                | voltage        |
|                |                |                | winding always |
|                |                |                | has clock      |
|                |                |                | position 0 and |
|                |                |                | is not         |
|                |                |                | included in    |
|                |                |                | the vector     |
|                |                |                | group string.  |
|                |                |                | Some examples: |
|                |                |                | YNy0 (two      |
|                |                |                | winding wye to |
|                |                |                | wye with no    |
|                |                |                | phase          |
|                |                |                | displacement), |
|                |                |                | YNd11 (two     |
|                |                |                | winding wye to |
|                |                |                | delta with 330 |
|                |                |                | degrees phase  |
|                |                |                | displacement), |
|                |                |                | YNyn0d5 (three |
|                |                |                | winding        |
|                |                |                | transformer    |
|                |                |                | wye with       |
|                |                |                | neutral high   |
|                |                |                | voltage, wye   |
|                |                |                | with neutral   |
|                |                |                | mid voltage    |
|                |                |                | and no phase   |
|                |                |                | displacement,  |
|                |                |                | delta low      |
|                |                |                | voltage with   |
|                |                |                | 150 degrees    |
|                |                |                | displacement). |
|                |                |                |                |
|                |                |                | Phase          |
|                |                |                | displacement   |
|                |                |                | is defined as  |
|                |                |                | the angular    |
|                |                |                | difference     |
|                |                |                | between the    |
|                |                |                | phasors        |
|                |                |                | representing   |
|                |                |                | the voltages   |
|                |                |                | between the    |
|                |                |                | neutral point  |
|                |                |                | (real or       |
|                |                |                | imaginary) and |
|                |                |                | the            |
|                |                |                | corresponding  |
|                |                |                | terminals of   |
|                |                |                | two windings,  |
|                |                |                | a positive     |
|                |                |                | sequence       |
|                |                |                | voltage system |
|                |                |                | being applied  |
|                |                |                | to the         |
|                |                |                | high-voltage   |
|                |                |                | terminals,     |
|                |                |                | following each |
|                |                |                | other in       |
|                |                |                | alphabetical   |
|                |                |                | sequence if    |
|                |                |                | they are       |
|                |                |                | lettered, or   |
|                |                |                | in numerical   |
|                |                |                | sequence if    |
|                |                |                | they are       |
|                |                |                | numbered: the  |
|                |                |                | phasors are    |
|                |                |                | assumed to     |
|                |                |                | rotate in a co |
|                |                |                | u              |
|                |                |                | nter-clockwise |
|                |                |                | sense.         |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#PowerTransformerEnd .container .group}
[#PowerTransformerEnd](#PowerTransformerEnd)

**PowerTransformerEnd**

Wires

A PowerTransformerEnd is associated with each Terminal of a
PowerTransformer.

The impedance values r, r0, x, and x0 of a PowerTransformerEnd
represents a star equivalent as follows.

1\) two PowerTransformerEnd-s shall be defined for a two Terminal
PowerTransformer even if the two PowerTransformerEnd-s have the same
rated voltage. The high voltage PowerTransformerEnd
(TransformerEnd.endNumber=1) is the one used to exchange resistances (r,
r0) and reactances (x, x0) of the PowerTransformer while the low voltage
PowerTransformerEnd (TransformerEnd.endNumber=2) shall have zero
impedance values.

2\) for a three Terminal PowerTransformer the three PowerTransformerEnds
represent a star equivalent with each leg in the star represented by r,
r0, x, and x0 values.

3\) For a three Terminal transformer each PowerTransformerEnd shall have
g, g0, b and b0 values corresponding to the no load losses distributed
on the three PowerTransformerEnds. The total no load loss shunt
impedances may also be placed at one of the PowerTransformerEnds,
preferably the end numbered 1, having the shunt values on end 1. This is
the preferred way.

4\) for a PowerTransformer with more than three Terminals the
PowerTransformerEnd impedance values cannot be used. Instead use the
TransformerMeshImpedance or split the transformer into multiple
PowerTransformers.

Each PowerTransformerEnd must be contained by a PowerTransformer.
Because a PowerTransformerEnd (or any other object) can not be contained
by more than one parent, a PowerTransformerEnd can not have an
association to an EquipmentContainer (Substation, VoltageLevel, etc).

**Native Members**

+----------------+----------------+----------------+----------------+
| connectionKind | 1..1           | [WindingC      | Kind of        |
|                |                | onnectio n     | connection.    |
|                |                | \<#Win%20ding  |                |
|                |                | C              |                |
|                |                | onnection\>]{. |                |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+
| p              | 1..1           | [Int           | Terminal       |
| haseAngleClock |                | e              | voltage phase  |
|                |                | ger](#Integer) | angle          |
|                |                |                | displacement   |
|                |                |                | where 360      |
|                |                |                | degrees are    |
|                |                |                | represented    |
|                |                |                | with clock     |
|                |                |                | hours. The     |
|                |                |                | valid values   |
|                |                |                | are 0 to 11.   |
|                |                |                | For example,   |
|                |                |                | for the        |
|                |                |                | secondary side |
|                |                |                | end of a       |
|                |                |                | transformer    |
|                |                |                | with vector    |
|                |                |                | group code of  |
|                |                |                | \'Dyn11\',     |
|                |                |                | specify the    |
|                |                |                | connection     |
|                |                |                | kind as wye    |
|                |                |                | with neutral   |
|                |                |                | and specify    |
|                |                |                | the phase      |
|                |                |                | angle of the   |
|                |                |                | clock as 11.   |
|                |                |                | The clock      |
|                |                |                | value of the   |
|                |                |                | transformer    |
|                |                |                | end number     |
|                |                |                | specified as   |
|                |                |                | 1, is assumed  |
|                |                |                | to be zero.    |
|                |                |                | Note the       |
|                |                |                | transformer    |
|                |                |                | end number is  |
|                |                |                | not assumed to |
|                |                |                | be the same as |
|                |                |                | the terminal   |
|                |                |                | sequence       |
|                |                |                | number.        |
+----------------+----------------+----------------+----------------+
| ratedS         | 1..1           | [Appar         | Normal         |
|                |                | entPower       | apparent power |
|                |                | \<#App         | rating.        |
|                |                | a              |                |
|                |                | rentPower\>]{. | The attribute  |
|                |                | title-ref}\_\_ | shall be a     |
|                |                |                | positive       |
|                |                |                | value. For a   |
|                |                |                | two-winding    |
|                |                |                | transformer    |
|                |                |                | the values for |
|                |                |                | the high and   |
|                |                |                | low voltage    |
|                |                |                | sides shall be |
|                |                |                | identical.     |
+----------------+----------------+----------------+----------------+
| ratedU         | 1..1           | [Vol           | Rated voltage: |
|                |                | t              | phase-phase    |
|                |                | age](#Voltage) | for            |
|                |                |                | three-phase    |
|                |                |                | windings, and  |
|                |                |                | either         |
|                |                |                | phase-phase or |
|                |                |                | phase-neutral  |
|                |                |                | for            |
|                |                |                | single-phase   |
|                |                |                | windings.      |
|                |                |                |                |
|                |                |                | A high voltage |
|                |                |                | side, as given |
|                |                |                | by Transforme  |
|                |                |                | r              |
|                |                |                | End.endNumber, |
|                |                |                | shall have a   |
|                |                |                | ratedU that is |
|                |                |                | greater than   |
|                |                |                | or equal to    |
|                |                |                | ratedU for the |
|                |                |                | lower voltage  |
|                |                |                | sides.         |
|                |                |                |                |
|                |                |                | The attribute  |
|                |                |                | shall be a     |
|                |                |                | positive       |
|                |                |                | value.         |
+----------------+----------------+----------------+----------------+
| P o            | 1..1           | [PowerT        | The power      |
| werTransformer |                | ransform er    | transformer of |
|                |                | \<#Po%20werT   | this power     |
|                |                | r              | transformer    |
|                |                | ansformer\>]{. | end.           |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  mRID          1..1   [String](#String)      see [ TransformerEnd \<#Tra
                                              nsformerEnd.mRID\>]{.title-ref}\_\_

  endNumber     1..1   [I nteger](#Integer)   see [Trans formerEnd \<#Transfor
                                              merEnd.endNumber\>]{.title-ref}\_\_

  grounded      1..1   [B oolean](#Boolean)   see [Tran sformerEnd \<#Transfo
                                              rmerEnd.grounded\>]{.title-ref}\_\_

  name          1..1   [String](#String)      see [ TransformerEnd \<#Tra
                                              nsformerEnd.name\>]{.title-ref}\_\_

  rground       1..1   [Resista               see [Tra nsformerEnd \<#Transf
                       nce](#Resistance)      ormerEnd.rground\>]{.title-ref}\_\_

  xground       1..1   [React                 see [Tra nsformerEnd \<#Transf
                       ance](#Reactance)      ormerEnd.xground\>]{.title-ref}\_\_

  BaseVoltage   1..1   [BaseVolta             see [Transfo rmerEnd \<#Transforme
                       ge](#BaseVoltage)      rEnd.BaseVoltage\>]{.title-ref}\_\_

  Terminal      1..1   [Ter minal](#Terminal) see [Tran sformerEnd \<#Transfo
                                              rmerEnd.Terminal\>]{.title-ref}\_\_
  ------------- ------ ---------------------- -------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#RatioTapChanger .container .group}
[#RatioTapChanger](#RatioTapChanger)

**RatioTapChanger**

Wires

A tap changer that changes the voltage ratio impacting the voltage
magnitude but not the phase angle across the transformer.

Angle sign convention (general): Positive value indicates a positive
phase shift from the winding where the tap is located to the other
winding (for a two-winding transformer).

**Native Members**

+----------------+----------------+----------------+----------------+
| stepV o        | 1..1           | [Per           | Tap step       |
| ltageIncrement |                | C              | increment, in  |
|                |                | ent](#PerCent) | per cent of    |
|                |                |                | rated voltage  |
|                |                |                | of the power   |
|                |                |                | transformer    |
|                |                |                | end, per step  |
|                |                |                | position.      |
|                |                |                |                |
|                |                |                | When the       |
|                |                |                | increment is   |
|                |                |                | negative, the  |
|                |                |                | voltage        |
|                |                |                | decreases when |
|                |                |                | the tap step   |
|                |                |                | increases.     |
+----------------+----------------+----------------+----------------+
| TransformerEnd | 1..1           | [Tr ansforme   | Transformer    |
|                |                | rEnd           | end to which   |
|                |                | \<#%20Tran     | this ratio tap |
|                |                | s              | changer        |
|                |                | formerEnd\>]{. | belongs.       |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  highStep      0..1   [I nteger](#Integer)   see [TapChanger \<#Tap
                                              Changer.highStep\>]{.title-ref}\_\_

  lowStep       0..1   [I nteger](#Integer)   see [TapChanger \<#Ta
                                              pChanger.lowStep\>]{.title-ref}\_\_

  neutralStep   0..1   [I nteger](#Integer)   see [TapChanger \<#TapCha
                                              nger.neutralStep\>]{.title-ref}\_\_

  neutralU      0..1   [V oltage](#Voltage)   see [TapChanger \<#Tap
                                              Changer.neutralU\>]{.title-ref}\_\_

  normalStep    0..1   [I nteger](#Integer)   see [TapChanger \<#TapCh
                                              anger.normalStep\>]{.title-ref}\_\_

  step          1..1   [Float](#Float)        see [TapChanger \<
                                              #TapChanger.step\>]{.title-ref}\_\_
  ------------- ------ ---------------------- -------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#RotatingMachinePlant .container .group}
[#RotatingMachinePlant](#RotatingMachinePlant)

**RotatingMachinePlant**

Emtiop

A conventional generating plant, e.g., SynchronousMachine with
associated controls and GeneratingUnit, a PowerTransformer, and a
DisconnectingCircuitBreaker for thermal and hydro plants.

**Inherited Members**

  ---------------- -------------- ------------------------------- -------------------------------
  ACPointOf        0..1           [ACPointOfCo mmonCoupling \<    see [Connected Facility \<#Con
  CommonCoupling                  #ACPointOfComm                  nectedFacility .ACPointOfComm
                                  onCoupling\>]{.title-ref}\_\_   onCoupling\>]{.title-ref}\_\_

  Equipments       0..unbounded   [Equipment \<                   see [ConnectedF acility \<#Conn
                                  #Equipment\>]{.title-ref}\_\_   ectedFacility.
                                                                  Equipments\>]{.title-ref}\_\_
  ---------------- -------------- ------------------------------- -------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#SeriesCompensator .container .group}
[#SeriesCompensator](#SeriesCompensator)

**SeriesCompensator**

Wires

A Series Compensator is a series capacitor or reactor or an AC
transmission line without charging susceptance. It is a two terminal
device.

**Native Members**

  ---- ------ --------------------------- -------------------------------
  r    1..1   [Resistance](#Resistance)   Positive sequence resistance.
  r0   1..1   [Resistance](#Resistance)   Zero sequence resistance.
  x    1..1   [Reactance](#Reactance)     Positive sequence reactance.
  x0   1..1   [Reactance](#Reactance)     Zero sequence reactance.
  ---- ------ --------------------------- -------------------------------

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#StaticVarCompensator .container .group}
[#StaticVarCompensator](#StaticVarCompensator)

**StaticVarCompensator**

FACTS

A facility for providing variable and controllable shunt reactive power.
The SVC typically consists of a stepdown transformer, filter,
thyristor-controlled reactor, and thyristor-switched capacitor arms.

The SVC may operate in fixed MVar output mode or in voltage control
mode. When in voltage control mode, the output of the SVC will be
proportional to the deviation of voltage at the controlled bus from the
voltage setpoint. The SVC characteristic slope defines the proportion.
If the voltage at the controlled bus is equal to the voltage setpoint,
the SVC MVar output is zero.

**Native Members**

+----------------+----------------+----------------+----------------+
| c a            | 0..1           | [Reactan ce \< | Capacitive     |
| pacitiveRating |                | #              | reactance at   |
|                |                | Reactance\>]{. | maximum        |
|                |                | title-ref}\_\_ | capacitive     |
|                |                |                | reactive       |
|                |                |                | power. Shall   |
|                |                |                | always be      |
|                |                |                | positive.      |
+----------------+----------------+----------------+----------------+
| i              | 0..1           | [Reactan ce \< | Inductive      |
| nductiveRating |                | #              | reactance at   |
|                |                | Reactance\>]{. | maximum        |
|                |                | title-ref}\_\_ | inductive      |
|                |                |                | reactive       |
|                |                |                | power. Shall   |
|                |                |                | always be      |
|                |                |                | negative.      |
+----------------+----------------+----------------+----------------+
| q              | 0..1           | [React         | Reactive power |
|                |                | ivePower       | injection.     |
|                |                | \<#Rea         | Load sign      |
|                |                | c              | convention is  |
|                |                | tivePower\>]{. | used, i.e.     |
|                |                | title-ref}\_\_ | positive sign  |
|                |                |                | means flow out |
|                |                |                | from a node.   |
|                |                |                |                |
|                |                |                | Starting value |
|                |                |                | for a steady   |
|                |                |                | state          |
|                |                |                | solution.      |
+----------------+----------------+----------------+----------------+
| slope          | 0..1           | [Volta g       | The c          |
|                |                | ePerReactivePo | haracteristics |
|                |                | wer \<#Vo      | slope of an    |
|                |                | ltagePe%20rRea | SVC defines    |
|                |                | c              | how the        |
|                |                | tivePower\>]{. | reactive power |
|                |                | title-ref}\_\_ | output changes |
|                |                |                | in proportion  |
|                |                |                | to the         |
|                |                |                | difference     |
|                |                |                | between the    |
|                |                |                | regulated bus  |
|                |                |                | voltage and    |
|                |                |                | the voltage    |
|                |                |                | setpoint.      |
|                |                |                |                |
|                |                |                | The attribute  |
|                |                |                | shall be a     |
|                |                |                | positive value |
|                |                |                | or zero.       |
+----------------+----------------+----------------+----------------+
| sVCControlMode | 0..1           | [SV CControl   | SVC control    |
|                |                | Mode           | mode.          |
|                |                | \<#%20SVCC     |                |
|                |                | o              |                |
|                |                | ntrolMode\>]{. |                |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+
| v              | 0..1           | [Vol           | The reactive   |
| oltageSetPoint |                | t              | power output   |
|                |                | age](#Voltage) | of the SVC is  |
|                |                |                | proportional   |
|                |                |                | to the         |
|                |                |                | difference     |
|                |                |                | between the    |
|                |                |                | voltage at the |
|                |                |                | regulated bus  |
|                |                |                | and the        |
|                |                |                | voltage        |
|                |                |                | setpoint. When |
|                |                |                | the regulated  |
|                |                |                | bus voltage is |
|                |                |                | equal to the   |
|                |                |                | voltage        |
|                |                |                | setpoint, the  |
|                |                |                | reactive power |
|                |                |                | output is      |
|                |                |                | zero.          |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#SvDCPowerFlow .container .group}
[#SvDCPowerFlow](#SvDCPowerFlow)

**SvDCPowerFlow**

StateVariables

State variable for power flow. Load convention is used for flow
direction. This means flow out from the DCTopologicalNode into the
equipment is positive.

**Native Members**

  ------------ ------ ----------------------- -----------------------
  p            0..1   [ActivePo               The active power flow.
                      wer](#ActivePower)      Load sign convention is
                                              used, i.e. positive
                                              sign means flow out
                                              from a
                                              DCTopologicalNode (bus)
                                              into the conducting
                                              equipment.

  DCTerminal   0..1   [DCTerm                 The DC terminal
                      inal](#DCTerminal)      associated with the DC
                                              power flow state
                                              variable.
  ------------ ------ ----------------------- -----------------------

**Inherited Members**
:::

::: {#SvDCVoltage .container .group}
[#SvDCVoltage](#SvDCVoltage)

**SvDCVoltage**

StateVariables

State variable for direct current voltage.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  v                   0..1   [Volt age](#Voltage)               State variable for
                                                                direct current
                                                                voltage.

  DCTopologicalNode   0..1   [DCTopol ogicalNode \<#DCTo        The DC topological
                             pologicalNode\>]{.title-ref}\_\_   node associated
                                                                with the DC voltage
                                                                state.
  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**
:::

::: {#SvPowerFlow .container .group}
[#SvPowerFlow](#SvPowerFlow)

**SvPowerFlow**

StateVariables

State variable for power flow. Load convention is used for flow
direction. This means flow out from the TopologicalNode into the
equipment is positive.

**Native Members**

  ---------- ------ ------------------------ ------------------------
  p          0..1   [ActiveP                 The active power flow.
                    ower](#ActivePower)      Load sign convention is
                                             used, i.e. positive sign
                                             means flow out from a
                                             TopologicalNode (bus)
                                             into the conducting
                                             equipment.

  q          0..1   [ReactivePow             The reactive power flow.
                    er](#ReactivePower)      Load sign convention is
                                             used, i.e. positive sign
                                             means flow out from a
                                             TopologicalNode (bus)
                                             into the conducting
                                             equipment.

  Terminal   0..1   [T erminal](#Terminal)   The terminal associated
                                             with the power flow
                                             state variable.
  ---------- ------ ------------------------ ------------------------

**Inherited Members**
:::

::: {#SvShuntCompensatorSections .container .group}
[#SvShuntCompensatorSections](#SvShuntCompensatorSections)

**SvShuntCompensatorSections**

StateVariables

State variable for the number of sections in service for a shunt
compensator.

**Native Members**

  ------------------ ------ ---------------------------------- -------------------
  phase              0..1   [Sin glePhaseKind \<#Si            The terminal phase
                            nglePhaseKind\>]{.title-ref}\_\_   at which the
                                                               connection is
                                                               applied. If
                                                               missing, the
                                                               injection is
                                                               assumed to be
                                                               balanced among
                                                               non-neutral phases.

  sections           0..1   [Float](#Float)                    The number of
                                                               sections in service
                                                               as a continuous
                                                               variable. The
                                                               attribute shall be
                                                               a positive value or
                                                               zero. To get
                                                               integer value scale
                                                               with ShuntCompens
                                                               ator.bPerSection.

  ShuntCompensator   0..1   [Shunt Compensator \<#Shu          The shunt
                            ntCompensator\>]{.title-ref}\_\_   compensator for
                                                               which the state
                                                               applies.
  ------------------ ------ ---------------------------------- -------------------

**Inherited Members**
:::

::: {#SvStatus .container .group}
[#SvStatus](#SvStatus)

**SvStatus**

StateVariables

State variable for status.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  inService           0..1   [Bool ean](#Boolean)               The in service
                                                                status as a result
                                                                of topology
                                                                processing. It
                                                                indicates if the
                                                                equipment is
                                                                considered as
                                                                energized by the
                                                                power flow. It
                                                                reflects if the
                                                                equipment is
                                                                connected within a
                                                                solvable island. It
                                                                does not
                                                                necessarily reflect
                                                                whether or not the
                                                                island was solved
                                                                by the power flow.

  phase               0..1   [Sin glePhaseKind \<#Si            The individual
                             nglePhaseKind\>]{.title-ref}\_\_   phase status. If
                                                                the attribute is
                                                                unspecified, then
                                                                three phase model
                                                                is assumed.

  Co                  0..1   [ConductingE quipment \<#Conduc    The conducting
  nductingEquipment          tingEquipment\>]{.title-ref}\_\_   equipment
                                                                associated with the
                                                                status state
                                                                variable.
  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**
:::

::: {#SvSwitch .container .group}
[#SvSwitch](#SvSwitch)

**SvSwitch**

StateVariables

State variable for switch.

**Native Members**

  -------- ------ ------------------------- -------------------------
  open     0..1   [Boolean](#Boolean)       The attribute tells if
                                            the computed state of the
                                            switch is considered
                                            open.

  phase    0..1   [SinglePhaseKin           The terminal phase at
                  d](#SinglePhaseKind)      which the connection is
                                            applied. If missing, the
                                            injection is assumed to
                                            be balanced among
                                            non-neutral phases.

  Switch   0..1   [Switch](#Switch)         The switch associated
                                            with the switch state.
  -------- ------ ------------------------- -------------------------

**Inherited Members**
:::

::: {#SvTapStep .container .group}
[#SvTapStep](#SvTapStep)

**SvTapStep**

StateVariables

State variable for transformer tap step.

**Native Members**

  ------------ ------ ----------------------- -----------------------
  position     0..1   [Float](#Float)         The floating point tap
                                              position. This is not
                                              the tap ratio, but
                                              rather the tap step
                                              position as defined by
                                              the related tap changer
                                              model and normally is
                                              constrained to be
                                              within the range of
                                              minimum and maximum tap
                                              positions.

  TapChanger   0..1   [TapCha                 The tap changer
                      nger](#TapChanger)      associated with the tap
                                              step state.
  ------------ ------ ----------------------- -----------------------

**Inherited Members**
:::

::: {#SvVoltage .container .group}
[#SvVoltage](#SvVoltage)

**SvVoltage**

StateVariables

State variable for voltage.

**Native Members**

  ----------------- ------ ---------------------------------- -------------------
  angle             0..1   [AngleDegrees \<                   The voltage angle
                           #AngleDegrees\>]{.title-ref}\_\_   of the topological
                                                              node complex
                                                              voltage with
                                                              respect to system
                                                              reference.

  v                 0..1   [Volt age](#Voltage)               The voltage
                                                              magnitude at the
                                                              topological node.
                                                              The attribute shall
                                                              be a positive
                                                              value.

  TopologicalNode   0..1   [Top ologicalNode \<#To            The topological
                           pologicalNode\>]{.title-ref}\_\_   node associated
                                                              with the voltage
                                                              state.
  ----------------- ------ ---------------------------------- -------------------

**Inherited Members**
:::

::: {#SynchronousMachine .container .group}
[#SynchronousMachine](#SynchronousMachine)

**SynchronousMachine**

Wires

An electromechanical device that operates with shaft rotating
synchronously with the network. It is a single machine operating either
as a generator or synchronous condenser or pump.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  earthing            1..1   [Bool ean](#Boolean)               Indicates whether
                                                                or not the
                                                                generator is
                                                                earthed. Used for
                                                                short circuit data
                                                                exchange according
                                                                to IEC 60909.

  e arthingStarPointR 1..1   [Resistance](#Resistance)          Generator star
                                                                point earthing
                                                                resistance (Re).
                                                                Used for short
                                                                circuit data
                                                                exchange according
                                                                to IEC 60909.

  e arthingStarPointX 1..1   [Reactanc e](#Reactance)           Generator star
                                                                point earthing
                                                                reactance (Xe).
                                                                Used for short
                                                                circuit data
                                                                exchange according
                                                                to IEC 60909.

  maxQ                1..1   [ReactivePower \<#                 Maximum reactive
                             ReactivePower\>]{.title-ref}\_\_   power limit. This
                                                                is the maximum
                                                                (nameplate) limit
                                                                for the unit.

  minQ                1..1   [ReactivePower \<#                 Minimum reactive
                             ReactivePower\>]{.title-ref}\_\_   power limit for the
                                                                unit.

  operatingMode       1..1   [S ynchronousMachine OperatingMode Current mode of
                             \<#S ynchronousMachine             operation.
                             OperatingMode\>]{.title-ref}\_\_   

  type                1..1   [ SynchronousMachin eKind          Modes that this
                             \<#Synchrono                       synchronous machine
                             usMachineKind\>]{.title-ref}\_\_   can operate in.
  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**

  ---------------- ------ ---------------------------------- ----------------------------------
  p                1..1   [ActivePower](#ActivePower)        see [Rotat ingMachine \<#Rota
                                                             tingMachine.p\>]{.title-ref}\_\_

  q                1..1   [ReactivePower \<#                 see [Rotat ingMachine \<#Rota
                          ReactivePower\>]{.title-ref}\_\_   tingMachine.q\>]{.title-ref}\_\_

  ratedS           1..1   [ApparentPower \<#                 see [RotatingMa chine \<#RotatingM
                          ApparentPower\>]{.title-ref}\_\_   achine.ratedS\>]{.title-ref}\_\_

  ratedU           1..1   [Volt age](#Voltage)               see [RotatingMa chine \<#RotatingM
                                                             achine.ratedU\>]{.title-ref}\_\_

  GeneratingUnit   1..1   [G eneratingUnit \<#G              see [R otatingMachine \<#
                          eneratingUnit\>]{.title-ref}\_\_   RotatingMachine.G
                                                             eneratingUnit\>]{.title-ref}\_\_
  ---------------- ------ ---------------------------------- ----------------------------------

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#SynchronousMachineSimplified .container .group}
[#SynchronousMachineSimplified](#SynchronousMachineSimplified)

**SynchronousMachineSimplified**

SynchronousMachineDynamics

The simplified model represents a synchronous generator as a constant
internal voltage behind an impedance (*Rs + jXp*) as shown in the
Simplified diagram.

Since internal voltage is held constant, there is no *Efd* input and any
excitation system model will be ignored. There is also no *Ifd* output.

This model should not be used for representing a real generator except,
perhaps, small generators whose response is insignificant.

The parameters used for the simplified model include:

-   RotatingMachineDynamics.damping (*D*);
-   RotatingMachineDynamics.inertia (*H*);

\- RotatingMachineDynamics.statorLeakageReactance (used to exchange
*jXp* for SynchronousMachineSimplified);

-   RotatingMachineDynamics.statorResistance (*Rs*).

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  S ynchronousMachine 0..1   [Synchrono usMachine \<#Synch      see [Synchronou sMachineDynamics
                             ronousMachine\>]{.title-ref}\_\_   \<#SynchronousMach
                                                                ineDynamics.Synch
                                                                ronousMachine\>]{.title-ref}\_\_

  ------------------- ------ ---------------------------------- ----------------------------------

  ------------------- ------ ------------------- ----------------------------------
  damping             1..1   [Float](#Float)     see [RotatingMa chineDynamics \<#R
                                                 otatingMachineDyn
                                                 amics.damping\>]{.title-ref}\_\_

  inertia             1..1   [Seco               see [RotatingMa chineDynamics \<#R
                             nds](#Seconds)      otatingMachineDyn
                                                 amics.inertia\>]{.title-ref}\_\_

  stato               1..1   [PU](#PU)           see [Rotating MachineDynamics \<
  rLeakageReactance                              #RotatingMachineD
                                                 ynamics.statorLea
                                                 kageReactance\>]{.title-ref}\_\_

  statorResistance    1..1   [PU](#PU)           see [Ro tatingMachineDyna mics
                                                 \<#RotatingMa chineDynamics.sta
                                                 torResistance\>]{.title-ref}\_\_
  ------------------- ------ ------------------- ----------------------------------

  --------- ------ ------------------------ ---------------------------------------
  mRID      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.mRID\>]{.title-ref}\_\_

  enabled   1..1   [Boolean](#Boolean)      see [DynamicsFunct ionBlock
                                            \<#DynamicsFun
                                            ctionBlock.enabled\>]{.title-ref}\_\_

  name      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.name\>]{.title-ref}\_\_
  --------- ------ ------------------------ ---------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#SynchronousMachineTimeConstantReactance .container .group}
[#SynchronousMachineTimeConstantReactance](#SynchronousMachineTimeConstantReactance)

**SynchronousMachineTimeConstantReactance**

SynchronousMachineDynamics

Synchronous machine detailed modelling types are defined by the
combination of the attributes
SynchronousMachineTimeConstantReactance.modelType and
SynchronousMachineTimeConstantReactance.rotorType.

Parameter details:

1.  The "p" in the time-related attribute names is a substitution for a
    "prime" in the usual parameter notation, e.g. tpdo refers to
    *T\'do*.

**Native Members**

+----------------+----------------+----------------+----------------+
| ks             | 1..1           | [Flo           | Saturation     |
|                |                | at](#Float)    | loading        |
|                |                |                | correction     |
|                |                |                | factor (*Ks*)  |
|                |                |                | (\>= 0). Used  |
|                |                |                | only by type J |
|                |                |                | model. Typical |
|                |                |                | value = 0.     |
+----------------+----------------+----------------+----------------+
| modelType      | 1..1           | \              | Type of        |
|                |                | [SynchronousMa | synchronous    |
|                |                | c              | machine model  |
|                |                | h              | used in        |
|                |                | ineModelKind\] | dynamic        |
|                |                | (              | simulation     |
|                |                | #SynchronousMa | applications.  |
|                |                | c              |                |
|                |                | hineModelKind) |                |
+----------------+----------------+----------------+----------------+
| rotorType      | 1..1           | [RotorKi nd \< | Type of rotor  |
|                |                | #              | on physical    |
|                |                | RotorKind\>]{. | machine.       |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+
| tc             | 1..1           | [Sec           | Damping time   |
|                |                | o              | constant for   |
|                |                | nds](#Seconds) | "Canay"        |
|                |                |                | reactance (\>= |
|                |                |                | 0). Typical    |
|                |                |                | value = 0.     |
+----------------+----------------+----------------+----------------+
| tpdo           | 1..1           | [Sec           | Direct-axis    |
|                |                | o              | transient      |
|                |                | nds](#Seconds) | rotor time     |
|                |                |                | constant       |
|                |                |                | (*T\'do*) (\>  |
|                |                |                | Sy n           |
|                |                |                | chronousMachin |
|                |                |                | e              |
|                |                |                | TimeConstantRe |
|                |                |                | a              |
|                |                |                | ctance.tppdo). |
|                |                |                | Typical value  |
|                |                |                | = 5.           |
+----------------+----------------+----------------+----------------+
| tppdo          | 1..1           | [Sec           | Direct-axis    |
|                |                | o              | subtransient   |
|                |                | nds](#Seconds) | rotor time     |
|                |                |                | constant       |
|                |                |                | (*T\'\'do*)    |
|                |                |                | (\> 0).        |
|                |                |                | Typical value  |
|                |                |                | = 0,03.        |
+----------------+----------------+----------------+----------------+
| tppqo          | 1..1           | [Sec           | Q              |
|                |                | o              | uadrature-axis |
|                |                | nds](#Seconds) | subtransient   |
|                |                |                | rotor time     |
|                |                |                | constant       |
|                |                |                | (*T\'\'qo*)    |
|                |                |                | (\> 0).        |
|                |                |                | Typical value  |
|                |                |                | = 0,03.        |
+----------------+----------------+----------------+----------------+
| tpqo           | 1..1           | [Sec           | Q              |
|                |                | o              | uadrature-axis |
|                |                | nds](#Seconds) | transient      |
|                |                |                | rotor time     |
|                |                |                | constant       |
|                |                |                | (*T\'qo*) (\>  |
|                |                |                | Sy n           |
|                |                |                | chronousMachin |
|                |                |                | e              |
|                |                |                | TimeConstantRe |
|                |                |                | a              |
|                |                |                | ctance.tppqo). |
|                |                |                | Typical value  |
|                |                |                | = 0,5.         |
+----------------+----------------+----------------+----------------+
| x              | 1..1           | [PU](#PU)      | Direct-axis    |
| DirectSubtrans |                |                | subtransient   |
|                |                |                | reactance      |
|                |                |                | (unsaturated)  |
|                |                |                | (*X\'\'d*) (\> |
|                |                |                | Rot a          |
|                |                |                | tingMachineDyn |
|                |                |                | a              |
|                |                |                | mics.statorLea |
|                |                |                | k              |
|                |                |                | ageReactance). |
|                |                |                | Typical value  |
|                |                |                | = 0,2.         |
+----------------+----------------+----------------+----------------+
| xDirectSync    | 1..1           | [PU](#PU)      | Direct-axis    |
|                |                |                | synchronous    |
|                |                |                | reactance      |
|                |                |                | (*Xd*) (\>=    |
|                |                |                | Synchrono u    |
|                |                |                | sMachineTimeCo |
|                |                |                | n              |
|                |                |                | stantReactance |
|                |                |                | .              |
|                |                |                | xDirectTrans). |
|                |                |                | The quotient   |
|                |                |                | of a sustained |
|                |                |                | value of that  |
|                |                |                | AC component   |
|                |                |                | of armature    |
|                |                |                | voltage that   |
|                |                |                | is produced by |
|                |                |                | the total      |
|                |                |                | direct-axis    |
|                |                |                | flux due to    |
|                |                |                | direct-axis    |
|                |                |                | armature       |
|                |                |                | current and    |
|                |                |                | the value of   |
|                |                |                | the AC         |
|                |                |                | component of   |
|                |                |                | this current,  |
|                |                |                | the machine    |
|                |                |                | running at     |
|                |                |                | rated speed.   |
|                |                |                | Typical value  |
|                |                |                | = 1,8.         |
+----------------+----------------+----------------+----------------+
| xDirectTrans   | 1..1           | [PU](#PU)      | Direct-axis    |
|                |                |                | transient      |
|                |                |                | reactance      |
|                |                |                | (unsaturated)  |
|                |                |                | (*X\'d*) (\>=  |
|                |                |                | SynchronousM a |
|                |                |                | chineTimeConst |
|                |                |                | a              |
|                |                |                | ntReactance.xD |
|                |                |                | i              |
|                |                |                | rectSubtrans). |
|                |                |                | Typical value  |
|                |                |                | = 0,5.         |
+----------------+----------------+----------------+----------------+
| xQuadSubtrans  | 1..1           | [PU](#PU)      | Q              |
|                |                |                | uadrature-axis |
|                |                |                | subtransient   |
|                |                |                | reactance      |
|                |                |                | (*X\'\'q*) (\> |
|                |                |                | Rot a          |
|                |                |                | tingMachineDyn |
|                |                |                | a              |
|                |                |                | mics.statorLea |
|                |                |                | k              |
|                |                |                | ageReactance). |
|                |                |                | Typical value  |
|                |                |                | = 0,2.         |
+----------------+----------------+----------------+----------------+
| xQuadSync      | 1..1           | [PU](#PU)      | Q              |
|                |                |                | uadrature-axis |
|                |                |                | synchronous    |
|                |                |                | reactance      |
|                |                |                | (*Xq*) (\>=    |
|                |                |                | Synchro n      |
|                |                |                | ousMachineTime |
|                |                |                | C              |
|                |                |                | onstantReactan |
|                |                |                | c              |
|                |                |                | e.xQuadTrans). |
|                |                |                |                |
|                |                |                | The ratio of   |
|                |                |                | the component  |
|                |                |                | of reactive    |
|                |                |                | armature       |
|                |                |                | voltage, due   |
|                |                |                | to the q       |
|                |                |                | uadrature-axis |
|                |                |                | component of   |
|                |                |                | armature       |
|                |                |                | current, to    |
|                |                |                | this component |
|                |                |                | of current,    |
|                |                |                | under steady   |
|                |                |                | state          |
|                |                |                | conditions and |
|                |                |                | at rated       |
|                |                |                | frequency.     |
|                |                |                | Typical value  |
|                |                |                | = 1,6.         |
+----------------+----------------+----------------+----------------+
| xQuadTrans     | 1..1           | [PU](#PU)      | Q              |
|                |                |                | uadrature-axis |
|                |                |                | transient      |
|                |                |                | reactance      |
|                |                |                | (*X\'q*) (\>=  |
|                |                |                | Synchronou s   |
|                |                |                | MachineTimeCon |
|                |                |                | s              |
|                |                |                | tantReactance. |
|                |                |                | x              |
|                |                |                | QuadSubtrans). |
|                |                |                | Typical value  |
|                |                |                | = 0,3.         |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------------------- ------ ----------------------------- ----------------------------------
  efdBaseRatio        1..1   [Float](#Float)               see [Sync hronousMachineDet ailed
                                                           \<#Synchrono usMachineDetailed
                                                           .efdBaseRatio\>]{.title-ref}\_\_

  ifdBaseType         1..1   [IfdBaseKind](#IfdBaseKind)   see [Syn chronousMachineDe tailed
                                                           \<#Synchron ousMachineDetaile
                                                           d.ifdBaseType\>]{.title-ref}\_\_

  saturationFactor    1..1   [Float](#Float)               see [Synchron ousMachineDetaile d
                                                           \<#SynchronousMa chineDetailed.sat
                                                           urationFactor\>]{.title-ref}\_\_

  sa                  1..1   [Float](#Float)               see [Synchronous MachineDetailed
  turationFactor120                                        \< #SynchronousMachi
                                                           neDetailed.satura
                                                           tionFactor120\>]{.title-ref}\_\_

  saturat             1..1   [Float](#Float)               see [SynchronousMachi neDetailed
  ionFactor120QAxis                                        \<#Sync hronousMachineDet
                                                           ailed.saturationF
                                                           actor120QAxis\>]{.title-ref}\_\_

  satu                1..1   [Float](#Float)               see [SynchronousMa chineDetailed
  rationFactorQAxis                                        \<#S ynchronousMachine
                                                           Detailed.saturati
                                                           onFactorQAxis\>]{.title-ref}\_\_
  ------------------- ------ ----------------------------- ----------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  S ynchronousMachine 0..1   [Synchrono usMachine \<#Synch      see [Synchronou sMachineDynamics
                             ronousMachine\>]{.title-ref}\_\_   \<#SynchronousMach
                                                                ineDynamics.Synch
                                                                ronousMachine\>]{.title-ref}\_\_

  ------------------- ------ ---------------------------------- ----------------------------------

  ------------------- ------ ------------------- ----------------------------------
  damping             1..1   [Float](#Float)     see [RotatingMa chineDynamics \<#R
                                                 otatingMachineDyn
                                                 amics.damping\>]{.title-ref}\_\_

  inertia             1..1   [Seco               see [RotatingMa chineDynamics \<#R
                             nds](#Seconds)      otatingMachineDyn
                                                 amics.inertia\>]{.title-ref}\_\_

  stato               1..1   [PU](#PU)           see [Rotating MachineDynamics \<
  rLeakageReactance                              #RotatingMachineD
                                                 ynamics.statorLea
                                                 kageReactance\>]{.title-ref}\_\_

  statorResistance    1..1   [PU](#PU)           see [Ro tatingMachineDyna mics
                                                 \<#RotatingMa chineDynamics.sta
                                                 torResistance\>]{.title-ref}\_\_
  ------------------- ------ ------------------- ----------------------------------

  --------- ------ ------------------------ ---------------------------------------
  mRID      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.mRID\>]{.title-ref}\_\_

  enabled   1..1   [Boolean](#Boolean)      see [DynamicsFunct ionBlock
                                            \<#DynamicsFun
                                            ctionBlock.enabled\>]{.title-ref}\_\_

  name      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.name\>]{.title-ref}\_\_
  --------- ------ ------------------------ ---------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#Terminal .container .group}
[#Terminal](#Terminal)

**Terminal**

Core

An AC electrical connection point to a piece of conducting equipment.
Terminals are connected at physical connection points called
connectivity nodes.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  Co                  1..1   [ConductingE quipment \<#Conduc    The conducting
  nductingEquipment          tingEquipment\>]{.title-ref}\_\_   equipment of the
                                                                terminal.
                                                                Conducting
                                                                equipment have
                                                                terminals that may
                                                                be connected to
                                                                other conducting
                                                                equipment terminals
                                                                via connectivity
                                                                nodes or
                                                                topological nodes.

  ConnectivityNode    1..1   [Conne ctivityNode \<#Con          The connectivity
                             nectivityNode\>]{.title-ref}\_\_   node to which this
                                                                terminal connects
                                                                with zero
                                                                impedance.
  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**

  ---------------- ------ ------------------- ----------------------------------
  sequenceNumber   1..1   [Inte               see [ACDCTerminal
                          ger](#Integer)      \<#ACDCTerminal.s
                                              equenceNumber\>]{.title-ref}\_\_

  ---------------- ------ ------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#TextDiagramObject .container .group}
[#TextDiagramObject](#TextDiagramObject)

**TextDiagramObject**

DiagramLayout

A diagram object for placing free-text or text derived from an
associated domain object.

**Native Members**

  ------ ------ ---------------------- --------------------------
  text   1..1   [String](#String)      The text that is displayed
                                       by this text diagram
                                       object.

  ------ ------ ---------------------- --------------------------

**Inherited Members**

  ------------------ ------ ---------------------------------- ----------------------------------
  mRID               1..1   [St ring](#String)                 see [Diag ramObject \<#Diagr
                                                               amObject.mRID\>]{.title-ref}\_\_

  drawingOrder       1..1   [Inte ger](#Integer)               see [DiagramObjec t
                                                               \<#DiagramObject
                                                               .drawingOrder\>]{.title-ref}\_\_

  isPolygon          1..1   [Bool ean](#Boolean)               see [DiagramOb ject \<#DiagramObj
                                                               ect.isPolygon\>]{.title-ref}\_\_

  name               1..1   [St ring](#String)                 see [Diag ramObject \<#Diagr
                                                               amObject.name\>]{.title-ref}\_\_

  IdentifiedObject   1..1   [Ident ifiedObject \<#Ide          see [DiagramObject \<#
                            ntifiedObject\>]{.title-ref}\_\_   DiagramObject.Ide
                                                               ntifiedObject\>]{.title-ref}\_\_
  ------------------ ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#ThermalGeneratingUnit .container .group}
[#ThermalGeneratingUnit](#ThermalGeneratingUnit)

**ThermalGeneratingUnit**

Production

A generating unit whose prime mover could be a steam turbine, combustion
turbine, or diesel engine.

**Inherited Members**

  --------------- ------ --------------------- ------------------------------------
  maxOperatingP   1..1   [ActivePowe           see [GeneratingU nit
                         r](#ActivePower)      \<#GeneratingUni
                                               t.maxOperatingP\>]{.title-ref}\_\_

  minOperatingP   1..1   [ActivePowe           see [GeneratingU nit
                         r](#ActivePower)      \<#GeneratingUni
                                               t.minOperatingP\>]{.title-ref}\_\_
  --------------- ------ --------------------- ------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#TopologicalNode .container .group}
[#TopologicalNode](#TopologicalNode)

**TopologicalNode**

Topology

For a detailed substation model a topological node is a set of
connectivity nodes that, in the current network state, are connected
together through any type of closed switches, including jumpers.
Topological nodes change as the current network state changes (i.e.,
switches, breakers, etc. change state).

For a planning model, switch statuses are not used to form topological
nodes. Instead they are manually created or deleted in a model builder
tool. Topological nodes maintained this way are also called \"busses\".

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#TransformerCoreAdmittance .container .group}
[#TransformerCoreAdmittance](#TransformerCoreAdmittance)

**TransformerCoreAdmittance**

Wires

The transformer core admittance. Used to specify the core admittance of
a transformer in a manner that can be shared among power transformers.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 1..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| b              | 1..1           | [S usceptance  | Magnetizing    |
|                |                | \<#S           | branch         |
|                |                | u              | susceptance (B |
|                |                | sceptance\>]{. | mag). The      |
|                |                | title-ref}\_\_ | value can be   |
|                |                |                | positive or    |
|                |                |                | negative.      |
+----------------+----------------+----------------+----------------+
| b0             | 1..1           | [S usceptance  | Zero sequence  |
|                |                | \<#S           | magnetizing    |
|                |                | u              | branch         |
|                |                | sceptance\>]{. | susceptance.   |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+
| g              | 1..1           | [C onductance  | Magnetizing    |
|                |                | \<#C           | branch         |
|                |                | o              | conductance (G |
|                |                | nductance\>]{. | mag).          |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+
| g0             | 1..1           | [C onductance  | Zero sequence  |
|                |                | \<#C           | magnetizing    |
|                |                | o              | branch         |
|                |                | nductance\>]{. | conductance.   |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+
| name           | 1..1           | [S trin        | The name is    |
|                |                | g](#String)    | any free human |
|                |                |                | readable and   |
|                |                |                | possibly non   |
|                |                |                | unique text    |
|                |                |                | naming the     |
|                |                |                | object.        |
+----------------+----------------+----------------+----------------+
| TransformerEnd | 1..1           | [Tr ansforme   | All            |
|                |                | rEnd           | transformer    |
|                |                | \<#%20Tran     | ends having    |
|                |                | s              | this core      |
|                |                | formerEnd\>]{. | admittance.    |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#TransformerMeshImpedance .container .group}
[#TransformerMeshImpedance](#TransformerMeshImpedance)

**TransformerMeshImpedance**

Wires

Transformer mesh impedance (Delta-model) between transformer ends.

The typical case is that this class describes the impedance between two
transformer ends pair-wise, i.e. the cardinalities at both transformer
end associations are 1. However, in cases where two or more transformer
ends are modelled the cardinalities are larger than 1.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 1..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| name           | 1..1           | [S trin        | The name is    |
|                |                | g](#String)    | any free human |
|                |                |                | readable and   |
|                |                |                | possibly non   |
|                |                |                | unique text    |
|                |                |                | naming the     |
|                |                |                | object.        |
+----------------+----------------+----------------+----------------+
| r              | 1..1           | [Resistanc e   | Resistance     |
|                |                | \<#            | between the    |
|                |                | R              | \'from\' and   |
|                |                | esistance\>]{. | the \'to\'     |
|                |                | title-ref}\_\_ | end, seen from |
|                |                |                | the \'from\'   |
|                |                |                | end.           |
+----------------+----------------+----------------+----------------+
| r0             | 1..1           | [Resistanc e   | Zero-sequence  |
|                |                | \<#            | resistance     |
|                |                | R              | between the    |
|                |                | esistance\>]{. | \'from\' and   |
|                |                | title-ref}\_\_ | the \'to\'     |
|                |                |                | end, seen from |
|                |                |                | the \'from\'   |
|                |                |                | end.           |
+----------------+----------------+----------------+----------------+
| x              | 1..1           | [Reactan ce \< | Reactance      |
|                |                | #              | between the    |
|                |                | Reactance\>]{. | \'from\' and   |
|                |                | title-ref}\_\_ | the \'to\'     |
|                |                |                | end, seen from |
|                |                |                | the \'from\'   |
|                |                |                | end.           |
+----------------+----------------+----------------+----------------+
| x0             | 1..1           | [Reactan ce \< | Zero-sequence  |
|                |                | #              | reactance      |
|                |                | Reactance\>]{. | between the    |
|                |                | title-ref}\_\_ | \'from\' and   |
|                |                |                | the \'to\'     |
|                |                |                | end, seen from |
|                |                |                | the \'from\'   |
|                |                |                | end.           |
+----------------+----------------+----------------+----------------+
| Fro m          | 1..1           | [Tr ansforme   | From end this  |
| TransformerEnd |                | rEnd           | mesh impedance |
|                |                | \<#%20Tran     | is connected   |
|                |                | s              | to. It         |
|                |                | formerEnd\>]{. | determines the |
|                |                | title-ref}\_\_ | voltage        |
|                |                |                | reference.     |
+----------------+----------------+----------------+----------------+
| T o            | 1..\*          | [Tr ansforme   | All            |
| TransformerEnd |                | rEnd           | transformer    |
|                |                | \<#%20Tran     | ends this mesh |
|                |                | s              | impedance is   |
|                |                | formerEnd\>]{. | connected to.  |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#TransformerSaturationCurve .container .group}
[#TransformerSaturationCurve](#TransformerSaturationCurve)

**TransformerSaturationCurve**

Emtiop

Represents a piecewise linear transformer saturation characteristic.
It\'s connected to the same TransformerEnd as the
TransformerCoreAdmittance, which is typically the lowest voltage winding
other than a tertiary. The attached Curve is a piecewise linear
magnetization characteristic, plotted as core flux linkage vs.
magnetizing current. This replaces the linear magnetizing characteristic
defined by TransformerCoreAdmittance.b and TransformerCoreAdmittance.b0.
The TransformerSaturation characteristic does not include hysteresis,
i.e., the origin point \[0,0\] is implied. The
TransformerCoreAdmittance.g and TransformerCoreAdmittance.g0 should
still be used to model core losses.

This data is of most interest to electromagnetic transient analysis,
which typically uses SI units without multipliers.

xMultiplier inherited attribute should be UnitMultiplier.none

xUnit inherited attribute should be UnitSymbol.A

y1Multiplier inherited attribute should be UnitMultiplier.none

y1Unit inherited attribute should be UnitSymbol.Vs

xvalue in associated CurveData should be magnetizing current in peak A
(not RMS), referenced to the TransformerEnd associated through
TransformerCoreAdmittance. Do not enter the origin point \[0,0\].

y1value in associated CurveData should be core flux linkage in peak Vs
(not RMS), referenced to the TransformerEnd associated through
TransformerCoreAdmittance. Do not enter the origin point \[0,0\].

**Native Members**

  --------------------------- ------ ------------------------------------------ ---
  TransformerCoreAdmittance   0..1   [Transfo rmerCoreAdmittance \<#Tran        
                                     sformerCoreAdmittance\>]{.title-ref}\_\_   

  --------------------------- ------ ------------------------------------------ ---

**Inherited Members**

  -------------- ------ ----------------------------------- -------------------------------------
  mRID           1..1   [String](#String)                   see [Cu rve](#Curve.mRID)

  curveStyle     0..1   [CurveSt yle](#CurveStyle)          see [Curve \<#
                                                            Curve.curveStyle\>]{.title-ref}\_\_

  name           1..1   [String](#String)                   see [Cu rve](#Curve.name)

  xMultiplier    0..1   [UnitMultiplier](#UnitMultiplier)   see [Curve \<#C
                                                            urve.xMultiplier\>]{.title-ref}\_\_

  xUnit          0..1   [UnitSym bol](#UnitSymbol)          see [Cur ve](#Curve.xUnit)

  y1Multiplier   0..1   [UnitMultiplier](#UnitMultiplier)   see [Curve \<#Cu
                                                            rve.y1Multiplier\>]{.title-ref}\_\_

  y1Unit         0..1   [UnitSym bol](#UnitSymbol)          see [Curv e](#Curve.y1Unit)
  -------------- ------ ----------------------------------- -------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#VsConverter .container .group}
[#VsConverter](#VsConverter)

**VsConverter**

DC

DC side of the voltage source converter (VSC).

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  delta               0..1   [AngleDegrees \<                   Angle between
                             #AngleDegrees\>]{.title-ref}\_\_   VsConverter.uv and
                                                                ACDCConverter.uc.
                                                                It is converter\'s
                                                                state variable used
                                                                in power flow. The
                                                                attribute shall be
                                                                a positive value or
                                                                zero.

  droop               0..1   [PU](#PU)                          Droop constant. The
                                                                pu value is
                                                                obtained as D
                                                                \[kV/MW\] \* Sb /
                                                                Ubdc. The attribute
                                                                shall be a positive
                                                                value.

  droopCompensation   0..1   [Resistance](#Resistance)          Compensation
                                                                constant. Used to
                                                                compensate for
                                                                voltage drop when
                                                                controlling voltage
                                                                at a distant bus.
                                                                The attribute shall
                                                                be a positive
                                                                value.

  m axModulationIndex 0..1   [Float](#Float)                    The maximum
                                                                quotient between
                                                                the AC converter
                                                                voltage (Uc) and DC
                                                                voltage (Ud). A
                                                                factor typically
                                                                less than 1. It is
                                                                converter\'s
                                                                configuration data
                                                                used in power flow.

  maxValveCurrent     0..1   [CurrentFlow](#CurrentFlow)        The maximum current
                                                                through a valve. It
                                                                is converter\'s
                                                                configuration data.

  pPccControl         0..1   [VsPpccC ontrolKind \<#VsPp        Kind of control of
                             ccControlKind\>]{.title-ref}\_\_   real power and/or
                                                                DC voltage.

  qPccControl         0..1   [VsQpccC ontrolKind \<#VsQp        Kind of reactive
                             ccControlKind\>]{.title-ref}\_\_   power control.

  qShare              0..1   [PerC ent](#PerCent)               Reactive power
                                                                sharing factor
                                                                among parallel
                                                                converters on Uac
                                                                control. The
                                                                attribute shall be
                                                                a positive value or
                                                                zero.

  targetPhasePcc      0..1   [AngleDegrees \<                   Phase target at AC
                             #AngleDegrees\>]{.title-ref}\_\_   side, at point of
                                                                common coupling.
                                                                The attribute shall
                                                                be a positive
                                                                value.

  tar                 0..1   [Float](#Float)                    Power factor target
  getPowerFactorPcc                                             at the AC side, at
                                                                point of common
                                                                coupling. The
                                                                attribute shall be
                                                                a positive value.

  targetPWMfactor     0..1   [Float](#Float)                    Magnitude of
                                                                pulse-modulation
                                                                factor. The
                                                                attribute shall be
                                                                a positive value.

  targetQpcc          0..1   [ReactivePower \<#                 Reactive power
                             ReactivePower\>]{.title-ref}\_\_   injection target in
                                                                AC grid, at point
                                                                of common coupling.
                                                                Load sign
                                                                convention is used,
                                                                i.e. positive sign
                                                                means flow out from
                                                                a node.

  targetUpcc          0..1   [Volt age](#Voltage)               Voltage target in
                                                                AC grid, at point
                                                                of common coupling.
                                                                The attribute shall
                                                                be a positive
                                                                value.

  uv                  0..1   [Volt age](#Voltage)               Line-to-line
                                                                voltage on the
                                                                valve side of the
                                                                converter
                                                                transformer. It is
                                                                converter\'s state
                                                                variable, result
                                                                from power flow.
                                                                The attribute shall
                                                                be a positive
                                                                value.
  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**

  ---------------- ------ ---------------------------------- ----------------------------------
  baseS            0..1   [ApparentPower \<#                 see [ACDCC onverter \<#ACDCCo
                          ApparentPower\>]{.title-ref}\_\_   nverter.baseS\>]{.title-ref}\_\_

  idc              0..1   [CurrentFlow](#CurrentFlow)        see [ACD CConverter \<#ACDC
                                                             Converter.idc\>]{.title-ref}\_\_

  idleLoss         0..1   [ActivePower](#ActivePower)        see [ACDCConv erter \<#ACDCConve
                                                             rter.idleLoss\>]{.title-ref}\_\_

  maxP             0..1   [ActivePower](#ActivePower)        see [ACDC Converter \<#ACDCC
                                                             onverter.maxP\>]{.title-ref}\_\_

  maxUdc           0..1   [Volt age](#Voltage)               see [ACDCCo nverter \<#ACDCCon
                                                             verter.maxUdc\>]{.title-ref}\_\_

  minP             0..1   [ActivePower](#ActivePower)        see [ACDC Converter \<#ACDCC
                                                             onverter.minP\>]{.title-ref}\_\_

  minUdc           0..1   [Volt age](#Voltage)               see [ACDCCo nverter \<#ACDCCon
                                                             verter.minUdc\>]{.title-ref}\_\_

  numberOfValves   0..1   [Inte ger](#Integer)               see [ACDCConverter
                                                             \<#ACDCConverter.n
                                                             umberOfValves\>]{.title-ref}\_\_

  p                0..1   [ActivePower](#ActivePower)        see [A CDCConverter \<#AC
                                                             DCConverter.p\>]{.title-ref}\_\_

  poleLossP        0..1   [ActivePower](#ActivePower)        see [ACDCConve rter \<#ACDCConver
                                                             ter.poleLossP\>]{.title-ref}\_\_

  q                0..1   [ReactivePower \<#                 see [A CDCConverter \<#AC
                          ReactivePower\>]{.title-ref}\_\_   DCConverter.q\>]{.title-ref}\_\_

  ratedUdc         0..1   [Volt age](#Voltage)               see [ACDCConv erter \<#ACDCConve
                                                             rter.ratedUdc\>]{.title-ref}\_\_

  resistiveLoss    0..1   [Resistance](#Resistance)          see [ACDCConverter
                                                             \<#ACDCConverter.
                                                             resistiveLoss\>]{.title-ref}\_\_

  switchingLoss    0..1   [Active PowerPerCurrentFl ow       see [ACDCConverter
                          \<#ActivePowerP                    \<#ACDCConverter.
                          erCurrentFlow\>]{.title-ref}\_\_   switchingLoss\>]{.title-ref}\_\_

  targetPpcc       0..1   [ActivePower](#ActivePower)        see [ACDCConver ter \<#ACDCConvert
                                                             er.targetPpcc\>]{.title-ref}\_\_

  targetUdc        0..1   [Volt age](#Voltage)               see [ACDCConve rter \<#ACDCConver
                                                             ter.targetUdc\>]{.title-ref}\_\_

  uc               0..1   [Volt age](#Voltage)               see [AC DCConverter \<#ACD
                                                             CConverter.uc\>]{.title-ref}\_\_

  udc              0..1   [Volt age](#Voltage)               see [ACD CConverter \<#ACDC
                                                             Converter.udc\>]{.title-ref}\_\_

  valveU0          0..1   [Volt age](#Voltage)               see [ACDCCon verter \<#ACDCConv
                                                             erter.valveU0\>]{.title-ref}\_\_
  ---------------- ------ ---------------------------------- ----------------------------------

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

# Abstract Classes

::: {#ACDCConverter .container .group}
[#ACDCConverter](#ACDCConverter)

**ACDCConverter**

DC

A unit with valves for three phases, together with unit control
equipment, essential protective and switching devices, DC storage
capacitors, phase reactors and auxiliaries, if any, used for conversion.

**Native Members**

+----------------+----------------+----------------+----------------+
| baseS          | 0..1           | [Appar         | Base apparent  |
|                |                | entPower       | power of the   |
|                |                | \<#App         | converter      |
|                |                | a              | pole. The      |
|                |                | rentPower\>]{. | attribute      |
|                |                | title-ref}\_\_ | shall be a     |
|                |                |                | positive       |
|                |                |                | value.         |
+----------------+----------------+----------------+----------------+
| idc            | 0..1           | [C urrentFlow  | Converter DC   |
|                |                | \<#C           | current, also  |
|                |                | u              | called Id. It  |
|                |                | rrentFlow\>]{. | is             |
|                |                | title-ref}\_\_ | converter\'s   |
|                |                |                | state          |
|                |                |                | variable,      |
|                |                |                | result from    |
|                |                |                | power flow.    |
+----------------+----------------+----------------+----------------+
| idleLoss       | 0..1           | [A ctivePower  | Active power   |
|                |                | \<#A           | loss in pole   |
|                |                | c              | at no power    |
|                |                | tivePower\>]{. | transfer. It   |
|                |                | title-ref}\_\_ | is the         |
|                |                |                | converter\'s   |
|                |                |                | configuration  |
|                |                |                | data used in   |
|                |                |                | power flow.    |
|                |                |                | The attribute  |
|                |                |                | shall be a     |
|                |                |                | positive       |
|                |                |                | value.         |
+----------------+----------------+----------------+----------------+
| maxP           | 0..1           | [A ctivePower  | Maximum active |
|                |                | \<#A           | power limit.   |
|                |                | c              | The value is   |
|                |                | tivePower\>]{. | overwritten by |
|                |                | title-ref}\_\_ | values of VsC  |
|                |                |                | a              |
|                |                |                | pabilityCurve, |
|                |                |                | if present.    |
+----------------+----------------+----------------+----------------+
| maxUdc         | 0..1           | [Vol           | The maximum    |
|                |                | t              | voltage on the |
|                |                | age](#Voltage) | DC side at     |
|                |                |                | which the      |
|                |                |                | converter      |
|                |                |                | should         |
|                |                |                | operate. It is |
|                |                |                | the            |
|                |                |                | converter\'s   |
|                |                |                | configuration  |
|                |                |                | data used in   |
|                |                |                | power flow.    |
|                |                |                | The attribute  |
|                |                |                | shall be a     |
|                |                |                | positive       |
|                |                |                | value.         |
+----------------+----------------+----------------+----------------+
| minP           | 0..1           | [A ctivePower  | Minimum active |
|                |                | \<#A           | power limit.   |
|                |                | c              | The value is   |
|                |                | tivePower\>]{. | overwritten by |
|                |                | title-ref}\_\_ | values of VsC  |
|                |                |                | a              |
|                |                |                | pabilityCurve, |
|                |                |                | if present.    |
+----------------+----------------+----------------+----------------+
| minUdc         | 0..1           | [Vol           | The minimum    |
|                |                | t              | voltage on the |
|                |                | age](#Voltage) | DC side at     |
|                |                |                | which the      |
|                |                |                | converter      |
|                |                |                | should         |
|                |                |                | operate. It is |
|                |                |                | the            |
|                |                |                | converter\'s   |
|                |                |                | configuration  |
|                |                |                | data used in   |
|                |                |                | power flow.    |
|                |                |                | The attribute  |
|                |                |                | shall be a     |
|                |                |                | positive       |
|                |                |                | value.         |
+----------------+----------------+----------------+----------------+
| numberOfValves | 0..1           | [Int           | Number of      |
|                |                | e              | valves in the  |
|                |                | ger](#Integer) | converter.     |
|                |                |                | Used in loss   |
|                |                |                | calculations.  |
+----------------+----------------+----------------+----------------+
| p              | 0..1           | [A ctivePower  | Active power   |
|                |                | \<#A           | at the point   |
|                |                | c              | of common      |
|                |                | tivePower\>]{. | coupling. Load |
|                |                | title-ref}\_\_ | sign           |
|                |                |                | convention is  |
|                |                |                | used, i.e.     |
|                |                |                | positive sign  |
|                |                |                | means flow out |
|                |                |                | from a node.   |
|                |                |                |                |
|                |                |                | Starting value |
|                |                |                | for a steady   |
|                |                |                | state solution |
|                |                |                | in the case a  |
|                |                |                | simplified     |
|                |                |                | power flow     |
|                |                |                | model is used. |
+----------------+----------------+----------------+----------------+
| poleLossP      | 0..1           | [A ctivePower  | The active     |
|                |                | \<#A           | power loss at  |
|                |                | c              | a DC Pole      |
|                |                | tivePower\>]{. |                |
|                |                | title-ref}\_\_ | = idleLoss +   |
|                |                |                | switching      |
|                |                |                | L              |
|                |                |                | oss\*\|Idc\| + |
|                |                |                | resiti         |
|                |                |                | v              |
|                |                |                | eLoss\*Idc\^2. |
|                |                |                |                |
|                |                |                | For lossless   |
|                |                |                | operation      |
|                |                |                | Pdc=Pac.       |
|                |                |                |                |
|                |                |                | For rectifier  |
|                |                |                | operation with |
|                |                |                | losses         |
|                |                |                | Pdc=Pac-lossP. |
|                |                |                |                |
|                |                |                | For inverter   |
|                |                |                | operation with |
|                |                |                | losses         |
|                |                |                | Pdc=Pac+lossP. |
|                |                |                |                |
|                |                |                | It is          |
|                |                |                | converter\'s   |
|                |                |                | state variable |
|                |                |                | used in power  |
|                |                |                | flow. The      |
|                |                |                | attribute      |
|                |                |                | shall be a     |
|                |                |                | positive       |
|                |                |                | value.         |
+----------------+----------------+----------------+----------------+
| q              | 0..1           | [React         | Reactive power |
|                |                | ivePower       | at the point   |
|                |                | \<#Rea         | of common      |
|                |                | c              | coupling. Load |
|                |                | tivePower\>]{. | sign           |
|                |                | title-ref}\_\_ | convention is  |
|                |                |                | used, i.e.     |
|                |                |                | positive sign  |
|                |                |                | means flow out |
|                |                |                | from a node.   |
|                |                |                |                |
|                |                |                | Starting value |
|                |                |                | for a steady   |
|                |                |                | state solution |
|                |                |                | in the case a  |
|                |                |                | simplified     |
|                |                |                | power flow     |
|                |                |                | model is used. |
+----------------+----------------+----------------+----------------+
| ratedUdc       | 0..1           | [Vol           | Rated          |
|                |                | t              | converter DC   |
|                |                | age](#Voltage) | voltage, also  |
|                |                |                | called UdN.    |
|                |                |                | The attribute  |
|                |                |                | shall be a     |
|                |                |                | positive       |
|                |                |                | value. It is   |
|                |                |                | the            |
|                |                |                | converter\'s   |
|                |                |                | configuration  |
|                |                |                | data used in   |
|                |                |                | power flow.    |
|                |                |                | For instance a |
|                |                |                | bipolar DC     |
|                |                |                | link with      |
|                |                |                | value 200 kV   |
|                |                |                | has a 400kV    |
|                |                |                | difference     |
|                |                |                | between the dc |
|                |                |                | lines.         |
+----------------+----------------+----------------+----------------+
| resistiveLoss  | 0..1           | [Resistanc e   | It is the      |
|                |                | \<#            | converter\'s   |
|                |                | R              | configuration  |
|                |                | esistance\>]{. | data used in   |
|                |                | title-ref}\_\_ | power flow.    |
|                |                |                | Refer to       |
|                |                |                | poleLossP. The |
|                |                |                | attribute      |
|                |                |                | shall be a     |
|                |                |                | positive       |
|                |                |                | value.         |
+----------------+----------------+----------------+----------------+
| switchingLoss  | 0..1           | [ActivePow e   | Switching      |
|                |                | rPerCurrentFlo | losses,        |
|                |                | w \<#Acti      | relative to    |
|                |                | vePower%20PerC | the base       |
|                |                | u              | apparent power |
|                |                | rrentFlow\>]{. | \'baseS\'.     |
|                |                | title-ref}\_\_ | Refer to       |
|                |                |                | poleLossP. The |
|                |                |                | attribute      |
|                |                |                | shall be a     |
|                |                |                | positive       |
|                |                |                | value.         |
+----------------+----------------+----------------+----------------+
| targetPpcc     | 0..1           | [A ctivePower  | Real power     |
|                |                | \<#A           | injection      |
|                |                | c              | target in AC   |
|                |                | tivePower\>]{. | grid, at point |
|                |                | title-ref}\_\_ | of common      |
|                |                |                | coupling. Load |
|                |                |                | sign           |
|                |                |                | convention is  |
|                |                |                | used, i.e.     |
|                |                |                | positive sign  |
|                |                |                | means flow out |
|                |                |                | from a node.   |
+----------------+----------------+----------------+----------------+
| targetUdc      | 0..1           | [Vol           | Target value   |
|                |                | t              | for DC voltage |
|                |                | age](#Voltage) | magnitude. The |
|                |                |                | attribute      |
|                |                |                | shall be a     |
|                |                |                | positive       |
|                |                |                | value.         |
+----------------+----------------+----------------+----------------+
| uc             | 0..1           | [Vol           | Line-to-line   |
|                |                | t              | converter      |
|                |                | age](#Voltage) | voltage, the   |
|                |                |                | voltage at the |
|                |                |                | AC side of the |
|                |                |                | valve. It is   |
|                |                |                | converter\'s   |
|                |                |                | state          |
|                |                |                | variable,      |
|                |                |                | result from    |
|                |                |                | power flow.    |
|                |                |                | The attribute  |
|                |                |                | shall be a     |
|                |                |                | positive       |
|                |                |                | value.         |
+----------------+----------------+----------------+----------------+
| udc            | 0..1           | [Vol           | Converter      |
|                |                | t              | voltage at the |
|                |                | age](#Voltage) | DC side, also  |
|                |                |                | called Ud. It  |
|                |                |                | is             |
|                |                |                | converter\'s   |
|                |                |                | state          |
|                |                |                | variable,      |
|                |                |                | result from    |
|                |                |                | power flow.    |
|                |                |                | The attribute  |
|                |                |                | shall be a     |
|                |                |                | positive       |
|                |                |                | value.         |
+----------------+----------------+----------------+----------------+
| valveU0        | 0..1           | [Vol           | Valve          |
|                |                | t              | threshold      |
|                |                | age](#Voltage) | voltage, also  |
|                |                |                | called Uvalve. |
|                |                |                | Forward        |
|                |                |                | voltage drop   |
|                |                |                | when the valve |
|                |                |                | is conducting. |
|                |                |                | Used in loss   |
|                |                |                | calculations,  |
|                |                |                | i.e. the       |
|                |                |                | switchLoss     |
|                |                |                | depend on      |
|                |                |                | numberOfV      |
|                |                |                | a              |
|                |                |                | lves\*valveU0. |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#ACDCTerminal .container .group}
[#ACDCTerminal](#ACDCTerminal)

**ACDCTerminal**

Core

An electrical connection point (AC or DC) to a piece of conducting
equipment. Terminals are connected at physical connection points called
connectivity nodes.

**Native Members**

  ---------------- ------ ------------------- -------------------
  sequenceNumber   1..1   [Inte               The orientation of
                          ger](#Integer)      the terminal
                                              connections for a
                                              multiple terminal
                                              conducting
                                              equipment. The
                                              sequence numbering
                                              starts with 1 and
                                              additional
                                              terminals should
                                              follow in
                                              increasing order.
                                              The first terminal
                                              is the \"starting
                                              point\" for a two
                                              terminal branch.

  ---------------- ------ ------------------- -------------------

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#AsynchronousMachineDynamics .container .group}
[#AsynchronousMachineDynamics](#AsynchronousMachineDynamics)

**AsynchronousMachineDynamics**

AsynchronousMachineDynamics

Asynchronous machine whose behaviour is described by reference to a
standard model expressed in either time constant reactance form or
equivalent circuit form or by definition of a user-defined model.

Parameter details:

1.  Asynchronous machine parameters such as *Xl, Xs,* etc. are actually
    used as inductances in the model, but are commonly referred to as
    reactances since, at nominal frequency, the PU values are the same.
    However, some references use the symbol *L* instead of *X*.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  As                  0..1   [Asynchronou sMachine \<#Asynch    Asynchronous
  ynchronousMachine          ronousMachine\>]{.title-ref}\_\_   machine to which
                                                                this asynchronous
                                                                machine dynamics
                                                                model applies.

  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**

  ------------------- ------ ------------------- ----------------------------------
  damping             1..1   [Float](#Float)     see [RotatingMa chineDynamics \<#R
                                                 otatingMachineDyn
                                                 amics.damping\>]{.title-ref}\_\_

  inertia             1..1   [Seco               see [RotatingMa chineDynamics \<#R
                             nds](#Seconds)      otatingMachineDyn
                                                 amics.inertia\>]{.title-ref}\_\_

  stato               1..1   [PU](#PU)           see [Rotating MachineDynamics \<
  rLeakageReactance                              #RotatingMachineD
                                                 ynamics.statorLea
                                                 kageReactance\>]{.title-ref}\_\_

  statorResistance    1..1   [PU](#PU)           see [Ro tatingMachineDyna mics
                                                 \<#RotatingMa chineDynamics.sta
                                                 torResistance\>]{.title-ref}\_\_
  ------------------- ------ ------------------- ----------------------------------

  --------- ------ ------------------------ ---------------------------------------
  mRID      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.mRID\>]{.title-ref}\_\_

  enabled   1..1   [Boolean](#Boolean)      see [DynamicsFunct ionBlock
                                            \<#DynamicsFun
                                            ctionBlock.enabled\>]{.title-ref}\_\_

  name      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.name\>]{.title-ref}\_\_
  --------- ------ ------------------------ ---------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#Breaker .container .group}
[#Breaker](#Breaker)

**Breaker**

Wires

A mechanical switching device capable of making, carrying, and breaking
currents under normal circuit conditions and also making, carrying for a
specified time, and breaking currents under specified abnormal circuit
conditions e.g. those of short circuit.

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#ConductingEquipment .container .group}
[#ConductingEquipment](#ConductingEquipment)

**ConductingEquipment**

Core

The parts of the AC power system that are designed to carry current or
that are conductively connected through terminals.

**Native Members**

  ------------- ------ ---------------------- ----------------------
  BaseVoltage   0..1   [BaseVolta             Base voltage of this
                       ge](#BaseVoltage)      conducting equipment.
                                              Use only when there is
                                              no voltage level
                                              container used and
                                              only one base voltage
                                              applies. For example,
                                              not used for
                                              transformers.

  ------------- ------ ---------------------- ----------------------

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#Conductor .container .group}
[#Conductor](#Conductor)

**Conductor**

Wires

Combination of conducting material with consistent electrical
characteristics, building a single electrical system, used to carry
current between points in the power system.

**Native Members**

  -------- ------ ---------------------- -------------------------
  length   1..1   [Length](#Length)      Segment length for
                                         calculating line segment
                                         capabilities.

  -------- ------ ---------------------- -------------------------

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#ConnectedFacility .container .group}
[#ConnectedFacility](#ConnectedFacility)

**ConnectedFacility**

Emtiop

A collection of components that comprise a facility connected to the
grid, such as a generating plant or large load.

**Native Members**

  ------------------- ------- ---------------------------------- -------------------
  ACPoin              0..1    [AC PointOfCommonCoup ling         The connection
  tOfCommonCoupling           \<#ACPointOfC                      point for this
                              ommonCoupling\>]{.title-ref}\_\_   facility. It should
                                                                 be associated with
                                                                 a ConnectivityNode
                                                                 within the facility
                                                                 network model,
                                                                 where it may be
                                                                 connected to an
                                                                 external network
                                                                 model.

  Equipments          0..\*   [Equipmen t](#Equipment)           The Equipments
                                                                 associated with
                                                                 this C
                                                                 onnectedFacility.
  ------------------- ------- ---------------------------------- -------------------

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#ConnectivityNodeContainer .container .group}
[#ConnectivityNodeContainer](#ConnectivityNodeContainer)

**ConnectivityNodeContainer**

Core

A base class for all objects that may contain connectivity nodes or
topological nodes.

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#Curve .container .group}
[#Curve](#Curve)

**Curve**

Core

A multi-purpose curve or functional relationship between an independent
variable (X-axis) and dependent (Y-axis) variables.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 1..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| curveStyle     | 0..1           | [CurveStyl e   | The style or   |
|                |                | \<#            | shape of the   |
|                |                | C              | curve.         |
|                |                | urveStyle\>]{. |                |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+
| name           | 1..1           | [S trin        | The name is    |
|                |                | g](#String)    | any free human |
|                |                |                | readable and   |
|                |                |                | possibly non   |
|                |                |                | unique text    |
|                |                |                | naming the     |
|                |                |                | object.        |
+----------------+----------------+----------------+----------------+
| xMultiplier    | 0..1           | [Un itMultip   | Multiplier for |
|                |                | lier           | X-axis.        |
|                |                | \<#%20Unit     |                |
|                |                | M              |                |
|                |                | ultiplier\>]{. |                |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+
| xUnit          | 0..1           | [UnitSymbo l   | The X-axis     |
|                |                | \<#            | units of       |
|                |                | U              | measure.       |
|                |                | nitSymbol\>]{. |                |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+
| y1Multiplier   | 0..1           | [Un itMultip   | Multiplier for |
|                |                | lier           | Y1-axis.       |
|                |                | \<#%20Unit     |                |
|                |                | M              |                |
|                |                | ultiplier\>]{. |                |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+
| y1Unit         | 0..1           | [UnitSymbo l   | The Y1-axis    |
|                |                | \<#            | units of       |
|                |                | U              | measure.       |
|                |                | nitSymbol\>]{. |                |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DCBaseTerminal .container .group}
[#DCBaseTerminal](#DCBaseTerminal)

**DCBaseTerminal**

DC

An electrical connection point at a piece of DC conducting equipment. DC
terminals are connected at one physical DC node that may have multiple
DC terminals connected. A DC node is similar to an AC connectivity node.
The model requires that DC connections are distinct from AC connections.

**Native Members**

  -------- ------ ---------------------- -------------------------
  DCNode   1..1   [DCNode](#DCNode)      The DC connectivity node
                                         to which this DC base
                                         terminal connects with
                                         zero impedance.

  -------- ------ ---------------------- -------------------------

**Inherited Members**

  ---------------- ------ ------------------- ----------------------------------
  sequenceNumber   1..1   [Inte               see [ACDCTerminal
                          ger](#Integer)      \<#ACDCTerminal.s
                                              equenceNumber\>]{.title-ref}\_\_

  ---------------- ------ ------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DCConductingEquipment .container .group}
[#DCConductingEquipment](#DCConductingEquipment)

**DCConductingEquipment**

DC

The parts of the DC power system that are designed to carry current or
that are conductively connected through DC terminals.

**Native Members**

+----------------+----------------+----------------+----------------+
| ratedCurrent   | 0..1           | [C urrentFlow  | The maximum    |
|                |                | \<#C           | continuous     |
|                |                | u              | current        |
|                |                | rrentFlow\>]{. | carrying       |
|                |                | title-ref}\_\_ | capacity in    |
|                |                |                | amps governed  |
|                |                |                | by the device  |
|                |                |                | material and   |
|                |                |                | construction.  |
|                |                |                |                |
|                |                |                | The attribute  |
|                |                |                | shall be a     |
|                |                |                | positive       |
|                |                |                | value.         |
+----------------+----------------+----------------+----------------+
| ratedUdc       | 0..1           | [Vol           | Rated DC       |
|                |                | t              | device         |
|                |                | age](#Voltage) | voltage. The   |
|                |                |                | attribute      |
|                |                |                | shall be a     |
|                |                |                | positive       |
|                |                |                | value. It is   |
|                |                |                | configuration  |
|                |                |                | data used in   |
|                |                |                | power flow.    |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DCSwitch .container .group}
[#DCSwitch](#DCSwitch)

**DCSwitch**

DC

A switch within the DC system.

**Native Members**

+----------------+----------------+----------------+----------------+
| locked         | 0..1           | [Boo           | If true, the   |
|                |                | l              | switch is      |
|                |                | ean](#Boolean) | locked. The    |
|                |                |                | resulting      |
|                |                |                | switch state   |
|                |                |                | is a           |
|                |                |                | combination of |
|                |                |                | locked and     |
|                |                |                | DCSwitch.open  |
|                |                |                | attributes as  |
|                |                |                | follows:       |
|                |                |                |                |
|                |                |                | \- locked=true |
|                |                |                |                |
|                |                |                | :   and DCSw i |
|                |                |                |                |
|                |                |                | tch.open=true. |
|                |                |                |                |
|                |                |                | :   The        |
|                |                |                |     resulting  |
|                |                |                |     state is   |
|                |                |                |     open and   |
|                |                |                |     locked;    |
|                |                |                |                |
|                |                |                | \              |
|                |                |                | - locked=false |
|                |                |                |                |
|                |                |                | :   and DCSw i |
|                |                |                |                |
|                |                |                | tch.open=true. |
|                |                |                |                |
|                |                |                | :   The        |
|                |                |                |     resulting  |
|                |                |                |     state is   |
|                |                |                |     open;      |
|                |                |                |                |
|                |                |                | \              |
|                |                |                | - locked=false |
|                |                |                |                |
|                |                |                | :   and DCSwi  |
|                |                |                |     t          |
|                |                |                |                |
|                |                |                | ch.open=false. |
|                |                |                |                |
|                |                |                | :   The        |
|                |                |                |     resulting  |
|                |                |                |     state is   |
|                |                |                |     closed.    |
+----------------+----------------+----------------+----------------+
| normalOpen     | 0..1           | [Boo           | The attribute  |
|                |                | l              | is used in     |
|                |                | ean](#Boolean) | cases when no  |
|                |                |                | Measurement    |
|                |                |                | for the status |
|                |                |                | value is       |
|                |                |                | present. If    |
|                |                |                | the DCSwitch   |
|                |                |                | has a status   |
|                |                |                | measurement    |
|                |                |                | the Discr e    |
|                |                |                | te.normalValue |
|                |                |                | is expected to |
|                |                |                | match with the |
|                |                |                | DCSwi t        |
|                |                |                | ch.normalOpen. |
+----------------+----------------+----------------+----------------+
| open           | 0..1           | [Boo           | The attribute  |
|                |                | l              | tells if the   |
|                |                | ean](#Boolean) | switch is      |
|                |                |                | considered     |
|                |                |                | open when used |
|                |                |                | as input to    |
|                |                |                | topology       |
|                |                |                | processing.    |
+----------------+----------------+----------------+----------------+
| retained       | 0..1           | [Boo           | Branch is      |
|                |                | l              | retained in    |
|                |                | ean](#Boolean) | the            |
|                |                |                | topological    |
|                |                |                | solution. The  |
|                |                |                | flow through   |
|                |                |                | retained       |
|                |                |                | switches will  |
|                |                |                | normally be    |
|                |                |                | calculated in  |
|                |                |                | power flow.    |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  -------------- ------ ---------------------- -------------------------------------
  ratedCurrent   0..1   [CurrentFl             see [DC ConductingEquipment
                        ow](#CurrentFlow)      \<#DCConductingEquipm
                                               ent.ratedCurrent\>]{.title-ref}\_\_

  ratedUdc       0..1   [V oltage](#Voltage)   see [DCConductingEquipm ent
                                               \<#DCConductingEq
                                               uipment.ratedUdc\>]{.title-ref}\_\_
  -------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DetailedModelDescriptor .container .group}
[#DetailedModelDescriptor](#DetailedModelDescriptor)

**DetailedModelDescriptor**

DetailedModelDescription

Describes different components of a detailed model.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 0..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| DetailedMo d   | 0..1           | [DetailedM o   | The detailed   |
| elTypeDynamics |                | delTypeDynamic | model type     |
|                |                | s \<#Deta      | dynamics that  |
|                |                | iledMod%20elTy | has detailed   |
|                |                | p              | model          |
|                |                | eDynamics\>]{. | descriptor.    |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DetailedModelTypeDynamics .container .group}
[#DetailedModelTypeDynamics](#DetailedModelTypeDynamics)

**DetailedModelTypeDynamics**

DetailedModelDescription

The main class that packages all related to this type of a detailed
model. This includes all parameters, functions, signals, etc.
:::

::: {#DiagramObject .container .group}
[#DiagramObject](#DiagramObject)

**DiagramObject**

DiagramLayout

An object that defines one or more points in a given space. This object
can be associated with anything that specializes IdentifiedObject. For
single line diagrams such objects typically include such items as analog
values, breakers, disconnectors, power transformers, and transmission
lines.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 1..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| drawingOrder   | 1..1           | [Int           | The drawing    |
|                |                | e              | order of this  |
|                |                | ger](#Integer) | element. The   |
|                |                |                | higher the     |
|                |                |                | number, the    |
|                |                |                | later the      |
|                |                |                | element is     |
|                |                |                | drawn in       |
|                |                |                | sequence. This |
|                |                |                | is used to     |
|                |                |                | ensure that    |
|                |                |                | elements that  |
|                |                |                | overlap are    |
|                |                |                | rendered in    |
|                |                |                | the correct    |
|                |                |                | order.         |
+----------------+----------------+----------------+----------------+
| isPolygon      | 1..1           | [Boo           | Defines        |
|                |                | l              | whether or not |
|                |                | ean](#Boolean) | the diagram    |
|                |                |                | objects points |
|                |                |                | define the     |
|                |                |                | boundaries of  |
|                |                |                | a polygon or   |
|                |                |                | the routing of |
|                |                |                | a polyline. If |
|                |                |                | this value is  |
|                |                |                | true then a    |
|                |                |                | receiving      |
|                |                |                | application    |
|                |                |                | should         |
|                |                |                | consider the   |
|                |                |                | first and last |
|                |                |                | points to be   |
|                |                |                | connected.     |
+----------------+----------------+----------------+----------------+
| name           | 1..1           | [S trin        | The name is    |
|                |                | g](#String)    | any free human |
|                |                |                | readable and   |
|                |                |                | possibly non   |
|                |                |                | unique text    |
|                |                |                | naming the     |
|                |                |                | object.        |
+----------------+----------------+----------------+----------------+
| I d            | 1..1           | [Identi        | The domain     |
| entifiedObject |                | fiedObje ct    | object to      |
|                |                | \<#Id%20enti   | which this     |
|                |                | f              | diagram object |
|                |                | iedObject\>]{. | is associated. |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#DynamicsFunctionBlock .container .group}
[#DynamicsFunctionBlock](#DynamicsFunctionBlock)

**DynamicsFunctionBlock**

StandardModels

Abstract parent class for all Dynamics function blocks.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 1..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| enabled        | 1..1           | [Boo           | Function block |
|                |                | l              | used           |
|                |                | ean](#Boolean) | indicator.     |
|                |                |                |                |
|                |                |                | true = use of  |
|                |                |                | function block |
|                |                |                | is enabled     |
|                |                |                |                |
|                |                |                | false = use of |
|                |                |                | function block |
|                |                |                | is disabled.   |
+----------------+----------------+----------------+----------------+
| name           | 1..1           | [S trin        | The name is    |
|                |                | g](#String)    | any free human |
|                |                |                | readable and   |
|                |                |                | possibly non   |
|                |                |                | unique text    |
|                |                |                | naming the     |
|                |                |                | object.        |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#EnergyConnection .container .group}
[#EnergyConnection](#EnergyConnection)

**EnergyConnection**

Wires

A connection of energy generation or consumption on the power system
model.

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#Equipment .container .group}
[#Equipment](#Equipment)

**Equipment**

Core

The parts of a power system that are physical devices, electronic or
mechanical.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  inService           1..1   [Bool ean](#Boolean)               Specifies the
                                                                availability of the
                                                                equipment. True
                                                                means the equipment
                                                                is available for
                                                                topology
                                                                processing, which
                                                                determines if the
                                                                equipment is
                                                                energized or not.
                                                                False means that
                                                                the equipment is
                                                                treated by network
                                                                applications as if
                                                                it is not in the
                                                                model.

  E quipmentContainer 1..1   [Equipment Container \<#Equip      Container of this
                             mentContainer\>]{.title-ref}\_\_   equipment.
  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#GeneratingUnit .container .group}
[#GeneratingUnit](#GeneratingUnit)

**GeneratingUnit**

Production

A single or set of synchronous machines for converting mechanical power
into alternating-current power. For example, individual machines within
a set may be defined for scheduling purposes while a single control
signal is derived for the set. In this case there would be a
GeneratingUnit for each member of the set and an additional
GeneratingUnit corresponding to the set.

**Native Members**

  --------------- ------ --------------------- ---------------------
  maxOperatingP   1..1   [ActivePowe           This is the maximum
                         r](#ActivePower)      operating active
                                               power limit the
                                               dispatcher can enter
                                               for this unit.

  minOperatingP   1..1   [ActivePowe           This is the minimum
                         r](#ActivePower)      operating active
                                               power limit the
                                               dispatcher can enter
                                               for this unit.
  --------------- ------ --------------------- ---------------------

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#IEEECigreAPISignal .container .group}
[#IEEECigreAPISignal](#IEEECigreAPISignal)

**IEEECigreAPISignal**

Emtiop

The parent class for CIGRE TB 958 input and output signals. Use the
ACDCTerminal association for network flows, the DCNode association for
DC bus quantities, the ConnectivityNode association for AC bus
quantities, or no association for references levels or other signals not
connected to the electric power networks.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  apiName             0..1   [St ring](#String)                 The name of this
                                                                signal, as returned
                                                                by the CIGRE TB 958
                                                                API. The inherited
                                                                Iden
                                                                tifiedObject.name
                                                                attribute might not
                                                                necessarily match
                                                                this name.

  apiParameterKind    0..1   [IEEECi greAPIParameterKi nd       Establishes the
                             \<#IEEECigreAPI                    signal value size,
                             ParameterKind\>]{.title-ref}\_\_   in bytes, expected
                                                                in the CIGRE TB 958
                                                                API.

  apiSequenceNumber   0..1   [Inte ger](#Integer)               The signal\'s
                                                                expected zero-based
                                                                sequence number in
                                                                the CIGRE TB 958
                                                                API array for input
                                                                and output signals.

  apiWidth            0..1   [Inte ger](#Integer)               Signal array
                                                                dimension from the
                                                                CIGRE TB 958 API,
                                                                defaults to 1.

  multiplier          0..1   [U nitMultiplier \<#U              Multiplier for the
                             nitMultiplier\>]{.title-ref}\_\_   units of this
                                                                signal, in CIM. May
                                                                require
                                                                interpretation of
                                                                information
                                                                returned from the
                                                                CIGRE TB 958 API.

  phase               0..1   [Sin glePhaseKind \<#Si            The signal\'s
                             nglePhaseKind\>]{.title-ref}\_\_   phase, as
                                                                applicable, for
                                                                multiphase signal
                                                                connections.

  unit                0..1   [UnitSymbol](#UnitSymbol)          Signal units, if
                                                                applicable, in CIM.
                                                                May require
                                                                interpretation of
                                                                information
                                                                returned from the
                                                                CIGRE TB 958 API.

  ConnectivityNode    0..1   [Conne ctivityNode \<#Con          Use for a bus
                             nectivityNode\>]{.title-ref}\_\_   voltage or other
                                                                bus quantity
                                                                signal. Mutually
                                                                exclusive with
                                                                association to
                                                                DCNode or
                                                                ACDCTerminal.

  DCNode              0..1   [DC Node](#DCNode)                 Use for a DC
                                                                voltage or other
                                                                quantity related to
                                                                DC buses. Mutually
                                                                exclusive with
                                                                assocation to
                                                                ConnectivityNode or
                                                                ACDCTerminal.

  IEEEC               0..1   [ IEEECigreAPISigna lInfo          Expanded set of
  igreAPISignalInfo          \<#IEEECigre                       attributes
                             APISignalInfo\>]{.title-ref}\_\_   available from the
                                                                CIGRE TB 958 API.
  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  ACDCTerminal        0..1   [ACDCTerminal \<                   see [S ignalDescriptor \<
                             #ACDCTerminal\>]{.title-ref}\_\_   #SignalDescriptor
                                                                .ACDCTerminal\>]{.title-ref}\_\_

  Dyna                0..1   [DynamicsFunctio nBlock            see [SignalDesc riptor \<#SignalDe
  micsFunctionBlock          \<#Dynamics                        scriptor.Dynamics
                             FunctionBlock\>]{.title-ref}\_\_   FunctionBlock\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  mRID                0..1   [St ring](#String)                 see [Detaile dModelDescriptor
                                                                \<#DetailedModelDe
                                                                scriptor.mRID\>]{.title-ref}\_\_

  Detailed            0..1   [Detail edModelTypeDynami cs       see [DetailedMod elDescriptor
  ModelTypeDynamics          \<#DetailedMode                    \<#De tailedModelDescri
                             lTypeDynamics\>]{.title-ref}\_\_   ptor.DetailedMode
                                                                lTypeDynamics\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#IdentifiedObject .container .group}
[#IdentifiedObject](#IdentifiedObject)

**IdentifiedObject**

Core

This is a class that provides common identification for all classes
needing identification and naming attributes.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 0..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| name           | 0..1           | [S trin        | The name is    |
|                |                | g](#String)    | any free human |
|                |                |                | readable and   |
|                |                |                | possibly non   |
|                |                |                | unique text    |
|                |                |                | naming the     |
|                |                |                | object.        |
+----------------+----------------+----------------+----------------+
:::

::: {#MutualCoupling .container .group}
[#MutualCoupling](#MutualCoupling)

**MutualCoupling**

Wires

This class represents the zero sequence line mutual coupling.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 1..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| b0ch           | 0..1           | [S usceptance  | Zero sequence  |
|                |                | \<#S           | mutual         |
|                |                | u              | coupling shunt |
|                |                | sceptance\>]{. | (charging)     |
|                |                | title-ref}\_\_ | susceptance,   |
|                |                |                | uniformly      |
|                |                |                | distributed,   |
|                |                |                | of the entire  |
|                |                |                | line section.  |
+----------------+----------------+----------------+----------------+
| distance11     | 0..1           | [L engt        | Distance to    |
|                |                | h](#Length)    | the start of   |
|                |                |                | the coupled    |
|                |                |                | region from    |
|                |                |                | the first      |
|                |                |                | line\'s        |
|                |                |                | terminal       |
|                |                |                | having         |
|                |                |                | sequence       |
|                |                |                | number equal   |
|                |                |                | to 1.          |
+----------------+----------------+----------------+----------------+
| distance12     | 0..1           | [L engt        | Distance to    |
|                |                | h](#Length)    | the end of the |
|                |                |                | coupled region |
|                |                |                | from the first |
|                |                |                | line\'s        |
|                |                |                | terminal with  |
|                |                |                | sequence       |
|                |                |                | number equal   |
|                |                |                | to 1.          |
+----------------+----------------+----------------+----------------+
| distance21     | 0..1           | [L engt        | Distance to    |
|                |                | h](#Length)    | the start of   |
|                |                |                | coupled region |
|                |                |                | from the       |
|                |                |                | second line\'s |
|                |                |                | terminal with  |
|                |                |                | sequence       |
|                |                |                | number equal   |
|                |                |                | to 1.          |
+----------------+----------------+----------------+----------------+
| distance22     | 0..1           | [L engt        | Distance to    |
|                |                | h](#Length)    | the end of     |
|                |                |                | coupled region |
|                |                |                | from the       |
|                |                |                | second line\'s |
|                |                |                | terminal with  |
|                |                |                | sequence       |
|                |                |                | number equal   |
|                |                |                | to 1.          |
+----------------+----------------+----------------+----------------+
| g0ch           | 0..1           | [C onductance  | Zero sequence  |
|                |                | \<#C           | mutual         |
|                |                | o              | coupling shunt |
|                |                | nductance\>]{. | (charging)     |
|                |                | title-ref}\_\_ | conductance,   |
|                |                |                | uniformly      |
|                |                |                | distributed,   |
|                |                |                | of the entire  |
|                |                |                | line section.  |
+----------------+----------------+----------------+----------------+
| name           | 1..1           | [S trin        | The name is    |
|                |                | g](#String)    | any free human |
|                |                |                | readable and   |
|                |                |                | possibly non   |
|                |                |                | unique text    |
|                |                |                | naming the     |
|                |                |                | object.        |
+----------------+----------------+----------------+----------------+
| r0             | 0..1           | [Resistanc e   | Zero sequence  |
|                |                | \<#            | b r            |
|                |                | R              | anch-to-branch |
|                |                | esistance\>]{. | mutual         |
|                |                | title-ref}\_\_ | impedance      |
|                |                |                | coupling,      |
|                |                |                | resistance.    |
+----------------+----------------+----------------+----------------+
| x0             | 0..1           | [Reactan ce \< | Zero sequence  |
|                |                | #              | b r            |
|                |                | Reactance\>]{. | anch-to-branch |
|                |                | title-ref}\_\_ | mutual         |
|                |                |                | impedance      |
|                |                |                | coupling,      |
|                |                |                | reactance.     |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#OperationalLimit .container .group}
[#OperationalLimit](#OperationalLimit)

**OperationalLimit**

OperationalLimits

A value and normal value associated with a specific kind of limit.

The sub class value and normalValue attributes vary inversely to the
associated OperationalLimitType.acceptableDuration (acceptableDuration
for short).

If a particular piece of equipment has multiple operational limits of
the same kind (apparent power, current, etc.), the limit with the
greatest acceptableDuration shall have the smallest limit value and the
limit with the smallest acceptableDuration shall have the largest limit
value. Note: A large current can only be allowed to flow through a piece
of equipment for a short duration without causing damage, but a lesser
current can be allowed to flow for a longer duration.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 1..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| name           | 1..1           | [S trin        | The name is    |
|                |                | g](#String)    | any free human |
|                |                |                | readable and   |
|                |                |                | possibly non   |
|                |                |                | unique text    |
|                |                |                | naming the     |
|                |                |                | object.        |
+----------------+----------------+----------------+----------------+
| Oper a         | 0..1           | [OperationalL  | The limit set  |
| tionalLimitSet |                | imitSet        | to which the   |
|                |                | \              | limit values   |
|                |                | <#Opera%20tion | belong.        |
|                |                | a              |                |
|                |                | lLimitSet\>]{. |                |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+
| Opera t        | 0..1           | [              | The limit type |
| ionalLimitType |                | OperationalLim | associated     |
|                |                | itType \<      | with this      |
|                |                | #Operat%20iona | limit.         |
|                |                | l              |                |
|                |                | LimitType\>]{. |                |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#PSRType .container .group}
[#PSRType](#PSRType)

**PSRType**

Core

Classifying instances of the same class, e.g. overhead and underground
ACLineSegments. This classification mechanism is intended to provide
flexibility outside the scope of this document, i.e. provide
customisation that is non standard.

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#PhaseTapChanger .container .group}
[#PhaseTapChanger](#PhaseTapChanger)

**PhaseTapChanger**

Wires

A transformer phase shifting tap model that controls the phase angle
difference across the power transformer and potentially the active power
flow through the power transformer. This phase tap model may also impact
the voltage magnitude.

**Native Members**

  ---------------- ------ ---------------------------------- -------------------
  TransformerEnd   0..1   [T ransformerEnd \<#T              Transformer end to
                          ransformerEnd\>]{.title-ref}\_\_   which this phase
                                                             tap changer
                                                             belongs.

  ---------------- ------ ---------------------------------- -------------------

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  highStep      0..1   [I nteger](#Integer)   see [TapChanger \<#Tap
                                              Changer.highStep\>]{.title-ref}\_\_

  lowStep       0..1   [I nteger](#Integer)   see [TapChanger \<#Ta
                                              pChanger.lowStep\>]{.title-ref}\_\_

  neutralStep   0..1   [I nteger](#Integer)   see [TapChanger \<#TapCha
                                              nger.neutralStep\>]{.title-ref}\_\_

  neutralU      0..1   [V oltage](#Voltage)   see [TapChanger \<#Tap
                                              Changer.neutralU\>]{.title-ref}\_\_

  normalStep    0..1   [I nteger](#Integer)   see [TapChanger \<#TapCh
                                              anger.normalStep\>]{.title-ref}\_\_

  step          1..1   [Float](#Float)        see [TapChanger \<
                                              #TapChanger.step\>]{.title-ref}\_\_
  ------------- ------ ---------------------- -------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#PointOfCommonCoupling .container .group}
[#PointOfCommonCoupling](#PointOfCommonCoupling)

**PointOfCommonCoupling**

Core

Point of Common Coupling (PCC) refers to the location where multiple
electrical sources or loads are electrically connected and provide a
reference point where the voltages and currents from different parts of
the system are considered to be common. The PCC is used to support
system analysis, control, and monitoring, as it provides a reference for
understanding the interactions and power flow between various components
within the system. It is also relevant to define the requirement and
responsibility between different actors in operating a power system.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 1..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| name           | 1..1           | [S trin        | The name is    |
|                |                | g](#String)    | any free human |
|                |                |                | readable and   |
|                |                |                | possibly non   |
|                |                |                | unique text    |
|                |                |                | naming the     |
|                |                |                | object.        |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#PowerElectronicsUnit .container .group}
[#PowerElectronicsUnit](#PowerElectronicsUnit)

**PowerElectronicsUnit**

Production

A generating unit or battery or aggregation that connects to the AC
network using power electronics rather than rotating machines.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  maxP                1..1   [ActivePower](#ActivePower)        Maximum active
                                                                power limit. This
                                                                is the maximum
                                                                (nameplate) limit
                                                                for the unit.

  minP                1..1   [ActivePower](#ActivePower)        Minimum active
                                                                power limit. This
                                                                is the minimum
                                                                (nameplate) limit
                                                                for the unit.

  PowerElec           1..1   [PowerEle ctronicsConnectio n      A power electronics
  tronicsConnection          \<#PowerElectron                   unit has a
                             icsConnection\>]{.title-ref}\_\_   connection to the
                                                                AC network.
  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#PowerSystemResource .container .group}
[#PowerSystemResource](#PowerSystemResource)

**PowerSystemResource**

Core

A power system resource (PSR) can be an item of equipment such as a
switch, an equipment container containing many individual items of
equipment such as a substation, or an organisational entity such as
sub-control area. Power system resources can have measurements
associated.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 1..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| name           | 1..1           | [S trin        | The name is    |
|                |                | g](#String)    | any free human |
|                |                |                | readable and   |
|                |                |                | possibly non   |
|                |                |                | unique text    |
|                |                |                | naming the     |
|                |                |                | object.        |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#ProtectedSwitch .container .group}
[#ProtectedSwitch](#ProtectedSwitch)

**ProtectedSwitch**

Wires

A ProtectedSwitch is a switching device that can be operated by
ProtectionEquipment.

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#RegulatingCondEq .container .group}
[#RegulatingCondEq](#RegulatingCondEq)

**RegulatingCondEq**

Wires

A type of conducting equipment that can regulate a quantity (i.e.
voltage or flow) at a specific point in the network.

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#RotatingMachine .container .group}
[#RotatingMachine](#RotatingMachine)

**RotatingMachine**

Wires

A rotating machine which may be used as a generator or motor.

**Native Members**

+----------------+----------------+----------------+----------------+
| p              | 1..1           | [A ctivePower  | Active power   |
|                |                | \<#A           | injection.     |
|                |                | c              | Load sign      |
|                |                | tivePower\>]{. | convention is  |
|                |                | title-ref}\_\_ | used, i.e.     |
|                |                |                | positive sign  |
|                |                |                | means flow out |
|                |                |                | from a node.   |
|                |                |                |                |
|                |                |                | Starting value |
|                |                |                | for a steady   |
|                |                |                | state          |
|                |                |                | solution.      |
+----------------+----------------+----------------+----------------+
| q              | 1..1           | [React         | Reactive power |
|                |                | ivePower       | injection.     |
|                |                | \<#Rea         | Load sign      |
|                |                | c              | convention is  |
|                |                | tivePower\>]{. | used, i.e.     |
|                |                | title-ref}\_\_ | positive sign  |
|                |                |                | means flow out |
|                |                |                | from a node.   |
|                |                |                |                |
|                |                |                | Starting value |
|                |                |                | for a steady   |
|                |                |                | state          |
|                |                |                | solution.      |
+----------------+----------------+----------------+----------------+
| ratedS         | 1..1           | [Appar         | Nameplate      |
|                |                | entPower       | apparent power |
|                |                | \<#App         | rating for the |
|                |                | a              | unit.          |
|                |                | rentPower\>]{. |                |
|                |                | title-ref}\_\_ | The attribute  |
|                |                |                | shall have a   |
|                |                |                | positive       |
|                |                |                | value.         |
+----------------+----------------+----------------+----------------+
| ratedU         | 1..1           | [Vol           | Rated voltage  |
|                |                | t              | (nameplate     |
|                |                | age](#Voltage) | data, Ur in    |
|                |                |                | IEC 60909-0).  |
|                |                |                | It is          |
|                |                |                | primarily used |
|                |                |                | for short      |
|                |                |                | circuit data   |
|                |                |                | exchange       |
|                |                |                | according to   |
|                |                |                | IEC 60909.     |
|                |                |                |                |
|                |                |                | The attribute  |
|                |                |                | shall be a     |
|                |                |                | positive       |
|                |                |                | value.         |
+----------------+----------------+----------------+----------------+
| GeneratingUnit | 1..1           | [Ge nerating   | A synchronous  |
|                |                | Unit           | machine may    |
|                |                | \<#%20Gene     | operate as a   |
|                |                | r              | generator and  |
|                |                | atingUnit\>]{. | as such        |
|                |                | title-ref}\_\_ | becomes a      |
|                |                |                | member of a    |
|                |                |                | generating     |
|                |                |                | unit.          |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#RotatingMachineDynamics .container .group}
[#RotatingMachineDynamics](#RotatingMachineDynamics)

**RotatingMachineDynamics**

StandardModels

Abstract parent class for all synchronous and asynchronous machine
standard models.

**Native Members**

  ------------------- ------ ------------------- -------------------
  damping             1..1   [Float](#Float)     Damping torque
                                                 coefficient (D)
                                                 (\>= 0) in pu
                                                 torque/pu speed
                                                 deviation
                                                 (differential
                                                 type). A
                                                 proportionality
                                                 constant that, when
                                                 multiplied by the
                                                 angular velocity of
                                                 the rotor poles
                                                 with respect to the
                                                 magnetic field
                                                 (frequency),
                                                 results in the
                                                 damping torque.
                                                 This value is often
                                                 zero when the
                                                 sources of damping
                                                 torques (generator
                                                 damper windings,
                                                 load damping
                                                 effects, etc.) are
                                                 modelled in detail.
                                                 Typical value = 0.

  inertia             1..1   [Seco               Inertia constant of
                             nds](#Seconds)      generator or motor
                                                 and mechanical load
                                                 (*H*) (\> 0). This
                                                 is the
                                                 specification for
                                                 the stored energy
                                                 in the rotating
                                                 mass when operating
                                                 at rated speed. For
                                                 a generator, this
                                                 includes the
                                                 generator plus all
                                                 other elements
                                                 (turbine, exciter)
                                                 on the same shaft
                                                 and has units of MW
                                                 x s. For a motor,
                                                 it includes the
                                                 motor plus its
                                                 mechanical load.
                                                 Conventional units
                                                 are PU on the
                                                 generator MVA base,
                                                 usually expressed
                                                 as MW x s / MVA or
                                                 just s. This value
                                                 is used in the
                                                 accelerating power
                                                 reference frame for
                                                 operator training
                                                 simulator
                                                 solutions. Typical
                                                 value = 3.

  stato               1..1   [PU](#PU)           Stator leakage
  rLeakageReactance                              reactance (*Xl*)
                                                 (\>= 0). Typical
                                                 value = 0,15.

  statorResistance    1..1   [PU](#PU)           Stator (armature)
                                                 resistance (*Rs*)
                                                 (\>= 0). Typical
                                                 value = 0,005.
  ------------------- ------ ------------------- -------------------

**Inherited Members**

  --------- ------ ------------------------ ---------------------------------------
  mRID      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.mRID\>]{.title-ref}\_\_

  enabled   1..1   [Boolean](#Boolean)      see [DynamicsFunct ionBlock
                                            \<#DynamicsFun
                                            ctionBlock.enabled\>]{.title-ref}\_\_

  name      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.name\>]{.title-ref}\_\_
  --------- ------ ------------------------ ---------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#ShuntCompensator .container .group}
[#ShuntCompensator](#ShuntCompensator)

**ShuntCompensator**

Wires

A shunt capacitor or reactor or switchable bank of shunt capacitors or
reactors. A section of a shunt compensator is an individual capacitor or
reactor. A negative value for bPerSection indicates that the compensator
is a reactor. ShuntCompensator is a single terminal device. Ground is
implied.

**Native Members**

+----------------+----------------+----------------+----------------+
| grounded       | 1..1           | [Boo           | Required for   |
|                |                | l              | Yn and I       |
|                |                | ean](#Boolean) | connections    |
|                |                |                | (as            |
|                |                |                | represented by |
|                |                |                | Shun t         |
|                |                |                | Compensator.ph |
|                |                |                | a              |
|                |                |                | seConnection). |
|                |                |                | True if the    |
|                |                |                | neutral is     |
|                |                |                | solidly        |
|                |                |                | grounded.      |
+----------------+----------------+----------------+----------------+
| m              | 1..1           | [Int           | The maximum    |
| aximumSections |                | e              | number of      |
|                |                | ger](#Integer) | sections that  |
|                |                |                | may be         |
|                |                |                | switched in.   |
+----------------+----------------+----------------+----------------+
| nomU           | 1..1           | [Vol           | The voltage at |
|                |                | t              | which the      |
|                |                | age](#Voltage) | nominal        |
|                |                |                | reactive power |
|                |                |                | may be         |
|                |                |                | calculated.    |
|                |                |                | This should    |
|                |                |                | normally be    |
|                |                |                | within 10% of  |
|                |                |                | the voltage at |
|                |                |                | which the      |
|                |                |                | capacitor is   |
|                |                |                | connected to   |
|                |                |                | the network.   |
+----------------+----------------+----------------+----------------+
| p              | 0..1           | [PhaseSh u     | The type of    |
| haseConnection |                | ntConnectionKi | phase          |
|                |                | nd \<#Pha      | connection,    |
|                |                | seShunt%20Conn | such as wye or |
|                |                | e              | delta.         |
|                |                | ctionKind\>]{. |                |
|                |                | title-ref}\_\_ |                |
+----------------+----------------+----------------+----------------+
| sections       | 1..1           | [Flo           | Shunt          |
|                |                | at](#Float)    | compensator    |
|                |                |                | sections in    |
|                |                |                | use. Starting  |
|                |                |                | value for      |
|                |                |                | steady state   |
|                |                |                | solution. The  |
|                |                |                | attribute      |
|                |                |                | shall be a     |
|                |                |                | positive value |
|                |                |                | or zero. Non   |
|                |                |                | integer values |
|                |                |                | are allowed to |
|                |                |                | support        |
|                |                |                | continuous     |
|                |                |                | variables. The |
|                |                |                | reasons for    |
|                |                |                | continuous     |
|                |                |                | value are to   |
|                |                |                | support study  |
|                |                |                | cases where no |
|                |                |                | discrete shunt |
|                |                |                | compensators   |
|                |                |                | has yet been   |
|                |                |                | designed, a    |
|                |                |                | solutions      |
|                |                |                | where a narrow |
|                |                |                | voltage band   |
|                |                |                | force the      |
|                |                |                | sections to    |
|                |                |                | oscillate or   |
|                |                |                | accommodate    |
|                |                |                | for a          |
|                |                |                | continuous     |
|                |                |                | solution as    |
|                |                |                | input.         |
|                |                |                |                |
|                |                |                | For LinearS h  |
|                |                |                | untConpensator |
|                |                |                | the value      |
|                |                |                | shall be       |
|                |                |                | between zero   |
|                |                |                | and Shu n      |
|                |                |                | tCompensator.m |
|                |                |                | a              |
|                |                |                | ximumSections. |
|                |                |                | At value zero  |
|                |                |                | the shunt      |
|                |                |                | compensator    |
|                |                |                | conductance    |
|                |                |                | and admittance |
|                |                |                | is zero.       |
|                |                |                | Linear         |
|                |                |                | interpolation  |
|                |                |                | of conductance |
|                |                |                | and admittance |
|                |                |                | between the    |
|                |                |                | previous and   |
|                |                |                | next integer   |
|                |                |                | section is     |
|                |                |                | applied in     |
|                |                |                | case of        |
|                |                |                | non-integer    |
|                |                |                | values.        |
|                |                |                |                |
|                |                |                | For            |
|                |                |                | NonlinearShunt |
|                |                |                | C              |
|                |                |                | ompensator(-s) |
|                |                |                | shall only be  |
|                |                |                | set to one of  |
|                |                |                | the            |
|                |                |                | NonlinearShunt |
|                |                |                | C              |
|                |                |                | ompenstorPoint |
|                |                |                | .              |
|                |                |                | sectionNumber. |
|                |                |                | There is no    |
|                |                |                | interpolation  |
|                |                |                | between Nonl i |
|                |                |                | nearShuntCompe |
|                |                |                | n              |
|                |                |                | storPoint(-s). |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#SignalDescriptor .container .group}
[#SignalDescriptor](#SignalDescriptor)

**SignalDescriptor**

DetailedModelDescription

Describes the signals both internal signals that connect different
functions or external signals.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  ACDCTerminal        0..1   [ACDCTerminal \<                   The terminal for
                             #ACDCTerminal\>]{.title-ref}\_\_   this signal
                                                                descriptor.

  Dyna                0..1   [DynamicsFunctio nBlock            The dynamics
  micsFunctionBlock          \<#Dynamics                        function block to
                             FunctionBlock\>]{.title-ref}\_\_   which this signal
                                                                belongs to.
  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  mRID                0..1   [St ring](#String)                 see [Detaile dModelDescriptor
                                                                \<#DetailedModelDe
                                                                scriptor.mRID\>]{.title-ref}\_\_

  Detailed            0..1   [Detail edModelTypeDynami cs       see [DetailedMod elDescriptor
  ModelTypeDynamics          \<#DetailedMode                    \<#De tailedModelDescri
                             lTypeDynamics\>]{.title-ref}\_\_   ptor.DetailedMode
                                                                lTypeDynamics\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#StateVariable .container .group}
[#StateVariable](#StateVariable)

**StateVariable**

StateVariables

An abstract class for state variables.
:::

::: {#Switch .container .group}
[#Switch](#Switch)

**Switch**

Wires

A generic device designed to close, or open, or both, one or more
electric circuits. All switches are two terminal devices including
grounding switches. The ACDCTerminal.connected at the two sides of the
switch shall not be considered for assessing switch connectivity, i.e.
only Switch.open, .normalOpen and .locked are relevant.

**Inherited Members**

  ------------- ------ ---------------------- -------------------------------------
  BaseVoltage   0..1   [BaseVolta             see [ConductingEquipme nt
                       ge](#BaseVoltage)      \<#ConductingEquip
                                              ment.BaseVoltage\>]{.title-ref}\_\_

  ------------- ------ ---------------------- -------------------------------------

  ------------------- ------ ---------------------------------- ----------------------------------
  inService           1..1   [Bool ean](#Boolean)               see [E quipment \<#Equipm
                                                                ent.inService\>]{.title-ref}\_\_

  E quipmentContainer 1..1   [Equipment Container \<#Equip      see [Equipment \<#Equipment.Equip
                             mentContainer\>]{.title-ref}\_\_   mentContainer\>]{.title-ref}\_\_
  ------------------- ------ ---------------------------------- ----------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#SynchronousMachineDetailed .container .group}
[#SynchronousMachineDetailed](#SynchronousMachineDetailed)

**SynchronousMachineDetailed**

SynchronousMachineDynamics

All synchronous machine detailed types use a subset of the same data
parameters and input/output variables.

The several variations differ in the following ways:

-   the number of equivalent windings that are included;
-   the way in which saturation is incorporated into the model;

\- whether or not "subtransient saliency" (*X\'\'q* not = *X\'\'d*) is
represented.

It is not necessary for each simulation tool to have separate models for
each of the model types. The same model can often be used for several
types by alternative logic within the model. Also, differences in
saturation representation might not result in significant model
performance differences so model substitutions are often acceptable.

**Native Members**

  ------------------- ------ ----------------------------- -------------------
  efdBaseRatio        1..1   [Float](#Float)               Ratio (exciter
                                                           voltage/generator
                                                           voltage) of *Efd*
                                                           bases of exciter
                                                           and generator
                                                           models (\> 0).
                                                           Typical value = 1.

  ifdBaseType         1..1   [IfdBaseKind](#IfdBaseKind)   Excitation base
                                                           system mode. It
                                                           should be equal to
                                                           the value of
                                                           *WLMDV* given by
                                                           the user. *WLMDV*
                                                           is the PU ratio
                                                           between the field
                                                           voltage and the
                                                           excitation current:
                                                           *Efd* = *WLMDV* x
                                                           *Ifd*. Typical
                                                           value = ifag.

  saturationFactor    1..1   [Float](#Float)               Saturation factor
                                                           at rated terminal
                                                           voltage (*S1*) (\>=
                                                           0). Defined by
                                                           defined by
                                                           *S*(*E1*) in the
                                                           Sync
                                                           hronousMachineSat
                                                           urationParameters
                                                           diagram. Typical
                                                           value = 0,02.

  sa                  1..1   [Float](#Float)               Saturation factor
  turationFactor120                                        at 120 % of rated
                                                           terminal voltage
                                                           (*S12*) (\>=
                                                           Rotating
                                                           MachineDynamics.s
                                                           aturationFactor).
                                                           Defined by
                                                           *S*(*E2*) in the
                                                           Sync
                                                           hronousMachineSat
                                                           urationParameters
                                                           diagram. Typical
                                                           value = 0,12.

  saturat             1..1   [Float](#Float)               Quadrature-axis
  ionFactor120QAxis                                        saturation factor
                                                           at 120% of rated
                                                           terminal voltage
                                                           (*S12q*) (\>=
                                                           SynchonousMachi
                                                           neDetailed.satura
                                                           tionFactorQAxis).
                                                           Typical value =
                                                           0,12.

  satu                1..1   [Float](#Float)               Quadrature-axis
  rationFactorQAxis                                        saturation factor
                                                           at rated terminal
                                                           voltage (*S1q*)
                                                           (\>= 0). Typical
                                                           value = 0,02.
  ------------------- ------ ----------------------------- -------------------

**Inherited Members**

  ------------------- ------ ---------------------------------- ----------------------------------
  S ynchronousMachine 0..1   [Synchrono usMachine \<#Synch      see [Synchronou sMachineDynamics
                             ronousMachine\>]{.title-ref}\_\_   \<#SynchronousMach
                                                                ineDynamics.Synch
                                                                ronousMachine\>]{.title-ref}\_\_

  ------------------- ------ ---------------------------------- ----------------------------------

  ------------------- ------ ------------------- ----------------------------------
  damping             1..1   [Float](#Float)     see [RotatingMa chineDynamics \<#R
                                                 otatingMachineDyn
                                                 amics.damping\>]{.title-ref}\_\_

  inertia             1..1   [Seco               see [RotatingMa chineDynamics \<#R
                             nds](#Seconds)      otatingMachineDyn
                                                 amics.inertia\>]{.title-ref}\_\_

  stato               1..1   [PU](#PU)           see [Rotating MachineDynamics \<
  rLeakageReactance                              #RotatingMachineD
                                                 ynamics.statorLea
                                                 kageReactance\>]{.title-ref}\_\_

  statorResistance    1..1   [PU](#PU)           see [Ro tatingMachineDyna mics
                                                 \<#RotatingMa chineDynamics.sta
                                                 torResistance\>]{.title-ref}\_\_
  ------------------- ------ ------------------- ----------------------------------

  --------- ------ ------------------------ ---------------------------------------
  mRID      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.mRID\>]{.title-ref}\_\_

  enabled   1..1   [Boolean](#Boolean)      see [DynamicsFunct ionBlock
                                            \<#DynamicsFun
                                            ctionBlock.enabled\>]{.title-ref}\_\_

  name      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.name\>]{.title-ref}\_\_
  --------- ------ ------------------------ ---------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#SynchronousMachineDynamics .container .group}
[#SynchronousMachineDynamics](#SynchronousMachineDynamics)

**SynchronousMachineDynamics**

SynchronousMachineDynamics

Synchronous machine whose behaviour is described by reference to a
standard model expressed in one of the following forms:

\- simplified (or classical), where a group of generators or motors is
not modelled in detail;

-   detailed, in equivalent circuit form;
-   detailed, in time constant reactance form; or
-   by definition of a user-defined model.

It is a common practice to represent small generators by a negative load
rather than by a dynamic generator model when performing dynamics
simulations. In this case, a SynchronousMachine in the static model is
not represented by anything in the dynamics model, instead it is treated
as an ordinary load.

Parameter details:

1.  Synchronous machine parameters such as *Xl, Xd, Xp* etc. are
    actually used as inductances in the models, but are commonly
    referred to as reactances since, at nominal frequency, the PU values
    are the same. However, some references use the symbol *L* instead of
    *X*.

**Native Members**

  ------------------- ------ ---------------------------------- -------------------
  S ynchronousMachine 0..1   [Synchrono usMachine \<#Synch      Synchronous machine
                             ronousMachine\>]{.title-ref}\_\_   to which
                                                                synchronous machine
                                                                dynamics model
                                                                applies.

  ------------------- ------ ---------------------------------- -------------------

**Inherited Members**

  ------------------- ------ ------------------- ----------------------------------
  damping             1..1   [Float](#Float)     see [RotatingMa chineDynamics \<#R
                                                 otatingMachineDyn
                                                 amics.damping\>]{.title-ref}\_\_

  inertia             1..1   [Seco               see [RotatingMa chineDynamics \<#R
                             nds](#Seconds)      otatingMachineDyn
                                                 amics.inertia\>]{.title-ref}\_\_

  stato               1..1   [PU](#PU)           see [Rotating MachineDynamics \<
  rLeakageReactance                              #RotatingMachineD
                                                 ynamics.statorLea
                                                 kageReactance\>]{.title-ref}\_\_

  statorResistance    1..1   [PU](#PU)           see [Ro tatingMachineDyna mics
                                                 \<#RotatingMa chineDynamics.sta
                                                 torResistance\>]{.title-ref}\_\_
  ------------------- ------ ------------------- ----------------------------------

  --------- ------ ------------------------ ---------------------------------------
  mRID      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.mRID\>]{.title-ref}\_\_

  enabled   1..1   [Boolean](#Boolean)      see [DynamicsFunct ionBlock
                                            \<#DynamicsFun
                                            ctionBlock.enabled\>]{.title-ref}\_\_

  name      1..1   [String](#String)        see [DynamicsFu nctionBlock \<#Dynamics
                                            FunctionBlock.name\>]{.title-ref}\_\_
  --------- ------ ------------------------ ---------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#TapChanger .container .group}
[#TapChanger](#TapChanger)

**TapChanger**

Wires

Mechanism for changing transformer winding tap positions.

**Native Members**

+----------------+----------------+----------------+----------------+
| highStep       | 0..1           | [Int           | Highest        |
|                |                | e              | possible tap   |
|                |                | ger](#Integer) | step position, |
|                |                |                | advance from   |
|                |                |                | neutral.       |
|                |                |                |                |
|                |                |                | The attribute  |
|                |                |                | shall be       |
|                |                |                | greater than   |
|                |                |                | lowStep.       |
+----------------+----------------+----------------+----------------+
| lowStep        | 0..1           | [Int           | Lowest         |
|                |                | e              | possible tap   |
|                |                | ger](#Integer) | step position, |
|                |                |                | retard from    |
|                |                |                | neutral.       |
+----------------+----------------+----------------+----------------+
| neutralStep    | 0..1           | [Int           | The neutral    |
|                |                | e              | tap step       |
|                |                | ger](#Integer) | position for   |
|                |                |                | this winding.  |
|                |                |                |                |
|                |                |                | The attribute  |
|                |                |                | shall be equal |
|                |                |                | to or greater  |
|                |                |                | than lowStep   |
|                |                |                | and equal or   |
|                |                |                | less than      |
|                |                |                | highStep.      |
|                |                |                |                |
|                |                |                | It is the step |
|                |                |                | position where |
|                |                |                | the voltage is |
|                |                |                | neutralU when  |
|                |                |                | the other      |
|                |                |                | terminals of   |
|                |                |                | the            |
|                |                |                | transformer    |
|                |                |                | are at the     |
|                |                |                | ratedU. If     |
|                |                |                | there are      |
|                |                |                | other tap      |
|                |                |                | changers on    |
|                |                |                | the            |
|                |                |                | transformer    |
|                |                |                | those taps are |
|                |                |                | kept constant  |
|                |                |                | at their       |
|                |                |                | neutralStep.   |
+----------------+----------------+----------------+----------------+
| neutralU       | 0..1           | [Vol           | Voltage at     |
|                |                | t              | which the      |
|                |                | age](#Voltage) | winding        |
|                |                |                | operates at    |
|                |                |                | the neutral    |
|                |                |                | tap setting.   |
|                |                |                | It is the      |
|                |                |                | voltage at the |
|                |                |                | terminal of    |
|                |                |                | the Powe r     |
|                |                |                | TransformerEnd |
|                |                |                | associated     |
|                |                |                | with the tap   |
|                |                |                | changer when   |
|                |                |                | all tap        |
|                |                |                | changers on    |
|                |                |                | the            |
|                |                |                | transformer    |
|                |                |                | are at their   |
|                |                |                | neutralStep    |
|                |                |                | position.      |
|                |                |                | Normally       |
|                |                |                | neutralU of    |
|                |                |                | the tap        |
|                |                |                | changer is the |
|                |                |                | same as ratedU |
|                |                |                | of the Power T |
|                |                |                | ransformerEnd, |
|                |                |                | but it can     |
|                |                |                | differ in      |
|                |                |                | special cases  |
|                |                |                | such as when   |
|                |                |                | the tapping    |
|                |                |                | mechanism is   |
|                |                |                | separate from  |
|                |                |                | the winding    |
|                |                |                | more common on |
|                |                |                | lower voltage  |
|                |                |                | transformers.  |
|                |                |                |                |
|                |                |                | This attribute |
|                |                |                | is not         |
|                |                |                | relevant for   |
|                |                |                | PhaseTapChang  |
|                |                |                | e              |
|                |                |                | rAsymmetrical, |
|                |                |                | PhaseTapCha n  |
|                |                |                | gerSymmetrical |
|                |                |                | and PhaseTa p  |
|                |                |                | ChangerLinear. |
+----------------+----------------+----------------+----------------+
| normalStep     | 0..1           | [Int           | The tap step   |
|                |                | e              | position used  |
|                |                | ger](#Integer) | in \"normal\"  |
|                |                |                | network        |
|                |                |                | operation for  |
|                |                |                | this winding.  |
|                |                |                | For a          |
|                |                |                | \"Fixed\" tap  |
|                |                |                | changer        |
|                |                |                | indicates the  |
|                |                |                | current        |
|                |                |                | physical tap   |
|                |                |                | setting.       |
|                |                |                |                |
|                |                |                | The attribute  |
|                |                |                | shall be equal |
|                |                |                | to or greater  |
|                |                |                | than lowStep   |
|                |                |                | and equal to   |
|                |                |                | or less than   |
|                |                |                | highStep.      |
+----------------+----------------+----------------+----------------+
| step           | 1..1           | [Flo           | Tap changer    |
|                |                | at](#Float)    | position.      |
|                |                |                |                |
|                |                |                | Starting step  |
|                |                |                | for a steady   |
|                |                |                | state          |
|                |                |                | solution. Non  |
|                |                |                | integer values |
|                |                |                | are allowed to |
|                |                |                | support        |
|                |                |                | continuous tap |
|                |                |                | variables. The |
|                |                |                | reasons for    |
|                |                |                | continuous     |
|                |                |                | value are to   |
|                |                |                | support study  |
|                |                |                | cases where no |
|                |                |                | discrete tap   |
|                |                |                | changer has    |
|                |                |                | yet been       |
|                |                |                | designed, a    |
|                |                |                | solution where |
|                |                |                | a narrow       |
|                |                |                | voltage band   |
|                |                |                | forces the tap |
|                |                |                | step to        |
|                |                |                | oscillate or   |
|                |                |                | to accommodate |
|                |                |                | for a          |
|                |                |                | continuous     |
|                |                |                | solution as    |
|                |                |                | input.         |
|                |                |                |                |
|                |                |                | The attribute  |
|                |                |                | shall be equal |
|                |                |                | to or greater  |
|                |                |                | than lowStep   |
|                |                |                | and equal to   |
|                |                |                | or less than   |
|                |                |                | highStep.      |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.mRID\>]{.title-ref}\_\_

  name   1..1   [String](#String)      see [Po werSystemResource \<#Powe
                                       rSystemResource.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

::: {#TransformerEnd .container .group}
[#TransformerEnd](#TransformerEnd)

**TransformerEnd**

Wires

A conducting connection point of a power transformer. It corresponds to
a physical transformer winding terminal. In earlier CIM versions, the
TransformerWinding class served a similar purpose, but this class is
more flexible because it associates to terminal but is not a
specialization of ConductingEquipment.

**Native Members**

+----------------+----------------+----------------+----------------+
| mRID           | 1..1           | [S trin        | Master         |
|                |                | g](#String)    | resource       |
|                |                |                | identifier     |
|                |                |                | issued by a    |
|                |                |                | model          |
|                |                |                | authority. The |
|                |                |                | mRID is unique |
|                |                |                | within an      |
|                |                |                | exchange       |
|                |                |                | context.       |
|                |                |                | Global         |
|                |                |                | uniqueness is  |
|                |                |                | easily         |
|                |                |                | achieved by    |
|                |                |                | using a UUID,  |
|                |                |                | as specified   |
|                |                |                | in IETF RFC    |
|                |                |                | 4122, for the  |
|                |                |                | mRID. The use  |
|                |                |                | of UUID is     |
|                |                |                | strongly       |
|                |                |                | recommended.   |
|                |                |                |                |
|                |                |                | For CIMXML     |
|                |                |                | data files in  |
|                |                |                | RDF syntax     |
|                |                |                | conforming to  |
|                |                |                | IEC 61970-552, |
|                |                |                | the mRID is    |
|                |                |                | mapped to      |
|                |                |                | rdf:ID or      |
|                |                |                | rdf:about      |
|                |                |                | attributes     |
|                |                |                | that identify  |
|                |                |                | CIM object     |
|                |                |                | elements.      |
+----------------+----------------+----------------+----------------+
| endNumber      | 1..1           | [Int           | Number for     |
|                |                | e              | this           |
|                |                | ger](#Integer) | transformer    |
|                |                |                | end,           |
|                |                |                | corresponding  |
|                |                |                | to the end\'s  |
|                |                |                | order in the   |
|                |                |                | power          |
|                |                |                | transformer    |
|                |                |                | vector group   |
|                |                |                | or phase angle |
|                |                |                | clock number.  |
|                |                |                | Highest        |
|                |                |                | voltage        |
|                |                |                | winding should |
|                |                |                | be 1. Each end |
|                |                |                | within a power |
|                |                |                | transformer    |
|                |                |                | should have a  |
|                |                |                | unique         |
|                |                |                | subsequent end |
|                |                |                | number. Note   |
|                |                |                | the            |
|                |                |                | transformer    |
|                |                |                | end number     |
|                |                |                | need not match |
|                |                |                | the terminal   |
|                |                |                | sequence       |
|                |                |                | number.        |
+----------------+----------------+----------------+----------------+
| grounded       | 1..1           | [Boo           | Used only for  |
|                |                | l              | Yn and Zn      |
|                |                | ean](#Boolean) | connections    |
|                |                |                | indicated by   |
|                |                |                | Power T        |
|                |                |                | ransformerEnd. |
|                |                |                | c              |
|                |                |                | onnectionKind. |
|                |                |                | If true, the   |
|                |                |                | neutral is     |
|                |                |                | grounded and   |
|                |                |                | attributes     |
|                |                |                | Transfo r      |
|                |                |                | merEnd.rground |
|                |                |                | and Transfo r  |
|                |                |                | merEnd.xground |
|                |                |                | are required.  |
|                |                |                | If false, the  |
|                |                |                | attributes     |
|                |                |                | Transfo r      |
|                |                |                | merEnd.rground |
|                |                |                | and Transfo r  |
|                |                |                | merEnd.xground |
|                |                |                | are not        |
|                |                |                | considered.    |
+----------------+----------------+----------------+----------------+
| name           | 1..1           | [S trin        | The name is    |
|                |                | g](#String)    | any free human |
|                |                |                | readable and   |
|                |                |                | possibly non   |
|                |                |                | unique text    |
|                |                |                | naming the     |
|                |                |                | object.        |
+----------------+----------------+----------------+----------------+
| rground        | 1..1           | [Resistanc e   | Resistance     |
|                |                | \<#            | part of        |
|                |                | R              | neutral        |
|                |                | esistance\>]{. | impedance.     |
|                |                | title-ref}\_\_ | Zero indicates |
|                |                |                | solidly        |
|                |                |                | grounded or    |
|                |                |                | grounded       |
|                |                |                | through a      |
|                |                |                | reactor.       |
+----------------+----------------+----------------+----------------+
| xground        | 1..1           | [Reactan ce \< | Reactance part |
|                |                | #              | of neutral     |
|                |                | Reactance\>]{. | impedance.     |
|                |                | title-ref}\_\_ | Zero indicates |
|                |                |                | solidly        |
|                |                |                | grounded or    |
|                |                |                | grounded       |
|                |                |                | through a      |
|                |                |                | reactor.       |
+----------------+----------------+----------------+----------------+
| BaseVoltage    | 1..1           | [B aseVoltage  | Base voltage   |
|                |                | \<#B           | of the         |
|                |                | a              | transformer    |
|                |                | seVoltage\>]{. | end. This is   |
|                |                | title-ref}\_\_ | essential for  |
|                |                |                | PU             |
|                |                |                | calculation.   |
+----------------+----------------+----------------+----------------+
| Terminal       | 1..1           | [Termi         | Terminal of    |
|                |                | n              | the power      |
|                |                | al](#Terminal) | transformer to |
|                |                |                | which this     |
|                |                |                | transformer    |
|                |                |                | end belongs.   |
+----------------+----------------+----------------+----------------+

**Inherited Members**

  ------ ------ ---------------------- -----------------------------------------
  mRID   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.mRID\>]{.title-ref}\_\_

  name   0..1   [String](#String)      see [IdentifiedObject \<#I
                                       dentifiedObject.name\>]{.title-ref}\_\_
  ------ ------ ---------------------- -----------------------------------------
:::

# Enumerations

::: {#AsynchronousMachineKind .container .group}
[#AsynchronousMachineKind](#AsynchronousMachineKind)

**AsynchronousMachineKind**

Wires

Kind of Asynchronous Machine.

  ----------- ------------------------------------------
  generator   The Asynchronous Machine is a generator.
  motor       The Asynchronous Machine is a motor.
  ----------- ------------------------------------------
:::

::: {#BatteryStateKind .container .group}
[#BatteryStateKind](#BatteryStateKind)

**BatteryStateKind**

Production

The state of the battery unit.

  -------------
  charging
  discharging
  empty
  full
  waiting
  -------------
:::

::: {#CsOperatingModeKind .container .group}
[#CsOperatingModeKind](#CsOperatingModeKind)

**CsOperatingModeKind**

DC

Operating mode for DC line operating as Current Source Converter.

  ----------- ----------------------------------------------------------
  inverter    Operating as inverter, which is the power receiving end.
  rectifier   Operating as rectifier, which is the power sending end.
  ----------- ----------------------------------------------------------
:::

::: {#CsPpccControlKind .container .group}
[#CsPpccControlKind](#CsPpccControlKind)

**CsPpccControlKind**

DC

Active power control modes for DC line operating as Current Source
Converter.

  ------------- -------------------------------------------------------
  activePower   Control is active power control at AC side, at point of
                common coupling. Target is provided by
                ACDCConverter.targetPpcc.

  dcCurrent     Control is DC current with target value provided by
                CsConverter.targetIdc.

  dcVoltage     Control is DC voltage with target value provided by
                ACDCConverter.targetUdc.
  ------------- -------------------------------------------------------
:::

::: {#CurveStyle .container .group}
[#CurveStyle](#CurveStyle)

**CurveStyle**

Core

Style or shape of curve.

  ---------------------
  constantYValue
  straightLineYValues
  ---------------------
:::

::: {#DCPolarityKind .container .group}
[#DCPolarityKind](#DCPolarityKind)

**DCPolarityKind**

DC

Polarity for DC circuits.

  ---------- ----------------------------------------------------------
  middle     Middle pole. The converter terminal is the midpoint in a
             bipolar or symmetric monopole configuration. The midpoint
             can be grounded and/or have a metallic return.

  negative   Negative pole. The converter terminal is intended to
             operate at a negative voltage relative the midpoint or
             positive terminal.

  positive   Positive pole. The converter terminal is intended to
             operate at a positive voltage relative the midpoint or
             negative terminal.
  ---------- ----------------------------------------------------------
:::

::: {#DCSourceKind .container .group}
[#DCSourceKind](#DCSourceKind)

**DCSourceKind**

Emtiop

  -------------- ------------------------------------------------------
  battery        Represent the DCEnergySource with a nonlinear battery
                 model, which should respond to state-of-charge (SoC)
                 controls.

  load           For electronic loads. Passive loads can be represented
                 in DCShunt.

  photoVoltaic   Represent the DCEnergySource with a nonlinear PV panel
                 model, which should respond to maximum power point
                 tracking (MPPT) control
  -------------- ------------------------------------------------------
:::

::: {#DCTerminalPolarityKind .container .group}
[#DCTerminalPolarityKind](#DCTerminalPolarityKind)

**DCTerminalPolarityKind**

DC

Polarity for DC terminal. Used in DC system configurations that have
explicit polarity of the terminals, e.g., voltage source converter (VSC)
technology.

  ---------- --------------------
  negative   Negative terminal.
  positive   Positive terminal.
  ---------- --------------------
:::

::: {#IEEECigreAPIInputKind .container .group}
[#IEEECigreAPIInputKind](#IEEECigreAPIInputKind)

**IEEECigreAPIInputKind**

Emtiop

  ------------------------ --------------------------------------------
  acCurrent                AC current from inverter into the AC filter.
                           Requires the phase attribute. Typically in
                           Amperes, but the CIGRE TB 958 API should be
                           used to verify units.

  acCurrentGrid            AC current from AC filter into the grid.
                           Requires the phase attribute. Typically in
                           Amperes, but the CIGRE TB 958 API should be
                           used to verify units.

  acVoltage                AC voltage at the filter-to-grid connection
                           point. Requires the phase attribute.
                           Typically in Volts, but the CIGRE TB 958 API
                           should be used to verify units.

  activePowerReference     Active power control reference. Typically in
                           per-unit but the CIGRE TB 958 API should be
                           used to verify units.

  apiDefined               Another kind of input or control signal not
                           enumerated in CIM. Use the CIGRE TB 958 API
                           for more information.

  dcCurrent                DC current into the inverter stage, if DC
                           bus modeling applies. Typically in Amperes,
                           but the DLL API should be used to verify
                           units.

  dcMPPTVoltage            DC voltage command from the maximum power
                           point tracking system, if DC bus modeling
                           applies. Typically in Volts, but the DLL API
                           should be used to verify units.

  dcVoltage                DC voltage at the inverter stage, if DC bus
                           modeling applies. Typically in Volts, but
                           the CIGRE TB 958 API should be used to
                           verify units.

  reactivePowerReference   Reactive power control reference. Typically
                           in per-unit but the CIGRE TB 958 API should
                           be used to verify units.

  voltageReference         Voltage control reference. Typically in
                           per-unit and positive sequence, but the
                           CIGRE TB 958 API should be used to verify
                           units.
  ------------------------ --------------------------------------------
:::

::: {#IEEECigreAPIModeKind .container .group}
[#IEEECigreAPIModeKind](#IEEECigreAPIModeKind)

**IEEECigreAPIModeKind**

Emtiop

  -------------- ------------------------------------------------------
  SupportsBoth   The CIGRE TB 958 model runs in either EMT or RMS
                 simulations.

  SupportsEMT    The CIGRE TB 958 model runs in EMT but not RMS
                 simulations.

  SupportsNone   This CIGRE TB 958 model is unusable.

  SupportsRMS    The CIGRE TB 958 model runs in RMS simulation, e.g.,
                 power flow, short-circuit, positive sequence dynamics,
                 transient stability. It does not run in EMT
                 simulation.
  -------------- ------------------------------------------------------
:::

::: {#IEEECigreAPIOutputKind .container .group}
[#IEEECigreAPIOutputKind](#IEEECigreAPIOutputKind)

**IEEECigreAPIOutputKind**

Emtiop

  ----------------- ---------------------------------------------------
  activePower       Active power from internal calculation; a
                    convenience output.

  apiDefined        Typically a convenience output for plotting and
                    analysis. Use CIGRE TB 958 API for more
                    information.

  modulationIndex   Modulation index for PWM switching in a detailed
                    VSC model. May be scaled by Vdc/2 in an average
                    model. Requires the phase attribute. If these
                    outputs are not provided, then vscVoltage outputs
                    shall be provided.

  pllFrequency      Frequency estimated from the model\'s phase locked
                    loop or similar algorithm.

  reactivePower     Reactive power from internal calculation; a
                    convenience output.

  rideThroughMode   A flag indicating fault-ride-through mode is
                    active, based on logic internal to the model.

  vscVoltage        VSC source voltage for an average model. Requires
                    the phase attribute. If these outputs are not
                    provided then modulationIndex outputs shall be
                    provided.
  ----------------- ---------------------------------------------------
:::

::: {#IEEECigreAPIParameterKind .container .group}
[#IEEECigreAPIParameterKind](#IEEECigreAPIParameterKind)

**IEEECigreAPIParameterKind**

Emtiop

Indicates the type and size (bytes) of a parameter, as documented in
IEEE_Cigre_DLLInterface_types.h from CIGRE TB 958.

  ------------
  Char_Ptr
  Char_Val
  Int16_Val
  Int32_Val
  Int8_Val
  Real32_Val
  Real64_Val
  Uint16_Val
  Uint32_Val
  Uint8_Val
  ------------
:::

::: {#IfdBaseKind .container .group}
[#IfdBaseKind](#IfdBaseKind)

**IfdBaseKind**

SynchronousMachineDynamics

Excitation base system mode.

  ------
  ifag
  iffl
  ifnl
  ------
:::

::: {#InputSignalKind .container .group}
[#InputSignalKind](#InputSignalKind)

**InputSignalKind**

PowerSystemStabilizerDynamics

Types of input signals. In dynamics modelling, commonly represented by
the *j* parameter.

  --------------------------------
  branchCurrent
  busFrequency
  busFrequencyDeviation
  busVoltage
  busVoltageDerivative
  fieldCurrent
  generatorAcceleratingPower
  generatorElectricalPower
  generatorMechanicalPower
  rotorAngularFrequencyDeviation
  rotorSpeed
  --------------------------------
:::

::: {#LimitKind .container .group}
[#LimitKind](#LimitKind)

**LimitKind**

OperationalLimits

Limit kinds.

+-----------------------------------+-----------------------------------+
| alarmVoltage                      | Voltage alarm.                    |
+-----------------------------------+-----------------------------------+
| highVoltage                       | Referring to the rating of the    |
|                                   | equipments, a voltage too high    |
|                                   | can lead to accelerated ageing or |
|                                   | the destruction of the equipment. |
|                                   |                                   |
|                                   | This limit type may or may not    |
|                                   | have duration.                    |
+-----------------------------------+-----------------------------------+
| lowVoltage                        | A too low voltage can disturb the |
|                                   | normal operation of some          |
|                                   | protections and transformer       |
|                                   | equipped with on-load tap         |
|                                   | changers, electronic power        |
|                                   | devices or can affect the         |
|                                   | behaviour of the auxiliaries of   |
|                                   | generation units.                 |
|                                   |                                   |
|                                   | This limit type may or may not    |
|                                   | have duration.                    |
+-----------------------------------+-----------------------------------+
| operationalVoltageLimit           | Operational voltage limit.        |
+-----------------------------------+-----------------------------------+
| patl                              | The Permanent Admissible          |
|                                   | Transmission Loading (PATL) is    |
|                                   | the loading in amperes, MVA or MW |
|                                   | that can be accepted by a network |
|                                   | branch for an unlimited duration  |
|                                   | without any risk for the          |
|                                   | material.                         |
|                                   |                                   |
|                                   | The Operati                       |
|                                   | onnalLimitType.isInfiniteDuration |
|                                   | is set to true. There shall be    |
|                                   | only one OperationalLimitType of  |
|                                   | kind PATL per OperationalLimitSet |
|                                   | if the PATL is                    |
|                                   | ApparentPowerLimit,               |
|                                   | ActivePowerLimit, or CurrentLimit |
|                                   | for a given Terminal or           |
|                                   | Equipment.                        |
+-----------------------------------+-----------------------------------+
| patlt                             | Permanent Admissible Transmission |
|                                   | Loading Threshold (PATLT) is a    |
|                                   | value in engineering units        |
|                                   | defined for PATL and calculated   |
|                                   | using a percentage less than 100  |
|                                   | % of the PATL type intended to    |
|                                   | alert operators of an arising     |
|                                   | condition. The percentage should  |
|                                   | be given in the name of the       |
|                                   | OperationalLimitSet. The          |
|                                   | aceptableDuration is another way  |
|                                   | to express the severity of the    |
|                                   | limit.                            |
+-----------------------------------+-----------------------------------+
| stability                         | Stability.                        |
+-----------------------------------+-----------------------------------+
| tatl                              | Temporarily Admissible            |
|                                   | Transmission Loading (TATL) which |
|                                   | is the loading in amperes, MVA or |
|                                   | MW that can be accepted by a      |
|                                   | branch for a certain limited      |
|                                   | duration.                         |
|                                   |                                   |
|                                   | The TATL can be defined in        |
|                                   | different ways:                   |
|                                   |                                   |
|                                   | -   as a fixed percentage of the  |
|                                   |     PATL for a given time (for    |
|                                   |     example, 115% of the PATL     |
|                                   |     that can be accepted during   |
|                                   |     15 minutes),                  |
|                                   |                                   |
|                                   | ```{=html}                        |
|                                   | <!-- -->                          |
|                                   | ```                               |
|                                   | -   pairs of TATL type and        |
|                                   |     Duration calculated for each  |
|                                   |     line taking into account its  |
|                                   |     particular configuration and  |
|                                   |     conditions of functioning     |
|                                   |     (for example, it can define a |
|                                   |     TATL acceptable during 20     |
|                                   |     minutes and another one       |
|                                   |     acceptable during 10          |
|                                   |     minutes).                     |
|                                   |                                   |
|                                   | Such a definition of TATL can     |
|                                   | depend on the initial operating   |
|                                   | conditions of the network element |
|                                   | (sag situation of a line).        |
|                                   |                                   |
|                                   | The duration attribute can be     |
|                                   | used to define several TATL limit |
|                                   | types. Hence multiple TATL limit  |
|                                   | values may exist having different |
|                                   | durations.                        |
+-----------------------------------+-----------------------------------+
| tc                                | Tripping Current (TC) is the      |
|                                   | ultimate intensity without any    |
|                                   | delay. It is defined as the       |
|                                   | threshold the line will trip      |
|                                   | without any possible remedial     |
|                                   | actions.                          |
|                                   |                                   |
|                                   | The tripping of the network       |
|                                   | element is ordered by protections |
|                                   | against short circuits or by      |
|                                   | overload protections, but in any  |
|                                   | case, the activation delay of     |
|                                   | these protections is not          |
|                                   | compatible with the reaction      |
|                                   | delay of an operator (less than   |
|                                   | one minute).                      |
|                                   |                                   |
|                                   | The duration is always zero if    |
|                                   | the Operat                        |
|                                   | ionalLimitType.acceptableDuration |
|                                   | is exchanged. Only one limit      |
|                                   | value exists for the TC type.     |
+-----------------------------------+-----------------------------------+
| tct                               | Tripping Current Threshold (TCT)  |
|                                   | is a value in engineering units   |
|                                   | defined for TC and calculated     |
|                                   | using a percentage less than 100  |
|                                   | % of the TC type intended to      |
|                                   | alert operators of an arising     |
|                                   | condition. The percentage should  |
|                                   | be given in the name of the       |
|                                   | OperationalLimitSet. The          |
|                                   | aceptableDuration is another way  |
|                                   | to express the severity of the    |
|                                   | limit.                            |
+-----------------------------------+-----------------------------------+
| warningVoltage                    | Voltage warning.                  |
+-----------------------------------+-----------------------------------+
:::

::: {#NthAmModelKind .container .group}
[#NthAmModelKind](#NthAmModelKind)

**NthAmModelKind**

Emtiop

Application of this model.

  -------------------------
  currentCompensation
  excitationSystem
  load
  loadController
  machine
  powerSystemStabilizer
  protection
  renewableEnergyResource
  signalPlayback
  staticVarAndFACTS
  turbineGovernor
  -------------------------
:::

::: {#NthAmModelNameKind .container .group}
[#NthAmModelNameKind](#NthAmModelNameKind)

**NthAmModelNameKind**

Emtiop

Describes the naming category for dynamic models recognized by NERC.

  -------
  AUX
  DGS
  DYD
  DYR
  Other
  -------
:::

::: {#NthAmModelStatusKind .container .group}
[#NthAmModelStatusKind](#NthAmModelStatusKind)

**NthAmModelStatusKind**

Emtiop

  ------------ --------------------------------------------------------
  allowed      NERC allows this model for interconnection-wide studies.
               NERC used to keep a list of allowed models; currently,
               it lists only prohibited models.

  deprecated   NERC allows this model in interconnection-wide studies,
               but other models are more suitable.

  prohibited   NERC prohibits use of this model in interconnection-side
               studies. Some legacy network examples may still use this
               model.
  ------------ --------------------------------------------------------
:::

::: {#OperationalLimitDirectionKind .container .group}
[#OperationalLimitDirectionKind](#OperationalLimitDirectionKind)

**OperationalLimitDirectionKind**

OperationalLimits

The direction attribute describes the side of a limit that is a
violation.

  --------------- -----------------------------------------------------
  absoluteValue   An absoluteValue limit means that a monitored
                  absolute value above the limit value is a violation.

  high            High means that a monitored value above the limit
                  value is a violation. If applied to a terminal flow,
                  the positive direction is into the terminal.

  low             Low means a monitored value below the limit is a
                  violation. If applied to a terminal flow, the
                  positive direction is into the terminal.
  --------------- -----------------------------------------------------
:::

::: {#PhaseShuntConnectionKind .container .group}
[#PhaseShuntConnectionKind](#PhaseShuntConnectionKind)

**PhaseShuntConnectionKind**

Wires

The configuration of phase connections for a single terminal device such
as a load or capacitor.

  ---- ----------------------------------------------------------------
  D    Delta connection.

  G    Ground connection; use when explicit connection to ground needs
       to be expressed in combination with the phase code, such as for
       electrical wire/cable or for meters.

  I    Independent winding, for single-phase connections.

  Y    Wye connection.

  Yn   Wye, with neutral brought out for grounding.
  ---- ----------------------------------------------------------------
:::

::: {#RotorKind .container .group}
[#RotorKind](#RotorKind)

**RotorKind**

SynchronousMachineDynamics

Type of rotor on physical machine.

  -------------
  roundRotor
  salientPole
  -------------
:::

::: {#SVCControlMode .container .group}
[#SVCControlMode](#SVCControlMode)

**SVCControlMode**

Wires

Static VAr Compensator control mode.

  --------------- -------------------------
  reactivePower   Reactive power control.
  voltage         Voltage control.
  --------------- -------------------------
:::

::: {#SinglePhaseKind .container .group}
[#SinglePhaseKind](#SinglePhaseKind)

**SinglePhaseKind**

Wires

Enumeration of phase identifiers used to designate the specific phase of
conducting equipment modelled as individual unbalanced phases.

Allows designation of specific phases for transmission and distribution
equipment, circuits and loads.

  ---- --------------------
  A    Phase A.
  B    Phase B.
  C    Phase C.
  N    Neutral.
  s1   Secondary phase 1.
  s2   Secondary phase 2.
  ---- --------------------
:::

::: {#SynchronousMachineKind .container .group}
[#SynchronousMachineKind](#SynchronousMachineKind)

**SynchronousMachineKind**

Wires

Synchronous machine type.

  -----------------------------
  condenser
  generator
  generatorOrCondenser
  generatorOrCondenserOrMotor
  generatorOrMotor
  motor
  motorOrCondenser
  -----------------------------
:::

::: {#SynchronousMachineModelKind .container .group}
[#SynchronousMachineModelKind](#SynchronousMachineModelKind)

**SynchronousMachineModelKind**

SynchronousMachineDynamics

Type of synchronous machine model used in dynamic simulation
applications.

  ----------------------------------
  subtransient
  subtransientSimplified
  subtransientSimplifiedDirectAxis
  subtransientTypeF
  subtransientTypeJ
  ----------------------------------
:::

::: {#SynchronousMachineOperatingMode .container .group}
[#SynchronousMachineOperatingMode](#SynchronousMachineOperatingMode)

**SynchronousMachineOperatingMode**

Wires

Synchronous machine operating mode.

  -----------
  condenser
  generator
  motor
  -----------
:::

::: {#UnitMultiplier .container .group}
[#UnitMultiplier](#UnitMultiplier)

**UnitMultiplier**

Domain

The unit multipliers defined for the CIM. When applied to unit symbols,
the unit symbol is treated as a derived unit. Regardless of the contents
of the unit symbol text, the unit symbol shall be treated as if it were
a single-character unit symbol. Unit symbols should not contain
multipliers, and it should be left to the multiplier to define the
multiple for an entire data type.

For example, if a unit symbol is \"m2Pers\" and the multiplier is \"k\",
then the value is k(m\*\*2/s), and the multiplier applies to the entire
final value, not to any individual part of the value. This can be
conceptualized by substituting a derived unit symbol for the unit type.
If one imagines that the symbol \"Þ\" represents the derived unit
\"m2Pers\", then applying the multiplier \"k\" can be conceptualized
simply as \"kÞ\".

For example, the SI unit for mass is \"kg\" and not \"g\". If the unit
symbol is defined as \"kg\", then the multiplier is applied to \"kg\" as
a whole and does not replace the \"k\" in front of the \"g\". In this
case, the multiplier of \"m\" would be used with the unit symbol of
\"kg\" to represent one gram. As a text string, this violates the
instructions in IEC 80000-1. However, because the unit symbol in CIM is
treated as a derived unit instead of as an SI unit, it makes more sense
to conceptualize the \"kg\" as if it were replaced by one of the
proposed replacements for the SI mass symbol. If one imagines that the
\"kg\" were replaced by a symbol \"Þ\", then it is easier to
conceptualize the multiplier \"m\" as creating the proper unit \"mÞ\",
and not the forbidden unit \"mkg\".

  -------
  E
  G
  M
  P
  T
  Y
  Z
  a
  c
  d
  da
  f
  h
  k
  m
  micro
  n
  none
  p
  y
  z
  -------
:::

::: {#UnitSymbol .container .group}
[#UnitSymbol](#UnitSymbol)

**UnitSymbol**

Domain

The derived units defined for usage in the CIM. In some cases, the
derived unit is equal to an SI unit. Whenever possible, the standard
derived symbol is used instead of the formula for the derived unit. For
example, the unit symbol Farad is defined as \"F\" instead of \"CPerV\".
In cases where a standard symbol does not exist for a derived unit, the
formula for the unit is used as the unit symbol. For example, density
does not have a standard symbol and so it is represented as
\"kgPerm\^3\". With the exception of the \"kg\", which is an SI unit,
the unit symbols do not contain multipliers and therefore represent the
base derived unit to which a multiplier can be applied as a whole.

Every unit symbol is treated as an unparseable text as if it were a
single-letter symbol. The meaning of each unit symbol is defined by the
accompanying descriptive text and not by the text contents of the unit
symbol.

To allow the widest possible range of serializations without requiring
special character handling, several substitutions are made which deviate
from the format described in IEC 80000-1. The division symbol \"/\" is
replaced by the letters \"Per\". Exponents are written in plain text
after the unit as \"m\^3\". The letters \"deg\" are used instead of the
degree symbol. Any clarification of the meaning for a substitution is
included in the description for the unit symbol.

Non-SI units are included in list of unit symbols to allow sources of
data to be correctly labelled with their non-SI units (for example, a
GPS sensor that is reporting numbers that represent feet instead of
meters). This allows software to use the unit symbol information
correctly convert and scale the raw data of those sources into SI-based
units.

The integer values are used for harmonization with IEC 61850.

  -----------------
  A
  A2
  A2h
  A2s
  APerA
  APerm
  Ah
  As
  Bq
  Btu
  C
  CPerkg
  CPerm2
  CPerm3
  F
  FPerm
  G
  Gy
  GyPers
  H
  HPerm
  Hz
  HzPerHz
  HzPers
  J
  JPerK
  JPerkg
  JPerkgK
  JPerm2
  JPerm3
  JPermol
  JPermolK
  JPers
  K
  KPers
  M
  Mx
  N
  NPerm
  Nm
  Oe
  Pa
  PaPers
  Pas
  Q
  Qh
  S
  SPerm
  Sv
  T
  V
  V2
  V2h
  VA
  VAh
  VAr
  VArh
  VPerHz
  VPerV
  VPerVA
  VPerVAr
  VPerm
  Vh
  Vs
  W
  WPerA
  WPerW
  WPerm2
  WPerm2sr
  WPermK
  WPers
  WPersr
  Wb
  Wh
  anglemin
  anglesec
  bar
  cd
  charPers
  character
  cosPhi
  count
  d
  dB
  dBm
  deg
  degC
  ft3
  gPerg
  gal
  h
  ha
  kat
  katPerm3
  kg
  kgPerJ
  kgPerm
  kgPerm3
  kgm
  kgm2
  kn
  l
  lPerh
  lPerl
  lPers
  lm
  lx
  m
  m2
  m2Pers
  m3
  m3Compensated
  m3Perh
  m3Perkg
  m3Pers
  m3Uncompensated
  mPerm3
  mPers
  mPers2
  min
  mmHg
  mol
  molPerkg
  molPerm3
  molPermol
  none
  ohm
  ohmPerm
  ohmm
  onePerHz
  onePerm
  ppm
  rad
  radPers
  radPers2
  rev
  rotPers
  s
  sPers
  sr
  therm
  tonne
  -----------------
:::

::: {#VsPpccControlKind .container .group}
[#VsPpccControlKind](#VsPpccControlKind)

**VsPpccControlKind**

DC

Types applicable to the control of real power and/or DC voltage by
voltage source converter.

  --------------------------------- -----------------------------------
  pPcc                              Control is real power at point of
                                    common coupling. The target value
                                    is provided by
                                    ACDCConverter.targetPpcc.

  pPccAndUdcDroop                   Control is active power at point of
                                    common coupling and local DC
                                    voltage, with the droop. Target
                                    values are provided by
                                    ACDCConverter.targetPpcc,
                                    ACDCConverter.targetUdc and
                                    VsConverter.droop.

  pPccAndUdcDroopPilot              Control is active power at point of
                                    common coupling and the pilot DC
                                    voltage, with the droop. The mode
                                    is used for Multi Terminal DC
                                    (MTDC) systems where multiple DC
                                    substations are connected to the DC
                                    transmission lines. The pilot
                                    voltage is then used to coordinate
                                    the control the DC voltage across
                                    the DC substations. Targets are
                                    provided by
                                    ACDCConverter.targetPpcc,
                                    ACDCConverter.targetUdc and
                                    VsConverter.droop.

  pPccAndUdcDroopWithCompensation   Control is active power at point of
                                    common coupling and compensated DC
                                    voltage, with the droop.
                                    Compensation factor is the
                                    resistance, as an approximation of
                                    the DC voltage of a common (real or
                                    virtual) node in the DC network.
                                    Targets are provided by
                                    ACDCConverter.targetPpcc,
                                    ACDCConverter.targetUdc,
                                    VsConverter.droop and
                                    VsConverter.droopCompensation.

  phasePcc                          Control is phase at point of common
                                    coupling. Target is provided by
                                    VsConverter.targetPhasePcc.

  udc                               Control is DC voltage with target
                                    value provided by
                                    ACDCConverter.targetUdc.
  --------------------------------- -----------------------------------
:::

::: {#VsQpccControlKind .container .group}
[#VsQpccControlKind](#VsQpccControlKind)

**VsQpccControlKind**

DC

Kind of reactive power control at point of common coupling for a voltage
source converter.

  ---------------------- ----------------------------------------------
  powerFactorPcc         Control is power factor at point of common
                         coupling. Target is provided by
                         VsConverter.targetPowerFactorPcc.

  pulseWidthModulation   No explicit control. Pulse-modulation factor
                         is directly set in magnitude
                         (VsConverter.targetPWMfactor) and phase
                         (VsConverter.targetPhasePcc).

  reactivePcc            Control is reactive power at point of common
                         coupling. Target is provided by
                         VsConverter.targetQpcc.

  voltagePcc             Control is voltage at point of common
                         coupling. Target is provided by
                         VsConverter.targetUpcc.
  ---------------------- ----------------------------------------------
:::

::: {#WindingConnection .container .group}
[#WindingConnection](#WindingConnection)

**WindingConnection**

Wires

Winding connection type.

  ----
  A
  D
  I
  Y
  Yn
  Z
  Zn
  ----
:::

# Compound Types

# Datatypes

::: {#ActivePower .container .group}
[#ActivePower](#ActivePower)

**ActivePower**

Domain

Product of RMS value of the voltage and the RMS value of the in-phase
component of the current.

XSD type: float
:::

::: {#ActivePowerPerCurrentFlow .container .group}
[#ActivePowerPerCurrentFlow](#ActivePowerPerCurrentFlow)

**ActivePowerPerCurrentFlow**

Domain

Active power variation with current flow.

XSD type: float
:::

::: {#AngleDegrees .container .group}
[#AngleDegrees](#AngleDegrees)

**AngleDegrees**

Domain

Measurement of angle in degrees.

XSD type: float
:::

::: {#AngleRadians .container .group}
[#AngleRadians](#AngleRadians)

**AngleRadians**

Domain

Phase angle in radians.

XSD type: float
:::

::: {#ApparentPower .container .group}
[#ApparentPower](#ApparentPower)

**ApparentPower**

Domain

Product of the RMS value of the voltage and the RMS value of the
current.

XSD type: float
:::

::: {#Capacitance .container .group}
[#Capacitance](#Capacitance)

**Capacitance**

Domain

Capacitive part of reactance (imaginary part of impedance), at rated
frequency.

XSD type: float
:::

::: {#Conductance .container .group}
[#Conductance](#Conductance)

**Conductance**

Domain

Factor by which voltage must be multiplied to give corresponding power
lost from a circuit. Real part of admittance.

XSD type: float
:::

::: {#CurrentFlow .container .group}
[#CurrentFlow](#CurrentFlow)

**CurrentFlow**

Domain

Electrical current with sign convention: positive flow is out of the
conducting equipment into the connectivity node. Can be both AC and DC.

XSD type: float
:::

::: {#Frequency .container .group}
[#Frequency](#Frequency)

**Frequency**

Domain

Cycles per second.

XSD type: float
:::

::: {#Inductance .container .group}
[#Inductance](#Inductance)

**Inductance**

Domain

Inductive part of reactance (imaginary part of impedance), at rated
frequency.

XSD type: float
:::

::: {#Length .container .group}
[#Length](#Length)

**Length**

Domain

Unit of length. It shall be a positive value or zero.

XSD type: float
:::

::: {#PU .container .group}
[#PU](#PU)

**PU**

Domain

Per Unit - a positive or negative value referred to a defined base.
Values typically range from -10 to +10.

XSD type: float
:::

::: {#PerCent .container .group}
[#PerCent](#PerCent)

**PerCent**

Domain

Percentage on a defined base. For example, specify as 100 to indicate at
the defined base.

XSD type: float
:::

::: {#Reactance .container .group}
[#Reactance](#Reactance)

**Reactance**

Domain

Reactance (imaginary part of impedance), at rated frequency.

XSD type: float
:::

::: {#ReactivePower .container .group}
[#ReactivePower](#ReactivePower)

**ReactivePower**

Domain

Product of RMS value of the voltage and the RMS value of the quadrature
component of the current.

XSD type: float
:::

::: {#RealEnergy .container .group}
[#RealEnergy](#RealEnergy)

**RealEnergy**

Domain

Real electrical energy.

XSD type: float
:::

::: {#Resistance .container .group}
[#Resistance](#Resistance)

**Resistance**

Domain

Resistance (real part of impedance).

XSD type: float
:::

::: {#RotationSpeed .container .group}
[#RotationSpeed](#RotationSpeed)

**RotationSpeed**

Domain

Number of revolutions per second.

XSD type: float
:::

::: {#Seconds .container .group}
[#Seconds](#Seconds)

**Seconds**

Domain

Time, in seconds.

XSD type: float
:::

::: {#Susceptance .container .group}
[#Susceptance](#Susceptance)

**Susceptance**

Domain

Imaginary part of admittance.

XSD type: float
:::

::: {#Voltage .container .group}
[#Voltage](#Voltage)

**Voltage**

Domain

Electrical voltage, can be both AC and DC.

XSD type: float
:::

::: {#VoltagePerReactivePower .container .group}
[#VoltagePerReactivePower](#VoltagePerReactivePower)

**VoltagePerReactivePower**

Domain

Voltage variation with reactive power.

XSD type: float
:::

# Primitive Types

::: {#Boolean .container .group}
[#Boolean](#Boolean)

**Boolean**

Domain

A type with the value space \"true\" and \"false\".

XSD type: boolean
:::

::: {#DateTime .container .group}
[#DateTime](#DateTime)

**DateTime**

Domain

Date and time as \"yyyy-mm-ddThh:mm:ss.sss\", which conforms with ISO
8601. UTC time zone is specified as \"yyyy-mm-ddThh:mm:ss.sssZ\". A
local timezone relative UTC is specified as
\"yyyy-mm-ddThh:mm:ss.sss-hh:mm\". The second component (shown here as
\"ss.sss\") could have any number of digits in its fractional part to
allow any kind of precision beyond seconds.

XSD type: dateTime
:::

::: {#Float .container .group}
[#Float](#Float)

**Float**

Domain

A floating point number. The range is unspecified and not limited.

XSD type: float
:::

::: {#Integer .container .group}
[#Integer](#Integer)

**Integer**

Domain

An integer number. The range is unspecified and not limited.

XSD type: integer
:::

::: {#String .container .group}
[#String](#String)

**String**

Domain

A string consisting of a sequence of characters. The character encoding
is UTF-8. The string length is unspecified and unlimited.

XSD type: string
:::
