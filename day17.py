#       --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
#  17   00:25:53    747      0   00:38:54    523      0

input = 304
loops = 50 * 1000 * 1000


# input = 3
# loops = 4


# buffer = [0]
val_at_one = None
buf_len = 1
pos = 0


for i in range(1, loops + 1):
    if i%100000 == 0:
        print(i)
    # print(pos, buffer)
    pos = (pos + input) % buf_len
    # for _ in range(0, input):
    #     pos = (pos + 1) % buf_len

    pos += 1
    if pos == 1:
        val_at_one = i
    # buffer.insert(pos, i)
    buf_len += 1

print(val_at_one)
