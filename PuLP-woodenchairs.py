from pulp import *

# Inialize Class
problem = LpProblem('Wooden Chairs', LpMaximize)

# Define Decision Variables
x1 = LpVariable('x1', lowBound=0, cat='Integer')
x2 = LpVariable('x2', lowBound=0, cat='Integer')

# Define Objective Function
problem += 20*x1 + 30*x2

# Define Constraints
problem += 1*x1 + 2*x2 <= 100
problem += 2*x1 + 1*x2 <= 100

# Display the LP problem
problem

# Solve with the default solver
status = problem.solve()

# Print the solution status
LpStatus[status] # total profit

# number of chair to manufacture
print(x1.varValue)
print(x2.varValue)

# LpStatusOptimal = 1

