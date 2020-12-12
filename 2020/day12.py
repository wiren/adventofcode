import numpy as np
import funs

# ls = funs.lines_from_file("12.intest")
ls = funs.lines_from_file("12.in")
# ls.append('')  # Add empty line if needed

a1 = 0
a2 = 0

dirs = {0: [-1, 0], 90: [0, 1], 180: [1, 0], 270: [0, -1]}

pos = np.array([0, 0])
head = 90

for l in ls:
    m = l[0]
    n = int(l[1:])
    diff = np.array([0, 0])
    if m == 'N':
        diff = n * np.array([-1, 0])
    if m == 'S':
        diff = n * np.array([1, 0])
    if m == 'W':
        diff = n * np.array([0, -1])
    if m == 'E':
        diff = n * np.array([0, 1])
    if m == 'L':
        head = (head - n) % 360
    if m == 'R':
        head = (head + n) % 360
    if m == 'F':
        diff = n * np.array(dirs[head])
    pos = np.add(pos, diff)

a1 = abs(pos[0]) + abs(pos[1])
print('\nRes 1:', a1)


def turn(p, dir, deg):
    y, x = p
    if deg == 180:
        return np.array([-y, -x])
    if deg == 270:
        if dir == 'L':
            dir = 'R'
        else:
            dir = 'L'
    if dir == 'L':
        return np.array([-x, y])
    else:
        return np.array([x, -y])


pos = np.array([0, 0])
wp = np.array([-1, 10])

for l in ls:
    m = l[0]
    n = int(l[1:])
    diff = np.array([0, 0])
    if m == 'N':
        diff = n * np.array([-1, 0])
    if m == 'S':
        diff = n * np.array([1, 0])
    if m == 'W':
        diff = n * np.array([0, -1])
    if m == 'E':
        diff = n * np.array([0, 1])
    if m in ['L', 'R']:
        wp = turn(wp, m, n)
    if m == 'F':
        pos = np.add(pos, n * wp)
    wp = wp + diff

a2 = abs(pos[0]) + abs(pos[1])
print('Res 2:', a2)
