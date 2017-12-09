# un peu de mal avec les list comprehension imbriquées
# oublié de mettre le 2 à permutations(2)
import itertools
data = open('day2.txt').read().strip()
rows = [[int(v) for v in row.split('\t')] for row in data.split('\n')]
print(sum(max(row) - min(row) for row in rows))
print(sum([x/y for row in rows for (x, y) in itertools.permutations(row, 2) if x%y == 0]))
