.. _target-dynamics:

EMT Dynamics
============

The package uses *DetailedModelTypeDynamics* to support the standard
library models in the *Emtiop* profile. To add more model types,
edit *detailed_model_types.json* in the *queries* subdirectory of the
package source. The CIM *StandardModels* for controllers are not supported
in *Emtiop*; only the *SynchronousMachineTimeConstantReactance* is used
from *StandardModels*.

For each dynamics controller type supported, the following attributes
are defined on the CIM class *NthAmDynamicModel*:
 
- **Model (Header)**: a mnemonic for this controller type, typically a 6-character codeword from the original *dyr* file schema.
- **nameKind**: the domain from which the *Model* name comes. May be *AUX*, *DGS*, *DYD*, *DYR* or *Other*. Use *Other* for user-code models that are not implemented in a DLL.
- **modelKind**: the expected application of this controller type. The package currently supports *machine*, *renewableEnergyResource*, *excitationSystem*, *powerSystemStabilizer*, and *turbineGovernor*.
- **statusKind**: the allowable use of this controller type for interconnection-wide studies in North America. May be *allowed*, *deprecated*, or *prohibited*.
- **description**: brief description of the controller, if available. Otherwise, use *Model* and *modelKind* for interpretation.
- **closestStandardModel**: the name of the best-matching model from *StandardModels* in the CIM *Dynamics* package. There may not be a close match. If there is a match, it may provide default values and units from the CIM documentation.
- **mRID**: a unique CIM identifier for this controller type, maintained within this package.

Each supported dynamics controller type has a list of parameters.
These map to the CIM class *ParameterDescriptor*.
 
- **name**: the name of the parameter, from orginal *dyr* file format
- **mRID**: a unique CIM identifier for this parameter descriptor, maintained within this package.
- **(sequence)Number**: an integer sequence number from original *dyr* file format. The sequence numbers of interest usually begins with **3**, because first three *dyr* parameters (*Bus*, *Model*, *ID*) are not handled as CIM model parameters. 
- **(typical)Value**: a default value, if available from a matching CIM attribute in the *closestStandardModel* class.
- **(engineering)Unit**: the expected input units, if available from a matching CIM attribute in the *closestStandardModel* class.
 
For EMT netlisting, use the CIM RDF queries *EMTDynamicsModel*,
*EMTDynamicsModelType*, *EMTDynamicsModelParameterDescriptor* and
*EMTDynamicsParameter* to retrieve the data. Refer to the original
*dyr* format documentation to interpret the applications,
parameter names and signal connections for each model type.
 
.. include:: dynamics_doc.rst
 
