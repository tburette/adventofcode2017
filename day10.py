# Part 1 : 34:17
# Part 2 : 47:29
# I had some difficulties with the knot twisting part
# I wanted to split the 'string' in three parts : before, to be
# reversed and after
# I got unstuck by changing approach : swapping the values inline
import operator
from functools import reduce
data = open('day10.txt').read().strip()
# lengths = [int(x) for x in data.split(',')]
lengths = [ord(x) for x in data] + [17, 31, 73, 47, 23]
lengths *= 64


def knot_hash(lengths):
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
    return lst
lst = knot_hash(lengths)
print(lst[0] * lst[1])

lst2 = [reduce(operator.xor, lst[16*i:16*i+16]) for i in range(0, 16)]
r = ''.join([format(x, '02X') for x in lst2])
print(r)
