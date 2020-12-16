from functools import *
from itertools import *
from computer import *
import funs
import copy

# ls = funs.lines_from_file("16.intest")
# ls = funs.lines_from_file("16.intest2")
ls = funs.lines_from_file("16.in")
# ls.append('')  # Add empty line if needed

a1 = 0
a2 = 0

rules = {}
ticket = []
nearby = []

section = 0

for l in ls:
    if not l:
        section += 1

    if l in ['your tickte:', 'nearby tickets:', '']:
        continue

    if section == 0:
        r = l.split(': ')
        rules[r[0]] = r[1].split(' or ')

    if section == 1:
        ticket = l.split(',')

    if section == 2:
        nearby.append(l.split(','))

# print(rules)
# print(ticket)
# print(nearby)

all_rules = []
for key, val in rules.items():
    all_rules.append(val[0].split('-'))
    all_rules.append(val[1].split('-'))
# print(all_rules)

all_vals = [int(val) for sublist in nearby for val in sublist]

def valid(x):
    for r in all_rules:
        min, max = r
        if int(min) <= x <= int(max):
            return True
    return False

def invalid_tkt(tkt):
    return not all([valid(int(x)) for x in tkt])

a1 = sum(list(filter(lambda x: not valid(int(x)), all_vals)))

valid_tkts = list(filter(lambda x: not invalid_tkt(x), nearby))

fields = []
for i in range(len(ticket)):
    fields.append(set(rules.keys()))
print(fields)

for t in valid_tkts:
    for i in range(len(t)):
        for key, val in rules.items():
            # print(key, val)
            min1, max1 = val[0].split('-')
            min2, max2 = val[1].split('-')
            # print(i, t, min1, max1, min2, max2)
            if not (int(min1) <= int(t[i]) <= int(max1) or int(min2) <= int(t[i]) <= int(max2)):
                # print(fields[i], key, fields[i] - {key})
                fields[i] = fields[i] - {key}

def done(fs):
    return all([len(f) == 1 for f in fs])

print(fields)

while not done(fields):
    ones = set()
    for f in fields:
        if len(f) == 1:
            ones.add(list(f)[0])
    print(ones)
    for i in range(len(fields)):
        if len(fields[i]) > 1:
            fields[i] = fields[i] - ones
    print(fields)

print(fields)

a2 = 1
for i in range(len(ticket)):
    if 'departure' in list(fields[i])[0]:
        a2 *= int(ticket[i])

print('\nRes 1:', a1)
print('Res 2:', a2)
