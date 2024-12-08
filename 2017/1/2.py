from itertools import cycle, islice

digits = tuple(map(int, input()))
assert not len(digits) % 2

print(
    sum(
        first_digit
        for first_digit, second_digit in zip(
            digits,
            islice(
                cycle(digits),
                len(digits) // 2,
                None # no stop value
            )
        )
        if first_digit == second_digit
    )
)
