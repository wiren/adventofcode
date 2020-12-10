import funs

# lines = funs.lines_from_file("8.intest")
lines = funs.lines_from_file("8.in")
# lines.append('')  # Add empty line if needed


def run_prg(prog):
    visited = set()
    acc = 0
    ptr = 0
    while True:
        if ptr in visited or ptr >= len(prog):
            return acc, ptr
        visited.add(ptr)
        op, arg = prog[ptr].split(' ')
        if op == 'nop':
            ptr += 1
        elif op == 'jmp':
            ptr += int(arg)
        elif op == 'acc':
            acc += int(arg)
            ptr += 1


a1, p1 = run_prg(lines)
a2 = 0

alter = [x for x in enumerate(lines) if(x[1].split(' ')[0] in ['jmp', 'nop'])]
op_sw = {'nop': 'jmp ', 'jmp': 'nop '}
for a in alter:
    newlines = lines.copy()
    op, arg = newlines[a[0]].split(' ')
    newlines[a[0]] = op_sw[op] + arg

    a2, p = run_prg(newlines)
    if p == len(newlines):
        break

print('Res 1:', a1)
print('Res 2:', a2)
