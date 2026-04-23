call clean.bat

emthub-extract-case 0
python raw_to_rdf.py 0
python bps_make_mpow.py 0
python mpow.py 0
python ic_to_rdf.py 0
python cim_to_atp.py 0

rem emthub-extract-case 1

rem emthub-extract-case 2

rem emthub-extract-case 3

rem emthub-extract-case 4

