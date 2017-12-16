#    --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
#  16   00:11:43    193      0   01:05:10    473      0
# For part 2 I quickly came to the realization that bruteforce ouldn't work but I had several bugs/mistakes which slowed me down

# execute all moves from the input
# execute the input moves in a loop (slow)
# calculate the net effect of the input moves, loop over that (less slow)
# calculate the net effect of x moves and loop over that (fast)


data = open('day16.txt').read().strip()
moves = data.split(',')

a = list("abcdefghijklmnop")
for move in moves:
    if move[0] == 's':
        X = int(move[1:])
        a = a[-X:] + a[:-X]
    if move[0] == 'x':
        A = int(move[1:].split('/')[0])
        B = int(move[1:].split('/')[1])
        tmp = a[A]
        a[A] = a[B]
        a[B] = tmp
    if move[0] == 'p':
        A = move[1]
        B = move[3]
        iA = a.index(A)
        iB = a.index(B)
        tmp = a[iA]
        a[iA] = a[iB]
        a[iB] = tmp
print(''.join(a))

# abcdefghijklmnop
# bijankplfgmeodhc
# 0123456789012345


# def swap(list, source, to):
#         tmp = a[source]
#         a[source] = a[to]
#         a[to] = tmp

# swaps=[
# (0, 3),
# (1, 0),
# (2, 15),
# (3, 13),
# (4, 11),
# (5, 8),
# (6, 9),
# (7, 14),
# (8, 1),
# (9, 2),
# (10, 5),
# (11, 7),
# (12, 10),
# (13, 4),
# (14, 12),
# (15, 6),
# ]

# a = list("abcdefghijklmnop")
# # for _ in range(0, 1000 * 1000 * 1000):
# for _ in range(0, 1000 * 1000):
#     for (source, to) in swaps:
#         swap(a, source, to)

# print('slow1', ''.join(a))

# a = list("abcdefghijklmnop")
# # for _ in range(0, 1000 * 1000 * 1000):
# for _ in range(0, 1):
#     a = a[1] + \
#         a[8] + \
#         a[9] + \
#         a[0] + \
#         a[13] + \
#         a[10] + \
#         a[15] + \
#         a[11] + \
#         a[5] + \
#         a[6] + \
#         a[12] + \
#         a[4] + \
#         a[14] + \
#         a[3] + \
#         a[7] + \
#         a[2]

# print('1mil bug', ''.join(a))


a = list("abcdefghijklmnop")
for _ in range(0, 1000):
    for move in moves:
        if move[0] == 's':
            X = int(move[1:])
            a = a[-X:] + a[:-X]
        if move[0] == 'x':
            A = int(move[1:].split('/')[0])
            B = int(move[1:].split('/')[1])
            tmp = a[A]
            a[A] = a[B]
            a[B] = tmp
        if move[0] == 'p':
            A = move[1]
            B = move[3]
            iA = a.index(A)
            iB = a.index(B)
            tmp = a[iA]
            a[iA] = a[iB]
            a[iB] = tmp
thousand = ''.join(a)





# abcdefghijklmnop
# bpjahknliomefdgc thousand
# 0123456789012345

for c in thousand:
    i = 'abcdefghijklmnop'.index(c)
    print('    a[' + str(i) + '] + \\')

a = list("abcdefghijklmnop")
# for _ in range(0, 1000 * 1000 * 1000):
# for _ in range(0, 1000 * 1000):
for _ in range(0, 10):
    # if _ % 1000000 == 0:
    #     print(_)
    a = a[1] + \
    a[15] + \
    a[9] + \
    a[0] + \
    a[7] + \
    a[10] + \
    a[13] + \
    a[11] + \
    a[8] + \
    a[14] + \
    a[12] + \
    a[4] + \
    a[5] + \
    a[3] + \
    a[6] + \
    a[2]

print('part 2', ''.join(a))
