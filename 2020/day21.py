import funs
import copy

# ls = funs.lines_from_file("21.intest")
ls = funs.lines_from_file("21.in")

foods = [[ings.split(), algs.split(', ')] for ings, algs in map(lambda l: l.strip(')').split(' (contains '), ls)]
candidates = {}  # allergen, foods
for ings, allgs in foods:
    for a in allgs:
        candidates[a] = candidates[a] & set(ings) if a in candidates else set(ings)

not_seen = {ing for ings, _ in foods for ing in ings}
for _, ings in candidates.items():
    not_seen -= set(ings)

a1 = sum([1 if ing in not_seen else 0 for ings, _ in foods for ing in ings])
print('\nRes 1:', a1)

# ============== PART 2 ================
found = {}
rem_cand = copy.copy(candidates)
while rem_cand:
    for a, ings in copy.copy(rem_cand).items():
        if len(ings) == 1:
            found[next(iter(ings))] = a
            del rem_cand[a]
        else:
            rem_cand[a] = ings - set(found.keys())

a2 = ','.join([x[0] for x in sorted(found.items(), key=lambda pair: pair[1])])
print('Res 2:', a2)
