# Partie 1 : 10:43
# Partie 2 : 2:05
# j'ai écrit le code comme si len(x) était l'indice du dernier elem et non pas
# le nombre d'élément. Ca a entrainé un IndexError
# J'imagine que ce n'est pas un hasard si l'on sort exactement un elem
# après la fin du tableau
data = open('day5.txt').read().strip()
offsets = [int(line) for line in data.split('\n')]
print(offsets)
len(offsets)

offset = 0
steps = 0
while offset >= 0 and offset < len(offsets):
    old_offset = offset
    offset += offsets[offset]
    if offsets[old_offset] >= 3:
        offsets[old_offset] -= 1
    else:
        offsets[old_offset] += 1
    steps += 1

print(steps)
