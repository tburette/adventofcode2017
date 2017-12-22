#       --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
#  22   00:20:28    214      0   00:28:19    196      0
# Spent quite a bit of time reading/understanding the puzzle
# No bug!

from collections import defaultdict
data = open('day22.txt').read().strip()
# data = open('day22_.txt').read().strip()
data = data.split('\n')
g = defaultdict(lambda: 'c')
for (y, line) in enumerate(data):
    for (x, c) in enumerate(line):
        print(y, x, c)
        g[(y, x)] = 'i' if c == '#' else 'c'

x = len(line) // 2
y = len(data) // 2
d = 0 #0, 1, 2, 3; 0=up, 1=right,...
b = 0
b_i = 0

print(b, b_i)
for _ in range(0, 10000000):
    if(g[(y, x)] == 'c'):
        d = (d-1) % 4
        g[(y, x)] = 'w'
    elif g[(y, x)] == 'w':
        g[(y, x)] = 'i'
        b_i += 1
    elif g[(y, x)] == 'i':
        d = (d+1) % 4
        g[(y, x)] = 'f'
    elif g[(y, x)] == 'f':
        d = (d+2) % 4
        g[(y, x)] = 'c'

    b += 1
    if d == 0:
        y -= 1
    if d == 1:
        x += 1
    if d == 2:
        y += 1
    if d == 3:
        x -= 1
    # print(b, b_i)

print(b, b_i)
