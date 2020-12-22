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

while all([p for p in players]):
    if players[0][0] > players[1][0]:
        players[0] = players[0][1:] + [players[0][0], players[1][0]]
        players[1] = players[1][1:]
    else:
        players[1] = players[1][1:] + [players[1][0], players[0][0]]
        players[0] = players[0][1:]


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

a2 = 0
print('Res 2:', a2)
