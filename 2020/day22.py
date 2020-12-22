from functools import *
from itertools import *
from computer import *
import funs
import copy

# ls = funs.lines_from_file("22.intest")
ls = funs.lines_from_file("22.in")
ls.append('')  # Add empty line if needed

players = []
curr = []
for l in ls:
    if ':' in l:
        continue
    if not l:
        players += [curr]
        curr = []
    else:
        curr += [int(l)]

print(players)
p2 = copy.copy(players)

while all([p for p in players]):
    if players[0][0] > players[1][0]:
        players[0] = players[0][1:] + [players[0][0], players[1][0]]
        players[1] = players[1][1:]
    else:
        players[1] = players[1][1:] + [players[1][0], players[0][0]]
        players[0] = players[0][1:]


print(players)
a1 = 0
for i, c in enumerate(reversed(list(sorted(players))[1])):
    a1 += (i+1) * c

print('\nRes 1:', a1, '\n')

# - Before either player deals a card, if there was a previous round in this game
#   that had exactly the same cards in the same order in the same players' decks,
#   the game instantly ends in a win for player 1. Previous rounds from other games
#   are not considered. (This prevents infinite games of Recursive Combat, which
#   everyone agrees is a bad idea.)
# - Otherwise, this round's cards must be in a new configuration; the players begin
#   the round by each drawing the top card of their deck as normal.
# - If both players have at least as many cards remaining in their deck as the value
#   of the card they just drew, the winner of the round is determined by playing a new
#   game of Recursive Combat (see below).
# - Otherwise, at least one player must not have enough cards left in their deck to
#   recurse; the winner of the round is the player with the higher-value card.

players = p2

x = 0
def play(players):
    seen = set()
    while all([p for p in players]):
        # print(players)
        key = tuple(players[0]), tuple(players[1])
        if key in seen:
            # print('seen', key)
            return 0, []
        else:
            seen.add(key)

        c0 = players[0].pop(0)
        c1 = players[1].pop(0)
        winner = 0
        if c0 <= len(players[0]) and c1 <= len(players[1]):
            # print(1, [c0, c1])
            deck = [players[0][:c0], players[1][:c1]]
            winner, _ = play(deck)
        else:
            # print(3, [c0, c1])
            if c0 < c1:
                winner = 1
        if winner == 0:
            players[winner] += [c0, c1]
        else:
            players[winner] += [c1, c0]

        if not players[0] or not players[1]:
            return winner, []


winner, rest = play(players)
players[winner] += rest
print('winner', winner, players)

a2 = 0
for i, c in enumerate(reversed(players[winner])):
    a2 += (i+1) * c
print('Res 2:', a2)
