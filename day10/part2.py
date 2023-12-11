import copy
import math

with open('input.txt', 'r') as fd:
    lines = fd.readlines()
    pipe_map = []
    visit_map = []
    for line in lines:
        pipe_map.append([x for x in line.strip()])
        visit_map.append([0 for _ in range(len(line.strip()))])


def print_matrix(matrix):
    print('-----------------------------------------------------------')
    for row_label, row in enumerate(matrix):
        print('[%s]' % (' '.join('%05s' % i for i in row)))
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
    maximilian_coords = [start_x, start_y]

    while queue:
        current_position = queue.pop(0)
        cur_x = current_position[0]
        cur_y = current_position[1]
        if visit_map[cur_x][cur_y] == 71:
            a = 2
        if has_2_consecutive_neighboors(visit_map, cur_x, cur_y, width, height):
            if visit_map[cur_x][cur_y] > maximilian:
                maximilian = visit_map[cur_x][cur_y]
                maximilian_coords = [cur_x, cur_y]


        next_x = cur_x + 1
        next_y = cur_y
        if is_valid(original_map, width, height, visit_map, next_x, next_y, direction=0):
            if visit_map[next_x][next_y]==71:
                a = 2
            visit_map[next_x][next_y] = visit_map[cur_x][cur_y] + 1
            queue.append([next_x, next_y])


        next_x = cur_x - 1
        next_y = cur_y
        if is_valid(original_map, width, height, visit_map, next_x, next_y, direction=1):
            if visit_map[next_x][next_y] == 71:
                a = 2
            visit_map[next_x][next_y] = visit_map[cur_x][next_y] + 1
            queue.append([next_x, next_y])


        next_x = cur_x
        next_y = cur_y + 1
        if is_valid(original_map, width, height, visit_map, next_x, next_y, direction=2):
            if visit_map[next_x][next_y] == 71:
                a = 2
            visit_map[next_x][next_y] = visit_map[next_x][cur_y] + 1
            queue.append([next_x, next_y])


        next_x = cur_x
        next_y = cur_y - 1
        if is_valid(original_map, width, height, visit_map, next_x, next_y, direction=3):
            if visit_map[next_x][next_y] == 71:
                a = 2
            visit_map[next_x][next_y] = visit_map[next_x][cur_y] + 1
            queue.append([next_x, next_y])


        step += 1
        print(queue)
    # visit_map[start_x][start_y] = -1

    return maximilian, maximilian_coords

width = len(pipe_map)
height = len(pipe_map[0])

for x in range(len(pipe_map)):
    for y in range(len(pipe_map[0])):
        if pipe_map[x][y] == 'S':
            maximilian, maximilian_coords = flood(pipe_map, width, height, visit_map, x, y, 1)
            print(maximilian, maximilian_coords)

print_matrix(visit_map)

visit_map_copy = copy.deepcopy(visit_map)

def mark_circle(start_x, start_y, visit_map, visit_map_copy):
    def is_valid_reversed(visit_map, x, y, curent_value, width, height):
        if x < 0 or x >= width:
            return False
        if y < 0 or y >= height:
            return False
        if visit_map[x][y] + 1 == curent_value and visit_map[x][y] != 0:
            return True
        return False

    polygon_points = []

    # while not getting back to start
    queue = []
    queue.append([start_x, start_y])
    polygon_points.append((start_x, start_y))
    visit_map_copy[start_x][start_y] = -2

    while queue:
        current_point = queue.pop()
        current_x = current_point[0]
        current_y = current_point[1]
        if current_point == -1:
            break


        for pair in [
            [current_x + 1, current_y], [current_x - 1, current_y],
            [current_x, current_y + 1], [current_x, current_y - 1]
        ]:
            if is_valid_reversed(visit_map, pair[0], pair[1], visit_map[current_x][current_y], width, height):
                visit_map_copy[pair[0]][pair[1]] = -2
                queue.append([pair[0], pair[1]])
                polygon_points.append((pair[0], pair[1]))

    return polygon_points





polygon_points = mark_circle(maximilian_coords[0], maximilian_coords[1], visit_map, visit_map_copy)
polygon_points = list(set(polygon_points))
print_matrix(visit_map_copy)

# s = 0
# for line in visit_map_copy:
#     s += line.count(-2)
# print(s)
# print(len(set(polygon_points)))
# # print(polygon_points)


# def point_in_polygon(x, y, polygon):
#     """
#     Check if a point (x, y) is inside a polygon defined by a list of vertices.
#     """
#     num_vertices = len(polygon)
#     inside = False
#
#     # Start from the last vertex and iterate through each edge
#     j = num_vertices - 1
#     for i in range(num_vertices):
#         xi, yi = polygon[i]
#         xj, yj = polygon[j]
#
#         # Check if the ray intersects with the edge
#         intersect_condition = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
#
#         if intersect_condition:
#             inside = not inside
#
#         j = i
#
#     return inside
#
# def get_polar_angle(point, reference_point):
#     x, y = point
#     ref_x, ref_y = reference_point
#     return math.atan2(y - ref_y, x - ref_x)
#
# def sort_vertices_counterclockwise(vertices):
#     reference_point = min(vertices, key=lambda p: (p[1], p[0]))
#     return sorted(vertices, key=lambda p: get_polar_angle(p, reference_point))
#
# polygon_points = sort_vertices_counterclockwise(polygon_points)
#
#
# def is_point_inside_polygon(x, y, polygon):
#     n = len(polygon)
#     inside = False
#
#     p1x, p1y = polygon[0]
#     for i in range(n + 1):
#         p2x, p2y = polygon[i % n]
#         if y > min(p1y, p2y) and y <= max(p1y, p2y) and x <= max(p1x, p2x):
#             if p1y != p2y and (p2y - min(p1y, p2y)) != 0:
#                 print(p1y, p2y)
#                 print(p2y - min(p1y, p2y))
#                 if x <= min(p1x, p2x) + (y - min(p1y, p2y)) * (p2x - min(p1x, p2x)) / (p2y - min(p1y, p2y)):
#                     inside = not inside
#             elif p1y == p2y and y == p1y and x >= min(p1x, p2x) and x <= max(p1x, p2x):
#                 inside = not inside
#         p1x, p1y = p2x, p2y
#
#     return inside
#
# included_points = 0
# for idx1 in range(len(visit_map_copy)):
#     for idx2 in range(len(visit_map_copy[0])):
#         if is_point_inside_polygon(idx1, idx2, polygon_points):
#             if visit_map_copy[idx1][idx2] != -2:
#                 visit_map_copy[idx1][idx2] = -11
#                 included_points += 1


# # shooting a ray diagonally. failed aproach for this input.
# included_points = 0
# for idx1 in range(len(visit_map_copy)):
#     for idx2 in range(len(visit_map_copy[0])):
#         if visit_map_copy[idx1][idx2] == -2:
#             continue
#
#         crosses = 0
#         aux_x, aux_y = idx1, idx2
#         while aux_x < width and aux_y < height:
#             if visit_map_copy[aux_x][aux_y] == -2 and pipe_map[aux_x][aux_y] != 'L' and pipe_map[aux_x][aux_y] != '7':
#                 crosses += 1
#             aux_x += 1
#             aux_y += 1
#
#         if crosses % 2 == 1:
#             included_points += 1
#             visit_map_copy[idx1][idx2] = -111

# included_points = 0
# last = ''
# for idx1 in range(len(visit_map_copy)):
#     out = True
#     for idx2 in range(len(visit_map_copy[0])):
#         if visit_map_copy[idx1][idx2] == -2:
#             if pipe_map[idx1][idx2] == '-' and last + pipe_map[idx1][idx2] not in ['L7', 'FJ']:
#                 out = not out
#                 last = pipe_map[idx1][idx2]
#             else:
#                 if not out:
#                     included_points += 1
#                     visit_map_copy[idx1][idx2] = -111


included_points = 0
for idx1 in range(len(visit_map_copy)):
    for idx2 in range(len(visit_map_copy[0])):
        if visit_map_copy[idx1][idx2] == -2:
            continue
        crosses = 0
        x2, y2 = idx2, idx1

        while x2 < height and y2 < width:
            # print(y2, x2, width, height)
            c2 = pipe_map[y2][x2]
            if visit_map_copy[y2][x2] == -2 and c2 != "L" and c2 != "7":
                crosses += 1
            x2 += 1
            y2 += 1

        if crosses % 2 == 1:
            included_points += 1
            visit_map_copy[idx1][idx2] = '-111111'


print_matrix(visit_map_copy)
# print_matrix(pipe_map)
print(included_points)

# 493