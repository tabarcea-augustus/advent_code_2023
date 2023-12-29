file_name = 'test_input.txt'
file_name = 'input.txt'

with open(file_name, 'r') as fd:
    lines = fd.readlines()
    grid = [tuple(x for x in line.strip()) for line in lines]

# print(grid)
start_row = start_col = -1
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[col][row] == 'S':
            start_row, start_col = row, col
            break

# print(start_row, start_col)

row_len, col_len = len(grid), len(grid[0])


def move_over_grid(grid, start_row, start_col, max_steps):
    step = 0
    q = [(start_row, start_col, step)]

    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    visited = set()
    distances_at_step = dict()

    while q:
        # print(q, distances_at_step)
        current_row, current_col, current_step = q.pop(0)

        if current_step == max_steps + 1:
            continue

        if (current_row, current_col) in visited:
            continue

        visited.add((current_row, current_col))

        if current_step in distances_at_step:
            distances_at_step[current_step] += 1
        else:
            distances_at_step[current_step] = 1

        for dir in directions:
            next_row = current_row + dir[0]
            next_col = current_col + dir[1]
            if grid[next_row % 131][next_col % 131] != '#':
                q.append((next_row, next_col, current_step + 1))

    return distances_at_step


first_n_quadratic_function_points = []

steps_goal = 26501365
diamond_axis_length = row_len // 2

for i in range(3):
    max_steps = diamond_axis_length + i * row_len
    # print(max_steps)
    distances_at_step = move_over_grid(grid, start_row, start_col, max_steps)
    # print(len(distances_at_step))
    # print()

    s = 0
    for k, v in distances_at_step.items():
        if k % 2 == max_steps % 2:
            s += v

    first_n_quadratic_function_points.append(s)

# print(first_n_quadratic_function_points)

a = (first_n_quadratic_function_points[2] - (2 * first_n_quadratic_function_points[1]) + first_n_quadratic_function_points[0]) // 2
b = first_n_quadratic_function_points[1] - first_n_quadratic_function_points[0] - a
c = first_n_quadratic_function_points[0]
n = (steps_goal - diamond_axis_length) // row_len
print((a * n ** 2) + (b * n) + c)