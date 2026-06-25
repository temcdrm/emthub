@echo off
rem (skip) cleaning up input files for CIM RDF

rem (skip) clean up my local scripts

rem (soft) clean up after MATPOWER
del solve*.m 2>nul
del *Solved.m 2>nul
git checkout *summary.txt 2>nul

rem (soft) clean up after ATP, leave the inputs and final outputs
del *.lis 2>nul
del *.dbg 2>nul
del fort.* 2>nul
del *.pl4 2>nul
del commands.script 2>nul
del *.log 2>nul
del *.tmp 2>nul
del *.bin 2>nul
del *.dat 2>nul
del *.cfg 2>nul
del *.png 2>nul
