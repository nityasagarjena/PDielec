python=$1
shift
params=$*
$python ../../../pdielec $params -matrix ptfe -sigma 5 -needle 0 0 1 -ellipsoid 0 0 1 0.5 -plate 1 0 0 qua_hf_2d_f_ir-int.out -optical_tensor 2.018 0 0 0 2.018 0 0 0 2.071  -masses program -csv command.csv  $*
