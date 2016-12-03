from __future__ import print_function
from constraint import *
from timeout import timeout
import time, sys

@timeout(30)
def nxn(prob, numSquares):
    start = time.time()
    n2 = numSquares**2
    magicSum = numSquares * ( n2 + 1 ) / 2
    problem = Problem(prob)

    problem.addVariables(range(0, n2), range(1, n2+1))
    problem.addConstraint(AllDifferentConstraint(), range(0, n2))
    problem.addConstraint(ExactSumConstraint(magicSum), [i for i in range(0, n2, 5)])
    problem.addConstraint(ExactSumConstraint(magicSum), [i for i in range(0, n2-1, 3)])
    for row in range(numSquares):
        problem.addConstraint(ExactSumConstraint(magicSum), [row*numSquares+i for i in range(numSquares)])
    for col in range(numSquares):
        problem.addConstraint(ExactSumConstraint(magicSum), [col+numSquares*i for i in range(numSquares)])

    solutions = problem.getSolution()
    print("\033[1;30;48mRan in -- {}\033[0m".format(time.time()-start))
    if(solutions):
        for i in range(n2):
            if i % numSquares == 0 and i != 0:
                print()
            num = solutions[i]
            print(repr(num).rjust(2),end=" ")
    else:
        print("No solution found")
            
def run_n_test(numSquares):
    try:
        print("{s:{c}^{n}}".format(s="Backtracking Solver",n=60,c='-'))
        nxn(BacktrackingSolver(),numSquares)
    except:
        print("Backtracking Solver took over 30 seconds and was terminated.",end="")
    try:
        print("\n\n{s:{c}^{n}}".format(s="Recursive Backtracking Solver",n=60,c='-'))
        nxn(RecursiveBacktrackingSolver(),numSquares)
    except:
        print("Backtracking Solver took over 30 seconds and was terminated.",end="")
    try:
        print("\n\n{s:{c}^{n}}".format(s="Minimum Conflicts Solver",n=60,c='-'))
        nxn(MinConflictsSolver(),numSquares)
    except:
        print("Backtracking Solver took over 30 seconds and was terminated.",end="")
                
if __name__ == "__main__":
    #print(len(sys.argv))
    if len(sys.argv) != 2:
        print("\033[1;31;48m-----Arguement missing: input [test] or [single-run] to run this program\033[0m")
        sys.exit()
    if sys.argv[1] == "test":
        for i in range(3,6):
            print("\033[1;32;48m{s:{c}^{n}}\033[0m".format(s="Testing Solvers for a {}x{} magic square".format(i,i),n=60,c='='))
            run_n_test(i)
            print()
    else:
        numSquares = int(input("Please enter the size N for the NxN magic square: "))
        run_n_test(numSquares)
