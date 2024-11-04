from collections import deque # to be used as a deck

decks = [] # not deques!
for _ in range(2):
    input()
    deck = deque() # lol

    line = input()
    try:
        while line:
            deck.append(int(line))
            line = input()
    except EOFError:
        pass
    finally:
        decks.append(deck) # which is a deque

first_player_deck, second_player_deck = decks
while first_player_deck and second_player_deck:
    first_player_card = first_player_deck.popleft()
    second_player_card = second_player_deck.popleft()

    first_player_won = first_player_card > second_player_card
    winning_player_deck = (
        first_player_deck
        if first_player_won
        else second_player_deck
    )
    winning_player_deck.append(
        first_player_card
        if first_player_won
        else second_player_card
    )
    winning_player_deck.append(
        second_player_card
        if first_player_won
        else first_player_card
    )

print(
    sum(
        card * (i + 1)
        for i, card in enumerate(reversed(winning_player_deck))
    )
)

# ...dequestrous
