cards = []
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
    cards.append(my_numbers.intersection(winning_numbers))

print(
    sum(
        2 ** ( len(matching_numbers) - 1 )
        for matching_numbers in cards
        if matching_numbers
    )
)
