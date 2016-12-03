""" A subclass of a constraint problem to solve an n-queens problem of
    a given size with a given solver """
# Patrick Custer
from constraint import *

class NQ(Problem):

    def __init__(self, n=8, solver=None):

        """N is the size of the board, solver is the CSP solver
           that will be used to sove the problem """

        # call the base class init method
        super(NQ, self).__init__(solver=solver)

        # set any NQ instance variables needed
        # define CSP variables with their domains
        # add CSP constraints 
        cols = range(n)
        rows = range(n)
        self.addVariables(cols, rows)
        for col1 in cols:
            for col2 in cols:
                if col1 < col2:
                    self.addConstraint(lambda row1, row2, col1=col1, col2=col2: abs(row1-row2) != abs(col1-col2) and row1 != row2, (col1, col2))
        solutions = self.getSolution()
