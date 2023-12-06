from collections import Counter

str_card_input = '''
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''
str_card_input = str_card_input[1:-1]


def power(x, y):
    if y == 0:
        return 1
    tmp = power(x, int(y / 2))

    if y % 2 == 0:
        return tmp * tmp
    else:
        if y > 0:
            return x * tmp * tmp
        else:
            return (tmp * tmp) / x


suma = 0
for line in str_card_input.split('\n'):
    print(line)
    card_number = line.split(': ')[0].split('Card ')[1]
    line = line.split(': ')[1]

    wining_numbers = line.split(' | ')[0]
    numbers_you_have = line.split(' | ')[1]

    wining_numbers = wining_numbers.replace('  ', ' ').strip().split(' ')
    numbers_you_have = numbers_you_have.replace('  ', ' ').strip().split(' ')

    wining_numbers = set(map(lambda x: int(x), wining_numbers))
    numbers_you_have = set(map(lambda x: int(x), numbers_you_have))
    intersection_numbers = wining_numbers.intersection(numbers_you_have)
    # print(wining_numbers, numbers_you_have, intersection_numbers)
    two_power = len(intersection_numbers)
    if two_power > 1:
        two_power -= 1
    points = power(2, two_power)
    print(points, two_power)
    suma += points
    # numbers_you_have = Counter(list(map(lambda x: int(x), numbers_you_have)))
    # # print(card_number, wining_numbers, numbers_you_have)
    # for number in numbers_you_have:
    #     count = numbers_you_have[number]
    #     print(number, count)

print(suma)