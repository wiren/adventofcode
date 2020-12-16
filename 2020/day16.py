import funs
from functools import reduce


def valid(x):
    return any([x for _min, _max in all_rules if _min <= x <= _max])


def rule_match(i, min1, max1, min2, max2):
    return all([min1 <= v <= max1 or min2 <= v <= max2 for v in [t[i] for t in valid_tkts]])


# ls = funs.lines_from_file("16.intest")
# ls = funs.lines_from_file("16.intest2")
ls = funs.lines_from_file("16.in")

rules, ticket, nearby, section = {}, [], [], 0
for l in ls:
    if not l:
        section += 1
        continue
    if l in ['your ticket:', 'nearby tickets:']:
        continue
    if section == 0:
        r = l.split(': ')
        rules[r[0]] = [int(y) for sub in map(lambda x: x.split('-'), r[1].split(' or ')) for y in sub]
    if section == 1:
        ticket = [int(x) for x in l.split(',')]
    if section == 2:
        nearby.append([int(x) for x in l.split(',')])

all_rules = list(reduce(lambda a, b: a + [b[:2], b[2:]], rules.values(), []))
all_vals = [val for sublist in nearby for val in sublist]

a1 = sum([x for x in all_vals if not valid(x)])

# PART 2
valid_tkts = [tkt for tkt in nearby if all([valid(t) for t in tkt])]
fields = []
for i in range(len(ticket)):
    fields.append({key for key, val in rules.items() if rule_match(i, *val)})

while True:
    ones = {next(iter(f)) for f in fields if len(f) == 1}
    rem = [f for f in enumerate(fields) if len(f[1]) > 1]
    if len(rem) == 0:
        break
    for i, r in rem:
        fields[i] = r - ones

deps = filter(lambda x: 'departure' in x[1], map(lambda f: (f[0], list(f[1])[0]), enumerate(fields)))
a2 = reduce(lambda a, b: a*b, map(lambda v: int(ticket[v[0]]), deps))

print('\nRes 1:', a1)
print('Res 2:', a2)
