from collections import defaultdict
data = open('day18.txt').read().strip()
data = data.split('\n')

def gen(p):

    regs = defaultdict(int)
    regs['p'] = p
    l_sound = None
    def value(val):
        if isinstance(val, int):
            return val
        else:
            return regs[val] 

    i = 0
    while i < len(data):
        line = data[i]
        instr = line[0:3]
        reg = line[4:5]
        val = line[6:]
        if val:
            if val[0] in '-0123456789':
                val = int(val)
        print(i, instr, reg, val, value(val), regs)
        if instr == 'jgz':
            if regs[reg]:
                i += value(val)
                continue
        if instr == 'snd':
            l_sound = regs[reg]
            # lregs[reg] = regs[reg] 
        elif instr == 'set':
            regs[reg] = value(val)
        elif instr == 'add':
            regs[reg] += value(val)
        elif instr == 'mul':
            regs[reg] *= value(val)
        elif instr == 'mod':
            regs[reg] = regs[reg] % value(val)
        elif instr == 'rcv':
            if regs[reg] != 0:
                # print(lregs[reg])
                print(l_sound)
                break
        i += 1

def snd_0(val):
    global gen_1
    gen_1.send(val)

def snd_1(val):
    global gen_0
    gen_0.send(val)

gen_0 = gen(0)
gen_1 = gen(1)
