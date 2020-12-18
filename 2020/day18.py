from functools import *
from itertools import *
from computer import *
import funs
import copy

# ls = funs.lines_from_file("18.intest")
ls = funs.lines_from_file("18.in")
# ls.append('')  # Add empty line if needed

a1 = 0
a2 = 0

def calc(rem, res):
    if not rem:
        return res, rem
    op = rem.pop(0)
    # print('op', op)
    if op == ')':
        return res, rem
    # if op[0] == "(":
    #     rem = [op[1:]] + rem
    #     return calc(rem, res)

    second = rem.pop(0)
    # print('second:', second)
    if second == '(':
        rem = ['+'] + rem
        second, rem = calc(rem, 0)
    elif second[-1] == ')':
        second = second[:-1]
    # print('eval {} {} {}'.format(res, op, second))
    res = eval('{} {} {}'.format(res, op, second))
    # print(res, rem)
    return calc(rem, res)


for l in ls:
    # print()
    # print()
    l = l.replace('(', '( ')
    l = l.replace(')', ' )')
    rem = l.split()
    rem = ['+'] + rem
    r, rem = calc(rem, 0)
    a1 += r

print('\nRes 1:', a1)


def calc2(nums, ops):
    nums = list(nums)
    ops = list(ops)
    for op in ['+', '*']:
        while op in ops:
            ix, oo = next((i, o) for i, o in enumerate(ops) if o in op)
            ops.pop(ix)
            a, b = nums[ix:ix+2]
            if op == '+':
                value = a + b
            else:
                value = a * b
            nums[ix:ix+2] = [value]
    return nums[0]


for l in ls:
    opstack = {0: []}
    nrstack = {0: []}
    nrack = ''
    lvl = 0
    # print(l)
    for c in l:
        if c == ' ':
            continue
        elif c == '(':
            lvl += 1
            opstack[lvl] = []
            nrstack[lvl] = []
        elif c == ')':
            if nrack != '':
                nrstack[lvl].append(int(nrack))
                nrack = ''
            # print('calc', nrstack[lvl], opstack[lvl])
            part = calc2(nrstack[lvl], opstack[lvl])
            # print('part', part)
            lvl -= 1
            nrstack[lvl] = nrstack[lvl] + [part]
        elif c in '+*':
            opstack[lvl] = opstack[lvl] + [c]
            if nrack:
                nrstack[lvl] = nrstack[lvl] + [int(nrack)]
                nrack = ''
        else:
            nrack += c
    if nrack:
        nrstack[lvl] = nrstack[lvl] + [int(nrack)]
    a2 += calc2(nrstack[0], opstack[0])


print('Res 2:', a2)
