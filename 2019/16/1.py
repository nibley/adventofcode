def repeating_pattern(i):
    while True:
        for digit in (0, 1, 0, -1):
            for _ in range(i + 1):
                yield digit

def simulate_step(sequence):
    for i in range(len(sequence)):
        new_digit_sum = 0
        coefficients = repeating_pattern(i)
        next(coefficients) # skip first

        for input_digit, coefficient in zip(sequence, coefficients):
            if coefficient:
                new_digit_sum += input_digit * coefficient

        yield abs(new_digit_sum) % 10

sequence = [ int(n) for n in input() ]
for _ in range(100):
    sequence = list(simulate_step(sequence))

print(''.join(str(n) for n in sequence[:8]))
