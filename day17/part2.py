import heapq


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
file_name = 'input.txt'

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
    'right': [right, up, down],
    'all_start': [up, down, left, right]
}


def flood_fill(screen, row_len, col_len):
    # cost, x, y, next_dir, steps
    q = [(0, 0, 0, 'all_start', -1)]
    d = {}
    while q:
        current_cost, current_row, current_column, direction, steps = heapq.heappop(q)

        if (current_row, current_column, direction, steps) in d:
            continue
        d[(current_row, current_column, direction, steps)] = current_cost
        for next_dir in next_dirs[direction]:
            next_row = current_row + next_dir[0]
            next_column = current_column + next_dir[1]
            next_direction = direction_to_name[next_dir]

            if next_direction == direction:
                next_steps = steps + 1
            else:
                next_steps = 1

            if 0 <= next_row < row_len and 0 <= next_column < col_len:
                if next_steps <= 10 and (next_direction == direction or steps >= 4 or steps == -1):
                    new_cost = int(screen[next_row][next_column])
                    if (next_row, next_column, next_direction, next_steps) in d:
                        continue
                    heapq.heappush(q,
                                   (current_cost + new_cost, next_row, next_column, next_direction, next_steps))

        # print(q)

    # print(d)
    res = 99999999
    for (row, col, direction, steps), cost in d.items():

        if row == row_len - 1 and col == col_len - 1:
            if steps >= 4:
                print(cost)
                res = min(res, cost)

    return res

print_matrix(grid)
print(flood_fill(grid, row_len=row_len, col_len=col_len))