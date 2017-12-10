# Partie 1 : 59:05
# beaucoup de temps passé su l'API de regexp: comment faire un match ET
# récupérer les résultats des groupes?
# Comment avoir des groupes lors de répétitions
# Se souvenir comment utiliser ipython et y invoquer le debuggeur
# Comment utiliser namedtuple et au final remplacé par une vrai classe
# car objet mutables
# Corrections de pep8 concernant l'indentation sur multilignes
# Partie 2 : 50:24
# Souffert pour déterminer quel child a un poid différent des autres,
# d'abord utilisé collections.Counter mais cela ne faisait pas ce que je veux.
# J'ai du chercher pour trouver comment récupérer le premier élément
# satisfaisant une condition dans une liste. J'aurais juré qu'il y avait
# mieux que next(x for x in list if cond(x)).
# J'ai perdu beaucoup de temps dans pdb à chercher d'ou venait le probleme
import re


class Node:
    def __init__(self, name, weight, children, parent=None):
        self.name = name
        self.weight = int(weight)
        self.children = children
        self.parent = parent

    def __repr__(self):
        ret_str = '<' + self.name + \
            '(' + str(self.weight) + ') ->' + \
            str([child.name if not isinstance(child, str) else child for child in self.children]) + \
            '. ' + str(self.parent.name if self.parent else self.parent) + '>'
        return ret_str

    def total_weight(self):
        return self.weight + sum([child.total_weight() for child in self.children])

data = open('day7.txt').read().strip()
lines = data.split('\n')


def make_node(line):
    global match
    match = re.match(r'(.+) \((\d+)\)( -> (.*))?', line)
    print(line, match)
    return Node(
        match.group(1),
        match.group(2),
        match.group(4).split(', ') if match.group(4) else [],
        None)


nodes = [make_node(line) for line in lines]
nodes_dict = {}
for node in nodes:
    nodes_dict[node.name] = node

def build_node(node, parent=None):
    if parent:
        node.parent = parent
    if not node.children:
        return node
    for i, c in enumerate(node.children):
        if isinstance(c, str):
            node.children[i] = build_node(nodes_dict[c], node)
    return node

for node in nodes:
    build_node(node)


root_node = None
for node in nodes:
    if not node.parent  :
        root_node = node
        print('root', node)
        break

def unbalanced(node):
    if not node.children:
        return node
    d = {}
    for c in node.children:
        if c.total_weight() not in d:
            d[c.total_weight()] = []
        d[c.total_weight()].append(c)
    try:
        unb_n = next(nodes[0] for (total_weight, nodes) in d.items() if len(nodes) == 1)
        return unbalanced(unb_n)
    except StopIteration:
        return node


unb_n = unbalanced(root_node)
print(unb_n)
