#    --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
#  15   00:14:18    482      0   00:19:10    386      0

valueA = 512
valueB = 191

factorA = 16807
factorB = 48271
mod = 2147483647

match = 0
for i in range(0, 5000000):
    while True:
        valueA = (valueA * factorA) % mod
        if valueA % 4 == 0:
            break
    while True:
        valueB = (valueB * factorB) %mod
        if valueB % 8 == 0:
            break
    if(valueA & 65535) == (valueB & 65535):
        match += 1
        print(i, match, valueA, valueB)

print(match)
