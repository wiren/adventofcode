import funs

ls = funs.lines_from_file("15.intest")
# ls = funs.lines_from_file("15.in")

nrs = list(map(int, ls[0].split(',')))

a1 = 0
a2 = 0


def next_nr(nrs):
    last = nrs[-1]
    if last in nrs[:-1]:
        l = len(nrs) - 1
        for i in range(1, l + 1):
            if nrs[l - i] == last:
                return i
    else:
        return 0


size = 2020

while len(nrs) < size:
    nrs.append(next_nr(nrs))

a1 = nrs[-1]

print('\nRes 1:', a1)

size = 30000000
# size = 2020
seen = {}
i = 0
nrs = list(map(int, ls[0].split(',')))
for i in range(len(nrs) - 1):
    seen[nrs[i]] = i
last = nrs[-1]
i = len(nrs) - 1
while i < size - 1:
    diff = 0
    if last in seen:
        diff = i - seen[last]

    seen[last] = i
    last = diff
    i += 1

a2 = last

print('Res 2:', a2)
