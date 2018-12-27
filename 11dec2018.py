import numpy as np
from scipy.signal import convolve2d

grid_serial = 9810
grid_width = 300

def fill_elem(elem):
    # Compute fuel cell power level
    row = elem % grid_width
    col = int(np.floor(elem / grid_width))
    x = col + 1
    y = row + 1
    rack_id = x + 10
    power_level = rack_id*y
    power_level += grid_serial
    power_level *= rack_id
    digit = int(np.floor(power_level / 100) % 10)
    power_level = digit - 5

    # Return power level
    return power_level


cell_id = np.arange(0,300*300)
cell_grid = np.vectorize(fill_elem)(cell_id)
cell_grid = cell_grid.reshape((300,300), order='F')

for kernel_width in np.arange(1,300+1):
    kernel = np.ones((kernel_width, kernel_width), dtype=np.uint32)
    grid_power_level = convolve2d(cell_grid, kernel, mode='valid')
    best_cell = np.unravel_index(np.argmax(grid_power_level, axis=None), grid_power_level.shape)
    print('(value,X,Y,size): (' + str(grid_power_level[best_cell]) + ',' + str(best_cell[1]+1) + ',' + str(best_cell[0]+1) + ',' + str(kernel_width) + ')')
