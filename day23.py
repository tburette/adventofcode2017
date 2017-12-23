#       --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
#  23   00:17:43    525      0   01:38:43    401      0


from collections import defaultdict
data = open('day23.txt').read().strip()
# data = open('day23_.txt').read().strip()
data = data.split('\n')

nb_mul = 0
# regs = defaultdict(int)
regs = {}
for c in 'abcdefgh':
    regs[c] = 0
regs['a'] = 1
def print_state():
    print(old_i+1, i+1, line)
    for c in 'abcdefgh':
        print(c, regs[c])


def value(val):
    if isinstance(val, int):
        return val
    else:
        return regs[val] 

i = 0
old_i = i
while i < len(data):    
    old_i = i
    # print(i)
    line = data[i]
    instr = line[0:3]
    reg = line[4:5]
    val = line[6:]
    if reg:
        if reg[0] in '-0123456789':
            reg = int(reg)
    if val:
        if val[0] in '-0123456789':
            val = int(val)
    # print(p, i, instr, reg, val, value(val), regs)
    if instr == 'jgz':
        if regs[reg]:
            i += value(val)
            continue
    if instr == 'jnz':
        if value(reg):
            i += value(val)
            print_state()
            input()
            continue
    elif instr == 'snd':
        print(p, ' sends ', regs[reg])
        snd(regs[reg])
        # lregs[reg] = regs[reg] 
    elif instr == 'set':
        regs[reg] = value(val)
    elif instr == 'sub':
        regs[reg] -= value(val)
    elif instr == 'add':
        regs[reg] += value(val)
    elif instr == 'mul':
        regs[reg] *= value(val)
        nb_mul += 1
    elif instr == 'mod':
        regs[reg] = regs[reg] % value(val)
    elif instr == 'rcv':
        print(regs[reg])
    else:
        print('unknown')
    i += 1
    print_state()
    input()
print(nb_mul)
