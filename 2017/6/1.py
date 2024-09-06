raw = input()
banks = list(int(piece) for piece in raw.split('\t'))
num_banks = len(banks)
states = set()

cycles_completed = 0
while True:
    current_state = tuple(banks)
    if current_state in states:
        break
    states.add(current_state)

    fullest_bank, fullest_contents = sorted(enumerate(banks), \
        key=lambda item: (item[1], -1 * item[0])
    )[-1]
    banks[fullest_bank] = 0
    share_per_bank = fullest_contents // num_banks
    for i in range(num_banks):
        banks[i] += share_per_bank

    remainder = fullest_contents % num_banks
    remainder_recipients = [(fullest_bank + i) % num_banks \
        for i in range(1, remainder + 1)
    ]
    for i in remainder_recipients:
        banks[i] += 1

    cycles_completed += 1

print(cycles_completed)
