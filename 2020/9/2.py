from itertools import combinations

sequence = []
while True:
    try:
        line = input()
    except EOFError:
        break

    sequence.append(int(line))

ROLLING_BUFFER_SIZE = 25
rolling_buffer = sequence[ : ROLLING_BUFFER_SIZE]

non_sum_number = None
for number in sequence[ ROLLING_BUFFER_SIZE : ]:
    pairs = combinations(rolling_buffer, 2)
    found_pair = False
    for a, b in pairs:
        if a + b == number:
            found_pair = True
            break

    if not found_pair:
        non_sum_number = number
        break

    rolling_buffer = rolling_buffer[ 1 : ] + [number]

subsequence = None
for start_index in range(len(sequence)):
    total = sequence[start_index]
    end_index = start_index + 1
    while end_index < len(sequence):
        total += sequence[end_index]
        end_index += 1

        if total == non_sum_number:
            subsequence = sorted(sequence[start_index : end_index + 1])
            break

print(subsequence[0] + subsequence[-1])
