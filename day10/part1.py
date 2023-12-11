with open('test_input3.txt', 'r') as fd:
# with open('input.txt', 'r') as fd:
    lines = fd.readlines()
    pipe_map = []
    visit_map = []
    for line in lines:
        pipe_map.append([x for x in line.strip()])
        visit_map.append([0 for _ in range(len(line.strip()))])


def print_matrix(matrix):
    print('-----------------------------------------------------------')
    # for x in range(len(matrix)):
    #     print(matrix[x])

    for row_label, row in enumerate(matrix):
        print('%s [%s]' % (row_label, ' '.join('%05s' % i for i in row)))
    print('-----------------------------------------------------------')


def is_valid(original_map, width, height, visit_map, new_x, new_y, direction):
    if new_x >= width or new_x < 0:
        return False
    if new_y >= height or new_y < 0:
        return False

    if direction == 0:
        # down
        prev_x = new_x - 1
        prev_y = new_y
        if original_map[new_x][new_y] == '.':
            return False
        elif 0 <= prev_x < width and 0 <= prev_y < height:
            # print(cur_x, cur_y, prev_x, prev_y)
            if original_map[prev_x][prev_y] in ['|', 'F', '7', 'S'] and original_map[new_x][new_y] in ['L', 'J', '|']:
                if visit_map[new_x][new_y] == 0:
                    return True
    elif direction == 1:
        # up
        prev_x = new_x + 1
        prev_y = new_y
        if original_map[new_x][new_y] == '.':
            return False
        elif 0 <= prev_x < width and 0 <= prev_y < height:
            if original_map[prev_x][prev_y] in ['|', 'L', 'J', 'S'] and original_map[new_x][new_y] in ['F', '7', '|']:
                if visit_map[new_x][new_y] == 0:
                    return True
    elif direction == 2:
        # right
        prev_x = new_x
        prev_y = new_y - 1
        if original_map[new_x][new_y] == '.':
            return False
        elif 0 <= prev_x < width and 0 <= prev_y < height:
            if original_map[prev_x][prev_y] in ['-', 'L', 'F', 'S'] and original_map[new_x][new_y] in ['J', '7', '-']:
                if visit_map[new_x][new_y] == 0:
                    return True
    elif direction == 3:
        # left
        prev_x = new_x
        prev_y = new_y + 1
        if original_map[new_x][new_y] == '.':
            return False
        elif 0 <= prev_x < width and 0 <= prev_y < height:
            if original_map[prev_x][prev_y] in ['J', '7', '-', 'S'] and original_map[new_x][new_y] in ['-', 'L', 'F']:
                if visit_map[new_x][new_y] == 0:
                    return True
    return False


def has_2_consecutive_neighboors(visit_matrix, x, y, width, height):
    cur_value = visit_matrix[x][y]
    neighboors = 0
    if x-1 >= 0:
        if visit_matrix[x - 1][y] == cur_value - 1:
            neighboors += 1
    if x+1 < width:
        if visit_matrix[x + 1][y] == cur_value - 1:
            neighboors += 1
    if y+1 < height:
        if visit_matrix[x][y + 1] == cur_value - 1:
            neighboors += 1
    if y-1 >= 0:
        if visit_matrix[x][y - 1] == cur_value - 1:
            neighboors += 1

    if neighboors >= 2:
        return True
    return False


def flood(original_map, width, height, visit_map, start_x, start_y, step):
    queue = []
    queue.append([start_x, start_y])
    visit_map[start_x][start_y] = step
    step += 1
    maximilian = 0
    maximilian_coords = []

    while queue:
        current_position = queue.pop(0)
        cur_x = current_position[0]
        cur_y = current_position[1]

        # print('------', cur_x, cur_y, step)
        next_x = cur_x + 1
        next_y = cur_y
        if is_valid(original_map, width, height, visit_map, next_x, next_y, direction=0):
            # print('\t', cur_x + 1, cur_y, step)
            visit_map[next_x][next_y] = visit_map[cur_x][cur_y] + 1
            queue.append([next_x, next_y])
            if has_2_consecutive_neighboors(visit_map, next_x, next_y, width, height):
                if visit_map[next_x][next_y] > maximilian:
                    maximilian = visit_map[next_x][next_y]
                    maximilian_coords = [next_x, next_y]

        next_x = cur_x - 1
        next_y = cur_y
        if is_valid(original_map, width, height, visit_map, next_x, next_y, direction=1):
            # print('\t', next_x, next_y, step)
            visit_map[next_x][next_y] = visit_map[cur_x][next_y] + 1
            queue.append([next_x, next_y])
            if has_2_consecutive_neighboors(visit_map, next_x, next_y, width, height):
                if visit_map[next_x][next_y] > maximilian:
                    maximilian = visit_map[next_x][next_y]
                    maximilian_coords = [next_x, next_y]

        next_x = cur_x
        next_y = cur_y + 1
        if is_valid(original_map, width, height, visit_map, next_x, next_y, direction=2):
            # print('\t', next_x, next_y, step)
            visit_map[next_x][next_y] = visit_map[next_x][cur_y] + 1
            queue.append([next_x, next_y])
            if has_2_consecutive_neighboors(visit_map, next_x, cur_y + 1, width, height):
                if visit_map[next_x][next_y] > maximilian:
                    maximilian = visit_map[next_x][next_y]
                    maximilian_coords = [next_x, next_y]

        next_x = cur_x
        next_y = cur_y - 1
        if is_valid(original_map, width, height, visit_map, next_x, next_y, direction=3):
            # print('\t', next_x, next_y, step)
            visit_map[next_x][next_y] = visit_map[next_x][cur_y] + 1
            queue.append([next_x, next_y])
            if has_2_consecutive_neighboors(visit_map, next_x, next_y, width, height):
                if visit_map[next_x][next_y] > maximilian:
                    maximilian = visit_map[next_x][next_y]
                    maximilian_coords = [next_x, next_y]

        # print('\t\t', queue)
        step += 1
        # print_matrix(visit_map)

    return maximilian, maximilian_coords


# print_matrix(pipe_map)
# print_matrix(visit_map)

width = len(pipe_map)
height = len(pipe_map[0])

for x in range(len(pipe_map)):
    for y in range(len(pipe_map[0])):
        if pipe_map[x][y] == 'S':
            # print(x, y)
            maximilian, maximilian_coords = flood(pipe_map, width, height, visit_map, x, y, 0)
            print(maximilian, maximilian_coords)

# maxx = 0
# for line in visit_map:
#     if max(line) > maxx:
#         maxx = max(line)
# print(maxx)

# inside = 0
# for x in range(len(visit_map)):
#     # intersects = 0
#     for y in range(len(visit_map[0])):
#         # if visit_map[x][y] == 0:
#         #     if intersects % 2 == 1:
#         #         inside += 1
#         #         visit_map[x][y] = 99999
#         # else:
#         #     intersects += 1
#         if visit_map[x][y] == 0:
#             intersections = 0
#             for j in range(y+1, len(visit_map[0])):
#                 if visit_map[x][j] != 0:
#                     intersections += 1
#                     # if j-1 > 0:
#                     #     if visit_map[x][j-1] == 0:
#                     #         intersections += 1
#                     # if j+1 < height:
#                     #     if visit_map[x][j + 1] == 0:
#                     #         intersections += 1
#             print(x, y, intersections)
#             if intersections % 2 == 1:
#                 inside += 1
#                 visit_map[x][y] = 99999
#
#
# print(inside)
# print_matrix(visit_map)
# #6773
