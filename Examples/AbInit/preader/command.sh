python=$1
shift
params=$*
$python ../../../preader $params -program abinit -masses program -mass Al 25.98689169 -neutral -eckart ../AlAs/AlAs.out ../BaTiO3/BaTiO3.out ../Na2SO42/Na2SO42.out
