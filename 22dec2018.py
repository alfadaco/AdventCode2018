import numpy as np
from data_22dec2018 import depth, target


# Initialize the erosion level of the cave system
buffer = 15
dims = tuple([i+buffer+1 for i in target])
el = np.zeros(dims, dtype=np.uint)

# Set the erosion level of the mouth and the borders
el[0, 0] = (0 + depth) % 20183
el[1:, 0] = (16807 * np.arange(1, dims[0]) + depth) % 20183
el[0, 1:] = (48271 * np.arange(1, dims[1]) + depth) % 20183

# Compute the erosion level for each region of the cave system
for d in range(1, max(dims)):
    y = min(d, dims[1]-1)
    for x in range(d, dims[0]):
        el[(x, y)] = (el[(x-1, y)]*el[(x, y-1)] + depth) % 20183
    x = min(d, dims[0]-1)
    for y in range(d, dims[1]):
        el[(x, y)] = (el[(x-1, y)]*el[(x, y-1)] + depth) % 20183

# Set the erosion level of the target
el[target] = 0

# Compute risk level
rl = (el % 3).astype(np.uint8)


##############
### Part 1 ###
##############

# Compute risk level of the area
rl_area = sum(sum(rl[0:target[0]+1, 0:target[1]+1]))
print('\nThe risk level for the area is: ' + str(rl_area) + '\n')


##############
### Part 2 ###
##############

# At any time instant tool and region must have a different id
# Region ids:    'rocky': 0      'wet': 1        'narrow': 2
# Tool ids:      'neither': 0    'torch': 1      'gear': 2

# Given a node compute its successors and the cost of reaching them
def get_succ_cost(node):
    # Initialize
    succ = set()
    cost = dict()

    # Get node coordinates
    (X, Y, T) = node

    # Change tool
    T_succ = int(3 - (rl[X, Y] + T))
    node_succ = (X, Y, T_succ)
    succ.add(node_succ)
    cost[node_succ] = 7

    # Move along X
    if X > 0 and rl[X-1, Y] != T:
        node_succ = (X-1, Y, T)
        succ.add(node_succ)
        cost[node_succ] = 1
    if X < dims[0]-1 and rl[X+1, Y] != T:
        node_succ = (X+1, Y, T)
        succ.add(node_succ)
        cost[node_succ] = 1

    # Move along Y
    if Y > 0 and rl[X, Y-1] != T:
        node_succ = (X, Y-1, T)
        succ.add(node_succ)
        cost[node_succ] = 1
    if Y < dims[1]-1 and rl[X, Y+1] != T:
        node_succ = (X, Y+1, T)
        succ.add(node_succ)
        cost[node_succ] = 1

    # Return
    return (succ, cost)


# Compute the minimum spanning tree using the mouth as the root
def find_mst(init_state):
    # Initialize predecessor map and states to check
    P = dict()
    P[init_state] = init_state
    Q = {init_state}

    # Initialize cost map
    C = dict()
    C[init_state] = 0

    # Run Dijikstra algorithm for finding the shortest path
    while len(Q) > 0:
        state = Q.pop()
        (succ_state, succ_cost) = get_succ_cost(state)
        for ss in succ_state:
            if (ss not in P.keys()) or (C[state] + succ_cost[ss] < C[ss]):
                P[ss] = state
                C[ss] = C[state] + succ_cost[ss]
                Q.add(ss)

    # Return predecessor list and associated cost
    return (P, C)


# Define extended initial and target state
initial_state = (0, 0, 1)
target_state = target + (1,)

# Compute the mst
(P_state, C_state) = find_mst(initial_state)

# Print time needed for reaching the target
print('Reaching the target requires: ' +
      str(C_state[target_state]) + ' minutes\n\n')


# Visual map
print('Cave system map')
image = np.ndarray(rl.shape, dtype='U8')
image[rl == 0] = '.'    # rocky
image[rl == 1] = '='    # wet
image[rl == 2] = '|'    # narrow
image[(0, 0)] = 'M'
image[target] = 'T'
for row in image:
    print(''.join(row))

# Compute route
curr_state = target_state
while True:
    curr_state = P_state[curr_state]
    if curr_state == initial_state:
        break
    else:
        image[curr_state[0], curr_state[1]] = 'x'

# Visual map of the route
print('\nCave system map with optimal route')
for row in image:
    print(''.join(row))
