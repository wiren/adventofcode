import funs

# ls = funs.lines_from_file("20.intest")
ls = funs.lines_from_file("20.in")
ls.append('')  # Add empty line if needed


def flip(tile):
    n = tile[0][::-1]
    e = tile[3][::-1]
    s = tile[2][::-1]
    w = tile[1][::-1]
    return [n, e, s, w]


def rot(tile):  # rotate 90 deg clockwise
    return [tile[3]] + tile[0:3]


def fix_tile(tile):
    fixed = []
    n = tile[0]
    s = tile[len(tile) - 1][::-1]
    e = ''
    w = ''
    for i in range(len(tile)):
        w += tile[i][0]
        e += tile[i][-1]
    w = w[::-1]
    fixed.append([n, e, s, w])
    fixed.append(rot(fixed[0]))
    fixed.append(rot(fixed[1]))
    fixed.append(rot(fixed[2]))
    fixed.append(flip(fixed[0]))
    fixed.append(rot(fixed[4]))
    fixed.append(rot(fixed[5]))
    fixed.append(rot(fixed[6]))
    return fixed


def find_matching(tiles, seen, side, ix):
    for nr, opts in tiles.items():
        if nr in seen:  # Already used
            continue
        for perm, t in enumerate(opts):
            if t[ix] == side:  # Got it!
                seen.add(nr)
                return nr, t, perm
    return None

full_tiles = {}
tiles = {}
currnr = 0
currtile = []
for l in ls:
    if not l:
        full_tiles[currnr] = currtile
        tiles[currnr] = fix_tile(currtile)
        currtile = []
    elif 'Tile' in l:
        currnr = int(l.split()[1][:-1])
    else:
        currtile.append(l)

seen = set()  # tilenr
laid = {}     # pos: (tilenr, tile_variant)
pos = (0, 0)
top_y = 0
left_x = 0
right_x = 0

# Start with last found tile in its original orientation and find top tile
# laid[pos] = (currnr, tiles[currnr][0], 0)
laid[pos] = (1951, tiles[1951][6], 6)
seen.add(laid[pos][0])
while True:
    currnr, currtile, _ = laid[pos]
    match = find_matching(tiles, seen, currtile[0][::-1], 2)
    if not match:
        # We have reached the top
        top_y = pos[0]
        break
    else:
        pos = (pos[0] - 1, pos[1])
        laid[pos] = match

# Now go west until we reach the leftmost tile
while True:
    currnr, currtile, _ = laid[pos]
    match = find_matching(tiles, seen, currtile[3][::-1], 1)
    if not match:
        # We have reached the leftmost tile
        left_x = pos[1]
        break
    else:
        pos = (pos[0], pos[1] - 1)
        laid[pos] = match

# Now go east until we reach the eastmost tile
while True:
    nextpos = (pos[0], pos[1] + 1)
    if nextpos in laid:
        pos = nextpos
        continue
    # New position
    currnr, currtile, _ = laid[pos]
    match = find_matching(tiles, seen, currtile[1][::-1], 3)
    if not match:
        # We have reached the rightmost tile
        right_x = pos[1]
        break
    else:
        pos = (pos[0], pos[1] + 1)
        laid[pos] = match

# Now get the rest. We don't know the y resolution yet, so loop until we find the end
y = top_y
y_bottom = 1000001
# while len(tiles) < len(seen):
# for y in range(top_y + 1, 20):
while y_bottom > 1000000:
    for x in range(left_x, right_x + 1):
        if (y, x) in laid:
            continue
        if x == left_x:  # Check against tile above
            match = find_matching(tiles, seen, laid[(y-1, x)][1][2][::-1], 0)
            if not match:
                y_bottom = y - 1
                break
            else:
                laid[(y, x)] = match
        else:       # Check against tile to the left
            match = find_matching(tiles, seen, laid[(y, x-1)][1][1][::-1], 3)
            assert match  # There should always be one
            laid[(y, x)] = match
    y += 1

a1 = laid[(top_y, left_x)][0] * laid[(top_y, right_x)][0] * laid[(y_bottom, left_x)][0] * laid[(y_bottom, right_x)][0]
print('\nRes 1:', a1)

# Lets hunt for sea monsters!
monster = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.split('\n')


def rot_tile(tile, rots):
    if rots == 0:
        return tile
    else:
        rotated = list(map(lambda r: ''.join(r), zip(*tile[::-1])))
        return rot_tile(rotated, rots - 1)


def flip_tile(tile):
    return list(map(lambda r: r[::-1], tile))


def get_tile(pos):
    nr, sides, perm = laid[pos]
    norm = full_tiles[nr]
    if perm < 4:  # only rotated
        return rot_tile(norm, perm)
    else:       # flipped and rotated
        return rot_tile(flip_tile(norm), perm - 4)


def truncate(tile):
    return list(map(lambda r: r[1:-1], tile[1:-1]))


def append_tile(rows, tile):
    return list(map(lambda x: ''.join(x), zip(rows, tile)))


# Get the correct image
img = []
for y in range(top_y, y_bottom + 1):
    rows = truncate(get_tile((y, left_x)))
    for x in range(left_x + 1, right_x + 1):
        tile = truncate(get_tile((y, x)))
        rows = append_tile(rows, tile)
    img += rows


def contains(im, monst):
    for i in range(len(im)):
        for j in range(len(im[i])):
            if monst[i][j] == '#' and im[i][j] != '#':
                return False
    return True


def paint_monster(img, monst, pos):
    for r in range(len(monst)):
        row = ''
        for c in range(len(monst[0])):
            if monst[r][c] == '#':
                row += 'O'
            else:
                row += img[pos[0]+r][pos[1] + c]
        img[pos[0]+r] = img[pos[0]+r][:pos[1]] + row + img[pos[0]+r][pos[1]+len(monst[0]):]
    return img


def count_monst(img, monst):
    monster_y = len(monst)
    monster_x = len(monst[0])
    monster_cnt = 0
    for y in range(len(img) - len(monst) + 1):
        for x in range(len(img[0]) - len(monst[0]) + 1):
            # cut out subimage
            if contains([dx[x:x+monster_x] for dx in img[y:y+monster_y]], monst):
                # found it, now color it!
                img = paint_monster(img, monst, (y, x))
                monster_cnt += 1
    return monster_cnt


mcnt = 0
for i in range(4):
    rotimg = rot_tile(img, i)
    found = count_monst(rotimg, monster)
    if found > 0:
        img = rotimg
        break
    mcnt += found
for i in range(4):
    rotimg = rot_tile(flip_tile(img), i)
    found = count_monst(rotimg, monster)
    if found > 0:
        img = rotimg
        break
    mcnt += found

a2 = len([x for x in ''.join(img) if x == '#'])
# print()
# print('\n'.join(img))

print('Res 2:', a2)
