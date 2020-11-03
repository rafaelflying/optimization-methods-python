from pulp import *

# Initialize Class
model = LpVariable('TV Commercial', LpMinimize)

# Define Decision Variables
A = LpVariable('A', lowBound=3, upBound=999, cat='Integer')
B = LpVariable('B', lowBound=2, upBound=999, cat='Integer')
C = LpVariable('C', lowBound=5, upBound=10, cat='Integer')
D = LpVariable('D', lowBound=5, upBound=10, cat='Integer')

# Define Objective Function
model += 4000000 * A + 90000 * B + 500000 * C + 200000 * D

# Define Constraints
model += 40000 * A + 75000 * B + 30000 * C + 15000 * D - 800000
model += 30000 * A + 400000 * B + 200000 * C + 100000 * D - 2000000
model += 40000 * A + 75000 * B - 500000

# Solve Model
model.solve()
print(A.varValue)
print(B.varValue)
print(C.varValue)
print(D.varValue)

