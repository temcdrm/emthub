call c:\atp\atpmingw\mytpbig smib.atp > smib.lis
python ..\src\pl4_to_pd5.py smib
rem python ..\src\plot_pd5.py smib.hdf5
python ..\src\plot_smib.py

