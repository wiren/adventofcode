import funs

# lines = funs.lines_from_file("6.intest")
lines = funs.lines_from_file("6.in")

a1 = 0
a2 = 0
qs = set()
qs2 = 0
for line in lines:
    if not line:
        a1 += len(qs)
        a2 += len(qs2)
        qs = set()
        qs2 = 0
    else:
        for c in line:
            qs.add(c)
        if qs2 == 0:
            qs2 = set(line)
        else:
            qs2 = qs2.intersection(set(line))

a1 += len(qs)
a2 += len(qs2)

print('Res 1:', a1)
print('Res 2:', a2)
