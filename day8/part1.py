
with open('input.txt', 'r') as fd:
    content = fd.read().split('\n\n')

    instruction = [int(x) for x in content[0].replace('L', '0').replace('R', '1')]
    map_lines = content[1].split('\n')

map_left_right = {}
for map_line in map_lines:
    aux_map_line_split = map_line.split(' = ')
    map_left_right[aux_map_line_split[0]] = [aux_map_line_split[1].split(', ')[0].replace('(', ''), aux_map_line_split[1].split(', ')[1].replace(')', '')]


print(instruction, map_left_right)

node_value = 'AAA'

steps = 0
while node_value != 'ZZZ':
    print(steps%len(instruction), steps, len(instruction), instruction[steps%len(instruction)])
    node_value = map_left_right[node_value][instruction[steps%len(instruction)]]
    print(node_value)
    steps += 1

print(steps)
