import gurobipy as gp

# Sets
Oils = ["Veg 1", "Veg 2", "Oil 1", "Oil 2", "Oil 3"]
I = range(len(Oils))

Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
T = range(len(Months))

# Data
veg = ["Veg" in Oils[i] for i in I]
h = [8.8, 6.1, 2.0, 4.2, 5.0]
c = [[110, 130, 110, 120, 100,  90], 
     [120, 130, 140, 110, 120, 100],
     [130, 110, 130, 120, 150, 140], 
     [110,  90, 100, 120, 110,  80], 
     [115, 115,  95, 125, 105, 135]]
jan = [c[i][0] for i in I]

MaxV = 200
MaxN = 250
Sell = 150
MinH = 3
MaxH = 6

StoreCost = 5
StoreMax = 1000
Initial = 500

m = gp.Model("Oil")

# Variables
X = {(i, t): m.addVar() for i in I for t in T} #blend
Y = {(i, t): m.addVar() for i in I for t in T} #purchase
S = {(i, t): m.addVar() for i in I for t in T} #store

# Objective
m.setObjective((gp.quicksum(X[i,t]*Sell for i in I for t in T) -
                gp.quicksum(c[i][t]*Y[i,t] for i in I for t in T) -
                gp.quicksum(StoreCost*S[i,t] for i in I for t in T)), gp.GRB.MAXIMIZE)

# Constraints
for t in T:
     #tonnage constraints
     m.addConstr(gp.quicksum(X[i,t] for i in I if veg[i]) <= MaxV)
     m.addConstr(gp.quicksum(X[i,t] for i in I if not veg[i]) <= MaxN)

     #hardness constraints
     m.addConstr(gp.quicksum((h[i]-MaxH)*X[i,t] for i in I) <= 0)
     m.addConstr(gp.quicksum((MinH-h[i])*X[i,t] for i in I) <= 0)

#inventory constraint
for i in I:
     m.addConstr(S[i, 5] >= Initial)
     for t in T:
          m.addConstr(S[i,t] <= StoreMax)
          if t == 0: #jan
               m.addConstr(S[i,0] == Initial + Y[i,0] - X[i,0])
          else:
               m.addConstr(S[i, t] == S[i, t-1] + Y[i, t] - X[i, t])

m.optimize()

# Print amount of each oil
for t in T:
     print(Months[t])
     print("Buy", [round(Y[i, t].x, 1) for i in I])
     print("Blend", [round(X[i, t].x, 1) for i in I])
     print("Store", [round(S[i, t].x, 1) for i in I])



print(m.objVal)


# print("Hardness", sum(h[i]*X[i,t].x for i in I)/sum(X[i].x for i in I))
