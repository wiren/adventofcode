import funs

# ls = funs.lines_from_file("19.intest")
# ls = funs.lines_from_file("19.in")
ls = funs.lines_from_file("19.in2")
# ls.append('')  # Add empty line if needed

a1 = 0
a2 = 0

rules = {}
msgs = []

chars = {}

parse_rules = True
for l in ls:
    if not l:
        parse_rules = False
        continue

    if parse_rules:
        id, rule = l.split(': ')
        if '"' in rule:
            chars[id] = rule.strip('"')
            # rules[id] = chars[id]
            # print(id, chars[id])
        else:
            rule = rule.split(' | ')
            if len(rule) > 1:
                rules[id] = list(map(lambda r: r.split(), rule))
            else:
                rules[id] = [rule[0].split()]
            # print(id, rules[id])
    else:
        msgs.append(l)

# print(msgs)


def submatch(subrules, message, start, end):
    if start == end and not subrules:
        return True
    if start == end:
        return False
    if not subrules:
        return False

    res = False
    for ix in range(start + 1, end + 1):
        if matches(subrules[0], message, start, ix) and submatch(subrules[1:], message, ix, end):
            res = True
    return res


seen = {}
def matches(rnr, message, start, end):
    # if rnr == '0':
    #     seen.clear()
    seen_key = (rnr, message, start, end)
    # print('matches?', seen_key, message[start:end])
    if seen_key in seen:
        # print('seen', seen_key, seen[seen_key])
        return seen[seen_key]

    res = False
    if rnr in chars:
        res = chars[rnr] == message[start:end]
    else:
        rule = rules[rnr]
        for subr in rule:
            if submatch(subr, message, start, end):
                res = True

    # print('match', seen_key, res)
    seen[seen_key] = res
    return res


a1 = len(list(filter(lambda x: matches('0', x, 0, len(x)), msgs)))

print('\nRes 1:', a1)
print('Res 2:', a2)
