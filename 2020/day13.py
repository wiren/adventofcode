from functools import *
from itertools import *
from computer import *
import numpy as np
import funs
import copy

# ls = funs.lines_from_file("13.intest")
ls = funs.lines_from_file("13.in")
# ls.append('')  # Add empty line if needed

start = int(ls[0])
buses = ls[1].split(',')

times = []
tt = []

for i in range(len(buses)):
    times.append(0)
    b = buses[i]
    if b == 'x':
        continue
    t = int(b)
    while t < start:
        t += int(b)
    times[i] = t

sched = list(filter(lambda x: x != 0, sorted(times)))
# print(sched)
ix = times.index(sched[0])
# print(ix, times)
# print(start, sched[0] - start)
# print(sched)
# print(buses[ix])
# print('start:', start)
# print('wait:', sched[0]-start)
# print('bus id:', buses[ix])

a1 = int(buses[ix]) * (sched[0] - start)

a2 = 0

# print(buses)
bs = list(map(lambda y: (y[0], int(y[1])), (filter(lambda x: x[1] != 'x', enumerate(buses)))))

# bs = [(0, 1789), (1, 37), (2, 47), (3, 1889)]
print(bs)


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod



def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

bus_times = []
bus_start_times = []
for i, time in bs:
    bus_times.append(time)
    # bus_start_times.append(b[1] - b[0])
    bus_start_times.append(time - i)

print(bus_times)
print(bus_start_times)

a2 = chinese_remainder(bus_times, bus_start_times)

print('\nRes 1:', a1)
print('Res 2:', a2)
