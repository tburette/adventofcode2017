# Part 1: 28:07
# Part 2: 28:55

from collections import defaultdict
data = open('day19.txt').read()
# data = open('day19_test.txt').read()
data = data.split('\n')

pos = (0, data[0].index('|'))
dir = 'd'
dirs = {
    'd': (1, 0),
    'u': (-1, 0),
    'l': (0, -1),
    'r': (0, 1),
}
opp = {
    'd': 'u',
    'u': 'd',
    'l': 'r',
    'r': 'l'
}

steps = 0
def add(pos, pos2):
    return (pos[0] + pos2[0], pos[1] + pos2[1])


def at(pos):
    # print(pos)
    return data[pos[0]][pos[1]]

message = ''
while at(pos) != ' ':
    v = at(pos)
    if v not in '-|+':
        message = message + v
        pos = add(pos, dirs[dir])
    elif v in '|-':
        pos = add(pos, dirs[dir])
    elif v == '+':
        matches = {k: v for (k, v) in dirs.items() if at(add(pos, v)) != ' '}
        del matches[opp[dir]]
        match = list(matches.keys())[0]
        dir = match
        pos = add(pos, dirs[dir])
    else:
        raise Error('should not happen')
    steps += 1


print(message)
print(steps)
