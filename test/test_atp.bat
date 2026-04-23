@echo off

for /L %%i in (0,1,0) do (
    python atp.py %%i "run"
    python atp.py %%i "convert"
    python atp.py %%i "plot"
    )


