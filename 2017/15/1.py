from itertools import islice

DIVISOR = 2147483647
GENERATOR_A_MULTIPLIER = 16807
GENERATOR_B_MULTIPLIER = 48271
BITMASK = 2 ** 16 - 1

def generator(initial, multiplier):
    value = initial
    while True:
        value = (value * multiplier) % DIVISOR
        yield value & BITMASK

generator_a_initial, generator_b_initial = (
    int(input().split()[-1]) for _ in range(2)
)
generator_a = generator(generator_a_initial, GENERATOR_A_MULTIPLIER)
generator_b = generator(generator_b_initial, GENERATOR_B_MULTIPLIER)

print(
    sum(
        generator_a_value == generator_b_value
        for generator_a_value, generator_b_value in islice(
            zip(generator_a, generator_b),
            40_000_000
        )
    )
)
