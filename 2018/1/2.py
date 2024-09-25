deltas = []
while True:
    try:
        line = input()
    except EOFError:
        break

    delta = int(line)
    deltas.append(delta)

frequency = 0
frequencies = set()
found_duplicate = False
while not found_duplicate:
    for delta in deltas:
        frequency += delta
        if frequency in frequencies:
            found_duplicate = True
            break
        frequencies.add(frequency)

print(frequency)
