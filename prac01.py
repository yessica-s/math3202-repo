import gurobipy as gp

""" v2 """

#Sets
cakes = ["Choc", "Plain"]
ingredients = ["Eggs", "Time", "Milk"]

#Data
revenue = [4, 2]                    # revenue per cake
availability = [30, 480, 5000]      # of ingredients
usage = [
            [4, 20, 250],           # usage per ingredient for chocolate cake
            [1, 50, 200]            # usage per ingredient for plain cake
        ]

#Setup Model
m = gp.Model("Farmer Jones")

#Create variables
X = {}
for c in range(len(cakes)):
    X[c] = m.addVar()

#Objective (to optimize)
m.setObjective(gp.quicksum(revenue[c]*X[c] for c in range(len(cakes))), gp.GRB.MAXIMIZE)

#Add constraints
for i in range(len(ingredients)):
    m.addConstr(gp.quicksum(usage[c][i]*X[c] for c in range(len(cakes))) <= availability[i])

#Run model
m.optimize()

#Find number of each cake
for c in range(len(cakes)):
    print(f"Make {X[c].x} {cakes[c]}")

    # X[n].lb = lowerbound
    # X[n].ub = upperbound
    # X[n].obj = coefficient in objective
    # where n is variable

print(f"Revenue is {m.ObjVal}")










""" 
v1 
    - hardcoded variables & constraints
"""

"""
#Setup Model
m = gp.Model("Farmer Jones")

#Create variables
#  - default non-negative constraints
x1 = m.addVar()
x2 = m.addVar()

#Objective (to optimize)
m.setObjective(4*x1+2*x2, gp.GRB.MAXIMIZE)

#Add constraints
#Matrix: 
#   - number of rows = number of constraints
#   - number of columns = number of variables
m.addConstr(4*x1 + x2 <= 30)            # eggs
m.addConstr(20*x1 + 50*x2 <= 480)       # time
m.addConstr(250*x1 + 200*x2 <= 5000)    # milk

#Run model
m.optimize()

#Find number of each cake
print(f"Make {x1.x} chocolate") #chocolate
print(f"Make {x2.x} plain") #plain
"""