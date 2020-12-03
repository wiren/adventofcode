#! /usr/bin/python3

import funs
import functools


def slope_trees(dx, dy):
    x, y, cnt = (0, 0, 0)
    while y < len(arr):
        if arr[y][x] == '#':
            cnt = cnt + 1
        y = y + dy
        x = (x + dx) % len(arr[0])
    return cnt


arr = list(funs.lines_from_file('input3'))

print(slope_trees(3, 1))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(functools.reduce(lambda a, b: a * b, map(lambda s: slope_trees(*s), slopes)))
