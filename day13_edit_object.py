from collections import defaultdict
from collections import namedtuple
data = open('day13.txt').read().strip()
# data = open('day13_example.txt').read().strip()
#global variable
layers = defaultdict(int)
for row in data.splitlines():
    row_data = row.split(': ')
    layers[int(row_data[0])] = int(row_data[1])

last_layer = max(layers.keys())

print(layers, last_layer)


State = namedtuple('State', ['me', 'scanners', 'severity', 'caught'])
# down True = down, False = up
# pos - 1 = null object
# Scanner = namedtuple('Scanner', ['pos', 'down'])
class Scanner:
    def __init__(self, pos, down):
        self.pos = pos
        self.down = down

    def __repr__(self):
        return '(' + str(self.pos) + ',' + str(self.down) + ')'

    def __eq__(self, other):
        return self.pos == other.pos and self.down == other.down

    def __hash__(self):
        return hash((self.pos, self.down))

def print_state(state):
    print(state.me, state.severity)
    for (layer, scanner) in enumerate(state.scanners):
        if layer > 60:
            break
        print(str(layer).zfill(2) + ':', end='')
        if scanner.pos < 0:
            if layer == state.me:
                print('M')
            else:
                print('X')
        else:
            lsc = list(" " * layers[layer])
            lsc[scanner.pos] = 'S'
            if layer == state.me:
                lsc[0] = 'M'
            sc = ''.join(lsc)
            sc += "]"
            print(sc)
    print()



# at zero
def scanner_at(state, layer):
    if layer < 0:
        return False
    return state.scanners[layer].pos == 0


def move_scanner(layer, scanner):
    if scanner.pos == -1:
        return scanner
    if scanner.down:
        if scanner.pos == layers[layer] - 1:
            #we are at bottom
            scanner.pos -= 1
            scanner.down = False
        else:
            scanner.pos += 1
    else:
        #go up
        if scanner.pos == 0:
            #go back down
            scanner.pos = 1
            scanner.down = True
        else:
            scanner.pos -= 1
    return scanner

initial_scanners_state = [Scanner(0, True) if layers[i] else Scanner(-1, False) for i in range(0, last_layer+1)]


#end state
def at_end(state):
    return state.me == last_layer

#end state
def at_end_or_caught(state):
    return at_end(state) or state.caught

def move_right(state):
    new_me = state.me + 1
    # print('s', new_me, state.scanners[new_me], scanner_at(state, new_me))
    new_severity = state.severity
    new_caught = state.caught
    if scanner_at(state, new_me):
        new_caught = True
        new_severity += (new_me * layers[new_me]) 
    new_scanners = [move_scanner(layer, scanner) for (layer, scanner) in enumerate(state.scanners)]
    return State(new_me, new_scanners, new_severity, new_caught)


def run(delay, end_state=at_end):
    state = State(-1 - delay, initial_scanners_state, 0, False)
    # print('run', delay, state)
    while not end_state(state):
        state = move_right(state)
        # print_state(state);input()
        
    # print(state.severity)
    return state

print(run(0))

d=0
while True:
    state=run(d, end_state=at_end_or_caught)
    # print(d, state.severity)
    if not state.caught:
        print(d, state)
        break
    d += 1
