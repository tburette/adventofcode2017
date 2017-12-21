#       --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
#  21   02:43:32    569      0   02:49:19    552      0
#Gigantic waste of time due to handling matrices manually with list of lists. I really should leanr numpy


from collections import defaultdict
data = open('day21.txt').read().strip()
# data = open('day21_t.txt').read().strip()
data = data.split('\n')

rulesS = []
rulesD = []
for line in data:
    if line[2] == '/':
        rulesS.append([list(line[0:2]), list(line[3:5])])
        rulesD.append([list(x) for x in line.split(' => ')[1].split('/')])
    else:
        rulesS.append([list(x) for x in line.split(' => ')[0].split('/')])
        rulesD.append([list(x) for x in line.split(' => ')[1].split('/')])
print('rules')
print(rulesS)
print(rulesD)

# .#.
# ..#
# ###

g = [ list('.#.'), 
list('..#'), 
list('###'), ]

# g = [ list('123'), 
# list('456'), 
# list('789'), ]

print("g")
print(g)
print()
def rotate(g):
    if len(g) == 2:
        return [[g[1][0], g[0][0]], [g[1][1], g[0][1]]] 
    if len(g) == 3:
        return [
            [g[2][0], g[1][0], g[0][0]], 
            [g[2][1], g[1][1], g[0][1]], 
            [g[2][2], g[1][2], g[0][2]], 
        ]

def flip_v(g):
    if len(g) == 2:
        return [g[1], g[0]]
    else:
        return [g[2], g[1], g[0]]

def flip_h(g):
    return [list(reversed(row)) for row in g]


def gen_variations(g):
    for _ in range(0, 4):
        yield g
        yield flip_v(g)
        yield flip_h(g)
        g = rotate(g)

# print("var g")
# for ng in gen_variations(g):
#     for x in ng:
#         print(x)
#     print()


def find_match(to_match):
    for (i, r) in enumerate(rulesS):
        for var_r in gen_variations(r):
            if to_match == var_r:
                return rulesD[i]
    return None


def extract(g, y, x, size):
    lines = g[y*size:(y*size)+size]
    return [line[x*size:(x*size)+size] for line in lines]

def gen_next_g(g):
    if len(g) % 2 == 0:
        size = 2
    else:
        size = 3

    new_size = (len(g) // size) * (size + 1)
    return [ [' '] * new_size ] * new_size


def inject(new_g, matched, y, x):
    # print('inject', y, x)
    # print('matched')
    # print(matched)
    # print('new_g')
    # print(new_g)
    size = len(matched)
    for i in range(0, size):
        replace_from = size * x
        replace_to = replace_from + size
        line = new_g[(y * size) + i]
        new_g[y * size + i] = line[0:replace_from] + matched[i] + line[replace_to:]
        # print('new_g')
        # print(new_g)
    return new_g

for _ in range(0, 18):
    print(_)
    if len(g) % 2 == 0:
        size = 2
    else:
        size = 3

    new_g = gen_next_g(g)
    # print('new_g')
    # print(new_g)
    for y in range(0, len(g) // size):
        for x in range(0, len(g) // size):
            to_match = extract(g, y, x, size)
            # print('to_match')
            # print(to_match)
            matched = find_match(to_match)
            new_g = inject(new_g, matched, y, x)
            # print('matched')
            # print(matched)
            # print('new_g')
            # print(new_g)
            # import sys
            # sys.exit()
    g = new_g

print()
# print(new_g)
flattened = ''.join([i for line in new_g for i in line])
print(flattened)
print(sum(1 for elem in flattened if elem == '#'))
