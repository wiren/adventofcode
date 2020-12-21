from functools import *
from itertools import *
from computer import *
import funs
import copy

# ls = funs.lines_from_file("21.intest")
ls = funs.lines_from_file("21.in")
# ls.append('')  # Add empty line if needed

candidates = {}  # allergen, foods
all_ings = []

for l in ls:
    a, b = l.split(' (contains ')
    ings = a.split()
    allgs = list(map(lambda x: x.strip(')'), b.split(', ')))
    all_ings = all_ings + ings

    for a in allgs:
        if a in candidates:
            c = candidates[a]
            c = {x for x in c if x in ings}
            candidates[a] = c
        else:
            candidates[a] = set(ings)

foo = set(all_ings)
not_seen = set()
all_seen = set()
for a, ings in candidates.items():
    for i in ings:
        all_seen.add(i)
not_seen = foo - all_seen

a1 = 0
for i in not_seen:
    a1 += all_ings.count(i)

print('\nRes 1:', a1)

# ============== PART 2 ================

found = {}
while True:
    rem_cand = {}
    for a, ings in candidates.items():
        if len(ings) == 1:
            for i in ings: break
            found[i] = a
            print('found', i, a)
        else:
            new_ings = {i for i in ings if i not in found}
            rem_cand[a] = new_ings
    candidates = rem_cand
    if len(rem_cand) == 0:
        break

a2 = ','.join(map(lambda x: x[0], sorted(found.items(), key=lambda i: i[1])))

print('\nRes 2:', a2)
