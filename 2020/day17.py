import funs
from itertools import product

# ls = funs.lines_from_file("17.intest")
ls = funs.lines_from_file("17.in")
# ls.append('')  # Add empty line if needed


def neighs(neigh_offsets, c):
    return map(lambda n: tuple(map(sum, zip(c, n))), neigh_offsets)


def calc(dim):
    assert(dim >= 2)
    cube = {tuple([y, x] + [0]*(dim-2)) for y, row in enumerate(ls) for x, c in enumerate(row) if c == '#'}
    neigh_offsets = set(product([-1, 0, 1], repeat=dim)) - {tuple([0] * dim)}

    for _ in range(6):
        seen = set()
        next_cube = set()
        for c1 in cube:
            for c2 in neighs(neigh_offsets, c1):
                if c2 in seen:
                    continue
                cnt = 0
                for n in neighs(neigh_offsets, c2):
                    if n in cube:
                        cnt += 1
                if c2 in cube:
                    if cnt in [2, 3]:
                        next_cube.add(c2)
                elif cnt == 3:
                    next_cube.add(c2)
                seen.add(c2)
        cube = next_cube
    return len(cube)


a1 = calc(3)
a2 = calc(4)

print('\nRes 1:', a1)
print('Res 2:', a2)
