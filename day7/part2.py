import copy
import operator

symbol_to_int = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}

with open('input.txt', 'r') as fd:
    lines = fd.readlines()
    cards = list(map(lambda x: [x.split(' ')[0], x.split(' ')[1].strip(), 0, 0, 0], lines))


def compute_base_13_number(card_hand, symbol_to_int):
    base_representation = 0
    len_card_hand = len(card_hand)
    for symbol_idx in range(1, len(card_hand)+1):
        # print(len_card_hand-symbol_idx)
        symbol_int = symbol_to_int[card_hand[symbol_idx-1]]
        base_representation += (13**(len_card_hand-symbol_idx)) * symbol_int

    return base_representation


def get_hand_type(card_hand):
    counts = {}
    for symbol in card_hand:
        if symbol in counts:
            counts[symbol] += 1
        else:
            counts[symbol] = 1

    if 'J' in counts:
        j_counts = counts['J']
        aux_counts = copy.deepcopy(counts)
        del aux_counts['J']
        count_values = list(aux_counts.values())
        max_count = 0
        if count_values:
            max_count = max(count_values)

        second_max_count = 0
        if len(count_values) >= 2:
            second_max_count = sorted(count_values)[-2]

        if j_counts == 5 or (j_counts + max_count) == 5:
            return 6
        elif (j_counts + max_count) == 4 or j_counts == 4:
            return 5
        elif ( (second_max_count + j_counts) == 2 and max_count == 3) or ( (second_max_count + j_counts) == 3 and max_count == 2):
            return 4
        elif 2 in count_values or j_counts == 3 or (1 in count_values and j_counts == 2):
            return 3
        else:
            return 1
        # key_max = max(counts.items(), key=operator.itemgetter(1))[0]
        # if key_max != 'J':
        #     counts[key_max] += counts['J']
        #     del counts['J']


    pairs = list(sorted(counts.values()))
    if pairs == [5]:
        return 6
    elif pairs == [1, 4]:
        return 5
    elif pairs == [2, 3]:
        return 4
    elif pairs == [1, 1, 3]:
        return 3
    elif pairs == [1, 2, 2]:
        return 2
    elif pairs == [1, 1, 1, 2]:
        return 1
    else:
        return 0




for idx in range(len(cards)):
    card = cards[idx]
    card_hand = card[0]
    card_bet = card[1]

    base_13_nmbr = compute_base_13_number(card_hand, symbol_to_int)
    card[2] = base_13_nmbr
    # card[3] = get_hand_type(card_hand)

    # we can add the card type to the next power of 13 since we got only 5 powers used (5^0..5^4); and the types of hands are bellow 13
    hand_type = get_hand_type(card_hand)
    # print(card, hand_type)
    card[2] += (13**5) * hand_type
    card[3] = base_13_nmbr
    card[4] = hand_type

cards = sorted(cards, key=lambda x: x[2])
# print(cards)

total = 0
for idx, card in enumerate(cards, start=1):
    bet = card[1]
    total += idx * int(bet)

# rank = 1
# for idx, card in enumerate(cards):
#     print(rank, card[1], card[2])
#     bet = card[1]
#     if idx > 1 and cards[idx-1][2] != cards[idx][2]:
#         rank += 1
#         total += rank * int(bet)
#     elif idx > 1:
#         print('da')
#         total += rank * int(bet)

print(total)
