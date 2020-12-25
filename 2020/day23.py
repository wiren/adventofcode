class Node:
    def __init__(self, data, prev, next_):
        self.data = data
        self.prev = prev
        self.next = next_

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.nodes = {}
        self.head = None

    def append(self, data, prev):
        if prev is None:
            n = Node(data, None, None)
            n.next, n.prev = n, n
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


def shuffle(nr_cups, nr_moves):
    cups = LinkedList()
    prev = None
    for i in range(nr_cups):
        cup = i + 1
        if i < 9:
            cup = circle[i]
        prev = cups.append(cup, prev)

    curr = cups.head
    maxix = len(cups.nodes)
    for i in range(nr_moves):
        pick = curr.next
        curr.next = pick.next.next.next
        curr.next.prev = curr
        nopick = [curr.data, pick.data, pick.next.data, pick.next.next.data]
        dest = maxix if curr.data == 1 else curr.data - 1
        while dest in nopick:
            dest = maxix if dest == 1 else dest - 1
        dnode = cups.find(dest)
        dnext = dnode.next
        dnode.next = pick
        pick.next.next.next = dnext
        curr = curr.next

    return cups


# circle = [int(x) for x in '389125467']  # Test input
circle = [int(x) for x in '739862541']

curr = shuffle(9, 100).find(1).next
a1 = ''
while True:
    if curr.data == 1:
        break
    a1 += str(curr.data)
    curr = curr.next
print('Res 1:', a1)

one = shuffle(int(1e6), int(1e7)).find(1)
a2 = one.next.data * one.next.next.data
print('Res 2:', a2)
