import data_10dec2018
import scipy.sparse as sp
import numpy as np
import cv2

data = data_10dec2018.data

positions = [elem['position'] for elem in data]
velocities = [elem['velocity'] for elem in data]

vx = [coord[0] for coord in velocities]
vy = [coord[1] for coord in velocities]
x = [coord[0] for coord in positions]
y = [coord[1] for coord in positions]

ones = [1 for elem in x]

print(str(len(x)) + ' moving points')

for t in range(0, 100000000):
    xt = x.copy()
    yt = y.copy()
    for i in range(0, len(xt)):
        xt[i] += t*vx[i]
        yt[i] += t*vy[i]
    xt_min = min(xt)
    yt_min = min(yt)
    xt = [elem-xt_min for elem in xt]
    yt = [elem-yt_min for elem in yt]

    img = sp.coo_matrix((ones, (yt, xt)), dtype=np.uint8)
    if t % 100 == 0:
        print(str(t) + ' ' + str(img.shape))

    if img.shape[0] < 1000 and img.shape[1] < 1000:
        print(str(t) + ' ' + str(img.shape))
        dense = img.todense()
        dense[dense > 0] = 255
        cv2.imshow('test', dense)
        cv2.waitKey(0)
