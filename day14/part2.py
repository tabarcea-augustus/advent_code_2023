def print_matrix(matrix, ):
    print('-----------------------------------------------------------')

    for row_label, row in enumerate(matrix):
        print('[%s]' % (' '.join('%03s' % i for i in row)))
    print('-----------------------------------------------------------')

def transpose(grid):
    return tuple("".join(row) for row in zip(*grid))


def spin_cycle(grid):
    grid = transpose(grid)
    tilted_grid = []
    for row in grid:
        tilted_grid.append(( "#".join( "".join(sorted(char, reverse=True)) for char in row.split('#')) ))
    grid = tuple(tilted_grid)

    grid = transpose(grid)
    tilted_grid = []
    for row in grid:
        tilted_grid.append(( "#".join( "".join(sorted(char, reverse=True)) for char in row.split('#')) ))
    grid = tuple(tilted_grid)

    grid = transpose(grid)
    tilted_grid = []
    for row in grid:
        tilted_grid.append(( "#".join( "".join(sorted(char, reverse=False)) for char in row.split('#')) ))
    grid = tuple(tilted_grid)

    grid = transpose(grid)
    tilted_grid = []
    for row in grid:
        tilted_grid.append(( "#".join( "".join(sorted(char, reverse=False)) for char in row.split('#')) ))
    grid = tuple(tilted_grid)

    return grid

file_name = 'input.txt'

with open(file_name, 'r') as fd:
    grid = fd.readlines()
    grid = tuple(map(lambda line: [x for x in line.strip()], grid))


cache = {}
idx = 1
while 1:
    grid = spin_cycle(grid)
    # print(grid)
    if grid in cache:
        period_length = idx - cache[grid]
        final_spin = (1_000_000_000 - cache[grid]) % period_length + cache[grid]
        print(final_spin)
        for k, v in cache.items():
            if v == final_spin:
                final_matrix = transpose(k)
        break
    cache[grid] = idx
    idx += 1

s = 0
# print_matrix(final_matrix)
for row in final_matrix:
    for idx, char in enumerate(row):
        if char == 'O':
            s += len(row) - idx

print(s)

def calculate_load(matrix: tuple[str, ...]) -> int:
    return sum(
        sum(len(row) - i for i, char in enumerate(row) if char == 'O')
        for row in matrix
    )

print(calculate_load(final_matrix))

#88371
