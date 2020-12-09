from itertools import *
import funs

# ls = funs.nrs_from_file("9.intest")
# preamble = 5
ls = funs.nrs_from_file("9.in")
preamble = 25
# ls.append('')  # Add empty line if needed

a1 = 0
a2 = 0

for i in range(preamble, len(ls)):
    ws = list(map(lambda c: c[0]+c[1], combinations(ls[i - preamble:i], 2)))
    if ls[i] not in ws:
        a1 = ls[i]
        break

res = []
for i in range(len(ls)):
    if res:
        break
    for j in range(i+1, len(ls)):
        nrs = ls[i:j+1]
        a = sum(nrs)
        if a == a1:
            res = nrs
            break
        elif a > a1:
            break

ns = sorted(res)
a2 = ns[0] + ns[-1]

print('Res 1:', a1)
print('Res 2:', a2)
