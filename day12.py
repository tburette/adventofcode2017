#       --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
#  12   00:23:28    775      0   00:25:30    565      0
# Recognized the description was of a graph
# I knew networkx would help me. It's API took quite a bit of time to understand
import re
import networkx as nx
data = open('day12.txt').read().strip()
lines = data.splitlines()
G = nx.Graph()
for line in lines:
    print(line)
    match = re.match(r'(.*) <-> (.*)$', line)
    source = int(match.group(1))
    for dest in match.group(2).split(', '):
        dest = int(dest)
        print(source, dest)
        G.add_edge(source, dest)
print(len(nx.node_connected_component(G, 0)))
print(nx.number_connected_components(G))
