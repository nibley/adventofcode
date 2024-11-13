rows = []
while True:
    try:
        line = input()
    except EOFError:
        break

    rows.append([ int(piece) for piece in line.split(' ') ])

total = 0
for row in rows:
    final_deltas = []
    sequence = row
    while True:
        final_deltas.append(sequence[-1])
        sequence = [ sequence[i + 1] - n for i, n in enumerate(sequence[:-1]) ]

        if not any(sequence):
            break

    extrapolated = 0
    for final_delta in reversed(final_deltas):
        extrapolated += final_delta

    total += extrapolated

print(total)
