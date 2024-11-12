from collections import Counter

matches = []
while True:
    try:
        line = input()
    except EOFError:
        break

    winning_numbers, my_numbers = (
        set( int(number) for number in piece.split(' ') if number )
        for piece in line.split(':')[1].split(' | ')
    )

    matching_numbers = my_numbers.intersection(winning_numbers)
    matches.append(len(matching_numbers))

total_cards = Counter({
    i : 1
    for i, _ in enumerate(matches)
})
cards_to_scan = total_cards.copy()
while cards_to_scan:
    new_cards_found = Counter()
    for card_number, copies in cards_to_scan.items():
        for i in range(matches[card_number]):
            new_cards_found[card_number + i + 1] += copies

    total_cards.update(new_cards_found)
    cards_to_scan = new_cards_found

print(total_cards.total())
