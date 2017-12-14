# Part 1: 45:00
# Part 2: 20:24
# Wasted a lot of time rebuilding the knot_hash function
# for some stupid reason I thought the *64 and 17,... were 
# not part of the hash and only added for part 2 of day 10
# I also wasted time in part 2 because I forgot to remove the tst
# input!
import operator
from functools import reduce
import networkx as nx
data = 'jxqlasbh'
# data = 'flqrgnkx'

def knot_hash(str):
    lengths = [ord(x) for x in str] + [17, 31, 73, 47, 23]
    lengths *= 64
    lst = list(range(0, 256))
    # lst = list(range(0, 5))
    # lengths = [3, 4, 1, 5]
    pos = 0
    skip = 0

    # print(pos, skip, lst)
    for length in lengths:
        for p in range(0, length // 2):
            src_i = (pos+p)%len(lst)
            dst_i = (pos + length - 1 -p)%len(lst)
            lst[src_i], lst[dst_i] = lst[dst_i], lst[src_i]
        pos = pos + length + skip
        skip += 1
        # print(length, pos, skip, lst)
        # input()
    lst2 = [reduce(operator.xor, lst[16*i:16*i+16]) for i in range(0, 16)]
    return ''.join([format(x, '02X') for x in lst2])
# r = ''.join([format(x, '02X') for x in lst2])
# print(r)


inputs = ['{}-{}'.format(data, i) for i in range(0, 128)]
outputs = [knot_hash(x) for x in inputs]
outputs = [list(map(lambda x: int(x, 16), h)) for h in outputs]
# outputs = [[ [x>>4, x&0b00001111] for x in h] for h in outputs]

# outputs = [[n for t in h for n in t] for h in outputs]
outputs = [['{:04b}'.format(x) for x in h] for h in outputs]
outputs = [[int(c) == 1 for x in h for c in x] for h in outputs]
print(sum([v for l in outputs for v in l if v == 1]))

def s(y, x):
    return str(y) + ',' + str(x)

def at(y, x):
    return outputs[y][x]

g = nx.Graph()
for (y, l) in enumerate(outputs):
    for (x, vinput) in enumerate(l):
        if not at(y, x):
            continue
        g.add_edge(s(y, x), s(y, x))
        if y > 0 and at(y-1, x):
            g.add_edge(s(y, x), s(y-1, x))
        if y < 127 and at(y+1, x):
            g.add_edge(s(y, x), s(y+1, x))
        if x > 0 and at(y, x-1):
            g.add_edge(s(y, x), s(y, x-1))
        if x < 127 and at(y, x+1):
            g.add_edge(s(y, x), s(y, x+1))
        # print(x, y, v, g.edges)
        # input()

print(nx.node_connected_component(g, '0,0'))
print(nx.number_connected_components(g))

# [ ''.join(map(str, map(int, line[:20]))) for line in outputs[:10]]
