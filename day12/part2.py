from functools import cache

# file_name = 'test_input.txt'
file_name = 'input.txt'

with open(file_name, 'r') as fd:
    lines = fd.readlines()
    lines = list(
        map(lambda line: (line.split(' ')[0].strip(), tuple(map(int, line.split(' ')[1].strip().split(',')))), lines))
    springs = list(map(lambda x: x[0], lines))
    groups = list(map(lambda x: x[1], lines))

print(springs, groups)


@cache
def count_solutions(springs_string, spring_counts, springs_checked_inside_current_group):
    # print(springs_string)
    if not springs_string:
        # finished the current branch of string
        # print(spring_counts, springs_checked_inside_current_group)
        if len(spring_counts) == 0 and springs_checked_inside_current_group == 0:
            # no more groups and we arrived with all the strings in group matched. final char is '.', artificially added
            return 1
        return 0

    total_solutions = 0

    if springs_string[0] == '?':
        variant = '#'
        total_solutions += count_solutions(springs_string[1:], spring_counts, springs_checked_inside_current_group + 1)

        variant = '.'
        # print(springs_checked_inside_current_group, spring_counts[0], spring_counts)
        if springs_checked_inside_current_group != 0:
            # we are inside a group
            if len(spring_counts) != 0 and spring_counts[0] == springs_checked_inside_current_group:
                # finished current group
                total_solutions += count_solutions(springs_string[1:], spring_counts[1:], 0)
        else:
            # we are not in a group, skip
            total_solutions += count_solutions(springs_string[1:], spring_counts, 0)
    else:
        # the spring can be damaged or not
        if springs_string[0] == '#':
            # the spring is damaged, continue with one more to the group
            total_solutions += count_solutions(springs_string[1:], spring_counts,
                                               springs_checked_inside_current_group + 1)
        else:
            # the spring is not damaged
            if springs_checked_inside_current_group != 0:
                # we are inside a group
                if len(spring_counts) != 0 and spring_counts[0] == springs_checked_inside_current_group:
                    # finished current group
                    total_solutions += count_solutions(springs_string[1:], spring_counts[1:], 0)
                # else group not finished, but the spring is not damaged
            else:
                # we are not in a group, skip
                total_solutions += count_solutions(springs_string[1:], spring_counts, 0)

    return total_solutions


suma = 0

for idx in range(len(springs)):
    spring = springs[idx]
    group = groups[idx]
    spring = "?".join([spring] * 5)
    group = group * 5
    print(spring, group)
    aux_suma = count_solutions(spring + '.', group, 0)
    suma += aux_suma
    print(aux_suma)

print(suma)




