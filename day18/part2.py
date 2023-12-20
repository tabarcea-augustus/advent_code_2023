file_name = 'test_input.txt'
file_name = 'input.txt'

with open(file_name, 'r') as fd:
    lines = fd.readlines()

directions = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1)
}
directions_from_hex = {
    3: (-1, 0),
    0: (0, 1),
    1: (1, 0),
    2: (0, -1)
}
shoelace_positive_sum = 0
shoelace_negative_sum = 0
polygon_border_points_sum = 0

current_point = (0, 0)

for line in lines:
    direction_string, steps, color = line.split()

    color = color.replace('(#', '').replace(')', '')
    steps = int(color[:5], base=16)
    direction = directions_from_hex[int(color[5])]

    polygon_border_points_sum += steps

    next_point = (current_point[0] + direction[0] * steps, current_point[1] + direction[1] * steps)

    shoelace_positive_sum += current_point[0] * next_point[1]
    shoelace_negative_sum += current_point[1] * next_point[0]

    current_point = next_point

# shoelace formula
internal_area = abs(shoelace_positive_sum - shoelace_negative_sum) / 2
#pick formula
print(internal_area + polygon_border_points_sum / 2 + 1)