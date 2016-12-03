from constraint import *

problem = Problem()
problem.addVariable("a", [1,2,3])
problem.addVariable("b", [4,5,6])

problem.addConstraint(lambda a,b: a*2 == b, ("a", "b"))
print(problem.getSolutions())

problem = Problem()
problem.addVariables(["a", "b"],[1,2,3])

problem.addConstraint(AllDifferentConstraint())
print(problem.getSolutions())
