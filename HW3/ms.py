""" A subclass of a constraint problem to find a magic square for a
    nxn grid and sum n*(n*n+1)/2. """
# Patrick Custer

from constraint import *
import time

class MS(Problem):

    def __init__(self, n=3, solver=None):

        """N is the size of the magic square, solver is the CSP solver
           that will be used to sove the problem """

        # call the base class init method
        super(MS, self).__init__(solver=solver)

        # set any MS instance variables needed
        # define CSP variables with their domains
        # add CSP constraints 
        start = time.time()
        numSquares = n
        n2 = numSquares**2
        magicSum = numSquares * ( n2 + 1 ) / 2
        
        self.addVariables(range(0, n2), range(1, n2+1))
        self.addConstraint(AllDifferentConstraint(), range(0, n2))
        self.addConstraint(ExactSumConstraint(magicSum), [i for i in range(0, n2, n+1)])
        self.addConstraint(ExactSumConstraint(magicSum), [i for i in range(0, n2-1, n)])
        for row in range(numSquares):
            self.addConstraint(ExactSumConstraint(magicSum), [row*numSquares+i for i in range(numSquares)])
        for col in range(numSquares):
            self.addConstraint(ExactSumConstraint(magicSum), [col+numSquares*i for i in range(numSquares)])

        solutions = self.getSolution()
        
