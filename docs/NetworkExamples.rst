.. role:: math(raw)
   :format: html latex
..

.. _target-examples-network:

Network Examples
################

Two versions of ATP are used in these examples. The script *atp.py*
chooses the correct version based on the example's case number.

#. **runtpgig** is the upsized GNU version for large cases. The *WECC240* example requires it.
#. **mytpbig** has been compiled to call *gfm_gfl_ibr2.dll*, the 32-bit version, at runtime. It is required for the *SMIBDLL* example. It also runs the other examples, except for *WECC240*.

The following WECC generic IBR model settings apply to the *IEEE39*, 
*IEEE118*, and *WECC240* examples. They are not necessarily optimized for 
best dynamic performance. Updates to the *dyr* file settings may produce 
better results.

========= =====
Parameter Value
========= =====
vFlag     True 
qFlag     True 
pqFlag    False 
pfFlag    False 
refFlag   True 
vcmpFlag  True 
frqFlag   True 
ivplsw    True 
pFlag     False 
kqv       2.0
kqp       1.0
kqi       0.33
kvp       0.2
kvi       5.0
kp        0.04
ki        8.0
kpg       0.5
kig       1.0
========= =====
 
.. _target-examples-xfmrsat:


Transformer Saturation
**********************

This example disconnects 400 MW of load from the end of a 500-km 
transformer-terminated line. It demonstrates the CIM extension for 
transformer saturation in the `TransformerSaturation` class. It does not require `gfm_gfl_ibr2.dll` to run in 
ATP. The first set of graphs represents a linear transformer and the second set of graphs represents a nonlinear transformer.

.. image:: ../atp/data/Xfmr_network.png

**Linear Transformer Core**

.. image:: ../atp/data/XfmrLinear.png

**Saturating Transformer Core**

.. image:: ../atp/data/XfmrNonlinear.png

.. _target-examples-ieee39:


IEEE 39-Bus
***********

This example demonstrates a single-line-to-ground fault (SLGF) applied and 
cleared on the IEEE 39-bus test system, which is generally representative 
of New England. One of the original 10 machines has been replace with a 
solar plant. The purpose of this example is to demonstrate CIM extensions 
to remove the CIM *Terminal* class and the WECC dynamic models for IBR. 
This example does not require `gfm_gfl_ibr2.dll` to run in ATP. 

.. image:: ../atp/data/IEEE39_network.png

.. image:: ../atp/data/IEEE39.png

.. _target-examples-ieee118:


IEEE 118-Bus
************

This example demonstrates a SLGF applied and cleared on the IEEE 118-bus 
test system, which is generally representative of the Midwestern United 
States circa 1962. This example has 193 buses so that each generator has 
its own generator stepup transformer (GSU), i.e., no generators are 
paralleled on the same bus. Several of the machines have been replaced 
with 14 solar and 5 wind plants, so this version of the test case includes 
56 synchronous machines and 19 IBR. The purpose of this example is to 
demonstrate CIM extensions to remove the CIM *Terminal* class and the WECC 
dynamic models for IBR. This example does not require `gfm_gfl_ibr2.dll` 
to run in ATP. It does not require `gfm_gfl_ibr2.dll` to run in ATP.

.. image:: ../atp/data/IEEE118_network.png

.. image:: ../atp/data/IEEE118.png

.. _target-examples-wecc240:


WECC 240-Bus
************

This example demonstrates a SLGF applied and cleared on the WECC 240-bus 
test system, which is generally representative of the Western United 
States. This version has 333 buses so that each generator has its own 
generator stepup transformer (GSU), i.e., no generators are paralleled on 
the same bus. It includes 105 synchronous machines and 35 IBR. The purpose 
of this example is to demonstrate CIM extensions to remove the CIM 
*Terminal* class and the WECC dynamic models for IBR. This example does 
not require `gfm_gfl_ibr2.dll` to run in ATP. 

.. image:: ../atp/data/wecc240_network.png

.. image:: ../atp/data/WECC240.png


.. _target-examples-smibdll:

SMIB DLL
********

This result comes from the EPRI generic grid-forming inverter model, 
implemented in a DLL compiled from C code. It is sized at 100 MW and 
connected to a single-machine, infinite-bus (SMIB) grid with adjustable 
short-circuit ratio (SCR). The example shows the DLL starting up, in 
preparation for a transient event to be applied at t=4.0 seconds. It 
requires `gfm_gfl_ibr2.dll` to run in ATP. 

.. image:: ../atp/data/smib_network.png

.. image:: ../atp/data/smib.png




