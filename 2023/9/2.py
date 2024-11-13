rows = []
while True:
    try:
        line = input()
    except EOFError:
        break

    rows.append([ int(piece) for piece in line.split(' ') ])

total = 0
for row in rows:
    first_deltas = []
    sequence = row
    while True:
        first_deltas.append(sequence[0])
        sequence = [ sequence[i + 1] - n for i, n in enumerate(sequence[:-1]) ]

        if not any(sequence):
            break

    extrapolated = 0
    for first_delta in reversed(first_deltas):
        extrapolated = first_delta - extrapolated

    total += extrapolated

print(total)
