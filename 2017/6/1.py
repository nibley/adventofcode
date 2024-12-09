banks = [ int(piece) for piece in input().split() ]
NUM_BANKS = len(banks)

states_visited = set()
cycles_completed = 0
current_state = tuple(banks)
while current_state not in states_visited:
    states_visited.add(current_state)

    fullest_index = max(
        range(NUM_BANKS),
        key=banks.__getitem__
    )
    share_per_bank, remainder = divmod(banks[fullest_index], NUM_BANKS)

    banks[fullest_index] = 0
    banks = [
        item + share_per_bank
        for item in banks
    ]
    for i in range(remainder):
        banks[ (fullest_index + i + 1) % NUM_BANKS ] += 1

    cycles_completed += 1
    current_state = tuple(banks)

print(cycles_completed)
