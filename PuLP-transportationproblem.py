from pulp import *

# SETS
GROVES = ['Mt.Dora', 'Eustis', 'Clermont']
PLANTS = ['Ocala', 'Orlando', 'Leesburg']

# Dictionary of max amount that can be shipped to each plant
maxship = {'Ocala': 200000,
           'Orlando': 600000,
           'Leesburg': 225000}

# Dictionary of amount each grove will supply
supply = {'Mt.Dora': 275000,
          'Eutis': 400000,
          'Clearmont': 300000}

# Dictionary of  miles for all groves and plants
bush = {'Mt.Dora': {'Ocala': 21, 'Orlando': 50, 'Leesburg': 40},
        'Eustis': {'Ocala': 35, 'Orlado': 30, 'Leesburg': 22},
        'Clermont': {'Ocala': 55, 'Orlando': 20, 'Leesburg': 25}}

# Set Problem Variable
prob = LpProblem("Transportation", LpMinimize)

routes = [(i, j) for i in GROVES for j in PLANTS]

# DECISION VARIABLE
amount_vars = LpVariable.dicts("ShipAmount", (GROVES, PLANTS),
                               0)

# OBJECTIVE FUNCTION
prob += lpSum(amount_vars[i][j] * bush[i][j] for (i, j) in routes)

# CONTRAINTS:
for j in PLANTS:
    prob += lpSum(amount_vars[i][j] for i in GROVES) <= maxship[j]

for i in GROVES:
    prob += lpSum(amount_vars[i][j] for j in PLANTS) == supply[i]

prob.solve()
print("Status:", LpStatus[prob.status])

for v in prob.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)

print("Total bushel-miles =", value(prob.objective))
