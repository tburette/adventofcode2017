# Partie 1 : 23:00
# Partie 2 : 5:20
# Pour eviter le probleme de list non hashable j'ai defini banks comme set
# et j'ai du convertir banks en banks_l (list) pour pouvoir modifier...moche
# bloqué sur partie 1 a cause de bugs
# Erreur dans partie 2 : introduit a quel etape commence la boucle au lieu du
# nombre de redistributions
data = open('day6.txt').read().strip()
banks = [int(bank) for bank in data.split('\t')]
# banks = [0, 2, 7, 0]
banks = tuple(banks)
print(banks)
seen = set()
seen.add(banks)
steps = 0
seen_at_step = {}
seen_at_step[banks] = steps
while True:
    print(banks, seen, seen_at_step)
    redis_bank_index = banks.index(max(banks))
    banks_l = list(banks)
    blocks_to_redis = banks_l[redis_bank_index]
    banks_l[redis_bank_index] = 0
    redis_bank_index = (redis_bank_index + 1) % len(banks)
    while blocks_to_redis > 0:
        banks_l[redis_bank_index] += 1
        blocks_to_redis -= 1
        redis_bank_index = (redis_bank_index + 1) % len(banks)
    banks = tuple(banks_l)
    steps += 1
    if banks in seen:
        break
    seen.add(banks)
    seen_at_step[banks] = steps
print(steps, seen_at_step[banks])
