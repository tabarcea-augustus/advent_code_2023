file_name = 'test_input.txt'
file_name = 'input.txt'

def is_power_of_two(n):
    return (n & (n-1) == 0) and n != 0

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

        powers_of_2_differences = []
        print()
        for idx2 in range(len(up)):
            aux_row_representation1 = up[idx2]
            aux_row_representation2 = down[idx2]
            if aux_row_representation1 != aux_row_representation2:
                powers_of_2_differences.append(aux_row_representation1 ^ aux_row_representation2)

        # the 2 rows differ by exactly 1 cell, and the difference is a power of 2
        if len(powers_of_2_differences) == 1 and is_power_of_two(powers_of_2_differences[0]):
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

        powers_of_2_differences = []
        for idx2 in range(len(left)):
            aux_column_representation1 = left[idx2]
            aux_column_representation2 = right[idx2]
            if aux_column_representation1 != aux_column_representation2:
                powers_of_2_differences.append(aux_column_representation1 ^ aux_column_representation2)

        # the 2 rows differ by exactly 1 cell, and the difference is a power of 2
        if len(powers_of_2_differences) == 1 and is_power_of_two(powers_of_2_differences[0]):
            mirrors_between_columns += idx
            # print(up, down)

    print(mirrors_between_rows, mirrors_between_columns)

    s += mirrors_between_rows * 100 + mirrors_between_columns

print(s)

#27587