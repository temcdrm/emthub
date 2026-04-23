@echo off
call clean.bat

for /L %%i in (0,1,3) do (
    emthub-extract-case %%i
    python raw_to_rdf.py %%i
    python bps_make_mpow.py %%i
    python mpow.py %%i
    python ic_to_rdf.py %%i
    python cim_to_atp.py %%i
    )

emthub-extract-case 4
python create_smib_dll.py 4
python cim_to_atp.py 4
