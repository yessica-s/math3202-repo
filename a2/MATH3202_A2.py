import gurobipy as gp
import sys

Skills = [
    "Electronics maintenance",
    "Mechanical maintenance",
    "Optics handling",
    "Software operation",
    "Instrument calibration",
    "Data acquisition",
    "Computing support",
    "Adaptive optics",
    "Cryogenics",
    "Network infrastructure",
    "Instrument integration",
    "Preventive maintenance",
    "Environment monitoring",
    "Technical reporting",
    "Management"
]

Days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
T = range(len(Days))

# Tasks to be completed (duration is in hours)
Tasks = [
    {'title': 'Structural and mechanical repairs', 'skill': 1, 'staff': 2, 'duration': 4, 'day': 0 },
    {'title': 'Adaptive optics system validation', 'skill': 7, 'staff': 1, 'duration': 2, 'day': 0 },
    {'title': 'Optical alignment checks', 'skill': 2, 'staff': 1, 'duration': 1, 'day': 0 },
    {'title': 'Testing weather\u2011monitoring systems', 'skill': 12, 'staff': 2, 'duration': 1, 'day': 0 },
    {'title': 'Assembly and testing of mechanical fixtures', 'skill': 1, 'staff': 1, 'duration': 3, 'day': 0 },
    {'title': 'Instrument calibration', 'skill': 4, 'staff': 2, 'duration': 2, 'day': 0 },
    {'title': 'Monitoring weather and system status', 'skill': 12, 'staff': 1, 'duration': 3, 'day': 0 },
    {'title': 'Cryogenic system checks', 'skill': 8, 'staff': 2, 'duration': 1, 'day': 0 },
    {'title': 'Testing remote\u2011observing systems', 'skill': 6, 'staff': 2, 'duration': 2, 'day': 0 },
    {'title': 'Drives and dome troubleshooting', 'skill': 1, 'staff': 2, 'duration': 2, 'day': 0 },
    {'title': 'Nightly telescope operation', 'skill': 3, 'staff': 2, 'duration': 8, 'day': 0 },
    {'title': 'Mentoring junior staff', 'skill': 14, 'staff': 1, 'duration': 2, 'day': 0 },
    {'title': 'Preparing dome and telescope for night operations', 'skill': 3, 'staff': 1, 'duration': 2, 'day': 0 },
    {'title': 'Updating and reviewing system logs', 'skill': 13, 'staff': 2, 'duration': 2, 'day': 0 },
    {'title': 'Documenting issues and proposed improvements', 'skill': 13, 'staff': 1, 'duration': 4, 'day': 0 },
    {'title': 'Preventive maintenance on control systems', 'skill': 11, 'staff': 2, 'duration': 3, 'day': 0 },
    {'title': 'Instrument data-acquisition monitoring', 'skill': 5, 'staff': 1, 'duration': 3, 'day': 0 },
    {'title': 'Facility maintenance (HVAC, water, power)', 'skill': 1, 'staff': 2, 'duration': 2, 'day': 0 },
    {'title': 'Adaptive optics system validation', 'skill': 7, 'staff': 1, 'duration': 3, 'day': 1 },
    {'title': 'Structural and mechanical repairs', 'skill': 1, 'staff': 3, 'duration': 4, 'day': 1 },
    {'title': 'Cryogenic system checks', 'skill': 8, 'staff': 2, 'duration': 1, 'day': 1 },
    {'title': 'Coordinating instrument upgrades', 'skill': 14, 'staff': 1, 'duration': 3, 'day': 1 },
    {'title': 'Testing weather\u2011monitoring systems', 'skill': 12, 'staff': 2, 'duration': 2, 'day': 1 },
    {'title': 'Software updates and testing', 'skill': 6, 'staff': 1, 'duration': 4, 'day': 1 },
    {'title': 'Preventive maintenance on control systems', 'skill': 11, 'staff': 1, 'duration': 3, 'day': 1 },
    {'title': 'Assisting astronomers with instrument setups', 'skill': 14, 'staff': 1, 'duration': 3, 'day': 1 },
    {'title': 'Sensor and actuator testing', 'skill': 0, 'staff': 1, 'duration': 3, 'day': 1 },
    {'title': 'Mentoring junior staff', 'skill': 14, 'staff': 1, 'duration': 1, 'day': 1 },
    {'title': 'Optical alignment checks', 'skill': 2, 'staff': 2, 'duration': 2, 'day': 1 },
    {'title': 'Safety tests (interlocks and motion limits)', 'skill': 11, 'staff': 1, 'duration': 2, 'day': 1 },
    {'title': 'Instrument data-acquisition monitoring', 'skill': 5, 'staff': 1, 'duration': 1, 'day': 1 },
    {'title': 'Documenting issues and proposed improvements', 'skill': 13, 'staff': 1, 'duration': 2, 'day': 1 },
    {'title': 'Preparing dome and telescope for night operations', 'skill': 3, 'staff': 1, 'duration': 2, 'day': 1 },
    {'title': 'Hardware installation and integration', 'skill': 10, 'staff': 3, 'duration': 5, 'day': 1 },
    {'title': 'Drives and dome troubleshooting', 'skill': 1, 'staff': 2, 'duration': 2, 'day': 1 },
    {'title': 'Nightly telescope operation', 'skill': 3, 'staff': 2, 'duration': 6, 'day': 1 },
    {'title': 'Assembly and testing of mechanical fixtures', 'skill': 1, 'staff': 1, 'duration': 2, 'day': 1 },
    {'title': 'Monitoring weather and system status', 'skill': 12, 'staff': 1, 'duration': 1, 'day': 1 },
    {'title': 'Electronics diagnostics and repair', 'skill': 0, 'staff': 1, 'duration': 2, 'day': 1 },
    {'title': 'Motorized component adjustments', 'skill': 1, 'staff': 1, 'duration': 1, 'day': 1 },
    {'title': 'Documenting issues and proposed improvements', 'skill': 13, 'staff': 1, 'duration': 4, 'day': 2 },
    {'title': 'Instrument calibration', 'skill': 4, 'staff': 1, 'duration': 1, 'day': 2 },
    {'title': 'Nightly telescope operation', 'skill': 3, 'staff': 2, 'duration': 7, 'day': 2 },
    {'title': 'Optical alignment checks', 'skill': 2, 'staff': 2, 'duration': 2, 'day': 2 },
    {'title': 'Drives and dome troubleshooting', 'skill': 1, 'staff': 2, 'duration': 3, 'day': 2 },
    {'title': 'Real-time fault troubleshooting', 'skill': 0, 'staff': 2, 'duration': 3, 'day': 2 },
    {'title': 'Assisting astronomers with instrument setups', 'skill': 14, 'staff': 1, 'duration': 4, 'day': 2 },
    {'title': 'Instrument data-acquisition monitoring', 'skill': 5, 'staff': 1, 'duration': 1, 'day': 2 },
    {'title': 'Preparing dome and telescope for night operations', 'skill': 3, 'staff': 1, 'duration': 2, 'day': 2 },
    {'title': 'IT and network maintenance', 'skill': 9, 'staff': 1, 'duration': 4, 'day': 2 },
    {'title': 'Monitoring weather and system status', 'skill': 12, 'staff': 1, 'duration': 2, 'day': 2 },
    {'title': 'Electronics diagnostics and repair', 'skill': 0, 'staff': 1, 'duration': 3, 'day': 2 },
    {'title': 'Cryogenic system checks', 'skill': 8, 'staff': 2, 'duration': 3, 'day': 2 },
    {'title': 'Testing weather\u2011monitoring systems', 'skill': 12, 'staff': 2, 'duration': 1, 'day': 3 },
    {'title': 'Thermal management of dome and telescope', 'skill': 12, 'staff': 1, 'duration': 1, 'day': 3 },
    {'title': 'Structural and mechanical repairs', 'skill': 1, 'staff': 3, 'duration': 4, 'day': 3 },
    {'title': 'Documenting issues and proposed improvements', 'skill': 13, 'staff': 1, 'duration': 3, 'day': 3 },
    {'title': 'Cleaning optical components', 'skill': 2, 'staff': 2, 'duration': 3, 'day': 3 },
    {'title': 'Preparing dome and telescope for night operations', 'skill': 3, 'staff': 1, 'duration': 3, 'day': 3 },
    {'title': 'Testing remote\u2011observing systems', 'skill': 6, 'staff': 2, 'duration': 2, 'day': 3 },
    {'title': 'Assisting astronomers with instrument setups', 'skill': 14, 'staff': 1, 'duration': 3, 'day': 3 },
    {'title': 'Instrument data-acquisition monitoring', 'skill': 5, 'staff': 1, 'duration': 2, 'day': 3 },
    {'title': 'Monitoring weather and system status', 'skill': 12, 'staff': 1, 'duration': 3, 'day': 3 },
    {'title': 'Assembly and testing of mechanical fixtures', 'skill': 1, 'staff': 2, 'duration': 1, 'day': 3 },
    {'title': 'Cryogenic system checks', 'skill': 8, 'staff': 2, 'duration': 1, 'day': 3 },
    {'title': 'Sensor and actuator testing', 'skill': 0, 'staff': 1, 'duration': 3, 'day': 3 },
    {'title': 'Nightly telescope operation', 'skill': 3, 'staff': 2, 'duration': 8, 'day': 3 },
    {'title': 'Electronics diagnostics and repair', 'skill': 0, 'staff': 2, 'duration': 3, 'day': 3 },
    {'title': 'Safety tests (interlocks and motion limits)', 'skill': 11, 'staff': 1, 'duration': 3, 'day': 3 },
    {'title': 'Optical alignment checks', 'skill': 2, 'staff': 1, 'duration': 2, 'day': 3 },
    {'title': 'Monitoring weather and system status', 'skill': 12, 'staff': 1, 'duration': 2, 'day': 4 },
    {'title': 'Documenting issues and proposed improvements', 'skill': 13, 'staff': 1, 'duration': 2, 'day': 4 },
    {'title': 'Optical alignment checks', 'skill': 2, 'staff': 1, 'duration': 2, 'day': 4 },
    {'title': 'Assembly and testing of mechanical fixtures', 'skill': 1, 'staff': 2, 'duration': 1, 'day': 4 },
    {'title': 'Nightly telescope operation', 'skill': 3, 'staff': 2, 'duration': 6, 'day': 4 },
    {'title': 'Thermal management of dome and telescope', 'skill': 12, 'staff': 1, 'duration': 2, 'day': 4 },
    {'title': 'Facility maintenance (HVAC, water, power)', 'skill': 1, 'staff': 2, 'duration': 1, 'day': 4 },
    {'title': 'Sensor and actuator testing', 'skill': 0, 'staff': 1, 'duration': 3, 'day': 4 },
    {'title': 'Electronics diagnostics and repair', 'skill': 0, 'staff': 1, 'duration': 1, 'day': 4 },
    {'title': 'Preventive maintenance on control systems', 'skill': 11, 'staff': 2, 'duration': 2, 'day': 4 },
    {'title': 'Mentoring junior staff', 'skill': 14, 'staff': 1, 'duration': 2, 'day': 4 },
    {'title': 'Hardware installation and integration', 'skill': 10, 'staff': 3, 'duration': 4, 'day': 4 },
    {'title': 'Preparing dome and telescope for night operations', 'skill': 3, 'staff': 1, 'duration': 2, 'day': 4 },
    {'title': 'Instrument data-acquisition monitoring', 'skill': 5, 'staff': 1, 'duration': 1, 'day': 4 },
    {'title': 'Testing remote\u2011observing systems', 'skill': 6, 'staff': 2, 'duration': 1, 'day': 4 },
    {'title': 'Motorized component adjustments', 'skill': 1, 'staff': 1, 'duration': 3, 'day': 4 },
    {'title': 'Cryogenic system checks', 'skill': 8, 'staff': 1, 'duration': 3, 'day': 4 },
    {'title': 'Assisting astronomers with instrument setups', 'skill': 14, 'staff': 1, 'duration': 2, 'day': 4 },
    {'title': 'Safety tests (interlocks and motion limits)', 'skill': 11, 'staff': 1, 'duration': 2, 'day': 5 },
    {'title': 'Real-time fault troubleshooting', 'skill': 0, 'staff': 1, 'duration': 3, 'day': 5 },
    {'title': 'Preventive maintenance on control systems', 'skill': 11, 'staff': 1, 'duration': 3, 'day': 5 },
    {'title': 'Monitoring weather and system status', 'skill': 12, 'staff': 1, 'duration': 2, 'day': 5 },
    {'title': 'Thermal management of dome and telescope', 'skill': 12, 'staff': 1, 'duration': 2, 'day': 5 },
    {'title': 'Cleaning optical components', 'skill': 2, 'staff': 2, 'duration': 3, 'day': 5 },
    {'title': 'Updating and reviewing system logs', 'skill': 13, 'staff': 1, 'duration': 2, 'day': 5 },
    {'title': 'Electronics diagnostics and repair', 'skill': 0, 'staff': 2, 'duration': 1, 'day': 5 },
    {'title': 'Preparing dome and telescope for night operations', 'skill': 3, 'staff': 1, 'duration': 1, 'day': 5 },
    {'title': 'Instrument data-acquisition monitoring', 'skill': 5, 'staff': 1, 'duration': 1, 'day': 5 },
    {'title': 'Nightly telescope operation', 'skill': 3, 'staff': 1, 'duration': 6, 'day': 5 },
    {'title': 'Instrument calibration', 'skill': 4, 'staff': 2, 'duration': 2, 'day': 5 },
    {'title': 'Real-time fault troubleshooting', 'skill': 0, 'staff': 2, 'duration': 2, 'day': 6 },
    {'title': 'Updating and reviewing system logs', 'skill': 13, 'staff': 2, 'duration': 1, 'day': 6 },
    {'title': 'Electronics diagnostics and repair', 'skill': 0, 'staff': 2, 'duration': 1, 'day': 6 },
    {'title': 'Preparing dome and telescope for night operations', 'skill': 3, 'staff': 1, 'duration': 2, 'day': 6 },
    {'title': 'Documenting issues and proposed improvements', 'skill': 13, 'staff': 1, 'duration': 3, 'day': 6 },
    {'title': 'Preventive maintenance on control systems', 'skill': 11, 'staff': 2, 'duration': 2, 'day': 6 },
    {'title': 'Nightly telescope operation', 'skill': 3, 'staff': 2, 'duration': 6, 'day': 6 },
    {'title': 'Motorized component adjustments', 'skill': 1, 'staff': 1, 'duration': 1, 'day': 6 },
    {'title': 'Sensor and actuator testing', 'skill': 0, 'staff': 1, 'duration': 4, 'day': 6 },
    {'title': 'Testing weather\u2011monitoring systems', 'skill': 12, 'staff': 2, 'duration': 2, 'day': 6 },
    {'title': 'Optical alignment checks', 'skill': 2, 'staff': 2, 'duration': 2, 'day': 6 },
    {'title': 'IT and network maintenance', 'skill': 9, 'staff': 2, 'duration': 2, 'day': 6 },
    {'title': 'Instrument calibration', 'skill': 4, 'staff': 2, 'duration': 3, 'day': 6 },
    {'title': 'Assisting astronomers with instrument setups', 'skill': 14, 'staff': 1, 'duration': 2, 'day': 6 },
    {'title': 'Monitoring weather and system status', 'skill': 12, 'staff': 1, 'duration': 2, 'day': 6 },
    {'title': 'Cryogenic system checks', 'skill': 8, 'staff': 2, 'duration': 1, 'day': 6 },
    {'title': 'Mentoring junior staff', 'skill': 14, 'staff': 1, 'duration': 1, 'day': 6 },
    {'title': 'Software updates and testing', 'skill': 6, 'staff': 1, 'duration': 3, 'day': 6 }
]

# Skill scores for each staff member
Staff = [
    [14.4,2.6,6.1,31.4,5.9,0,3.6,6.5,7.6,6.5,1.8,0,18.4,5.4,0],
    [3.6,7.9,0,10.2,19.3,2.7,13.1,18.0,2.5,0,3.1,2.2,10.0,1.7,14.1],
    [5.2,2.4,19.5,3.8,2.5,10.2,2.3,3.0,0,10.0,27.9,7.6,7.8,0,11.7],
    [5.5,7.1,10.1,2.2,2.2,5.9,3.9,3.6,10.6,1.9,13.6,10.2,5.3,15.3,5.2],
    [0,6.0,0,5.5,5.5,0,1.8,6.1,5.1,18.4,22.1,17.6,9.0,1.7,2.7],
    [13.8,10.0,3.0,6.0,11.4,7.9,5.2,0,11.6,14.3,7.9,7.7,6.1,6.0,0],
    [0,2.4,13.3,3.1,19.5,6.8,2.3,2.0,2.8,21.6,20.0,6.8,0,6.1,3.1],
    [3.1,5.8,5.3,5.3,0,2.8,10.1,6.9,9.4,11.7,15.1,6.4,2.8,5.4,14.2],
    [11.3,0,10.1,13.2,2.9,6.5,0,11.5,9.9,14.8,11.2,14.9,5.9,0,0],
    [14.0,1.4,10.8,9.5,0,10.7,5.0,5.6,5.6,7.9,0,1.5,6.8,18.0,5.7],
    [0,1.7,8.0,6.1,10.3,5.1,0,15.3,3.4,11.2,11.3,11.8,10.0,5.4,9.7],
    [2.7,15.1,10.7,14.1,7.3,0,2.3,6.1,1.3,13.9,11.7,3.3,7.7,5.7,7.5],
    [13.2,3.8,7.7,19.4,1.7,5.1,0,3.3,10.5,6.0,2.2,11.4,0,13.9,9.9]
]

S = range(len(Skills))
J = range(len(Tasks))
I = range(len(Staff))

forbiddenPairs = [(3, 5), (0, 10), (5, 11), (2, 6)]

""" Helper functions to access data """
#title of Task j
def title(j):
    return Tasks[j]['title']

#skill of Task j
def skill(j):
    return Tasks[j]['skill']

#num staff of Task j
def staff(j):
    return Tasks[j]['staff']

#duration of Task j
def duration(j):
    return Tasks[j]['duration']

#day of Task j
def day(j):
    return Tasks[j]['day']

#skill score of Staff i for Task j
def ss(i,j):
    return Staff[i][skill(j)]

#Data
maxWeeklyHours = 36 
maxDailyHours = 10                                  #(comm8)
minRestDays = 2                                     #(comm8)
maxDaysWorked = 7 - minRestDays                     #(comm8)
nightTask = 'Nightly telescope operation'           #(comm9)
trainingSlots = 5                                   #(comm10)
trainingSkillIncrease = 7                           #(comm10)

#Model
m = gp.Model("Ancestral Skies Collaboration")

#Variables
X = {(i, j): m.addVar(vtype=gp.GRB.BINARY) for i in I for j in J}   #tracks if staff i assigned to task j
Y = {(i, d): m.addVar(vtype=gp.GRB.BINARY) for i in I for d in T}   #tracks if staff i working on day d (comm8)
Z = {(i, s): m.addVar(vtype=gp.GRB.BINARY) for i in I for s in S}   #tracks if staff i trained in skill s (comm10)

#Objective
m.setObjective(gp.quicksum(X[i,j]*(ss(i,j) + Z[i,skill(j)]*trainingSkillIncrease) for i in I for j in J), gp.GRB.MAXIMIZE)

#Constraints
#Max Hours Weekly Constraint
for i in I:
    m.addConstr(gp.quicksum(X[i,j]*duration(j) for j in J) <= maxWeeklyHours)

#Num Required Staff per Task Constraint
for j in J:
    m.addConstr(gp.quicksum(X[i,j] for i in I) == staff(j))

#Forbidden Pairs Constraint (comm7)
for j in J:
    for fP in forbiddenPairs:
        m.addConstr(gp.quicksum(X[i,j] for i in fP) <= 1)

#Max Hours Daily Constraint (comm8)
for i in I:
    for d in T:  
        m.addConstr(gp.quicksum(X[i,j]*duration(j) for j in J if day(j)==d) <= maxDailyHours)

#Days Off Constraint (comm8)
for i in I:
    m.addConstr(gp.quicksum(Y[i,d] for d in T) <= maxDaysWorked) 

#Linking Days Worked to Tasks Performed (variable Y to X) Constraint (comm8)
for i in I:
    for d in T:
        m.addConstr(1000000*Y[i,d] >= gp.quicksum(X[i,j] for j in J if day(j)==d)) 

#Nightly telescope operation is a standalone task (comm9)
for i in I:
    for d in T:
        m.addConstr(gp.quicksum(X[i,j] for j in J if title(j)!=nightTask and day(j)==d) 
                    <= 1000000*(1 - gp.quicksum(X[i,j] for j in J if title(j)==nightTask and day(j)==d)))

#Available Training Slots Constraint (comm10)
m.addConstr(gp.quicksum(Z[i,s] for i in I for s in S) <= trainingSlots)

#One Training per Staff (comm10)
for i in I:
    m.addConstr(gp.quicksum(Z[i,s] for s in S) <= 1)

m.optimize()
print(m.ObjVal)

#print technicians for training
for i in I:
    for s in S:
        if Z[i,s].X:
            print(f"Technician {i} trained in {Skills[s]}")