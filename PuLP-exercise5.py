from pulp import *

# Inialize Class
problem = LpProblem('PuLP Exercise 6', LpMaximize)

# Define Decision Variables
x1 = LpVariable('x1', lowBound=0)
x2 = LpVariable('x2', lowBound=0)

# Define Objective Function
problem += 2*x1 + 3*x2

# Define Constraints
problem += x1 + x2 <= 10
problem += 2*x1 + x2 <= 15

# Solve With Default Solver
solution = problem.solve()

# Output information if optimum was found
#" ; x1_opt = "+str(pulp.value(x1))
#" : x2_opt = "+str(pulp.value(x2))

print("Status:", LpStatus[problem.status])
print(f'Optimal value for x1 = {x1.value()}')
print(f'Optimal value for x1 = {x2.value()}')
