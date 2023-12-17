file_name = 'test_input.txt'
file_name = 'input.txt'

with open(file_name, 'r') as fd:
    lines = fd.read()
    print(lines)
    grids = lines.split('\n\n')
    grids = list(map(lambda x: x.split('\n'), grids))

# print(int('000111', 2)[::-1])


s = 0
for grid in grids:
    # Rows
    mirrors_between_rows = 0
    rows_number_representation = list(map(lambda x: int(x.replace('.', '0').replace('#', '1'), 2), grid))

    for idx in range(1, len(rows_number_representation)):
        up = rows_number_representation[:idx]
        down = rows_number_representation[idx:]

        min_length = min(len(up), len(down))
        up = up[::-1][:min_length]
        down = down[:min_length]

        if up == down:
            mirrors_between_rows += idx
            # print(up, down)

    # Columns
    aux_grid = list(zip(*grid))
    aux_grid = list(map(lambda x: ''.join(x), aux_grid))
    print(grid, aux_grid)
    mirrors_between_columns = 0
    columns_number_representation = list(map(lambda x: int(x.replace('.', '0').replace('#', '1'), 2), aux_grid))

    for idx in range(1, len(columns_number_representation)):
        left = columns_number_representation[:idx]
        right = columns_number_representation[idx:]

        min_length = min(len(left), len(right))
        left = left[::-1][:min_length]
        right = right[:min_length]

        if left == right:
            mirrors_between_columns += idx
            # print(left, right)

    print(mirrors_between_rows, mirrors_between_columns)

    s += mirrors_between_rows * 100 + mirrors_between_columns

print(s)
