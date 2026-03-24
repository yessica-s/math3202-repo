
""" my code:"""
import gurobipy as gp

#Sets
telescopes = ["AU1", "CL1", "SA1", "AU2", "CL2", "HI1"]
larger_telescopes = ["CL1", "CL2"]
days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]

T = range(len(telescopes))
D = range(len(days))

#Data
efficiency = [0.99, 0.99, 0.93, 0.41, 0.40, 0.33] #efficiency in detecting NEOs
discovery_rate = [2.4, 3.4] #discovery rate per belt (hourly) - main, neo respectively
total_visibility_per_day = [4.8, 5.5, 6.5, 4.7, 5.4, 5.6, 6.1]
neo_visibility_per_day = [3.3, 3.9, 4.0, 3.6, 3.6, 3.8, 4.8]
maxData = 500 #GB per day
dataPerTelescope = 25 #GB per day
minUsage = 10 #hrs per week per telescope

#Setup model
m = gp.Model("ASC")

#Create variables
X = {} #hrs per telescope per day main/total belt
Y = {} #hrs per telescope per day on neo belt
H = {} #total hrs of telescope use per day
S = {}
for t in T:
    for d in D:
        X[t, d] = m.addVar(vtype=gp.GRB.CONTINUOUS)
        Y[t, d] = m.addVar(vtype=gp.GRB.CONTINUOUS)
        # Add variable to track how many hours the telescopes are used
        H[t,d] = m.addVar(vtype=gp.GRB.CONTINUOUS)

for d in D:
    S[d] = m.addVar(vtype=gp.GRB.CONTINUOUS)

#Objective
m.setObjective(gp.quicksum(efficiency[t]*discovery_rate[0]*X[t, d]+efficiency[t]*discovery_rate[1]*Y[t, d] for d in D for t in T), gp.GRB.MAXIMIZE)

#Add constraints
for t in T:
    for d in D:
        if telescopes[t] in larger_telescopes:
            m.addConstr(Y[t, d] <= neo_visibility_per_day[d])
            m.addConstr(X[t, d] <= total_visibility_per_day[d])

            # track hrs, choose max between neo and main belt observing hours since simultaneous
            m.addConstr(H[t, d] >= X[t, d])
            m.addConstr(H[t, d] >= Y[t, d])
        else:
            m.addConstr(Y[t, d] <= neo_visibility_per_day[d])
            m.addConstr(X[t, d] + Y[t, d] <= total_visibility_per_day[d])

            # track hrs, sum hours observing neo belt and main belt
            m.addConstr(H[t, d] == X[t, d] + Y[t, d])
    m.addConstr(gp.quicksum(H[t, d] for d in D) >= minUsage)


# #todo: our original comm5 answer - improves discoveries
# for d in D:
#     if d > 0:
#         m.addConstr(S[d] >= S[d-1] + gp.quicksum(H[t, d] for t in T) * dataPerTelescope - maxData)
#     else:
#         # monday
#         m.addConstr(S[d] == gp.quicksum(H[t, d] for t in T) * dataPerTelescope - maxData)
#     m.addConstr(S[d] <= maxData)

# todo: maybe the new answer? but doesnt' impact discoveries.
for d in D:
    if d == 0:
        # Monday
        m.addConstr(S[d] >= S[6] + gp.quicksum(H[t, d] for t in T) * dataPerTelescope - maxData)
    else:
        m.addConstr(S[d] >= S[d-1] + gp.quicksum(H[t, d] for t in T) * dataPerTelescope - maxData)
    m.addConstr(S[d] <= maxData)  # cannot store more than daily capacity
    m.addConstr(S[d] >= 0)        # cannot store negative data

#Run model
m.optimize()

for t in T:
    print(f"Hours on main belt on {telescopes[t]}: {sum(X[t, d].x for d in D)}")
    print(f"Hours on neo belt on {telescopes[t]}: {sum(Y[t, d].x for d in D)}")

#Find optimal discoveries
print(m.ObjVal)









# """ marees code """
# import gurobipy as gp
#
# # SETS
# telescopes = ["AU1", "CL1", "SA1", "AU2", "CL2", "HI1"]
# efficiencies = [0.99, 0.99, 0.93, 0.41, 0.40, 0.33] #efficiency in detecting NEOs
# neo_discovery_rate = [2.4, 3.4] #discovery rate per belt (hourly)
# total_hrs = [4.8, 5.5, 6.5, 4.7, 5.4, 5.6, 6.1]
# neo_belt_hrs = [3.3, 3.9, 4.0, 3.6, 3.6, 3.8, 4.8]
# extra_main_hrs = [3.3, 3.9, 4.0, 3.6, 3.6, 3.8, 4.8]
# days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#
#
# index_cl2 = 4
# index_cl1 = 1
# minUsage = 10  # hrs per week per telescope
# maxData = 500  # GB per day
# dataPerTelescope = 25  # GB per day
#
# E = range(len(efficiencies))
# D = range(len(days))
#
# m = gp.Model("MATH3202 - A1")
#
# # VARIABLES
# MH = {}  # Main belt hours
# BH = {}  # Neo belt hours
# SD = {}  # Stored data per day
# for d in D:
#     SD[d] = m.addVar(vtype=gp.GRB.CONTINUOUS)
#     for e in E:
#         MH[e, d] = m.addVar(vtype=gp.GRB.CONTINUOUS)
#         BH[e, d] = m.addVar(vtype=gp.GRB.CONTINUOUS)
#
# # OBJECTIVE
# m.setObjective(
#     gp.quicksum(efficiencies[e] * (MH[e, d] * neo_discovery_rate[0] + BH[e, d] * neo_discovery_rate[1]) for e in E for d in D)
#     + efficiencies[index_cl2] * (gp.quicksum(BH[index_cl2, d] * neo_discovery_rate[0] for d in D))
#     + efficiencies[index_cl1] * (gp.quicksum(BH[index_cl1, d] * neo_discovery_rate[0] for d in D)),
#     gp.GRB.MAXIMIZE
# )
#
# # CONSTRAINTS
# for e in E:
#     for d in D:
#         m.addConstr(MH[e, d] + BH[e, d] <= total_hrs[d])
#         m.addConstr(BH[e, d] <= neo_belt_hrs[d])
# for e in E:
#     m.addConstr(gp.quicksum(MH[e, d] + BH[e, d] for d in D) >= minUsage)
#
# for d in D:
#     daily_data = gp.quicksum(dataPerTelescope * (MH[e, d] + BH[e, d]) for e in E)
#
#     if d == 0:  # Monday
#         m.addConstr(SD[d] == daily_data - maxData)
#     else:
#         m.addConstr(SD[d] == SD[d-1] + daily_data - maxData)
#
#     m.addConstr(SD[d] <= maxData)
#
# # RESULTS
# m.optimize()
# print("Total NEOs discovered is", m.ObjVal)
#







