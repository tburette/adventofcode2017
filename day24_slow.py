import itertools
import re

data = open('day24.txt').read().strip()
# data = open('day24_.txt').read().strip()
data = data.splitlines()

ports = [line.split('/') for line in data]
ports = [list(map(int, l)) for l in ports]
ports = [tuple(l) for l in ports]

# search
def pin(r):
    if not r:
        return 0
    else:
        return r[-1][1]

def strength(b):
    return sum([x[0] + x[1] for x in b])

best = None
best_strength = -999

def search(result, ports_left):
    def add(port, reverse=False):
        print(best_strength, best)
        n_ports_left = ports_left.copy()
        n_ports_left.remove(port)
        n_result = result.copy()
        if reverse:
            port = (port[1], port[0])
        n_result.append(port)
        global best
        global best_strength
        if strength(n_result) > best_strength:
            best = n_result
            best_strength = strength(n_result)
        search(n_result, n_ports_left)
    for port in ports_left:
        if port[0] == pin(result):
            add(port)
        if port[1] == pin(result):
            add(port, True)


ports = sorted(ports, key=lambda x:x[0]+x[1])
search([], ports.copy())
print(best)
print(best_strength)
