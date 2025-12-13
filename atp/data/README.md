# ATP System Examples

The ATP netlists for _XfmrSat_, _IEEE39_, _IEEE118_, and _WECC240_ examples were created from 
scripts and rawfiles located in the sibling _../../CIM_ directory. Python scripts to convert outputs
to COMTRADE and plot them are located in the sibling _../src_ directory.

To run these examples:

- _go.bat_: Runs ATP from the command line. Edit this file to select which case to run.
- _convert.bat_: Converts and plots the ATP output. Edit this file to select which case to post-process.

Other files of interest:

- _\*_net.atp_: ATP network data produced by the CIM scripts. These should not be edited by the user.
- _\[XfmrSat|IEEE39|IEEE118|WECC240].atp_: Four specific top-level ATP example files. These may be edited.
- _\*.prm_: Sets ATP parameters, called from the _\*.atp_ files. These may be edited.
- _\*.atpmap_: Lists the CIM buses that correspond to each ATP bus (ATP buses must be numbered sequentially).
- _clean.bat_: Deletes ATP temporary files.

Supporting files, of interest to experienced ATP users:

- _\*.acp_: ATPDraw files to help develop subsystem models.
- _\*.atp_: ATP scripts to help develop subsystem models.
- _\*.dbm_: Input files for the ATP subsystem compiler.
- _\*.pch_: Compiled subsystem models called by ATP.

## Load Rejection of a Transformer-Terminated Line

This example disconnects 400 MW of load from the end of a 500-km transformer-terminated line. It
demonstrates the CIM extension for transformer saturation.

![Results with Saturation of Transformer Core](XfmrSat.png)

![Results with Linear Transformer Core](XfmrLinear.png)

## IEEE 39-bus Example with IBR

## IEEE 118-bus Example with IBR

## WECC 240-bus Example with IBR


Copyright &copy; 2024-25, Meltran, Inc
