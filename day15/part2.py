from functools import reduce

# file_name = 'test_input.txt'
file_name = 'input.txt'

with open(file_name, 'r') as fd:
    content = fd.read().split(',')

def hashish(old_hasish, string_input):
    return ((old_hasish + ord(string_input)) * 17) % 256

dict = {}
for current_string_particle in content:
    # print(current_string_particle, dict)
    if '=' in current_string_particle:
        split_before, split_after = current_string_particle.split('=')[0], current_string_particle.split('=')[1]
        hash_val = reduce(hashish, split_before, 0)
        if hash_val in dict:
            dict[hash_val][split_before] = split_after
        else:
            dict[hash_val] = {}
            dict[hash_val][split_before] = split_after
    elif '-' in current_string_particle:
        hash_val = reduce(hashish, current_string_particle[:-1], 0)
        # print(hash_val)
        if hash_val in dict:
            # print(hash_val)
            if current_string_particle[:-1] in dict[hash_val]:
                # print(dict[hash_val][current_string_particle[:-1]])
                del dict[hash_val][current_string_particle[:-1]]

s = 0
# print(dict)
for k,v in dict.items():
    if v:
        for idx, k2 in enumerate(dict[k]):
            s += (k+1) * (idx+1) * int(dict[k][k2])

print(s)