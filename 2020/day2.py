#! /usr/bin/python3

import funs


def parse_line(l):
    minmax, ch, pwd = l.split()
    lo, hi = [int(x) for x in minmax.split('-')]
    return lo, hi, ch[0], pwd


def pwd_valid(cmin, cmax, ch, pwd):
    return cmin <= pwd.count(ch) <= cmax


def pwd_valid2(pos1, pos2, ch, pwd):
    return (pwd[pos1 - 1] == ch) != (pwd[pos2 - 1] == ch)


def count_valid(val_fun, rule_lst):
    return sum(map(lambda r: val_fun(*r), rule_lst))


# lines = funs.read_lines_from_file('2.intest')
lines = funs.lines_from_file('2.in')
rules = list(map(parse_line, lines))

print(count_valid(pwd_valid, rules))
print(count_valid(pwd_valid2, rules))
