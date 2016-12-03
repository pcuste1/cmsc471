#! /bin/csh
echo "running tests"
touch test.out
echo; echo "PROBLEM P00"; echo
blackbox -o domain.pddl -f p00.pddl >> test.out
echo; echo "PROBLEM P0"; echo
blackbox -o domain.pddl -f p0.pddl >> test.out
echo; echo "PROBLEM P1"; echo
blackbox -o domain.pddl -f p1.pddl >> test.out
echo; echo "PROBLEM P2"; echo
blackbox -o domain.pddl -f p2.pddl >> test.out
echo; echo "PROBLEM P3"; echo
blackbox -o domain.pddl -f p3.pddl >> test.out
echo; echo "PROBLEM P4"; echo
blackbox -o domain.pddl -f p4.pddl >> test.out

