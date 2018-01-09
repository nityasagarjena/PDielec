python=$1
shift
params=$*
$python ../../../pdielec $params  -LO 1 0 0 -vmin 300 -vmax 800 -sphere -needle 0 0 1 -dielectric 3  -vf 0.1 -vf 0.2 -method maxwell -method bruggeman  -method ap -sigma 10 -csv command.csv phonon  $*
