rem cleaning up input files for CIM RDF
del *.dyr
del *.raw
del *_Network.json
del *_mRIDs.dat

rem clean up after MATPOWER
del solve*.m
del *Solved.m
del matpower_*.m

rem clean up after ATP
del *_base.atp
del *.prm
del *.lis
del *.dbg
del fort.*
del *.pl4
del commands.script
del *.log
del *.tmp
del *.bin
del *.pch
del *.hdf5
rem these are COMTRADE intermediate files
del *.dat
del *.cfg
rem still relevant?
del README.html

