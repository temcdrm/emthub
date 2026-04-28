#!/bin/bash

for i in {0..3}
do
    emthub-extract-case $i
    python3 raw_to_rdf.py $i
    python3 bps_make_mpow.py $i
    python3 mpow.py $i
    python3 ic_to_rdf.py $i
    python3 cim_to_atp.py $i
done

emthub-extract-case 4
python3 create_smib_dll.py 4
python3 cim_to_atp.py 4

python3 cim_summary.py
