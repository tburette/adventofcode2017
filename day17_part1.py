input = 304
loops = 2017


# input = 3
# loops = 9


buffer = [0]
pos = 0


for i in range(1, loops + 1):
    # print(pos, buffer)
    for _ in range(0, input):
        pos = (pos + 1) % len(buffer)
    pos += 1
    buffer.insert(pos, i)

print(pos, buffer[pos+1])
