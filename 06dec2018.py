import data_06dec2018
import numpy as np
import matplotlib.pyplot as plt
import time

data = data_06dec2018.data

# Create empty image
region_mask = np.zeros(np.amax(data, 0) + 1, dtype=int)
for i in range(0, len(data)):
    region_mask[data[i][0]][data[i][1]] = i
plt.imshow(region_mask)

cumulative_distance_mask = np.zeros(np.amax(data, 0) + 1, dtype=int)

# 1. For each point in the image, evaluate the closest point between the datas.
#    That point will give its label to the current one
# 2. Eval the sum of the cumulative distance from the points
for r in range(0, region_mask.shape[0]):
    for c in range(0, region_mask.shape[1]):
        distance = {}
        for i in range(0, len(data)):
            d = data[i]
            distance[i] = abs(r-d[0]) + abs(c-d[1])

        min_distance_idx = min(distance, key=distance.get)
        min_distance = distance[min_distance_idx]
        if list(distance.values()).count(min_distance) == 1:
            region_mask[r][c] = min_distance_idx
        else:
            region_mask[r][c] = -1

        cumulative_distance_mask[r][c] = sum(distance.values())

fig1 = plt.figure()
plt.imshow(region_mask)
fig2 = plt.figure()
plt.imshow(cumulative_distance_mask)
plt.show(block=False)

# Get greatest area
area = {}
for i in range(0, len(data)):
    d = data[i]
    mask = region_mask == i
    if sum(mask[0]) > 0 or sum(mask[:,0]) > 0 or sum(mask[-1]) > 0 or sum(mask[:,-1]) > 0:
        area[i] = -1
    else:
        area[i] = sum(sum(mask))
max_area = max(list(area.values()))
print(max_area)

# Filter cumulative distances
max_distance = 10000
mask_distance = cumulative_distance_mask < max_distance
print(sum(sum(mask_distance)))

distance_ok = np.zeros(np.amax(data, 0) + 1, dtype=int)
distance_ok[mask_distance] = 1
fig3 = plt.figure()
plt.imshow(distance_ok)

plt.show()







