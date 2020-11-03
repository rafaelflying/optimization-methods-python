from pulp import *

# Initialize Class
model = LpProblem("Maximaze Bakery Profits", LpMaximize)

# Define Decision Variable
A = LpVariable('A', lowBound=0, cat='Integer')
B = LpVariable('B', lowBound=0, cat='Integer')

# Define Objective Function
model += 20 * A + 40 * B

# Define Constraints
model += 0.5 * A + 1 * B <= 30
model += 1 * A + 2.5 * B <= 60
model += 1 * A + 2 * B <= 22

# Solve Model
model.solve()
print(f'Produce {A.varValue} Cake A')
print(f'Produce {B.varValue} Cake B')

