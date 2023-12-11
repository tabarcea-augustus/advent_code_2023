# file_name = 'test_input.txt'
file_name = 'input.txt'

with open(file_name, 'r') as fd:
    lines = fd.readlines()

suma = 0
for line in lines:
    eq = [int(x) for x in line.split(' ')]
    all_diffs = [eq]

    while eq.count(0) != len(eq):
        aux_diffs = []
        for idx in range(len(eq)-1):
            aux_diffs.append(eq[idx+1] - eq[idx])
        eq = aux_diffs
        all_diffs.append(aux_diffs)

    number = all_diffs[-1][-1]
    for idx in reversed(range(len(all_diffs)-1)):
        number = number + all_diffs[idx][-1]
        # print(number)

    # print(line, all_diffs, number)
    suma += number

print(suma)
