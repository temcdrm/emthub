Profile Documentation
=====================

Profile namespace: http://opensource.ieee.org/emtiop01p01#

Concrete Classes
================

.. container:: group
   :name: ACDCConverterDCTerminal

   ` <#ACDCConverterDCTerminal>`__

   .. rubric:: ACDCConverterDCTerminal
      :name: acdcconverterdcterminal
      :class: concrete

   DC

   A DC electrical connection point at the AC/DC converter. The AC/DC
   converter is electrically connected also to the AC side. The AC
   connection is inherited from the AC conducting equipment in the same
   way as any other AC equipment. The AC/DC converter DC terminal is
   separate from generic DC terminal to restrict the connection with the
   AC side to AC/DC converter and so that no other DC conducting
   equipment can be connected to the AC side.

   .. rubric:: Native Members
      :name: native-members

   +----------------+----------------+----------------+----------------+
   | polarity       | 0..1           | `DC            | Represents the |
   |                |                | Polarity       | normal network |
   |                |                | Kind <#%20DCPo | polarity       |
   |                |                | larityKind>`__ | condition.     |
   |                |                |                | Depending on   |
   |                |                |                | the converter  |
   |                |                |                | configuration  |
   |                |                |                | the value      |
   |                |                |                | shall be set   |
   |                |                |                | as follows:    |
   |                |                |                |                |
   |                |                |                | - For a        |
   |                |                |                | monopole with  |
   |                |                |                | two converter  |
   |                |                |                | terminals use  |
   |                |                |                | DCPolarityKind |
   |                |                |                | "positive" and |
   |                |                |                | "negative".    |
   |                |                |                |                |
   |                |                |                | - For a        |
   |                |                |                | bi-pole or     |
   |                |                |                | symmetric      |
   |                |                |                | monopole with  |
   |                |                |                | three          |
   |                |                |                | converter      |
   |                |                |                | terminals use  |
   |                |                |                | DCPolarityKind |
   |                |                |                | "positive",    |
   |                |                |                | "middle" and   |
   |                |                |                | "negative".    |
   +----------------+----------------+----------------+----------------+
   | DCCond         | 0..1           | `ACDCC         | A DC converter |
   | u              |                | onverter <#ACD | terminal       |
   | ctingEquipment |                | CConverter>`__ | belong to an   |
   |                |                |                | DC converter.  |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members

   +--------+------+----------------------+-------------------------+
   | DCNode | 1..1 | `DCNode <#DCNode>`__ | see                     |
   |        |      |                      | `DCBaseTerminal <#DC    |
   |        |      |                      | BaseTerminal.DCNode>`__ |
   +--------+------+----------------------+-------------------------+

   +----------------+------+-------------------+-------------------+
   | sequenceNumber | 1..1 | `Inte             | see               |
   |                |      | ger <#Integer>`__ | `ACDCTerminal     |
   |                |      |                   |  <#ACDCTerminal.s |
   |                |      |                   | equenceNumber>`__ |
   +----------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: ACLineSegment

   ` <#ACLineSegment>`__

   .. rubric:: ACLineSegment
      :name: aclinesegment
      :class: concrete

   Wires

   A line segment is a conductor or combination of conductors, with
   consistent electrical characteristics along its length, building a
   single electrical system that carries alternating current between two
   points in the power system.

   The BaseVoltage at the two ends of a line segment shall have the same
   BaseVoltage.nominalVoltage. However, boundary lines may have slightly
   different BaseVoltage.nominalVoltages and variation is allowed.
   Larger voltage difference in general requires use of an equivalent
   branch.

   Line segment impedances can be either directly described in
   electrical terms or physical line detail can be provided from which
   impedances can be calculated.

   **Directly described impedances**

   For symmetrical, transposed three phase line segments, it is
   sufficient to use attributes of the line segment, which describe
   impedances and admittances for the entire length of the line segment.
   Additionally, line segment impedances can be computed by using line
   segment length and associated per length impedances.

   Unbalanced modeling of impedances is supported by the per length
   phase impedance matrix (PerLengthPhaseImpedance) in conjunction with
   phase-to-sequence number mapping supplied by either
   ACLineSegmentPhase or WirePosition. The sequence numbers are
   referenced by the row and column attributes of the per length phase
   impedance matrix. This method enables single-phase and two-phase line
   segments, and transpositions of phases, to be described using the
   same per length phase impedance matrix. The length of the line
   segment is used in the computation of total impedance values for the
   line segment.

   **Line detail characteristics**

   There are three approaches to providing line detail and all use
   WireAssembly to supply line positions:

   -  Option 1 - WireAssembly supplies only line positions.
      ACLineSegmentPhase points to wire type and intraphase spacing and
      supplies the phase-to-sequence number mapping.
   -  Option 2 - WireAssembly supplies line position and, for each
      position, also supplies wire type and intraphase spacing.
      ACLineSegmentPhase supplies the phase-to-sequence number mapping.
   -  Option 3 - WireAssembly supplies line position and, for each
      position, also supplies wire type and intraphase spacing and
      phase. WireAssembly therefore supplies the phase-to-sequence
      number mapping and ACLineSegmentPhase is not needed.

   .. rubric:: Native Members
      :name: native-members-1

   +------+------+--------------------------+--------------------------+
   | b0ch | 1..1 | `Susce                   | Zero sequence shunt      |
   |      |      | ptance <#Susceptance>`__ | (charging) susceptance,  |
   |      |      |                          | uniformly distributed,   |
   |      |      |                          | of the entire line       |
   |      |      |                          | segment.                 |
   +------+------+--------------------------+--------------------------+
   | bch  | 1..1 | `Susce                   | Positive sequence shunt  |
   |      |      | ptance <#Susceptance>`__ | (charging) susceptance,  |
   |      |      |                          | uniformly distributed,   |
   |      |      |                          | of the entire line       |
   |      |      |                          | segment. This value      |
   |      |      |                          | represents the full      |
   |      |      |                          | charging over the full   |
   |      |      |                          | length of the line       |
   |      |      |                          | segment.                 |
   +------+------+--------------------------+--------------------------+
   | r    | 1..1 | `Res                     | Positive sequence series |
   |      |      | istance <#Resistance>`__ | resistance of the entire |
   |      |      |                          | line segment.            |
   +------+------+--------------------------+--------------------------+
   | r0   | 1..1 | `Res                     | Zero sequence series     |
   |      |      | istance <#Resistance>`__ | resistance of the entire |
   |      |      |                          | line segment.            |
   +------+------+--------------------------+--------------------------+
   | x    | 1..1 | `R                       | Positive sequence series |
   |      |      | eactance <#Reactance>`__ | reactance of the entire  |
   |      |      |                          | line segment.            |
   +------+------+--------------------------+--------------------------+
   | x0   | 1..1 | `R                       | Zero sequence series     |
   |      |      | eactance <#Reactance>`__ | reactance of the entire  |
   |      |      |                          | line segment.            |
   +------+------+--------------------------+--------------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-1

   ====== ==== ==================== =====================================
   length 1..1 `Length <#Length>`__ see `Conductor <#Conductor.length>`__
   ====== ==== ==================== =====================================

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: ACPointOfCommonCoupling

   ` <#ACPointOfCommonCoupling>`__

   .. rubric:: ACPointOfCommonCoupling
      :name: acpointofcommoncoupling
      :class: concrete

   Core

   Point of interconnection of the DC converter station to the adjacent
   AC system (IEC 60633).

   .. rubric:: Native Members
      :name: native-members-2

   +------------------+------+-------------------+-------------------+
   | ConnectivityNode | 0..1 | `Conne            | Connectivity node |
   |                  |      | ctivityNode <#Con | which is a point  |
   |                  |      | nectivityNode>`__ | of common         |
   |                  |      |                   | coupling AC.      |
   +------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-2

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `PointO                  |
   |      |      |                      | fCommonCoupling <#PointO |
   |      |      |                      | fCommonCoupling.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `PointO                  |
   |      |      |                      | fCommonCoupling <#PointO |
   |      |      |                      | fCommonCoupling.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: ApparentPowerLimit

   ` <#ApparentPowerLimit>`__

   .. rubric:: ApparentPowerLimit
      :name: apparentpowerlimit
      :class: concrete

   OperationalLimits

   Apparent power limit.

   .. rubric:: Native Members
      :name: native-members-3

   +-------+------+-------------------------+-------------------------+
   | value | 0..1 | `ApparentPo             | The apparent power      |
   |       |      | wer <#ApparentPower>`__ | limit. The attribute    |
   |       |      |                         | shall be a positive     |
   |       |      |                         | value or zero.          |
   +-------+------+-------------------------+-------------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-3

   +-------------------+------+-------------------+-------------------+
   | mRID              | 1..1 | `St               | see               |
   |                   |      | ring <#String>`__ | `Operationa       |
   |                   |      |                   | lLimit <#Operatio |
   |                   |      |                   | nalLimit.mRID>`__ |
   +-------------------+------+-------------------+-------------------+
   | name              | 1..1 | `St               | see               |
   |                   |      | ring <#String>`__ | `Operationa       |
   |                   |      |                   | lLimit <#Operatio |
   |                   |      |                   | nalLimit.name>`__ |
   +-------------------+------+-------------------+-------------------+
   | Op                | 0..1 | `Operational      | see               |
   | erationalLimitSet |      | LimitSet <#Operat | `Operatio         |
   |                   |      | ionalLimitSet>`__ | nalLimit <#Operat |
   |                   |      |                   | ionalLimit.Operat |
   |                   |      |                   | ionalLimitSet>`__ |
   +-------------------+------+-------------------+-------------------+
   | Ope               | 0..1 | `OperationalLi    | see               |
   | rationalLimitType |      | mitType <#Operati | `Operation        |
   |                   |      | onalLimitType>`__ | alLimit <#Operati |
   |                   |      |                   | onalLimit.Operati |
   |                   |      |                   | onalLimitType>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: AsynchronousMachine

   ` <#AsynchronousMachine>`__

   .. rubric:: AsynchronousMachine
      :name: asynchronousmachine
      :class: concrete

   Wires

   A rotating machine whose shaft rotates asynchronously with the
   electrical field. Also known as an induction machine with no external
   connection to the rotor windings, e.g. squirrel-cage induction
   machine.

   .. rubric:: Native Members
      :name: native-members-4

   +-------------------+------+-------------------+-------------------+
   | asynch            | 0..1 | `As               | Indicates the     |
   | ronousMachineType |      | ynchronousMachine | type of           |
   |                   |      | Kind <#Asynchrono | Asynchronous      |
   |                   |      | usMachineKind>`__ | Machine (motor or |
   |                   |      |                   | generator).       |
   +-------------------+------+-------------------+-------------------+
   | converterFedDrive | 0..1 | `Bool             | Indicates whether |
   |                   |      | ean <#Boolean>`__ | the machine is a  |
   |                   |      |                   | converter fed     |
   |                   |      |                   | drive. Used for   |
   |                   |      |                   | short circuit     |
   |                   |      |                   | data exchange     |
   |                   |      |                   | according to IEC  |
   |                   |      |                   | 60909.            |
   +-------------------+------+-------------------+-------------------+
   | efficiency        | 0..1 | `PerC             | Efficiency of the |
   |                   |      | ent <#PerCent>`__ | asynchronous      |
   |                   |      |                   | machine at        |
   |                   |      |                   | nominal operation |
   |                   |      |                   | as a percentage.  |
   |                   |      |                   | Indicator for     |
   |                   |      |                   | converter drive   |
   |                   |      |                   | motors. Used for  |
   |                   |      |                   | short circuit     |
   |                   |      |                   | data exchange     |
   |                   |      |                   | according to IEC  |
   |                   |      |                   | 60909.            |
   +-------------------+------+-------------------+-------------------+
   | iaIrRatio         | 0..1 | `                 | Ratio of          |
   |                   |      | Float <#Float>`__ | locked-rotor      |
   |                   |      |                   | current to the    |
   |                   |      |                   | rated current of  |
   |                   |      |                   | the motor         |
   |                   |      |                   | (Ia/Ir). Used for |
   |                   |      |                   | short circuit     |
   |                   |      |                   | data exchange     |
   |                   |      |                   | according to IEC  |
   |                   |      |                   | 60909.            |
   +-------------------+------+-------------------+-------------------+
   | nominalFrequency  | 0..1 | `Frequenc         | Nameplate data    |
   |                   |      | y <#Frequency>`__ | indicates if the  |
   |                   |      |                   | machine is 50 Hz  |
   |                   |      |                   | or 60 Hz.         |
   +-------------------+------+-------------------+-------------------+
   | nominalSpeed      | 0..1 | `RotationSpeed <# | Nameplate data.   |
   |                   |      | RotationSpeed>`__ | Depends on the    |
   |                   |      |                   | slip and number   |
   |                   |      |                   | of pole pairs.    |
   +-------------------+------+-------------------+-------------------+
   | polePairNumber    | 0..1 | `Inte             | Number of pole    |
   |                   |      | ger <#Integer>`__ | pairs of stator.  |
   |                   |      |                   | Used for short    |
   |                   |      |                   | circuit data      |
   |                   |      |                   | exchange          |
   |                   |      |                   | according to IEC  |
   |                   |      |                   | 60909.            |
   +-------------------+------+-------------------+-------------------+
   | rat               | 0..1 | `ActivePower      | Rated mechanical  |
   | edMechanicalPower |      | <#ActivePower>`__ | power (Pr in IEC  |
   |                   |      |                   | 60909-0). Used    |
   |                   |      |                   | for short circuit |
   |                   |      |                   | data exchange     |
   |                   |      |                   | according to IEC  |
   |                   |      |                   | 60909.            |
   +-------------------+------+-------------------+-------------------+
   | reversible        | 0..1 | `Bool             | Indicates for     |
   |                   |      | ean <#Boolean>`__ | converter drive   |
   |                   |      |                   | motors if the     |
   |                   |      |                   | power can be      |
   |                   |      |                   | reversible. Used  |
   |                   |      |                   | for short circuit |
   |                   |      |                   | data exchange     |
   |                   |      |                   | according to IEC  |
   |                   |      |                   | 60909.            |
   +-------------------+------+-------------------+-------------------+
   | rr1               | 0..1 | `Resistance       | Damper 1 winding  |
   |                   |      |  <#Resistance>`__ | resistance.       |
   +-------------------+------+-------------------+-------------------+
   | rr2               | 0..1 | `Resistance       | Damper 2 winding  |
   |                   |      |  <#Resistance>`__ | resistance.       |
   +-------------------+------+-------------------+-------------------+
   | r                 | 0..1 | `                 | Locked rotor      |
   | xLockedRotorRatio |      | Float <#Float>`__ | ratio (R/X). Used |
   |                   |      |                   | for short circuit |
   |                   |      |                   | data exchange     |
   |                   |      |                   | according to IEC  |
   |                   |      |                   | 60909.            |
   +-------------------+------+-------------------+-------------------+
   | tpo               | 0..1 | `Seco             | Transient rotor   |
   |                   |      | nds <#Seconds>`__ | time constant     |
   |                   |      |                   | (greater than     |
   |                   |      |                   | tppo).            |
   +-------------------+------+-------------------+-------------------+
   | tppo              | 0..1 | `Seco             | Sub-transient     |
   |                   |      | nds <#Seconds>`__ | rotor time        |
   |                   |      |                   | constant (greater |
   |                   |      |                   | than 0).          |
   +-------------------+------+-------------------+-------------------+
   | xlr1              | 0..1 | `Reactanc         | Damper 1 winding  |
   |                   |      | e <#Reactance>`__ | leakage           |
   |                   |      |                   | reactance.        |
   +-------------------+------+-------------------+-------------------+
   | xlr2              | 0..1 | `Reactanc         | Damper 2 winding  |
   |                   |      | e <#Reactance>`__ | leakage           |
   |                   |      |                   | reactance.        |
   +-------------------+------+-------------------+-------------------+
   | xm                | 0..1 | `Reactanc         | Magnetizing       |
   |                   |      | e <#Reactance>`__ | reactance.        |
   +-------------------+------+-------------------+-------------------+
   | xp                | 0..1 | `Reactanc         | Transient         |
   |                   |      | e <#Reactance>`__ | reactance         |
   |                   |      |                   | (unsaturated)     |
   |                   |      |                   | (greater than or  |
   |                   |      |                   | equal to xpp).    |
   +-------------------+------+-------------------+-------------------+
   | xpp               | 0..1 | `Reactanc         | Sub-transient     |
   |                   |      | e <#Reactance>`__ | reactance         |
   |                   |      |                   | (unsaturated).    |
   +-------------------+------+-------------------+-------------------+
   | xs                | 0..1 | `Reactanc         | Synchronous       |
   |                   |      | e <#Reactance>`__ | reactance         |
   |                   |      |                   | (greater than     |
   |                   |      |                   | xp).              |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-4

   +----------------+------+-------------------+-------------------+
   | p              | 1..1 | `ActivePower      | see               |
   |                |      | <#ActivePower>`__ | `Rotat            |
   |                |      |                   | ingMachine <#Rota |
   |                |      |                   | tingMachine.p>`__ |
   +----------------+------+-------------------+-------------------+
   | q              | 1..1 | `ReactivePower <# | see               |
   |                |      | ReactivePower>`__ | `Rotat            |
   |                |      |                   | ingMachine <#Rota |
   |                |      |                   | tingMachine.q>`__ |
   +----------------+------+-------------------+-------------------+
   | ratedS         | 1..1 | `ApparentPower <# | see               |
   |                |      | ApparentPower>`__ | `RotatingMa       |
   |                |      |                   | chine <#RotatingM |
   |                |      |                   | achine.ratedS>`__ |
   +----------------+------+-------------------+-------------------+
   | ratedU         | 1..1 | `Volt             | see               |
   |                |      | age <#Voltage>`__ | `RotatingMa       |
   |                |      |                   | chine <#RotatingM |
   |                |      |                   | achine.ratedU>`__ |
   +----------------+------+-------------------+-------------------+
   | GeneratingUnit | 1..1 | `G                | see               |
   |                |      | eneratingUnit <#G | `R                |
   |                |      | eneratingUnit>`__ | otatingMachine <# |
   |                |      |                   | RotatingMachine.G |
   |                |      |                   | eneratingUnit>`__ |
   +----------------+------+-------------------+-------------------+

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: AsynchronousMachineTimeConstantReactance

   ` <#AsynchronousMachineTimeConstantReactance>`__

   .. rubric:: AsynchronousMachineTimeConstantReactance
      :name: asynchronousmachinetimeconstantreactance
      :class: concrete

   AsynchronousMachineDynamics

   Parameter details:

   1. If *X''* = *X'*, a single cage (one equivalent rotor winding per
      axis) is modelled.
   2. The “*p*” in the attribute names is a substitution for a “prime”
      in the usual parameter notation, e.g. *tpo* refers to *T'o*.

   The parameters used for models expressed in time constant reactance
   form include:

   - RotatingMachine.ratedS (*MVAbase*);

   - RotatingMachineDynamics.damping (*D*);

   - RotatingMachineDynamics.inertia (*H*);

   - RotatingMachineDynamics.saturationFactor (*S1*);

   - RotatingMachineDynamics.saturationFactor120 (*S12*);

   - RotatingMachineDynamics.statorLeakageReactance (*Xl*);

   - RotatingMachineDynamics.statorResistance (*Rs*);

   - .xs (*Xs*);

   - .xp (*X'*);

   - .xpp (*X''*);

   - .tpo (*T'o*);

   - .tppo (*T''o*).

   .. rubric:: Native Members
      :name: native-members-5

   +------+------+------------------------+--------------------------+
   | tpo  | 0..1 | `Seconds <#Seconds>`__ | Transient rotor time     |
   |      |      |                        | constant (*T'o*) (>      |
   |      |      |                        | AsynchronousMachineTime  |
   |      |      |                        | ConstantReactance.tppo). |
   |      |      |                        | Typical value = 5.       |
   +------+------+------------------------+--------------------------+
   | tppo | 0..1 | `Seconds <#Seconds>`__ | Subtransient rotor time  |
   |      |      |                        | constant (*T''o*) (> 0). |
   |      |      |                        | Typical value = 0,03.    |
   +------+------+------------------------+--------------------------+
   | xp   | 0..1 | `PU <#PU>`__           | Transient reactance      |
   |      |      |                        | (unsaturated) (*X'*) (>= |
   |      |      |                        | AsynchronousMachineTim   |
   |      |      |                        | eConstantReactance.xpp). |
   |      |      |                        | Typical value = 0,5.     |
   +------+------+------------------------+--------------------------+
   | xpp  | 0..1 | `PU <#PU>`__           | Subtransient reactance   |
   |      |      |                        | (unsaturated) (*X''*) (> |
   |      |      |                        | RotatingMachineDynamics. |
   |      |      |                        | statorLeakageReactance). |
   |      |      |                        | Typical value = 0,2.     |
   +------+------+------------------------+--------------------------+
   | xs   | 0..1 | `PU <#PU>`__           | Synchronous reactance    |
   |      |      |                        | (*Xs*) (>=               |
   |      |      |                        | AsynchronousMachineTi    |
   |      |      |                        | meConstantReactance.xp). |
   |      |      |                        | Typical value = 1,8.     |
   +------+------+------------------------+--------------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-5

   +-------------------+------+-------------------+-------------------+
   | As                | 0..1 | `Asynchronou      | see               |
   | ynchronousMachine |      | sMachine <#Asynch | `AsynchronousM    |
   |                   |      | ronousMachine>`__ | achineDynamics <# |
   |                   |      |                   | AsynchronousMachi |
   |                   |      |                   | neDynamics.Asynch |
   |                   |      |                   | ronousMachine>`__ |
   +-------------------+------+-------------------+-------------------+

   +-------------------+------+-------------------+-------------------+
   | damping           | 1..1 | `                 | see               |
   |                   |      | Float <#Float>`__ | `RotatingMa       |
   |                   |      |                   | chineDynamics <#R |
   |                   |      |                   | otatingMachineDyn |
   |                   |      |                   | amics.damping>`__ |
   +-------------------+------+-------------------+-------------------+
   | inertia           | 1..1 | `Seco             | see               |
   |                   |      | nds <#Seconds>`__ | `RotatingMa       |
   |                   |      |                   | chineDynamics <#R |
   |                   |      |                   | otatingMachineDyn |
   |                   |      |                   | amics.inertia>`__ |
   +-------------------+------+-------------------+-------------------+
   | stato             | 1..1 | `PU <#PU>`__      | see               |
   | rLeakageReactance |      |                   | `Rotating         |
   |                   |      |                   | MachineDynamics < |
   |                   |      |                   | #RotatingMachineD |
   |                   |      |                   | ynamics.statorLea |
   |                   |      |                   | kageReactance>`__ |
   +-------------------+------+-------------------+-------------------+
   | statorResistance  | 1..1 | `PU <#PU>`__      | see               |
   |                   |      |                   | `Ro               |
   |                   |      |                   | tatingMachineDyna |
   |                   |      |                   | mics <#RotatingMa |
   |                   |      |                   | chineDynamics.sta |
   |                   |      |                   | torResistance>`__ |
   +-------------------+------+-------------------+-------------------+

   +---------+------+------------------------+------------------------+
   | mRID    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.mRID>`__ |
   +---------+------+------------------------+------------------------+
   | enabled | 1..1 | `Boolean <#Boolean>`__ | see                    |
   |         |      |                        | `DynamicsFunct         |
   |         |      |                        | ionBlock <#DynamicsFun |
   |         |      |                        | ctionBlock.enabled>`__ |
   +---------+------+------------------------+------------------------+
   | name    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.name>`__ |
   +---------+------+------------------------+------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: BaseVoltage

   ` <#BaseVoltage>`__

   .. rubric:: BaseVoltage
      :name: basevoltage
      :class: concrete

   Core

   Defines a system base voltage which is referenced. This may be
   different than the rated voltage.

   .. rubric:: Native Members
      :name: native-members-6

   +----------------+----------------+----------------+----------------+
   | mRID           | 1..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | name           | 1..1           | `S             | The name is    |
   |                |                | trin           | any free human |
   |                |                | g <#String>`__ | readable and   |
   |                |                |                | possibly non   |
   |                |                |                | unique text    |
   |                |                |                | naming the     |
   |                |                |                | object.        |
   +----------------+----------------+----------------+----------------+
   | nominalVoltage | 1..1           | `Vol           | The power      |
   |                |                | tage           | system         |
   |                |                |  <#Voltage>`__ | resource's     |
   |                |                |                | base voltage,  |
   |                |                |                | expressed on a |
   |                |                |                | phase-to-phase |
   |                |                |                | (line-to-line) |
   |                |                |                | basis. Shall   |
   |                |                |                | be a positive  |
   |                |                |                | value and not  |
   |                |                |                | zero.          |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-6

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: BatteryUnit

   ` <#BatteryUnit>`__

   .. rubric:: BatteryUnit
      :name: batteryunit
      :class: concrete

   Production

   An electrochemical energy storage device.

   .. rubric:: Native Members
      :name: native-members-7

   +--------------+------+----------------------+----------------------+
   | batteryState | 1..1 | `BatteryStateKind <# | The current state of |
   |              |      | BatteryStateKind>`__ | the battery          |
   |              |      |                      | (charging, full,     |
   |              |      |                      | etc.).               |
   +--------------+------+----------------------+----------------------+
   | ratedE       | 1..1 | `RealEne             | Full energy storage  |
   |              |      | rgy <#RealEnergy>`__ | capacity of the      |
   |              |      |                      | battery. The         |
   |              |      |                      | attribute shall be a |
   |              |      |                      | positive value.      |
   +--------------+------+----------------------+----------------------+
   | storedE      | 1..1 | `RealEne             | Amount of energy     |
   |              |      | rgy <#RealEnergy>`__ | currently stored.    |
   |              |      |                      | The attribute shall  |
   |              |      |                      | be a positive value  |
   |              |      |                      | or zero and lower    |
   |              |      |                      | than                 |
   |              |      |                      | BatteryUnit.ratedE.  |
   +--------------+------+----------------------+----------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-7

   +-------------------+------+-------------------+-------------------+
   | maxP              | 1..1 | `ActivePower      | see               |
   |                   |      | <#ActivePower>`__ | `P                |
   |                   |      |                   | owerElectronicsUn |
   |                   |      |                   | it <#PowerElectro |
   |                   |      |                   | nicsUnit.maxP>`__ |
   +-------------------+------+-------------------+-------------------+
   | minP              | 1..1 | `ActivePower      | see               |
   |                   |      | <#ActivePower>`__ | `P                |
   |                   |      |                   | owerElectronicsUn |
   |                   |      |                   | it <#PowerElectro |
   |                   |      |                   | nicsUnit.minP>`__ |
   +-------------------+------+-------------------+-------------------+
   | PowerElec         | 1..1 | `PowerEle         | see               |
   | tronicsConnection |      | ctronicsConnectio | `PowerE           |
   |                   |      | n <#PowerElectron | lectronicsUnit <# |
   |                   |      | icsConnection>`__ | PowerElectronicsU |
   |                   |      |                   | nit.PowerElectron |
   |                   |      |                   | icsConnection>`__ |
   +-------------------+------+-------------------+-------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: ConnectivityNode

   ` <#ConnectivityNode>`__

   .. rubric:: ConnectivityNode
      :name: connectivitynode
      :class: concrete

   Core

   Connectivity nodes are points where terminals of AC conducting
   equipment are connected together with zero impedance.

   .. rubric:: Native Members
      :name: native-members-8

   +----------------+----------------+----------------+----------------+
   | mRID           | 1..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | name           | 1..1           | `S             | The name is    |
   |                |                | trin           | any free human |
   |                |                | g <#String>`__ | readable and   |
   |                |                |                | possibly non   |
   |                |                |                | unique text    |
   |                |                |                | naming the     |
   |                |                |                | object.        |
   +----------------+----------------+----------------+----------------+
   | Connectivi     | 1..1           | `Connectiv     | Container of   |
   | t              |                | i              | this           |
   | yNodeContainer |                | tyNodeContaine | connectivity   |
   |                |                | r <#Conn       | node.          |
   |                |                | ectivit%20yNod |                |
   |                |                | eContainer>`__ |                |
   +----------------+----------------+----------------+----------------+
   | T              | 0..1           | `Topo          | The            |
   | opologicalNode |                | logicalN       | topological    |
   |                |                | ode <#T%20opol | node to which  |
   |                |                | ogicalNode>`__ | this           |
   |                |                |                | connectivity   |
   |                |                |                | node is        |
   |                |                |                | assigned. May  |
   |                |                |                | depend on the  |
   |                |                |                | current state  |
   |                |                |                | of switches in |
   |                |                |                | the network.   |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-8

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: CsConverter

   ` <#CsConverter>`__

   .. rubric:: CsConverter
      :name: csconverter
      :class: concrete

   DC

   DC side of the current source converter (CSC).

   The firing angle controls the dc voltage at the converter, both for
   rectifier and inverter. The difference between the dc voltages of the
   rectifier and inverter determines the dc current. The extinction
   angle is used to limit the dc voltage at the inverter, if needed, and
   is not used in active power control. The firing angle, transformer
   tap position and number of connected filters are the primary means to
   control a current source dc line. Higher level controls are built on
   top, e.g. DC voltage, dc current and active power. From a steady
   state perspective it is sufficient to specify the desired active
   power transfer (ACDCConverter.targetPpcc) and the control functions
   will set the dc voltage, dc current, firing angle, transformer tap
   position and number of connected filters to meet this. Therefore
   attributes targetAlpha and targetGamma are not applicable in this
   case.

   Attributes targetAlpha and targetGamma are mutually exclusive
   therefore only one of them can be defined to describe an operating
   target.

   The reactive power consumed by the converter is a function of the
   firing angle, transformer tap position and number of connected
   filter, which can be approximated with half of the active power. The
   losses are a function of the dc voltage and dc current.

   The attributes minAlpha and maxAlpha define the range of firing
   angles for rectifier operation between which no discrete tap changer
   action takes place. The range is typically 10 to 18 degrees.

   The attributes minGamma and maxGamma define the range of extinction
   angles for inverter operation between which no discrete tap changer
   action takes place. The range is typically 17 to 20 degrees.

   .. rubric:: Native Members
      :name: native-members-9

   +---------------+------+---------------------+---------------------+
   | alpha         | 0..1 | `AngleDegrees       | Firing angle that   |
   |               |      |  <#AngleDegrees>`__ | determines the DC   |
   |               |      |                     | voltage at the      |
   |               |      |                     | converter DC        |
   |               |      |                     | terminal. Typical   |
   |               |      |                     | value between 10    |
   |               |      |                     | degrees and 18      |
   |               |      |                     | degrees for a       |
   |               |      |                     | rectifier. It is    |
   |               |      |                     | converter's state   |
   |               |      |                     | variable, result    |
   |               |      |                     | from power flow.    |
   |               |      |                     | The attribute shall |
   |               |      |                     | be a positive       |
   |               |      |                     | value.              |
   +---------------+------+---------------------+---------------------+
   | gamma         | 0..1 | `AngleDegrees       | Extinction angle.   |
   |               |      |  <#AngleDegrees>`__ | It is used to limit |
   |               |      |                     | the DC voltage at   |
   |               |      |                     | the inverter if     |
   |               |      |                     | needed. Typical     |
   |               |      |                     | value between 17    |
   |               |      |                     | degrees and 20      |
   |               |      |                     | degrees for an      |
   |               |      |                     | inverter. It is     |
   |               |      |                     | converter's state   |
   |               |      |                     | variable, result    |
   |               |      |                     | from power flow.    |
   |               |      |                     | The attribute shall |
   |               |      |                     | be a positive       |
   |               |      |                     | value.              |
   +---------------+------+---------------------+---------------------+
   | maxAlpha      | 0..1 | `AngleDegrees       | Maximum firing      |
   |               |      |  <#AngleDegrees>`__ | angle. It is the    |
   |               |      |                     | converter's         |
   |               |      |                     | configuration data  |
   |               |      |                     | used in power flow. |
   |               |      |                     | The attribute shall |
   |               |      |                     | be a positive       |
   |               |      |                     | value.              |
   +---------------+------+---------------------+---------------------+
   | maxGamma      | 0..1 | `AngleDegrees       | Maximum extinction  |
   |               |      |  <#AngleDegrees>`__ | angle. It is the    |
   |               |      |                     | converter's         |
   |               |      |                     | configuration data  |
   |               |      |                     | used in power flow. |
   |               |      |                     | The attribute shall |
   |               |      |                     | be a positive       |
   |               |      |                     | value.              |
   +---------------+------+---------------------+---------------------+
   | maxIdc        | 0..1 | `CurrentFlo         | The maximum direct  |
   |               |      | w <#CurrentFlow>`__ | current (Id) on the |
   |               |      |                     | DC side at which    |
   |               |      |                     | the converter       |
   |               |      |                     | should operate. It  |
   |               |      |                     | is the converter's  |
   |               |      |                     | configuration data  |
   |               |      |                     | use in power flow.  |
   |               |      |                     | The attribute shall |
   |               |      |                     | be a positive       |
   |               |      |                     | value.              |
   +---------------+------+---------------------+---------------------+
   | minAlpha      | 0..1 | `AngleDegrees       | Minimum firing      |
   |               |      |  <#AngleDegrees>`__ | angle. It is the    |
   |               |      |                     | converter's         |
   |               |      |                     | configuration data  |
   |               |      |                     | used in power flow. |
   |               |      |                     | The attribute shall |
   |               |      |                     | be a positive       |
   |               |      |                     | value.              |
   +---------------+------+---------------------+---------------------+
   | minGamma      | 0..1 | `AngleDegrees       | Minimum extinction  |
   |               |      |  <#AngleDegrees>`__ | angle. It is the    |
   |               |      |                     | converter's         |
   |               |      |                     | configuration data  |
   |               |      |                     | used in power flow. |
   |               |      |                     | The attribute shall |
   |               |      |                     | be a positive       |
   |               |      |                     | value.              |
   +---------------+------+---------------------+---------------------+
   | minIdc        | 0..1 | `CurrentFlo         | The minimum direct  |
   |               |      | w <#CurrentFlow>`__ | current (Id) on the |
   |               |      |                     | DC side at which    |
   |               |      |                     | the converter       |
   |               |      |                     | should operate. It  |
   |               |      |                     | is the converter's  |
   |               |      |                     | configuration data  |
   |               |      |                     | used in power flow. |
   |               |      |                     | The attribute shall |
   |               |      |                     | be a positive       |
   |               |      |                     | value.              |
   +---------------+------+---------------------+---------------------+
   | operatingMode | 0..1 | `CsOpera            | Indicates whether   |
   |               |      | tingModeKind <#CsOp | the DC pole is      |
   |               |      | eratingModeKind>`__ | operating as an     |
   |               |      |                     | inverter or as a    |
   |               |      |                     | rectifier. It is    |
   |               |      |                     | converter's control |
   |               |      |                     | variable used in    |
   |               |      |                     | power flow.         |
   +---------------+------+---------------------+---------------------+
   | pPccControl   | 0..1 | `CsP                | Kind of active      |
   |               |      | pccControlKind <#Cs | power control.      |
   |               |      | PpccControlKind>`__ |                     |
   +---------------+------+---------------------+---------------------+
   | ratedIdc      | 0..1 | `CurrentFlo         | Rated converter DC  |
   |               |      | w <#CurrentFlow>`__ | current, also       |
   |               |      |                     | called IdN. The     |
   |               |      |                     | attribute shall be  |
   |               |      |                     | a positive value.   |
   |               |      |                     | It is the           |
   |               |      |                     | converter's         |
   |               |      |                     | configuration data  |
   |               |      |                     | used in power flow. |
   +---------------+------+---------------------+---------------------+
   | targetAlpha   | 0..1 | `AngleDegrees       | Target firing       |
   |               |      |  <#AngleDegrees>`__ | angle. It is        |
   |               |      |                     | converter's control |
   |               |      |                     | variable used in    |
   |               |      |                     | power flow. It is   |
   |               |      |                     | only applicable for |
   |               |      |                     | rectifier control.  |
   |               |      |                     | Allowed values are  |
   |               |      |                     | within the range    |
   |               |      |                     | minAlpha<=tar       |
   |               |      |                     | getAlpha<=maxAlpha. |
   |               |      |                     | The attribute shall |
   |               |      |                     | be a positive       |
   |               |      |                     | value.              |
   +---------------+------+---------------------+---------------------+
   | targetGamma   | 0..1 | `AngleDegrees       | Target extinction   |
   |               |      |  <#AngleDegrees>`__ | angle. It is        |
   |               |      |                     | converter's control |
   |               |      |                     | variable used in    |
   |               |      |                     | power flow. It is   |
   |               |      |                     | only applicable for |
   |               |      |                     | inverter control.   |
   |               |      |                     | Allowed values are  |
   |               |      |                     | within the range    |
   |               |      |                     | minGamma<=tar       |
   |               |      |                     | getGamma<=maxGamma. |
   |               |      |                     | The attribute shall |
   |               |      |                     | be a positive       |
   |               |      |                     | value.              |
   +---------------+------+---------------------+---------------------+
   | targetIdc     | 0..1 | `CurrentFlo         | DC current target   |
   |               |      | w <#CurrentFlow>`__ | value. It is        |
   |               |      |                     | converter's control |
   |               |      |                     | variable used in    |
   |               |      |                     | power flow. The     |
   |               |      |                     | attribute shall be  |
   |               |      |                     | a positive value.   |
   +---------------+------+---------------------+---------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-9

   +----------------+------+-------------------+-------------------+
   | baseS          | 0..1 | `ApparentPower <# | see               |
   |                |      | ApparentPower>`__ | `ACDCC            |
   |                |      |                   | onverter <#ACDCCo |
   |                |      |                   | nverter.baseS>`__ |
   +----------------+------+-------------------+-------------------+
   | idc            | 0..1 | `CurrentFlow      | see               |
   |                |      | <#CurrentFlow>`__ | `ACD              |
   |                |      |                   | CConverter <#ACDC |
   |                |      |                   | Converter.idc>`__ |
   +----------------+------+-------------------+-------------------+
   | idleLoss       | 0..1 | `ActivePower      | see               |
   |                |      | <#ActivePower>`__ | `ACDCConv         |
   |                |      |                   | erter <#ACDCConve |
   |                |      |                   | rter.idleLoss>`__ |
   +----------------+------+-------------------+-------------------+
   | maxP           | 0..1 | `ActivePower      | see               |
   |                |      | <#ActivePower>`__ | `ACDC             |
   |                |      |                   | Converter <#ACDCC |
   |                |      |                   | onverter.maxP>`__ |
   +----------------+------+-------------------+-------------------+
   | maxUdc         | 0..1 | `Volt             | see               |
   |                |      | age <#Voltage>`__ | `ACDCCo           |
   |                |      |                   | nverter <#ACDCCon |
   |                |      |                   | verter.maxUdc>`__ |
   +----------------+------+-------------------+-------------------+
   | minP           | 0..1 | `ActivePower      | see               |
   |                |      | <#ActivePower>`__ | `ACDC             |
   |                |      |                   | Converter <#ACDCC |
   |                |      |                   | onverter.minP>`__ |
   +----------------+------+-------------------+-------------------+
   | minUdc         | 0..1 | `Volt             | see               |
   |                |      | age <#Voltage>`__ | `ACDCCo           |
   |                |      |                   | nverter <#ACDCCon |
   |                |      |                   | verter.minUdc>`__ |
   +----------------+------+-------------------+-------------------+
   | numberOfValves | 0..1 | `Inte             | see               |
   |                |      | ger <#Integer>`__ | `ACDCConverter    |
   |                |      |                   | <#ACDCConverter.n |
   |                |      |                   | umberOfValves>`__ |
   +----------------+------+-------------------+-------------------+
   | p              | 0..1 | `ActivePower      | see               |
   |                |      | <#ActivePower>`__ | `A                |
   |                |      |                   | CDCConverter <#AC |
   |                |      |                   | DCConverter.p>`__ |
   +----------------+------+-------------------+-------------------+
   | poleLossP      | 0..1 | `ActivePower      | see               |
   |                |      | <#ActivePower>`__ | `ACDCConve        |
   |                |      |                   | rter <#ACDCConver |
   |                |      |                   | ter.poleLossP>`__ |
   +----------------+------+-------------------+-------------------+
   | q              | 0..1 | `ReactivePower <# | see               |
   |                |      | ReactivePower>`__ | `A                |
   |                |      |                   | CDCConverter <#AC |
   |                |      |                   | DCConverter.q>`__ |
   +----------------+------+-------------------+-------------------+
   | ratedUdc       | 0..1 | `Volt             | see               |
   |                |      | age <#Voltage>`__ | `ACDCConv         |
   |                |      |                   | erter <#ACDCConve |
   |                |      |                   | rter.ratedUdc>`__ |
   +----------------+------+-------------------+-------------------+
   | resistiveLoss  | 0..1 | `Resistance       | see               |
   |                |      |  <#Resistance>`__ | `ACDCConverter    |
   |                |      |                   |  <#ACDCConverter. |
   |                |      |                   | resistiveLoss>`__ |
   +----------------+------+-------------------+-------------------+
   | switchingLoss  | 0..1 | `Active           | see               |
   |                |      | PowerPerCurrentFl | `ACDCConverter    |
   |                |      | ow <#ActivePowerP |  <#ACDCConverter. |
   |                |      | erCurrentFlow>`__ | switchingLoss>`__ |
   +----------------+------+-------------------+-------------------+
   | targetPpcc     | 0..1 | `ActivePower      | see               |
   |                |      | <#ActivePower>`__ | `ACDCConver       |
   |                |      |                   | ter <#ACDCConvert |
   |                |      |                   | er.targetPpcc>`__ |
   +----------------+------+-------------------+-------------------+
   | targetUdc      | 0..1 | `Volt             | see               |
   |                |      | age <#Voltage>`__ | `ACDCConve        |
   |                |      |                   | rter <#ACDCConver |
   |                |      |                   | ter.targetUdc>`__ |
   +----------------+------+-------------------+-------------------+
   | uc             | 0..1 | `Volt             | see               |
   |                |      | age <#Voltage>`__ | `AC               |
   |                |      |                   | DCConverter <#ACD |
   |                |      |                   | CConverter.uc>`__ |
   +----------------+------+-------------------+-------------------+
   | udc            | 0..1 | `Volt             | see               |
   |                |      | age <#Voltage>`__ | `ACD              |
   |                |      |                   | CConverter <#ACDC |
   |                |      |                   | Converter.udc>`__ |
   +----------------+------+-------------------+-------------------+
   | valveU0        | 0..1 | `Volt             | see               |
   |                |      | age <#Voltage>`__ | `ACDCCon          |
   |                |      |                   | verter <#ACDCConv |
   |                |      |                   | erter.valveU0>`__ |
   +----------------+------+-------------------+-------------------+

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: CurveData

   ` <#CurveData>`__

   .. rubric:: CurveData
      :name: curvedata
      :class: concrete

   Core

   Multi-purpose data points for defining a curve. The use of this
   generic class is discouraged if a more specific class can be used to
   specify the X and Y axis values along with their specific data types.

   .. rubric:: Native Members
      :name: native-members-10

   +---------+------+--------------------+------------------------+
   | xvalue  | 1..1 | `Float <#Float>`__ | The data value of the  |
   |         |      |                    | X-axis variable,       |
   |         |      |                    | depending on the       |
   |         |      |                    | X-axis units.          |
   +---------+------+--------------------+------------------------+
   | y1value | 1..1 | `Float <#Float>`__ | The data value of the  |
   |         |      |                    | first Y-axis variable, |
   |         |      |                    | depending on the       |
   |         |      |                    | Y-axis units.          |
   +---------+------+--------------------+------------------------+
   | Curve   | 1..1 | `Curve <#Curve>`__ | The curve of this      |
   |         |      |                    | curve data point.      |
   +---------+------+--------------------+------------------------+

.. container:: group
   :name: DCBreaker

   ` <#DCBreaker>`__

   .. rubric:: DCBreaker
      :name: dcbreaker
      :class: concrete

   DC

   A breaker within a DC system.

   .. rubric:: Inherited Members
      :name: inherited-members-10

   +------------+------+-----------------------+-----------------------+
   | locked     | 0..1 | `                     | see                   |
   |            |      | Boolean <#Boolean>`__ | `DCSwitch             |
   |            |      |                       | <#DCSwitch.locked>`__ |
   +------------+------+-----------------------+-----------------------+
   | normalOpen | 0..1 | `                     | see                   |
   |            |      | Boolean <#Boolean>`__ | `DCSwitch <#DC        |
   |            |      |                       | Switch.normalOpen>`__ |
   +------------+------+-----------------------+-----------------------+
   | open       | 0..1 | `                     | see                   |
   |            |      | Boolean <#Boolean>`__ | `DCSwitc              |
   |            |      |                       | h <#DCSwitch.open>`__ |
   +------------+------+-----------------------+-----------------------+
   | retained   | 0..1 | `                     | see                   |
   |            |      | Boolean <#Boolean>`__ | `DCSwitch <#          |
   |            |      |                       | DCSwitch.retained>`__ |
   +------------+------+-----------------------+-----------------------+

   +--------------+------+----------------------+----------------------+
   | ratedCurrent | 0..1 | `CurrentFl           | see                  |
   |              |      | ow <#CurrentFlow>`__ | `DC                  |
   |              |      |                      | ConductingEquipment  |
   |              |      |                      | <#DCConductingEquipm |
   |              |      |                      | ent.ratedCurrent>`__ |
   +--------------+------+----------------------+----------------------+
   | ratedUdc     | 0..1 | `V                   | see                  |
   |              |      | oltage <#Voltage>`__ | `DCConductingEquipm  |
   |              |      |                      | ent <#DCConductingEq |
   |              |      |                      | uipment.ratedUdc>`__ |
   +--------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DCDisconnector

   ` <#DCDisconnector>`__

   .. rubric:: DCDisconnector
      :name: dcdisconnector
      :class: concrete

   DC

   A disconnector within a DC system.

   .. rubric:: Inherited Members
      :name: inherited-members-11

   +------------+------+-----------------------+-----------------------+
   | locked     | 0..1 | `                     | see                   |
   |            |      | Boolean <#Boolean>`__ | `DCSwitch             |
   |            |      |                       | <#DCSwitch.locked>`__ |
   +------------+------+-----------------------+-----------------------+
   | normalOpen | 0..1 | `                     | see                   |
   |            |      | Boolean <#Boolean>`__ | `DCSwitch <#DC        |
   |            |      |                       | Switch.normalOpen>`__ |
   +------------+------+-----------------------+-----------------------+
   | open       | 0..1 | `                     | see                   |
   |            |      | Boolean <#Boolean>`__ | `DCSwitc              |
   |            |      |                       | h <#DCSwitch.open>`__ |
   +------------+------+-----------------------+-----------------------+
   | retained   | 0..1 | `                     | see                   |
   |            |      | Boolean <#Boolean>`__ | `DCSwitch <#          |
   |            |      |                       | DCSwitch.retained>`__ |
   +------------+------+-----------------------+-----------------------+

   +--------------+------+----------------------+----------------------+
   | ratedCurrent | 0..1 | `CurrentFl           | see                  |
   |              |      | ow <#CurrentFlow>`__ | `DC                  |
   |              |      |                      | ConductingEquipment  |
   |              |      |                      | <#DCConductingEquipm |
   |              |      |                      | ent.ratedCurrent>`__ |
   +--------------+------+----------------------+----------------------+
   | ratedUdc     | 0..1 | `V                   | see                  |
   |              |      | oltage <#Voltage>`__ | `DCConductingEquipm  |
   |              |      |                      | ent <#DCConductingEq |
   |              |      |                      | uipment.ratedUdc>`__ |
   +--------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DCEnergySource

   ` <#DCEnergySource>`__

   .. rubric:: DCEnergySource
      :name: dcenergysource
      :class: concrete

   Emtiop

   A source of DC power that is independent of the AC system, e.g., a
   battery or solar panel. The internal representation may include
   current sources, voltage sources, diodes, etc. Use DCSourceKind to
   provide guidance on the internal representation.

   .. rubric:: Native Members
      :name: native-members-11

   +----------+------+------------------------+------------------------+
   | kind     | 0..1 | `DCSourceK             |                        |
   |          |      | ind <#DCSourceKind>`__ |                        |
   +----------+------+------------------------+------------------------+
   | p        | 0..1 | `ActiveP               | The power output,      |
   |          |      | ower <#ActivePower>`__ | negative for load or   |
   |          |      |                        | charging.              |
   +----------+------+------------------------+------------------------+
   | pMax     | 0..1 | `ActiveP               | Maximum power          |
   |          |      | ower <#ActivePower>`__ | available from the     |
   |          |      |                        | primary source, e.g.,  |
   |          |      |                        | photovoltaic panels or |
   |          |      |                        | a battery.             |
   +----------+------+------------------------+------------------------+
   | pMaxLoad | 0..1 | `ActiveP               | Maximum load or        |
   |          |      | ower <#ActivePower>`__ | battery charging       |
   |          |      |                        | power.                 |
   +----------+------+------------------------+------------------------+
   | pMin     | 0..1 | `ActiveP               | Minimum power          |
   |          |      | ower <#ActivePower>`__ | available from the     |
   |          |      |                        | supply.                |
   +----------+------+------------------------+------------------------+
   | pMinLoad | 0..1 | `ActiveP               | Minimum load or        |
   |          |      | ower <#ActivePower>`__ | battery charging       |
   |          |      |                        | power.                 |
   +----------+------+------------------------+------------------------+
   | rSeries  | 0..1 | `Resis                 | Series source          |
   |          |      | tance <#Resistance>`__ | resistance.            |
   +----------+------+------------------------+------------------------+
   | rShunt   | 0..1 | `Resis                 | Shunt source           |
   |          |      | tance <#Resistance>`__ | resistance.            |
   +----------+------+------------------------+------------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-12

   +--------------+------+----------------------+----------------------+
   | ratedCurrent | 0..1 | `CurrentFl           | see                  |
   |              |      | ow <#CurrentFlow>`__ | `DC                  |
   |              |      |                      | ConductingEquipment  |
   |              |      |                      | <#DCConductingEquipm |
   |              |      |                      | ent.ratedCurrent>`__ |
   +--------------+------+----------------------+----------------------+
   | ratedUdc     | 0..1 | `V                   | see                  |
   |              |      | oltage <#Voltage>`__ | `DCConductingEquipm  |
   |              |      |                      | ent <#DCConductingEq |
   |              |      |                      | uipment.ratedUdc>`__ |
   +--------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DCEquipmentContainer

   ` <#DCEquipmentContainer>`__

   .. rubric:: DCEquipmentContainer
      :name: dcequipmentcontainer
      :class: concrete

   DC

   A modelling construct to provide a root class for containment of DC
   as well as AC equipment. The class differ from the EquipmentContainer
   for AC in that it may also contain DCNode(-s). Hence it can contain
   both AC and DC equipment.

   .. rubric:: Inherited Members
      :name: inherited-members-13

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DCGround

   ` <#DCGround>`__

   .. rubric:: DCGround
      :name: dcground
      :class: concrete

   DC

   A ground within a DC system.

   .. rubric:: Native Members
      :name: native-members-12

   ========== ==== ============================ =====================
   inductance 0..1 `Inductance <#Inductance>`__ Inductance to ground.
   r          0..1 `Resistance <#Resistance>`__ Resistance to ground.
   ========== ==== ============================ =====================

   .. rubric:: Inherited Members
      :name: inherited-members-14

   +--------------+------+----------------------+----------------------+
   | ratedCurrent | 0..1 | `CurrentFl           | see                  |
   |              |      | ow <#CurrentFlow>`__ | `DC                  |
   |              |      |                      | ConductingEquipment  |
   |              |      |                      | <#DCConductingEquipm |
   |              |      |                      | ent.ratedCurrent>`__ |
   +--------------+------+----------------------+----------------------+
   | ratedUdc     | 0..1 | `V                   | see                  |
   |              |      | oltage <#Voltage>`__ | `DCConductingEquipm  |
   |              |      |                      | ent <#DCConductingEq |
   |              |      |                      | uipment.ratedUdc>`__ |
   +--------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DCLineSegment

   ` <#DCLineSegment>`__

   .. rubric:: DCLineSegment
      :name: dclinesegment
      :class: concrete

   DC

   A wire or combination of wires not insulated from one another, with
   consistent electrical characteristics, used to carry direct current
   between points in the DC region of the power system.

   .. rubric:: Native Members
      :name: native-members-13

   +-------------+------+----------------------+----------------------+
   | capacitance | 0..1 | `Capacitan           | Capacitance of the   |
   |             |      | ce <#Capacitance>`__ | DC line segment.     |
   |             |      |                      | Significant for      |
   |             |      |                      | cables only.         |
   +-------------+------+----------------------+----------------------+
   | inductance  | 0..1 | `Inducta             | Inductance of the DC |
   |             |      | nce <#Inductance>`__ | line segment.        |
   |             |      |                      | Negligible compared  |
   |             |      |                      | with DCSeriesDevice  |
   |             |      |                      | used for smoothing.  |
   +-------------+------+----------------------+----------------------+
   | length      | 0..1 | `Length <#Length>`__ | Segment length for   |
   |             |      |                      | calculating line     |
   |             |      |                      | section              |
   |             |      |                      | capabilities.        |
   +-------------+------+----------------------+----------------------+
   | resistance  | 0..1 | `Resista             | Resistance of the DC |
   |             |      | nce <#Resistance>`__ | line segment.        |
   +-------------+------+----------------------+----------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-15

   +--------------+------+----------------------+----------------------+
   | ratedCurrent | 0..1 | `CurrentFl           | see                  |
   |              |      | ow <#CurrentFlow>`__ | `DC                  |
   |              |      |                      | ConductingEquipment  |
   |              |      |                      | <#DCConductingEquipm |
   |              |      |                      | ent.ratedCurrent>`__ |
   +--------------+------+----------------------+----------------------+
   | ratedUdc     | 0..1 | `V                   | see                  |
   |              |      | oltage <#Voltage>`__ | `DCConductingEquipm  |
   |              |      |                      | ent <#DCConductingEq |
   |              |      |                      | uipment.ratedUdc>`__ |
   +--------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DCNode

   ` <#DCNode>`__

   .. rubric:: DCNode
      :name: dcnode
      :class: concrete

   DC

   DC nodes are points where terminals of DC conducting equipment are
   connected together with zero impedance.

   .. rubric:: Native Members
      :name: native-members-14

   +----------------+----------------+----------------+----------------+
   | mRID           | 1..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | name           | 1..1           | `S             | The name is    |
   |                |                | trin           | any free human |
   |                |                | g <#String>`__ | readable and   |
   |                |                |                | possibly non   |
   |                |                |                | unique text    |
   |                |                |                | naming the     |
   |                |                |                | object.        |
   +----------------+----------------+----------------+----------------+
   | DCEqu          | 0..1           | `              | The DC         |
   | i              |                | DCEquipmentCon | container for  |
   | pmentContainer |                | tainer <       | the DC nodes.  |
   |                |                | #DCEqui%20pmen |                |
   |                |                | tContainer>`__ |                |
   +----------------+----------------+----------------+----------------+
   | DC             | 0..1           | `DCTopolo      | The DC         |
   | T              |                | gicalNod       | topological    |
   | opologicalNode |                | e <#DCT%20opol | node to which  |
   |                |                | ogicalNode>`__ | this DC        |
   |                |                |                | connectivity   |
   |                |                |                | node is        |
   |                |                |                | assigned. May  |
   |                |                |                | depend on the  |
   |                |                |                | current state  |
   |                |                |                | of switches in |
   |                |                |                | the network.   |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-16

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DCSeriesDevice

   ` <#DCSeriesDevice>`__

   .. rubric:: DCSeriesDevice
      :name: dcseriesdevice
      :class: concrete

   DC

   A series device within the DC system, typically a reactor used for
   filtering or smoothing. Needed for transient and short circuit
   studies.

   .. rubric:: Native Members
      :name: native-members-15

   +------------+------+------------------------------+------------------------------+
   | inductance | 0..1 | `Inductance <#Inductance>`__ | Inductance of the device.    |
   +------------+------+------------------------------+------------------------------+
   | resistance | 0..1 | `Resistance <#Resistance>`__ | Resistance of the DC device. |
   +------------+------+------------------------------+------------------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-17

   +--------------+------+----------------------+----------------------+
   | ratedCurrent | 0..1 | `CurrentFl           | see                  |
   |              |      | ow <#CurrentFlow>`__ | `DC                  |
   |              |      |                      | ConductingEquipment  |
   |              |      |                      | <#DCConductingEquipm |
   |              |      |                      | ent.ratedCurrent>`__ |
   +--------------+------+----------------------+----------------------+
   | ratedUdc     | 0..1 | `V                   | see                  |
   |              |      | oltage <#Voltage>`__ | `DCConductingEquipm  |
   |              |      |                      | ent <#DCConductingEq |
   |              |      |                      | uipment.ratedUdc>`__ |
   +--------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DCShunt

   ` <#DCShunt>`__

   .. rubric:: DCShunt
      :name: dcshunt
      :class: concrete

   DC

   A shunt device within the DC system, typically used for filtering.
   Needed for transient and short circuit studies.

   .. rubric:: Native Members
      :name: native-members-16

   +-------------+------+----------------------+----------------------+
   | capacitance | 0..1 | `Capacitan           | Capacitance of the   |
   |             |      | ce <#Capacitance>`__ | DC shunt.            |
   +-------------+------+----------------------+----------------------+
   | resistance  | 0..1 | `Resista             | Resistance of the DC |
   |             |      | nce <#Resistance>`__ | device.              |
   +-------------+------+----------------------+----------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-18

   +--------------+------+----------------------+----------------------+
   | ratedCurrent | 0..1 | `CurrentFl           | see                  |
   |              |      | ow <#CurrentFlow>`__ | `DC                  |
   |              |      |                      | ConductingEquipment  |
   |              |      |                      | <#DCConductingEquipm |
   |              |      |                      | ent.ratedCurrent>`__ |
   +--------------+------+----------------------+----------------------+
   | ratedUdc     | 0..1 | `V                   | see                  |
   |              |      | oltage <#Voltage>`__ | `DCConductingEquipm  |
   |              |      |                      | ent <#DCConductingEq |
   |              |      |                      | uipment.ratedUdc>`__ |
   +--------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DCTerminal

   ` <#DCTerminal>`__

   .. rubric:: DCTerminal
      :name: dcterminal
      :class: concrete

   DC

   An electrical connection point to generic DC conducting equipment.

   .. rubric:: Native Members
      :name: native-members-17

   +-------------------+------+-------------------+-------------------+
   | polarity          | 0..1 | `                 | Represents the    |
   |                   |      | DCTerminalPolarit | normal network    |
   |                   |      | yKind <#DCTermina | polarity          |
   |                   |      | lPolarityKind>`__ | condition. Used   |
   |                   |      |                   | in DC system      |
   |                   |      |                   | configurations    |
   |                   |      |                   | that have         |
   |                   |      |                   | explicit polarity |
   |                   |      |                   | of the terminals, |
   |                   |      |                   | e.g., voltage     |
   |                   |      |                   | source converter  |
   |                   |      |                   | (VSC) technology. |
   +-------------------+------+-------------------+-------------------+
   | DCCo              | 0..1 | `DCConductingEqu  | An DC terminal    |
   | nductingEquipment |      | ipment <#DCConduc | belong to a DC    |
   |                   |      | tingEquipment>`__ | conducting        |
   |                   |      |                   | equipment.        |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-19

   +--------+------+----------------------+-------------------------+
   | DCNode | 1..1 | `DCNode <#DCNode>`__ | see                     |
   |        |      |                      | `DCBaseTerminal <#DC    |
   |        |      |                      | BaseTerminal.DCNode>`__ |
   +--------+------+----------------------+-------------------------+

   +----------------+------+-------------------+-------------------+
   | sequenceNumber | 1..1 | `Inte             | see               |
   |                |      | ger <#Integer>`__ | `ACDCTerminal     |
   |                |      |                   |  <#ACDCTerminal.s |
   |                |      |                   | equenceNumber>`__ |
   +----------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DCTopologicalNode

   ` <#DCTopologicalNode>`__

   .. rubric:: DCTopologicalNode
      :name: dctopologicalnode
      :class: concrete

   DC

   DC bus.

   .. rubric:: Inherited Members
      :name: inherited-members-20

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DetailedModelDynamics

   ` <#DetailedModelDynamics>`__

   .. rubric:: DetailedModelDynamics
      :name: detailedmodeldynamics
      :class: concrete

   DetailedModelDescription

   The main class that packages all related to this detailed model. This
   includes all parameters, functions, signals, etc.

   .. rubric:: Native Members
      :name: native-members-18

   +-------------------+------+-------------------+-------------------+
   | Detailed          | 0..1 | `Detail           | The type of       |
   | ModelTypeDynamics |      | edModelTypeDynami | detailed model    |
   |                   |      | cs <#DetailedMode | dynamics that is  |
   |                   |      | lTypeDynamics>`__ | applied to the    |
   |                   |      |                   | detailed model    |
   |                   |      |                   | dynamics.         |
   +-------------------+------+-------------------+-------------------+
   | Dyna              | 0..1 | `DynamicsFunctio  | The dynamics      |
   | micsFunctionBlock |      | nBlock <#Dynamics | function block    |
   |                   |      | FunctionBlock>`__ | for this detailed |
   |                   |      |                   | model dynamics.   |
   +-------------------+------+-------------------+-------------------+
   | Equipment         | 0..1 | `Equipmen         | The equipment     |
   |                   |      | t <#Equipment>`__ | which behaviour   |
   |                   |      |                   | this detailed     |
   |                   |      |                   | model dynamics    |
   |                   |      |                   | represents.       |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-21

   +---------+------+------------------------+------------------------+
   | mRID    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.mRID>`__ |
   +---------+------+------------------------+------------------------+
   | enabled | 1..1 | `Boolean <#Boolean>`__ | see                    |
   |         |      |                        | `DynamicsFunct         |
   |         |      |                        | ionBlock <#DynamicsFun |
   |         |      |                        | ctionBlock.enabled>`__ |
   +---------+------+------------------------+------------------------+
   | name    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.name>`__ |
   +---------+------+------------------------+------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DiagramObjectPoint

   ` <#DiagramObjectPoint>`__

   .. rubric:: DiagramObjectPoint
      :name: diagramobjectpoint
      :class: concrete

   DiagramLayout

   A point in a given space defined by 3 coordinates and associated to a
   diagram object. The coordinates may be positive or negative as the
   origin does not have to be in the corner of a diagram.

   .. rubric:: Native Members
      :name: native-members-19

   +----------------+------+-------------------+-------------------+
   | sequenceNumber | 1..1 | `Inte             | The sequence      |
   |                |      | ger <#Integer>`__ | position of the   |
   |                |      |                   | point, used for   |
   |                |      |                   | defining the      |
   |                |      |                   | order of points   |
   |                |      |                   | for diagram       |
   |                |      |                   | objects acting as |
   |                |      |                   | a polyline or     |
   |                |      |                   | polygon with more |
   |                |      |                   | than one point.   |
   |                |      |                   | The attribute     |
   |                |      |                   | shall be a        |
   |                |      |                   | positive value.   |
   +----------------+------+-------------------+-------------------+
   | xPosition      | 1..1 | `                 | The X coordinate  |
   |                |      | Float <#Float>`__ | of this point.    |
   +----------------+------+-------------------+-------------------+
   | yPosition      | 1..1 | `                 | The Y coordinate  |
   |                |      | Float <#Float>`__ | of this point.    |
   +----------------+------+-------------------+-------------------+
   | DiagramObject  | 1..1 | `DiagramObject <# | The diagram       |
   |                |      | DiagramObject>`__ | object with which |
   |                |      |                   | the points are    |
   |                |      |                   | associated.       |
   +----------------+------+-------------------+-------------------+

.. container:: group
   :name: DisconnectingCircuitBreaker

   ` <#DisconnectingCircuitBreaker>`__

   .. rubric:: DisconnectingCircuitBreaker
      :name: disconnectingcircuitbreaker
      :class: concrete

   Wires

   A circuit breaking device including disconnecting function,
   eliminating the need for separate disconnectors.

   .. rubric:: Inherited Members
      :name: inherited-members-22

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: EnergyConsumer

   ` <#EnergyConsumer>`__

   .. rubric:: EnergyConsumer
      :name: energyconsumer
      :class: concrete

   Wires

   Generic user of energy - a point of consumption on the power system
   model.

   EnergyConsumer.pfixed, .qfixed, .pfixedPct and .qfixedPct have
   meaning only if there is no LoadResponseCharacteristic associated
   with EnergyConsumer or if LoadResponseCharacteristic.exponentModel is
   set to False.

   .. rubric:: Native Members
      :name: native-members-20

   +----------------+----------------+----------------+----------------+
   | p              | 1..1           | `A             | Active power   |
   |                |                | ctivePower <#A | of the load.   |
   |                |                | ctivePower>`__ | Load sign      |
   |                |                |                | convention is  |
   |                |                |                | used, i.e.     |
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
   | q              | 1..1           | `React         | Reactive power |
   |                |                | ivePower <#Rea | of the load.   |
   |                |                | ctivePower>`__ | Load sign      |
   |                |                |                | convention is  |
   |                |                |                | used, i.e.     |
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
   | LoadResponse   | 1..1           | `LoadRespons   | The load       |
   |                |                | eCharacte      | response       |
   |                |                | ristic <#LoadR | characteristic |
   |                |                | esponse%20Char | of this load.  |
   |                |                | acteristic>`__ | If missing,    |
   |                |                |                | this load is   |
   |                |                |                | assumed to be  |
   |                |                |                | constant       |
   |                |                |                | power.         |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-23

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: EnergySource

   ` <#EnergySource>`__

   .. rubric:: EnergySource
      :name: energysource
      :class: concrete

   Wires

   A generic equivalent for an energy supplier on a transmission or
   distribution voltage level.

   .. rubric:: Native Members
      :name: native-members-21

   +------------------+------+-------------------+-------------------+
   | nominalVoltage   | 1..1 | `Volt             | Phase-to-phase    |
   |                  |      | age <#Voltage>`__ | nominal voltage.  |
   +------------------+------+-------------------+-------------------+
   | r                | 1..1 | `Resistance       | Positive sequence |
   |                  |      |  <#Resistance>`__ | Thevenin          |
   |                  |      |                   | resistance.       |
   +------------------+------+-------------------+-------------------+
   | r0               | 1..1 | `Resistance       | Zero sequence     |
   |                  |      |  <#Resistance>`__ | Thevenin          |
   |                  |      |                   | resistance.       |
   +------------------+------+-------------------+-------------------+
   | voltageAngle     | 1..1 | `AngleRadians <   | Phase angle of    |
   |                  |      | #AngleRadians>`__ | a-phase open      |
   |                  |      |                   | circuit used when |
   |                  |      |                   | voltage           |
   |                  |      |                   | characteristics   |
   |                  |      |                   | need to be        |
   |                  |      |                   | imposed at the    |
   |                  |      |                   | node associated   |
   |                  |      |                   | with the terminal |
   |                  |      |                   | of the energy     |
   |                  |      |                   | source, such as   |
   |                  |      |                   | when voltages and |
   |                  |      |                   | angles from the   |
   |                  |      |                   | transmission      |
   |                  |      |                   | level are used as |
   |                  |      |                   | input to the      |
   |                  |      |                   | distribution      |
   |                  |      |                   | network. The      |
   |                  |      |                   | attribute shall   |
   |                  |      |                   | be a positive     |
   |                  |      |                   | value or zero.    |
   +------------------+------+-------------------+-------------------+
   | voltageMagnitude | 1..1 | `Volt             | Phase-to-phase    |
   |                  |      | age <#Voltage>`__ | open circuit      |
   |                  |      |                   | voltage magnitude |
   |                  |      |                   | used when voltage |
   |                  |      |                   | characteristics   |
   |                  |      |                   | need to be        |
   |                  |      |                   | imposed at the    |
   |                  |      |                   | node associated   |
   |                  |      |                   | with the terminal |
   |                  |      |                   | of the energy     |
   |                  |      |                   | source, such as   |
   |                  |      |                   | when voltages and |
   |                  |      |                   | angles from the   |
   |                  |      |                   | transmission      |
   |                  |      |                   | level are used as |
   |                  |      |                   | input to the      |
   |                  |      |                   | distribution      |
   |                  |      |                   | network. The      |
   |                  |      |                   | attribute shall   |
   |                  |      |                   | be a positive     |
   |                  |      |                   | value or zero.    |
   +------------------+------+-------------------+-------------------+
   | x                | 1..1 | `Reactanc         | Positive sequence |
   |                  |      | e <#Reactance>`__ | Thevenin          |
   |                  |      |                   | reactance.        |
   +------------------+------+-------------------+-------------------+
   | x0               | 1..1 | `Reactanc         | Zero sequence     |
   |                  |      | e <#Reactance>`__ | Thevenin          |
   |                  |      |                   | reactance.        |
   +------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-24

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: EquipmentContainer

   ` <#EquipmentContainer>`__

   .. rubric:: EquipmentContainer
      :name: equipmentcontainer
      :class: concrete

   Core

   A modelling construct to provide a root class for containing
   equipment.

   .. rubric:: Inherited Members
      :name: inherited-members-25

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: HydroGeneratingUnit

   ` <#HydroGeneratingUnit>`__

   .. rubric:: HydroGeneratingUnit
      :name: hydrogeneratingunit
      :class: concrete

   Production

   A generating unit whose prime mover is a hydraulic turbine (e.g.
   Francis, Pelton, Kaplan).

   .. rubric:: Inherited Members
      :name: inherited-members-26

   +---------------+------+---------------------+---------------------+
   | maxOperatingP | 1..1 | `ActivePowe         | see                 |
   |               |      | r <#ActivePower>`__ | `GeneratingU        |
   |               |      |                     | nit <#GeneratingUni |
   |               |      |                     | t.maxOperatingP>`__ |
   +---------------+------+---------------------+---------------------+
   | minOperatingP | 1..1 | `ActivePowe         | see                 |
   |               |      | r <#ActivePower>`__ | `GeneratingU        |
   |               |      |                     | nit <#GeneratingUni |
   |               |      |                     | t.minOperatingP>`__ |
   +---------------+------+---------------------+---------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: IBRPlant

   ` <#IBRPlant>`__

   .. rubric:: IBRPlant
      :name: ibrplant
      :class: concrete

   Emtiop

   An inverter-based resource (IBR) plant comprising a collection of
   components, e.g., a PowerElectronicsConnection with associated
   controls and GeneratingUnit, one or more PowerTransformers, one or
   more DisconnectingCircuitBreakers, and one or more ACLineSegments.
   The components may also include AC filter and DC bus modeling.

   .. rubric:: Native Members
      :name: native-members-22

   +-------------------+------+-------------------+-------------------+
   | dcLinkVoltage     | 0..1 | `Volt             | Voltage of the DC |
   |                   |      | age <#Voltage>`__ | bus, used to      |
   |                   |      |                   | scale average     |
   |                   |      |                   | source models or  |
   |                   |      |                   | to supply         |
   |                   |      |                   | switching models  |
   |                   |      |                   | of the converter. |
   +-------------------+------+-------------------+-------------------+
   | s                 | 0..1 | `Frequenc         | Pulse width       |
   | witchingFrequency |      | y <#Frequency>`__ | modulation (PWM)  |
   |                   |      |                   | switching         |
   |                   |      |                   | frequency of the  |
   |                   |      |                   | firing pulses in  |
   |                   |      |                   | a switching model |
   |                   |      |                   | of the converter. |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-27

   +----------------+--------------+----------------+----------------+
   | ACPointOf      | 0..1         | `ACPointOfCo   | see            |
   | CommonCoupling |              | mmonCoupling < | `Connected     |
   |                |              | #ACPointOfComm | Facility <#Con |
   |                |              | onCoupling>`__ | nectedFacility |
   |                |              |                | .ACPointOfComm |
   |                |              |                | onCoupling>`__ |
   +----------------+--------------+----------------+----------------+
   | Equipments     | 0..unbounded | `Equipment <   | see            |
   |                |              | #Equipment>`__ | `ConnectedF    |
   |                |              |                | acility <#Conn |
   |                |              |                | ectedFacility. |
   |                |              |                | Equipments>`__ |
   +----------------+--------------+----------------+----------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: IEEECigreAPI

   ` <#IEEECigreAPI>`__

   .. rubric:: IEEECigreAPI
      :name: ieeecigreapi
      :class: concrete

   Emtiop

   A dynamic link library (DLL) or other application programming
   interface (API) for inverter-based resource (IBR) control and other
   control applications, as defined in CIGRE Technical Brochure TB 958
   and IEEE Standards Association P3597. Attributes prefixed by **api**
   correspond to members of the IEEE_Cigre_DLLInterface_Model_Info
   header file structure that was documented in TB 958; they should be
   obtained and verified using the API.

   .. rubric:: Native Members
      :name: native-members-23

   +-------------------+------+-------------------+-------------------+
   | apiDL             | 0..1 | `St               | Codifies a        |
   | LInterfaceVersion |      | ring <#String>`__ | four-number       |
   |                   |      |                   | version of the    |
   |                   |      |                   | CIGRE TB 958      |
   |                   |      |                   | interface         |
   |                   |      |                   | standard          |
   |                   |      |                   | supported by this |
   |                   |      |                   | model, in string  |
   |                   |      |                   | format, as        |
   |                   |      |                   | returned from the |
   |                   |      |                   | API.              |
   +-------------------+------+-------------------+-------------------+
   | apiEmtRmsMode     | 0..1 | `IEEECigreAPIM    | Identify whether  |
   |                   |      | odeKind <#IEEECig | the model runs in |
   |                   |      | reAPIModeKind>`__ | EMT, RMS, or both |
   |                   |      |                   | kinds of          |
   |                   |      |                   | simulation, as    |
   |                   |      |                   | returned from the |
   |                   |      |                   | CIGRE TB 958 API. |
   +-------------------+------+-------------------+-------------------+
   | apiFixedS         | 0..1 | `Seco             | Hard-coded        |
   | tepBaseSampleTime |      | nds <#Seconds>`__ | simulation time   |
   |                   |      |                   | step for this     |
   |                   |      |                   | model, as         |
   |                   |      |                   | returned from the |
   |                   |      |                   | CIGRE TB 958 API. |
   +-------------------+------+-------------------+-------------------+
   | apiModelName      | 0..1 | `St               | The ModelName as  |
   |                   |      | ring <#String>`__ | returned from the |
   |                   |      |                   | CIGRE TB 958 API. |
   |                   |      |                   | Not necessarily   |
   |                   |      |                   | equal to the      |
   |                   |      |                   | inherited         |
   |                   |      |                   | Ident             |
   |                   |      |                   | ifiedObject.name. |
   +-------------------+------+-------------------+-------------------+
   | apiModelVersion   | 0..1 | `St               | Version of this   |
   |                   |      | ring <#String>`__ | model instance,   |
   |                   |      |                   | as returned from  |
   |                   |      |                   | the CIGRE TB 958  |
   |                   |      |                   | API.              |
   +-------------------+------+-------------------+-------------------+
   | shareable         | 0..1 | `Bool             | True if this DLL  |
   |                   |      | ean <#Boolean>`__ | can be loaded and |
   |                   |      |                   | used by different |
   |                   |      |                   | instances of      |
   |                   |      |                   | Equipment in the  |
   |                   |      |                   | same simulation.  |
   |                   |      |                   | This information  |
   |                   |      |                   | is not available  |
   |                   |      |                   | from the DLL API; |
   |                   |      |                   | it must be        |
   |                   |      |                   | determined from   |
   |                   |      |                   | careful review of |
   |                   |      |                   | the DLL           |
   |                   |      |                   | documentation.    |
   +-------------------+------+-------------------+-------------------+
   | snapshotUri       | 0..1 | `St               | Location of the   |
   |                   |      | ring <#String>`__ | optional snapshot |
   |                   |      |                   | file for          |
   |                   |      |                   | initializing the  |
   |                   |      |                   | DLL from a saved  |
   |                   |      |                   | state. Either a   |
   |                   |      |                   | universal         |
   |                   |      |                   | resource          |
   |                   |      |                   | identifier or     |
   |                   |      |                   | n                 |
   |                   |      |                   | etwork-accessible |
   |                   |      |                   | filename. It is   |
   |                   |      |                   | not obtainable    |
   |                   |      |                   | from the DLL API. |
   +-------------------+------+-------------------+-------------------+
   | uri               | 0..1 | `St               | Location of the   |
   |                   |      | ring <#String>`__ | DLL, e.g., a      |
   |                   |      |                   | universal         |
   |                   |      |                   | resource          |
   |                   |      |                   | identifier or     |
   |                   |      |                   | n                 |
   |                   |      |                   | etwork-accessible |
   |                   |      |                   | filename. It is   |
   |                   |      |                   | not obtainable    |
   |                   |      |                   | from the DLL API. |
   +-------------------+------+-------------------+-------------------+
   | IEEECigreAPIInfo  | 0..1 | `IEEEC            | Expanded set of   |
   |                   |      | igreAPIInfo <#IEE | attributes        |
   |                   |      | ECigreAPIInfo>`__ | available from    |
   |                   |      |                   | the CIGRE TB 958  |
   |                   |      |                   | API.              |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-28

   +-------------------+------+-------------------+-------------------+
   | Detailed          | 0..1 | `Detail           | see               |
   | ModelTypeDynamics |      | edModelTypeDynami | `Detaile          |
   |                   |      | cs <#DetailedMode | dModelDynamics <# |
   |                   |      | lTypeDynamics>`__ | DetailedModelDyna |
   |                   |      |                   | mics.DetailedMode |
   |                   |      |                   | lTypeDynamics>`__ |
   +-------------------+------+-------------------+-------------------+
   | Dyna              | 0..1 | `DynamicsFunctio  | see               |
   | micsFunctionBlock |      | nBlock <#Dynamics | `Det              |
   |                   |      | FunctionBlock>`__ | ailedModelDynamic |
   |                   |      |                   | s <#DetailedModel |
   |                   |      |                   | Dynamics.Dynamics |
   |                   |      |                   | FunctionBlock>`__ |
   +-------------------+------+-------------------+-------------------+
   | Equipment         | 0..1 | `Equipmen         | see               |
   |                   |      | t <#Equipment>`__ | `Detailed         |
   |                   |      |                   | ModelDynamics <#D |
   |                   |      |                   | etailedModelDynam |
   |                   |      |                   | ics.Equipment>`__ |
   +-------------------+------+-------------------+-------------------+

   +---------+------+------------------------+------------------------+
   | mRID    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.mRID>`__ |
   +---------+------+------------------------+------------------------+
   | enabled | 1..1 | `Boolean <#Boolean>`__ | see                    |
   |         |      |                        | `DynamicsFunct         |
   |         |      |                        | ionBlock <#DynamicsFun |
   |         |      |                        | ctionBlock.enabled>`__ |
   +---------+------+------------------------+------------------------+
   | name    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.name>`__ |
   +---------+------+------------------------+------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: IEEECigreAPIInfo

   ` <#IEEECigreAPIInfo>`__

   .. rubric:: IEEECigreAPIInfo
      :name: ieeecigreapiinfo
      :class: concrete

   Emtiop

   Supplemental information about this interface from the CIGRE TB 958
   API.

   .. rubric:: Native Members
      :name: native-members-24

   +-------------------+-------+-------------------+-------------------+
   | apiG              | 0..1  | `St               | One of two        |
   | eneralInformation |       | ring <#String>`__ | general           |
   |                   |       |                   | description       |
   |                   |       |                   | fields; also see  |
   |                   |       |                   | the               |
   |                   |       |                   | ap                |
   |                   |       |                   | iModelDescription |
   |                   |       |                   | attribute.        |
   +-------------------+-------+-------------------+-------------------+
   | apiModelCreated   | 0..1  | `DateTi           | Date and time of  |
   |                   |       | me <#DateTime>`__ | the first model   |
   |                   |       |                   | (not API)         |
   |                   |       |                   | version.          |
   +-------------------+-------+-------------------+-------------------+
   | apiModelCreator   | 0..1  | `St               | Identifies the    |
   |                   |       | ring <#String>`__ | person or the     |
   |                   |       |                   | organization who  |
   |                   |       |                   | first created the |
   |                   |       |                   | model.            |
   +-------------------+-------+-------------------+-------------------+
   | ap                | 0..1  | `St               | One of two        |
   | iModelDescription |       | ring <#String>`__ | general           |
   |                   |       |                   | description       |
   |                   |       |                   | fields; also see  |
   |                   |       |                   | the               |
   |                   |       |                   | apiG              |
   |                   |       |                   | eneralDescription |
   |                   |       |                   | attribute.        |
   +-------------------+-------+-------------------+-------------------+
   | apiMo             | 0..1  | `St               | Identifies the    |
   | delLastModifiedBy |       | ring <#String>`__ | person or the     |
   |                   |       |                   | organization who  |
   |                   |       |                   | first created the |
   |                   |       |                   | model.            |
   +-------------------+-------+-------------------+-------------------+
   | apiMode           | 0..1  | `DateTi           | Date and time of  |
   | lLastModifiedDate |       | me <#DateTime>`__ | the latest model  |
   |                   |       |                   | version.          |
   +-------------------+-------+-------------------+-------------------+
   | apiMod            | 0..1  | `St               | A description of  |
   | elModifiedComment |       | ring <#String>`__ | the latest model  |
   |                   |       |                   | update.           |
   +-------------------+-------+-------------------+-------------------+
   | apiMod            | 0..1  | `St               | A history of      |
   | elModifiedHistory |       | ring <#String>`__ | model updates;    |
   |                   |       |                   | may be a change   |
   |                   |       |                   | log or other      |
   |                   |       |                   | multi-paragraph   |
   |                   |       |                   | text.             |
   +-------------------+-------+-------------------+-------------------+
   | a                 | 0..1  | `Inte             | Size of internal  |
   | piNumDoubleStates |       | ger <#Integer>`__ | double-precision  |
   |                   |       |                   | array storage     |
   |                   |       |                   | needed by the     |
   |                   |       |                   | model instance    |
   |                   |       |                   | for state         |
   |                   |       |                   | variables. These  |
   |                   |       |                   | are not           |
   |                   |       |                   | represented in    |
   |                   |       |                   | CIM, but the      |
   |                   |       |                   | information could |
   |                   |       |                   | help identify     |
   |                   |       |                   | different         |
   |                   |       |                   | versions of this  |
   |                   |       |                   | model. The        |
   |                   |       |                   | EMT/RMS simulator |
   |                   |       |                   | manages this      |
   |                   |       |                   | memory.           |
   +-------------------+-------+-------------------+-------------------+
   | apiNumFloatStates | 0..1  | `Inte             | Size of internal  |
   |                   |       | ger <#Integer>`__ | single-precision  |
   |                   |       |                   | array storage     |
   |                   |       |                   | needed by this    |
   |                   |       |                   | model for state   |
   |                   |       |                   | variables. These  |
   |                   |       |                   | are not           |
   |                   |       |                   | represented in    |
   |                   |       |                   | CIM, but the      |
   |                   |       |                   | information could |
   |                   |       |                   | help identify     |
   |                   |       |                   | different         |
   |                   |       |                   | versions of this  |
   |                   |       |                   | model. The        |
   |                   |       |                   | EMT/RMS simulator |
   |                   |       |                   | manages this      |
   |                   |       |                   | memory.           |
   +-------------------+-------+-------------------+-------------------+
   | apiNumInputPorts  | 0..1  | `Inte             | The number of     |
   |                   |       | ger <#Integer>`__ | input ports       |
   |                   |       |                   | expected by this  |
   |                   |       |                   | model, which      |
   |                   |       |                   | should match      |
   |                   |       |                   | cardinality of    |
   |                   |       |                   | the associated    |
   |                   |       |                   | IEEECigreAPI ->   |
   |                   |       |                   | IEEECigr          |
   |                   |       |                   | eAPIInputSignals. |
   +-------------------+-------+-------------------+-------------------+
   | apiNumIntStates   | 0..1  | `Inte             | Size of internal  |
   |                   |       | ger <#Integer>`__ | integer array     |
   |                   |       |                   | storage needed by |
   |                   |       |                   | this model for    |
   |                   |       |                   | state variables.  |
   |                   |       |                   | These are not     |
   |                   |       |                   | represented in    |
   |                   |       |                   | CIM, but the      |
   |                   |       |                   | information could |
   |                   |       |                   | help identify     |
   |                   |       |                   | different         |
   |                   |       |                   | versions of this  |
   |                   |       |                   | model. The        |
   |                   |       |                   | EMT/RMS simulator |
   |                   |       |                   | manages this      |
   |                   |       |                   | memory.           |
   +-------------------+-------+-------------------+-------------------+
   | apiNumOutputPorts | 0..1  | `Inte             | The number of     |
   |                   |       | ger <#Integer>`__ | output ports      |
   |                   |       |                   | expected by this  |
   |                   |       |                   | model, which      |
   |                   |       |                   | should match      |
   |                   |       |                   | cardinality of    |
   |                   |       |                   | the associated    |
   |                   |       |                   | IEEECigreAPI ->   |
   |                   |       |                   | IEEECigre         |
   |                   |       |                   | APIOutputSignals. |
   +-------------------+-------+-------------------+-------------------+
   | apiNumParameters  | 0..1  | `Inte             | The number of     |
   |                   |       | ger <#Integer>`__ | input parameters  |
   |                   |       |                   | expected by this  |
   |                   |       |                   | model, which      |
   |                   |       |                   | should match      |
   |                   |       |                   | cardinality of    |
   |                   |       |                   | the associated    |
   |                   |       |                   | IEEECigreAPI ->   |
   |                   |       |                   | IEEECi            |
   |                   |       |                   | greAPIParameters. |
   +-------------------+-------+-------------------+-------------------+
   | IEEECigreAPIs     | 0..\* | `IEEECigreAPI <   | Minimum set of    |
   |                   |       | #IEEECigreAPI>`__ | attributes        |
   |                   |       |                   | required to use   |
   |                   |       |                   | this model.       |
   +-------------------+-------+-------------------+-------------------+

.. container:: group
   :name: IEEECigreAPIInput

   ` <#IEEECigreAPIInput>`__

   .. rubric:: IEEECigreAPIInput
      :name: ieeecigreapiinput
      :class: concrete

   Emtiop

   Connects the set of CIGRE TB 958 API input signals, for this
   instance, to points in the network model or to external references,
   like other controllers.

   .. rubric:: Native Members
      :name: native-members-25

   +-------------+------+----------------------+----------------------+
   | kind        | 0..1 | `IEEECigre           | The type of input    |
   |             |      | APIInputKind <#IEEEC | signal. If           |
   |             |      | igreAPIInputKind>`__ | remoteInputSignal,   |
   |             |      |                      | supply the           |
   |             |      |                      | RemoteInputSignal    |
   |             |      |                      | association. The     |
   |             |      |                      | phase attribute is   |
   |             |      |                      | required for         |
   |             |      |                      | acTerminalVoltage,   |
   |             |      |                      | acCurrentVsc, and    |
   |             |      |                      | acCurrentGrid. If    |
   |             |      |                      | apiDefined, the      |
   |             |      |                      | model must be        |
   |             |      |                      | queried through its  |
   |             |      |                      | API for more         |
   |             |      |                      | information.         |
   +-------------+------+----------------------+----------------------+
   | sensorRatio | 0..1 | `Float <#Float>`__   | Ratio between        |
   |             |      |                      | measured quantity on |
   |             |      |                      | the power network    |
   |             |      |                      | and signal quantity  |
   |             |      |                      | in the control       |
   |             |      |                      | system, e.g., a      |
   |             |      |                      | current transformer  |
   |             |      |                      | (CT) or voltage      |
   |             |      |                      | transformer (VT)     |
   |             |      |                      | ratio. Should be     |
   |             |      |                      | greater than or      |
   |             |      |                      | equal to 1.          |
   +-------------+------+----------------------+----------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-29

   +-------------------+------+-------------------+-------------------+
   | apiName           | 0..1 | `St               | see               |
   |                   |      | ring <#String>`__ | `                 |
   |                   |      |                   | IEEECigreAPISigna |
   |                   |      |                   | l <#IEEECigreAPIS |
   |                   |      |                   | ignal.apiName>`__ |
   +-------------------+------+-------------------+-------------------+
   | apiParameterKind  | 0..1 | `IEEECi           | see               |
   |                   |      | greAPIParameterKi | `IEEECigre        |
   |                   |      | nd <#IEEECigreAPI | APISignal <#IEEEC |
   |                   |      | ParameterKind>`__ | igreAPISignal.api |
   |                   |      |                   | ParameterKind>`__ |
   +-------------------+------+-------------------+-------------------+
   | apiSequenceNumber | 0..1 | `Inte             | see               |
   |                   |      | ger <#Integer>`__ | `IEEECigreA       |
   |                   |      |                   | PISignal <#IEEECi |
   |                   |      |                   | greAPISignal.apiS |
   |                   |      |                   | equenceNumber>`__ |
   +-------------------+------+-------------------+-------------------+
   | apiWidth          | 0..1 | `Inte             | see               |
   |                   |      | ger <#Integer>`__ | `I                |
   |                   |      |                   | EEECigreAPISignal |
   |                   |      |                   |  <#IEEECigreAPISi |
   |                   |      |                   | gnal.apiWidth>`__ |
   +-------------------+------+-------------------+-------------------+
   | multiplier        | 0..1 | `U                | see               |
   |                   |      | nitMultiplier <#U | `IEE              |
   |                   |      | nitMultiplier>`__ | ECigreAPISignal < |
   |                   |      |                   | #IEEECigreAPISign |
   |                   |      |                   | al.multiplier>`__ |
   +-------------------+------+-------------------+-------------------+
   | phase             | 0..1 | `Sin              | see               |
   |                   |      | glePhaseKind <#Si | `IEEECigreAPISig  |
   |                   |      | nglePhaseKind>`__ | nal <#IEEECigreAP |
   |                   |      |                   | ISignal.phase>`__ |
   +-------------------+------+-------------------+-------------------+
   | unit              | 0..1 | `UnitSymbol       | see               |
   |                   |      |  <#UnitSymbol>`__ | `IEEECigreAPISi   |
   |                   |      |                   | gnal <#IEEECigreA |
   |                   |      |                   | PISignal.unit>`__ |
   +-------------------+------+-------------------+-------------------+
   | ConnectivityNode  | 0..1 | `Conne            | see               |
   |                   |      | ctivityNode <#Con | `IEEECigre        |
   |                   |      | nectivityNode>`__ | APISignal <#IEEEC |
   |                   |      |                   | igreAPISignal.Con |
   |                   |      |                   | nectivityNode>`__ |
   +-------------------+------+-------------------+-------------------+
   | DCNode            | 0..1 | `DC               | see               |
   |                   |      | Node <#DCNode>`__ | `IEEECigreAPISign |
   |                   |      |                   | al <#IEEECigreAPI |
   |                   |      |                   | Signal.DCNode>`__ |
   +-------------------+------+-------------------+-------------------+
   | IEEEC             | 0..1 | `                 | see               |
   | igreAPISignalInfo |      | IEEECigreAPISigna | `IEEECigreAPISig  |
   |                   |      | lInfo <#IEEECigre | nal <#IEEECigreAP |
   |                   |      | APISignalInfo>`__ | ISignal.IEEECigre |
   |                   |      |                   | APISignalInfo>`__ |
   +-------------------+------+-------------------+-------------------+

   +-------------------+------+-------------------+-------------------+
   | ACDCTerminal      | 0..1 | `ACDCTerminal <   | see               |
   |                   |      | #ACDCTerminal>`__ | `S                |
   |                   |      |                   | ignalDescriptor < |
   |                   |      |                   | #SignalDescriptor |
   |                   |      |                   | .ACDCTerminal>`__ |
   +-------------------+------+-------------------+-------------------+
   | Dyna              | 0..1 | `DynamicsFunctio  | see               |
   | micsFunctionBlock |      | nBlock <#Dynamics | `SignalDesc       |
   |                   |      | FunctionBlock>`__ | riptor <#SignalDe |
   |                   |      |                   | scriptor.Dynamics |
   |                   |      |                   | FunctionBlock>`__ |
   +-------------------+------+-------------------+-------------------+

   +-------------------+------+-------------------+-------------------+
   | mRID              | 0..1 | `St               | see               |
   |                   |      | ring <#String>`__ | `Detaile          |
   |                   |      |                   | dModelDescriptor  |
   |                   |      |                   | <#DetailedModelDe |
   |                   |      |                   | scriptor.mRID>`__ |
   +-------------------+------+-------------------+-------------------+
   | Detailed          | 0..1 | `Detail           | see               |
   | ModelTypeDynamics |      | edModelTypeDynami | `DetailedMod      |
   |                   |      | cs <#DetailedMode | elDescriptor <#De |
   |                   |      | lTypeDynamics>`__ | tailedModelDescri |
   |                   |      |                   | ptor.DetailedMode |
   |                   |      |                   | lTypeDynamics>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: IEEECigreAPIOutput

   ` <#IEEECigreAPIOutput>`__

   .. rubric:: IEEECigreAPIOutput
      :name: ieeecigreapioutput
      :class: concrete

   Emtiop

   Connects the set of CIGRE TB 958 API output signals, for this
   instance, to points in the network model.

   .. rubric:: Native Members
      :name: native-members-26

   +--------------+------+----------------------+----------------------+
   | kind         | 0..1 | `IEEECigreAP         | The type of output   |
   |              |      | IOutputKind <#IEEECi | signal. The phase    |
   |              |      | greAPIOutputKind>`__ | attribute must be    |
   |              |      |                      | supplied with        |
   |              |      |                      | modulationIndex and  |
   |              |      |                      | vscVoltage. If       |
   |              |      |                      | apiDefined, obtain   |
   |              |      |                      | more information     |
   |              |      |                      | from the CIGRE TB    |
   |              |      |                      | 958 API.             |
   +--------------+------+----------------------+----------------------+
   | scalingRatio | 0..1 | `Float <#Float>`__   | Ratio between the    |
   |              |      |                      | controller output    |
   |              |      |                      | and the power system |
   |              |      |                      | connection point.    |
   |              |      |                      | For example, a       |
   |              |      |                      | modulation index     |
   |              |      |                      | output could be      |
   |              |      |                      | multiplied by 50% of |
   |              |      |                      | the DC link voltage  |
   |              |      |                      | of a converter to    |
   |              |      |                      | create a controlled  |
   |              |      |                      | voltage source       |
   |              |      |                      | connected to the AC  |
   |              |      |                      | power network. If    |
   |              |      |                      | the DC link voltage  |
   |              |      |                      | is 1200 V, the       |
   |              |      |                      | scalingRatio should  |
   |              |      |                      | then be 600. May be  |
   |              |      |                      | any value, noting    |
   |              |      |                      | that a value of zero |
   |              |      |                      | has no effect on the |
   |              |      |                      | power network.       |
   +--------------+------+----------------------+----------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-30

   +-------------------+------+-------------------+-------------------+
   | apiName           | 0..1 | `St               | see               |
   |                   |      | ring <#String>`__ | `                 |
   |                   |      |                   | IEEECigreAPISigna |
   |                   |      |                   | l <#IEEECigreAPIS |
   |                   |      |                   | ignal.apiName>`__ |
   +-------------------+------+-------------------+-------------------+
   | apiParameterKind  | 0..1 | `IEEECi           | see               |
   |                   |      | greAPIParameterKi | `IEEECigre        |
   |                   |      | nd <#IEEECigreAPI | APISignal <#IEEEC |
   |                   |      | ParameterKind>`__ | igreAPISignal.api |
   |                   |      |                   | ParameterKind>`__ |
   +-------------------+------+-------------------+-------------------+
   | apiSequenceNumber | 0..1 | `Inte             | see               |
   |                   |      | ger <#Integer>`__ | `IEEECigreA       |
   |                   |      |                   | PISignal <#IEEECi |
   |                   |      |                   | greAPISignal.apiS |
   |                   |      |                   | equenceNumber>`__ |
   +-------------------+------+-------------------+-------------------+
   | apiWidth          | 0..1 | `Inte             | see               |
   |                   |      | ger <#Integer>`__ | `I                |
   |                   |      |                   | EEECigreAPISignal |
   |                   |      |                   |  <#IEEECigreAPISi |
   |                   |      |                   | gnal.apiWidth>`__ |
   +-------------------+------+-------------------+-------------------+
   | multiplier        | 0..1 | `U                | see               |
   |                   |      | nitMultiplier <#U | `IEE              |
   |                   |      | nitMultiplier>`__ | ECigreAPISignal < |
   |                   |      |                   | #IEEECigreAPISign |
   |                   |      |                   | al.multiplier>`__ |
   +-------------------+------+-------------------+-------------------+
   | phase             | 0..1 | `Sin              | see               |
   |                   |      | glePhaseKind <#Si | `IEEECigreAPISig  |
   |                   |      | nglePhaseKind>`__ | nal <#IEEECigreAP |
   |                   |      |                   | ISignal.phase>`__ |
   +-------------------+------+-------------------+-------------------+
   | unit              | 0..1 | `UnitSymbol       | see               |
   |                   |      |  <#UnitSymbol>`__ | `IEEECigreAPISi   |
   |                   |      |                   | gnal <#IEEECigreA |
   |                   |      |                   | PISignal.unit>`__ |
   +-------------------+------+-------------------+-------------------+
   | ConnectivityNode  | 0..1 | `Conne            | see               |
   |                   |      | ctivityNode <#Con | `IEEECigre        |
   |                   |      | nectivityNode>`__ | APISignal <#IEEEC |
   |                   |      |                   | igreAPISignal.Con |
   |                   |      |                   | nectivityNode>`__ |
   +-------------------+------+-------------------+-------------------+
   | DCNode            | 0..1 | `DC               | see               |
   |                   |      | Node <#DCNode>`__ | `IEEECigreAPISign |
   |                   |      |                   | al <#IEEECigreAPI |
   |                   |      |                   | Signal.DCNode>`__ |
   +-------------------+------+-------------------+-------------------+
   | IEEEC             | 0..1 | `                 | see               |
   | igreAPISignalInfo |      | IEEECigreAPISigna | `IEEECigreAPISig  |
   |                   |      | lInfo <#IEEECigre | nal <#IEEECigreAP |
   |                   |      | APISignalInfo>`__ | ISignal.IEEECigre |
   |                   |      |                   | APISignalInfo>`__ |
   +-------------------+------+-------------------+-------------------+

   +-------------------+------+-------------------+-------------------+
   | ACDCTerminal      | 0..1 | `ACDCTerminal <   | see               |
   |                   |      | #ACDCTerminal>`__ | `S                |
   |                   |      |                   | ignalDescriptor < |
   |                   |      |                   | #SignalDescriptor |
   |                   |      |                   | .ACDCTerminal>`__ |
   +-------------------+------+-------------------+-------------------+
   | Dyna              | 0..1 | `DynamicsFunctio  | see               |
   | micsFunctionBlock |      | nBlock <#Dynamics | `SignalDesc       |
   |                   |      | FunctionBlock>`__ | riptor <#SignalDe |
   |                   |      |                   | scriptor.Dynamics |
   |                   |      |                   | FunctionBlock>`__ |
   +-------------------+------+-------------------+-------------------+

   +-------------------+------+-------------------+-------------------+
   | mRID              | 0..1 | `St               | see               |
   |                   |      | ring <#String>`__ | `Detaile          |
   |                   |      |                   | dModelDescriptor  |
   |                   |      |                   | <#DetailedModelDe |
   |                   |      |                   | scriptor.mRID>`__ |
   +-------------------+------+-------------------+-------------------+
   | Detailed          | 0..1 | `Detail           | see               |
   | ModelTypeDynamics |      | edModelTypeDynami | `DetailedMod      |
   |                   |      | cs <#DetailedMode | elDescriptor <#De |
   |                   |      | lTypeDynamics>`__ | tailedModelDescri |
   |                   |      |                   | ptor.DetailedMode |
   |                   |      |                   | lTypeDynamics>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: IEEECigreAPIParameter

   ` <#IEEECigreAPIParameter>`__

   .. rubric:: IEEECigreAPIParameter
      :name: ieeecigreapiparameter
      :class: concrete

   Emtiop

   A single value in the array of CIGRE TB 958 API input values. The
   meaning of this parameter is discoverable through the API for an
   implementation, like a DLL, and/or documentation provided with the
   model. This CIM class maintains only the essential parameter setting
   and location/size in the array of API inputs.

   .. rubric:: Native Members
      :name: native-members-27

   +-------------------+------+-------------------+-------------------+
   | apiParameterKind  | 0..1 | `IEEECi           | The C type of     |
   |                   |      | greAPIParameterKi | this parameter as |
   |                   |      | nd <#IEEECigreAPI | expected by the   |
   |                   |      | ParameterKind>`__ | CIGRE TB 958 API. |
   |                   |      |                   | This also         |
   |                   |      |                   | determines the    |
   |                   |      |                   | memory size of    |
   |                   |      |                   | this parameter in |
   |                   |      |                   | the array of      |
   |                   |      |                   | model inputs. It  |
   |                   |      |                   | indicates whether |
   |                   |      |                   | the value         |
   |                   |      |                   | attribute should  |
   |                   |      |                   | be considered a   |
   |                   |      |                   | string, integer,  |
   |                   |      |                   | or floating point |
   |                   |      |                   | value.            |
   +-------------------+------+-------------------+-------------------+
   | apiSequenceNumber | 0..1 | `Inte             | The zero-based    |
   |                   |      | ger <#Integer>`__ | array index for   |
   |                   |      |                   | this parameter,   |
   |                   |      |                   | as expected in    |
   |                   |      |                   | the CIGRE TB 958  |
   |                   |      |                   | API.              |
   +-------------------+------+-------------------+-------------------+
   | value             | 0..1 | `St               | The parameter     |
   |                   |      | ring <#String>`__ | value, to be      |
   |                   |      |                   | parsed from       |
   |                   |      |                   | string format     |
   |                   |      |                   | according to the  |
   |                   |      |                   | apiParameterKind. |
   +-------------------+------+-------------------+-------------------+
   | IEEECigreAPI      | 0..1 | `IEEECigreAPI <   | The API model     |
   |                   |      | #IEEECigreAPI>`__ | instance          |
   |                   |      |                   | associated with   |
   |                   |      |                   | this parameter.   |
   +-------------------+------+-------------------+-------------------+
   | IEEECigr          | 0..1 | `IEEECi           | Expanded set of   |
   | eAPIParameterInfo |      | greAPIParameterIn | attributes        |
   |                   |      | fo <#IEEECigreAPI | available from    |
   |                   |      | ParameterInfo>`__ | the CIGRE TB 958  |
   |                   |      |                   | API.              |
   +-------------------+------+-------------------+-------------------+

.. container:: group
   :name: IEEECigreAPIParameterInfo

   ` <#IEEECigreAPIParameterInfo>`__

   .. rubric:: IEEECigreAPIParameterInfo
      :name: ieeecigreapiparameterinfo
      :class: concrete

   Emtiop

   Supplemental information about this parameter from the CIGRE TB 958
   API.

   .. rubric:: Native Members
      :name: native-members-28

   +-------------------+-------+-------------------+-------------------+
   | apiDefaultValue   | 0..1  | `St               | Default value     |
   |                   |       | ring <#String>`__ | internally        |
   |                   |       |                   | assigned by the   |
   |                   |       |                   | model             |
   |                   |       |                   | implementation.   |
   +-------------------+-------+-------------------+-------------------+
   | apiDescription    | 0..1  | `St               | General           |
   |                   |       | ring <#String>`__ | description.      |
   +-------------------+-------+-------------------+-------------------+
   | apiFixedValue     | 0..1  | `Bool             | True if the       |
   |                   |       | ean <#Boolean>`__ | parameter can be  |
   |                   |       |                   | changed any time  |
   |                   |       |                   | during            |
   |                   |       |                   | simulation, False |
   |                   |       |                   | if the parameter  |
   |                   |       |                   | value must be set |
   |                   |       |                   | and time zero and |
   |                   |       |                   | not changed       |
   |                   |       |                   | thereafter.       |
   +-------------------+-------+-------------------+-------------------+
   | apiGroupName      | 0..1  | `St               | A group name, if  |
   |                   |       | ring <#String>`__ | applicable.       |
   +-------------------+-------+-------------------+-------------------+
   | apiMaxValue       | 0..1  | `St               | Maximum value     |
   |                   |       | ring <#String>`__ | allowed, for      |
   |                   |       |                   | numerical         |
   |                   |       |                   | parameters.       |
   +-------------------+-------+-------------------+-------------------+
   | apiMinValue       | 0..1  | `St               | Minimum value     |
   |                   |       | ring <#String>`__ | allowed, for      |
   |                   |       |                   | numerical         |
   |                   |       |                   | parameters.       |
   +-------------------+-------+-------------------+-------------------+
   | apiName           | 0..1  | `St               | The name of this  |
   |                   |       | ring <#String>`__ | parameter, as     |
   |                   |       |                   | returned by the   |
   |                   |       |                   | CIGRE TB 958 API. |
   |                   |       |                   | If there is an    |
   |                   |       |                   | inherited         |
   |                   |       |                   | Iden              |
   |                   |       |                   | tifiedObject.name |
   |                   |       |                   | attribute, it may |
   |                   |       |                   | not necessarily   |
   |                   |       |                   | match this name.  |
   +-------------------+-------+-------------------+-------------------+
   | apiUnit           | 0..1  | `St               | The parameter     |
   |                   |       | ring <#String>`__ | units expected by |
   |                   |       |                   | the CIGRE TB 958  |
   |                   |       |                   | API. This may not |
   |                   |       |                   | correspond to CIM |
   |                   |       |                   | units, so         |
   |                   |       |                   | interpretation    |
   |                   |       |                   | may be required.  |
   +-------------------+-------+-------------------+-------------------+
   | IEEEC             | 0..\* | `IEEECigreAPIPar  | Minimum set of    |
   | igreAPIParameters |       | ameter <#IEEECigr | attributes        |
   |                   |       | eAPIParameter>`__ | required to use   |
   |                   |       |                   | this parameter.   |
   +-------------------+-------+-------------------+-------------------+

.. container:: group
   :name: IEEECigreAPISignalInfo

   ` <#IEEECigreAPISignalInfo>`__

   .. rubric:: IEEECigreAPISignalInfo
      :name: ieeecigreapisignalinfo
      :class: concrete

   Emtiop

   Supplemental information about the signal from the CIGRE TB 958 API.

   .. rubric:: Native Members
      :name: native-members-29

   +-------------------+-------+-------------------+-------------------+
   | apiDescription    | 0..1  | `St               | A description of  |
   |                   |       | ring <#String>`__ | the signal as     |
   |                   |       |                   | written by the    |
   |                   |       |                   | model's           |
   |                   |       |                   | developer.        |
   +-------------------+-------+-------------------+-------------------+
   | apiUnit           | 0..1  | `St               | The signal units  |
   |                   |       | ring <#String>`__ | expected by the   |
   |                   |       |                   | CIGRE TB 958 API. |
   |                   |       |                   | This may not      |
   |                   |       |                   | correspond to CIM |
   |                   |       |                   | units, so         |
   |                   |       |                   | interpretation    |
   |                   |       |                   | may be required.  |
   +-------------------+-------+-------------------+-------------------+
   | IE                | 0..\* | `IEEECigre        | Minimum set of    |
   | EECigreAPISignals |       | APISignal <#IEEEC | attributes        |
   |                   |       | igreAPISignal>`__ | required to use   |
   |                   |       |                   | this signal.      |
   +-------------------+-------+-------------------+-------------------+

.. container:: group
   :name: LinearShuntCompensator

   ` <#LinearShuntCompensator>`__

   .. rubric:: LinearShuntCompensator
      :name: linearshuntcompensator
      :class: concrete

   Wires

   A linear shunt compensator has banks or sections with equal
   admittance values.

   .. rubric:: Native Members
      :name: native-members-30

   +-------------+------+----------------------+----------------------+
   | bPerSection | 1..1 | `Susceptan           | Positive sequence    |
   |             |      | ce <#Susceptance>`__ | shunt (charging)     |
   |             |      |                      | susceptance per      |
   |             |      |                      | section.             |
   +-------------+------+----------------------+----------------------+
   | gPerSection | 1..1 | `Conductan           | Positive sequence    |
   |             |      | ce <#Conductance>`__ | shunt (charging)     |
   |             |      |                      | conductance per      |
   |             |      |                      | section.             |
   +-------------+------+----------------------+----------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-31

   +-----------------+------+-------------------+-------------------+
   | grounded        | 1..1 | `Bool             | see               |
   |                 |      | ean <#Boolean>`__ | `ShuntCompensat   |
   |                 |      |                   | or <#ShuntCompens |
   |                 |      |                   | ator.grounded>`__ |
   +-----------------+------+-------------------+-------------------+
   | maximumSections | 1..1 | `Inte             | see               |
   |                 |      | ger <#Integer>`__ | `Shun             |
   |                 |      |                   | tCompensator <#Sh |
   |                 |      |                   | untCompensator.ma |
   |                 |      |                   | ximumSections>`__ |
   +-----------------+------+-------------------+-------------------+
   | nomU            | 1..1 | `Volt             | see               |
   |                 |      | age <#Voltage>`__ | `ShuntCompe       |
   |                 |      |                   | nsator <#ShuntCom |
   |                 |      |                   | pensator.nomU>`__ |
   +-----------------+------+-------------------+-------------------+
   | phaseConnection | 0..1 | `Phas             | see               |
   |                 |      | eShuntConnectionK | `Shun             |
   |                 |      | ind <#PhaseShuntC | tCompensator <#Sh |
   |                 |      | onnectionKind>`__ | untCompensator.ph |
   |                 |      |                   | aseConnection>`__ |
   +-----------------+------+-------------------+-------------------+
   | sections        | 1..1 | `                 | see               |
   |                 |      | Float <#Float>`__ | `ShuntCompensat   |
   |                 |      |                   | or <#ShuntCompens |
   |                 |      |                   | ator.sections>`__ |
   +-----------------+------+-------------------+-------------------+

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: LoadResponseCharacteristic

   ` <#LoadResponseCharacteristic>`__

   .. rubric:: LoadResponseCharacteristic
      :name: loadresponsecharacteristic
      :class: concrete

   LoadModel

   Models the characteristic response of the load demand due to changes
   in system conditions such as voltage and frequency. It is not related
   to demand response.

   If LoadResponseCharacteristic.exponentModel is True, the exponential
   voltage or frequency dependent models are specified and used as to
   calculate active and reactive power components of the load model.

   The equations to calculate active and reactive power components of
   the load model are internal to the power flow calculation, hence they
   use different quantities depending on the use case of the data
   exchange.

   The equations for exponential voltage dependent load model injected
   power are:

   pInjection= Pnominal\* (Voltage/cim:BaseVoltage.nominalVoltage) \*\*
   cim:LoadResponseCharacteristic.pVoltageExponent

   qInjection= Qnominal\* (Voltage/cim:BaseVoltage.nominalVoltage) \*\*
   cim:LoadResponseCharacteristic.qVoltageExponent

   pInjection = Pnominal\* (Frequency/(Nominal
   frequency))**cim:LoadResponseCharacteristic.pFrequencyExponent

   qInjection = Qnominal\* (Frequency/(Nominal
   frequency))**cim:LoadResponseCharacteristic.qFrequencyExponent

   Note that both voltage and frequency exponents could be used together
   so the full equation would be:

   pInjection = Pnominal\*
   (Voltage/(cim:BaseVoltage.nominalVoltage))**cim:LoadResponseCharacteristic.pVoltageExponent
   \* (Frequency/(base
   frequency))**cim:LoadResponseCharacteristic.pFrequencyExponent

   qInjection = Qnominal\*
   (Voltage/(cim:BaseVoltage.nominalVoltage))**cim:LoadResponseCharacteristic.qVoltageExponent
   \* (Frequency/(base
   frequency))**cim:LoadResponseCharacteristic.qFrequencyExponent

   The voltage and frequency expressed in the equation are values
   obtained from solved power flow. Base voltage and base frequency are
   those derived from the connectivity of the static network model.

   Where:

   1) \* means "multiply" and \*\* is "raised to the power of";

   2) Pnominal and Qnominal represent the active power and reactive
   power at nominal voltage as any load described by the voltage
   exponential model shall be given at nominal voltage. This means that
   EnergyConsumer.p and EnergyConsumer.q are at nominal voltage.

   3) After power flow is solved:

   -pInjection and qInjection correspond to SvPowerflow.p and
   SvPowerflow.q respectively.

   - Voltage corresponds to SvVoltage.v at the TopologicalNode where the
   load is connected.

   .. rubric:: Native Members
      :name: native-members-31

   +----------------+----------------+----------------+----------------+
   | exponentModel  | 1..1           | `Boo           | Indicates the  |
   |                |                | lean           | exponential    |
   |                |                |  <#Boolean>`__ | voltage        |
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
   |                |                |                | - p            |
   |                |                |                | V              |
   |                |                |                | oltageExponent |
   |                |                |                |                |
   |                |                |                | - q            |
   |                |                |                | V              |
   |                |                |                | oltageExponent |
   |                |                |                |                |
   |                |                |                | - pFr          |
   |                |                |                | e              |
   |                |                |                | quencyExponent |
   |                |                |                |                |
   |                |                |                | - qFre         |
   |                |                |                | q              |
   |                |                |                | uencyExponent. |
   |                |                |                |                |
   |                |                |                | The            |
   |                |                |                | coefficient    |
   |                |                |                | model consist  |
   |                |                |                | of the         |
   |                |                |                | attributes:    |
   |                |                |                |                |
   |                |                |                | - pCo          |
   |                |                |                | n              |
   |                |                |                | stantImpedance |
   |                |                |                |                |
   |                |                |                | - p            |
   |                |                |                | C              |
   |                |                |                | onstantCurrent |
   |                |                |                |                |
   |                |                |                | -              |
   |                |                |                | pConstantPower |
   |                |                |                |                |
   |                |                |                | - qCo          |
   |                |                |                | n              |
   |                |                |                | stantImpedance |
   |                |                |                |                |
   |                |                |                | - q            |
   |                |                |                | C              |
   |                |                |                | onstantCurrent |
   |                |                |                |                |
   |                |                |                | -              |
   |                |                |                | q              |
   |                |                |                | ConstantPower. |
   |                |                |                |                |
   |                |                |                | The sum of     |
   |                |                |                | pCon           |
   |                |                |                | s              |
   |                |                |                | tantImpedance, |
   |                |                |                | p              |
   |                |                |                | C              |
   |                |                |                | onstantCurrent |
   |                |                |                | and            |
   |                |                |                | pConstantPower |
   |                |                |                | shall equal 1. |
   |                |                |                |                |
   |                |                |                | The sum of     |
   |                |                |                | qCon           |
   |                |                |                | s              |
   |                |                |                | tantImpedance, |
   |                |                |                | q              |
   |                |                |                | C              |
   |                |                |                | onstantCurrent |
   |                |                |                | and            |
   |                |                |                | qConstantPower |
   |                |                |                | shall equal 1. |
   +----------------+----------------+----------------+----------------+
   | p              | 1..1           | `Flo           | Portion of     |
   | C              |                | at <#Float>`__ | active power   |
   | onstantCurrent |                |                | load modelled  |
   |                |                |                | as constant    |
   |                |                |                | current.       |
   +----------------+----------------+----------------+----------------+
   | pCo            | 1..1           | `Flo           | Portion of     |
   | n              |                | at <#Float>`__ | active power   |
   | stantImpedance |                |                | load modelled  |
   |                |                |                | as constant    |
   |                |                |                | impedance.     |
   +----------------+----------------+----------------+----------------+
   | pConstantPower | 1..1           | `Flo           | Portion of     |
   |                |                | at <#Float>`__ | active power   |
   |                |                |                | load modelled  |
   |                |                |                | as constant    |
   |                |                |                | power.         |
   +----------------+----------------+----------------+----------------+
   | pFr            | 1..1           | `Flo           | Exponent of    |
   | e              |                | at <#Float>`__ | per unit       |
   | quencyExponent |                |                | frequency      |
   |                |                |                | effecting      |
   |                |                |                | active power.  |
   +----------------+----------------+----------------+----------------+
   | p              | 1..1           | `Flo           | Exponent of    |
   | V              |                | at <#Float>`__ | per unit       |
   | oltageExponent |                |                | voltage        |
   |                |                |                | effecting real |
   |                |                |                | power.         |
   +----------------+----------------+----------------+----------------+
   | q              | 1..1           | `Flo           | Portion of     |
   | C              |                | at <#Float>`__ | reactive power |
   | onstantCurrent |                |                | load modelled  |
   |                |                |                | as constant    |
   |                |                |                | current.       |
   +----------------+----------------+----------------+----------------+
   | qCo            | 1..1           | `Flo           | Portion of     |
   | n              |                | at <#Float>`__ | reactive power |
   | stantImpedance |                |                | load modelled  |
   |                |                |                | as constant    |
   |                |                |                | impedance.     |
   +----------------+----------------+----------------+----------------+
   | qConstantPower | 1..1           | `Flo           | Portion of     |
   |                |                | at <#Float>`__ | reactive power |
   |                |                |                | load modelled  |
   |                |                |                | as constant    |
   |                |                |                | power.         |
   +----------------+----------------+----------------+----------------+
   | qFr            | 1..1           | `Flo           | Exponent of    |
   | e              |                | at <#Float>`__ | per unit       |
   | quencyExponent |                |                | frequency      |
   |                |                |                | effecting      |
   |                |                |                | reactive       |
   |                |                |                | power.         |
   +----------------+----------------+----------------+----------------+
   | q              | 1..1           | `Flo           | Exponent of    |
   | V              |                | at <#Float>`__ | per unit       |
   | oltageExponent |                |                | voltage        |
   |                |                |                | effecting      |
   |                |                |                | reactive       |
   |                |                |                | power.         |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-32

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: MachineSaturationCurve

   ` <#MachineSaturationCurve>`__

   .. rubric:: MachineSaturationCurve
      :name: machinesaturationcurve
      :class: concrete

   Emtiop

   Use to define machine saturation with more than two points. xUnit is
   A (RMS current) and y1Unit is none (per-unit voltage).

   .. rubric:: Native Members
      :name: native-members-32

   +-------------------+------+-------------------+-------------------+
   | Synchrono         | 0..1 | `Synchron         | The synchronous   |
   | usMachineDetailed |      | ousMachineDetaile | machine this      |
   |                   |      | d <#SynchronousMa | saturation        |
   |                   |      | chineDetailed>`__ | characteristic    |
   |                   |      |                   | applies to.       |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-33

   +--------------+------+----------------------+----------------------+
   | mRID         | 1..1 | `String <#String>`__ | see                  |
   |              |      |                      | `Cu                  |
   |              |      |                      | rve <#Curve.mRID>`__ |
   +--------------+------+----------------------+----------------------+
   | curveStyle   | 0..1 | `CurveSt             | see                  |
   |              |      | yle <#CurveStyle>`__ | `Curve <#            |
   |              |      |                      | Curve.curveStyle>`__ |
   +--------------+------+----------------------+----------------------+
   | name         | 1..1 | `String <#String>`__ | see                  |
   |              |      |                      | `Cu                  |
   |              |      |                      | rve <#Curve.name>`__ |
   +--------------+------+----------------------+----------------------+
   | xMultiplier  | 0..1 | `UnitMultiplier      | see                  |
   |              |      | <#UnitMultiplier>`__ | `Curve <#C           |
   |              |      |                      | urve.xMultiplier>`__ |
   +--------------+------+----------------------+----------------------+
   | xUnit        | 0..1 | `UnitSym             | see                  |
   |              |      | bol <#UnitSymbol>`__ | `Cur                 |
   |              |      |                      | ve <#Curve.xUnit>`__ |
   +--------------+------+----------------------+----------------------+
   | y1Multiplier | 0..1 | `UnitMultiplier      | see                  |
   |              |      | <#UnitMultiplier>`__ | `Curve <#Cu          |
   |              |      |                      | rve.y1Multiplier>`__ |
   +--------------+------+----------------------+----------------------+
   | y1Unit       | 0..1 | `UnitSym             | see                  |
   |              |      | bol <#UnitSymbol>`__ | `Curv                |
   |              |      |                      | e <#Curve.y1Unit>`__ |
   +--------------+------+----------------------+----------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: NthAmDynamicModel

   ` <#NthAmDynamicModel>`__

   .. rubric:: NthAmDynamicModel
      :name: nthamdynamicmodel
      :class: concrete

   Emtiop

   Parameterized models from software libraries or user code that rely
   on documentation provided elsewhere, e.g., software documentation.
   The model is named within the domain of nameKind, e.g., ST6B for DYR
   or esst6b for DYD. Parameters are maintained by name and sequence
   number in the ParameterDescriptor class.

   .. rubric:: Native Members
      :name: native-members-33

   +-------------------+------+-------------------+-------------------+
   | clo               | 0..1 | `St               | Name of the       |
   | sestStandardModel |      | ring <#String>`__ | closest match     |
   |                   |      |                   | from Dynamics /   |
   |                   |      |                   | StandardModels,   |
   |                   |      |                   | if such a match   |
   |                   |      |                   | exists.           |
   +-------------------+------+-------------------+-------------------+
   | modelKind         | 0..1 | `N                | Suggested         |
   |                   |      | thAmModelKind <#N | application of    |
   |                   |      | thAmModelKind>`__ | this dynamic      |
   |                   |      |                   | model.            |
   +-------------------+------+-------------------+-------------------+
   | nameKind          | 0..1 | `NthAmMode        |                   |
   |                   |      | lNameKind <#NthAm |                   |
   |                   |      | ModelNameKind>`__ |                   |
   +-------------------+------+-------------------+-------------------+
   | statusKind        | 0..1 | `NthAmModelSta    |                   |
   |                   |      | tusKind <#NthAmMo |                   |
   |                   |      | delStatusKind>`__ |                   |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-34

.. container:: group
   :name: NuclearGeneratingUnit

   ` <#NuclearGeneratingUnit>`__

   .. rubric:: NuclearGeneratingUnit
      :name: nucleargeneratingunit
      :class: concrete

   Production

   A nuclear generating unit.

   .. rubric:: Inherited Members
      :name: inherited-members-35

   +---------------+------+---------------------+---------------------+
   | maxOperatingP | 1..1 | `ActivePowe         | see                 |
   |               |      | r <#ActivePower>`__ | `GeneratingU        |
   |               |      |                     | nit <#GeneratingUni |
   |               |      |                     | t.maxOperatingP>`__ |
   +---------------+------+---------------------+---------------------+
   | minOperatingP | 1..1 | `ActivePowe         | see                 |
   |               |      | r <#ActivePower>`__ | `GeneratingU        |
   |               |      |                     | nit <#GeneratingUni |
   |               |      |                     | t.minOperatingP>`__ |
   +---------------+------+---------------------+---------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: OperationalLimitSet

   ` <#OperationalLimitSet>`__

   .. rubric:: OperationalLimitSet
      :name: operationallimitset
      :class: concrete

   OperationalLimits

   A set of limits associated with equipment. Sets of limits might apply
   to a specific temperature, or season for example. A set of limits may
   contain different severities of limit levels that would apply to the
   same equipment. The set may contain limits of different types such as
   apparent power and current limits or high and low voltage limits that
   are logically applied together as a set.

   .. rubric:: Native Members
      :name: native-members-34

   +----------------+----------------+----------------+----------------+
   | mRID           | 1..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | name           | 1..1           | `S             | The name is    |
   |                |                | trin           | any free human |
   |                |                | g <#String>`__ | readable and   |
   |                |                |                | possibly non   |
   |                |                |                | unique text    |
   |                |                |                | naming the     |
   |                |                |                | object.        |
   +----------------+----------------+----------------+----------------+
   | Terminal       | 1..1           | `ACD           | The terminal   |
   |                |                | CTerminal <#ac | where the      |
   |                |                | dcterminal>`__ | operational    |
   |                |                | (              | limit set      |
   |                |                | #ACDCTerminal) | apply.         |
   +----------------+----------------+----------------+----------------+

.. container:: group
   :name: OperationalLimitType

   ` <#OperationalLimitType>`__

   .. rubric:: OperationalLimitType
      :name: operationallimittype
      :class: concrete

   OperationalLimits

   The operational meaning of a category of limits.

   .. rubric:: Native Members
      :name: native-members-35

   +----------------+----------------+----------------+----------------+
   | mRID           | 1..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | acc            | 0..1           | `Sec           | The nominal    |
   | e              |                | onds           | acceptable     |
   | ptableDuration |                |  <#Seconds>`__ | duration of    |
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
   |                |                |                | flag isI       |
   |                |                |                | n              |
   |                |                |                | finiteDuration |
   |                |                |                | is set to      |
   |                |                |                | false, hence   |
   |                |                |                | it shall not   |
   |                |                |                | be exchanged   |
   |                |                |                | when isI       |
   |                |                |                | n              |
   |                |                |                | finiteDuration |
   |                |                |                | is set to      |
   |                |                |                | true.          |
   +----------------+----------------+----------------+----------------+
   | direction      | 0..1           | `Op            | The direction  |
   |                |                | e              | of the limit.  |
   |                |                | rationalLimitD |                |
   |                |                | irectionKind   |                |
   |                |                |  <#%20Operatio |                |
   |                |                | nalLimi%20tDir |                |
   |                |                | ectionKind>`__ |                |
   +----------------+----------------+----------------+----------------+
   | isI            | 0..1           | `Boo           | Defines if the |
   | n              |                | lean           | operational    |
   | finiteDuration |                |  <#Boolean>`__ | limit type has |
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
   |                |                |                | acce           |
   |                |                |                | p              |
   |                |                |                | tableDuration. |
   +----------------+----------------+----------------+----------------+
   | name           | 1..1           | `S             | The name is    |
   |                |                | trin           | any free human |
   |                |                | g <#String>`__ | readable and   |
   |                |                |                | possibly non   |
   |                |                |                | unique text    |
   |                |                |                | naming the     |
   |                |                |                | object.        |
   +----------------+----------------+----------------+----------------+

.. container:: group
   :name: ParameterDescriptor

   ` <#ParameterDescriptor>`__

   .. rubric:: ParameterDescriptor
      :name: parameterdescriptor
      :class: concrete

   DetailedModelDescription

   Supports definition of one or more parameters of several different
   datatypes for use by the detailed model. It describes the parameters
   used in the equations of the detailed model.

   The name of the parameter shall be the same as the name used in the
   equations of the detailed model.

   .. rubric:: Native Members
      :name: native-members-36

   +-----------------+------+-------------------+-------------------+
   | engineeringUnit | 0..1 | `St               | The engineering   |
   |                 |      | ring <#String>`__ | unit of the       |
   |                 |      |                   | value.            |
   +-----------------+------+-------------------+-------------------+
   | sequenceNumber  | 0..1 | `Inte             | Sequence number   |
   |                 |      | ger <#Integer>`__ | of the parameter  |
   |                 |      |                   | among the set of  |
   |                 |      |                   | parameters        |
   |                 |      |                   | associated with   |
   |                 |      |                   | the related       |
   |                 |      |                   | proprietary       |
   |                 |      |                   | user-defined      |
   |                 |      |                   | model.            |
   +-----------------+------+-------------------+-------------------+
   | typicalValue    | 0..1 | `St               | Typical value for |
   |                 |      | ring <#String>`__ | the parameter.    |
   |                 |      |                   | The datatype is   |
   |                 |      |                   | as specified in   |
   |                 |      |                   | attribute         |
   |                 |      |                   | valueXSDdatatype. |
   +-----------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-36

   +-------------------+------+-------------------+-------------------+
   | mRID              | 0..1 | `St               | see               |
   |                   |      | ring <#String>`__ | `Detaile          |
   |                   |      |                   | dModelDescriptor  |
   |                   |      |                   | <#DetailedModelDe |
   |                   |      |                   | scriptor.mRID>`__ |
   +-------------------+------+-------------------+-------------------+
   | Detailed          | 0..1 | `Detail           | see               |
   | ModelTypeDynamics |      | edModelTypeDynami | `DetailedMod      |
   |                   |      | cs <#DetailedMode | elDescriptor <#De |
   |                   |      | lTypeDynamics>`__ | tailedModelDescri |
   |                   |      |                   | ptor.DetailedMode |
   |                   |      |                   | lTypeDynamics>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: ParameterValue

   ` <#ParameterValue>`__

   .. rubric:: ParameterValue
      :name: parametervalue
      :class: concrete

   DetailedModelDescription

   Provides the value of a given parameter of a detailed model dynamics.

   .. rubric:: Native Members
      :name: native-members-37

   +-------------------+------+-------------------+-------------------+
   | value             | 0..1 | `St               | The value of the  |
   |                   |      | ring <#String>`__ | parameter.        |
   +-------------------+------+-------------------+-------------------+
   | Deta              | 0..1 | `DetailedModelDy  | The detailed      |
   | iledModelDynamics |      | namics <#Detailed | model to which    |
   |                   |      | ModelDynamics>`__ | this parameter    |
   |                   |      |                   | value applies.    |
   +-------------------+------+-------------------+-------------------+
   | Pa                | 0..1 | `ParameterDe      | The parameter     |
   | rameterDescriptor |      | scriptor <#Parame | descriptor that   |
   |                   |      | terDescriptor>`__ | has this value.   |
   +-------------------+------+-------------------+-------------------+

.. container:: group
   :name: PhaseTapChangerLinear

   ` <#PhaseTapChangerLinear>`__

   .. rubric:: PhaseTapChangerLinear
      :name: phasetapchangerlinear
      :class: concrete

   Wires

   Describes a tap changer with a linear relation between the tap step
   and the phase angle difference across the transformer. This is a
   mathematical model that is an approximation of a real phase tap
   changer.

   The phase angle is computed as stepPhaseShiftIncrement times the tap
   position.

   The voltage magnitude of both sides is the same.

   .. rubric:: Native Members
      :name: native-members-38

   +----------------+----------------+----------------+----------------+
   | stepPhas       | 0..1           | `Ang           | Phase shift    |
   | e              |                | leDegrees <#an | per step       |
   | ShiftIncrement |                | gledegrees>`__ | position. A    |
   |                |                | (              | positive value |
   |                |                | #AngleDegrees) | indicates a    |
   |                |                |                | positive angle |
   |                |                |                | variation from |
   |                |                |                | the Terminal   |
   |                |                |                | at the Power   |
   |                |                |                | T              |
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
   | xMax           | 0..1           | `Reactan       | The reactance  |
   |                |                | ce <           | depends on the |
   |                |                | #Reactance>`__ | tap position   |
   |                |                |                | according to a |
   |                |                |                | "u" shaped     |
   |                |                |                | curve. The     |
   |                |                |                | maximum        |
   |                |                |                | reactance      |
   |                |                |                | (xMax) appears |
   |                |                |                | at the low and |
   |                |                |                | high tap       |
   |                |                |                | positions.     |
   |                |                |                | Depending on   |
   |                |                |                | the "u" curve  |
   |                |                |                | the attribute  |
   |                |                |                | can be either  |
   |                |                |                | higher or      |
   |                |                |                | lower than     |
   |                |                |                | PowerTr        |
   |                |                |                | a              |
   |                |                |                | nsformerEnd.x. |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-37

   +----------------+------+-------------------+-------------------+
   | TransformerEnd | 0..1 | `T                | see               |
   |                |      | ransformerEnd <#T | `P                |
   |                |      | ransformerEnd>`__ | haseTapChanger <# |
   |                |      |                   | PhaseTapChanger.T |
   |                |      |                   | ransformerEnd>`__ |
   +----------------+------+-------------------+-------------------+

   +-------------+------+----------------------+----------------------+
   | highStep    | 0..1 | `I                   | see                  |
   |             |      | nteger <#Integer>`__ | `TapChanger <#Tap    |
   |             |      |                      | Changer.highStep>`__ |
   +-------------+------+----------------------+----------------------+
   | lowStep     | 0..1 | `I                   | see                  |
   |             |      | nteger <#Integer>`__ | `TapChanger <#Ta     |
   |             |      |                      | pChanger.lowStep>`__ |
   +-------------+------+----------------------+----------------------+
   | neutralStep | 0..1 | `I                   | see                  |
   |             |      | nteger <#Integer>`__ | `TapChanger <#TapCha |
   |             |      |                      | nger.neutralStep>`__ |
   +-------------+------+----------------------+----------------------+
   | neutralU    | 0..1 | `V                   | see                  |
   |             |      | oltage <#Voltage>`__ | `TapChanger <#Tap    |
   |             |      |                      | Changer.neutralU>`__ |
   +-------------+------+----------------------+----------------------+
   | normalStep  | 0..1 | `I                   | see                  |
   |             |      | nteger <#Integer>`__ | `TapChanger <#TapCh  |
   |             |      |                      | anger.normalStep>`__ |
   +-------------+------+----------------------+----------------------+
   | step        | 1..1 | `Float <#Float>`__   | see                  |
   |             |      |                      | `TapChanger <        |
   |             |      |                      | #TapChanger.step>`__ |
   +-------------+------+----------------------+----------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: PhotoVoltaicUnit

   ` <#PhotoVoltaicUnit>`__

   .. rubric:: PhotoVoltaicUnit
      :name: photovoltaicunit
      :class: concrete

   Production

   A photovoltaic device or an aggregation of such devices.

   .. rubric:: Inherited Members
      :name: inherited-members-38

   +-------------------+------+-------------------+-------------------+
   | maxP              | 1..1 | `ActivePower      | see               |
   |                   |      | <#ActivePower>`__ | `P                |
   |                   |      |                   | owerElectronicsUn |
   |                   |      |                   | it <#PowerElectro |
   |                   |      |                   | nicsUnit.maxP>`__ |
   +-------------------+------+-------------------+-------------------+
   | minP              | 1..1 | `ActivePower      | see               |
   |                   |      | <#ActivePower>`__ | `P                |
   |                   |      |                   | owerElectronicsUn |
   |                   |      |                   | it <#PowerElectro |
   |                   |      |                   | nicsUnit.minP>`__ |
   +-------------------+------+-------------------+-------------------+
   | PowerElec         | 1..1 | `PowerEle         | see               |
   | tronicsConnection |      | ctronicsConnectio | `PowerE           |
   |                   |      | n <#PowerElectron | lectronicsUnit <# |
   |                   |      | icsConnection>`__ | PowerElectronicsU |
   |                   |      |                   | nit.PowerElectron |
   |                   |      |                   | icsConnection>`__ |
   +-------------------+------+-------------------+-------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: PowerElectronicsConnection

   ` <#PowerElectronicsConnection>`__

   .. rubric:: PowerElectronicsConnection
      :name: powerelectronicsconnection
      :class: concrete

   Wires

   A connection to the AC network for energy production or consumption
   that uses power electronics rather than rotating machines.

   .. rubric:: Native Members
      :name: native-members-39

   +----------------+----------------+----------------+----------------+
   | maxIFault      | 1..1           | `PU <#PU>`__   | Maximum fault  |
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
   | maxQ           | 1..1           | `React         | Maximum        |
   |                |                | ivePower <#Rea | reactive power |
   |                |                | ctivePower>`__ | limit. This is |
   |                |                |                | the maximum    |
   |                |                |                | (nameplate)    |
   |                |                |                | limit for the  |
   |                |                |                | unit.          |
   +----------------+----------------+----------------+----------------+
   | minQ           | 1..1           | `React         | Minimum        |
   |                |                | ivePower <#Rea | reactive power |
   |                |                | ctivePower>`__ | limit for the  |
   |                |                |                | unit. This is  |
   |                |                |                | the minimum    |
   |                |                |                | (nameplate)    |
   |                |                |                | limit for the  |
   |                |                |                | unit.          |
   +----------------+----------------+----------------+----------------+
   | p              | 1..1           | `A             | Active power   |
   |                |                | ctivePower <#A | injection.     |
   |                |                | ctivePower>`__ | Load sign      |
   |                |                |                | convention is  |
   |                |                |                | used, i.e.     |
   |                |                |                | positive sign  |
   |                |                |                | means flow out |
   |                |                |                | from a node.   |
   |                |                |                |                |
   |                |                |                | Starting value |
   |                |                |                | for a steady   |
   |                |                |                | state          |
   |                |                |                | solution.      |
   +----------------+----------------+----------------+----------------+
   | q              | 1..1           | `React         | Reactive power |
   |                |                | ivePower <#Rea | injection.     |
   |                |                | ctivePower>`__ | Load sign      |
   |                |                |                | convention is  |
   |                |                |                | used, i.e.     |
   |                |                |                | positive sign  |
   |                |                |                | means flow out |
   |                |                |                | from a node.   |
   |                |                |                |                |
   |                |                |                | Starting value |
   |                |                |                | for a steady   |
   |                |                |                | state          |
   |                |                |                | solution.      |
   +----------------+----------------+----------------+----------------+
   | ratedS         | 1..1           | `Appar         | Nameplate      |
   |                |                | entPower <#App | apparent power |
   |                |                | arentPower>`__ | rating for the |
   |                |                |                | unit.          |
   |                |                |                |                |
   |                |                |                | The attribute  |
   |                |                |                | shall have a   |
   |                |                |                | positive       |
   |                |                |                | value.         |
   +----------------+----------------+----------------+----------------+
   | ratedU         | 1..1           | `Vol           | Rated voltage  |
   |                |                | tage           | (nameplate     |
   |                |                |  <#Voltage>`__ | data, Ur in    |
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

   .. rubric:: Inherited Members
      :name: inherited-members-39

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: PowerElectronicsConnectionDCTerminal

   ` <#PowerElectronicsConnectionDCTerminal>`__

   .. rubric:: PowerElectronicsConnectionDCTerminal
      :name: powerelectronicsconnectiondcterminal
      :class: concrete

   Emtiop

   A DC connection point at the converter, which is also connected on
   the AC side as any other AC ConductingEquipment. This special
   terminal is separate from the regular DCTerminal to restrict the
   connection, such that no other DC conducting equipment can be
   connected to the AC side.

   .. rubric:: Native Members
      :name: native-members-40

   +-------------------+------+-------------------+-------------------+
   | polarity          | 0..1 | `                 | Use to indicated  |
   |                   |      | DCTerminalPolarit | positive or       |
   |                   |      | yKind <#DCTermina | negative polarity |
   |                   |      | lPolarityKind>`__ | on the DC side.   |
   +-------------------+------+-------------------+-------------------+
   | PowerElec         | 0..1 | `PowerEle         | The               |
   | tronicsConnection |      | ctronicsConnectio | PowerElec         |
   |                   |      | n <#PowerElectron | tronicsConnection |
   |                   |      | icsConnection>`__ | for this          |
   |                   |      |                   | terminal.         |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-40

   +--------+------+----------------------+-------------------------+
   | DCNode | 1..1 | `DCNode <#DCNode>`__ | see                     |
   |        |      |                      | `DCBaseTerminal <#DC    |
   |        |      |                      | BaseTerminal.DCNode>`__ |
   +--------+------+----------------------+-------------------------+

   +----------------+------+-------------------+-------------------+
   | sequenceNumber | 1..1 | `Inte             | see               |
   |                |      | ger <#Integer>`__ | `ACDCTerminal     |
   |                |      |                   |  <#ACDCTerminal.s |
   |                |      |                   | equenceNumber>`__ |
   +----------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: PowerElectronicsWindUnit

   ` <#PowerElectronicsWindUnit>`__

   .. rubric:: PowerElectronicsWindUnit
      :name: powerelectronicswindunit
      :class: concrete

   Production

   A wind generating unit that connects to the AC network with power
   electronics rather than rotating machines or an aggregation of such
   units.

   .. rubric:: Inherited Members
      :name: inherited-members-41

   +-------------------+------+-------------------+-------------------+
   | maxP              | 1..1 | `ActivePower      | see               |
   |                   |      | <#ActivePower>`__ | `P                |
   |                   |      |                   | owerElectronicsUn |
   |                   |      |                   | it <#PowerElectro |
   |                   |      |                   | nicsUnit.maxP>`__ |
   +-------------------+------+-------------------+-------------------+
   | minP              | 1..1 | `ActivePower      | see               |
   |                   |      | <#ActivePower>`__ | `P                |
   |                   |      |                   | owerElectronicsUn |
   |                   |      |                   | it <#PowerElectro |
   |                   |      |                   | nicsUnit.minP>`__ |
   +-------------------+------+-------------------+-------------------+
   | PowerElec         | 1..1 | `PowerEle         | see               |
   | tronicsConnection |      | ctronicsConnectio | `PowerE           |
   |                   |      | n <#PowerElectron | lectronicsUnit <# |
   |                   |      | icsConnection>`__ | PowerElectronicsU |
   |                   |      |                   | nit.PowerElectron |
   |                   |      |                   | icsConnection>`__ |
   +-------------------+------+-------------------+-------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: PowerTransformer

   ` <#PowerTransformer>`__

   .. rubric:: PowerTransformer
      :name: powertransformer
      :class: concrete

   Wires

   An electrical device consisting of two or more coupled windings, with
   or without a magnetic core, for introducing mutual coupling between
   electric circuits. Transformers can be used to control voltage and
   phase shift (active power flow).

   A power transformer may be composed of separate transformer tanks
   that need not be identical.

   A power transformer can be modelled with or without tanks and is
   intended for use in both balanced and unbalanced representations. A
   power transformer typically has two terminals, but may have one
   (grounding), three or more terminals.

   The inherited association ConductingEquipment.BaseVoltage should not
   be used. The association from TransformerEnd to BaseVoltage should be
   used instead.

   .. rubric:: Native Members
      :name: native-members-41

   +----------------+----------------+----------------+----------------+
   | vectorGroup    | 1..1           | `S             | Vector group   |
   |                |                | trin           | of the         |
   |                |                | g <#String>`__ | transformer    |
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

   .. rubric:: Inherited Members
      :name: inherited-members-42

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: PowerTransformerEnd

   ` <#PowerTransformerEnd>`__

   .. rubric:: PowerTransformerEnd
      :name: powertransformerend
      :class: concrete

   Wires

   A PowerTransformerEnd is associated with each Terminal of a
   PowerTransformer.

   The impedance values r, r0, x, and x0 of a PowerTransformerEnd
   represents a star equivalent as follows.

   1) two PowerTransformerEnd-s shall be defined for a two Terminal
   PowerTransformer even if the two PowerTransformerEnd-s have the same
   rated voltage. The high voltage PowerTransformerEnd
   (TransformerEnd.endNumber=1) is the one used to exchange resistances
   (r, r0) and reactances (x, x0) of the PowerTransformer while the low
   voltage PowerTransformerEnd (TransformerEnd.endNumber=2) shall have
   zero impedance values.

   2) for a three Terminal PowerTransformer the three
   PowerTransformerEnds represent a star equivalent with each leg in the
   star represented by r, r0, x, and x0 values.

   3) For a three Terminal transformer each PowerTransformerEnd shall
   have g, g0, b and b0 values corresponding to the no load losses
   distributed on the three PowerTransformerEnds. The total no load loss
   shunt impedances may also be placed at one of the
   PowerTransformerEnds, preferably the end numbered 1, having the shunt
   values on end 1. This is the preferred way.

   4) for a PowerTransformer with more than three Terminals the
   PowerTransformerEnd impedance values cannot be used. Instead use the
   TransformerMeshImpedance or split the transformer into multiple
   PowerTransformers.

   Each PowerTransformerEnd must be contained by a PowerTransformer.
   Because a PowerTransformerEnd (or any other object) can not be
   contained by more than one parent, a PowerTransformerEnd can not have
   an association to an EquipmentContainer (Substation, VoltageLevel,
   etc).

   .. rubric:: Native Members
      :name: native-members-42

   +----------------+----------------+----------------+----------------+
   | connectionKind | 1..1           | `WindingC      | Kind of        |
   |                |                | onnectio       | connection.    |
   |                |                | n <#Win%20ding |                |
   |                |                | Connection>`__ |                |
   +----------------+----------------+----------------+----------------+
   | p              | 1..1           | `Int           | Terminal       |
   | haseAngleClock |                | eger           | voltage phase  |
   |                |                |  <#Integer>`__ | angle          |
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
   |                |                |                | 'Dyn11',       |
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
   | ratedS         | 1..1           | `Appar         | Normal         |
   |                |                | entPower <#App | apparent power |
   |                |                | arentPower>`__ | rating.        |
   |                |                |                |                |
   |                |                |                | The attribute  |
   |                |                |                | shall be a     |
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
   | ratedU         | 1..1           | `Vol           | Rated voltage: |
   |                |                | tage           | phase-phase    |
   |                |                |  <#Voltage>`__ | for            |
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
   | P              | 1..1           | `PowerT        | The power      |
   | o              |                | ransform       | transformer of |
   | werTransformer |                | er <#Po%20werT | this power     |
   |                |                | ransformer>`__ | transformer    |
   |                |                |                | end.           |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-43

   +-------------+------+----------------------+----------------------+
   | mRID        | 1..1 | `String <#String>`__ | see                  |
   |             |      |                      | `                    |
   |             |      |                      | TransformerEnd <#Tra |
   |             |      |                      | nsformerEnd.mRID>`__ |
   +-------------+------+----------------------+----------------------+
   | endNumber   | 1..1 | `I                   | see                  |
   |             |      | nteger <#Integer>`__ | `Trans               |
   |             |      |                      | formerEnd <#Transfor |
   |             |      |                      | merEnd.endNumber>`__ |
   +-------------+------+----------------------+----------------------+
   | grounded    | 1..1 | `B                   | see                  |
   |             |      | oolean <#Boolean>`__ | `Tran                |
   |             |      |                      | sformerEnd <#Transfo |
   |             |      |                      | rmerEnd.grounded>`__ |
   +-------------+------+----------------------+----------------------+
   | name        | 1..1 | `String <#String>`__ | see                  |
   |             |      |                      | `                    |
   |             |      |                      | TransformerEnd <#Tra |
   |             |      |                      | nsformerEnd.name>`__ |
   +-------------+------+----------------------+----------------------+
   | rground     | 1..1 | `Resista             | see                  |
   |             |      | nce <#Resistance>`__ | `Tra                 |
   |             |      |                      | nsformerEnd <#Transf |
   |             |      |                      | ormerEnd.rground>`__ |
   +-------------+------+----------------------+----------------------+
   | xground     | 1..1 | `React               | see                  |
   |             |      | ance <#Reactance>`__ | `Tra                 |
   |             |      |                      | nsformerEnd <#Transf |
   |             |      |                      | ormerEnd.xground>`__ |
   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 1..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `Transfo             |
   |             |      |                      | rmerEnd <#Transforme |
   |             |      |                      | rEnd.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+
   | Terminal    | 1..1 | `Ter                 | see                  |
   |             |      | minal <#Terminal>`__ | `Tran                |
   |             |      |                      | sformerEnd <#Transfo |
   |             |      |                      | rmerEnd.Terminal>`__ |
   +-------------+------+----------------------+----------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: RatioTapChanger

   ` <#RatioTapChanger>`__

   .. rubric:: RatioTapChanger
      :name: ratiotapchanger
      :class: concrete

   Wires

   A tap changer that changes the voltage ratio impacting the voltage
   magnitude but not the phase angle across the transformer.

   Angle sign convention (general): Positive value indicates a positive
   phase shift from the winding where the tap is located to the other
   winding (for a two-winding transformer).

   .. rubric:: Native Members
      :name: native-members-43

   +----------------+----------------+----------------+----------------+
   | stepV          | 1..1           | `Per           | Tap step       |
   | o              |                | Cent           | increment, in  |
   | ltageIncrement |                |  <#PerCent>`__ | per cent of    |
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
   | TransformerEnd | 1..1           | `Tr            | Transformer    |
   |                |                | ansforme       | end to which   |
   |                |                | rEnd <#%20Tran | this ratio tap |
   |                |                | sformerEnd>`__ | changer        |
   |                |                |                | belongs.       |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-44

   +-------------+------+----------------------+----------------------+
   | highStep    | 0..1 | `I                   | see                  |
   |             |      | nteger <#Integer>`__ | `TapChanger <#Tap    |
   |             |      |                      | Changer.highStep>`__ |
   +-------------+------+----------------------+----------------------+
   | lowStep     | 0..1 | `I                   | see                  |
   |             |      | nteger <#Integer>`__ | `TapChanger <#Ta     |
   |             |      |                      | pChanger.lowStep>`__ |
   +-------------+------+----------------------+----------------------+
   | neutralStep | 0..1 | `I                   | see                  |
   |             |      | nteger <#Integer>`__ | `TapChanger <#TapCha |
   |             |      |                      | nger.neutralStep>`__ |
   +-------------+------+----------------------+----------------------+
   | neutralU    | 0..1 | `V                   | see                  |
   |             |      | oltage <#Voltage>`__ | `TapChanger <#Tap    |
   |             |      |                      | Changer.neutralU>`__ |
   +-------------+------+----------------------+----------------------+
   | normalStep  | 0..1 | `I                   | see                  |
   |             |      | nteger <#Integer>`__ | `TapChanger <#TapCh  |
   |             |      |                      | anger.normalStep>`__ |
   +-------------+------+----------------------+----------------------+
   | step        | 1..1 | `Float <#Float>`__   | see                  |
   |             |      |                      | `TapChanger <        |
   |             |      |                      | #TapChanger.step>`__ |
   +-------------+------+----------------------+----------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: RotatingMachinePlant

   ` <#RotatingMachinePlant>`__

   .. rubric:: RotatingMachinePlant
      :name: rotatingmachineplant
      :class: concrete

   Emtiop

   A conventional generating plant, e.g., SynchronousMachine with
   associated controls and GeneratingUnit, a PowerTransformer, and a
   DisconnectingCircuitBreaker for thermal and hydro plants.

   .. rubric:: Inherited Members
      :name: inherited-members-45

   +----------------+--------------+----------------+----------------+
   | ACPointOf      | 0..1         | `ACPointOfCo   | see            |
   | CommonCoupling |              | mmonCoupling < | `Connected     |
   |                |              | #ACPointOfComm | Facility <#Con |
   |                |              | onCoupling>`__ | nectedFacility |
   |                |              |                | .ACPointOfComm |
   |                |              |                | onCoupling>`__ |
   +----------------+--------------+----------------+----------------+
   | Equipments     | 0..unbounded | `Equipment <   | see            |
   |                |              | #Equipment>`__ | `ConnectedF    |
   |                |              |                | acility <#Conn |
   |                |              |                | ectedFacility. |
   |                |              |                | Equipments>`__ |
   +----------------+--------------+----------------+----------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: SeriesCompensator

   ` <#SeriesCompensator>`__

   .. rubric:: SeriesCompensator
      :name: seriescompensator
      :class: concrete

   Wires

   A Series Compensator is a series capacitor or reactor or an AC
   transmission line without charging susceptance. It is a two terminal
   device.

   .. rubric:: Native Members
      :name: native-members-44

   == ==== ============================ =============================
   r  1..1 `Resistance <#Resistance>`__ Positive sequence resistance.
   r0 1..1 `Resistance <#Resistance>`__ Zero sequence resistance.
   x  1..1 `Reactance <#Reactance>`__   Positive sequence reactance.
   x0 1..1 `Reactance <#Reactance>`__   Zero sequence reactance.
   == ==== ============================ =============================

   .. rubric:: Inherited Members
      :name: inherited-members-46

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: StaticVarCompensator

   ` <#StaticVarCompensator>`__

   .. rubric:: StaticVarCompensator
      :name: staticvarcompensator
      :class: concrete

   FACTS

   A facility for providing variable and controllable shunt reactive
   power. The SVC typically consists of a stepdown transformer, filter,
   thyristor-controlled reactor, and thyristor-switched capacitor arms.

   The SVC may operate in fixed MVar output mode or in voltage control
   mode. When in voltage control mode, the output of the SVC will be
   proportional to the deviation of voltage at the controlled bus from
   the voltage setpoint. The SVC characteristic slope defines the
   proportion. If the voltage at the controlled bus is equal to the
   voltage setpoint, the SVC MVar output is zero.

   .. rubric:: Native Members
      :name: native-members-45

   +----------------+----------------+----------------+----------------+
   | c              | 0..1           | `Reactan       | Capacitive     |
   | a              |                | ce <           | reactance at   |
   | pacitiveRating |                | #Reactance>`__ | maximum        |
   |                |                |                | capacitive     |
   |                |                |                | reactive       |
   |                |                |                | power. Shall   |
   |                |                |                | always be      |
   |                |                |                | positive.      |
   +----------------+----------------+----------------+----------------+
   | i              | 0..1           | `Reactan       | Inductive      |
   | nductiveRating |                | ce <           | reactance at   |
   |                |                | #Reactance>`__ | maximum        |
   |                |                |                | inductive      |
   |                |                |                | reactive       |
   |                |                |                | power. Shall   |
   |                |                |                | always be      |
   |                |                |                | negative.      |
   +----------------+----------------+----------------+----------------+
   | q              | 0..1           | `React         | Reactive power |
   |                |                | ivePower <#Rea | injection.     |
   |                |                | ctivePower>`__ | Load sign      |
   |                |                |                | convention is  |
   |                |                |                | used, i.e.     |
   |                |                |                | positive sign  |
   |                |                |                | means flow out |
   |                |                |                | from a node.   |
   |                |                |                |                |
   |                |                |                | Starting value |
   |                |                |                | for a steady   |
   |                |                |                | state          |
   |                |                |                | solution.      |
   +----------------+----------------+----------------+----------------+
   | slope          | 0..1           | `Volta         | The            |
   |                |                | g              | c              |
   |                |                | ePerReactivePo | haracteristics |
   |                |                | wer <#Vo       | slope of an    |
   |                |                | ltagePe%20rRea | SVC defines    |
   |                |                | ctivePower>`__ | how the        |
   |                |                |                | reactive power |
   |                |                |                | output changes |
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
   | sVCControlMode | 0..1           | `SV            | SVC control    |
   |                |                | CControl       | mode.          |
   |                |                | Mode <#%20SVCC |                |
   |                |                | ontrolMode>`__ |                |
   +----------------+----------------+----------------+----------------+
   | v              | 0..1           | `Vol           | The reactive   |
   | oltageSetPoint |                | tage           | power output   |
   |                |                |  <#Voltage>`__ | of the SVC is  |
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

   .. rubric:: Inherited Members
      :name: inherited-members-47

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: SvDCPowerFlow

   ` <#SvDCPowerFlow>`__

   .. rubric:: SvDCPowerFlow
      :name: svdcpowerflow
      :class: concrete

   StateVariables

   State variable for power flow. Load convention is used for flow
   direction. This means flow out from the DCTopologicalNode into the
   equipment is positive.

   .. rubric:: Native Members
      :name: native-members-46

   +------------+------+-----------------------+-----------------------+
   | p          | 0..1 | `ActivePo             | The active power      |
   |            |      | wer <#ActivePower>`__ | flow. Load sign       |
   |            |      |                       | convention is used,   |
   |            |      |                       | i.e. positive sign    |
   |            |      |                       | means flow out from a |
   |            |      |                       | DCTopologicalNode     |
   |            |      |                       | (bus) into the        |
   |            |      |                       | conducting equipment. |
   +------------+------+-----------------------+-----------------------+
   | DCTerminal | 0..1 | `DCTerm               | The DC terminal       |
   |            |      | inal <#DCTerminal>`__ | associated with the   |
   |            |      |                       | DC power flow state   |
   |            |      |                       | variable.             |
   +------------+------+-----------------------+-----------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-48

.. container:: group
   :name: SvDCVoltage

   ` <#SvDCVoltage>`__

   .. rubric:: SvDCVoltage
      :name: svdcvoltage
      :class: concrete

   StateVariables

   State variable for direct current voltage.

   .. rubric:: Native Members
      :name: native-members-47

   +-------------------+------+-------------------+-------------------+
   | v                 | 0..1 | `Volt             | State variable    |
   |                   |      | age <#Voltage>`__ | for direct        |
   |                   |      |                   | current voltage.  |
   +-------------------+------+-------------------+-------------------+
   | DCTopologicalNode | 0..1 | `DCTopol          | The DC            |
   |                   |      | ogicalNode <#DCTo | topological node  |
   |                   |      | pologicalNode>`__ | associated with   |
   |                   |      |                   | the DC voltage    |
   |                   |      |                   | state.            |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-49

.. container:: group
   :name: SvPowerFlow

   ` <#SvPowerFlow>`__

   .. rubric:: SvPowerFlow
      :name: svpowerflow
      :class: concrete

   StateVariables

   State variable for power flow. Load convention is used for flow
   direction. This means flow out from the TopologicalNode into the
   equipment is positive.

   .. rubric:: Native Members
      :name: native-members-48

   +----------+------+------------------------+------------------------+
   | p        | 0..1 | `ActiveP               | The active power flow. |
   |          |      | ower <#ActivePower>`__ | Load sign convention   |
   |          |      |                        | is used, i.e. positive |
   |          |      |                        | sign means flow out    |
   |          |      |                        | from a TopologicalNode |
   |          |      |                        | (bus) into the         |
   |          |      |                        | conducting equipment.  |
   +----------+------+------------------------+------------------------+
   | q        | 0..1 | `ReactivePow           | The reactive power     |
   |          |      | er <#ReactivePower>`__ | flow. Load sign        |
   |          |      |                        | convention is used,    |
   |          |      |                        | i.e. positive sign     |
   |          |      |                        | means flow out from a  |
   |          |      |                        | TopologicalNode (bus)  |
   |          |      |                        | into the conducting    |
   |          |      |                        | equipment.             |
   +----------+------+------------------------+------------------------+
   | Terminal | 0..1 | `T                     | The terminal           |
   |          |      | erminal <#Terminal>`__ | associated with the    |
   |          |      |                        | power flow state       |
   |          |      |                        | variable.              |
   +----------+------+------------------------+------------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-50

.. container:: group
   :name: SvShuntCompensatorSections

   ` <#SvShuntCompensatorSections>`__

   .. rubric:: SvShuntCompensatorSections
      :name: svshuntcompensatorsections
      :class: concrete

   StateVariables

   State variable for the number of sections in service for a shunt
   compensator.

   .. rubric:: Native Members
      :name: native-members-49

   +------------------+------+-------------------+-------------------+
   | phase            | 0..1 | `Sin              | The terminal      |
   |                  |      | glePhaseKind <#Si | phase at which    |
   |                  |      | nglePhaseKind>`__ | the connection is |
   |                  |      |                   | applied. If       |
   |                  |      |                   | missing, the      |
   |                  |      |                   | injection is      |
   |                  |      |                   | assumed to be     |
   |                  |      |                   | balanced among    |
   |                  |      |                   | non-neutral       |
   |                  |      |                   | phases.           |
   +------------------+------+-------------------+-------------------+
   | sections         | 0..1 | `                 | The number of     |
   |                  |      | Float <#Float>`__ | sections in       |
   |                  |      |                   | service as a      |
   |                  |      |                   | continuous        |
   |                  |      |                   | variable. The     |
   |                  |      |                   | attribute shall   |
   |                  |      |                   | be a positive     |
   |                  |      |                   | value or zero. To |
   |                  |      |                   | get integer value |
   |                  |      |                   | scale with        |
   |                  |      |                   | ShuntCompens      |
   |                  |      |                   | ator.bPerSection. |
   +------------------+------+-------------------+-------------------+
   | ShuntCompensator | 0..1 | `Shunt            | The shunt         |
   |                  |      | Compensator <#Shu | compensator for   |
   |                  |      | ntCompensator>`__ | which the state   |
   |                  |      |                   | applies.          |
   +------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-51

.. container:: group
   :name: SvStatus

   ` <#SvStatus>`__

   .. rubric:: SvStatus
      :name: svstatus
      :class: concrete

   StateVariables

   State variable for status.

   .. rubric:: Native Members
      :name: native-members-50

   +-------------------+------+-------------------+-------------------+
   | inService         | 0..1 | `Bool             | The in service    |
   |                   |      | ean <#Boolean>`__ | status as a       |
   |                   |      |                   | result of         |
   |                   |      |                   | topology          |
   |                   |      |                   | processing. It    |
   |                   |      |                   | indicates if the  |
   |                   |      |                   | equipment is      |
   |                   |      |                   | considered as     |
   |                   |      |                   | energized by the  |
   |                   |      |                   | power flow. It    |
   |                   |      |                   | reflects if the   |
   |                   |      |                   | equipment is      |
   |                   |      |                   | connected within  |
   |                   |      |                   | a solvable        |
   |                   |      |                   | island. It does   |
   |                   |      |                   | not necessarily   |
   |                   |      |                   | reflect whether   |
   |                   |      |                   | or not the island |
   |                   |      |                   | was solved by the |
   |                   |      |                   | power flow.       |
   +-------------------+------+-------------------+-------------------+
   | phase             | 0..1 | `Sin              | The individual    |
   |                   |      | glePhaseKind <#Si | phase status. If  |
   |                   |      | nglePhaseKind>`__ | the attribute is  |
   |                   |      |                   | unspecified, then |
   |                   |      |                   | three phase model |
   |                   |      |                   | is assumed.       |
   +-------------------+------+-------------------+-------------------+
   | Co                | 0..1 | `ConductingE      | The conducting    |
   | nductingEquipment |      | quipment <#Conduc | equipment         |
   |                   |      | tingEquipment>`__ | associated with   |
   |                   |      |                   | the status state  |
   |                   |      |                   | variable.         |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-52

.. container:: group
   :name: SvSwitch

   ` <#SvSwitch>`__

   .. rubric:: SvSwitch
      :name: svswitch
      :class: concrete

   StateVariables

   State variable for switch.

   .. rubric:: Native Members
      :name: native-members-51

   +--------+------+-------------------------+-------------------------+
   | open   | 0..1 | `Boolean <#Boolean>`__  | The attribute tells if  |
   |        |      |                         | the computed state of   |
   |        |      |                         | the switch is           |
   |        |      |                         | considered open.        |
   +--------+------+-------------------------+-------------------------+
   | phase  | 0..1 | `SinglePhaseKin         | The terminal phase at   |
   |        |      | d <#SinglePhaseKind>`__ | which the connection is |
   |        |      |                         | applied. If missing,    |
   |        |      |                         | the injection is        |
   |        |      |                         | assumed to be balanced  |
   |        |      |                         | among non-neutral       |
   |        |      |                         | phases.                 |
   +--------+------+-------------------------+-------------------------+
   | Switch | 0..1 | `Switch <#Switch>`__    | The switch associated   |
   |        |      |                         | with the switch state.  |
   +--------+------+-------------------------+-------------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-53

.. container:: group
   :name: SvTapStep

   ` <#SvTapStep>`__

   .. rubric:: SvTapStep
      :name: svtapstep
      :class: concrete

   StateVariables

   State variable for transformer tap step.

   .. rubric:: Native Members
      :name: native-members-52

   +------------+------+-----------------------+-----------------------+
   | position   | 0..1 | `Float <#Float>`__    | The floating point    |
   |            |      |                       | tap position. This is |
   |            |      |                       | not the tap ratio,    |
   |            |      |                       | but rather the tap    |
   |            |      |                       | step position as      |
   |            |      |                       | defined by the        |
   |            |      |                       | related tap changer   |
   |            |      |                       | model and normally is |
   |            |      |                       | constrained to be     |
   |            |      |                       | within the range of   |
   |            |      |                       | minimum and maximum   |
   |            |      |                       | tap positions.        |
   +------------+------+-----------------------+-----------------------+
   | TapChanger | 0..1 | `TapCha               | The tap changer       |
   |            |      | nger <#TapChanger>`__ | associated with the   |
   |            |      |                       | tap step state.       |
   +------------+------+-----------------------+-----------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-54

.. container:: group
   :name: SvVoltage

   ` <#SvVoltage>`__

   .. rubric:: SvVoltage
      :name: svvoltage
      :class: concrete

   StateVariables

   State variable for voltage.

   .. rubric:: Native Members
      :name: native-members-53

   +-----------------+------+-------------------+-------------------+
   | angle           | 0..1 | `AngleDegrees <   | The voltage angle |
   |                 |      | #AngleDegrees>`__ | of the            |
   |                 |      |                   | topological node  |
   |                 |      |                   | complex voltage   |
   |                 |      |                   | with respect to   |
   |                 |      |                   | system reference. |
   +-----------------+------+-------------------+-------------------+
   | v               | 0..1 | `Volt             | The voltage       |
   |                 |      | age <#Voltage>`__ | magnitude at the  |
   |                 |      |                   | topological node. |
   |                 |      |                   | The attribute     |
   |                 |      |                   | shall be a        |
   |                 |      |                   | positive value.   |
   +-----------------+------+-------------------+-------------------+
   | TopologicalNode | 0..1 | `Top              | The topological   |
   |                 |      | ologicalNode <#To | node associated   |
   |                 |      | pologicalNode>`__ | with the voltage  |
   |                 |      |                   | state.            |
   +-----------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-55

.. container:: group
   :name: SynchronousMachine

   ` <#SynchronousMachine>`__

   .. rubric:: SynchronousMachine
      :name: synchronousmachine
      :class: concrete

   Wires

   An electromechanical device that operates with shaft rotating
   synchronously with the network. It is a single machine operating
   either as a generator or synchronous condenser or pump.

   .. rubric:: Native Members
      :name: native-members-54

   +-------------------+------+-------------------+-------------------+
   | earthing          | 1..1 | `Bool             | Indicates whether |
   |                   |      | ean <#Boolean>`__ | or not the        |
   |                   |      |                   | generator is      |
   |                   |      |                   | earthed. Used for |
   |                   |      |                   | short circuit     |
   |                   |      |                   | data exchange     |
   |                   |      |                   | according to IEC  |
   |                   |      |                   | 60909.            |
   +-------------------+------+-------------------+-------------------+
   | e                 | 1..1 | `Resistance       | Generator star    |
   | arthingStarPointR |      |  <#Resistance>`__ | point earthing    |
   |                   |      |                   | resistance (Re).  |
   |                   |      |                   | Used for short    |
   |                   |      |                   | circuit data      |
   |                   |      |                   | exchange          |
   |                   |      |                   | according to IEC  |
   |                   |      |                   | 60909.            |
   +-------------------+------+-------------------+-------------------+
   | e                 | 1..1 | `Reactanc         | Generator star    |
   | arthingStarPointX |      | e <#Reactance>`__ | point earthing    |
   |                   |      |                   | reactance (Xe).   |
   |                   |      |                   | Used for short    |
   |                   |      |                   | circuit data      |
   |                   |      |                   | exchange          |
   |                   |      |                   | according to IEC  |
   |                   |      |                   | 60909.            |
   +-------------------+------+-------------------+-------------------+
   | maxQ              | 1..1 | `ReactivePower <# | Maximum reactive  |
   |                   |      | ReactivePower>`__ | power limit. This |
   |                   |      |                   | is the maximum    |
   |                   |      |                   | (nameplate) limit |
   |                   |      |                   | for the unit.     |
   +-------------------+------+-------------------+-------------------+
   | minQ              | 1..1 | `ReactivePower <# | Minimum reactive  |
   |                   |      | ReactivePower>`__ | power limit for   |
   |                   |      |                   | the unit.         |
   +-------------------+------+-------------------+-------------------+
   | operatingMode     | 1..1 | `S                | Current mode of   |
   |                   |      | ynchronousMachine | operation.        |
   |                   |      | OperatingMode <#S |                   |
   |                   |      | ynchronousMachine |                   |
   |                   |      | OperatingMode>`__ |                   |
   +-------------------+------+-------------------+-------------------+
   | type              | 1..1 | `                 | Modes that this   |
   |                   |      | SynchronousMachin | synchronous       |
   |                   |      | eKind <#Synchrono | machine can       |
   |                   |      | usMachineKind>`__ | operate in.       |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-56

   +----------------+------+-------------------+-------------------+
   | p              | 1..1 | `ActivePower      | see               |
   |                |      | <#ActivePower>`__ | `Rotat            |
   |                |      |                   | ingMachine <#Rota |
   |                |      |                   | tingMachine.p>`__ |
   +----------------+------+-------------------+-------------------+
   | q              | 1..1 | `ReactivePower <# | see               |
   |                |      | ReactivePower>`__ | `Rotat            |
   |                |      |                   | ingMachine <#Rota |
   |                |      |                   | tingMachine.q>`__ |
   +----------------+------+-------------------+-------------------+
   | ratedS         | 1..1 | `ApparentPower <# | see               |
   |                |      | ApparentPower>`__ | `RotatingMa       |
   |                |      |                   | chine <#RotatingM |
   |                |      |                   | achine.ratedS>`__ |
   +----------------+------+-------------------+-------------------+
   | ratedU         | 1..1 | `Volt             | see               |
   |                |      | age <#Voltage>`__ | `RotatingMa       |
   |                |      |                   | chine <#RotatingM |
   |                |      |                   | achine.ratedU>`__ |
   +----------------+------+-------------------+-------------------+
   | GeneratingUnit | 1..1 | `G                | see               |
   |                |      | eneratingUnit <#G | `R                |
   |                |      | eneratingUnit>`__ | otatingMachine <# |
   |                |      |                   | RotatingMachine.G |
   |                |      |                   | eneratingUnit>`__ |
   +----------------+------+-------------------+-------------------+

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: SynchronousMachineSimplified

   ` <#SynchronousMachineSimplified>`__

   .. rubric:: SynchronousMachineSimplified
      :name: synchronousmachinesimplified
      :class: concrete

   SynchronousMachineDynamics

   The simplified model represents a synchronous generator as a constant
   internal voltage behind an impedance (*Rs + jXp*) as shown in the
   Simplified diagram.

   Since internal voltage is held constant, there is no *Efd* input and
   any excitation system model will be ignored. There is also no *Ifd*
   output.

   This model should not be used for representing a real generator
   except, perhaps, small generators whose response is insignificant.

   The parameters used for the simplified model include:

   - RotatingMachineDynamics.damping (*D*);

   - RotatingMachineDynamics.inertia (*H*);

   - RotatingMachineDynamics.statorLeakageReactance (used to exchange
   *jXp* for SynchronousMachineSimplified);

   - RotatingMachineDynamics.statorResistance (*Rs*).

   .. rubric:: Inherited Members
      :name: inherited-members-57

   +-------------------+------+-------------------+-------------------+
   | S                 | 0..1 | `Synchrono        | see               |
   | ynchronousMachine |      | usMachine <#Synch | `Synchronou       |
   |                   |      | ronousMachine>`__ | sMachineDynamics  |
   |                   |      |                   | <#SynchronousMach |
   |                   |      |                   | ineDynamics.Synch |
   |                   |      |                   | ronousMachine>`__ |
   +-------------------+------+-------------------+-------------------+

   +-------------------+------+-------------------+-------------------+
   | damping           | 1..1 | `                 | see               |
   |                   |      | Float <#Float>`__ | `RotatingMa       |
   |                   |      |                   | chineDynamics <#R |
   |                   |      |                   | otatingMachineDyn |
   |                   |      |                   | amics.damping>`__ |
   +-------------------+------+-------------------+-------------------+
   | inertia           | 1..1 | `Seco             | see               |
   |                   |      | nds <#Seconds>`__ | `RotatingMa       |
   |                   |      |                   | chineDynamics <#R |
   |                   |      |                   | otatingMachineDyn |
   |                   |      |                   | amics.inertia>`__ |
   +-------------------+------+-------------------+-------------------+
   | stato             | 1..1 | `PU <#PU>`__      | see               |
   | rLeakageReactance |      |                   | `Rotating         |
   |                   |      |                   | MachineDynamics < |
   |                   |      |                   | #RotatingMachineD |
   |                   |      |                   | ynamics.statorLea |
   |                   |      |                   | kageReactance>`__ |
   +-------------------+------+-------------------+-------------------+
   | statorResistance  | 1..1 | `PU <#PU>`__      | see               |
   |                   |      |                   | `Ro               |
   |                   |      |                   | tatingMachineDyna |
   |                   |      |                   | mics <#RotatingMa |
   |                   |      |                   | chineDynamics.sta |
   |                   |      |                   | torResistance>`__ |
   +-------------------+------+-------------------+-------------------+

   +---------+------+------------------------+------------------------+
   | mRID    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.mRID>`__ |
   +---------+------+------------------------+------------------------+
   | enabled | 1..1 | `Boolean <#Boolean>`__ | see                    |
   |         |      |                        | `DynamicsFunct         |
   |         |      |                        | ionBlock <#DynamicsFun |
   |         |      |                        | ctionBlock.enabled>`__ |
   +---------+------+------------------------+------------------------+
   | name    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.name>`__ |
   +---------+------+------------------------+------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: SynchronousMachineTimeConstantReactance

   ` <#SynchronousMachineTimeConstantReactance>`__

   .. rubric:: SynchronousMachineTimeConstantReactance
      :name: synchronousmachinetimeconstantreactance
      :class: concrete

   SynchronousMachineDynamics

   Synchronous machine detailed modelling types are defined by the
   combination of the attributes
   SynchronousMachineTimeConstantReactance.modelType and
   SynchronousMachineTimeConstantReactance.rotorType.

   Parameter details:

   1. The “p” in the time-related attribute names is a substitution for
      a “prime” in the usual parameter notation, e.g. tpdo refers to
      *T'do*.

   .. rubric:: Native Members
      :name: native-members-55

   +----------------+----------------+----------------+----------------+
   | ks             | 1..1           | `Flo           | Saturation     |
   |                |                | at <#Float>`__ | loading        |
   |                |                |                | correction     |
   |                |                |                | factor (*Ks*)  |
   |                |                |                | (>= 0). Used   |
   |                |                |                | only by type J |
   |                |                |                | model. Typical |
   |                |                |                | value = 0.     |
   +----------------+----------------+----------------+----------------+
   | modelType      | 1..1           | [SynchronousMa | Type of        |
   |                |                | c              | synchronous    |
   |                |                | hineModelKind] | machine model  |
   |                |                | (              | used in        |
   |                |                | #SynchronousMa | dynamic        |
   |                |                | c              | simulation     |
   |                |                | hineModelKind) | applications.  |
   +----------------+----------------+----------------+----------------+
   | rotorType      | 1..1           | `RotorKi       | Type of rotor  |
   |                |                | nd <           | on physical    |
   |                |                | #RotorKind>`__ | machine.       |
   +----------------+----------------+----------------+----------------+
   | tc             | 1..1           | `Sec           | Damping time   |
   |                |                | onds           | constant for   |
   |                |                |  <#Seconds>`__ | “Canay”        |
   |                |                |                | reactance (>=  |
   |                |                |                | 0). Typical    |
   |                |                |                | value = 0.     |
   +----------------+----------------+----------------+----------------+
   | tpdo           | 1..1           | `Sec           | Direct-axis    |
   |                |                | onds           | transient      |
   |                |                |  <#Seconds>`__ | rotor time     |
   |                |                |                | constant       |
   |                |                |                | (*T'do*) (> Sy |
   |                |                |                | n              |
   |                |                |                | chronousMachin |
   |                |                |                | e              |
   |                |                |                | TimeConstantRe |
   |                |                |                | a              |
   |                |                |                | ctance.tppdo). |
   |                |                |                | Typical value  |
   |                |                |                | = 5.           |
   +----------------+----------------+----------------+----------------+
   | tppdo          | 1..1           | `Sec           | Direct-axis    |
   |                |                | onds           | subtransient   |
   |                |                |  <#Seconds>`__ | rotor time     |
   |                |                |                | constant       |
   |                |                |                | (*T''do*) (>   |
   |                |                |                | 0). Typical    |
   |                |                |                | value = 0,03.  |
   +----------------+----------------+----------------+----------------+
   | tppqo          | 1..1           | `Sec           | Q              |
   |                |                | onds           | uadrature-axis |
   |                |                |  <#Seconds>`__ | subtransient   |
   |                |                |                | rotor time     |
   |                |                |                | constant       |
   |                |                |                | (*T''qo*) (>   |
   |                |                |                | 0). Typical    |
   |                |                |                | value = 0,03.  |
   +----------------+----------------+----------------+----------------+
   | tpqo           | 1..1           | `Sec           | Q              |
   |                |                | onds           | uadrature-axis |
   |                |                |  <#Seconds>`__ | transient      |
   |                |                |                | rotor time     |
   |                |                |                | constant       |
   |                |                |                | (*T'qo*) (> Sy |
   |                |                |                | n              |
   |                |                |                | chronousMachin |
   |                |                |                | e              |
   |                |                |                | TimeConstantRe |
   |                |                |                | a              |
   |                |                |                | ctance.tppqo). |
   |                |                |                | Typical value  |
   |                |                |                | = 0,5.         |
   +----------------+----------------+----------------+----------------+
   | x              | 1..1           | `PU <#PU>`__   | Direct-axis    |
   | DirectSubtrans |                |                | subtransient   |
   |                |                |                | reactance      |
   |                |                |                | (unsaturated)  |
   |                |                |                | (*X''d*) (>    |
   |                |                |                | Rot            |
   |                |                |                | a              |
   |                |                |                | tingMachineDyn |
   |                |                |                | a              |
   |                |                |                | mics.statorLea |
   |                |                |                | k              |
   |                |                |                | ageReactance). |
   |                |                |                | Typical value  |
   |                |                |                | = 0,2.         |
   +----------------+----------------+----------------+----------------+
   | xDirectSync    | 1..1           | `PU <#PU>`__   | Direct-axis    |
   |                |                |                | synchronous    |
   |                |                |                | reactance      |
   |                |                |                | (*Xd*) (>=     |
   |                |                |                | Synchrono      |
   |                |                |                | u              |
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
   | xDirectTrans   | 1..1           | `PU <#PU>`__   | Direct-axis    |
   |                |                |                | transient      |
   |                |                |                | reactance      |
   |                |                |                | (unsaturated)  |
   |                |                |                | (*X'd*) (>=    |
   |                |                |                | SynchronousM   |
   |                |                |                | a              |
   |                |                |                | chineTimeConst |
   |                |                |                | a              |
   |                |                |                | ntReactance.xD |
   |                |                |                | i              |
   |                |                |                | rectSubtrans). |
   |                |                |                | Typical value  |
   |                |                |                | = 0,5.         |
   +----------------+----------------+----------------+----------------+
   | xQuadSubtrans  | 1..1           | `PU <#PU>`__   | Q              |
   |                |                |                | uadrature-axis |
   |                |                |                | subtransient   |
   |                |                |                | reactance      |
   |                |                |                | (*X''q*) (>    |
   |                |                |                | Rot            |
   |                |                |                | a              |
   |                |                |                | tingMachineDyn |
   |                |                |                | a              |
   |                |                |                | mics.statorLea |
   |                |                |                | k              |
   |                |                |                | ageReactance). |
   |                |                |                | Typical value  |
   |                |                |                | = 0,2.         |
   +----------------+----------------+----------------+----------------+
   | xQuadSync      | 1..1           | `PU <#PU>`__   | Q              |
   |                |                |                | uadrature-axis |
   |                |                |                | synchronous    |
   |                |                |                | reactance      |
   |                |                |                | (*Xq*) (>=     |
   |                |                |                | Synchro        |
   |                |                |                | n              |
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
   |                |                |                | to the         |
   |                |                |                | q              |
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
   | xQuadTrans     | 1..1           | `PU <#PU>`__   | Q              |
   |                |                |                | uadrature-axis |
   |                |                |                | transient      |
   |                |                |                | reactance      |
   |                |                |                | (*X'q*) (>=    |
   |                |                |                | Synchronou     |
   |                |                |                | s              |
   |                |                |                | MachineTimeCon |
   |                |                |                | s              |
   |                |                |                | tantReactance. |
   |                |                |                | x              |
   |                |                |                | QuadSubtrans). |
   |                |                |                | Typical value  |
   |                |                |                | = 0,3.         |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-58

   +-------------------+------+-------------------+-------------------+
   | efdBaseRatio      | 1..1 | `                 | see               |
   |                   |      | Float <#Float>`__ | `Sync             |
   |                   |      |                   | hronousMachineDet |
   |                   |      |                   | ailed <#Synchrono |
   |                   |      |                   | usMachineDetailed |
   |                   |      |                   | .efdBaseRatio>`__ |
   +-------------------+------+-------------------+-------------------+
   | ifdBaseType       | 1..1 | `IfdBaseKind      | see               |
   |                   |      | <#IfdBaseKind>`__ | `Syn              |
   |                   |      |                   | chronousMachineDe |
   |                   |      |                   | tailed <#Synchron |
   |                   |      |                   | ousMachineDetaile |
   |                   |      |                   | d.ifdBaseType>`__ |
   +-------------------+------+-------------------+-------------------+
   | saturationFactor  | 1..1 | `                 | see               |
   |                   |      | Float <#Float>`__ | `Synchron         |
   |                   |      |                   | ousMachineDetaile |
   |                   |      |                   | d <#SynchronousMa |
   |                   |      |                   | chineDetailed.sat |
   |                   |      |                   | urationFactor>`__ |
   +-------------------+------+-------------------+-------------------+
   | sa                | 1..1 | `                 | see               |
   | turationFactor120 |      | Float <#Float>`__ | `Synchronous      |
   |                   |      |                   | MachineDetailed < |
   |                   |      |                   | #SynchronousMachi |
   |                   |      |                   | neDetailed.satura |
   |                   |      |                   | tionFactor120>`__ |
   +-------------------+------+-------------------+-------------------+
   | saturat           | 1..1 | `                 | see               |
   | ionFactor120QAxis |      | Float <#Float>`__ | `SynchronousMachi |
   |                   |      |                   | neDetailed <#Sync |
   |                   |      |                   | hronousMachineDet |
   |                   |      |                   | ailed.saturationF |
   |                   |      |                   | actor120QAxis>`__ |
   +-------------------+------+-------------------+-------------------+
   | satu              | 1..1 | `                 | see               |
   | rationFactorQAxis |      | Float <#Float>`__ | `SynchronousMa    |
   |                   |      |                   | chineDetailed <#S |
   |                   |      |                   | ynchronousMachine |
   |                   |      |                   | Detailed.saturati |
   |                   |      |                   | onFactorQAxis>`__ |
   +-------------------+------+-------------------+-------------------+

   +-------------------+------+-------------------+-------------------+
   | S                 | 0..1 | `Synchrono        | see               |
   | ynchronousMachine |      | usMachine <#Synch | `Synchronou       |
   |                   |      | ronousMachine>`__ | sMachineDynamics  |
   |                   |      |                   | <#SynchronousMach |
   |                   |      |                   | ineDynamics.Synch |
   |                   |      |                   | ronousMachine>`__ |
   +-------------------+------+-------------------+-------------------+

   +-------------------+------+-------------------+-------------------+
   | damping           | 1..1 | `                 | see               |
   |                   |      | Float <#Float>`__ | `RotatingMa       |
   |                   |      |                   | chineDynamics <#R |
   |                   |      |                   | otatingMachineDyn |
   |                   |      |                   | amics.damping>`__ |
   +-------------------+------+-------------------+-------------------+
   | inertia           | 1..1 | `Seco             | see               |
   |                   |      | nds <#Seconds>`__ | `RotatingMa       |
   |                   |      |                   | chineDynamics <#R |
   |                   |      |                   | otatingMachineDyn |
   |                   |      |                   | amics.inertia>`__ |
   +-------------------+------+-------------------+-------------------+
   | stato             | 1..1 | `PU <#PU>`__      | see               |
   | rLeakageReactance |      |                   | `Rotating         |
   |                   |      |                   | MachineDynamics < |
   |                   |      |                   | #RotatingMachineD |
   |                   |      |                   | ynamics.statorLea |
   |                   |      |                   | kageReactance>`__ |
   +-------------------+------+-------------------+-------------------+
   | statorResistance  | 1..1 | `PU <#PU>`__      | see               |
   |                   |      |                   | `Ro               |
   |                   |      |                   | tatingMachineDyna |
   |                   |      |                   | mics <#RotatingMa |
   |                   |      |                   | chineDynamics.sta |
   |                   |      |                   | torResistance>`__ |
   +-------------------+------+-------------------+-------------------+

   +---------+------+------------------------+------------------------+
   | mRID    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.mRID>`__ |
   +---------+------+------------------------+------------------------+
   | enabled | 1..1 | `Boolean <#Boolean>`__ | see                    |
   |         |      |                        | `DynamicsFunct         |
   |         |      |                        | ionBlock <#DynamicsFun |
   |         |      |                        | ctionBlock.enabled>`__ |
   +---------+------+------------------------+------------------------+
   | name    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.name>`__ |
   +---------+------+------------------------+------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: Terminal

   ` <#Terminal>`__

   .. rubric:: Terminal
      :name: terminal
      :class: concrete

   Core

   An AC electrical connection point to a piece of conducting equipment.
   Terminals are connected at physical connection points called
   connectivity nodes.

   .. rubric:: Native Members
      :name: native-members-56

   +-------------------+------+-------------------+-------------------+
   | Co                | 1..1 | `ConductingE      | The conducting    |
   | nductingEquipment |      | quipment <#Conduc | equipment of the  |
   |                   |      | tingEquipment>`__ | terminal.         |
   |                   |      |                   | Conducting        |
   |                   |      |                   | equipment have    |
   |                   |      |                   | terminals that    |
   |                   |      |                   | may be connected  |
   |                   |      |                   | to other          |
   |                   |      |                   | conducting        |
   |                   |      |                   | equipment         |
   |                   |      |                   | terminals via     |
   |                   |      |                   | connectivity      |
   |                   |      |                   | nodes or          |
   |                   |      |                   | topological       |
   |                   |      |                   | nodes.            |
   +-------------------+------+-------------------+-------------------+
   | ConnectivityNode  | 1..1 | `Conne            | The connectivity  |
   |                   |      | ctivityNode <#Con | node to which     |
   |                   |      | nectivityNode>`__ | this terminal     |
   |                   |      |                   | connects with     |
   |                   |      |                   | zero impedance.   |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-59

   +----------------+------+-------------------+-------------------+
   | sequenceNumber | 1..1 | `Inte             | see               |
   |                |      | ger <#Integer>`__ | `ACDCTerminal     |
   |                |      |                   |  <#ACDCTerminal.s |
   |                |      |                   | equenceNumber>`__ |
   +----------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: TextDiagramObject

   ` <#TextDiagramObject>`__

   .. rubric:: TextDiagramObject
      :name: textdiagramobject
      :class: concrete

   DiagramLayout

   A diagram object for placing free-text or text derived from an
   associated domain object.

   .. rubric:: Native Members
      :name: native-members-57

   +------+------+----------------------+--------------------------+
   | text | 1..1 | `String <#String>`__ | The text that is         |
   |      |      |                      | displayed by this text   |
   |      |      |                      | diagram object.          |
   +------+------+----------------------+--------------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-60

   +------------------+------+-------------------+-------------------+
   | mRID             | 1..1 | `St               | see               |
   |                  |      | ring <#String>`__ | `Diag             |
   |                  |      |                   | ramObject <#Diagr |
   |                  |      |                   | amObject.mRID>`__ |
   +------------------+------+-------------------+-------------------+
   | drawingOrder     | 1..1 | `Inte             | see               |
   |                  |      | ger <#Integer>`__ | `DiagramObjec     |
   |                  |      |                   | t <#DiagramObject |
   |                  |      |                   | .drawingOrder>`__ |
   +------------------+------+-------------------+-------------------+
   | isPolygon        | 1..1 | `Bool             | see               |
   |                  |      | ean <#Boolean>`__ | `DiagramOb        |
   |                  |      |                   | ject <#DiagramObj |
   |                  |      |                   | ect.isPolygon>`__ |
   +------------------+------+-------------------+-------------------+
   | name             | 1..1 | `St               | see               |
   |                  |      | ring <#String>`__ | `Diag             |
   |                  |      |                   | ramObject <#Diagr |
   |                  |      |                   | amObject.name>`__ |
   +------------------+------+-------------------+-------------------+
   | IdentifiedObject | 1..1 | `Ident            | see               |
   |                  |      | ifiedObject <#Ide | `DiagramObject <# |
   |                  |      | ntifiedObject>`__ | DiagramObject.Ide |
   |                  |      |                   | ntifiedObject>`__ |
   +------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: ThermalGeneratingUnit

   ` <#ThermalGeneratingUnit>`__

   .. rubric:: ThermalGeneratingUnit
      :name: thermalgeneratingunit
      :class: concrete

   Production

   A generating unit whose prime mover could be a steam turbine,
   combustion turbine, or diesel engine.

   .. rubric:: Inherited Members
      :name: inherited-members-61

   +---------------+------+---------------------+---------------------+
   | maxOperatingP | 1..1 | `ActivePowe         | see                 |
   |               |      | r <#ActivePower>`__ | `GeneratingU        |
   |               |      |                     | nit <#GeneratingUni |
   |               |      |                     | t.maxOperatingP>`__ |
   +---------------+------+---------------------+---------------------+
   | minOperatingP | 1..1 | `ActivePowe         | see                 |
   |               |      | r <#ActivePower>`__ | `GeneratingU        |
   |               |      |                     | nit <#GeneratingUni |
   |               |      |                     | t.minOperatingP>`__ |
   +---------------+------+---------------------+---------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: TopologicalNode

   ` <#TopologicalNode>`__

   .. rubric:: TopologicalNode
      :name: topologicalnode
      :class: concrete

   Topology

   For a detailed substation model a topological node is a set of
   connectivity nodes that, in the current network state, are connected
   together through any type of closed switches, including jumpers.
   Topological nodes change as the current network state changes (i.e.,
   switches, breakers, etc. change state).

   For a planning model, switch statuses are not used to form
   topological nodes. Instead they are manually created or deleted in a
   model builder tool. Topological nodes maintained this way are also
   called "busses".

   .. rubric:: Inherited Members
      :name: inherited-members-62

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: TransformerCoreAdmittance

   ` <#TransformerCoreAdmittance>`__

   .. rubric:: TransformerCoreAdmittance
      :name: transformercoreadmittance
      :class: concrete

   Wires

   The transformer core admittance. Used to specify the core admittance
   of a transformer in a manner that can be shared among power
   transformers.

   .. rubric:: Native Members
      :name: native-members-58

   +----------------+----------------+----------------+----------------+
   | mRID           | 1..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | b              | 1..1           | `S             | Magnetizing    |
   |                |                | usceptance <#S | branch         |
   |                |                | usceptance>`__ | susceptance (B |
   |                |                |                | mag). The      |
   |                |                |                | value can be   |
   |                |                |                | positive or    |
   |                |                |                | negative.      |
   +----------------+----------------+----------------+----------------+
   | b0             | 1..1           | `S             | Zero sequence  |
   |                |                | usceptance <#S | magnetizing    |
   |                |                | usceptance>`__ | branch         |
   |                |                |                | susceptance.   |
   +----------------+----------------+----------------+----------------+
   | g              | 1..1           | `C             | Magnetizing    |
   |                |                | onductance <#C | branch         |
   |                |                | onductance>`__ | conductance (G |
   |                |                |                | mag).          |
   +----------------+----------------+----------------+----------------+
   | g0             | 1..1           | `C             | Zero sequence  |
   |                |                | onductance <#C | magnetizing    |
   |                |                | onductance>`__ | branch         |
   |                |                |                | conductance.   |
   +----------------+----------------+----------------+----------------+
   | name           | 1..1           | `S             | The name is    |
   |                |                | trin           | any free human |
   |                |                | g <#String>`__ | readable and   |
   |                |                |                | possibly non   |
   |                |                |                | unique text    |
   |                |                |                | naming the     |
   |                |                |                | object.        |
   +----------------+----------------+----------------+----------------+
   | TransformerEnd | 1..1           | `Tr            | All            |
   |                |                | ansforme       | transformer    |
   |                |                | rEnd <#%20Tran | ends having    |
   |                |                | sformerEnd>`__ | this core      |
   |                |                |                | admittance.    |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-63

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: TransformerMeshImpedance

   ` <#TransformerMeshImpedance>`__

   .. rubric:: TransformerMeshImpedance
      :name: transformermeshimpedance
      :class: concrete

   Wires

   Transformer mesh impedance (Delta-model) between transformer ends.

   The typical case is that this class describes the impedance between
   two transformer ends pair-wise, i.e. the cardinalities at both
   transformer end associations are 1. However, in cases where two or
   more transformer ends are modelled the cardinalities are larger than
   1.

   .. rubric:: Native Members
      :name: native-members-59

   +----------------+----------------+----------------+----------------+
   | mRID           | 1..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | name           | 1..1           | `S             | The name is    |
   |                |                | trin           | any free human |
   |                |                | g <#String>`__ | readable and   |
   |                |                |                | possibly non   |
   |                |                |                | unique text    |
   |                |                |                | naming the     |
   |                |                |                | object.        |
   +----------------+----------------+----------------+----------------+
   | r              | 1..1           | `Resistanc     | Resistance     |
   |                |                | e <#           | between the    |
   |                |                | Resistance>`__ | 'from' and the |
   |                |                |                | 'to' end, seen |
   |                |                |                | from the       |
   |                |                |                | 'from' end.    |
   +----------------+----------------+----------------+----------------+
   | r0             | 1..1           | `Resistanc     | Zero-sequence  |
   |                |                | e <#           | resistance     |
   |                |                | Resistance>`__ | between the    |
   |                |                |                | 'from' and the |
   |                |                |                | 'to' end, seen |
   |                |                |                | from the       |
   |                |                |                | 'from' end.    |
   +----------------+----------------+----------------+----------------+
   | x              | 1..1           | `Reactan       | Reactance      |
   |                |                | ce <           | between the    |
   |                |                | #Reactance>`__ | 'from' and the |
   |                |                |                | 'to' end, seen |
   |                |                |                | from the       |
   |                |                |                | 'from' end.    |
   +----------------+----------------+----------------+----------------+
   | x0             | 1..1           | `Reactan       | Zero-sequence  |
   |                |                | ce <           | reactance      |
   |                |                | #Reactance>`__ | between the    |
   |                |                |                | 'from' and the |
   |                |                |                | 'to' end, seen |
   |                |                |                | from the       |
   |                |                |                | 'from' end.    |
   +----------------+----------------+----------------+----------------+
   | Fro            | 1..1           | `Tr            | From end this  |
   | m              |                | ansforme       | mesh impedance |
   | TransformerEnd |                | rEnd <#%20Tran | is connected   |
   |                |                | sformerEnd>`__ | to. It         |
   |                |                |                | determines the |
   |                |                |                | voltage        |
   |                |                |                | reference.     |
   +----------------+----------------+----------------+----------------+
   | T              | 1..\*          | `Tr            | All            |
   | o              |                | ansforme       | transformer    |
   | TransformerEnd |                | rEnd <#%20Tran | ends this mesh |
   |                |                | sformerEnd>`__ | impedance is   |
   |                |                |                | connected to.  |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-64

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: TransformerSaturationCurve

   ` <#TransformerSaturationCurve>`__

   .. rubric:: TransformerSaturationCurve
      :name: transformersaturationcurve
      :class: concrete

   Emtiop

   Represents a piecewise linear transformer saturation characteristic.
   It's connected to the same TransformerEnd as the
   TransformerCoreAdmittance, which is typically the lowest voltage
   winding other than a tertiary. The attached Curve is a piecewise
   linear magnetization characteristic, plotted as core flux linkage vs.
   magnetizing current. This replaces the linear magnetizing
   characteristic defined by TransformerCoreAdmittance.b and
   TransformerCoreAdmittance.b0. The TransformerSaturation
   characteristic does not include hysteresis, i.e., the origin point
   [0,0] is implied. The TransformerCoreAdmittance.g and
   TransformerCoreAdmittance.g0 should still be used to model core
   losses.

   This data is of most interest to electromagnetic transient analysis,
   which typically uses SI units without multipliers.

   xMultiplier inherited attribute should be UnitMultiplier.none

   xUnit inherited attribute should be UnitSymbol.A

   y1Multiplier inherited attribute should be UnitMultiplier.none

   y1Unit inherited attribute should be UnitSymbol.Vs

   xvalue in associated CurveData should be magnetizing current in peak
   A (not RMS), referenced to the TransformerEnd associated through
   TransformerCoreAdmittance. Do not enter the origin point [0,0].

   y1value in associated CurveData should be core flux linkage in peak
   Vs (not RMS), referenced to the TransformerEnd associated through
   TransformerCoreAdmittance. Do not enter the origin point [0,0].

   .. rubric:: Native Members
      :name: native-members-60

   +---------------------------+------+---------------------------+---+
   | TransformerCoreAdmittance | 0..1 | `Transfo                  |   |
   |                           |      | rmerCoreAdmittance <#Tran |   |
   |                           |      | sformerCoreAdmittance>`__ |   |
   +---------------------------+------+---------------------------+---+

   .. rubric:: Inherited Members
      :name: inherited-members-65

   +--------------+------+----------------------+----------------------+
   | mRID         | 1..1 | `String <#String>`__ | see                  |
   |              |      |                      | `Cu                  |
   |              |      |                      | rve <#Curve.mRID>`__ |
   +--------------+------+----------------------+----------------------+
   | curveStyle   | 0..1 | `CurveSt             | see                  |
   |              |      | yle <#CurveStyle>`__ | `Curve <#            |
   |              |      |                      | Curve.curveStyle>`__ |
   +--------------+------+----------------------+----------------------+
   | name         | 1..1 | `String <#String>`__ | see                  |
   |              |      |                      | `Cu                  |
   |              |      |                      | rve <#Curve.name>`__ |
   +--------------+------+----------------------+----------------------+
   | xMultiplier  | 0..1 | `UnitMultiplier      | see                  |
   |              |      | <#UnitMultiplier>`__ | `Curve <#C           |
   |              |      |                      | urve.xMultiplier>`__ |
   +--------------+------+----------------------+----------------------+
   | xUnit        | 0..1 | `UnitSym             | see                  |
   |              |      | bol <#UnitSymbol>`__ | `Cur                 |
   |              |      |                      | ve <#Curve.xUnit>`__ |
   +--------------+------+----------------------+----------------------+
   | y1Multiplier | 0..1 | `UnitMultiplier      | see                  |
   |              |      | <#UnitMultiplier>`__ | `Curve <#Cu          |
   |              |      |                      | rve.y1Multiplier>`__ |
   +--------------+------+----------------------+----------------------+
   | y1Unit       | 0..1 | `UnitSym             | see                  |
   |              |      | bol <#UnitSymbol>`__ | `Curv                |
   |              |      |                      | e <#Curve.y1Unit>`__ |
   +--------------+------+----------------------+----------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: VsConverter

   ` <#VsConverter>`__

   .. rubric:: VsConverter
      :name: vsconverter
      :class: concrete

   DC

   DC side of the voltage source converter (VSC).

   .. rubric:: Native Members
      :name: native-members-61

   +-------------------+------+-------------------+-------------------+
   | delta             | 0..1 | `AngleDegrees <   | Angle between     |
   |                   |      | #AngleDegrees>`__ | VsConverter.uv    |
   |                   |      |                   | and               |
   |                   |      |                   | ACDCConverter.uc. |
   |                   |      |                   | It is converter's |
   |                   |      |                   | state variable    |
   |                   |      |                   | used in power     |
   |                   |      |                   | flow. The         |
   |                   |      |                   | attribute shall   |
   |                   |      |                   | be a positive     |
   |                   |      |                   | value or zero.    |
   +-------------------+------+-------------------+-------------------+
   | droop             | 0..1 | `PU <#PU>`__      | Droop constant.   |
   |                   |      |                   | The pu value is   |
   |                   |      |                   | obtained as D     |
   |                   |      |                   | [kV/MW] \* Sb /   |
   |                   |      |                   | Ubdc. The         |
   |                   |      |                   | attribute shall   |
   |                   |      |                   | be a positive     |
   |                   |      |                   | value.            |
   +-------------------+------+-------------------+-------------------+
   | droopCompensation | 0..1 | `Resistance       | Compensation      |
   |                   |      |  <#Resistance>`__ | constant. Used to |
   |                   |      |                   | compensate for    |
   |                   |      |                   | voltage drop when |
   |                   |      |                   | controlling       |
   |                   |      |                   | voltage at a      |
   |                   |      |                   | distant bus. The  |
   |                   |      |                   | attribute shall   |
   |                   |      |                   | be a positive     |
   |                   |      |                   | value.            |
   +-------------------+------+-------------------+-------------------+
   | m                 | 0..1 | `                 | The maximum       |
   | axModulationIndex |      | Float <#Float>`__ | quotient between  |
   |                   |      |                   | the AC converter  |
   |                   |      |                   | voltage (Uc) and  |
   |                   |      |                   | DC voltage (Ud).  |
   |                   |      |                   | A factor          |
   |                   |      |                   | typically less    |
   |                   |      |                   | than 1. It is     |
   |                   |      |                   | converter's       |
   |                   |      |                   | configuration     |
   |                   |      |                   | data used in      |
   |                   |      |                   | power flow.       |
   +-------------------+------+-------------------+-------------------+
   | maxValveCurrent   | 0..1 | `CurrentFlow      | The maximum       |
   |                   |      | <#CurrentFlow>`__ | current through a |
   |                   |      |                   | valve. It is      |
   |                   |      |                   | converter's       |
   |                   |      |                   | configuration     |
   |                   |      |                   | data.             |
   +-------------------+------+-------------------+-------------------+
   | pPccControl       | 0..1 | `VsPpccC          | Kind of control   |
   |                   |      | ontrolKind <#VsPp | of real power     |
   |                   |      | ccControlKind>`__ | and/or DC         |
   |                   |      |                   | voltage.          |
   +-------------------+------+-------------------+-------------------+
   | qPccControl       | 0..1 | `VsQpccC          | Kind of reactive  |
   |                   |      | ontrolKind <#VsQp | power control.    |
   |                   |      | ccControlKind>`__ |                   |
   +-------------------+------+-------------------+-------------------+
   | qShare            | 0..1 | `PerC             | Reactive power    |
   |                   |      | ent <#PerCent>`__ | sharing factor    |
   |                   |      |                   | among parallel    |
   |                   |      |                   | converters on Uac |
   |                   |      |                   | control. The      |
   |                   |      |                   | attribute shall   |
   |                   |      |                   | be a positive     |
   |                   |      |                   | value or zero.    |
   +-------------------+------+-------------------+-------------------+
   | targetPhasePcc    | 0..1 | `AngleDegrees <   | Phase target at   |
   |                   |      | #AngleDegrees>`__ | AC side, at point |
   |                   |      |                   | of common         |
   |                   |      |                   | coupling. The     |
   |                   |      |                   | attribute shall   |
   |                   |      |                   | be a positive     |
   |                   |      |                   | value.            |
   +-------------------+------+-------------------+-------------------+
   | tar               | 0..1 | `                 | Power factor      |
   | getPowerFactorPcc |      | Float <#Float>`__ | target at the AC  |
   |                   |      |                   | side, at point of |
   |                   |      |                   | common coupling.  |
   |                   |      |                   | The attribute     |
   |                   |      |                   | shall be a        |
   |                   |      |                   | positive value.   |
   +-------------------+------+-------------------+-------------------+
   | targetPWMfactor   | 0..1 | `                 | Magnitude of      |
   |                   |      | Float <#Float>`__ | pulse-modulation  |
   |                   |      |                   | factor. The       |
   |                   |      |                   | attribute shall   |
   |                   |      |                   | be a positive     |
   |                   |      |                   | value.            |
   +-------------------+------+-------------------+-------------------+
   | targetQpcc        | 0..1 | `ReactivePower <# | Reactive power    |
   |                   |      | ReactivePower>`__ | injection target  |
   |                   |      |                   | in AC grid, at    |
   |                   |      |                   | point of common   |
   |                   |      |                   | coupling. Load    |
   |                   |      |                   | sign convention   |
   |                   |      |                   | is used,          |
   |                   |      |                   | i.e. positive     |
   |                   |      |                   | sign means flow   |
   |                   |      |                   | out from a node.  |
   +-------------------+------+-------------------+-------------------+
   | targetUpcc        | 0..1 | `Volt             | Voltage target in |
   |                   |      | age <#Voltage>`__ | AC grid, at point |
   |                   |      |                   | of common         |
   |                   |      |                   | coupling. The     |
   |                   |      |                   | attribute shall   |
   |                   |      |                   | be a positive     |
   |                   |      |                   | value.            |
   +-------------------+------+-------------------+-------------------+
   | uv                | 0..1 | `Volt             | Line-to-line      |
   |                   |      | age <#Voltage>`__ | voltage on the    |
   |                   |      |                   | valve side of the |
   |                   |      |                   | converter         |
   |                   |      |                   | transformer. It   |
   |                   |      |                   | is converter's    |
   |                   |      |                   | state variable,   |
   |                   |      |                   | result from power |
   |                   |      |                   | flow. The         |
   |                   |      |                   | attribute shall   |
   |                   |      |                   | be a positive     |
   |                   |      |                   | value.            |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-66

   +----------------+------+-------------------+-------------------+
   | baseS          | 0..1 | `ApparentPower <# | see               |
   |                |      | ApparentPower>`__ | `ACDCC            |
   |                |      |                   | onverter <#ACDCCo |
   |                |      |                   | nverter.baseS>`__ |
   +----------------+------+-------------------+-------------------+
   | idc            | 0..1 | `CurrentFlow      | see               |
   |                |      | <#CurrentFlow>`__ | `ACD              |
   |                |      |                   | CConverter <#ACDC |
   |                |      |                   | Converter.idc>`__ |
   +----------------+------+-------------------+-------------------+
   | idleLoss       | 0..1 | `ActivePower      | see               |
   |                |      | <#ActivePower>`__ | `ACDCConv         |
   |                |      |                   | erter <#ACDCConve |
   |                |      |                   | rter.idleLoss>`__ |
   +----------------+------+-------------------+-------------------+
   | maxP           | 0..1 | `ActivePower      | see               |
   |                |      | <#ActivePower>`__ | `ACDC             |
   |                |      |                   | Converter <#ACDCC |
   |                |      |                   | onverter.maxP>`__ |
   +----------------+------+-------------------+-------------------+
   | maxUdc         | 0..1 | `Volt             | see               |
   |                |      | age <#Voltage>`__ | `ACDCCo           |
   |                |      |                   | nverter <#ACDCCon |
   |                |      |                   | verter.maxUdc>`__ |
   +----------------+------+-------------------+-------------------+
   | minP           | 0..1 | `ActivePower      | see               |
   |                |      | <#ActivePower>`__ | `ACDC             |
   |                |      |                   | Converter <#ACDCC |
   |                |      |                   | onverter.minP>`__ |
   +----------------+------+-------------------+-------------------+
   | minUdc         | 0..1 | `Volt             | see               |
   |                |      | age <#Voltage>`__ | `ACDCCo           |
   |                |      |                   | nverter <#ACDCCon |
   |                |      |                   | verter.minUdc>`__ |
   +----------------+------+-------------------+-------------------+
   | numberOfValves | 0..1 | `Inte             | see               |
   |                |      | ger <#Integer>`__ | `ACDCConverter    |
   |                |      |                   | <#ACDCConverter.n |
   |                |      |                   | umberOfValves>`__ |
   +----------------+------+-------------------+-------------------+
   | p              | 0..1 | `ActivePower      | see               |
   |                |      | <#ActivePower>`__ | `A                |
   |                |      |                   | CDCConverter <#AC |
   |                |      |                   | DCConverter.p>`__ |
   +----------------+------+-------------------+-------------------+
   | poleLossP      | 0..1 | `ActivePower      | see               |
   |                |      | <#ActivePower>`__ | `ACDCConve        |
   |                |      |                   | rter <#ACDCConver |
   |                |      |                   | ter.poleLossP>`__ |
   +----------------+------+-------------------+-------------------+
   | q              | 0..1 | `ReactivePower <# | see               |
   |                |      | ReactivePower>`__ | `A                |
   |                |      |                   | CDCConverter <#AC |
   |                |      |                   | DCConverter.q>`__ |
   +----------------+------+-------------------+-------------------+
   | ratedUdc       | 0..1 | `Volt             | see               |
   |                |      | age <#Voltage>`__ | `ACDCConv         |
   |                |      |                   | erter <#ACDCConve |
   |                |      |                   | rter.ratedUdc>`__ |
   +----------------+------+-------------------+-------------------+
   | resistiveLoss  | 0..1 | `Resistance       | see               |
   |                |      |  <#Resistance>`__ | `ACDCConverter    |
   |                |      |                   |  <#ACDCConverter. |
   |                |      |                   | resistiveLoss>`__ |
   +----------------+------+-------------------+-------------------+
   | switchingLoss  | 0..1 | `Active           | see               |
   |                |      | PowerPerCurrentFl | `ACDCConverter    |
   |                |      | ow <#ActivePowerP |  <#ACDCConverter. |
   |                |      | erCurrentFlow>`__ | switchingLoss>`__ |
   +----------------+------+-------------------+-------------------+
   | targetPpcc     | 0..1 | `ActivePower      | see               |
   |                |      | <#ActivePower>`__ | `ACDCConver       |
   |                |      |                   | ter <#ACDCConvert |
   |                |      |                   | er.targetPpcc>`__ |
   +----------------+------+-------------------+-------------------+
   | targetUdc      | 0..1 | `Volt             | see               |
   |                |      | age <#Voltage>`__ | `ACDCConve        |
   |                |      |                   | rter <#ACDCConver |
   |                |      |                   | ter.targetUdc>`__ |
   +----------------+------+-------------------+-------------------+
   | uc             | 0..1 | `Volt             | see               |
   |                |      | age <#Voltage>`__ | `AC               |
   |                |      |                   | DCConverter <#ACD |
   |                |      |                   | CConverter.uc>`__ |
   +----------------+------+-------------------+-------------------+
   | udc            | 0..1 | `Volt             | see               |
   |                |      | age <#Voltage>`__ | `ACD              |
   |                |      |                   | CConverter <#ACDC |
   |                |      |                   | Converter.udc>`__ |
   +----------------+------+-------------------+-------------------+
   | valveU0        | 0..1 | `Volt             | see               |
   |                |      | age <#Voltage>`__ | `ACDCCon          |
   |                |      |                   | verter <#ACDCConv |
   |                |      |                   | erter.valveU0>`__ |
   +----------------+------+-------------------+-------------------+

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

Abstract Classes
================

.. container:: group
   :name: ACDCConverter

   ` <#ACDCConverter>`__

   .. rubric:: ACDCConverter
      :name: acdcconverter
      :class: abstract

   DC

   A unit with valves for three phases, together with unit control
   equipment, essential protective and switching devices, DC storage
   capacitors, phase reactors and auxiliaries, if any, used for
   conversion.

   .. rubric:: Native Members
      :name: native-members-62

   +----------------+----------------+----------------+----------------+
   | baseS          | 0..1           | `Appar         | Base apparent  |
   |                |                | entPower <#App | power of the   |
   |                |                | arentPower>`__ | converter      |
   |                |                |                | pole. The      |
   |                |                |                | attribute      |
   |                |                |                | shall be a     |
   |                |                |                | positive       |
   |                |                |                | value.         |
   +----------------+----------------+----------------+----------------+
   | idc            | 0..1           | `C             | Converter DC   |
   |                |                | urrentFlow <#C | current, also  |
   |                |                | urrentFlow>`__ | called Id. It  |
   |                |                |                | is converter's |
   |                |                |                | state          |
   |                |                |                | variable,      |
   |                |                |                | result from    |
   |                |                |                | power flow.    |
   +----------------+----------------+----------------+----------------+
   | idleLoss       | 0..1           | `A             | Active power   |
   |                |                | ctivePower <#A | loss in pole   |
   |                |                | ctivePower>`__ | at no power    |
   |                |                |                | transfer. It   |
   |                |                |                | is the         |
   |                |                |                | converter's    |
   |                |                |                | configuration  |
   |                |                |                | data used in   |
   |                |                |                | power flow.    |
   |                |                |                | The attribute  |
   |                |                |                | shall be a     |
   |                |                |                | positive       |
   |                |                |                | value.         |
   +----------------+----------------+----------------+----------------+
   | maxP           | 0..1           | `A             | Maximum active |
   |                |                | ctivePower <#A | power limit.   |
   |                |                | ctivePower>`__ | The value is   |
   |                |                |                | overwritten by |
   |                |                |                | values of VsC  |
   |                |                |                | a              |
   |                |                |                | pabilityCurve, |
   |                |                |                | if present.    |
   +----------------+----------------+----------------+----------------+
   | maxUdc         | 0..1           | `Vol           | The maximum    |
   |                |                | tage           | voltage on the |
   |                |                |  <#Voltage>`__ | DC side at     |
   |                |                |                | which the      |
   |                |                |                | converter      |
   |                |                |                | should         |
   |                |                |                | operate. It is |
   |                |                |                | the            |
   |                |                |                | converter's    |
   |                |                |                | configuration  |
   |                |                |                | data used in   |
   |                |                |                | power flow.    |
   |                |                |                | The attribute  |
   |                |                |                | shall be a     |
   |                |                |                | positive       |
   |                |                |                | value.         |
   +----------------+----------------+----------------+----------------+
   | minP           | 0..1           | `A             | Minimum active |
   |                |                | ctivePower <#A | power limit.   |
   |                |                | ctivePower>`__ | The value is   |
   |                |                |                | overwritten by |
   |                |                |                | values of VsC  |
   |                |                |                | a              |
   |                |                |                | pabilityCurve, |
   |                |                |                | if present.    |
   +----------------+----------------+----------------+----------------+
   | minUdc         | 0..1           | `Vol           | The minimum    |
   |                |                | tage           | voltage on the |
   |                |                |  <#Voltage>`__ | DC side at     |
   |                |                |                | which the      |
   |                |                |                | converter      |
   |                |                |                | should         |
   |                |                |                | operate. It is |
   |                |                |                | the            |
   |                |                |                | converter's    |
   |                |                |                | configuration  |
   |                |                |                | data used in   |
   |                |                |                | power flow.    |
   |                |                |                | The attribute  |
   |                |                |                | shall be a     |
   |                |                |                | positive       |
   |                |                |                | value.         |
   +----------------+----------------+----------------+----------------+
   | numberOfValves | 0..1           | `Int           | Number of      |
   |                |                | eger           | valves in the  |
   |                |                |  <#Integer>`__ | converter.     |
   |                |                |                | Used in loss   |
   |                |                |                | calculations.  |
   +----------------+----------------+----------------+----------------+
   | p              | 0..1           | `A             | Active power   |
   |                |                | ctivePower <#A | at the point   |
   |                |                | ctivePower>`__ | of common      |
   |                |                |                | coupling. Load |
   |                |                |                | sign           |
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
   | poleLossP      | 0..1           | `A             | The active     |
   |                |                | ctivePower <#A | power loss at  |
   |                |                | ctivePower>`__ | a DC Pole      |
   |                |                |                |                |
   |                |                |                | = idleLoss +   |
   |                |                |                | switching      |
   |                |                |                | Loss*|Idc\| +  |
   |                |                |                | resiti         |
   |                |                |                | veLoss*Idc^2.  |
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
   |                |                |                | converter's    |
   |                |                |                | state variable |
   |                |                |                | used in power  |
   |                |                |                | flow. The      |
   |                |                |                | attribute      |
   |                |                |                | shall be a     |
   |                |                |                | positive       |
   |                |                |                | value.         |
   +----------------+----------------+----------------+----------------+
   | q              | 0..1           | `React         | Reactive power |
   |                |                | ivePower <#Rea | at the point   |
   |                |                | ctivePower>`__ | of common      |
   |                |                |                | coupling. Load |
   |                |                |                | sign           |
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
   | ratedUdc       | 0..1           | `Vol           | Rated          |
   |                |                | tage           | converter DC   |
   |                |                |  <#Voltage>`__ | voltage, also  |
   |                |                |                | called UdN.    |
   |                |                |                | The attribute  |
   |                |                |                | shall be a     |
   |                |                |                | positive       |
   |                |                |                | value. It is   |
   |                |                |                | the            |
   |                |                |                | converter's    |
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
   | resistiveLoss  | 0..1           | `Resistanc     | It is the      |
   |                |                | e <#           | converter's    |
   |                |                | Resistance>`__ | configuration  |
   |                |                |                | data used in   |
   |                |                |                | power flow.    |
   |                |                |                | Refer to       |
   |                |                |                | poleLossP. The |
   |                |                |                | attribute      |
   |                |                |                | shall be a     |
   |                |                |                | positive       |
   |                |                |                | value.         |
   +----------------+----------------+----------------+----------------+
   | switchingLoss  | 0..1           | `ActivePow     | Switching      |
   |                |                | e              | losses,        |
   |                |                | rPerCurrentFlo | relative to    |
   |                |                | w <#Acti       | the base       |
   |                |                | vePower%20PerC | apparent power |
   |                |                | urrentFlow>`__ | 'baseS'. Refer |
   |                |                |                | to poleLossP.  |
   |                |                |                | The attribute  |
   |                |                |                | shall be a     |
   |                |                |                | positive       |
   |                |                |                | value.         |
   +----------------+----------------+----------------+----------------+
   | targetPpcc     | 0..1           | `A             | Real power     |
   |                |                | ctivePower <#A | injection      |
   |                |                | ctivePower>`__ | target in AC   |
   |                |                |                | grid, at point |
   |                |                |                | of common      |
   |                |                |                | coupling. Load |
   |                |                |                | sign           |
   |                |                |                | convention is  |
   |                |                |                | used, i.e.     |
   |                |                |                | positive sign  |
   |                |                |                | means flow out |
   |                |                |                | from a node.   |
   +----------------+----------------+----------------+----------------+
   | targetUdc      | 0..1           | `Vol           | Target value   |
   |                |                | tage           | for DC voltage |
   |                |                |  <#Voltage>`__ | magnitude. The |
   |                |                |                | attribute      |
   |                |                |                | shall be a     |
   |                |                |                | positive       |
   |                |                |                | value.         |
   +----------------+----------------+----------------+----------------+
   | uc             | 0..1           | `Vol           | Line-to-line   |
   |                |                | tage           | converter      |
   |                |                |  <#Voltage>`__ | voltage, the   |
   |                |                |                | voltage at the |
   |                |                |                | AC side of the |
   |                |                |                | valve. It is   |
   |                |                |                | converter's    |
   |                |                |                | state          |
   |                |                |                | variable,      |
   |                |                |                | result from    |
   |                |                |                | power flow.    |
   |                |                |                | The attribute  |
   |                |                |                | shall be a     |
   |                |                |                | positive       |
   |                |                |                | value.         |
   +----------------+----------------+----------------+----------------+
   | udc            | 0..1           | `Vol           | Converter      |
   |                |                | tage           | voltage at the |
   |                |                |  <#Voltage>`__ | DC side, also  |
   |                |                |                | called Ud. It  |
   |                |                |                | is converter's |
   |                |                |                | state          |
   |                |                |                | variable,      |
   |                |                |                | result from    |
   |                |                |                | power flow.    |
   |                |                |                | The attribute  |
   |                |                |                | shall be a     |
   |                |                |                | positive       |
   |                |                |                | value.         |
   +----------------+----------------+----------------+----------------+
   | valveU0        | 0..1           | `Vol           | Valve          |
   |                |                | tage           | threshold      |
   |                |                |  <#Voltage>`__ | voltage, also  |
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
   |                |                |                | alves*valveU0. |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-67

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: ACDCTerminal

   ` <#ACDCTerminal>`__

   .. rubric:: ACDCTerminal
      :name: acdcterminal
      :class: abstract

   Core

   An electrical connection point (AC or DC) to a piece of conducting
   equipment. Terminals are connected at physical connection points
   called connectivity nodes.

   .. rubric:: Native Members
      :name: native-members-63

   +----------------+------+-------------------+-------------------+
   | sequenceNumber | 1..1 | `Inte             | The orientation   |
   |                |      | ger <#Integer>`__ | of the terminal   |
   |                |      |                   | connections for a |
   |                |      |                   | multiple terminal |
   |                |      |                   | conducting        |
   |                |      |                   | equipment. The    |
   |                |      |                   | sequence          |
   |                |      |                   | numbering starts  |
   |                |      |                   | with 1 and        |
   |                |      |                   | additional        |
   |                |      |                   | terminals should  |
   |                |      |                   | follow in         |
   |                |      |                   | increasing order. |
   |                |      |                   | The first         |
   |                |      |                   | terminal is the   |
   |                |      |                   | "starting point"  |
   |                |      |                   | for a two         |
   |                |      |                   | terminal branch.  |
   +----------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-68

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: AsynchronousMachineDynamics

   ` <#AsynchronousMachineDynamics>`__

   .. rubric:: AsynchronousMachineDynamics
      :name: asynchronousmachinedynamics
      :class: abstract

   AsynchronousMachineDynamics

   Asynchronous machine whose behaviour is described by reference to a
   standard model expressed in either time constant reactance form or
   equivalent circuit form or by definition of a user-defined model.

   Parameter details:

   1. Asynchronous machine parameters such as *Xl, Xs,* etc. are
      actually used as inductances in the model, but are commonly
      referred to as reactances since, at nominal frequency, the PU
      values are the same. However, some references use the symbol *L*
      instead of *X*.

   .. rubric:: Native Members
      :name: native-members-64

   +-------------------+------+-------------------+-------------------+
   | As                | 0..1 | `Asynchronou      | Asynchronous      |
   | ynchronousMachine |      | sMachine <#Asynch | machine to which  |
   |                   |      | ronousMachine>`__ | this asynchronous |
   |                   |      |                   | machine dynamics  |
   |                   |      |                   | model applies.    |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-69

   +-------------------+------+-------------------+-------------------+
   | damping           | 1..1 | `                 | see               |
   |                   |      | Float <#Float>`__ | `RotatingMa       |
   |                   |      |                   | chineDynamics <#R |
   |                   |      |                   | otatingMachineDyn |
   |                   |      |                   | amics.damping>`__ |
   +-------------------+------+-------------------+-------------------+
   | inertia           | 1..1 | `Seco             | see               |
   |                   |      | nds <#Seconds>`__ | `RotatingMa       |
   |                   |      |                   | chineDynamics <#R |
   |                   |      |                   | otatingMachineDyn |
   |                   |      |                   | amics.inertia>`__ |
   +-------------------+------+-------------------+-------------------+
   | stato             | 1..1 | `PU <#PU>`__      | see               |
   | rLeakageReactance |      |                   | `Rotating         |
   |                   |      |                   | MachineDynamics < |
   |                   |      |                   | #RotatingMachineD |
   |                   |      |                   | ynamics.statorLea |
   |                   |      |                   | kageReactance>`__ |
   +-------------------+------+-------------------+-------------------+
   | statorResistance  | 1..1 | `PU <#PU>`__      | see               |
   |                   |      |                   | `Ro               |
   |                   |      |                   | tatingMachineDyna |
   |                   |      |                   | mics <#RotatingMa |
   |                   |      |                   | chineDynamics.sta |
   |                   |      |                   | torResistance>`__ |
   +-------------------+------+-------------------+-------------------+

   +---------+------+------------------------+------------------------+
   | mRID    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.mRID>`__ |
   +---------+------+------------------------+------------------------+
   | enabled | 1..1 | `Boolean <#Boolean>`__ | see                    |
   |         |      |                        | `DynamicsFunct         |
   |         |      |                        | ionBlock <#DynamicsFun |
   |         |      |                        | ctionBlock.enabled>`__ |
   +---------+------+------------------------+------------------------+
   | name    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.name>`__ |
   +---------+------+------------------------+------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: Breaker

   ` <#Breaker>`__

   .. rubric:: Breaker
      :name: breaker
      :class: abstract

   Wires

   A mechanical switching device capable of making, carrying, and
   breaking currents under normal circuit conditions and also making,
   carrying for a specified time, and breaking currents under specified
   abnormal circuit conditions e.g. those of short circuit.

   .. rubric:: Inherited Members
      :name: inherited-members-70

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: ConductingEquipment

   ` <#ConductingEquipment>`__

   .. rubric:: ConductingEquipment
      :name: conductingequipment
      :class: abstract

   Core

   The parts of the AC power system that are designed to carry current
   or that are conductively connected through terminals.

   .. rubric:: Native Members
      :name: native-members-65

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | Base voltage of this |
   |             |      | ge <#BaseVoltage>`__ | conducting           |
   |             |      |                      | equipment. Use only  |
   |             |      |                      | when there is no     |
   |             |      |                      | voltage level        |
   |             |      |                      | container used and   |
   |             |      |                      | only one base        |
   |             |      |                      | voltage applies. For |
   |             |      |                      | example, not used    |
   |             |      |                      | for transformers.    |
   +-------------+------+----------------------+----------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-71

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: Conductor

   ` <#Conductor>`__

   .. rubric:: Conductor
      :name: conductor
      :class: abstract

   Wires

   Combination of conducting material with consistent electrical
   characteristics, building a single electrical system, used to carry
   current between points in the power system.

   .. rubric:: Native Members
      :name: native-members-66

   +--------+------+----------------------+-------------------------+
   | length | 1..1 | `Length <#Length>`__ | Segment length for      |
   |        |      |                      | calculating line        |
   |        |      |                      | segment capabilities.   |
   +--------+------+----------------------+-------------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-72

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: ConnectedFacility

   ` <#ConnectedFacility>`__

   .. rubric:: ConnectedFacility
      :name: connectedfacility
      :class: abstract

   Emtiop

   A collection of components that comprise a facility connected to the
   grid, such as a generating plant or large load.

   .. rubric:: Native Members
      :name: native-members-67

   +-------------------+-------+-------------------+-------------------+
   | ACPoin            | 0..1  | `AC               | The connection    |
   | tOfCommonCoupling |       | PointOfCommonCoup | point for this    |
   |                   |       | ling <#ACPointOfC | facility. It      |
   |                   |       | ommonCoupling>`__ | should be         |
   |                   |       |                   | associated with a |
   |                   |       |                   | ConnectivityNode  |
   |                   |       |                   | within the        |
   |                   |       |                   | facility network  |
   |                   |       |                   | model, where it   |
   |                   |       |                   | may be connected  |
   |                   |       |                   | to an external    |
   |                   |       |                   | network model.    |
   +-------------------+-------+-------------------+-------------------+
   | Equipments        | 0..\* | `Equipmen         | The Equipments    |
   |                   |       | t <#Equipment>`__ | associated with   |
   |                   |       |                   | this              |
   |                   |       |                   | C                 |
   |                   |       |                   | onnectedFacility. |
   +-------------------+-------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-73

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: ConnectivityNodeContainer

   ` <#ConnectivityNodeContainer>`__

   .. rubric:: ConnectivityNodeContainer
      :name: connectivitynodecontainer
      :class: abstract

   Core

   A base class for all objects that may contain connectivity nodes or
   topological nodes.

   .. rubric:: Inherited Members
      :name: inherited-members-74

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: Curve

   ` <#Curve>`__

   .. rubric:: Curve
      :name: curve
      :class: abstract

   Core

   A multi-purpose curve or functional relationship between an
   independent variable (X-axis) and dependent (Y-axis) variables.

   .. rubric:: Native Members
      :name: native-members-68

   +----------------+----------------+----------------+----------------+
   | mRID           | 1..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | curveStyle     | 0..1           | `CurveStyl     | The style or   |
   |                |                | e <#           | shape of the   |
   |                |                | CurveStyle>`__ | curve.         |
   +----------------+----------------+----------------+----------------+
   | name           | 1..1           | `S             | The name is    |
   |                |                | trin           | any free human |
   |                |                | g <#String>`__ | readable and   |
   |                |                |                | possibly non   |
   |                |                |                | unique text    |
   |                |                |                | naming the     |
   |                |                |                | object.        |
   +----------------+----------------+----------------+----------------+
   | xMultiplier    | 0..1           | `Un            | Multiplier for |
   |                |                | itMultip       | X-axis.        |
   |                |                | lier <#%20Unit |                |
   |                |                | Multiplier>`__ |                |
   +----------------+----------------+----------------+----------------+
   | xUnit          | 0..1           | `UnitSymbo     | The X-axis     |
   |                |                | l <#           | units of       |
   |                |                | UnitSymbol>`__ | measure.       |
   +----------------+----------------+----------------+----------------+
   | y1Multiplier   | 0..1           | `Un            | Multiplier for |
   |                |                | itMultip       | Y1-axis.       |
   |                |                | lier <#%20Unit |                |
   |                |                | Multiplier>`__ |                |
   +----------------+----------------+----------------+----------------+
   | y1Unit         | 0..1           | `UnitSymbo     | The Y1-axis    |
   |                |                | l <#           | units of       |
   |                |                | UnitSymbol>`__ | measure.       |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-75

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DCBaseTerminal

   ` <#DCBaseTerminal>`__

   .. rubric:: DCBaseTerminal
      :name: dcbaseterminal
      :class: abstract

   DC

   An electrical connection point at a piece of DC conducting equipment.
   DC terminals are connected at one physical DC node that may have
   multiple DC terminals connected. A DC node is similar to an AC
   connectivity node. The model requires that DC connections are
   distinct from AC connections.

   .. rubric:: Native Members
      :name: native-members-69

   +--------+------+----------------------+-------------------------+
   | DCNode | 1..1 | `DCNode <#DCNode>`__ | The DC connectivity     |
   |        |      |                      | node to which this DC   |
   |        |      |                      | base terminal connects  |
   |        |      |                      | with zero impedance.    |
   +--------+------+----------------------+-------------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-76

   +----------------+------+-------------------+-------------------+
   | sequenceNumber | 1..1 | `Inte             | see               |
   |                |      | ger <#Integer>`__ | `ACDCTerminal     |
   |                |      |                   |  <#ACDCTerminal.s |
   |                |      |                   | equenceNumber>`__ |
   +----------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DCConductingEquipment

   ` <#DCConductingEquipment>`__

   .. rubric:: DCConductingEquipment
      :name: dcconductingequipment
      :class: abstract

   DC

   The parts of the DC power system that are designed to carry current
   or that are conductively connected through DC terminals.

   .. rubric:: Native Members
      :name: native-members-70

   +----------------+----------------+----------------+----------------+
   | ratedCurrent   | 0..1           | `C             | The maximum    |
   |                |                | urrentFlow <#C | continuous     |
   |                |                | urrentFlow>`__ | current        |
   |                |                |                | carrying       |
   |                |                |                | capacity in    |
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
   | ratedUdc       | 0..1           | `Vol           | Rated DC       |
   |                |                | tage           | device         |
   |                |                |  <#Voltage>`__ | voltage. The   |
   |                |                |                | attribute      |
   |                |                |                | shall be a     |
   |                |                |                | positive       |
   |                |                |                | value. It is   |
   |                |                |                | configuration  |
   |                |                |                | data used in   |
   |                |                |                | power flow.    |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-77

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DCSwitch

   ` <#DCSwitch>`__

   .. rubric:: DCSwitch
      :name: dcswitch
      :class: abstract

   DC

   A switch within the DC system.

   .. rubric:: Native Members
      :name: native-members-71

   +----------------+----------------+----------------+----------------+
   | locked         | 0..1           | `Boo           | If true, the   |
   |                |                | lean           | switch is      |
   |                |                |  <#Boolean>`__ | locked. The    |
   |                |                |                | resulting      |
   |                |                |                | switch state   |
   |                |                |                | is a           |
   |                |                |                | combination of |
   |                |                |                | locked and     |
   |                |                |                | DCSwitch.open  |
   |                |                |                | attributes as  |
   |                |                |                | follows:       |
   |                |                |                |                |
   |                |                |                | -  locked=true |
   |                |                |                |    and DCSw    |
   |                |                |                |    i           |
   |                |                |                | tch.open=true. |
   |                |                |                |    The         |
   |                |                |                |    resulting   |
   |                |                |                |    state is    |
   |                |                |                |    open and    |
   |                |                |                |    locked;     |
   |                |                |                | -              |
   |                |                |                |   locked=false |
   |                |                |                |    and DCSw    |
   |                |                |                |    i           |
   |                |                |                | tch.open=true. |
   |                |                |                |    The         |
   |                |                |                |    resulting   |
   |                |                |                |    state is    |
   |                |                |                |    open;       |
   |                |                |                | -              |
   |                |                |                |   locked=false |
   |                |                |                |    and DCSwi   |
   |                |                |                |    t           |
   |                |                |                | ch.open=false. |
   |                |                |                |    The         |
   |                |                |                |    resulting   |
   |                |                |                |    state is    |
   |                |                |                |    closed.     |
   +----------------+----------------+----------------+----------------+
   | normalOpen     | 0..1           | `Boo           | The attribute  |
   |                |                | lean           | is used in     |
   |                |                |  <#Boolean>`__ | cases when no  |
   |                |                |                | Measurement    |
   |                |                |                | for the status |
   |                |                |                | value is       |
   |                |                |                | present. If    |
   |                |                |                | the DCSwitch   |
   |                |                |                | has a status   |
   |                |                |                | measurement    |
   |                |                |                | the Discr      |
   |                |                |                | e              |
   |                |                |                | te.normalValue |
   |                |                |                | is expected to |
   |                |                |                | match with the |
   |                |                |                | DCSwi          |
   |                |                |                | t              |
   |                |                |                | ch.normalOpen. |
   +----------------+----------------+----------------+----------------+
   | open           | 0..1           | `Boo           | The attribute  |
   |                |                | lean           | tells if the   |
   |                |                |  <#Boolean>`__ | switch is      |
   |                |                |                | considered     |
   |                |                |                | open when used |
   |                |                |                | as input to    |
   |                |                |                | topology       |
   |                |                |                | processing.    |
   +----------------+----------------+----------------+----------------+
   | retained       | 0..1           | `Boo           | Branch is      |
   |                |                | lean           | retained in    |
   |                |                |  <#Boolean>`__ | the            |
   |                |                |                | topological    |
   |                |                |                | solution. The  |
   |                |                |                | flow through   |
   |                |                |                | retained       |
   |                |                |                | switches will  |
   |                |                |                | normally be    |
   |                |                |                | calculated in  |
   |                |                |                | power flow.    |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-78

   +--------------+------+----------------------+----------------------+
   | ratedCurrent | 0..1 | `CurrentFl           | see                  |
   |              |      | ow <#CurrentFlow>`__ | `DC                  |
   |              |      |                      | ConductingEquipment  |
   |              |      |                      | <#DCConductingEquipm |
   |              |      |                      | ent.ratedCurrent>`__ |
   +--------------+------+----------------------+----------------------+
   | ratedUdc     | 0..1 | `V                   | see                  |
   |              |      | oltage <#Voltage>`__ | `DCConductingEquipm  |
   |              |      |                      | ent <#DCConductingEq |
   |              |      |                      | uipment.ratedUdc>`__ |
   +--------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DetailedModelDescriptor

   ` <#DetailedModelDescriptor>`__

   .. rubric:: DetailedModelDescriptor
      :name: detailedmodeldescriptor
      :class: abstract

   DetailedModelDescription

   Describes different components of a detailed model.

   .. rubric:: Native Members
      :name: native-members-72

   +----------------+----------------+----------------+----------------+
   | mRID           | 0..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | DetailedMo     | 0..1           | `DetailedM     | The detailed   |
   | d              |                | o              | model type     |
   | elTypeDynamics |                | delTypeDynamic | dynamics that  |
   |                |                | s <#Deta       | has detailed   |
   |                |                | iledMod%20elTy | model          |
   |                |                | peDynamics>`__ | descriptor.    |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-79

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DetailedModelTypeDynamics

   ` <#DetailedModelTypeDynamics>`__

   .. rubric:: DetailedModelTypeDynamics
      :name: detailedmodeltypedynamics
      :class: abstract

   DetailedModelDescription

   The main class that packages all related to this type of a detailed
   model. This includes all parameters, functions, signals, etc.

.. container:: group
   :name: DiagramObject

   ` <#DiagramObject>`__

   .. rubric:: DiagramObject
      :name: diagramobject
      :class: abstract

   DiagramLayout

   An object that defines one or more points in a given space. This
   object can be associated with anything that specializes
   IdentifiedObject. For single line diagrams such objects typically
   include such items as analog values, breakers, disconnectors, power
   transformers, and transmission lines.

   .. rubric:: Native Members
      :name: native-members-73

   +----------------+----------------+----------------+----------------+
   | mRID           | 1..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | drawingOrder   | 1..1           | `Int           | The drawing    |
   |                |                | eger           | order of this  |
   |                |                |  <#Integer>`__ | element. The   |
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
   | isPolygon      | 1..1           | `Boo           | Defines        |
   |                |                | lean           | whether or not |
   |                |                |  <#Boolean>`__ | the diagram    |
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
   | name           | 1..1           | `S             | The name is    |
   |                |                | trin           | any free human |
   |                |                | g <#String>`__ | readable and   |
   |                |                |                | possibly non   |
   |                |                |                | unique text    |
   |                |                |                | naming the     |
   |                |                |                | object.        |
   +----------------+----------------+----------------+----------------+
   | I              | 1..1           | `Identi        | The domain     |
   | d              |                | fiedObje       | object to      |
   | entifiedObject |                | ct <#Id%20enti | which this     |
   |                |                | fiedObject>`__ | diagram object |
   |                |                |                | is associated. |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-80

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: DynamicsFunctionBlock

   ` <#DynamicsFunctionBlock>`__

   .. rubric:: DynamicsFunctionBlock
      :name: dynamicsfunctionblock
      :class: abstract

   StandardModels

   Abstract parent class for all Dynamics function blocks.

   .. rubric:: Native Members
      :name: native-members-74

   +----------------+----------------+----------------+----------------+
   | mRID           | 1..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | enabled        | 1..1           | `Boo           | Function block |
   |                |                | lean           | used           |
   |                |                |  <#Boolean>`__ | indicator.     |
   |                |                |                |                |
   |                |                |                | true = use of  |
   |                |                |                | function block |
   |                |                |                | is enabled     |
   |                |                |                |                |
   |                |                |                | false = use of |
   |                |                |                | function block |
   |                |                |                | is disabled.   |
   +----------------+----------------+----------------+----------------+
   | name           | 1..1           | `S             | The name is    |
   |                |                | trin           | any free human |
   |                |                | g <#String>`__ | readable and   |
   |                |                |                | possibly non   |
   |                |                |                | unique text    |
   |                |                |                | naming the     |
   |                |                |                | object.        |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-81

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: EnergyConnection

   ` <#EnergyConnection>`__

   .. rubric:: EnergyConnection
      :name: energyconnection
      :class: abstract

   Wires

   A connection of energy generation or consumption on the power system
   model.

   .. rubric:: Inherited Members
      :name: inherited-members-82

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: Equipment

   ` <#Equipment>`__

   .. rubric:: Equipment
      :name: equipment
      :class: abstract

   Core

   The parts of a power system that are physical devices, electronic or
   mechanical.

   .. rubric:: Native Members
      :name: native-members-75

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | Specifies the     |
   |                   |      | ean <#Boolean>`__ | availability of   |
   |                   |      |                   | the equipment.    |
   |                   |      |                   | True means the    |
   |                   |      |                   | equipment is      |
   |                   |      |                   | available for     |
   |                   |      |                   | topology          |
   |                   |      |                   | processing, which |
   |                   |      |                   | determines if the |
   |                   |      |                   | equipment is      |
   |                   |      |                   | energized or not. |
   |                   |      |                   | False means that  |
   |                   |      |                   | the equipment is  |
   |                   |      |                   | treated by        |
   |                   |      |                   | network           |
   |                   |      |                   | applications as   |
   |                   |      |                   | if it is not in   |
   |                   |      |                   | the model.        |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | Container of this |
   | quipmentContainer |      | Container <#Equip | equipment.        |
   |                   |      | mentContainer>`__ |                   |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-83

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: GeneratingUnit

   ` <#GeneratingUnit>`__

   .. rubric:: GeneratingUnit
      :name: generatingunit
      :class: abstract

   Production

   A single or set of synchronous machines for converting mechanical
   power into alternating-current power. For example, individual
   machines within a set may be defined for scheduling purposes while a
   single control signal is derived for the set. In this case there
   would be a GeneratingUnit for each member of the set and an
   additional GeneratingUnit corresponding to the set.

   .. rubric:: Native Members
      :name: native-members-76

   +---------------+------+---------------------+---------------------+
   | maxOperatingP | 1..1 | `ActivePowe         | This is the maximum |
   |               |      | r <#ActivePower>`__ | operating active    |
   |               |      |                     | power limit the     |
   |               |      |                     | dispatcher can      |
   |               |      |                     | enter for this      |
   |               |      |                     | unit.               |
   +---------------+------+---------------------+---------------------+
   | minOperatingP | 1..1 | `ActivePowe         | This is the minimum |
   |               |      | r <#ActivePower>`__ | operating active    |
   |               |      |                     | power limit the     |
   |               |      |                     | dispatcher can      |
   |               |      |                     | enter for this      |
   |               |      |                     | unit.               |
   +---------------+------+---------------------+---------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-84

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: IEEECigreAPISignal

   ` <#IEEECigreAPISignal>`__

   .. rubric:: IEEECigreAPISignal
      :name: ieeecigreapisignal
      :class: abstract

   Emtiop

   The parent class for CIGRE TB 958 input and output signals. Use the
   ACDCTerminal association for network flows, the DCNode association
   for DC bus quantities, the ConnectivityNode association for AC bus
   quantities, or no association for references levels or other signals
   not connected to the electric power networks.

   .. rubric:: Native Members
      :name: native-members-77

   +-------------------+------+-------------------+-------------------+
   | apiName           | 0..1 | `St               | The name of this  |
   |                   |      | ring <#String>`__ | signal, as        |
   |                   |      |                   | returned by the   |
   |                   |      |                   | CIGRE TB 958 API. |
   |                   |      |                   | The inherited     |
   |                   |      |                   | Iden              |
   |                   |      |                   | tifiedObject.name |
   |                   |      |                   | attribute might   |
   |                   |      |                   | not necessarily   |
   |                   |      |                   | match this name.  |
   +-------------------+------+-------------------+-------------------+
   | apiParameterKind  | 0..1 | `IEEECi           | Establishes the   |
   |                   |      | greAPIParameterKi | signal value      |
   |                   |      | nd <#IEEECigreAPI | size, in bytes,   |
   |                   |      | ParameterKind>`__ | expected in the   |
   |                   |      |                   | CIGRE TB 958 API. |
   +-------------------+------+-------------------+-------------------+
   | apiSequenceNumber | 0..1 | `Inte             | The signal's      |
   |                   |      | ger <#Integer>`__ | expected          |
   |                   |      |                   | zero-based        |
   |                   |      |                   | sequence number   |
   |                   |      |                   | in the CIGRE TB   |
   |                   |      |                   | 958 API array for |
   |                   |      |                   | input and output  |
   |                   |      |                   | signals.          |
   +-------------------+------+-------------------+-------------------+
   | apiWidth          | 0..1 | `Inte             | Signal array      |
   |                   |      | ger <#Integer>`__ | dimension from    |
   |                   |      |                   | the CIGRE TB 958  |
   |                   |      |                   | API, defaults to  |
   |                   |      |                   | 1.                |
   +-------------------+------+-------------------+-------------------+
   | multiplier        | 0..1 | `U                | Multiplier for    |
   |                   |      | nitMultiplier <#U | the units of this |
   |                   |      | nitMultiplier>`__ | signal, in CIM.   |
   |                   |      |                   | May require       |
   |                   |      |                   | interpretation of |
   |                   |      |                   | information       |
   |                   |      |                   | returned from the |
   |                   |      |                   | CIGRE TB 958 API. |
   +-------------------+------+-------------------+-------------------+
   | phase             | 0..1 | `Sin              | The signal's      |
   |                   |      | glePhaseKind <#Si | phase, as         |
   |                   |      | nglePhaseKind>`__ | applicable, for   |
   |                   |      |                   | multiphase signal |
   |                   |      |                   | connections.      |
   +-------------------+------+-------------------+-------------------+
   | unit              | 0..1 | `UnitSymbol       | Signal units, if  |
   |                   |      |  <#UnitSymbol>`__ | applicable, in    |
   |                   |      |                   | CIM. May require  |
   |                   |      |                   | interpretation of |
   |                   |      |                   | information       |
   |                   |      |                   | returned from the |
   |                   |      |                   | CIGRE TB 958 API. |
   +-------------------+------+-------------------+-------------------+
   | ConnectivityNode  | 0..1 | `Conne            | Use for a bus     |
   |                   |      | ctivityNode <#Con | voltage or other  |
   |                   |      | nectivityNode>`__ | bus quantity      |
   |                   |      |                   | signal. Mutually  |
   |                   |      |                   | exclusive with    |
   |                   |      |                   | association to    |
   |                   |      |                   | DCNode or         |
   |                   |      |                   | ACDCTerminal.     |
   +-------------------+------+-------------------+-------------------+
   | DCNode            | 0..1 | `DC               | Use for a DC      |
   |                   |      | Node <#DCNode>`__ | voltage or other  |
   |                   |      |                   | quantity related  |
   |                   |      |                   | to DC buses.      |
   |                   |      |                   | Mutually          |
   |                   |      |                   | exclusive with    |
   |                   |      |                   | assocation to     |
   |                   |      |                   | ConnectivityNode  |
   |                   |      |                   | or ACDCTerminal.  |
   +-------------------+------+-------------------+-------------------+
   | IEEEC             | 0..1 | `                 | Expanded set of   |
   | igreAPISignalInfo |      | IEEECigreAPISigna | attributes        |
   |                   |      | lInfo <#IEEECigre | available from    |
   |                   |      | APISignalInfo>`__ | the CIGRE TB 958  |
   |                   |      |                   | API.              |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-85

   +-------------------+------+-------------------+-------------------+
   | ACDCTerminal      | 0..1 | `ACDCTerminal <   | see               |
   |                   |      | #ACDCTerminal>`__ | `S                |
   |                   |      |                   | ignalDescriptor < |
   |                   |      |                   | #SignalDescriptor |
   |                   |      |                   | .ACDCTerminal>`__ |
   +-------------------+------+-------------------+-------------------+
   | Dyna              | 0..1 | `DynamicsFunctio  | see               |
   | micsFunctionBlock |      | nBlock <#Dynamics | `SignalDesc       |
   |                   |      | FunctionBlock>`__ | riptor <#SignalDe |
   |                   |      |                   | scriptor.Dynamics |
   |                   |      |                   | FunctionBlock>`__ |
   +-------------------+------+-------------------+-------------------+

   +-------------------+------+-------------------+-------------------+
   | mRID              | 0..1 | `St               | see               |
   |                   |      | ring <#String>`__ | `Detaile          |
   |                   |      |                   | dModelDescriptor  |
   |                   |      |                   | <#DetailedModelDe |
   |                   |      |                   | scriptor.mRID>`__ |
   +-------------------+------+-------------------+-------------------+
   | Detailed          | 0..1 | `Detail           | see               |
   | ModelTypeDynamics |      | edModelTypeDynami | `DetailedMod      |
   |                   |      | cs <#DetailedMode | elDescriptor <#De |
   |                   |      | lTypeDynamics>`__ | tailedModelDescri |
   |                   |      |                   | ptor.DetailedMode |
   |                   |      |                   | lTypeDynamics>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: IdentifiedObject

   ` <#IdentifiedObject>`__

   .. rubric:: IdentifiedObject
      :name: identifiedobject
      :class: abstract

   Core

   This is a class that provides common identification for all classes
   needing identification and naming attributes.

   .. rubric:: Native Members
      :name: native-members-78

   +----------------+----------------+----------------+----------------+
   | mRID           | 0..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | name           | 0..1           | `S             | The name is    |
   |                |                | trin           | any free human |
   |                |                | g <#String>`__ | readable and   |
   |                |                |                | possibly non   |
   |                |                |                | unique text    |
   |                |                |                | naming the     |
   |                |                |                | object.        |
   +----------------+----------------+----------------+----------------+

.. container:: group
   :name: MutualCoupling

   ` <#MutualCoupling>`__

   .. rubric:: MutualCoupling
      :name: mutualcoupling
      :class: abstract

   Wires

   This class represents the zero sequence line mutual coupling.

   .. rubric:: Native Members
      :name: native-members-79

   +----------------+----------------+----------------+----------------+
   | mRID           | 1..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | b0ch           | 0..1           | `S             | Zero sequence  |
   |                |                | usceptance <#S | mutual         |
   |                |                | usceptance>`__ | coupling shunt |
   |                |                |                | (charging)     |
   |                |                |                | susceptance,   |
   |                |                |                | uniformly      |
   |                |                |                | distributed,   |
   |                |                |                | of the entire  |
   |                |                |                | line section.  |
   +----------------+----------------+----------------+----------------+
   | distance11     | 0..1           | `L             | Distance to    |
   |                |                | engt           | the start of   |
   |                |                | h <#Length>`__ | the coupled    |
   |                |                |                | region from    |
   |                |                |                | the first      |
   |                |                |                | line's         |
   |                |                |                | terminal       |
   |                |                |                | having         |
   |                |                |                | sequence       |
   |                |                |                | number equal   |
   |                |                |                | to 1.          |
   +----------------+----------------+----------------+----------------+
   | distance12     | 0..1           | `L             | Distance to    |
   |                |                | engt           | the end of the |
   |                |                | h <#Length>`__ | coupled region |
   |                |                |                | from the first |
   |                |                |                | line's         |
   |                |                |                | terminal with  |
   |                |                |                | sequence       |
   |                |                |                | number equal   |
   |                |                |                | to 1.          |
   +----------------+----------------+----------------+----------------+
   | distance21     | 0..1           | `L             | Distance to    |
   |                |                | engt           | the start of   |
   |                |                | h <#Length>`__ | coupled region |
   |                |                |                | from the       |
   |                |                |                | second line's  |
   |                |                |                | terminal with  |
   |                |                |                | sequence       |
   |                |                |                | number equal   |
   |                |                |                | to 1.          |
   +----------------+----------------+----------------+----------------+
   | distance22     | 0..1           | `L             | Distance to    |
   |                |                | engt           | the end of     |
   |                |                | h <#Length>`__ | coupled region |
   |                |                |                | from the       |
   |                |                |                | second line's  |
   |                |                |                | terminal with  |
   |                |                |                | sequence       |
   |                |                |                | number equal   |
   |                |                |                | to 1.          |
   +----------------+----------------+----------------+----------------+
   | g0ch           | 0..1           | `C             | Zero sequence  |
   |                |                | onductance <#C | mutual         |
   |                |                | onductance>`__ | coupling shunt |
   |                |                |                | (charging)     |
   |                |                |                | conductance,   |
   |                |                |                | uniformly      |
   |                |                |                | distributed,   |
   |                |                |                | of the entire  |
   |                |                |                | line section.  |
   +----------------+----------------+----------------+----------------+
   | name           | 1..1           | `S             | The name is    |
   |                |                | trin           | any free human |
   |                |                | g <#String>`__ | readable and   |
   |                |                |                | possibly non   |
   |                |                |                | unique text    |
   |                |                |                | naming the     |
   |                |                |                | object.        |
   +----------------+----------------+----------------+----------------+
   | r0             | 0..1           | `Resistanc     | Zero sequence  |
   |                |                | e <#           | b              |
   |                |                | Resistance>`__ | r              |
   |                |                |                | anch-to-branch |
   |                |                |                | mutual         |
   |                |                |                | impedance      |
   |                |                |                | coupling,      |
   |                |                |                | resistance.    |
   +----------------+----------------+----------------+----------------+
   | x0             | 0..1           | `Reactan       | Zero sequence  |
   |                |                | ce <           | b              |
   |                |                | #Reactance>`__ | r              |
   |                |                |                | anch-to-branch |
   |                |                |                | mutual         |
   |                |                |                | impedance      |
   |                |                |                | coupling,      |
   |                |                |                | reactance.     |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-86

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: OperationalLimit

   ` <#OperationalLimit>`__

   .. rubric:: OperationalLimit
      :name: operationallimit
      :class: abstract

   OperationalLimits

   A value and normal value associated with a specific kind of limit.

   The sub class value and normalValue attributes vary inversely to the
   associated OperationalLimitType.acceptableDuration
   (acceptableDuration for short).

   If a particular piece of equipment has multiple operational limits of
   the same kind (apparent power, current, etc.), the limit with the
   greatest acceptableDuration shall have the smallest limit value and
   the limit with the smallest acceptableDuration shall have the largest
   limit value. Note: A large current can only be allowed to flow
   through a piece of equipment for a short duration without causing
   damage, but a lesser current can be allowed to flow for a longer
   duration.

   .. rubric:: Native Members
      :name: native-members-80

   +----------------+----------------+----------------+----------------+
   | mRID           | 1..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | name           | 1..1           | `S             | The name is    |
   |                |                | trin           | any free human |
   |                |                | g <#String>`__ | readable and   |
   |                |                |                | possibly non   |
   |                |                |                | unique text    |
   |                |                |                | naming the     |
   |                |                |                | object.        |
   +----------------+----------------+----------------+----------------+
   | Oper           | 0..1           | `OperationalL  | The limit set  |
   | a              |                | imitSet        | to which the   |
   | tionalLimitSet |                | <#Opera%20tion | limit values   |
   |                |                | alLimitSet>`__ | belong.        |
   +----------------+----------------+----------------+----------------+
   | Opera          | 0..1           | `              | The limit type |
   | t              |                | OperationalLim | associated     |
   | ionalLimitType |                | itType <       | with this      |
   |                |                | #Operat%20iona | limit.         |
   |                |                | lLimitType>`__ |                |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-87

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: PSRType

   ` <#PSRType>`__

   .. rubric:: PSRType
      :name: psrtype
      :class: abstract

   Core

   Classifying instances of the same class, e.g. overhead and
   underground ACLineSegments. This classification mechanism is intended
   to provide flexibility outside the scope of this document,
   i.e. provide customisation that is non standard.

   .. rubric:: Inherited Members
      :name: inherited-members-88

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: PhaseTapChanger

   ` <#PhaseTapChanger>`__

   .. rubric:: PhaseTapChanger
      :name: phasetapchanger
      :class: abstract

   Wires

   A transformer phase shifting tap model that controls the phase angle
   difference across the power transformer and potentially the active
   power flow through the power transformer. This phase tap model may
   also impact the voltage magnitude.

   .. rubric:: Native Members
      :name: native-members-81

   +----------------+------+-------------------+-------------------+
   | TransformerEnd | 0..1 | `T                | Transformer end   |
   |                |      | ransformerEnd <#T | to which this     |
   |                |      | ransformerEnd>`__ | phase tap changer |
   |                |      |                   | belongs.          |
   +----------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-89

   +-------------+------+----------------------+----------------------+
   | highStep    | 0..1 | `I                   | see                  |
   |             |      | nteger <#Integer>`__ | `TapChanger <#Tap    |
   |             |      |                      | Changer.highStep>`__ |
   +-------------+------+----------------------+----------------------+
   | lowStep     | 0..1 | `I                   | see                  |
   |             |      | nteger <#Integer>`__ | `TapChanger <#Ta     |
   |             |      |                      | pChanger.lowStep>`__ |
   +-------------+------+----------------------+----------------------+
   | neutralStep | 0..1 | `I                   | see                  |
   |             |      | nteger <#Integer>`__ | `TapChanger <#TapCha |
   |             |      |                      | nger.neutralStep>`__ |
   +-------------+------+----------------------+----------------------+
   | neutralU    | 0..1 | `V                   | see                  |
   |             |      | oltage <#Voltage>`__ | `TapChanger <#Tap    |
   |             |      |                      | Changer.neutralU>`__ |
   +-------------+------+----------------------+----------------------+
   | normalStep  | 0..1 | `I                   | see                  |
   |             |      | nteger <#Integer>`__ | `TapChanger <#TapCh  |
   |             |      |                      | anger.normalStep>`__ |
   +-------------+------+----------------------+----------------------+
   | step        | 1..1 | `Float <#Float>`__   | see                  |
   |             |      |                      | `TapChanger <        |
   |             |      |                      | #TapChanger.step>`__ |
   +-------------+------+----------------------+----------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: PointOfCommonCoupling

   ` <#PointOfCommonCoupling>`__

   .. rubric:: PointOfCommonCoupling
      :name: pointofcommoncoupling
      :class: abstract

   Core

   Point of Common Coupling (PCC) refers to the location where multiple
   electrical sources or loads are electrically connected and provide a
   reference point where the voltages and currents from different parts
   of the system are considered to be common. The PCC is used to support
   system analysis, control, and monitoring, as it provides a reference
   for understanding the interactions and power flow between various
   components within the system. It is also relevant to define the
   requirement and responsibility between different actors in operating
   a power system.

   .. rubric:: Native Members
      :name: native-members-82

   +----------------+----------------+----------------+----------------+
   | mRID           | 1..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | name           | 1..1           | `S             | The name is    |
   |                |                | trin           | any free human |
   |                |                | g <#String>`__ | readable and   |
   |                |                |                | possibly non   |
   |                |                |                | unique text    |
   |                |                |                | naming the     |
   |                |                |                | object.        |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-90

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: PowerElectronicsUnit

   ` <#PowerElectronicsUnit>`__

   .. rubric:: PowerElectronicsUnit
      :name: powerelectronicsunit
      :class: abstract

   Production

   A generating unit or battery or aggregation that connects to the AC
   network using power electronics rather than rotating machines.

   .. rubric:: Native Members
      :name: native-members-83

   +-------------------+------+-------------------+-------------------+
   | maxP              | 1..1 | `ActivePower      | Maximum active    |
   |                   |      | <#ActivePower>`__ | power limit. This |
   |                   |      |                   | is the maximum    |
   |                   |      |                   | (nameplate) limit |
   |                   |      |                   | for the unit.     |
   +-------------------+------+-------------------+-------------------+
   | minP              | 1..1 | `ActivePower      | Minimum active    |
   |                   |      | <#ActivePower>`__ | power limit. This |
   |                   |      |                   | is the minimum    |
   |                   |      |                   | (nameplate) limit |
   |                   |      |                   | for the unit.     |
   +-------------------+------+-------------------+-------------------+
   | PowerElec         | 1..1 | `PowerEle         | A power           |
   | tronicsConnection |      | ctronicsConnectio | electronics unit  |
   |                   |      | n <#PowerElectron | has a connection  |
   |                   |      | icsConnection>`__ | to the AC         |
   |                   |      |                   | network.          |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-91

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: PowerSystemResource

   ` <#PowerSystemResource>`__

   .. rubric:: PowerSystemResource
      :name: powersystemresource
      :class: abstract

   Core

   A power system resource (PSR) can be an item of equipment such as a
   switch, an equipment container containing many individual items of
   equipment such as a substation, or an organisational entity such as
   sub-control area. Power system resources can have measurements
   associated.

   .. rubric:: Native Members
      :name: native-members-84

   +----------------+----------------+----------------+----------------+
   | mRID           | 1..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | name           | 1..1           | `S             | The name is    |
   |                |                | trin           | any free human |
   |                |                | g <#String>`__ | readable and   |
   |                |                |                | possibly non   |
   |                |                |                | unique text    |
   |                |                |                | naming the     |
   |                |                |                | object.        |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-92

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: ProtectedSwitch

   ` <#ProtectedSwitch>`__

   .. rubric:: ProtectedSwitch
      :name: protectedswitch
      :class: abstract

   Wires

   A ProtectedSwitch is a switching device that can be operated by
   ProtectionEquipment.

   .. rubric:: Inherited Members
      :name: inherited-members-93

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: RegulatingCondEq

   ` <#RegulatingCondEq>`__

   .. rubric:: RegulatingCondEq
      :name: regulatingcondeq
      :class: abstract

   Wires

   A type of conducting equipment that can regulate a quantity (i.e.
   voltage or flow) at a specific point in the network.

   .. rubric:: Inherited Members
      :name: inherited-members-94

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: RotatingMachine

   ` <#RotatingMachine>`__

   .. rubric:: RotatingMachine
      :name: rotatingmachine
      :class: abstract

   Wires

   A rotating machine which may be used as a generator or motor.

   .. rubric:: Native Members
      :name: native-members-85

   +----------------+----------------+----------------+----------------+
   | p              | 1..1           | `A             | Active power   |
   |                |                | ctivePower <#A | injection.     |
   |                |                | ctivePower>`__ | Load sign      |
   |                |                |                | convention is  |
   |                |                |                | used, i.e.     |
   |                |                |                | positive sign  |
   |                |                |                | means flow out |
   |                |                |                | from a node.   |
   |                |                |                |                |
   |                |                |                | Starting value |
   |                |                |                | for a steady   |
   |                |                |                | state          |
   |                |                |                | solution.      |
   +----------------+----------------+----------------+----------------+
   | q              | 1..1           | `React         | Reactive power |
   |                |                | ivePower <#Rea | injection.     |
   |                |                | ctivePower>`__ | Load sign      |
   |                |                |                | convention is  |
   |                |                |                | used, i.e.     |
   |                |                |                | positive sign  |
   |                |                |                | means flow out |
   |                |                |                | from a node.   |
   |                |                |                |                |
   |                |                |                | Starting value |
   |                |                |                | for a steady   |
   |                |                |                | state          |
   |                |                |                | solution.      |
   +----------------+----------------+----------------+----------------+
   | ratedS         | 1..1           | `Appar         | Nameplate      |
   |                |                | entPower <#App | apparent power |
   |                |                | arentPower>`__ | rating for the |
   |                |                |                | unit.          |
   |                |                |                |                |
   |                |                |                | The attribute  |
   |                |                |                | shall have a   |
   |                |                |                | positive       |
   |                |                |                | value.         |
   +----------------+----------------+----------------+----------------+
   | ratedU         | 1..1           | `Vol           | Rated voltage  |
   |                |                | tage           | (nameplate     |
   |                |                |  <#Voltage>`__ | data, Ur in    |
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
   | GeneratingUnit | 1..1           | `Ge            | A synchronous  |
   |                |                | nerating       | machine may    |
   |                |                | Unit <#%20Gene | operate as a   |
   |                |                | ratingUnit>`__ | generator and  |
   |                |                |                | as such        |
   |                |                |                | becomes a      |
   |                |                |                | member of a    |
   |                |                |                | generating     |
   |                |                |                | unit.          |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-95

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: RotatingMachineDynamics

   ` <#RotatingMachineDynamics>`__

   .. rubric:: RotatingMachineDynamics
      :name: rotatingmachinedynamics
      :class: abstract

   StandardModels

   Abstract parent class for all synchronous and asynchronous machine
   standard models.

   .. rubric:: Native Members
      :name: native-members-86

   +-------------------+------+-------------------+-------------------+
   | damping           | 1..1 | `                 | Damping torque    |
   |                   |      | Float <#Float>`__ | coefficient (D)   |
   |                   |      |                   | (>= 0) in pu      |
   |                   |      |                   | torque/pu speed   |
   |                   |      |                   | deviation         |
   |                   |      |                   | (differential     |
   |                   |      |                   | type). A          |
   |                   |      |                   | proportionality   |
   |                   |      |                   | constant that,    |
   |                   |      |                   | when multiplied   |
   |                   |      |                   | by the angular    |
   |                   |      |                   | velocity of the   |
   |                   |      |                   | rotor poles with  |
   |                   |      |                   | respect to the    |
   |                   |      |                   | magnetic field    |
   |                   |      |                   | (frequency),      |
   |                   |      |                   | results in the    |
   |                   |      |                   | damping torque.   |
   |                   |      |                   | This value is     |
   |                   |      |                   | often zero when   |
   |                   |      |                   | the sources of    |
   |                   |      |                   | damping torques   |
   |                   |      |                   | (generator damper |
   |                   |      |                   | windings, load    |
   |                   |      |                   | damping effects,  |
   |                   |      |                   | etc.) are         |
   |                   |      |                   | modelled in       |
   |                   |      |                   | detail. Typical   |
   |                   |      |                   | value = 0.        |
   +-------------------+------+-------------------+-------------------+
   | inertia           | 1..1 | `Seco             | Inertia constant  |
   |                   |      | nds <#Seconds>`__ | of generator or   |
   |                   |      |                   | motor and         |
   |                   |      |                   | mechanical load   |
   |                   |      |                   | (*H*) (> 0). This |
   |                   |      |                   | is the            |
   |                   |      |                   | specification for |
   |                   |      |                   | the stored energy |
   |                   |      |                   | in the rotating   |
   |                   |      |                   | mass when         |
   |                   |      |                   | operating at      |
   |                   |      |                   | rated speed. For  |
   |                   |      |                   | a generator, this |
   |                   |      |                   | includes the      |
   |                   |      |                   | generator plus    |
   |                   |      |                   | all other         |
   |                   |      |                   | elements          |
   |                   |      |                   | (turbine,         |
   |                   |      |                   | exciter) on the   |
   |                   |      |                   | same shaft and    |
   |                   |      |                   | has units of MW x |
   |                   |      |                   | s. For a motor,   |
   |                   |      |                   | it includes the   |
   |                   |      |                   | motor plus its    |
   |                   |      |                   | mechanical load.  |
   |                   |      |                   | Conventional      |
   |                   |      |                   | units are PU on   |
   |                   |      |                   | the generator MVA |
   |                   |      |                   | base, usually     |
   |                   |      |                   | expressed as MW x |
   |                   |      |                   | s / MVA or just   |
   |                   |      |                   | s. This value is  |
   |                   |      |                   | used in the       |
   |                   |      |                   | accelerating      |
   |                   |      |                   | power reference   |
   |                   |      |                   | frame for         |
   |                   |      |                   | operator training |
   |                   |      |                   | simulator         |
   |                   |      |                   | solutions.        |
   |                   |      |                   | Typical value =   |
   |                   |      |                   | 3.                |
   +-------------------+------+-------------------+-------------------+
   | stato             | 1..1 | `PU <#PU>`__      | Stator leakage    |
   | rLeakageReactance |      |                   | reactance (*Xl*)  |
   |                   |      |                   | (>= 0). Typical   |
   |                   |      |                   | value = 0,15.     |
   +-------------------+------+-------------------+-------------------+
   | statorResistance  | 1..1 | `PU <#PU>`__      | Stator (armature) |
   |                   |      |                   | resistance (*Rs*) |
   |                   |      |                   | (>= 0). Typical   |
   |                   |      |                   | value = 0,005.    |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-96

   +---------+------+------------------------+------------------------+
   | mRID    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.mRID>`__ |
   +---------+------+------------------------+------------------------+
   | enabled | 1..1 | `Boolean <#Boolean>`__ | see                    |
   |         |      |                        | `DynamicsFunct         |
   |         |      |                        | ionBlock <#DynamicsFun |
   |         |      |                        | ctionBlock.enabled>`__ |
   +---------+------+------------------------+------------------------+
   | name    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.name>`__ |
   +---------+------+------------------------+------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: ShuntCompensator

   ` <#ShuntCompensator>`__

   .. rubric:: ShuntCompensator
      :name: shuntcompensator
      :class: abstract

   Wires

   A shunt capacitor or reactor or switchable bank of shunt capacitors
   or reactors. A section of a shunt compensator is an individual
   capacitor or reactor. A negative value for bPerSection indicates that
   the compensator is a reactor. ShuntCompensator is a single terminal
   device. Ground is implied.

   .. rubric:: Native Members
      :name: native-members-87

   +----------------+----------------+----------------+----------------+
   | grounded       | 1..1           | `Boo           | Required for   |
   |                |                | lean           | Yn and I       |
   |                |                |  <#Boolean>`__ | connections    |
   |                |                |                | (as            |
   |                |                |                | represented by |
   |                |                |                | Shun           |
   |                |                |                | t              |
   |                |                |                | Compensator.ph |
   |                |                |                | a              |
   |                |                |                | seConnection). |
   |                |                |                | True if the    |
   |                |                |                | neutral is     |
   |                |                |                | solidly        |
   |                |                |                | grounded.      |
   +----------------+----------------+----------------+----------------+
   | m              | 1..1           | `Int           | The maximum    |
   | aximumSections |                | eger           | number of      |
   |                |                |  <#Integer>`__ | sections that  |
   |                |                |                | may be         |
   |                |                |                | switched in.   |
   +----------------+----------------+----------------+----------------+
   | nomU           | 1..1           | `Vol           | The voltage at |
   |                |                | tage           | which the      |
   |                |                |  <#Voltage>`__ | nominal        |
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
   | p              | 0..1           | `PhaseSh       | The type of    |
   | haseConnection |                | u              | phase          |
   |                |                | ntConnectionKi | connection,    |
   |                |                | nd <#Pha       | such as wye or |
   |                |                | seShunt%20Conn | delta.         |
   |                |                | ectionKind>`__ |                |
   +----------------+----------------+----------------+----------------+
   | sections       | 1..1           | `Flo           | Shunt          |
   |                |                | at <#Float>`__ | compensator    |
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
   |                |                |                | For LinearS    |
   |                |                |                | h              |
   |                |                |                | untConpensator |
   |                |                |                | the value      |
   |                |                |                | shall be       |
   |                |                |                | between zero   |
   |                |                |                | and Shu        |
   |                |                |                | n              |
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
   |                |                |                | between Nonl   |
   |                |                |                | i              |
   |                |                |                | nearShuntCompe |
   |                |                |                | n              |
   |                |                |                | storPoint(-s). |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-97

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: SignalDescriptor

   ` <#SignalDescriptor>`__

   .. rubric:: SignalDescriptor
      :name: signaldescriptor
      :class: abstract

   DetailedModelDescription

   Describes the signals both internal signals that connect different
   functions or external signals.

   .. rubric:: Native Members
      :name: native-members-88

   +-------------------+------+-------------------+-------------------+
   | ACDCTerminal      | 0..1 | `ACDCTerminal <   | The terminal for  |
   |                   |      | #ACDCTerminal>`__ | this signal       |
   |                   |      |                   | descriptor.       |
   +-------------------+------+-------------------+-------------------+
   | Dyna              | 0..1 | `DynamicsFunctio  | The dynamics      |
   | micsFunctionBlock |      | nBlock <#Dynamics | function block to |
   |                   |      | FunctionBlock>`__ | which this signal |
   |                   |      |                   | belongs to.       |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-98

   +-------------------+------+-------------------+-------------------+
   | mRID              | 0..1 | `St               | see               |
   |                   |      | ring <#String>`__ | `Detaile          |
   |                   |      |                   | dModelDescriptor  |
   |                   |      |                   | <#DetailedModelDe |
   |                   |      |                   | scriptor.mRID>`__ |
   +-------------------+------+-------------------+-------------------+
   | Detailed          | 0..1 | `Detail           | see               |
   | ModelTypeDynamics |      | edModelTypeDynami | `DetailedMod      |
   |                   |      | cs <#DetailedMode | elDescriptor <#De |
   |                   |      | lTypeDynamics>`__ | tailedModelDescri |
   |                   |      |                   | ptor.DetailedMode |
   |                   |      |                   | lTypeDynamics>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: StateVariable

   ` <#StateVariable>`__

   .. rubric:: StateVariable
      :name: statevariable
      :class: abstract

   StateVariables

   An abstract class for state variables.

.. container:: group
   :name: Switch

   ` <#Switch>`__

   .. rubric:: Switch
      :name: switch
      :class: abstract

   Wires

   A generic device designed to close, or open, or both, one or more
   electric circuits. All switches are two terminal devices including
   grounding switches. The ACDCTerminal.connected at the two sides of
   the switch shall not be considered for assessing switch connectivity,
   i.e. only Switch.open, .normalOpen and .locked are relevant.

   .. rubric:: Inherited Members
      :name: inherited-members-99

   +-------------+------+----------------------+----------------------+
   | BaseVoltage | 0..1 | `BaseVolta           | see                  |
   |             |      | ge <#BaseVoltage>`__ | `ConductingEquipme   |
   |             |      |                      | nt <#ConductingEquip |
   |             |      |                      | ment.BaseVoltage>`__ |
   +-------------+------+----------------------+----------------------+

   +-------------------+------+-------------------+-------------------+
   | inService         | 1..1 | `Bool             | see               |
   |                   |      | ean <#Boolean>`__ | `E                |
   |                   |      |                   | quipment <#Equipm |
   |                   |      |                   | ent.inService>`__ |
   +-------------------+------+-------------------+-------------------+
   | E                 | 1..1 | `Equipment        | see               |
   | quipmentContainer |      | Container <#Equip | `Equipment        |
   |                   |      | mentContainer>`__ | <#Equipment.Equip |
   |                   |      |                   | mentContainer>`__ |
   +-------------------+------+-------------------+-------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: SynchronousMachineDetailed

   ` <#SynchronousMachineDetailed>`__

   .. rubric:: SynchronousMachineDetailed
      :name: synchronousmachinedetailed
      :class: abstract

   SynchronousMachineDynamics

   All synchronous machine detailed types use a subset of the same data
   parameters and input/output variables.

   The several variations differ in the following ways:

   - the number of equivalent windings that are included;

   - the way in which saturation is incorporated into the model;

   - whether or not “subtransient saliency” (*X''q* not = *X''d*) is
   represented.

   It is not necessary for each simulation tool to have separate models
   for each of the model types. The same model can often be used for
   several types by alternative logic within the model. Also,
   differences in saturation representation might not result in
   significant model performance differences so model substitutions are
   often acceptable.

   .. rubric:: Native Members
      :name: native-members-89

   +-------------------+------+-------------------+-------------------+
   | efdBaseRatio      | 1..1 | `                 | Ratio (exciter    |
   |                   |      | Float <#Float>`__ | voltage/generator |
   |                   |      |                   | voltage) of *Efd* |
   |                   |      |                   | bases of exciter  |
   |                   |      |                   | and generator     |
   |                   |      |                   | models (> 0).     |
   |                   |      |                   | Typical value =   |
   |                   |      |                   | 1.                |
   +-------------------+------+-------------------+-------------------+
   | ifdBaseType       | 1..1 | `IfdBaseKind      | Excitation base   |
   |                   |      | <#IfdBaseKind>`__ | system mode. It   |
   |                   |      |                   | should be equal   |
   |                   |      |                   | to the value of   |
   |                   |      |                   | *WLMDV* given by  |
   |                   |      |                   | the user. *WLMDV* |
   |                   |      |                   | is the PU ratio   |
   |                   |      |                   | between the field |
   |                   |      |                   | voltage and the   |
   |                   |      |                   | excitation        |
   |                   |      |                   | current: *Efd* =  |
   |                   |      |                   | *WLMDV* x *Ifd*.  |
   |                   |      |                   | Typical value =   |
   |                   |      |                   | ifag.             |
   +-------------------+------+-------------------+-------------------+
   | saturationFactor  | 1..1 | `                 | Saturation factor |
   |                   |      | Float <#Float>`__ | at rated terminal |
   |                   |      |                   | voltage (*S1*)    |
   |                   |      |                   | (>= 0). Defined   |
   |                   |      |                   | by defined by     |
   |                   |      |                   | *S*\ (*E1*) in    |
   |                   |      |                   | the               |
   |                   |      |                   | Sync              |
   |                   |      |                   | hronousMachineSat |
   |                   |      |                   | urationParameters |
   |                   |      |                   | diagram. Typical  |
   |                   |      |                   | value = 0,02.     |
   +-------------------+------+-------------------+-------------------+
   | sa                | 1..1 | `                 | Saturation factor |
   | turationFactor120 |      | Float <#Float>`__ | at 120 % of rated |
   |                   |      |                   | terminal voltage  |
   |                   |      |                   | (*S12*) (>=       |
   |                   |      |                   | Rotating          |
   |                   |      |                   | MachineDynamics.s |
   |                   |      |                   | aturationFactor). |
   |                   |      |                   | Defined by        |
   |                   |      |                   | *S*\ (*E2*) in    |
   |                   |      |                   | the               |
   |                   |      |                   | Sync              |
   |                   |      |                   | hronousMachineSat |
   |                   |      |                   | urationParameters |
   |                   |      |                   | diagram. Typical  |
   |                   |      |                   | value = 0,12.     |
   +-------------------+------+-------------------+-------------------+
   | saturat           | 1..1 | `                 | Quadrature-axis   |
   | ionFactor120QAxis |      | Float <#Float>`__ | saturation factor |
   |                   |      |                   | at 120% of rated  |
   |                   |      |                   | terminal voltage  |
   |                   |      |                   | (*S12q*) (>=      |
   |                   |      |                   | SynchonousMachi   |
   |                   |      |                   | neDetailed.satura |
   |                   |      |                   | tionFactorQAxis). |
   |                   |      |                   | Typical value =   |
   |                   |      |                   | 0,12.             |
   +-------------------+------+-------------------+-------------------+
   | satu              | 1..1 | `                 | Quadrature-axis   |
   | rationFactorQAxis |      | Float <#Float>`__ | saturation factor |
   |                   |      |                   | at rated terminal |
   |                   |      |                   | voltage (*S1q*)   |
   |                   |      |                   | (>= 0). Typical   |
   |                   |      |                   | value = 0,02.     |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-100

   +-------------------+------+-------------------+-------------------+
   | S                 | 0..1 | `Synchrono        | see               |
   | ynchronousMachine |      | usMachine <#Synch | `Synchronou       |
   |                   |      | ronousMachine>`__ | sMachineDynamics  |
   |                   |      |                   | <#SynchronousMach |
   |                   |      |                   | ineDynamics.Synch |
   |                   |      |                   | ronousMachine>`__ |
   +-------------------+------+-------------------+-------------------+

   +-------------------+------+-------------------+-------------------+
   | damping           | 1..1 | `                 | see               |
   |                   |      | Float <#Float>`__ | `RotatingMa       |
   |                   |      |                   | chineDynamics <#R |
   |                   |      |                   | otatingMachineDyn |
   |                   |      |                   | amics.damping>`__ |
   +-------------------+------+-------------------+-------------------+
   | inertia           | 1..1 | `Seco             | see               |
   |                   |      | nds <#Seconds>`__ | `RotatingMa       |
   |                   |      |                   | chineDynamics <#R |
   |                   |      |                   | otatingMachineDyn |
   |                   |      |                   | amics.inertia>`__ |
   +-------------------+------+-------------------+-------------------+
   | stato             | 1..1 | `PU <#PU>`__      | see               |
   | rLeakageReactance |      |                   | `Rotating         |
   |                   |      |                   | MachineDynamics < |
   |                   |      |                   | #RotatingMachineD |
   |                   |      |                   | ynamics.statorLea |
   |                   |      |                   | kageReactance>`__ |
   +-------------------+------+-------------------+-------------------+
   | statorResistance  | 1..1 | `PU <#PU>`__      | see               |
   |                   |      |                   | `Ro               |
   |                   |      |                   | tatingMachineDyna |
   |                   |      |                   | mics <#RotatingMa |
   |                   |      |                   | chineDynamics.sta |
   |                   |      |                   | torResistance>`__ |
   +-------------------+------+-------------------+-------------------+

   +---------+------+------------------------+------------------------+
   | mRID    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.mRID>`__ |
   +---------+------+------------------------+------------------------+
   | enabled | 1..1 | `Boolean <#Boolean>`__ | see                    |
   |         |      |                        | `DynamicsFunct         |
   |         |      |                        | ionBlock <#DynamicsFun |
   |         |      |                        | ctionBlock.enabled>`__ |
   +---------+------+------------------------+------------------------+
   | name    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.name>`__ |
   +---------+------+------------------------+------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: SynchronousMachineDynamics

   ` <#SynchronousMachineDynamics>`__

   .. rubric:: SynchronousMachineDynamics
      :name: synchronousmachinedynamics
      :class: abstract

   SynchronousMachineDynamics

   Synchronous machine whose behaviour is described by reference to a
   standard model expressed in one of the following forms:

   - simplified (or classical), where a group of generators or motors is
   not modelled in detail;

   - detailed, in equivalent circuit form;

   - detailed, in time constant reactance form; or

   - by definition of a user-defined model.

   It is a common practice to represent small generators by a negative
   load rather than by a dynamic generator model when performing
   dynamics simulations. In this case, a SynchronousMachine in the
   static model is not represented by anything in the dynamics model,
   instead it is treated as an ordinary load.

   Parameter details:

   1. Synchronous machine parameters such as *Xl, Xd, Xp* etc. are
      actually used as inductances in the models, but are commonly
      referred to as reactances since, at nominal frequency, the PU
      values are the same. However, some references use the symbol *L*
      instead of *X*.

   .. rubric:: Native Members
      :name: native-members-90

   +-------------------+------+-------------------+-------------------+
   | S                 | 0..1 | `Synchrono        | Synchronous       |
   | ynchronousMachine |      | usMachine <#Synch | machine to which  |
   |                   |      | ronousMachine>`__ | synchronous       |
   |                   |      |                   | machine dynamics  |
   |                   |      |                   | model applies.    |
   +-------------------+------+-------------------+-------------------+

   .. rubric:: Inherited Members
      :name: inherited-members-101

   +-------------------+------+-------------------+-------------------+
   | damping           | 1..1 | `                 | see               |
   |                   |      | Float <#Float>`__ | `RotatingMa       |
   |                   |      |                   | chineDynamics <#R |
   |                   |      |                   | otatingMachineDyn |
   |                   |      |                   | amics.damping>`__ |
   +-------------------+------+-------------------+-------------------+
   | inertia           | 1..1 | `Seco             | see               |
   |                   |      | nds <#Seconds>`__ | `RotatingMa       |
   |                   |      |                   | chineDynamics <#R |
   |                   |      |                   | otatingMachineDyn |
   |                   |      |                   | amics.inertia>`__ |
   +-------------------+------+-------------------+-------------------+
   | stato             | 1..1 | `PU <#PU>`__      | see               |
   | rLeakageReactance |      |                   | `Rotating         |
   |                   |      |                   | MachineDynamics < |
   |                   |      |                   | #RotatingMachineD |
   |                   |      |                   | ynamics.statorLea |
   |                   |      |                   | kageReactance>`__ |
   +-------------------+------+-------------------+-------------------+
   | statorResistance  | 1..1 | `PU <#PU>`__      | see               |
   |                   |      |                   | `Ro               |
   |                   |      |                   | tatingMachineDyna |
   |                   |      |                   | mics <#RotatingMa |
   |                   |      |                   | chineDynamics.sta |
   |                   |      |                   | torResistance>`__ |
   +-------------------+------+-------------------+-------------------+

   +---------+------+------------------------+------------------------+
   | mRID    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.mRID>`__ |
   +---------+------+------------------------+------------------------+
   | enabled | 1..1 | `Boolean <#Boolean>`__ | see                    |
   |         |      |                        | `DynamicsFunct         |
   |         |      |                        | ionBlock <#DynamicsFun |
   |         |      |                        | ctionBlock.enabled>`__ |
   +---------+------+------------------------+------------------------+
   | name    | 1..1 | `String <#String>`__   | see                    |
   |         |      |                        | `DynamicsFu            |
   |         |      |                        | nctionBlock <#Dynamics |
   |         |      |                        | FunctionBlock.name>`__ |
   +---------+------+------------------------+------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: TapChanger

   ` <#TapChanger>`__

   .. rubric:: TapChanger
      :name: tapchanger
      :class: abstract

   Wires

   Mechanism for changing transformer winding tap positions.

   .. rubric:: Native Members
      :name: native-members-91

   +----------------+----------------+----------------+----------------+
   | highStep       | 0..1           | `Int           | Highest        |
   |                |                | eger           | possible tap   |
   |                |                |  <#Integer>`__ | step position, |
   |                |                |                | advance from   |
   |                |                |                | neutral.       |
   |                |                |                |                |
   |                |                |                | The attribute  |
   |                |                |                | shall be       |
   |                |                |                | greater than   |
   |                |                |                | lowStep.       |
   +----------------+----------------+----------------+----------------+
   | lowStep        | 0..1           | `Int           | Lowest         |
   |                |                | eger           | possible tap   |
   |                |                |  <#Integer>`__ | step position, |
   |                |                |                | retard from    |
   |                |                |                | neutral.       |
   +----------------+----------------+----------------+----------------+
   | neutralStep    | 0..1           | `Int           | The neutral    |
   |                |                | eger           | tap step       |
   |                |                |  <#Integer>`__ | position for   |
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
   | neutralU       | 0..1           | `Vol           | Voltage at     |
   |                |                | tage           | which the      |
   |                |                |  <#Voltage>`__ | winding        |
   |                |                |                | operates at    |
   |                |                |                | the neutral    |
   |                |                |                | tap setting.   |
   |                |                |                | It is the      |
   |                |                |                | voltage at the |
   |                |                |                | terminal of    |
   |                |                |                | the Powe       |
   |                |                |                | r              |
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
   |                |                |                | of the Power   |
   |                |                |                | T              |
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
   |                |                |                | PhaseTapCha    |
   |                |                |                | n              |
   |                |                |                | gerSymmetrical |
   |                |                |                | and PhaseTa    |
   |                |                |                | p              |
   |                |                |                | ChangerLinear. |
   +----------------+----------------+----------------+----------------+
   | normalStep     | 0..1           | `Int           | The tap step   |
   |                |                | eger           | position used  |
   |                |                |  <#Integer>`__ | in "normal"    |
   |                |                |                | network        |
   |                |                |                | operation for  |
   |                |                |                | this winding.  |
   |                |                |                | For a "Fixed"  |
   |                |                |                | tap changer    |
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
   | step           | 1..1           | `Flo           | Tap changer    |
   |                |                | at <#Float>`__ | position.      |
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

   .. rubric:: Inherited Members
      :name: inherited-members-102

   +------+------+----------------------+--------------------------+
   | mRID | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 1..1 | `String <#String>`__ | see                      |
   |      |      |                      | `Po                      |
   |      |      |                      | werSystemResource <#Powe |
   |      |      |                      | rSystemResource.name>`__ |
   +------+------+----------------------+--------------------------+

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

.. container:: group
   :name: TransformerEnd

   ` <#TransformerEnd>`__

   .. rubric:: TransformerEnd
      :name: transformerend
      :class: abstract

   Wires

   A conducting connection point of a power transformer. It corresponds
   to a physical transformer winding terminal. In earlier CIM versions,
   the TransformerWinding class served a similar purpose, but this class
   is more flexible because it associates to terminal but is not a
   specialization of ConductingEquipment.

   .. rubric:: Native Members
      :name: native-members-92

   +----------------+----------------+----------------+----------------+
   | mRID           | 1..1           | `S             | Master         |
   |                |                | trin           | resource       |
   |                |                | g <#String>`__ | identifier     |
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
   | endNumber      | 1..1           | `Int           | Number for     |
   |                |                | eger           | this           |
   |                |                |  <#Integer>`__ | transformer    |
   |                |                |                | end,           |
   |                |                |                | corresponding  |
   |                |                |                | to the end's   |
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
   | grounded       | 1..1           | `Boo           | Used only for  |
   |                |                | lean           | Yn and Zn      |
   |                |                |  <#Boolean>`__ | connections    |
   |                |                |                | indicated by   |
   |                |                |                | Power          |
   |                |                |                | T              |
   |                |                |                | ransformerEnd. |
   |                |                |                | c              |
   |                |                |                | onnectionKind. |
   |                |                |                | If true, the   |
   |                |                |                | neutral is     |
   |                |                |                | grounded and   |
   |                |                |                | attributes     |
   |                |                |                | Transfo        |
   |                |                |                | r              |
   |                |                |                | merEnd.rground |
   |                |                |                | and Transfo    |
   |                |                |                | r              |
   |                |                |                | merEnd.xground |
   |                |                |                | are required.  |
   |                |                |                | If false, the  |
   |                |                |                | attributes     |
   |                |                |                | Transfo        |
   |                |                |                | r              |
   |                |                |                | merEnd.rground |
   |                |                |                | and Transfo    |
   |                |                |                | r              |
   |                |                |                | merEnd.xground |
   |                |                |                | are not        |
   |                |                |                | considered.    |
   +----------------+----------------+----------------+----------------+
   | name           | 1..1           | `S             | The name is    |
   |                |                | trin           | any free human |
   |                |                | g <#String>`__ | readable and   |
   |                |                |                | possibly non   |
   |                |                |                | unique text    |
   |                |                |                | naming the     |
   |                |                |                | object.        |
   +----------------+----------------+----------------+----------------+
   | rground        | 1..1           | `Resistanc     | Resistance     |
   |                |                | e <#           | part of        |
   |                |                | Resistance>`__ | neutral        |
   |                |                |                | impedance.     |
   |                |                |                | Zero indicates |
   |                |                |                | solidly        |
   |                |                |                | grounded or    |
   |                |                |                | grounded       |
   |                |                |                | through a      |
   |                |                |                | reactor.       |
   +----------------+----------------+----------------+----------------+
   | xground        | 1..1           | `Reactan       | Reactance part |
   |                |                | ce <           | of neutral     |
   |                |                | #Reactance>`__ | impedance.     |
   |                |                |                | Zero indicates |
   |                |                |                | solidly        |
   |                |                |                | grounded or    |
   |                |                |                | grounded       |
   |                |                |                | through a      |
   |                |                |                | reactor.       |
   +----------------+----------------+----------------+----------------+
   | BaseVoltage    | 1..1           | `B             | Base voltage   |
   |                |                | aseVoltage <#B | of the         |
   |                |                | aseVoltage>`__ | transformer    |
   |                |                |                | end. This is   |
   |                |                |                | essential for  |
   |                |                |                | PU             |
   |                |                |                | calculation.   |
   +----------------+----------------+----------------+----------------+
   | Terminal       | 1..1           | `Termi         | Terminal of    |
   |                |                | nal            | the power      |
   |                |                | <#Terminal>`__ | transformer to |
   |                |                |                | which this     |
   |                |                |                | transformer    |
   |                |                |                | end belongs.   |
   +----------------+----------------+----------------+----------------+

   .. rubric:: Inherited Members
      :name: inherited-members-103

   +------+------+----------------------+--------------------------+
   | mRID | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.mRID>`__ |
   +------+------+----------------------+--------------------------+
   | name | 0..1 | `String <#String>`__ | see                      |
   |      |      |                      | `IdentifiedObject <#I    |
   |      |      |                      | dentifiedObject.name>`__ |
   +------+------+----------------------+--------------------------+

Enumerations
============

.. container:: group
   :name: AsynchronousMachineKind

   ` <#AsynchronousMachineKind>`__

   .. rubric:: AsynchronousMachineKind
      :name: asynchronousmachinekind
      :class: enumerated

   Wires

   Kind of Asynchronous Machine.

   ========= ========================================
   generator The Asynchronous Machine is a generator.
   motor     The Asynchronous Machine is a motor.
   ========= ========================================

.. container:: group
   :name: BatteryStateKind

   ` <#BatteryStateKind>`__

   .. rubric:: BatteryStateKind
      :name: batterystatekind
      :class: enumerated

   Production

   The state of the battery unit.

   ===========
   charging    
   discharging 
   empty       
   full        
   waiting     
   ===========

.. container:: group
   :name: CsOperatingModeKind

   ` <#CsOperatingModeKind>`__

   .. rubric:: CsOperatingModeKind
      :name: csoperatingmodekind
      :class: enumerated

   DC

   Operating mode for DC line operating as Current Source Converter.

   ========= ========================================================
   inverter  Operating as inverter, which is the power receiving end.
   rectifier Operating as rectifier, which is the power sending end.
   ========= ========================================================

.. container:: group
   :name: CsPpccControlKind

   ` <#CsPpccControlKind>`__

   .. rubric:: CsPpccControlKind
      :name: csppcccontrolkind
      :class: enumerated

   DC

   Active power control modes for DC line operating as Current Source
   Converter.

   +-------------+-------------------------------------------------------+
   | activePower | Control is active power control at AC side, at point  |
   |             | of common coupling. Target is provided by             |
   |             | ACDCConverter.targetPpcc.                             |
   +-------------+-------------------------------------------------------+
   | dcCurrent   | Control is DC current with target value provided by   |
   |             | CsConverter.targetIdc.                                |
   +-------------+-------------------------------------------------------+
   | dcVoltage   | Control is DC voltage with target value provided by   |
   |             | ACDCConverter.targetUdc.                              |
   +-------------+-------------------------------------------------------+

.. container:: group
   :name: CurveStyle

   ` <#CurveStyle>`__

   .. rubric:: CurveStyle
      :name: curvestyle
      :class: enumerated

   Core

   Style or shape of curve.

   ===================
   constantYValue      
   straightLineYValues 
   ===================

.. container:: group
   :name: DCPolarityKind

   ` <#DCPolarityKind>`__

   .. rubric:: DCPolarityKind
      :name: dcpolaritykind
      :class: enumerated

   DC

   Polarity for DC circuits.

   +----------+----------------------------------------------------------+
   | middle   | Middle pole. The converter terminal is the midpoint in a |
   |          | bipolar or symmetric monopole configuration. The         |
   |          | midpoint can be grounded and/or have a metallic return.  |
   +----------+----------------------------------------------------------+
   | negative | Negative pole. The converter terminal is intended to     |
   |          | operate at a negative voltage relative the midpoint or   |
   |          | positive terminal.                                       |
   +----------+----------------------------------------------------------+
   | positive | Positive pole. The converter terminal is intended to     |
   |          | operate at a positive voltage relative the midpoint or   |
   |          | negative terminal.                                       |
   +----------+----------------------------------------------------------+

.. container:: group
   :name: DCSourceKind

   ` <#DCSourceKind>`__

   .. rubric:: DCSourceKind
      :name: dcsourcekind
      :class: enumerated

   Emtiop

   +--------------+------------------------------------------------------+
   | battery      | Represent the DCEnergySource with a nonlinear        |
   |              | battery model, which should respond to               |
   |              | state-of-charge (SoC) controls.                      |
   +--------------+------------------------------------------------------+
   | load         | For electronic loads. Passive loads can be           |
   |              | represented in DCShunt.                              |
   +--------------+------------------------------------------------------+
   | photoVoltaic | Represent the DCEnergySource with a nonlinear PV     |
   |              | panel model, which should respond to maximum power   |
   |              | point tracking (MPPT) control                        |
   +--------------+------------------------------------------------------+

.. container:: group
   :name: DCTerminalPolarityKind

   ` <#DCTerminalPolarityKind>`__

   .. rubric:: DCTerminalPolarityKind
      :name: dcterminalpolaritykind
      :class: enumerated

   DC

   Polarity for DC terminal. Used in DC system configurations that have
   explicit polarity of the terminals, e.g., voltage source converter
   (VSC) technology.

   ======== ==================
   negative Negative terminal.
   positive Positive terminal.
   ======== ==================

.. container:: group
   :name: IEEECigreAPIInputKind

   ` <#IEEECigreAPIInputKind>`__

   .. rubric:: IEEECigreAPIInputKind
      :name: ieeecigreapiinputkind
      :class: enumerated

   Emtiop

   +------------------------+--------------------------------------------+
   | acCurrent              | AC current from inverter into the AC       |
   |                        | filter. Requires the phase attribute.      |
   |                        | Typically in Amperes, but the CIGRE TB 958 |
   |                        | API should be used to verify units.        |
   +------------------------+--------------------------------------------+
   | acCurrentGrid          | AC current from AC filter into the grid.   |
   |                        | Requires the phase attribute. Typically in |
   |                        | Amperes, but the CIGRE TB 958 API should   |
   |                        | be used to verify units.                   |
   +------------------------+--------------------------------------------+
   | acVoltage              | AC voltage at the filter-to-grid           |
   |                        | connection point. Requires the phase       |
   |                        | attribute. Typically in Volts, but the     |
   |                        | CIGRE TB 958 API should be used to verify  |
   |                        | units.                                     |
   +------------------------+--------------------------------------------+
   | activePowerReference   | Active power control reference. Typically  |
   |                        | in per-unit but the CIGRE TB 958 API       |
   |                        | should be used to verify units.            |
   +------------------------+--------------------------------------------+
   | apiDefined             | Another kind of input or control signal    |
   |                        | not enumerated in CIM. Use the CIGRE TB    |
   |                        | 958 API for more information.              |
   +------------------------+--------------------------------------------+
   | dcCurrent              | DC current into the inverter stage, if DC  |
   |                        | bus modeling applies. Typically in         |
   |                        | Amperes, but the DLL API should be used to |
   |                        | verify units.                              |
   +------------------------+--------------------------------------------+
   | dcMPPTVoltage          | DC voltage command from the maximum power  |
   |                        | point tracking system, if DC bus modeling  |
   |                        | applies. Typically in Volts, but the DLL   |
   |                        | API should be used to verify units.        |
   +------------------------+--------------------------------------------+
   | dcVoltage              | DC voltage at the inverter stage, if DC    |
   |                        | bus modeling applies. Typically in Volts,  |
   |                        | but the CIGRE TB 958 API should be used to |
   |                        | verify units.                              |
   +------------------------+--------------------------------------------+
   | reactivePowerReference | Reactive power control reference.          |
   |                        | Typically in per-unit but the CIGRE TB 958 |
   |                        | API should be used to verify units.        |
   +------------------------+--------------------------------------------+
   | voltageReference       | Voltage control reference. Typically in    |
   |                        | per-unit and positive sequence, but the    |
   |                        | CIGRE TB 958 API should be used to verify  |
   |                        | units.                                     |
   +------------------------+--------------------------------------------+

.. container:: group
   :name: IEEECigreAPIModeKind

   ` <#IEEECigreAPIModeKind>`__

   .. rubric:: IEEECigreAPIModeKind
      :name: ieeecigreapimodekind
      :class: enumerated

   Emtiop

   +--------------+------------------------------------------------------+
   | SupportsBoth | The CIGRE TB 958 model runs in either EMT or RMS     |
   |              | simulations.                                         |
   +--------------+------------------------------------------------------+
   | SupportsEMT  | The CIGRE TB 958 model runs in EMT but not RMS       |
   |              | simulations.                                         |
   +--------------+------------------------------------------------------+
   | SupportsNone | This CIGRE TB 958 model is unusable.                 |
   +--------------+------------------------------------------------------+
   | SupportsRMS  | The CIGRE TB 958 model runs in RMS simulation, e.g., |
   |              | power flow, short-circuit, positive sequence         |
   |              | dynamics, transient stability. It does not run in    |
   |              | EMT simulation.                                      |
   +--------------+------------------------------------------------------+

.. container:: group
   :name: IEEECigreAPIOutputKind

   ` <#IEEECigreAPIOutputKind>`__

   .. rubric:: IEEECigreAPIOutputKind
      :name: ieeecigreapioutputkind
      :class: enumerated

   Emtiop

   +-----------------+---------------------------------------------------+
   | activePower     | Active power from internal calculation; a         |
   |                 | convenience output.                               |
   +-----------------+---------------------------------------------------+
   | apiDefined      | Typically a convenience output for plotting and   |
   |                 | analysis. Use CIGRE TB 958 API for more           |
   |                 | information.                                      |
   +-----------------+---------------------------------------------------+
   | modulationIndex | Modulation index for PWM switching in a detailed  |
   |                 | VSC model. May be scaled by Vdc/2 in an average   |
   |                 | model. Requires the phase attribute. If these     |
   |                 | outputs are not provided, then vscVoltage outputs |
   |                 | shall be provided.                                |
   +-----------------+---------------------------------------------------+
   | pllFrequency    | Frequency estimated from the model's phase locked |
   |                 | loop or similar algorithm.                        |
   +-----------------+---------------------------------------------------+
   | reactivePower   | Reactive power from internal calculation; a       |
   |                 | convenience output.                               |
   +-----------------+---------------------------------------------------+
   | rideThroughMode | A flag indicating fault-ride-through mode is      |
   |                 | active, based on logic internal to the model.     |
   +-----------------+---------------------------------------------------+
   | vscVoltage      | VSC source voltage for an average model. Requires |
   |                 | the phase attribute. If these outputs are not     |
   |                 | provided then modulationIndex outputs shall be    |
   |                 | provided.                                         |
   +-----------------+---------------------------------------------------+

.. container:: group
   :name: IEEECigreAPIParameterKind

   ` <#IEEECigreAPIParameterKind>`__

   .. rubric:: IEEECigreAPIParameterKind
      :name: ieeecigreapiparameterkind
      :class: enumerated

   Emtiop

   Indicates the type and size (bytes) of a parameter, as documented in
   IEEE_Cigre_DLLInterface_types.h from CIGRE TB 958.

   ==========
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
   ==========

.. container:: group
   :name: IfdBaseKind

   ` <#IfdBaseKind>`__

   .. rubric:: IfdBaseKind
      :name: ifdbasekind
      :class: enumerated

   SynchronousMachineDynamics

   Excitation base system mode.

   ====
   ifag 
   iffl 
   ifnl 
   ====

.. container:: group
   :name: InputSignalKind

   ` <#InputSignalKind>`__

   .. rubric:: InputSignalKind
      :name: inputsignalkind
      :class: enumerated

   PowerSystemStabilizerDynamics

   Types of input signals. In dynamics modelling, commonly represented
   by the *j* parameter.

   ==============================
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
   ==============================

.. container:: group
   :name: LimitKind

   ` <#LimitKind>`__

   .. rubric:: LimitKind
      :name: limitkind
      :class: enumerated

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
   |                                   | -  as a fixed percentage of the   |
   |                                   |    PATL for a given time (for     |
   |                                   |    example, 115% of the PATL that |
   |                                   |    can be accepted during 15      |
   |                                   |    minutes),                      |
   |                                   |                                   |
   |                                   | .. raw:: html                     |
   |                                   |                                   |
   |                                   |    <!-- -->                       |
   |                                   |                                   |
   |                                   | -  pairs of TATL type and         |
   |                                   |    Duration calculated for each   |
   |                                   |    line taking into account its   |
   |                                   |    particular configuration and   |
   |                                   |    conditions of functioning (for |
   |                                   |    example, it can define a TATL  |
   |                                   |    acceptable during 20 minutes   |
   |                                   |    and another one acceptable     |
   |                                   |    during 10 minutes).            |
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

.. container:: group
   :name: NthAmModelKind

   ` <#NthAmModelKind>`__

   .. rubric:: NthAmModelKind
      :name: nthammodelkind
      :class: enumerated

   Emtiop

   Application of this model.

   =======================
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
   =======================

.. container:: group
   :name: NthAmModelNameKind

   ` <#NthAmModelNameKind>`__

   .. rubric:: NthAmModelNameKind
      :name: nthammodelnamekind
      :class: enumerated

   Emtiop

   Describes the naming category for dynamic models recognized by NERC.

   =====
   AUX   
   DGS   
   DYD   
   DYR   
   Other 
   =====

.. container:: group
   :name: NthAmModelStatusKind

   ` <#NthAmModelStatusKind>`__

   .. rubric:: NthAmModelStatusKind
      :name: nthammodelstatuskind
      :class: enumerated

   Emtiop

   +------------+--------------------------------------------------------+
   | allowed    | NERC allows this model for interconnection-wide        |
   |            | studies. NERC used to keep a list of allowed models;   |
   |            | currently, it lists only prohibited models.            |
   +------------+--------------------------------------------------------+
   | deprecated | NERC allows this model in interconnection-wide         |
   |            | studies, but other models are more suitable.           |
   +------------+--------------------------------------------------------+
   | prohibited | NERC prohibits use of this model in                    |
   |            | interconnection-side studies. Some legacy network      |
   |            | examples may still use this model.                     |
   +------------+--------------------------------------------------------+

.. container:: group
   :name: OperationalLimitDirectionKind

   ` <#OperationalLimitDirectionKind>`__

   .. rubric:: OperationalLimitDirectionKind
      :name: operationallimitdirectionkind
      :class: enumerated

   OperationalLimits

   The direction attribute describes the side of a limit that is a
   violation.

   +---------------+-----------------------------------------------------+
   | absoluteValue | An absoluteValue limit means that a monitored       |
   |               | absolute value above the limit value is a           |
   |               | violation.                                          |
   +---------------+-----------------------------------------------------+
   | high          | High means that a monitored value above the limit   |
   |               | value is a violation. If applied to a terminal      |
   |               | flow, the positive direction is into the terminal.  |
   +---------------+-----------------------------------------------------+
   | low           | Low means a monitored value below the limit is a    |
   |               | violation. If applied to a terminal flow, the       |
   |               | positive direction is into the terminal.            |
   +---------------+-----------------------------------------------------+

.. container:: group
   :name: PhaseShuntConnectionKind

   ` <#PhaseShuntConnectionKind>`__

   .. rubric:: PhaseShuntConnectionKind
      :name: phaseshuntconnectionkind
      :class: enumerated

   Wires

   The configuration of phase connections for a single terminal device
   such as a load or capacitor.

   +----+----------------------------------------------------------------+
   | D  | Delta connection.                                              |
   +----+----------------------------------------------------------------+
   | G  | Ground connection; use when explicit connection to ground      |
   |    | needs to be expressed in combination with the phase code, such |
   |    | as for electrical wire/cable or for meters.                    |
   +----+----------------------------------------------------------------+
   | I  | Independent winding, for single-phase connections.             |
   +----+----------------------------------------------------------------+
   | Y  | Wye connection.                                                |
   +----+----------------------------------------------------------------+
   | Yn | Wye, with neutral brought out for grounding.                   |
   +----+----------------------------------------------------------------+

.. container:: group
   :name: RotorKind

   ` <#RotorKind>`__

   .. rubric:: RotorKind
      :name: rotorkind
      :class: enumerated

   SynchronousMachineDynamics

   Type of rotor on physical machine.

   ===========
   roundRotor  
   salientPole 
   ===========

.. container:: group
   :name: SVCControlMode

   ` <#SVCControlMode>`__

   .. rubric:: SVCControlMode
      :name: svccontrolmode
      :class: enumerated

   Wires

   Static VAr Compensator control mode.

   ============= =======================
   reactivePower Reactive power control.
   voltage       Voltage control.
   ============= =======================

.. container:: group
   :name: SinglePhaseKind

   ` <#SinglePhaseKind>`__

   .. rubric:: SinglePhaseKind
      :name: singlephasekind
      :class: enumerated

   Wires

   Enumeration of phase identifiers used to designate the specific phase
   of conducting equipment modelled as individual unbalanced phases.

   Allows designation of specific phases for transmission and
   distribution equipment, circuits and loads.

   == ==================
   A  Phase A.
   B  Phase B.
   C  Phase C.
   N  Neutral.
   s1 Secondary phase 1.
   s2 Secondary phase 2.
   == ==================

.. container:: group
   :name: SynchronousMachineKind

   ` <#SynchronousMachineKind>`__

   .. rubric:: SynchronousMachineKind
      :name: synchronousmachinekind
      :class: enumerated

   Wires

   Synchronous machine type.

   ===========================
   condenser                   
   generator                   
   generatorOrCondenser        
   generatorOrCondenserOrMotor 
   generatorOrMotor            
   motor                       
   motorOrCondenser            
   ===========================

.. container:: group
   :name: SynchronousMachineModelKind

   ` <#SynchronousMachineModelKind>`__

   .. rubric:: SynchronousMachineModelKind
      :name: synchronousmachinemodelkind
      :class: enumerated

   SynchronousMachineDynamics

   Type of synchronous machine model used in dynamic simulation
   applications.

   ================================
   subtransient                     
   subtransientSimplified           
   subtransientSimplifiedDirectAxis 
   subtransientTypeF                
   subtransientTypeJ                
   ================================

.. container:: group
   :name: SynchronousMachineOperatingMode

   ` <#SynchronousMachineOperatingMode>`__

   .. rubric:: SynchronousMachineOperatingMode
      :name: synchronousmachineoperatingmode
      :class: enumerated

   Wires

   Synchronous machine operating mode.

   =========
   condenser 
   generator 
   motor     
   =========

.. container:: group
   :name: UnitMultiplier

   ` <#UnitMultiplier>`__

   .. rubric:: UnitMultiplier
      :name: unitmultiplier
      :class: enumerated

   Domain

   The unit multipliers defined for the CIM. When applied to unit
   symbols, the unit symbol is treated as a derived unit. Regardless of
   the contents of the unit symbol text, the unit symbol shall be
   treated as if it were a single-character unit symbol. Unit symbols
   should not contain multipliers, and it should be left to the
   multiplier to define the multiple for an entire data type.

   For example, if a unit symbol is "m2Pers" and the multiplier is "k",
   then the value is k(m**2/s), and the multiplier applies to the entire
   final value, not to any individual part of the value. This can be
   conceptualized by substituting a derived unit symbol for the unit
   type. If one imagines that the symbol "Þ" represents the derived unit
   "m2Pers", then applying the multiplier "k" can be conceptualized
   simply as "kÞ".

   For example, the SI unit for mass is "kg" and not "g". If the unit
   symbol is defined as "kg", then the multiplier is applied to "kg" as
   a whole and does not replace the "k" in front of the "g". In this
   case, the multiplier of "m" would be used with the unit symbol of
   "kg" to represent one gram. As a text string, this violates the
   instructions in IEC 80000-1. However, because the unit symbol in CIM
   is treated as a derived unit instead of as an SI unit, it makes more
   sense to conceptualize the "kg" as if it were replaced by one of the
   proposed replacements for the SI mass symbol. If one imagines that
   the "kg" were replaced by a symbol "Þ", then it is easier to
   conceptualize the multiplier "m" as creating the proper unit "mÞ",
   and not the forbidden unit "mkg".

   =====
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
   =====

.. container:: group
   :name: UnitSymbol

   ` <#UnitSymbol>`__

   .. rubric:: UnitSymbol
      :name: unitsymbol
      :class: enumerated

   Domain

   The derived units defined for usage in the CIM. In some cases, the
   derived unit is equal to an SI unit. Whenever possible, the standard
   derived symbol is used instead of the formula for the derived unit.
   For example, the unit symbol Farad is defined as "F" instead of
   "CPerV". In cases where a standard symbol does not exist for a
   derived unit, the formula for the unit is used as the unit symbol.
   For example, density does not have a standard symbol and so it is
   represented as "kgPerm^3". With the exception of the "kg", which is
   an SI unit, the unit symbols do not contain multipliers and therefore
   represent the base derived unit to which a multiplier can be applied
   as a whole.

   Every unit symbol is treated as an unparseable text as if it were a
   single-letter symbol. The meaning of each unit symbol is defined by
   the accompanying descriptive text and not by the text contents of the
   unit symbol.

   To allow the widest possible range of serializations without
   requiring special character handling, several substitutions are made
   which deviate from the format described in IEC 80000-1. The division
   symbol "/" is replaced by the letters "Per". Exponents are written in
   plain text after the unit as "m^3". The letters "deg" are used
   instead of the degree symbol. Any clarification of the meaning for a
   substitution is included in the description for the unit symbol.

   Non-SI units are included in list of unit symbols to allow sources of
   data to be correctly labelled with their non-SI units (for example, a
   GPS sensor that is reporting numbers that represent feet instead of
   meters). This allows software to use the unit symbol information
   correctly convert and scale the raw data of those sources into
   SI-based units.

   The integer values are used for harmonization with IEC 61850.

   ===============
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
   ===============

.. container:: group
   :name: VsPpccControlKind

   ` <#VsPpccControlKind>`__

   .. rubric:: VsPpccControlKind
      :name: vsppcccontrolkind
      :class: enumerated

   DC

   Types applicable to the control of real power and/or DC voltage by
   voltage source converter.

   +---------------------------------+-----------------------------------+
   | pPcc                            | Control is real power at point of |
   |                                 | common coupling. The target value |
   |                                 | is provided by                    |
   |                                 | ACDCConverter.targetPpcc.         |
   +---------------------------------+-----------------------------------+
   | pPccAndUdcDroop                 | Control is active power at point  |
   |                                 | of common coupling and local DC   |
   |                                 | voltage, with the droop. Target   |
   |                                 | values are provided by            |
   |                                 | ACDCConverter.targetPpcc,         |
   |                                 | ACDCConverter.targetUdc and       |
   |                                 | VsConverter.droop.                |
   +---------------------------------+-----------------------------------+
   | pPccAndUdcDroopPilot            | Control is active power at point  |
   |                                 | of common coupling and the pilot  |
   |                                 | DC voltage, with the droop. The   |
   |                                 | mode is used for Multi Terminal   |
   |                                 | DC (MTDC) systems where multiple  |
   |                                 | DC substations are connected to   |
   |                                 | the DC transmission lines. The    |
   |                                 | pilot voltage is then used to     |
   |                                 | coordinate the control the DC     |
   |                                 | voltage across the DC             |
   |                                 | substations. Targets are provided |
   |                                 | by ACDCConverter.targetPpcc,      |
   |                                 | ACDCConverter.targetUdc and       |
   |                                 | VsConverter.droop.                |
   +---------------------------------+-----------------------------------+
   | pPccAndUdcDroopWithCompensation | Control is active power at point  |
   |                                 | of common coupling and            |
   |                                 | compensated DC voltage, with the  |
   |                                 | droop. Compensation factor is the |
   |                                 | resistance, as an approximation   |
   |                                 | of the DC voltage of a common     |
   |                                 | (real or virtual) node in the DC  |
   |                                 | network. Targets are provided by  |
   |                                 | ACDCConverter.targetPpcc,         |
   |                                 | ACDCConverter.targetUdc,          |
   |                                 | VsConverter.droop and             |
   |                                 | VsConverter.droopCompensation.    |
   +---------------------------------+-----------------------------------+
   | phasePcc                        | Control is phase at point of      |
   |                                 | common coupling. Target is        |
   |                                 | provided by                       |
   |                                 | VsConverter.targetPhasePcc.       |
   +---------------------------------+-----------------------------------+
   | udc                             | Control is DC voltage with target |
   |                                 | value provided by                 |
   |                                 | ACDCConverter.targetUdc.          |
   +---------------------------------+-----------------------------------+

.. container:: group
   :name: VsQpccControlKind

   ` <#VsQpccControlKind>`__

   .. rubric:: VsQpccControlKind
      :name: vsqpcccontrolkind
      :class: enumerated

   DC

   Kind of reactive power control at point of common coupling for a
   voltage source converter.

   +----------------------+----------------------------------------------+
   | powerFactorPcc       | Control is power factor at point of common   |
   |                      | coupling. Target is provided by              |
   |                      | VsConverter.targetPowerFactorPcc.            |
   +----------------------+----------------------------------------------+
   | pulseWidthModulation | No explicit control. Pulse-modulation factor |
   |                      | is directly set in magnitude                 |
   |                      | (VsConverter.targetPWMfactor) and phase      |
   |                      | (VsConverter.targetPhasePcc).                |
   +----------------------+----------------------------------------------+
   | reactivePcc          | Control is reactive power at point of common |
   |                      | coupling. Target is provided by              |
   |                      | VsConverter.targetQpcc.                      |
   +----------------------+----------------------------------------------+
   | voltagePcc           | Control is voltage at point of common        |
   |                      | coupling. Target is provided by              |
   |                      | VsConverter.targetUpcc.                      |
   +----------------------+----------------------------------------------+

.. container:: group
   :name: WindingConnection

   ` <#WindingConnection>`__

   .. rubric:: WindingConnection
      :name: windingconnection
      :class: enumerated

   Wires

   Winding connection type.

   ==
   A  
   D  
   I  
   Y  
   Yn 
   Z  
   Zn 
   ==

Compound Types
==============

Datatypes
=========

.. container:: group
   :name: ActivePower

   ` <#ActivePower>`__

   .. rubric:: ActivePower
      :name: activepower
      :class: domain

   Domain

   Product of RMS value of the voltage and the RMS value of the in-phase
   component of the current.

   XSD type: float

.. container:: group
   :name: ActivePowerPerCurrentFlow

   ` <#ActivePowerPerCurrentFlow>`__

   .. rubric:: ActivePowerPerCurrentFlow
      :name: activepowerpercurrentflow
      :class: domain

   Domain

   Active power variation with current flow.

   XSD type: float

.. container:: group
   :name: AngleDegrees

   ` <#AngleDegrees>`__

   .. rubric:: AngleDegrees
      :name: angledegrees
      :class: domain

   Domain

   Measurement of angle in degrees.

   XSD type: float

.. container:: group
   :name: AngleRadians

   ` <#AngleRadians>`__

   .. rubric:: AngleRadians
      :name: angleradians
      :class: domain

   Domain

   Phase angle in radians.

   XSD type: float

.. container:: group
   :name: ApparentPower

   ` <#ApparentPower>`__

   .. rubric:: ApparentPower
      :name: apparentpower
      :class: domain

   Domain

   Product of the RMS value of the voltage and the RMS value of the
   current.

   XSD type: float

.. container:: group
   :name: Capacitance

   ` <#Capacitance>`__

   .. rubric:: Capacitance
      :name: capacitance
      :class: domain

   Domain

   Capacitive part of reactance (imaginary part of impedance), at rated
   frequency.

   XSD type: float

.. container:: group
   :name: Conductance

   ` <#Conductance>`__

   .. rubric:: Conductance
      :name: conductance
      :class: domain

   Domain

   Factor by which voltage must be multiplied to give corresponding
   power lost from a circuit. Real part of admittance.

   XSD type: float

.. container:: group
   :name: CurrentFlow

   ` <#CurrentFlow>`__

   .. rubric:: CurrentFlow
      :name: currentflow
      :class: domain

   Domain

   Electrical current with sign convention: positive flow is out of the
   conducting equipment into the connectivity node. Can be both AC and
   DC.

   XSD type: float

.. container:: group
   :name: Frequency

   ` <#Frequency>`__

   .. rubric:: Frequency
      :name: frequency
      :class: domain

   Domain

   Cycles per second.

   XSD type: float

.. container:: group
   :name: Inductance

   ` <#Inductance>`__

   .. rubric:: Inductance
      :name: inductance
      :class: domain

   Domain

   Inductive part of reactance (imaginary part of impedance), at rated
   frequency.

   XSD type: float

.. container:: group
   :name: Length

   ` <#Length>`__

   .. rubric:: Length
      :name: length
      :class: domain

   Domain

   Unit of length. It shall be a positive value or zero.

   XSD type: float

.. container:: group
   :name: PU

   ` <#PU>`__

   .. rubric:: PU
      :name: pu
      :class: domain

   Domain

   Per Unit - a positive or negative value referred to a defined base.
   Values typically range from -10 to +10.

   XSD type: float

.. container:: group
   :name: PerCent

   ` <#PerCent>`__

   .. rubric:: PerCent
      :name: percent
      :class: domain

   Domain

   Percentage on a defined base. For example, specify as 100 to indicate
   at the defined base.

   XSD type: float

.. container:: group
   :name: Reactance

   ` <#Reactance>`__

   .. rubric:: Reactance
      :name: reactance
      :class: domain

   Domain

   Reactance (imaginary part of impedance), at rated frequency.

   XSD type: float

.. container:: group
   :name: ReactivePower

   ` <#ReactivePower>`__

   .. rubric:: ReactivePower
      :name: reactivepower
      :class: domain

   Domain

   Product of RMS value of the voltage and the RMS value of the
   quadrature component of the current.

   XSD type: float

.. container:: group
   :name: RealEnergy

   ` <#RealEnergy>`__

   .. rubric:: RealEnergy
      :name: realenergy
      :class: domain

   Domain

   Real electrical energy.

   XSD type: float

.. container:: group
   :name: Resistance

   ` <#Resistance>`__

   .. rubric:: Resistance
      :name: resistance
      :class: domain

   Domain

   Resistance (real part of impedance).

   XSD type: float

.. container:: group
   :name: RotationSpeed

   ` <#RotationSpeed>`__

   .. rubric:: RotationSpeed
      :name: rotationspeed
      :class: domain

   Domain

   Number of revolutions per second.

   XSD type: float

.. container:: group
   :name: Seconds

   ` <#Seconds>`__

   .. rubric:: Seconds
      :name: seconds
      :class: domain

   Domain

   Time, in seconds.

   XSD type: float

.. container:: group
   :name: Susceptance

   ` <#Susceptance>`__

   .. rubric:: Susceptance
      :name: susceptance
      :class: domain

   Domain

   Imaginary part of admittance.

   XSD type: float

.. container:: group
   :name: Voltage

   ` <#Voltage>`__

   .. rubric:: Voltage
      :name: voltage
      :class: domain

   Domain

   Electrical voltage, can be both AC and DC.

   XSD type: float

.. container:: group
   :name: VoltagePerReactivePower

   ` <#VoltagePerReactivePower>`__

   .. rubric:: VoltagePerReactivePower
      :name: voltageperreactivepower
      :class: domain

   Domain

   Voltage variation with reactive power.

   XSD type: float

Primitive Types
===============

.. container:: group
   :name: Boolean

   ` <#Boolean>`__

   .. rubric:: Boolean
      :name: boolean
      :class: domain

   Domain

   A type with the value space "true" and "false".

   XSD type: boolean

.. container:: group
   :name: DateTime

   ` <#DateTime>`__

   .. rubric:: DateTime
      :name: datetime
      :class: domain

   Domain

   Date and time as "yyyy-mm-ddThh:mm:ss.sss", which conforms with ISO
   8601. UTC time zone is specified as "yyyy-mm-ddThh:mm:ss.sssZ". A
   local timezone relative UTC is specified as
   "yyyy-mm-ddThh:mm:ss.sss-hh:mm". The second component (shown here as
   "ss.sss") could have any number of digits in its fractional part to
   allow any kind of precision beyond seconds.

   XSD type: dateTime

.. container:: group
   :name: Float

   ` <#Float>`__

   .. rubric:: Float
      :name: float
      :class: domain

   Domain

   A floating point number. The range is unspecified and not limited.

   XSD type: float

.. container:: group
   :name: Integer

   ` <#Integer>`__

   .. rubric:: Integer
      :name: integer
      :class: domain

   Domain

   An integer number. The range is unspecified and not limited.

   XSD type: integer

.. container:: group
   :name: String

   ` <#String>`__

   .. rubric:: String
      :name: string
      :class: domain

   Domain

   A string consisting of a sequence of characters. The character
   encoding is UTF-8. The string length is unspecified and unlimited.

   XSD type: string
