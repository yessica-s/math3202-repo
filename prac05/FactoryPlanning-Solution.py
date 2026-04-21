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
target = [sum(maint[t][m] for t in T) for m in M]

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

fp.setParam("OutputFlag", 1)

# Variables
# X[p,t] is amount to make
X = { (p,t): fp.addVar() for p in P for t in T }

# Y[p,t] is amount to sell
Y = { (p,t): fp.addVar() for p in P for t in T }

# S[p,t] is amount to store
S = { (p,t): fp.addVar() for p in P for t in T }

# Z[t,m] number of machines m to maintain in month t
Z = { (t,m): fp.addVar(vtype=gp.GRB.INTEGER) for t in T for m in M }

# Objective
fp.setObjective(gp.quicksum(profit[p]*Y[p,t] for p in P for t in T) -
                gp.quicksum(storecost*S[p,t] for p in P for t in T), gp.GRB.MAXIMIZE)

# Constraints

for t in T:
    for m in M:
        fp.addConstr(gp.quicksum(usage[p][m]*X[p,t] for p in P) <= 
                     n[m]*monthhours - Z[t,m]*monthhours)
        
    for p in P:
        fp.addConstr(Y[p,t] <= market[p][t])
        if t > 0:
            fp.addConstr(S[p,t] == S[p,t-1] + X[p,t] - Y[p,t])
        else:
            fp.addConstr(S[p,0] == X[p,0] - Y[p,0])
            
        fp.addConstr(S[p,t] <= maxstore)
              
for p in P:
    fp.addConstr(S[p,5] >= endstore)

for m in M:
    fp.addConstr(gp.quicksum(Z[t,m] for t in T) == target[m])

for t in T:
    fp.addConstr(gp.quicksum(Z[t,m] for m in M) >= 1)
    
    fp.addConstr(gp.quicksum(Z[t,m] for m in M) <= 2)
    
fp.optimize()

print("Total profit",fp.objVal)

print("Make")
for p in P:
    print(p,[round(X[p,t].x,1) for t in T])

print("Sell")
for p in P:
    print(p,[round(Y[p,t].x,1) for t in T])

print("Store")
for p in P:
    print(p,[round(S[p,t].x,1) for t in T])  
    
print("Maintain")
for m in M:
    print(m,[round(Z[t,m].x) for t in T])  