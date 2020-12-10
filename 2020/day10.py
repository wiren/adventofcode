from itertools import *
from computer import *
import funs

# ls = funs.nrs_from_file("10.intest")
# ls = funs.nrs_from_file("10.intest2")
ls = funs.nrs_from_file("10.in")
# ls.append('')  # Add empty line if needed

a1 = 0
a2 = 0

rate = sorted(ls)[-1] + 3
ls.append(rate)
ls.append(0)

sort = sorted(ls)

diffs = [0, 0, 0, 0]
for i in range(len(sort) - 1):
    diff = sort[i+1] - sort[i]
    diffs[diff] = diffs[diff] + 1

a1 = diffs[1] * diffs[3]


val = {}
def nr_val(i):
    if i == len(sort) - 1:
        return 1
    if i in val:
        return val[i]
    res = 0
    for j in range(i+1, len(sort)):
        if sort[j] - sort[i] < 4:
            res += nr_val(j)
    val[i] = res
    return res

a2 = nr_val(0)

print('Res 1:', a1)
print('Res 2:', a2)
