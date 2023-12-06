

with open('input.txt', 'r') as fd:
    input_str = fd.read()

parts = input_str.split('\n\n')
seeds, *others = parts
seeds = [int(x) for x in seeds.split(':')[1].split()]

for idx in range(len(others)):
    others[idx] = others[idx].split('\n')[1:]
    others[idx] = list(map(lambda x: x.split(' '), others[idx]))
    others[idx] = list(map(lambda x: (int(x[0]), int(x[1]), int(x[2])), others[idx]))

print(seeds, others)
mappings_values = []
for seed in seeds:
    current_mapping_value = seed
    for curent_map in others:
        found = 0
        for interval in curent_map:
            dest = interval[0]
            src = interval[1]
            offset = interval[2]
            if src <= current_mapping_value < src + offset:
                current_mapping_value = dest + (current_mapping_value-src)
                found = 1
                break

        if not found:
            current_mapping_value = current_mapping_value
    mappings_values.append(current_mapping_value)
    # print(seed, current_mapping_value)

print(min(mappings_values))
