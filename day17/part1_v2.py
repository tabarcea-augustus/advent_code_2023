def print_matrix(matrix, ):
    print('-----------------------------------------------------------')

    for row_label, row in enumerate(matrix):
        print('[%s]' % (' '.join('%03s' % i for i in row)))
    print('-----------------------------------------------------------')


def print_matrix2(matrix, ):
    print('-----------------------------------------------------------')

    for row_label, row in enumerate(matrix):
        print('[%s]' % (' '.join('%03s' % i[0] for i in row)))
    print('-----------------------------------------------------------')


file_name = 'test_input.txt'
# file_name = 'input.txt'

with open(file_name, 'r') as fd:
    content = fd.readlines()
    grid = list(map(lambda x: [y for y in x.strip() if x], content))

row_len = len(grid)
col_len = len(grid[0])
visit_grid = [[[99999999, set()] for _ in range(col_len)] for _ in range(row_len)]

up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)
direction_to_name = {
    (-1, 0): 'up',
    (1, 0): 'down',
    (0, -1): 'left',
    (0, 1): 'right'
}
name_to_direction = {
    'up': up,
    'down': down,
    'left': left,
    'right': right
}
next_dirs = {
    'up': [up, left, right],
    'down': [down, left, right],
    'left': [left, up, down],
    'right': [right, up, down]
}

def flood_fill(screen, visit_grid, start_row=0, start_column=0, row_len, col_len, color):
