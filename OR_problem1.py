import numpy as np
from scipy.optimize import minimize


def objective_fcn(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    return 4 * x1 + 2 * x2 + 3 * x3 #maximize

def inequality_constraint1(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    return 7*x1 + 3*x2 + 6*x3 - 150

def inequality_contratint2(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    return 4*x1 + 4*x2 + 5*x3 -200

bounds_x1 = (0, 999)
bounds_x2 = (0, 999)
bounds_x3 = (0, 999)

bounds = [bounds_x1, bounds_x2, bounds_x3]

constraint1 = {'type': 'ineq', 'fun': inequality_constraint1}
constraint2 = {'type': 'ineq', 'fun': inequality_contratint2}

constraints = [constraint1, constraint2]

x0 = [1, 1, 1]

result = minimize(objective_fcn, x0, method='SLSQP', bounds= bounds, constraints=constraints)

print(result)


