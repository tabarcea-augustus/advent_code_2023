file_name = 'test_input.txt'
file_name = 'input.txt'

from collections import defaultdict

with open(file_name, 'r') as fd:
    lines = fd.readlines()

bricks = []
for line in lines:
    p1, p2 = line.split('~')
    p1 = [int(x) for x in p1.split(',')]
    p2 = [int(x) for x in p2.split(',')]

    bricks.append((p1, p2))

bricks.sort(key=lambda x: x[0][2])
# print(bricks)

tower = defaultdict(lambda: defaultdict(lambda: '#'))
snapshot_z_to_brick_idx = defaultdict(list)

for brick_idx, brick in enumerate(bricks):
    snapshot_z = brick[0][2]
    snapshot_z_to_brick_idx[snapshot_z].append(brick_idx)

min_snapshot_z, max_snapshot_z = min(list(snapshot_z_to_brick_idx.keys())), max(list(snapshot_z_to_brick_idx.keys()))

graph = [[] for i in range(len(bricks))]
under = defaultdict(list)

for brick_idx, brick in enumerate(bricks, start=0):
    brick_first_point_z = brick[0][2]
    brick_second_point_z = brick[1][2]

    current_level = brick_first_point_z

    brick_first_point_x = brick[0][0]
    brick_second_point_x = brick[1][0]

    brick_first_point_y = brick[0][1]
    brick_second_point_y = brick[1][1]

    # print('@@@', current_level)
    while current_level > 1:
        bellow_level_is_clear = True
        for x in range(brick_first_point_x, brick_second_point_x + 1):
            for y in range(brick_first_point_y, brick_second_point_y + 1):
                if tower[current_level - 1][(x, y)] != '#':
                    bellow_level_is_clear = False
                    break

        if bellow_level_is_clear:
            current_level -= 1
        else:
            break

    # print(current_level)

    # print(set(tower[current_level-1].values()))

    # bricks_ids_bellow = []
    # for z_bellow in range(current_level-1, current_level):
    #     bricks_ids_bellow.extend(list(tower[z_bellow].values()))
    #
    # bricks_ids_bellow = [x for x in set(bricks_ids_bellow) if x != '#']

    bricks_ids_bellow = set()
    for x in range(brick_first_point_x, brick_second_point_x + 1):
        for y in range(brick_first_point_y, brick_second_point_y + 1):
            if tower[current_level-1][(x, y)] != '#':
                bricks_ids_bellow.add(tower[current_level-1][(x, y)])

    # bricks_ids_bellow = set(
    #     [
    #         x
    #         for x in [tower[current_level - 1][pt] for pt in cube.get_xy_points()]
    #         if x != "."
    #     ]
    # )

    for brick_id_bellow in bricks_ids_bellow:
        graph[brick_id_bellow].append(brick_idx)
        under[brick_idx].append(brick_id_bellow)

    # print(current_level)
    # print()
    for x in range(brick_first_point_x, brick_second_point_x + 1):
        for y in range(brick_first_point_y, brick_second_point_y + 1):
            z_diff = abs(brick_first_point_z - brick_second_point_z)
            for z in range(z_diff + 1):
                # print((x,y), current_level, z)
                tower[current_level + z][(x, y)] = brick_idx

# print(graph)
# print(under)
# print()

required = set()
for k, brick_under in under.items():
    # print(brick_under)
    if len(brick_under) == 1:
        # print(brick_under)
        required.add(brick_under[0])

# print(len(required))
print('part1: ', len(bricks) - len(required))

def topological_sort(graph, node_start):
    in_degree = [0 for __ in range(len(graph))]
    for node in range(len(graph)):
        for children in graph[node]:
            in_degree[children] += 1

    # degrees 'with indegree 0'
    q = [node_start]
    count = -1

    while len(q) > 0:
        count += 1
        node = q.pop()
        for children in graph[node]:
            in_degree[children] -= 1
            if in_degree[children] == 0:
                q.append(children)

    return count

s = 0
for idx, brick in enumerate(bricks):
    s += topological_sort(graph, idx)

print('p2:', s)