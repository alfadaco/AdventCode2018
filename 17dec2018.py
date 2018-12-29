import re
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import data_17dec2018
data = data_17dec2018.data

# Define figure
plt.figure(1)
plt.clf()

# Parse input
idx = 0
data_parsed = [None] * len(data)
max_x = 0
max_y = 0
min_x = np.Inf
min_y = np.Inf
for string in data:
    match = re.match(r'([xy])=(\d+), ([xy])=(\d+)..(\d+)', string).groups()
    if match is None:
        raise ValueError('Input parsing error', idx, string)
    first_label = match[0]
    first_value = np.array([int(match[1])])
    second_label = match[2]
    second_value = np.arange(int(match[3]), int(match[4])+1)
    data_parsed[idx] = {
        first_label: first_value,
        second_label: second_value
    }

    max_x = max(max_x, data_parsed[idx]['x'].max())
    max_y = max(max_y, data_parsed[idx]['y'].max())
    min_x = min(min_x, data_parsed[idx]['x'].min())
    min_y = min(min_y, data_parsed[idx]['y'].min())

    idx += 1

# Make sure not to be on the border
max_x = max_x + 1
min_x = min_x - 1

# Remove horizontal offset
for datum in data_parsed:
    datum['x'] = datum['x'] - min_x
    #datum['y'] = datum['y']

# Create matrix
matrix_shape = (max_y+1, max_x-min_x+1)
matrix = np.zeros(matrix_shape, dtype='U1')
matrix[:] = '.'
for entry in data_parsed:
    rows = entry['y']
    columns = entry['x']
    matrix[np.ix_(rows, columns)] = '#'

# Add spring
spring_col = 500 - min_x
spring_row = 0
matrix[spring_row][spring_col] = '+'

##############
### Part 1 ###
##############

# Simulate water falling
k = 0
max_row = 0
rows_to_check = set()
changed = True
while changed:
    # Reset changed flag
    changed = False

    # Grow water flow
    flow_idx = np.asarray(np.where(np.logical_or(matrix == '|', matrix == '+')))
    for idx in range(0, flow_idx.shape[1]):
        coord = flow_idx[:, idx]
        row = coord[0]
        col = coord[1]
        max_row = max(max_row, row)

        if row < matrix.shape[0]-1 and matrix[row+1, col] == '.':
            matrix[row+1, col] = '|'
            rows_to_check.add(row+1)
            changed = True
        elif row < matrix.shape[0]-1 and (matrix[row+1, col] == '#' or matrix[row+1, col] == '~'):
            if col > 0 and matrix[row, col-1] == '.':
                matrix[row, col-1] = '|'
                rows_to_check.add(row)
                changed = True
            if col < matrix.shape[1]-1 and matrix[row, col+1] == '.':
                matrix[row, col+1] = '|'
                rows_to_check.add(row)
                changed = True

    # Check for water at rest
    if not changed:
        while len(rows_to_check) > 0:
            row = rows_to_check.pop()
            row_string = ''.join(matrix[row])
            match = re.search(r'#[|]+#', row_string)
            if match is not None:
                col_i = match.span()[0] + 1
                col_f = match.span()[1] - 1
                matrix[row, col_i:col_f] = '~'
                rows_to_check.add(row)
                changed = True

    # Print status
    if k % 25 == 0:
        print(max_row)

    # Advance counter
    k += 1

# Plot
#height = 150
#row_i = max(0, max_row-height) + 1
#row_f = max(height, max_row) + 2
#view = matrix[row_i:row_f, :]
view = matrix
image = np.zeros(view.shape, dtype=np.uint8)
image[view == '+'] = 1
image[view == '~'] = 1
image[view == '|'] = 1
image[view == '#'] = 2
#plt.imshow(image, cmap=CustomCmap)
plt.imshow(image)
plt.title('Current max row: ' + str(max_row))
plt.show()

# Output
water = np.asarray(np.where(np.logical_or(matrix == '|', matrix == '~'))).shape[1]
print('There are ' + str(water) + ' squares of water')
