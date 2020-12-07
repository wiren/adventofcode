import funs

# lines = funs.lines_from_file("7.intest")
# lines = funs.lines_from_file("7.intest2")
lines = funs.lines_from_file("7.in")

a1 = 0
a2 = 0
bags = {}
for line in lines:
    cont = line.split(' contain ')
    inner_bags = []
    if 'no other bags' not in cont[1]:
        inner_bags = list(map(lambda y: [y[1]+y[2], int(y[0])], [x.split(' ') for x in cont[1].split(', ')]))
    bags[''.join(cont[0].split(' ')[:2])] = inner_bags

found = set()
search = {'shinygold'}
while len(search) > 0:
    new_search = set()
    for k, v in bags.items():
        for s in search:
            for vx in v:
                if s in vx:
                    new_search.add(k)
    found.update(new_search)
    search = new_search

a1 = len(found)


def nr_bags_in(bag):
    contents = bags[bag]
    if len(contents) == 0:
        return 0
    else:
        cnt = 0
        for b in contents:
            cnt += b[1] * (1 + nr_bags_in(b[0]))
        return cnt


a2 = nr_bags_in('shinygold')

print('Res 1:', a1)
print('Res 2:', a2)
