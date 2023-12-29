file_name = 'test_input1.txt'
file_name = 'input.txt'

with open(file_name, 'r') as fd:
    lines = fd.readlines()

fflops = {}
conjs = {}
graph = {}

for line in lines:
    source, dests = line.split(' -> ')
    dests = [x.strip() for x in dests.split(', ')]

    if source[0] in ['%', '&']:
        type = source[0]
        source = source[1:]
        if type == '%':
            fflops[source] = False
        elif type == '&':
            conjs[source] = {}


    graph[source] = dests

for source, dests in graph.items():
    for dest in dests:
        if dest in conjs:
            conjs[dest][source] = False

print(graph, conjs, fflops)

def push_button(graph, fflops, conjs):

    q = [('aptly - button module', 'broadcaster', False)]
    lows = highs = 0

    HIGH = True
    LOW = False

    while q:
        sender, receiver, signal = q.pop(0)
        if signal:
            highs += 1
        else:
            lows += 1

        receiver_is_in_network = True
        if receiver in fflops:
            if signal == HIGH:
                continue
            else:
                fflops[receiver] = not fflops[receiver]
                new_signal = fflops[receiver]
        elif receiver in conjs:
            conjs[receiver][sender] = signal
            if all(conjs[receiver].values()):
                new_signal = False
            else:
                new_signal = True
        elif receiver in graph:
            new_signal = signal
        else:
            receiver_is_in_network = False

        if receiver_is_in_network:
            for new_receiver in graph[receiver]:
                q.append([receiver, new_receiver, new_signal])

        # print(q)

    return lows, highs

# print(push_button(graph, fflops, conjs))

total_low = total_high = 0
for _ in range(1000):
    aux_low, aux_high = push_button(graph, fflops, conjs)
    total_low += aux_low
    total_high += aux_high

print(total_low * total_high)

    
