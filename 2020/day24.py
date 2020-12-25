import funs
import copy

# ls = funs.lines_from_file("24.intest")
ls = funs.lines_from_file("24.in")


def move(dirs, x, y):
    while dirs:
        d = dirs.pop(0)
        if d == 'e':
            x += 1
        elif d == 'w':
            x -= 1
        elif d == 'n':
            if dirs.pop(0) == 'e':
                y += 1
            else:
                x, y = x-1, y+1
        else:  # must be 's'
            if dirs.pop(0) == 'e':
                x, y = x+1, y-1
            else:
                y -= 1
    return x, y


black = set()
for line in ls:
    coord = move([x for x in line], 0, 0)
    if coord in black:
        black.remove(coord)
    else:
        black.add(coord)

a1 = len(black)
print('\nRes 1:', a1)


def neighbors(x, y):
    return [(x + c[0], y + c[1]) for c in [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1), (0, -1)]]


for _ in range(100):
    nextblack = set()
    search = copy.copy(black)
    for tile in black:
        for s in set(neighbors(*tile)):
            search.add(s)
    for tile in search:
        cnt = sum([n in black for n in neighbors(*tile)])
        if tile in black:
            if 0 < cnt < 3:
                nextblack.add(tile)
        elif cnt == 2:
            nextblack.add(tile)
    black = nextblack


a2 = len(black)
print('Res 2:', a2)
