import numpy as np
from scipy.optimize import minimize

# describe the objective function, x[0] = fist number
objective_fcn = lambda x: 4 * x[0] + 2 * x[1] + 3 * x[2]

# define the constraints, use 'eq' for equality and 'ineq' for inequality
constraint = [{'type': 'ineq', 'fun': lambda x: 7 * x[0] + 3 * x[1] + 6 * x[2] - 150},
              {'type': 'ineq', 'fun': lambda x: 4 * x[0] + 4 * x[1] + 5 * x[2] - 200}]

#x0 = initial value for the optimization
x0 = [1, 1, 1]

#bounds = the limits for the equation
bounds = [(0, None), (0, None), (0, None)]

#method may vary
result = minimize(objective_fcn, x0, method='SLSQP', bounds=bounds, constraints=constraint)

print(result)
