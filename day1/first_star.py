str_input = ''


lines = str_input.split('\n')

print(len(lines))

def find_first_and_last_number(line):
    digits = []
    map_string_to_int = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
        }
    for idx, x in enumerate(line):
        if x.isdigit():
            digits.append( [idx, int(x)] )
    
    for string_number in map_string_to_int.keys():
        res = [i for i in range(len(line)) if line.startswith(string_number, i)]
        for idx_pos in res:
            digits.append( [idx_pos, map_string_to_int[string_number]] )
            
    digits.sort(key=lambda final_numbers: final_numbers[0])
            
    return int(str(digits[0][1])+str(digits[-1][1]))
            
            

numbers = list(map(lambda x: find_first_and_last_number(x), lines))

print(numbers[-2])
print(sum(numbers))
