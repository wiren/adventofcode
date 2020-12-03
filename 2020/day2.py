#! /usr/bin/python3

import funs


def parse_line(l):
    s = l.split(': ')
    r = s[0].split(' ')
    minmax = r[0].split('-')
    return int(minmax[0]), int(minmax[1]), r[1], s[1]


def pwd_valid(cmin, cmax, chr, pwd):
    cnt = pwd.count(chr)
    return cmin <= cnt <= cmax


def pwd_valid2(pos1, pos2, chr, pwd):
    return (pwd[pos1 - 1] == chr) != (pwd[pos2 - 1] == chr)


def count_valid(val_fun, rules):
    return sum(map(lambda r: 1 if val_fun(*r) else 0, rules))


# lines = funs.read_lines_from_file('testinput2')
lines = funs.lines_from_file('input2')
rules = list(map(parse_line, lines))

print(count_valid(pwd_valid, rules))
print(count_valid(pwd_valid2, rules))
