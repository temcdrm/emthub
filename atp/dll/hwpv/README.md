## HWPV DLL Example

Files to run this example:

- _Ex_HWPV.atp_: a standalone call to the DLL. No grid is connected.
- _hwpv.acp_: an ATPDraw file with the HWPV connected to a network.
- _hwpv.atp_: an ATP netlist, produced from ATPDraw, with the HWPV connected to a network.
- _hwpv.mod_: the HWPV component for ATP's MODELS, suitable for use in ATPDraw.

These files are not essential, but provide some context for the example:

- _GFM_v8.acp_: an ATPDraw file with the three-phase, average model, 100-kW GFM used to train the HWPV model.
- _GFM_v8.atp_: an ATP netlist, produced from ATPDraw, with a three-phase average model GFM.
- _pv1_osg.acp_: an ATPDraw file with a single-phase, switching model of an IBR, used to train a different HWPV model. This may be used for testing the DLL at a later time. The HWPV model takes approximately the same simulation time as the average model used to train it, for the same time step. The HWPV model is expected to run much faster than a switching model used to train it.
- _pv1_osg.atp_: an ATP netlist, produced from ATPDraw, tiwht a single-phase switching model IBR.

Copyright &copy; 2024-25, Meltran, Inc

