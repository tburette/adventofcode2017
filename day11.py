#       --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
#  11   00:54:58   1048      0   01:05:20   1046      0
# Je n'avais jamais utilisé de coordonnees hex avant,
# https://www.redblobgames.com/grids/hexagons/ a ete utile
# J'ai perdu beaucoup de temps sur la structure du code:
# - classe Pos car je pensais que j'aurais besoins d'objets utilisables comme clé de dictionnaire
# - Etat et fonction de changement d'etat pour faire marcher reduce.
#   des vars globales et une simple boucle aurait été plus simple

from collections import namedtuple
from functools import reduce
data = open('day11.txt').read().strip()
moves = data.split(',')


# Axial pos
class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

    def __str__(self):
        return 'Pos(' + str(self.x) + ', ' + str(self.y) + ')'


Cube = namedtuple('Cube', ['x', 'y', 'z'])


def axial_to_cube(pos_a):
    return (pos_a.x, -pos_a.x - pos_a.y, pos_a.y)


def cube_distance(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))


# axial distance
def distance(a, b):
    return cube_distance(axial_to_cube(a), axial_to_cube(b))


moves_offset = {
    'n': Pos(0, -1),
    'ne': Pos(1, -1),
    'se': Pos(1, 0),
    's': Pos(0, 1),
    'sw': Pos(-1, 1),
    'nw': Pos(-1, 0)
}

State = namedtuple('State', ['pos', 'furthest'])
state = State(Pos(0, 0), 0)


def calc_new_state(old_state, dir):
    new_pos = old_state.pos + moves_offset[dir]
    new_distance = distance(Pos(0, 0), new_pos)
    return State(
        new_pos,
        new_distance if new_distance > old_state.furthest
        else old_state.furthest)


(pos, furthest) = reduce(calc_new_state, moves, state)
print(pos)

print(distance(Pos(0, 0), pos))
print(furthest)
