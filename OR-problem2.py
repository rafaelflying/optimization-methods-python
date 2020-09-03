import numpy as np
from scipy.optimize import minimize


def objective_fcn(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    return 400000 * x1 + 900000 * x2 + 500000 * x3 + 200000 * x4


# Budged
def inequality_constraint1(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    return 40000 * x1 + 75000 * x2 + 30000 * x3 + 15000 * x4 - 800000


# Woman reached
def inequality_constraint2(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    return 300000 * x1 + 400000 * x2 + 200000 * x3 + 100000 * x4 - 2000000

#Spent with TV
def inequality_constraint3(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    return 40000*x1 + 75000*x2 - 500000

bounds_x1 = (3, 999) #tv horário nobre
bounds_x2 = (2, 999) #TV horário normal
bounds_x3 = (5, 10) #Rário
bounds_x4 = (5, 10) #Revistas

bounds = [bounds_x1, bounds_x2, bounds_x3, bounds_x4]

constraint1 = {'type': 'ineq', 'fun': inequality_constraint1}
constraint2 = {'type': 'ineq', 'fun': inequality_constraint2}
constraint3 = {'type': 'ineq', 'fun': inequality_constraint3}

constraints = [constraint1, constraint2, constraint3]

x0 = [1, 1, 1, 1]

result = minimize(objective_fcn, x0, method='SLSQP', bounds=bounds, constraints=constraints)

print(result)






