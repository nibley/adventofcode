def get_hand_type(cards):
    unique_cards = set(cards)
    card_amounts = sorted([ cards.count(card) for card in unique_cards ])

    if card_amounts[-1] == 5:
        return 6 # five of a kind
    elif card_amounts[-1] == 4:
        return 5 # four of a kind
    elif card_amounts[ -2 : ] == [2, 3]:
        return 4 # full house
    elif card_amounts[-1] == 3:
        return 3 # three of a kind
    elif card_amounts[ -2 : ] == [2, 2]:
        return 2 # two pair
    elif card_amounts[-1] == 2:
        return 1 # one pair
    else:
        return 0 # high card

hands = []
while True:
    try:
        line = input()
    except EOFError:
        break

    cards, bid = line.split(' ')
    bid = int(bid)

    hands.append( (cards, get_hand_type(cards), bid) )

def compare_hands(hand):
    cards, hand_type, _ = hand
    card_precedences = [ '23456789TJQKA'.index(card) for card in cards ]

    return tuple([hand_type] + card_precedences)

sorted_hands = sorted(hands, key=compare_hands)
total = sum( (i + 1) * hand[2] for i, hand in enumerate(sorted_hands) )
print(total)
