import sys
h = 0
for val in range(105700, 122700 + 1, 17):
    for i in range(2, val):
        if val % i == 0:
            h += 1
            break
print(h)
sys.exit()

b=0;c=0;d=0;e=0;f=0;g=0;h=0

b = 57 * 100 + 100000
c = b + 17000

while True:
    f = 1
    d = 2

    while True:
        while True:
            e = 2
            g = d * e - b
            if g == 0:
                f = 0
            e += 1
            g = e - b
            if g == 0:
                break
        d += 1
        g = d - b
        if g == 0:
            break
    if f == 0:
        h += 1
    g = b - c
    if g == 0:
        print(h)
        exit()
    b += 17
