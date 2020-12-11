from functools import reduce
import funs
import copy

# m = funs.lines_from_file("11.intest")
m = funs.lines_from_file("11.in")
# m.append('')  # Add empty line if needed

adj = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

m = list(map(list, m))


def add(a, b):
    return [a[0] + b[0], a[1] + b[1]]


def inside(m, pos):
    return 0 <= pos[0] < len(m) and 0 <= pos[1] < len(m[0])


def neighbors(m, pos):
    return filter(lambda y: inside(m, y), map(lambda x: add(x, pos), adj))


def neighs(m, pos, d):
    res = []
    curr = pos
    while True:
        curr = add(curr, d)
        if inside(m, curr):
            res.append(curr)
            w = m[curr[0]][curr[1]]
            if w in['L', '#']:
                break
        else:
            break
    return res


def neighbors2(m, pos):
    ns = []
    for d in adj:
        ns += (neighs(m, pos, d))
    ns = list(filter(lambda x: x, ns))
    return ns


def update(m, neigh_fun, max_neighs, pos):
    ns = list(neigh_fun(m, pos))
    cnt = 0
    for p in ns:
        if m[p[0]][p[1]] == '#':
            cnt += 1
    if m[pos[0]][pos[1]] == 'L' and cnt == 0:
        return '#'
    if m[pos[0]][pos[1]] == '#' and cnt >= max_neighs:
        return 'L'
    return m[pos[0]][pos[1]]


def calc(m, neigh_fun, max_neighs):
    while True:
        newm = copy.deepcopy(m)
        for i in range(len(m)):
            for j in range(len(m[i])):
                newm[i][j] = update(m, neigh_fun, max_neighs, [i, j])

        changed = False
        for i in range(len(m)):
            if changed:
                break
            for j in range(len(m[i])):
                if m[i][j] != newm[i][j]:
                    changed = True
                    break
        if changed:
            m = newm
        else:
            return reduce(lambda a, b: a + 1 if b == '#' else a, [item for sublist in m for item in sublist], 0)

a1 = calc(m, neighbors, 4)
print('\nRes 1:', a1)

a2 = calc(m, neighbors2, 5)
print('Res 2:', a2)
