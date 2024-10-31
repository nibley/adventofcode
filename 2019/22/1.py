operations = []
while True:
    try:
        line = input()
    except EOFError:
        break

    if line == 'deal into new stack':
        operation = 'new'
        n = None
    else:
        words = line.split(' ')

        operation = words[0]
        n = int(words[-1])

    operations.append( (operation, n) )

deck = list(range(10_007))

for operation, n in operations:
    if operation == 'new':
        deck.reverse()
    elif operation == 'cut': # re: cut for negative n, lol python moment
        deck = deck[ n : ] + deck[ : n ]
    elif operation == 'deal':
        new_deck = [None] * len(deck)

        for i, card in enumerate(deck):
            new_deck[ (n * i) % len(deck) ] = card

        deck = new_deck

print(deck.index(2019))
