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


def flood_fill(screen, visit_grid, current_row, current_column, row_len, col_len, color, direction) -> None:
    if current_row < 0 or current_row >= row_len or current_column < 0 or current_column >= col_len:
        return
    # print(2)
    curent_color = color+1
    ok = False
    directions = visit_grid[current_row][current_column][1]
    if len(directions) == 4:
        return
    # print(screen[current_row][current_column], direction, directions)
    print_matrix(visit_grid)
    if direction not in directions:
        ok = True

    if visit_grid[current_row][current_column] == 0:
        visit_grid[current_row][current_column][0] = curent_color
        visit_grid[current_row][current_column][1].add(direction)
    else:
        visit_grid[current_row][current_column][0] = curent_color
        visit_grid[current_row][current_column][1].add(direction)


    # print(curent_color, screen[current_row][current_column])
    if ok:
        if screen[current_row][current_column] == '.':
            if direction == 0:
                flood_fill(screen, visit_grid, current_row - 1, current_column, row_len, col_len, curent_color, direction=direction)  # top
            elif direction == 1:
                flood_fill(screen, visit_grid, current_row, current_column + 1, row_len, col_len, curent_color, direction=direction)  # right
            elif direction == 2:
                flood_fill(screen, visit_grid, current_row + 1, current_column, row_len, col_len, curent_color, direction=direction)  # bottom
            elif direction == 3:
                flood_fill(screen, visit_grid, current_row, current_column - 1, row_len, col_len, curent_color, direction=direction)  # left

        elif screen[current_row][current_column] == '\\':
            if direction == 0:
                flood_fill(screen, visit_grid, current_row, current_column - 1, row_len, col_len, curent_color, direction=3)  # top to left
            elif direction == 1:
                flood_fill(screen, visit_grid, current_row + 1, current_column, row_len, col_len, curent_color, direction=2)  # right to bottom
            elif direction == 2:
                flood_fill(screen, visit_grid, current_row, current_column + 1, row_len, col_len, curent_color, direction=1)  # bottom to right
            elif direction == 3:
                flood_fill(screen, visit_grid, current_row - 1, current_column, row_len, col_len, curent_color, direction=0) # left to top

        elif screen[current_row][current_column] == '/':
            if direction == 0:
                flood_fill(screen, visit_grid, current_row, current_column + 1, row_len, col_len, curent_color, direction=1) # top to right
            elif direction == 1:
                flood_fill(screen, visit_grid, current_row - 1, current_column, row_len, col_len, curent_color, direction=0)  # right to top
            elif direction == 2:
                flood_fill(screen, visit_grid, current_row, current_column - 1, row_len, col_len, curent_color, direction=3) # bottom to left
            elif direction == 3:
                flood_fill(screen, visit_grid, current_row + 1, current_column, row_len, col_len, curent_color, direction=2) # left to bottom

        elif screen[current_row][current_column] == '|':
            if direction in [0, 2]:
                aux_current_row = current_row - 1 if direction == 0 else current_row + 1
                flood_fill(screen, visit_grid, aux_current_row, current_column, row_len, col_len, curent_color, direction=direction) # top to top, bot to bot
            else:
                flood_fill(screen, visit_grid, current_row - 1, current_column, row_len, col_len, curent_color, direction=0) # top
                flood_fill(screen, visit_grid, current_row + 1, current_column, row_len, col_len, curent_color, direction=2) # bot

        elif screen[current_row][current_column] == '-':
            if direction in [1, 3]:
                aux_current_col = current_column + 1 if direction == 1 else current_column - 1
                flood_fill(screen, visit_grid, current_row, aux_current_col, row_len, col_len, curent_color, direction=direction)  # top to top, bot to bot
            else:
                flood_fill(screen, visit_grid, current_row, current_column + 1, row_len, col_len, curent_color, direction=1) # right
                flood_fill(screen, visit_grid, current_row, current_column - 1, row_len, col_len, curent_color, direction=3) # left





file_name = 'test_input.txt'
# file_name = 'input.txt'

with open(file_name, 'r') as fd:
    content = fd.readlines()
    grid = list(map(lambda x: [y for y in x.strip() if x], content))

print_matrix(grid)

row_len = len(grid)
col_len = len(grid[0])
print(row_len, col_len)

visit_grid = [[[0, set()] for _ in range(col_len)] for _ in range(row_len)]
print(len(visit_grid), len(visit_grid[0]))
# print_matrix(visit_grid)

try:
    flood_fill(grid, visit_grid, 0, 0, row_len, col_len, 0, direction=1)
    print_matrix2(visit_grid)
except:
    for row in visit_grid:
        print([x[0] for x in row])
print()


s = 0
for row in visit_grid:
    for x in row:
        if x[0] != 0:
            s+=1
print(s)