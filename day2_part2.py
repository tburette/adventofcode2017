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

for line in data:
    
data = {}


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

while True:
    data = [simul(part) for part in data]
    # print(data)
    print(min(enumerate(data), key=lambda x: sum([abs(xx) for xx in x[1][P]])))
