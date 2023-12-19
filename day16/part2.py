def print_matrix(matrix, ):
    print('-----------------------------------------------------------')

    for row_label, row in enumerate(matrix):
        print('[%s]' % (' '.join('%02s' % i for i in row)))
    print('-----------------------------------------------------------')


def print_matrix2(matrix, ):
    print('-----------------------------------------------------------')

    for row_label, row in enumerate(matrix):
        print('[%s]' % (' '.join('%02s' % i[0] for i in row)))
    print('-----------------------------------------------------------')


file_name = 'test_input.txt'
file_name = 'input.txt'

with open(file_name, 'r') as fd:
    content = fd.readlines()
    grid = list(map(lambda x: [y for y in x.strip() if x], content))

row_len = len(grid)
col_len = len(grid[0])
visit_grid = [[[0, set()] for _ in range(col_len)] for _ in range(row_len)]

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
    '-': {
        'up': [left, right],
        'down': [left, right],
        'left': [left],
        'right': [right]

    },
    '|': {
        'up': [up],
        'down': [down],
        'left': [up, down],
        'right': [up, down]
    },
    '\\': {
        'up': [left],
        'down': [right],
        'left': [up],
        'right': [down]
    },
    '/': {
        'up': [right],
        'down': [left],
        'left': [down],
        'right': [up]
    },
    '.': {
        'up': [up],
        'down': [down],
        'left': [left],
        'right': [right]
    }
}


def flood_fill(screen, visit_grid, start_row, start_column, row_len, col_len, color, direction):
    queue = []
    current_color = color + 1
    visited_directions = visit_grid[start_row][start_column][1]

    queue.append([start_row, start_column, direction])

    visit_grid[start_row][start_column][0] = current_color
    visit_grid[start_row][start_column][1].add(direction)
    current_color += 1

    while queue:
        current_row, current_column, direction = queue.pop()
        symbol = screen[current_row][current_column]

        for next_dir in next_dirs[symbol][direction]:
            next_row = current_row + next_dir[0]
            next_column = current_column + next_dir[1]

            if next_row < 0 or next_row >= row_len or next_column < 0 or next_column >= col_len:
                continue

            # print(visit_grid[next_row][next_column])
            next_visited_directions = visit_grid[next_row][next_column][1]
            next_visited_direction = direction_to_name[next_dir]

            if next_visited_direction not in next_visited_directions:
                queue.append([next_row, next_column, next_visited_direction])
                visit_grid[next_row][next_column][1].add(next_visited_direction)
                visit_grid[next_row][next_column][0] = current_color
                current_color += 1

def get_visit_grid_light_squares(grid_visit):
    s = 0
    for row in grid_visit:
        for x in row:
            if x[0] != 0:
                s+=1
    return s

res = []

for row_num in range(1, row_len-1):
    visit_grid = [[[0, set()] for _ in range(col_len)] for _ in range(row_len)]
    flood_fill(grid, visit_grid, row_num, 0, row_len, col_len, 0, direction='right')
    res.append(get_visit_grid_light_squares(visit_grid))

    visit_grid = [[[0, set()] for _ in range(col_len)] for _ in range(row_len)]
    flood_fill(grid, visit_grid, row_num, col_len-1, row_len, col_len, 0, direction='left')
    res.append(get_visit_grid_light_squares(visit_grid))

visit_grid = [[[0, set()] for _ in range(col_len)] for _ in range(row_len)]
flood_fill(grid, visit_grid, 0, 0, row_len, col_len, 0, direction='down')
res.append(get_visit_grid_light_squares(visit_grid))

visit_grid = [[[0, set()] for _ in range(col_len)] for _ in range(row_len)]
flood_fill(grid, visit_grid, 0, 0, row_len, col_len, 0, direction='right')
res.append(get_visit_grid_light_squares(visit_grid))

visit_grid = [[[0, set()] for _ in range(col_len)] for _ in range(row_len)]
flood_fill(grid, visit_grid, row_len-1, col_len-1, row_len, col_len, 0, direction='left')
res.append(get_visit_grid_light_squares(visit_grid))

visit_grid = [[[0, set()] for _ in range(col_len)] for _ in range(row_len)]
flood_fill(grid, visit_grid, row_len-1, col_len-1, row_len, col_len, 0, direction='up')
res.append(get_visit_grid_light_squares(visit_grid))

for col_num in range(1, col_len-1):
    visit_grid = [[[0, set()] for _ in range(col_len)] for _ in range(row_len)]
    flood_fill(grid, visit_grid, 0, col_num, row_len, col_len, 0, direction='down')
    res.append(get_visit_grid_light_squares(visit_grid))

    visit_grid = [[[0, set()] for _ in range(col_len)] for _ in range(row_len)]
    flood_fill(grid, visit_grid, row_len-1, col_num, row_len, col_len, 0, direction='up')
    res.append(get_visit_grid_light_squares(visit_grid))

print(max(res))


