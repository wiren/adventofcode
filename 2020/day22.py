from functools import *
import funs
import copy

# ls = funs.lines_from_file("22.intest")
ls = funs.lines_from_file("22.in")
ls.append('')  # Add empty line if needed

nr, decks = 0, [[], []]
for line in ls:
    if ':' in line:
        continue
    if not line:
        nr += 1
    else:
        decks[nr] += [int(line)]


def play(decks, recurse):
    seen = set()
    while True:
        key = tuple(decks[0]), tuple(decks[1])
        if key in seen:
            return 0, decks[0]
        else:
            seen.add(key)
        draw = [decks[0].pop(0), decks[1].pop(0)]
        if recurse and all([c <= len(d) for c, d in zip(draw, decks)]):
            winner, _ = play([d[:c] for c, d in zip(draw, decks)], recurse)
        else:
            winner = 0 if draw[0] > draw[1] else 1
        decks[winner] += draw if winner == 0 else reversed(draw)
        if not all([d for d in decks]):
            return winner, decks[winner]


_, winning_deck = play(copy.deepcopy(decks), False)
a1 = reduce(lambda res, x: res + (x[0]+1) * x[1], enumerate(reversed(winning_deck)), 0)
print('\nRes 1:', a1)

_, winning_deck = play(copy.deepcopy(decks), True)
a2 = reduce(lambda res, x: res + (x[0]+1) * x[1], enumerate(reversed(winning_deck)), 0)
print('Res 2:', a2)
