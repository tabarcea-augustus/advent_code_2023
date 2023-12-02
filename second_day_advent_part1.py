MAX_REDS = 12
MAX_GREEN = 13
MAX_BLUES = 14

with open('puzzle2_input.txt', 'r') as fd:
    puzzle_input_lines = fd.readlines()

puzzle_input_lines_num = len(puzzle_input_lines)
print('Lines num: ', puzzle_input_lines_num)
print('Max sum: ', (puzzle_input_lines_num * (puzzle_input_lines_num+1))/2 )
suma = 0

for game in puzzle_input_lines:
    ok = True
    print(game)
    game_number = game.split(':')[0].split('Game ')[1]
    game_inputs = game.split(': ')[1].split('; ')
    print(game_inputs)
    for game_input in game_inputs:
        for game_subset in game_input.split(', '):
            if 'red' in game_subset:
                cube_numbers = game_subset.replace(' red', '')
                if int(cube_numbers) > MAX_REDS:
                    ok = False
                    break
                    
            if 'blue' in game_subset:
                cube_numbers = game_subset.replace(' blue', '')
                if int(cube_numbers) > MAX_BLUES:
                    ok = False
                    break
                    
            if 'green' in game_subset:
                cube_numbers = game_subset.replace(' green', '')
                if int(cube_numbers) > MAX_GREEN:
                    ok = False
                    break
                    
    
    if ok:
        suma += int(game_number)

print(suma)
