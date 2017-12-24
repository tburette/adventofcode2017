from collections import defaultdict
import itertools
import re

data = open('day24.txt').read().strip()
# data = open('day24_.txt').read().strip()
data = data.splitlines()
ports = defaultdict(set)
for line in data:
    a, b = [int(x) for x in line.split('/')]
    ports[a].add(b)
    ports[b].add(a)

print(ports)

best = None
best_strength = -999
best_len = - 1

# search
def pin(r):
    if not r:
        return 0
    else:
        return r[-1][1]

def strength(b):
    return sum([x[0] + x[1] for x in b])

def search(result):
    a = pin(result)
    for b in ports[a]:
        if not (a, b) in result and not (b, a) in result:
            n_result = result + [(a, b)]
            global best, best_strength, best_len
            if len(n_result) > best_len or \
                (len(n_result) == best_len and strength(n_result) > best_strength):
                best = n_result
                best_len = len(n_result)
                best_strength = strength(n_result)
                print(best_strength, best)
            search(n_result)

search([])

print(best)
print(best_strength)
