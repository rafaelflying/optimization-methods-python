from pulp import *

# Inialize Class
model = LpProblem('Exercise4', LpMaximize)

# Define Decision Variables
x1 = LpVariable('x1', lowBound=0, cat='Continuous')
x2 = LpVariable('x2', lowBound=0, cat='Continuous')

# Define Objective Function
model += 60*x1 + 9*x2

# Define Constraints
model += x1 <= 10
model += x2 <= 58
model += 2*x2 <= 20
model += 6*x1 + 9*x2 <= 20

# Solve Model
model.solve()

# Print Solution
for v in model.variables():
    print(v.name, '=', v.varValue)

# Show Object function Value
print('Objective funcion value = ', value(model.objective))





