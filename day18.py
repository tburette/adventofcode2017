#       --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
# 18   00:29:51    429      0   01:41:53    488      0

from collections import defaultdict
data = open('day18.txt').read().strip()
data = data.split('\n')

def gen(p, snd):
    regs = defaultdict(int)
    regs['p'] = p
    def value(val):
        if isinstance(val, int):
            return val
        else:
            return regs[val] 

    i = 0
    print('run', p)
    while i < len(data):
        line = data[i]
        instr = line[0:3]
        reg = line[4:5]
        val = line[6:]
        if val:
            if val[0] in '-0123456789':
                val = int(val)
        # print(p, i, instr, reg, val, value(val), regs)
        if instr == 'jgz':
            if regs[reg]:
                i += value(val)
                continue
        if instr == 'snd':
            print(p, ' sends ', regs[reg])
            snd(regs[reg])
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
            print(p, ' to receive')
            regs[reg] = yield
            print(p, ' received ', regs[reg])
        i += 1
    print(p, 'end')

import queue
q0 = queue.Queue(maxsize=0)
q1 = queue.Queue(maxsize=0)

def snd_0(val):
    global q1
    q1.put(val)


p1_sends = 0
def snd_1(val):
    global q0
    global p1_sends
    q0.put(val)
    p1_sends += 1


gen_0 = gen(0, snd_0)
gen_1 = gen(1, snd_1)

next(gen_0)
next(gen_1)
finished_0 = False
finished_1 = False
while not (finished_0 and finished_1):
    print(finished_0, finished_1)
    if not finished_0:
        if q0.empty() and finished_1:
            finished_0 = True
            print('O done')
        else:
            try:
                while not q0.empty():
                    gen_0.send(q0.get_nowait())
                print('q0 empty')
            except StopIteration:
                print('0 done x')
                finished_0 = True


    if not finished_1:
        if q1.empty() and finished_0:
            finished_1 = True
        else:
            try:
                print('x', finished_0, finished_1)
                while not q1.empty():
                    gen_1.send(q1.get_nowait())
                print('q1 empty')
                print('y', finished_0, finished_1)
            except StopIteration:
                print('1 done')
                finished_1 = True

print(p1_sends)
