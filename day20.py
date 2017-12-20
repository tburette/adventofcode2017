#       --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
#  20   00:39:58    665      0   00:56:25    471      0

from collections import defaultdict
data = open('day20.txt').read().strip()
# data = open('day20_test.txt').read().strip()
data = data.split('\n')

def parse(line):
    print(line)
    p = [int(x) for x in line[3:line.index('>')].split(',')]
    v = [int(x) for x in line[line.index('>, ')+6:line.rindex('>, a')].split(",")]
    a = [int (x) for x in line[line.rindex('>, a=<')+6:-1].split(',')]
    return [p, v, a]

data = [parse(x) for x in data]

P, V, A = 0, 1, 2
X, Y, Z = 0, 1, 2

print(data)
def simul(x):
    x[V][X] += x[A][X]
    x[V][Y] += x[A][Y]
    x[V][Z] += x[A][Z]

    x[P][X] += x[V][X]
    x[P][Y] += x[V][Y]
    x[P][Z] += x[V][Z]
    return x

# while True:
#     data = [simul(part) for part in data]
#     # print(data)
#     print(min(enumerate(data), key=lambda x: sum([abs(xx) for xx in x[1][P]])))

# part 2

while True:
    #remove collisions
    pos_set = set() 
    dups = []
    for p in data:
        if tuple(p[0]) in pos_set:
            dups.append(tuple(p[0]))
        pos_set.add(tuple(p[0]))

    data = [p for p in data if tuple(p[0]) not in dups]

    data = [simul(part) for part in data]
    # print(data)
    print(len(data), min(enumerate(data), key=lambda x: sum([abs(xx) for xx in x[1][P]])))
