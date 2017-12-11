#       --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
# 11   00:54:58   1048      0   01:05:20   1046      0
# Part1 : 18:00
# Part2 : 19:08
# perdu du temps avec l'expression régulière : je m'étais dit à un challenge précédent que j'aurais du utiliser des groups nommés car plus clair et auto documenté mais cela m'a fait perdre du temps
# J'ai eu l'idée d'utiliser eval pour gagner du temps mais la réflexion sur la conversion du nom de registre en sa valeur + lecture de doc + écrire la bonne regexp m'a fait perdre du temps. J'aurais peut-être été tout aussi rapide en écrivant du code 'manuel' pour la vérification de la condition
#Le linter est 'trop bien fait'. le texte entouré est si génant que je préfère perdre du temps à l'enlever plutôt que de progresser.

from collections import defaultdict
import re
data = open('day8.txt').read().strip()
rows = data.split('\n')
registers = defaultdict(int)
global_max = -9999999
for row in rows:
    match = re.match(r'(?P<reg>.*) (?P<dir>inc|dec) (?P<amount>.*) if (?P<cond_reg>.*?) (?P<cond>.*)$', row)
    reg = match.group('reg')
    if eval(str(registers[match.group('cond_reg')]) + match.group('cond')):
        change_by = int(match.group('amount'))
        if match.group('dir') == 'dec':
            change_by *= -1
        registers[reg] += change_by
        if registers[reg] > global_max: global_max = registers[reg]

max = -99999999
for (reg, val) in registers.items():
    if(val > max): max = val

print(max)

print(global_max)
