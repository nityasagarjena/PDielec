python ../../../pdielec -matrix ptfe -sigma 5 -method maxwell -method bruggeman -method ap -vf 0.1\
                         -needle 0 0 1 -ellipsoid 0 0 1 0.5 -plate 1 0 0 \
                         -LO 1 1 1 \
                         -csv command.csv \
                         -neutral -program phonopy vasp VASP/OUTCAR  $*