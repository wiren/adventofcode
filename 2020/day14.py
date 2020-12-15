import funs

# ls = funs.lines_from_file("14.intest")
# ls = funs.lines_from_file("14.intest2")
ls = funs.lines_from_file("14.in")
ls.append('END')  # Add empty line if needed

a1 = 0
a2 = 0

mask = []
memory = dict()
mem = []

for l in ls:
    if not l.startswith('END'):
        op, val = l.split(' = ')
    else:
        op, val = 'END', None
    if op in ['mask', 'END']:
        if not mask:
            mask = val
            continue

        for pos, v in mem:
            b = bin(int(v))[2:].zfill(36)
            res = ''
            for i in range(len(mask)):
                if mask[i] == 'X':
                    res += b[i]
                else:
                    res += mask[i]
            memory[pos] = int(res, 2)

        mask = val
        mem = []
    else:
        mem.append((op[4:-1], val))

keys = []
for k, v in memory.items():
    a1 += v
    keys.append(k)

print('\nRes 1:', a1)

memory = {}

def indices(idx, exp):
    if len(exp) == 0:
        return [idx]

    first = exp[0]
    rest = exp[1:]
    return indices(idx, rest) + indices(idx + 2**first, rest)


def expand(mask):
    idx = 0
    unkn = []
    for i, b in enumerate(reversed(mask)):
        if b == 'X':
            unkn.append(i)
        else:
            idx += int(b) * 2**i
    res = indices(idx, unkn)
    return res


for l in ls:
    if not l.startswith('END'):
        op, val = l.split(' = ')
    else:
        op, val = 'END', None
    if op in ['mask', 'END']:
        if not mask:
            mask = val
            continue

        for pos, v in mem:
            b = bin(int(pos))[2:].zfill(36)
            res = ''
            for i in range(len(mask)):
                if mask[i] == '0':
                    res += b[i]
                elif mask[i] == '1':
                    res += '1'
                else:
                    res += 'X'
            for ix in expand(res):
                memory[ix] = int(v)

        mask = val
        mem = []
    else:
        mem.append((op[4:-1], val))

keys = []
for k, v in memory.items():
    a2 += v
    keys.append(k)

print('Res 2:', a2)
