# file_name = 'test_input.txt'
file_name = 'input.txt'

def print_matrix(matrix, ):
    print('-----------------------------------------------------------')

    for row_label, row in enumerate(matrix):
        print('[%s]' % (' '.join('%03s' % i for i in row)))
    print('-----------------------------------------------------------')

with open(file_name, 'r') as fd:
    lines = fd.readlines()
    galaxy = list(map(lambda line: [x for x in line.strip() if x], lines))


new_lines = []
new_columns = []
points_coord = []
for x in range(len(galaxy)):
    print(galaxy[x])
    if all(y == '.' for y in galaxy[x]):
        new_lines.append(x)

    for y in range(len(galaxy[x])):
        if galaxy[x][y] == '#':
            points_coord.append([x, y])

galaxy_columns = list(zip(*galaxy))
for x in range(len(galaxy_columns)):
    if all(y == '.' for y in galaxy_columns[x]):
        new_columns.append(x)

print(new_lines, new_columns, points_coord)

debug_example_map = {
    (0,3): 1,
    (1,7): 2,
    (2,0): 3,
    (4,6): 4,
    (5,1): 5,
    (6,9): 6,
    (8,7): 7,
    (9,0): 8,
    (9,4): 9
}

expanded_galaxy = []

print_matrix(galaxy)

total_distance = 0
galaxy_pairs = 0
for i in range(len(points_coord)):
    for j in range(i+1, len(points_coord)):
        min_x = min(points_coord[i][0], points_coord[j][0])
        max_x = max(points_coord[i][0], points_coord[j][0])
        min_y = min(points_coord[i][1], points_coord[j][1])
        max_y = max(points_coord[i][1], points_coord[j][1])
        suplimentar_x = 0
        for x in new_lines:
            if min_x < x < max_x:
                suplimentar_x += 1
        suplimentar_y = 0
        for y in new_columns:
            if min_y < y < max_y:
                suplimentar_y += 1
        distance = abs(points_coord[i][0] - points_coord[j][0]) + abs(points_coord[i][1] - points_coord[j][1]) + suplimentar_x + suplimentar_y
        total_distance += distance
        galaxy_pairs += 1

        # print(points_coord[i], points_coord[j], distance)
        # print(debug_example_map[tuple(points_coord[i])], debug_example_map[tuple(points_coord[j])], points_coord[i], points_coord[j], distance, suplimentar_x, suplimentar_y)

print(total_distance, galaxy_pairs)