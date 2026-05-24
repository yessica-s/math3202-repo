from itertools import combinations

Sites = range(9)

# The state is a 9-tuple where each element is
# -1 = lost, 0 = fragile, 1 = restored
# GenerateOutcomes returns a list of tuples with a probability
# in position 0 and a state as a tuple in position 1
def GenerateOutcomes(State, LossProb):
    ans = []
    tempSites = [j for j in Sites if State[j]==0]
    n = len(tempSites)
    for i in range(n+1):
        for tlist in combinations(tempSites, i):
            p = 1.0
            slist = list(State)
            for j in range(n):
                if tempSites[j] in tlist:
                    p *= LossProb[tempSites[j]]
                    slist[tempSites[j]] = -1
                else:
                    p *= 1-LossProb[tempSites[j]]
            ans.append((p, tuple(slist)))
    return ans

# example
outcomes = GenerateOutcomes((1,0,0,-1,-1,0,1,1,-1), [0.2 for j in Sites])


# Data
Species = [
	[1, 17, 19],
	[8, 9, 10],
	[2, 7, 11],
	[12, 14, 17],
	[10, 12, 13],
	[0, 3, 6, 15, 16],
	[0, 4, 5],
	[1, 10],
	[0, 9, 12, 18]
]

import gurobipy as gp
m = gp.Model("ACS")

X = {}
for s in range(len(Sites)):
    X[s] = m.addVar()

#COMM11
#Constraints
#only one site can be accessed 
m.addConstr(gp.quicksum(X[s] for s in Sites) == 1)

#Objective
m.setObjective(gp.quicksum(len(Species[s]) * X[s] for s in Sites), gp.GRB.MAXIMIZE)

m.optimize()
print(m.ObjVal)

#COMM12
#Data
order = [5, 8, 6, 4, 3, 2, 1, 0, 7]
degradeChance = 0.2

state = {tuple([0]*9): 1.0}
for month in range(len(Sites)):
    future_states = {}
    for st, prob in state.items():
        # get next fragile site
        site_to_restore = None
        for s in order:
            if st[s] == 0:
                site_to_restore = s
                break

        if site_to_restore is None:
            future_states[st] = future_states.get(st, 0) + prob
            continue

        temp_state = list(st)
        temp_state[site_to_restore] = 1
        temp_state = tuple(temp_state)

        # get outcomes for next month
        for next_prob, next_state in GenerateOutcomes(temp_state, [0.2 for j in Sites]):
            future_states[next_state] = future_states.get(next_state, 0) + prob * next_prob
        
    state = future_states

#how many species saved in this 
def count_species(state):
    saved = set()
    for j in Sites:
        if state[j] == 1: #site sved
            saved.update(Species[j])

    return len(saved)

expected = sum(prob * count_species(state) for state, prob in state.items())
print(f"Expected species saved: {expected:.4f}")