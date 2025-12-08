-- REVISIT: Manually added "TransformerMeshImpedance.ToTransformerEnd" from the UML
-- REVISIT: Manually added IdentifiedObject.name, which is not unique, but should be within each UML class
-- REVISIT: Should remove unused PSRType
PRAGMA foreign_keys = ON;

CREATE TABLE "BatteryStateKind" ( "name" VARCHAR(100) UNIQUE );
INSERT INTO "BatteryStateKind" ( "name" ) VALUES ( 'charging' );
INSERT INTO "BatteryStateKind" ( "name" ) VALUES ( 'discharging' );
INSERT INTO "BatteryStateKind" ( "name" ) VALUES ( 'empty' );
INSERT INTO "BatteryStateKind" ( "name" ) VALUES ( 'full' );
INSERT INTO "BatteryStateKind" ( "name" ) VALUES ( 'waiting' );

CREATE TABLE "CurveStyle" ( "name" VARCHAR(100) UNIQUE );
INSERT INTO "CurveStyle" ( "name" ) VALUES ( 'constantYValue' );
INSERT INTO "CurveStyle" ( "name" ) VALUES ( 'straightLineYValues' );

CREATE TABLE "IfdBaseKind" ( "name" VARCHAR(100) UNIQUE );
INSERT INTO "IfdBaseKind" ( "name" ) VALUES ( 'ifag' );
INSERT INTO "IfdBaseKind" ( "name" ) VALUES ( 'iffl' );
INSERT INTO "IfdBaseKind" ( "name" ) VALUES ( 'ifnl' );

CREATE TABLE "InputSignalKind" ( "name" VARCHAR(100) UNIQUE );
INSERT INTO "InputSignalKind" ( "name" ) VALUES ( 'branchCurrent' );
INSERT INTO "InputSignalKind" ( "name" ) VALUES ( 'busFrequency' );
INSERT INTO "InputSignalKind" ( "name" ) VALUES ( 'busFrequencyDeviation' );
INSERT INTO "InputSignalKind" ( "name" ) VALUES ( 'busVoltage' );
INSERT INTO "InputSignalKind" ( "name" ) VALUES ( 'busVoltageDerivative' );
INSERT INTO "InputSignalKind" ( "name" ) VALUES ( 'fieldCurrent' );
INSERT INTO "InputSignalKind" ( "name" ) VALUES ( 'generatorAcceleratingPower' );
INSERT INTO "InputSignalKind" ( "name" ) VALUES ( 'generatorElectricalPower' );
INSERT INTO "InputSignalKind" ( "name" ) VALUES ( 'generatorMechanicalPower' );
INSERT INTO "InputSignalKind" ( "name" ) VALUES ( 'rotorAngularFrequencyDeviation' );
INSERT INTO "InputSignalKind" ( "name" ) VALUES ( 'rotorSpeed' );

CREATE TABLE "RotorKind" ( "name" VARCHAR(100) UNIQUE );
INSERT INTO "RotorKind" ( "name" ) VALUES ( 'roundRotor' );
INSERT INTO "RotorKind" ( "name" ) VALUES ( 'salientPole' );

CREATE TABLE "SynchronousMachineKind" ( "name" VARCHAR(100) UNIQUE );
INSERT INTO "SynchronousMachineKind" ( "name" ) VALUES ( 'condenser' );
INSERT INTO "SynchronousMachineKind" ( "name" ) VALUES ( 'generator' );
INSERT INTO "SynchronousMachineKind" ( "name" ) VALUES ( 'generatorOrCondenser' );
INSERT INTO "SynchronousMachineKind" ( "name" ) VALUES ( 'generatorOrCondenserOrMotor' );
INSERT INTO "SynchronousMachineKind" ( "name" ) VALUES ( 'generatorOrMotor' );
INSERT INTO "SynchronousMachineKind" ( "name" ) VALUES ( 'motor' );
INSERT INTO "SynchronousMachineKind" ( "name" ) VALUES ( 'motorOrCondenser' );

CREATE TABLE "SynchronousMachineModelKind" ( "name" VARCHAR(100) UNIQUE );
INSERT INTO "SynchronousMachineModelKind" ( "name" ) VALUES ( 'subtransient' );
INSERT INTO "SynchronousMachineModelKind" ( "name" ) VALUES ( 'subtransientSimplified' );
INSERT INTO "SynchronousMachineModelKind" ( "name" ) VALUES ( 'subtransientSimplifiedDirectAxis' );
INSERT INTO "SynchronousMachineModelKind" ( "name" ) VALUES ( 'subtransientTypeF' );
INSERT INTO "SynchronousMachineModelKind" ( "name" ) VALUES ( 'subtransientTypeJ' );

CREATE TABLE "SynchronousMachineOperatingMode" ( "name" VARCHAR(100) UNIQUE );
INSERT INTO "SynchronousMachineOperatingMode" ( "name" ) VALUES ( 'condenser' );
INSERT INTO "SynchronousMachineOperatingMode" ( "name" ) VALUES ( 'generator' );
INSERT INTO "SynchronousMachineOperatingMode" ( "name" ) VALUES ( 'motor' );

CREATE TABLE "UnitMultiplier" ( "name" VARCHAR(100) UNIQUE );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'E' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'G' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'M' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'P' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'T' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'Y' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'Z' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'a' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'c' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'd' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'da' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'f' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'h' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'k' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'm' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'micro' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'n' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'none' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'p' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'y' );
INSERT INTO "UnitMultiplier" ( "name" ) VALUES ( 'z' );

CREATE TABLE "UnitSymbol" ( "name" VARCHAR(100) UNIQUE );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'A' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'A2' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'A2h' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'A2s' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'APerA' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'APerm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Ah' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'As' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Bq' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Btu' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'C' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'CPerkg' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'CPerm2' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'CPerm3' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'F' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'FPerm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'G' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Gy' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'GyPers' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'H' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'HPerm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Hz' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'HzPerHz' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'HzPers' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'J' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'JPerK' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'JPerkg' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'JPerkgK' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'JPerm2' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'JPerm3' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'JPermol' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'JPermolK' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'JPers' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'K' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'KPers' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'M' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Mx' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'N' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'NPerm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Nm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Oe' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Pa' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'PaPers' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Pas' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Q' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Qh' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'S' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'SPerm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Sv' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'T' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'V' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'V2' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'V2h' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'VA' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'VAh' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'VAr' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'VArh' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'VPerHz' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'VPerV' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'VPerVA' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'VPerVAr' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'VPerm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Vh' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Vs' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'W' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'WPerA' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'WPerW' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'WPerm2' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'WPerm2sr' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'WPermK' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'WPers' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'WPersr' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Wb' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'Wh' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'anglemin' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'anglesec' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'bar' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'cd' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'charPers' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'character' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'cosPhi' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'count' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'd' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'dB' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'dBm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'deg' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'degC' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'ft3' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'gPerg' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'gal' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'h' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'ha' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'kat' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'katPerm3' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'kg' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'kgPerJ' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'kgPerm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'kgPerm3' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'kgm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'kgm2' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'kn' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'l' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'lPerh' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'lPerl' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'lPers' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'lm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'lx' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'm2' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'm2Pers' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'm3' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'm3Compensated' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'm3Perh' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'm3Perkg' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'm3Pers' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'm3Uncompensated' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'mPerm3' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'mPers' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'mPers2' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'min' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'mmHg' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'mol' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'molPerkg' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'molPerm3' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'molPermol' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'none' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'ohm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'ohmPerm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'ohmm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'onePerHz' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'onePerm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'ppm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'rad' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'radPers' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'radPers2' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'rev' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'rotPers' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 's' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'sPers' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'sr' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'therm' );
INSERT INTO "UnitSymbol" ( "name" ) VALUES ( 'tonne' );

CREATE TABLE "WindingConnection" ( "name" VARCHAR(100) UNIQUE );
INSERT INTO "WindingConnection" ( "name" ) VALUES ( 'A' );
INSERT INTO "WindingConnection" ( "name" ) VALUES ( 'D' );
INSERT INTO "WindingConnection" ( "name" ) VALUES ( 'I' );
INSERT INTO "WindingConnection" ( "name" ) VALUES ( 'Y' );
INSERT INTO "WindingConnection" ( "name" ) VALUES ( 'Yn' );
INSERT INTO "WindingConnection" ( "name" ) VALUES ( 'Z' );
INSERT INTO "WindingConnection" ( "name" ) VALUES ( 'Zn' );

CREATE TABLE "IdentifiedObject"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL
);

CREATE TABLE "BaseVoltage"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "nominalVoltage" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "IdentifiedObject" ( "mRID" )
);

CREATE TABLE "PowerSystemResource"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    FOREIGN KEY ( "mRID" ) REFERENCES "IdentifiedObject" ( "mRID" )
);

CREATE TABLE "ConnectivityNodeContainer"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    FOREIGN KEY ( "mRID" ) REFERENCES "PowerSystemResource" ( "mRID" )
);

CREATE TABLE "ConnectivityNode"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "ConnectivityNodeContainer" VARCHAR(100) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "IdentifiedObject" ( "mRID" ),
    FOREIGN KEY ( "ConnectivityNodeContainer" ) REFERENCES "ConnectivityNodeContainer" ( "mRID" )
);

CREATE TABLE "EquipmentContainer"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    FOREIGN KEY ( "mRID" ) REFERENCES "ConnectivityNodeContainer" ( "mRID" )
);

CREATE TABLE "Equipment"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "inService" INTEGER NOT NULL DEFAULT 1 CHECK ("inService" IN (0, 1)) NOT NULL,
    "EquipmentContainer" VARCHAR(100) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "PowerSystemResource" ( "mRID" ),
    FOREIGN KEY ( "EquipmentContainer" ) REFERENCES "EquipmentContainer" ( "mRID" )
);

CREATE TABLE "TransformerEnd"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "endNumber" INTEGER NOT NULL,
    "grounded" INTEGER NOT NULL DEFAULT 1 CHECK ("grounded" IN (0, 1)) NOT NULL,
    "rground" DOUBLE PRECISION NOT NULL,
    "xground" DOUBLE PRECISION NOT NULL,
    "BaseVoltage" VARCHAR(100) NOT NULL,
    "ConnectivityNode" VARCHAR(100) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "IdentifiedObject" ( "mRID" ),
    FOREIGN KEY ( "BaseVoltage" ) REFERENCES "BaseVoltage" ( "mRID" ),
    FOREIGN KEY ( "ConnectivityNode" ) REFERENCES "ConnectivityNode" ( "mRID" )
);

CREATE TABLE "GeneratingUnit"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "maxOperatingP" DOUBLE PRECISION NOT NULL,
    "minOperatingP" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "Equipment" ( "mRID" )
);

CREATE TABLE "ConductingEquipment"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "BaseVoltage" VARCHAR(100),
    "FromConnectivityNode" VARCHAR(100),
    "ToConnectivityNode" VARCHAR(100),
    FOREIGN KEY ( "mRID" ) REFERENCES "Equipment" ( "mRID" ),
    FOREIGN KEY ( "BaseVoltage" ) REFERENCES "BaseVoltage" ( "mRID" ),
    FOREIGN KEY ( "FromConnectivityNode" ) REFERENCES "FromConnectivityNode" ( "mRID" ),
    FOREIGN KEY ( "ToConnectivityNode" ) REFERENCES "ToConnectivityNode" ( "mRID" )
);

CREATE TABLE "EnergyConnection"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    FOREIGN KEY ( "mRID" ) REFERENCES "ConductingEquipment" ( "mRID" )
);

CREATE TABLE "EnergySource"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "nominalVoltage" DOUBLE PRECISION NOT NULL,
    "r" DOUBLE PRECISION NOT NULL,
    "r0" DOUBLE PRECISION NOT NULL,
    "voltageAngle" DOUBLE PRECISION NOT NULL,
    "voltageMagnitude" DOUBLE PRECISION NOT NULL,
    "x" DOUBLE PRECISION NOT NULL,
    "x0" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "EnergyConnection" ( "mRID" )
);

CREATE TABLE "LoadResponseCharacteristic"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "exponentModel" INTEGER NOT NULL DEFAULT 1 CHECK ("exponentModel" IN (0, 1)) NOT NULL,
    "pConstantCurrent" DOUBLE PRECISION NOT NULL,
    "pConstantImpedance" DOUBLE PRECISION NOT NULL,
    "pConstantPower" DOUBLE PRECISION NOT NULL,
    "pFrequencyExponent" DOUBLE PRECISION NOT NULL,
    "pVoltageExponent" DOUBLE PRECISION NOT NULL,
    "qConstantCurrent" DOUBLE PRECISION NOT NULL,
    "qConstantImpedance" DOUBLE PRECISION NOT NULL,
    "qConstantPower" DOUBLE PRECISION NOT NULL,
    "qFrequencyExponent" DOUBLE PRECISION NOT NULL,
    "qVoltageExponent" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "IdentifiedObject" ( "mRID" )
);

CREATE TABLE "Conductor"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "length" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "ConductingEquipment" ( "mRID" )
);

CREATE TABLE "ACLineSegment"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "b0ch" DOUBLE PRECISION NOT NULL,
    "bch" DOUBLE PRECISION NOT NULL,
    "r" DOUBLE PRECISION NOT NULL,
    "r0" DOUBLE PRECISION NOT NULL,
    "x" DOUBLE PRECISION NOT NULL,
    "x0" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "Conductor" ( "mRID" )
);

CREATE TABLE "RegulatingCondEq"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    FOREIGN KEY ( "mRID" ) REFERENCES "EnergyConnection" ( "mRID" )
);

CREATE TABLE "PowerElectronicsConnection"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "maxIFault" DOUBLE PRECISION NOT NULL,
    "maxQ" DOUBLE PRECISION NOT NULL,
    "minQ" DOUBLE PRECISION NOT NULL,
    "p" DOUBLE PRECISION NOT NULL,
    "q" DOUBLE PRECISION NOT NULL,
    "ratedS" DOUBLE PRECISION NOT NULL,
    "ratedU" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "RegulatingCondEq" ( "mRID" )
);

CREATE TABLE "PowerElectronicsUnit"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "maxP" DOUBLE PRECISION NOT NULL,
    "minP" DOUBLE PRECISION NOT NULL,
    "PowerElectronicsConnection" VARCHAR(100) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "Equipment" ( "mRID" ),
    FOREIGN KEY ( "PowerElectronicsConnection" ) REFERENCES "PowerElectronicsConnection" ( "mRID" )
);

CREATE TABLE "ShuntCompensator"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "grounded" INTEGER NOT NULL DEFAULT 1 CHECK ("grounded" IN (0, 1)) NOT NULL,
    "maximumSections" INTEGER NOT NULL,
    "nomU" DOUBLE PRECISION NOT NULL,
    "sections" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "RegulatingCondEq" ( "mRID" )
);

CREATE TABLE "RotatingMachine"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "p" DOUBLE PRECISION NOT NULL,
    "q" DOUBLE PRECISION NOT NULL,
    "ratedS" DOUBLE PRECISION NOT NULL,
    "ratedU" DOUBLE PRECISION NOT NULL,
    "GeneratingUnit" VARCHAR(100) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "RegulatingCondEq" ( "mRID" ),
    FOREIGN KEY ( "GeneratingUnit" ) REFERENCES "GeneratingUnit" ( "mRID" )
);

CREATE TABLE "AsynchronousMachine"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    FOREIGN KEY ( "mRID" ) REFERENCES "RotatingMachine" ( "mRID" )
);

CREATE TABLE "BatteryUnit"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "batteryState" VARCHAR(100) NOT NULL,
    "ratedE" DOUBLE PRECISION NOT NULL,
    "storedE" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "PowerElectronicsUnit" ( "mRID" ),
    FOREIGN KEY ( "batteryState" ) REFERENCES "BatteryStateKind" ( "name" )
);

CREATE TABLE "Curve"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "curveStyle" VARCHAR(100),
    "xMultiplier" VARCHAR(100),
    "xUnit" VARCHAR(100),
    "y1Multiplier" VARCHAR(100),
    "y1Unit" VARCHAR(100),
    FOREIGN KEY ( "mRID" ) REFERENCES "IdentifiedObject" ( "mRID" ),
    FOREIGN KEY ( "curveStyle" ) REFERENCES "CurveStyle" ( "name" ),
    FOREIGN KEY ( "xMultiplier" ) REFERENCES "UnitMultiplier" ( "name" ),
    FOREIGN KEY ( "y1Multiplier" ) REFERENCES "UnitMultiplier" ( "name" ),
    FOREIGN KEY ( "xUnit" ) REFERENCES "UnitSymbol" ( "name" ),
    FOREIGN KEY ( "y1Unit" ) REFERENCES "UnitSymbol" ( "name" )
);

CREATE TABLE "CurveData"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "xvalue" DOUBLE PRECISION NOT NULL,
    "y1value" DOUBLE PRECISION NOT NULL,
    "Curve" VARCHAR(100) NOT NULL,
    FOREIGN KEY ( "Curve" ) REFERENCES "Curve" ( "mRID" )
);

CREATE TABLE "DiagramObject"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "drawingOrder" INTEGER NOT NULL,
    "isPolygon" INTEGER NOT NULL DEFAULT 1 CHECK ("isPolygon" IN (0, 1)) NOT NULL,
    "IdentifiedObject" VARCHAR(100) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "IdentifiedObject" ( "mRID" ),
    FOREIGN KEY ( "IdentifiedObject" ) REFERENCES "IdentifiedObject" ( "mRID" )
);

CREATE TABLE "DiagramObjectPoint"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "sequenceNumber" INTEGER NOT NULL,
    "xPosition" DOUBLE PRECISION NOT NULL,
    "yPosition" DOUBLE PRECISION NOT NULL,
    "DiagramObject" VARCHAR(100) NOT NULL,
    FOREIGN KEY ( "DiagramObject" ) REFERENCES "DiagramObject" ( "mRID" )
);

CREATE TABLE "DynamicsFunctionBlock"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "enabled" INTEGER NOT NULL DEFAULT 1 CHECK ("enabled" IN (0, 1)) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "IdentifiedObject" ( "mRID" )
);

CREATE TABLE "EnergyConsumer"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "p" DOUBLE PRECISION NOT NULL,
    "q" DOUBLE PRECISION NOT NULL,
    "LoadResponse" VARCHAR(100) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "EnergyConnection" ( "mRID" ),
    FOREIGN KEY ( "LoadResponse" ) REFERENCES "LoadResponseCharacteristic" ( "mRID" )
);

CREATE TABLE "HydroGeneratingUnit"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    FOREIGN KEY ( "mRID" ) REFERENCES "GeneratingUnit" ( "mRID" )
);

CREATE TABLE "LinearShuntCompensator"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "bPerSection" DOUBLE PRECISION NOT NULL,
    "gPerSection" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "ShuntCompensator" ( "mRID" )
);

--CREATE TABLE "Name"
--(
--    "mRID" VARCHAR(100) PRIMARY KEY
--);

CREATE TABLE "NuclearGeneratingUnit"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    FOREIGN KEY ( "mRID" ) REFERENCES "GeneratingUnit" ( "mRID" )
);

--CREATE TABLE "PSRType"
--(
--    "mRID" VARCHAR(100) PRIMARY KEY,
--    FOREIGN KEY ( "mRID" ) REFERENCES "IdentifiedObject" ( "mRID" )
--);

CREATE TABLE "PhotoVoltaicUnit"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    FOREIGN KEY ( "mRID" ) REFERENCES "PowerElectronicsUnit" ( "mRID" )
);

CREATE TABLE "PowerElectronicsWindUnit"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    FOREIGN KEY ( "mRID" ) REFERENCES "PowerElectronicsUnit" ( "mRID" )
);

CREATE TABLE "PowerTransformer"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "vectorGroup" VARCHAR(255) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "ConductingEquipment" ( "mRID" )
);

CREATE TABLE "PowerTransformerEnd"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "connectionKind" VARCHAR(100) NOT NULL,
    "phaseAngleClock" INTEGER NOT NULL,
    "ratedS" DOUBLE PRECISION NOT NULL,
    "ratedU" DOUBLE PRECISION NOT NULL,
    "PowerTransformer" VARCHAR(100) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "TransformerEnd" ( "mRID" ),
    FOREIGN KEY ( "PowerTransformer" ) REFERENCES "PowerTransformer" ( "mRID" ),
    FOREIGN KEY ( "connectionKind" ) REFERENCES "WindingConnection" ( "name" )
);

CREATE TABLE "RotatingMachineDynamics"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "damping" DOUBLE PRECISION NOT NULL,
    "inertia" DOUBLE PRECISION NOT NULL,
    "statorLeakageReactance" DOUBLE PRECISION NOT NULL,
    "statorResistance" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "DynamicsFunctionBlock" ( "mRID" )
);

CREATE TABLE "SeriesCompensator"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "r" DOUBLE PRECISION NOT NULL,
    "r0" DOUBLE PRECISION NOT NULL,
    "x" DOUBLE PRECISION NOT NULL,
    "x0" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "ConductingEquipment" ( "mRID" )
);

CREATE TABLE "SynchronousMachine"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "earthing" INTEGER NOT NULL DEFAULT 1 CHECK ("earthing" IN (0, 1)) NOT NULL,
    "earthingStarPointR" DOUBLE PRECISION NOT NULL,
    "earthingStarPointX" DOUBLE PRECISION NOT NULL,
    "maxQ" DOUBLE PRECISION NOT NULL,
    "minQ" DOUBLE PRECISION NOT NULL,
    "operatingMode" VARCHAR(100) NOT NULL,
    "type" VARCHAR(100) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "RotatingMachine" ( "mRID" ),
    FOREIGN KEY ( "operatingMode" ) REFERENCES "SynchronousMachineOperatingMode" ( "name" ),
    FOREIGN KEY ( "type" ) REFERENCES "SynchronousMachineKind" ( "name" )
);

CREATE TABLE "SynchronousMachineDynamics"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "SynchronousMachine" VARCHAR(100),
    FOREIGN KEY ( "mRID" ) REFERENCES "RotatingMachineDynamics" ( "mRID" ),
    FOREIGN KEY ( "SynchronousMachine" ) REFERENCES "SynchronousMachine" ( "mRID" )
);

CREATE TABLE "SynchronousMachineDetailed"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "efdBaseRatio" DOUBLE PRECISION NOT NULL,
    "ifdBaseType" VARCHAR(100) NOT NULL,
    "saturationFactor" DOUBLE PRECISION NOT NULL,
    "saturationFactor120" DOUBLE PRECISION NOT NULL,
    "saturationFactor120QAxis" DOUBLE PRECISION NOT NULL,
    "saturationFactorQAxis" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "SynchronousMachineDynamics" ( "mRID" ),
    FOREIGN KEY ( "ifdBaseType" ) REFERENCES "IfdBaseKind" ( "name" )
);

CREATE TABLE "SynchronousMachineTimeConstantReactance"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "ks" DOUBLE PRECISION NOT NULL,
    "modelType" VARCHAR(100) NOT NULL,
    "rotorType" VARCHAR(100) NOT NULL,
    "tc" DOUBLE PRECISION NOT NULL,
    "tpdo" DOUBLE PRECISION NOT NULL,
    "tppdo" DOUBLE PRECISION NOT NULL,
    "tppqo" DOUBLE PRECISION NOT NULL,
    "tpqo" DOUBLE PRECISION NOT NULL,
    "xDirectSubtrans" DOUBLE PRECISION NOT NULL,
    "xDirectSync" DOUBLE PRECISION NOT NULL,
    "xDirectTrans" DOUBLE PRECISION NOT NULL,
    "xQuadSubtrans" DOUBLE PRECISION NOT NULL,
    "xQuadSync" DOUBLE PRECISION NOT NULL,
    "xQuadTrans" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "SynchronousMachineDetailed" ( "mRID" ),
    FOREIGN KEY ( "modelType" ) REFERENCES "SynchronousMachineModelKind" ( "name" ),
    FOREIGN KEY ( "rotorType" ) REFERENCES "RotorKind" ( "name" )
);

CREATE TABLE "TextDiagramObject"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "text" VARCHAR(255) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "DiagramObject" ( "mRID" )
);

CREATE TABLE "ThermalGeneratingUnit"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    FOREIGN KEY ( "mRID" ) REFERENCES "GeneratingUnit" ( "mRID" )
);

CREATE TABLE "TransformerCoreAdmittance"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "b" DOUBLE PRECISION NOT NULL,
    "b0" DOUBLE PRECISION NOT NULL,
    "g" DOUBLE PRECISION NOT NULL,
    "g0" DOUBLE PRECISION NOT NULL,
    "TransformerEnd" VARCHAR(100) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "IdentifiedObject" ( "mRID" ),
    FOREIGN KEY ( "TransformerEnd" ) REFERENCES "TransformerEnd" ( "mRID" )
);

CREATE TABLE "TransformerMeshImpedance"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "r" DOUBLE PRECISION NOT NULL,
    "r0" DOUBLE PRECISION NOT NULL,
    "x" DOUBLE PRECISION NOT NULL,
    "x0" DOUBLE PRECISION NOT NULL,
    "FromTransformerEnd" VARCHAR(100) NOT NULL,
    "ToTransformerEnd" VARCHAR(100) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "IdentifiedObject" ( "mRID" ),
    FOREIGN KEY ( "FromTransformerEnd" ) REFERENCES "TransformerEnd" ( "mRID" ),
    FOREIGN KEY ( "ToTransformerEnd" ) REFERENCES "TransformerEnd" ( "mRID" )
);

CREATE TABLE "TransformerSaturation"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "TransformerCoreAdmittance" VARCHAR(100) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "Curve" ( "mRID" ),
    FOREIGN KEY ( "TransformerCoreAdmittance" ) REFERENCES "TransformerCoreAdmittance" ( "mRID" )
);

CREATE TABLE "ExcitationSystemDynamics"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "SynchronousMachineDynamics" VARCHAR(100),
    FOREIGN KEY ( "mRID" ) REFERENCES "DynamicsFunctionBlock" ( "mRID" ),
    FOREIGN KEY ( "SynchronousMachineDynamics" ) REFERENCES "SynchronousMachineDynamics" ( "mRID" )
);

CREATE TABLE "ExcST1A"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "ilr" DOUBLE PRECISION NOT NULL,
    "ka" DOUBLE PRECISION NOT NULL,
    "kc" DOUBLE PRECISION NOT NULL,
    "kf" DOUBLE PRECISION NOT NULL,
    "klr" DOUBLE PRECISION NOT NULL,
    "ta" DOUBLE PRECISION NOT NULL,
    "tb" DOUBLE PRECISION NOT NULL,
    "tb1" DOUBLE PRECISION NOT NULL,
    "tc" DOUBLE PRECISION NOT NULL,
    "tc1" DOUBLE PRECISION NOT NULL,
    "tf" DOUBLE PRECISION NOT NULL,
    "vamax" DOUBLE PRECISION NOT NULL,
    "vamin" DOUBLE PRECISION NOT NULL,
    "vimax" DOUBLE PRECISION NOT NULL,
    "vimin" DOUBLE PRECISION NOT NULL,
    "vrmax" DOUBLE PRECISION NOT NULL,
    "vrmin" DOUBLE PRECISION NOT NULL,
    "xe" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "ExcitationSystemDynamics" ( "mRID" )
);

CREATE TABLE "PowerSystemStabilizerDynamics"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "ExcitationSystemDynamics" VARCHAR(100) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "DynamicsFunctionBlock" ( "mRID" ),
    FOREIGN KEY ( "ExcitationSystemDynamics" ) REFERENCES "ExcitationSystemDynamics" ( "mRID" )
);

CREATE TABLE "PssIEEE1A"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "a1" DOUBLE PRECISION NOT NULL,
    "a2" DOUBLE PRECISION NOT NULL,
    "inputSignalType" VARCHAR(100) NOT NULL,
    "ks" DOUBLE PRECISION NOT NULL,
    "t1" DOUBLE PRECISION NOT NULL,
    "t2" DOUBLE PRECISION NOT NULL,
    "t3" DOUBLE PRECISION NOT NULL,
    "t4" DOUBLE PRECISION NOT NULL,
    "t5" DOUBLE PRECISION NOT NULL,
    "t6" DOUBLE PRECISION NOT NULL,
    "vrmax" DOUBLE PRECISION NOT NULL,
    "vrmin" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "PowerSystemStabilizerDynamics" ( "mRID" ),
    FOREIGN KEY ( "inputSignalType" ) REFERENCES "InputSignalKind" ( "name" )
);

CREATE TABLE "TurbineGovernorDynamics"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "SynchronousMachineDynamics" VARCHAR(100),
    FOREIGN KEY ( "mRID" ) REFERENCES "DynamicsFunctionBlock" ( "mRID" ),
    FOREIGN KEY ( "SynchronousMachineDynamics" ) REFERENCES "SynchronousMachineDynamics" ( "mRID" )
);

CREATE TABLE "GovSteamSGO"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "k1" DOUBLE PRECISION NOT NULL,
    "k2" DOUBLE PRECISION NOT NULL,
    "k3" DOUBLE PRECISION NOT NULL,
    "mwbase" DOUBLE PRECISION NOT NULL,
    "pmax" DOUBLE PRECISION NOT NULL,
    "pmin" DOUBLE PRECISION NOT NULL,
    "t1" DOUBLE PRECISION NOT NULL,
    "t2" DOUBLE PRECISION NOT NULL,
    "t3" DOUBLE PRECISION NOT NULL,
    "t4" DOUBLE PRECISION NOT NULL,
    "t5" DOUBLE PRECISION NOT NULL,
    "t6" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "TurbineGovernorDynamics" ( "mRID" )
);

CREATE TABLE "WeccDynamics"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "PowerElectronicsConnection" VARCHAR(100) NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "DynamicsFunctionBlock" ( "mRID" ),
    FOREIGN KEY ( "PowerElectronicsConnection" ) REFERENCES "PowerElectronicsConnection" ( "mRID" )
);

CREATE TABLE "WeccREEC"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    FOREIGN KEY ( "mRID" ) REFERENCES "WeccDynamics" ( "mRID" )
);

CREATE TABLE "WeccREECA"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "db1" DOUBLE PRECISION NOT NULL,
    "db2" DOUBLE PRECISION NOT NULL,
    "dPmax" DOUBLE PRECISION NOT NULL,
    "dPmin" DOUBLE PRECISION NOT NULL,
    "imax" DOUBLE PRECISION NOT NULL,
    "iqfrz" DOUBLE PRECISION NOT NULL,
    "iqh1" DOUBLE PRECISION NOT NULL,
    "iql1" DOUBLE PRECISION NOT NULL,
    "kqi" DOUBLE PRECISION NOT NULL,
    "kqp" DOUBLE PRECISION NOT NULL,
    "kqv" DOUBLE PRECISION NOT NULL,
    "kvi" DOUBLE PRECISION NOT NULL,
    "kvp" DOUBLE PRECISION NOT NULL,
    "pfFlag" INTEGER NOT NULL DEFAULT 1 CHECK ("pfFlag" IN (0, 1)) NOT NULL,
    "pFlag" INTEGER NOT NULL DEFAULT 1 CHECK ("pFlag" IN (0, 1)) NOT NULL,
    "pmax" DOUBLE PRECISION NOT NULL,
    "pmin" DOUBLE PRECISION NOT NULL,
    "pqFlag" INTEGER NOT NULL DEFAULT 1 CHECK ("pqFlag" IN (0, 1)) NOT NULL,
    "qFlag" INTEGER NOT NULL DEFAULT 1 CHECK ("qFlag" IN (0, 1)) NOT NULL,
    "qmax" DOUBLE PRECISION NOT NULL,
    "qmin" DOUBLE PRECISION NOT NULL,
    "thld" DOUBLE PRECISION NOT NULL,
    "thld2" DOUBLE PRECISION NOT NULL,
    "tiq" DOUBLE PRECISION NOT NULL,
    "tp" DOUBLE PRECISION NOT NULL,
    "tpord" DOUBLE PRECISION NOT NULL,
    "trv" DOUBLE PRECISION NOT NULL,
    "vdi1i1" DOUBLE PRECISION NOT NULL,
    "vdi1i2" DOUBLE PRECISION NOT NULL,
    "vdi1i3" DOUBLE PRECISION NOT NULL,
    "vdi1i4" DOUBLE PRECISION NOT NULL,
    "vdi1v1" DOUBLE PRECISION NOT NULL,
    "vdi1v2" DOUBLE PRECISION NOT NULL,
    "vdi1v3" DOUBLE PRECISION NOT NULL,
    "vdi1v4" DOUBLE PRECISION NOT NULL,
    "vdi2i1" DOUBLE PRECISION NOT NULL,
    "vdi2i2" DOUBLE PRECISION NOT NULL,
    "vdi2i3" DOUBLE PRECISION NOT NULL,
    "vdi2i4" DOUBLE PRECISION NOT NULL,
    "vdi2v1" DOUBLE PRECISION NOT NULL,
    "vdi2v2" DOUBLE PRECISION NOT NULL,
    "vdi2v3" DOUBLE PRECISION NOT NULL,
    "vdi2v4" DOUBLE PRECISION NOT NULL,
    "vdip" DOUBLE PRECISION NOT NULL,
    "vFlag" INTEGER NOT NULL DEFAULT 1 CHECK ("vFlag" IN (0, 1)) NOT NULL,
    "vmax" DOUBLE PRECISION NOT NULL,
    "vmin" DOUBLE PRECISION NOT NULL,
    "vref0" DOUBLE PRECISION NOT NULL,
    "vref1" DOUBLE PRECISION NOT NULL,
    "vup" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "WeccREEC" ( "mRID" )
);

CREATE TABLE "WeccREGCA"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "brkpt" DOUBLE PRECISION NOT NULL,
    "iolim" DOUBLE PRECISION NOT NULL,
    "iqrmax" DOUBLE PRECISION NOT NULL,
    "iqrmin" DOUBLE PRECISION NOT NULL,
    "ivpl1" DOUBLE PRECISION NOT NULL,
    "ivplsw" INTEGER NOT NULL DEFAULT 1 CHECK ("ivplsw" IN (0, 1)) NOT NULL,
    "ivpnt0" DOUBLE PRECISION NOT NULL,
    "ivpnt1" DOUBLE PRECISION NOT NULL,
    "khv" DOUBLE PRECISION NOT NULL,
    "rrpwr" DOUBLE PRECISION NOT NULL,
    "tfltr" DOUBLE PRECISION NOT NULL,
    "tg" DOUBLE PRECISION NOT NULL,
    "volim" DOUBLE PRECISION NOT NULL,
    "zerox" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "WeccDynamics" ( "mRID" )
);

CREATE TABLE "WeccREPCA"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "db" DOUBLE PRECISION NOT NULL,
    "ddn" DOUBLE PRECISION NOT NULL,
    "dup" DOUBLE PRECISION NOT NULL,
    "emax" DOUBLE PRECISION NOT NULL,
    "emin" DOUBLE PRECISION NOT NULL,
    "fdbd1" DOUBLE PRECISION NOT NULL,
    "fdbd2" DOUBLE PRECISION NOT NULL,
    "femax" DOUBLE PRECISION NOT NULL,
    "femin" DOUBLE PRECISION NOT NULL,
    "frqFlag" INTEGER NOT NULL DEFAULT 1 CHECK ("frqFlag" IN (0, 1)) NOT NULL,
    "kc" DOUBLE PRECISION NOT NULL,
    "ki" DOUBLE PRECISION NOT NULL,
    "kig" DOUBLE PRECISION NOT NULL,
    "kp" DOUBLE PRECISION NOT NULL,
    "kpg" DOUBLE PRECISION NOT NULL,
    "pmax" DOUBLE PRECISION NOT NULL,
    "pmin" DOUBLE PRECISION NOT NULL,
    "qmax" DOUBLE PRECISION NOT NULL,
    "qmin" DOUBLE PRECISION NOT NULL,
    "rc" DOUBLE PRECISION NOT NULL,
    "refFlag" INTEGER NOT NULL DEFAULT 1 CHECK ("refFlag" IN (0, 1)) NOT NULL,
    "tfltr" DOUBLE PRECISION NOT NULL,
    "tft" DOUBLE PRECISION NOT NULL,
    "tfv" DOUBLE PRECISION NOT NULL,
    "tlag" DOUBLE PRECISION NOT NULL,
    "tp" DOUBLE PRECISION NOT NULL,
    "vcmpFlag" INTEGER NOT NULL DEFAULT 1 CHECK ("vcmpFlag" IN (0, 1)) NOT NULL,
    "vfrz" DOUBLE PRECISION NOT NULL,
    "xc" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "WeccDynamics" ( "mRID" )
);

CREATE TABLE "WeccWTGARA"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "ka" DOUBLE PRECISION NOT NULL,
    "t0" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "WeccDynamics" ( "mRID" )
);

CREATE TABLE "WeccWTGTA"
(
    "mRID" VARCHAR(100) PRIMARY KEY,
    "dshaft" DOUBLE PRECISION NOT NULL,
    "hg" DOUBLE PRECISION NOT NULL,
    "ht" DOUBLE PRECISION NOT NULL,
    "kshaft" DOUBLE PRECISION NOT NULL,
    FOREIGN KEY ( "mRID" ) REFERENCES "WeccDynamics" ( "mRID" )
);

------------------------------------------------------------------------------
-- Foreign key column indexes for optimized queries and joins
------------------------------------------------------------------------------

CREATE INDEX ix_ConductingEquipment_BaseVoltage ON "ConductingEquipment" ( "BaseVoltage" );
CREATE INDEX ix_ConductingEquipment_FromConnectivityNode ON "ConductingEquipment" ( "FromConnectivityNode" );
CREATE INDEX ix_ConductingEquipment_ToConnectivityNode ON "ConductingEquipment" ( "ToConnectivityNode" );
CREATE INDEX ix_ConnectivityNode_ConnectivityNodeContainer ON "ConnectivityNode" ( "ConnectivityNodeContainer" );
CREATE INDEX ix_CurveData_Curve ON "CurveData" ( "Curve" );
CREATE INDEX ix_DiagramObject_IdentifiedObject ON "DiagramObject" ( "IdentifiedObject" );
CREATE INDEX ix_DiagramObjectPoint_DiagramObject ON "DiagramObjectPoint" ( "DiagramObject" );
CREATE INDEX ix_EnergyConsumer_LoadResponse ON "EnergyConsumer" ( "LoadResponse" );
CREATE INDEX ix_Equipment_EquipmentContainer ON "Equipment" ( "EquipmentContainer" );
CREATE INDEX ix_ExcitationSystemDynamics_SynchronousMachineDynamics ON "ExcitationSystemDynamics" ( "SynchronousMachineDynamics" );
CREATE INDEX ix_PowerElectronicsUnit_PowerElectronicsConnection ON "PowerElectronicsUnit" ( "PowerElectronicsConnection" );
CREATE INDEX ix_PowerSystemStabilizerDynamics_ExcitationSystemDynamics ON "PowerSystemStabilizerDynamics" ( "ExcitationSystemDynamics" );
CREATE INDEX ix_PowerTransformerEnd_PowerTransformer ON "PowerTransformerEnd" ( "PowerTransformer" );
CREATE INDEX ix_RotatingMachine_GeneratingUnit ON "RotatingMachine" ( "GeneratingUnit" );
CREATE INDEX ix_SynchronousMachineDynamics_SynchronousMachine ON "SynchronousMachineDynamics" ( "SynchronousMachine" );
CREATE INDEX ix_TransformerCoreAdmittance_TransformerEnd ON "TransformerCoreAdmittance" ( "TransformerEnd" );
CREATE INDEX ix_TransformerEnd_BaseVoltage ON "TransformerEnd" ( "BaseVoltage" );
CREATE INDEX ix_TransformerEnd_ConnectivityNode ON "TransformerEnd" ( "ConnectivityNode" );
CREATE INDEX ix_TransformerMeshImpedance_FromTransformerEnd ON "TransformerMeshImpedance" ( "FromTransformerEnd" );
CREATE INDEX ix_TransformerSaturation_TransformerCoreAdmittance ON "TransformerSaturation" ( "TransformerCoreAdmittance" );
CREATE INDEX ix_TurbineGovernorDynamics_SynchronousMachineDynamics ON "TurbineGovernorDynamics" ( "SynchronousMachineDynamics" );
CREATE INDEX ix_WeccDynamics_PowerElectronicsConnection ON "WeccDynamics" ( "PowerElectronicsConnection" );
