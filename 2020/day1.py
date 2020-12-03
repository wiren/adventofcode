#! /usr/bin/python3

import funs
import functools as f
from itertools import *


def go(data, nr):
    print(type(data))
    for c in combinations(data, nr):
        if sum(c) == 2020:
            return f.reduce(lambda a, b: a * b, c)


lines = list(funs.nrs_from_file('input1'))

print(go(lines, 2))
print(go(lines, 3))
