import funs

# ls = funs.lines_from_file("19.intest")
# ls = funs.lines_from_file("19.intest2")
ls = funs.lines_from_file("19.in")


def submatch(subrules, message, seen):
    if not message:
        return not subrules
    if not subrules:
        return False

    for ix in range(1, len(message) + 1):
        if matches(subrules[0], message[:ix], seen) and submatch(subrules[1:], message[ix:], seen):
            return True
    return False


def matches(rnr, message, seen):
    seen_key = (rnr, message)
    if seen_key in seen:
        return seen[seen_key]

    res = False
    if rnr in chars:
        res = chars[rnr] == message
    else:
        rule = rules[rnr]
        for subr in rule:
            if submatch(subr, message, seen):
                res = True
                break

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

a1 = len(list(filter(lambda x: matches('0', x, {}), msgs)))
print('\nRes 1:', a1)

rules['8'] = [['42'], ['42', '8']]
rules['11'] = [['42', '31'], ['42', '11', '31']]
a2 = len(list(filter(lambda x: matches('0', x, {}), msgs)))
print('Res 2:', a2)
