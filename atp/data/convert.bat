rem python ..\src\pl4_to_pd5.py IBRCall
rem python ..\src\plot_pd5.py IBRCall.hdf5

rem python ..\src\pl4_to_pd5.py SyncMachCall
rem python ..\src\pl4_to_pd5.py IEEE118
python ..\src\pl4_to_pd5.py WECC240

rem python ..\src\plot_pd5.py SyncMachCall.hdf5
rem python ..\src\plot_pd5.py IEEE118.hdf5
rem python ..\src\plot_pd5.py WECC240.hdf5

rem python ..\src\plot118.py
python ..\src\plot240.py
