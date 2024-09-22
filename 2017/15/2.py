divisor = 2147483647
bitmask = 2 ** 16 - 1
def generator(initial, multiplier, modulus):
    value = initial
    while True:
        value = (value * multiplier) % divisor
        if not value % modulus:
            yield value & bitmask

generator_a_initial = int(input().split(' ')[-1])
generator_a_multiplier = 16807
generator_a_modulus = 4
generator_a = generator(
    generator_a_initial,
    generator_a_multiplier,
    generator_a_modulus
)

generator_b_initial = int(input().split(' ')[-1])
generator_b_multiplier = 48271
generator_b_modulus = 8
generator_b = generator(
    generator_b_initial,
    generator_b_multiplier,
    generator_b_modulus
)

matches = 0
for _ in range(5_000_000):
    if next(generator_a) == next(generator_b):
        matches += 1

print(matches)
