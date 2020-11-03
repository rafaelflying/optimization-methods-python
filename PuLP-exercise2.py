from pulp import *

# Initialize Class
model = LpProblem('OR Problem3', LpMinimize)

# Define Decision Variables
A = LpVariable('A', lowBound=0, cat='Integer')
B = LpVariable('B', lowBound=0, cat='Integer')
C = LpVariable('C', lowBound=0, cat='Integer')

# Define Objective Function
model += 4 * A + 2 * B + 3 * C

# Define Constraints
model += 7 * A + 3 * B + 6 * C - 150
model += 4 * A + 4 * B + 5 * C - 200

# Solve Problem
model.solve()
print(A.varValue)
print(B.varValue)
print(C.varValue)
