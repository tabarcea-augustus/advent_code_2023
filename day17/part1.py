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


def flood_fill(screen, visit_grid, start_row, start_column, row_len, col_len, color):
    queue = []
    min_heat = 99999999

    start_row = 0
    start_column = 0

    heat_loss = 0
    time = 2
    queue.append([start_row, start_column, time, heat_loss, 'down'])
    queue.append([start_row, start_column, time, heat_loss, 'right'])

    visit_grid[start_row][start_column][0] = 99999999
    visit_grid[start_row][start_column][1].add('right')
    visit_grid[start_row][start_column][1].add('down')

    ctx = 0
    while queue:
        current_row, current_column, time, heat_loss, direction = queue.pop(-1)

        if current_row == row_len - 1 and current_column == col_len - 1:
            # print(heat_loss)
            min_heat = min(min_heat, heat_loss)

        for next_dir in next_dirs[direction]:
            next_row = current_row + next_dir[0]
            next_column = current_column + next_dir[1]

            if next_row < 0 or next_row >= row_len or next_column < 0 or next_column >= col_len:
                continue

            # print(visit_grid[next_row][next_column])
            next_visited_directions = visit_grid[next_row][next_column][1]
            next_visited_direction = direction_to_name[next_dir]

            if next_visited_direction not in next_visited_directions:
                new_time = time
                if next_visited_direction == direction:
                    new_time -= 1
                else:
                    new_time = 3

                if new_time > 0:
                    new_heat_loss = heat_loss + int(screen[next_row][next_column])
                    # print(heat_loss, current_heat_loss)
                    queue.append([next_row, next_column, new_time, new_heat_loss, next_visited_direction])
                    # if current_row == 0 and current_column == 1 and next_visited_direction == 'left':
                    #     print(screen[next_row][next_column])
                    #     print(next_row, next_column)
                    #     print('time: ', new_time, ' heat: ', new_heat_loss)
                    #     print('next direction: ', next_visited_direction, 'current dir: ', direction)
                    #     print()
                    if next_row == 1 and next_column == 1:
                        print(screen[next_row][next_column])
                        print(next_row, next_column)
                        print('time: ', new_time, ' heat: ', new_heat_loss)
                        print('next direction: ', next_visited_direction, 'current dir: ', direction)
                        print()
                    visit_grid[next_row][next_column][1].add(next_visited_direction)
                    visit_grid[next_row][next_column][0] = min(visit_grid[next_row][next_column][0], new_heat_loss)
                    # print_matrix2(visit_grid)

        # print_matrix2(visit_grid)
        # ctx += 1
        # if ctx % 15 == 0:
        #     break
    return min_heat

print_matrix(grid)
min_heat = flood_fill(grid, visit_grid, 0, 0, row_len, col_len, 0)
print(min_heat)
print_matrix2(visit_grid)
