import funs
import copy

# ls = funs.lines_from_file("24.intest")
ls = funs.lines_from_file("24.in")

def move(input, start):
    x, y = start
    while input:
        print(input)
        if input.startswith('ne'):
            y += 1
            input = input[2:]
        elif input.startswith('se'):
            x += 1
            y -= 1
            input = input[2:]
        elif input.startswith('sw'):
            y -= 1
            input = input[2:]
        elif input.startswith('nw'):
            x -= 1
            y += 1
            input = input[2:]
        elif input.startswith('e'):
            x += 1
            input = input[1:]
        elif input.startswith('w'):
            x -= 1
            input = input[1:]
    return x, y


tiles = {}

for l in ls:
    coord = move(l, (0, 0))
    print(coord)
    if coord in tiles:
        tiles[coord] = not tiles[coord]
        print('found tile', coord, tiles[coord])
    else:
        print('new tile', coord, False)
        tiles[coord] = True

a1 = sum(tiles.values())
print('\nRes 1:', a1, '\n')

adj = [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1), (0, -1)]


def neighbors(x, y):
    return [(x + c[0], y + c[1]) for c in adj]


black = set(map(lambda y: y[0], (filter(lambda x: x[1], tiles.items()))))
for _ in range(100):
    # print(black)
    nextblack = set()
    search = copy.deepcopy(black)
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
