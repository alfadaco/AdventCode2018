import data_03dec2018
import numpy as np

data = data_03dec2018.data

max_c = 0
max_r = 0
vertices = []
for claim in data:
    c0 = claim[0]
    r0 = claim[1]
    w = claim[2]
    h = claim[3]
    cf = c0+w-1
    rf = r0+h-1
    vertices.append([c0, r0, cf, rf])
    max_c = max(max_c, cf)
    max_r = max(max_r, rf)

fabric = np.zeros((max_r+1,max_c+1))
for rect in vertices:
    c0 = rect[0]
    r0 = rect[1]
    cf = rect[2]
    rf = rect[3]
    row_range = np.arange(r0,rf+1)
    col_range = np.arange(c0,cf+1)
    fabric[np.ix_(row_range,col_range)] += 1

overlap = fabric.copy()
overlap[overlap < 1.5] = 0
overlap[overlap > 1.5] = 1
overlap_area = np.sum(np.sum(overlap))
print('Overlapping inches = ' + str(int(overlap_area)))

claim_id = 1
for rect in vertices:
    c0 = rect[0]
    r0 = rect[1]
    cf = rect[2]
    rf = rect[3]
    row_range = np.arange(r0,rf+1)
    col_range = np.arange(c0,cf+1)
    if fabric[np.ix_(row_range,col_range)].max() == 1:
        print("Claim " + str(claim_id) + " do not overlap")
        break
    claim_id += 1
