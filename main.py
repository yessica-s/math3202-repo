import numpy as np

# ---- PARAMETERS ----
annual_attrition = 0.10
quarterly_retention = (1 - annual_attrition) ** (1/4)

promotion_rate = 0.5
retention_rate = 0.5

# Training durations (quarters)
durations = {
    "A": 4, "B": 4, "C": 4, "D": 4,
    "E": 4, "F": 4, "G": 4,
    "H": 4, "I": 4, "J": 4
}

# Promotion structure
promotion_map = {
    "A": "B",
    "B": "C",
    "C": "D",
    "D": "H",
    "E": "F",
    "F": "G",
    "G": "H",
    "H": "I",
    "I": "J"
}


state_index = {}
index = 0

for level, d in durations.items():
    for stage in range(1, d+1):
        state_index[(level, stage)] = index
        index += 1

n_states = index

P = np.zeros((n_states, n_states))

for level, d in durations.items():
    for stage in range(1, d + 1):
        current = state_index[(level, stage)]

        # ---- If NOT final training stage ----
        if stage < d:
            next_stage = state_index[(level, stage + 1)]
            P[next_stage, current] = quarterly_retention

        # ---- If final stage ----
        else:
            # Retention (recycle to stage 1)
            first_stage = state_index[(level, 1)]
            P[first_stage, current] += retention_rate * quarterly_retention

            # Promotion (if exists)
            if level in promotion_map:
                next_level = promotion_map[level]
                promoted_stage = state_index[(next_level, 1)]
                P[promoted_stage, current] += promotion_rate * quarterly_retention

u = np.zeros(n_states)

u[state_index[("A", 1)]] = 20
u[state_index[("E", 1)]] = 10


def simulate(x0, P, u, quarters):
    x = x0.copy()
    history = [x.copy()]

    for _ in range(quarters):
        x = P @ x + u
        history.append(x.copy())

    return np.array(history)

# Initial workforce
x0 = np.zeros(n_states)

# Example initial condition
x0[state_index[("A",1)]] = 100
x0[state_index[("E",1)]] = 50

history = simulate(x0, P, u, quarters=40)

# Initial workforce
x0 = np.zeros(n_states)

# Example initial condition
x0[state_index[("A",1)]] = 100
x0[state_index[("E",1)]] = 50

history = simulate(x0, P, u, quarters=40)

def totals_by_level(x):
    totals = {}
    for (level, stage), idx in state_index.items():
        totals[level] = int(totals.get(level, 0) + x[idx])
    return totals

print(totals_by_level(history[-1]))