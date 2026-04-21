import gurobipy as gp

# Data
profit = [10, 6, 8, 4, 11, 9, 3]
P = range(len(profit))

Machines = ["Grinding","VDrilling","HDrilling","Boring","Planing"]
n = [4, 2, 3, 1, 1]
M = range(len(n))

# usage[P][M]
usage = [
    [0.5, 0.1, 0.2, 0.05, 0.00],
    [0.7, 0.2, 0.0, 0.03, 0.00],
    [0.0, 0.0, 0.8, 0.00, 0.01],
    [0.0, 0.3, 0.0, 0.07, 0.00],
    [0.3, 0.0, 0.0, 0.10, 0.05],
    [0.2, 0.6, 0.0, 0.00, 0.00],
    [0.5, 0.0, 0.6, 0.08, 0.05]
    ]

# months
T = range(6)

# maintenance[T][M]
maint = [
    [1, 0, 0, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1]
    ]

# market[P][T]
market = [
    [ 500, 600, 300, 200,   0, 500],
    [1000, 500, 600, 300, 100, 500],
    [ 300, 200,   0, 400, 500, 100],
    [ 300,   0,   0, 500, 100, 300],
    [ 800, 400, 500, 200,1000,1100],
    [ 200, 300, 400,   0, 300, 500],
    [ 100, 150, 100, 100,   0,  60]
    ]

maxstore = 100
storecost = 0.5
endstore = 50
initialstore = 0
monthhours = 16*24

fp = gp.Model("Factory Planning")

#Variables
X = {(p,t): fp.addVar() for p in P for t in T} #product p made in month T
Y = {(p,t): fp.addVar() for p in P for t in T} #product p sold in month T
S = {(p,t): fp.addVar() for p in P for t in T} #product p stored in month T

#Objective
fp.setObjective(gp.quicksum(Y[p,t]*profit[p] for p in P for t in T)-
                gp.quicksum(storecost*S[p,t] for p in P for t in T),
                gp.GRB.MAXIMIZE)

# Constraints
for t in T:
    for m in M:
        fp.addConstr(gp.quicksum(usage[p][m]*X[p,t] for p in P) <= n[m]*monthhours - maint[t][m]*monthhours)
#...need to add more here - see solution file

fp.optimize()
print(fp.ObjVal)
