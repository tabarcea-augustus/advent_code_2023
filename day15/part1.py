from functools import reduce

# file_name = 'test_input.txt'
file_name = 'input.txt'

with open(file_name, 'r') as fd:
    content = fd.read().split(',')

def hashish(old_hasish, string_input):
    return ((old_hasish + ord(string_input)) * 17) % 256

content = [reduce(hashish, list(current_string_particle), 0) for current_string_particle in content]
print(sum(content))