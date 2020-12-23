from collections import deque
from functools import *
from itertools import *
from computer import *
import funs
import copy

# circle = [3,8,9,1,2,5,4,6,7]
circle = [7,3,9,8,6,2,5,4,1]

# - The crab picks up the three cups that are immediately clockwise of the current cup.
#   They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
# - The crab selects a destination cup: the cup with a label equal to the current cup's label minus one.
#   If this would select one of the cups that was just picked up, the crab will keep subtracting one
#   until it finds a cup that wasn't just picked up. If at any point in this process the value goes below
#   the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.
# - The crab places the cups it just picked up so that they are immediately clockwise of the destination cup.
#   They keep the same order as when they were picked up.
# - The crab selects a new current cup: the cup which is immediately clockwise of the current cup.

print(circle)

for i in range(100):
    curr = circle[0]
    pick = circle[1:4]
    dest = curr
    found = False
    print(curr, pick)
    while dest > 0:
        dest -= 1
        if dest in circle[4:]:
            found = True
            break
    # print('found', found)
    if not found:  # pick highest
        # print(circle[4:])
        dest = list(sorted(circle[4:], reverse=True))[0]
    ix = circle.index(dest)
    next = circle[4:ix+1] + pick + circle[ix+1:] + [curr]
    print(dest, next)
    circle = next

print(circle)
start = circle.index(1)
print(start)
a1 = circle[start+1:] + circle[:start]
a1 = ''.join(map(str, a1))

# 67384529
print('\nRes 1:', a1, '\n')


class Node:
    def __init__(self, data, prev, next_):
        self.data = data
        self.prev = prev
        self.next = next_

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.nodes = {}
        self.head = None

    def append(self, data, prev):
        if prev is None:
            n = Node(data, None, None)
            n.next = n
            n.prev = n
            self.head = n
            self.nodes[data] = n
        else:
            n = Node(data, prev, prev.next)
            prev.next.prev = n
            prev.next = n
            self.nodes[data] = n
        return n

    def find(self, data):
        return self.nodes[data]

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


def printll(ll):
    curr = ll
    print('[', end=' ')
    while curr:
        print(curr.data, end=' ')
        curr = curr.next
    print(']')


def findlast(n):
    res = n
    nxt = res.next
    while nxt:
        res = nxt
        nxt = res.next
    return res


# circle = [3,8,9,1,2,5,4,6,7]
circle = [7,3,9,8,6,2,5,4,1]

circle = circle + list(range(10, 1000001))

cups = LinkedList(circle)
prev = None
for cup in circle:
    prev = cups.append(cup, prev)
curr = cups.head
maxix = len(cups.nodes)

for i in range(10000000):
    # printll(curr)
    # curr = cups.head.data
    # nextcurr = curr.next.next.next.next
    pick = curr.next
    rest = pick.next.next.next
    curr.next = rest
    rest.prev = curr
    # print(curr.data, end=' ')
    # printll(pick)
    # printll(rest)

    nopick = [curr.data, pick.data, pick.next.data, pick.next.next.data]
    # print('nopick', nopick)

    dest = maxix if curr.data == 1 else curr.data - 1
    while dest in nopick:
        dest = maxix if dest == 1 else dest - 1

    dnode = cups.find(dest)
    dnext = dnode.next
    dnode.next = pick
    pick.next.next.next = dnext

    # rem = dnode.next
    # dnode.next = pick
    # pick.next.next.next = rem

    # last = findlast(pick)
    # curr.next = None
    # last.next = curr

    curr = curr.next
    # print('tick')

    # printll(dnode)
    # print()


one = cups.find(1)
a2 = one.next.data * one.next.next.data

# a2 = 0

# 149245887792
print('Res 2:', a2)
