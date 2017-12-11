# Part1 : 21:30
# Part 2: 23:00
# j'ai voulu faire quelquechose de beau (genre fold avec fonction faisant évoluer l'état) en style fonctionnel.
# J'ai abandonné pour avancer et faire une machine état c-like

data = open('day9.txt').read().strip()

i = 0
total_score = 0
garbage_count = 0
cur_group_score = 0
state = 'group_sep'
while i < len(data):
    c = data[i]
    print(i, c, state, cur_group_score, total_score)
    i += 1
    if state == 'group_sep':  # debut ou entre , ou fin
        if c == ',':
            continue
        elif c == '{':
            cur_group_score += 1
            total_score += cur_group_score
        elif c == '}':
            cur_group_score -= 1
        elif c == '<':
            state = 'garbage'
    elif state == 'garbage':
        if c == '!':
            i += 1
        elif c == '>':
            state = 'group_sep'
        else:
            # skip garbage char
            garbage_count += 1

print(total_score)
print(garbage_count)
