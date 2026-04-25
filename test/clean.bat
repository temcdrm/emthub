@echo off
rem cleaning up input files for CIM RDF
del *.dyr 2>nul
del *.raw 2>nul
del *_Network.json 2>nul
del *_mRIDs.dat 2>nul

rem clean up my local scripts
del raw_to_rdf.py 2>nul
del bps_make_mpow.py 2>nul
del mpow.py 2>nul
del ic_to_rdf.py 2>nul
del cim_to_atp.py 2>nul
del atp.py 2>nul
del create_smib_dll.py 2>nul
del plot_bps.py 2>nul
del cim_summary.py 2>nul

rem clean up after MATPOWER
del solve*.m 2>nul
del *Solved.m 2>nul
del matpower_*.m 2>nul
git checkout *summary.txt 2>nul

rem clean up after ATP
del IEEE39.atp 2>nul
del IEEE118.atp 2>nul
del WECC240.atp 2>nul
del XfmrSat.atp 2>nul
del SMIBDLL.atp 2>nul
del *.atpmap 2>nul
del *.prm 2>nul
del *.lis 2>nul
del *.dbg 2>nul
del fort.* 2>nul
del *.pl4 2>nul
del commands.script 2>nul
del *.log 2>nul
del *.tmp 2>nul
del *.bin 2>nul
del *.pch 2>nul
del *.hdf5 2>nul
rem these are COMTRADE intermediate files
del *.dat 2>nul
del *.cfg 2>nul
rem still relevant?
del README.html 2>nul
del *.mod 2>nul
del *.png 2>nul

