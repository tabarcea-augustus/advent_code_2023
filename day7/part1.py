symbol_to_int = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}

with open('input.txt', 'r') as fd:
    lines = fd.readlines()
    cards = list(map(lambda x: [x.split(' ')[0], x.split(' ')[1].strip(), 0], lines))


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

    card[2] = compute_base_13_number(card_hand, symbol_to_int)
    # card[3] = get_hand_type(card_hand)

    # we can add the card type to the next power of 13 since we got only 5 powers used (5^0..5^4); and the types of hands are bellow 13
    card[2] += (13**5) * get_hand_type(card_hand)

cards = sorted(cards, key=lambda x: x[2])
# print(cards)

total = 0
for idx, card in enumerate(cards, start=1):
    bet = card[1]
    total += idx * int(bet)

    # print(idx, bet)
print(total)

