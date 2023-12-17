def print_matrix(matrix, ):
    print('-----------------------------------------------------------')

    for row_label, row in enumerate(matrix):
        print('[%s]' % (' '.join('%03s' % i for i in row)))
    print('-----------------------------------------------------------')

# file_name = 'test_input.txt'
file_name = 'input.txt'

with open(file_name, 'r') as fd:
    grid = fd.readlines()
    grid = list(map(lambda line: [x for x in line.strip()], grid))

grid = list(zip(*grid))
print_matrix(grid)

s = 0
for idx2, col in enumerate(grid):
    max_points = 0
    rocks_between = 0
    current_start = 0
    print(idx2)
    aux_s = 0
    for idx, x in enumerate(col):
        if x == '.':
            max_points += 1
        if x == 'O':
            max_points += 1
            rocks_between += 1
        if x == '#' or idx == len(col)-1:
            max_points = len(col) - max_points
            if rocks_between > 0:
                x = int(len(col) - current_start + 1)
                y = int(x - rocks_between - 1)
                print('\t', (x-1)*x/2 - y*(y+1)/2, x, y)
                # print(max_points-1, max_points-rocks_between)
                aux_s += (x-1)*x/2 - y*(y+1)/2
            max_points = 0
            rocks_between = 0
            current_start = idx+1
    s += aux_s
    print('\t\t', aux_s)
print(s)