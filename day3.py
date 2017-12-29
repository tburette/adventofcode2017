# un peu plus de 30 minutes pour résoudre
# erreur dans l'algo : ne calculait que les bord,a du rajouter une boucle interne pour afficher les cases entre les bords
# question sur la meilleure/plus simple façon de représenter une position. Au final utilise tuple + méthoes custom
# pas mal d'hésitations sur l'endroit ou commencer la boucle pour que cela colle avec la multiplication une iteration sur deux
# je me suis demandé pourquoi la boucle allait parfois plus loin que désiré : réponse = on va toujours jusqu'au bord suivant (cf boucle interne)

import itertools
from collections import defaultdict

input = 325489


def add(pos1, pos2):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])


def mul(pos, multiplier):
    return (pos[0] * multiplier, pos[1] * multiplier)

def get_pos(input):
    # h, g, b, d
    moves = [
        (0, 1),
        (-1, 0),
        (0, -1),
        (1, 0),
    ]
    next_move = itertools.cycle(moves)
    multiplier = 1
    increase_multiplier = False

    # x, y
    pos = (1, 0)
    num_pos = 2
    while num_pos <= input:
        if increase_multiplier:
            multiplier += 1
        increase_multiplier = not increase_multiplier
        current_move = next(next_move)
        for _ in range(0, multiplier):
            pos = add(pos, current_move)
            num_pos += 1
            if num_pos == input:
                print(num_pos, pos, abs(pos[0]) + abs(pos[1]))
                return pos

# print(get_pos(input))


# Part 2

# copy/pasted from above
def get_pos2(target, memo=None):
    if not memo:
        memo = defaultdict(int)
        memo[(0, 0)] = 1
        memo[(1, 0)] = 1

    # h, g, b, d
    moves = [
        (0, 1),
        (-1, 0),
        (0, -1),
        (1, 0),
    ]

    diag = [
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]

    next_move = itertools.cycle(moves)
    multiplier = 1
    increase_multiplier = False

    # x, y
    pos = (1, 0)
    while True:
        if increase_multiplier:
            multiplier += 1
        increase_multiplier = not increase_multiplier
        current_move = next(next_move)
        for _ in range(0, multiplier):
            pos = add(pos, current_move)
            if not memo[pos]:
                memo[pos] = sum([memo[add(pos, move)] for move in moves + diag])
            if memo[pos] > target:
                print(pos, memo[pos], abs(pos[0]) + abs(pos[1]))
                return memo[pos]

get_pos2(input)
