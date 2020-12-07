import funs

# lines = funs.lines_from_file("7.intest")
# lines = funs.lines_from_file("7.intest2")
lines = funs.lines_from_file("7.in")
# lines.append('')  # Add empty line if needed

a1 = 0
a2 = 0
rem = []
holders = []
hash = {}
for line in lines:
    cont = line.split(' contain ')
    y = []
    if 'no other bags' in cont[1]:
        pass
    else:
        for x in cont[1].split(', '):
            splt = x.split(' ')
            y.append([' '.join(splt[1:3]), int(splt[0])])
    hash[' '.join(cont[0].split(' ')[:2])] = y

found = set()
search = {'shiny gold'}
while len(search) > 0:
    new_search = set()
    for k,v in hash.items():
        for s in search:
            for vx in v:
                if s in vx:
                    new_search.add(k)
    found.update(new_search)
    search = new_search

a1 = len(found)


def find_cnt(bag):
    bags = hash[bag]
    if len(bags) == 0:
        return 1
    else:
        cnt = 0
        for b in bags:
            cnt += b[1] * find_cnt(b[0])
        return cnt + 1


curr = hash['shiny gold']
a2 = find_cnt('shiny gold') - 1

print('Res 1:', a1)
print('Res 2:', a2)
