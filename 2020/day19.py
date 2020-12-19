import funs

# ls = funs.lines_from_file("19.intest")
# ls = funs.lines_from_file("19.intest2")
ls = funs.lines_from_file("19.in")
# ls.append('')  # Add empty line if needed


def submatch(subrules, message, start, end, seen):
    if start == end and not subrules:
        return True
    if start == end:
        return False
    if not subrules:
        return False

    res = False
    for ix in range(start + 1, end + 1):
        if matches(subrules[0], message, start, ix, seen) and submatch(subrules[1:], message, ix, end, seen):
            res = True
    return res


def matches(rnr, message, start, end, seen):
    seen_key = (rnr, message, start, end)
    if seen_key in seen:
        return seen[seen_key]

    res = False
    if rnr in chars:
        res = chars[rnr] == message[start:end]
    else:
        rule = rules[rnr]
        for subr in rule:
            if submatch(subr, message, start, end, seen):
                res = True

    seen[seen_key] = res
    return res


rules, chars, msgs = {}, {}, []
parse_rules = True
for l in ls:
    if not l:
        parse_rules = False
        continue

    if parse_rules:
        id, rule = l.split(': ')
        if '"' in rule:
            chars[id] = rule.strip('"')
        else:
            rule = rule.split(' | ')
            if len(rule) > 1:
                rules[id] = list(map(lambda r: r.split(), rule))
            else:
                rules[id] = [rule[0].split()]
    else:
        msgs.append(l)

a1 = len(list(filter(lambda x: matches('0', x, 0, len(x), {}), msgs)))
print('\nRes 1:', a1)

rules['8'] = [['42'], ['42', '8']]
rules['11'] = [['42', '31'], ['42', '11', '31']]
a2 = len(list(filter(lambda x: matches('0', x, 0, len(x), {}), msgs)))
print('Res 2:', a2)
