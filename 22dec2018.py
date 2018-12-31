import numpy as np
from data_22dec2018 import depth, target


# Initialize the erosion level of the cave system
buffer = 10
dims = tuple([i+buffer+1 for i in target])
el = np.NaN * np.ndarray(dims)

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
rl = el % 3


##############
### Part 1 ###
##############

# Compute risk level of the area
rl_area = sum(sum(rl[0:target[0]+1, 0:target[1]+1]))
print('\nThe risk level for the area is: ' + str(rl_area) + '\n\n')

##############
### Part 2 ###
##############

# At any time instant tool and region must have a different id
# Region ids:    'rocky': 0      'wet': 1        'narrow': 2
# Tool ids:      'neither': 0    'torch': 1      'gear': 2

# Define extended initial and target state
state_init = (0, 0, 1)
state_target = target + (1,)

# Create map with current equipped tool
state = np.reshape(rl, rl.shape + (1,))
state = np.tile(state, (1, 1, 3))

# Delete incompatible states
for t in range(0, 3):
    view = state[:, :, t]
    view[view == t] = np.NaN

# Clear matrix
state[np.logical_not(np.isnan(state))] = True
state[np.isnan(state)] = False


# Visual map
image = np.ndarray(rl.shape, dtype='U8')
image[rl == 0] = '.'    # rocky
image[rl == 1] = '='    # wet
image[rl == 2] = '|'    # narrow
image[(0, 0)] = 'M'
image[target] = 'T'
for row in image:
    print(''.join(row))
