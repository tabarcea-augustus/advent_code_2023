with open('input.txt', 'r') as fd:
    input_str = fd.read()

parts = input_str.split('\n\n')
seeds, *others = parts
seeds = [int(x) for x in seeds.split(':')[1].split()]

for idx in range(len(others)):
    others[idx] = others[idx].split('\n')[1:]
    others[idx] = list(map(lambda x: x.split(' '), others[idx]))
    others[idx] = list(map(lambda x: (int(x[0]), int(x[1]), int(x[2])), others[idx]))


def interval_intersect(x1, x2, y1, y2):
    if y1 > x2 or x1 > y2:
        return None
    else:
        return [max(x1, y1), min(x2, y2)]


seed_ranges = []
for seed_idx in range(0, len(seeds), 2):
    seed_range_start = seeds[seed_idx]
    seed_range_end = seed_range_start + seeds[seed_idx + 1] - 1

    seed_ranges.append([seed_range_start, seed_range_end])
print(seed_ranges)
print()

current_ranges = seed_ranges
for otr in others:
    print('\n\n')
    aux_current_ranges = []
    for range in current_ranges:
        found = 0
        for interval in otr:
            print(interval, range)
            aux_intersect = interval_intersect(range[0], range[1], interval[1], interval[1] + interval[2])
            print(aux_intersect)
            if aux_intersect:
                aux_current_ranges.append([
                    interval[0] + (aux_intersect[0] - interval[1]), interval[0] + (aux_intersect[1] - interval[1])
                ])
                if aux_intersect[0] > range[0]:
                    aux_current_ranges.append([
                        range[0], aux_intersect[0] - range[0]
                    ])
                found += 1
        if not found:
            aux_current_ranges.append(range)
        # if found >1:
        #     print('@@@@@@@@@@@@@',found)

    current_ranges = aux_current_ranges
    print(current_ranges)

print()
print(current_ranges)

print(min(list(map(lambda x: x[0], current_ranges))))

