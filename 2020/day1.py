#! /usr/bin/python3

import funs
from itertools import *

for c in combinations(funs.read_nrs_from_file('input1'), 2):
    if sum(c) == 2020:
        print(c[0] * c[1])
        break

for c in combinations(funs.read_nrs_from_file('input1'), 3):
    if sum(c) == 2020:
        print(c[0] * c[1] * c[2])
        break
