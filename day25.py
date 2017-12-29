#       --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
#  25   00:11:55    136      0   00:12:23    130      0

from collections import defaultdict
data = open('day25.txt').read().strip()
# data = open('day25_.txt').read().strip()
lines = data.splitlines()

state = 'A'
diag = 12261543
tape = defaultdict(int)
c = 0

for i in range(0, diag):
    if state == 'A':
        if tape[c] == 0:
            tape[c] = 1
            c += 1
            state = 'B'
        else:
            tape[c] = 0
            c -= 1
            state = 'C'
    elif state == 'B':
        if tape[c] == 0:
            tape[c] = 1
            c -= 1
            state = 'A'
        else:
            tape[c] = 1
            c += 1
            state = 'C'
    elif state == 'C':
        if tape[c] == 0:
            tape[c] = 1
            c += 1
            state = 'A'
        else:
            tape[c] = 0
            c -= 1
            state = 'D'
    elif state == 'D':
        if tape[c] == 0:
            tape[c] = 1
            c -= 1
            state = 'E'
        else:
            tape[c] = 1
            c -= 1
            state = 'C'
    elif state == 'E':
        if tape[c] == 0:
            tape[c] = 1
            c += 1
            state = 'F'
        else:
            tape[c] = 1
            c += 1
            state = 'A'
    elif state == 'F':
        if tape[c] == 0:
            tape[c] = 1
            c += 1
            state = 'A'
        else:
            tape[c] = 1
            c += 1
            state = 'E'
