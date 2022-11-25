import numpy as np
import constants

C = int(constants.DISPLAY_WIDTH/constants.BLOCKSIZE)
R = int(constants.DISPLAY_HEIGHT/constants.BLOCKSIZE)

map = np.zeros((C, R), dtype="int8")

for idy, row in enumerate(map):
    for idx, block in enumerate(row):
        if idy == 0 or idy == R-1:
            map[idx, idy] = int(1)
        if idx == 0 or idx == C-1:
            map[idx, idy] = 1

np.savetxt("maps\map1.txt", map, fmt='%.1g')