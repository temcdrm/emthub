@echo off

for /L %%i in (0,1,4) do (
    python atp.py %%i "run"
    python atp.py %%i "convert"
    rem python atp.py %%i "plot"
    )


