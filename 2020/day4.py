#! /usr/bin/python3

import funs


def is_valid(pp, prop, fun):
    if prop not in pp:
        return False
    return fun(pp[prop])


def valid_hgt(h):
    if h.endswith('cm'):
        return 150 <= int(h[:-2]) <= 193
    elif h.endswith('in'):
        return 59 <= int(h[:-2]) <= 76
    else:
        return False


def valid_hcl(h):
    return h[0] == '#' and len(h) == 7 and all([c in '0123456789abcdef' for c in h[1:]])


# lines = funs.lines_from_file("4.intest")
lines = funs.lines_from_file("4.in")

passport = []
passports = []
for l in lines:
    if not l:
        passports += [dict(passport)]
        passport = []
    else:
        passport += [x.split(':') for x in l.split()]
passports += [dict(passport)]

cnt = 0
for p in passports:
    valid = True
    for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if field not in p:
            valid = False
    if valid:
        cnt += 1
print(cnt)

cnt = 0
for p in passports:
    # if len(p) == 8 or (len(p) == 7 and 'cid' not in p):
    if is_valid(p, 'byr', lambda val: 1920 <= int(val) <= 2002) \
            and is_valid(p, 'iyr', lambda val: 2010 <= int(val) <= 2020) \
            and is_valid(p, 'eyr', lambda val: 2020 <= int(val) <= 2030) \
            and is_valid(p, 'hgt', valid_hgt) \
            and is_valid(p, 'hcl', valid_hcl) \
            and is_valid(p, 'ecl', lambda val: val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) \
            and is_valid(p, 'pid', lambda pid: len(pid) == 9 and pid.isdigit()):
        cnt += 1

print(cnt)
