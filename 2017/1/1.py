from itertools import cycle, islice, pairwise

digits_raw = input()

print(
    sum(
        first_digit
        for first_digit, second_digit in pairwise(
            islice(
                cycle(map(int, digits_raw)),
                len(digits_raw) + 1
            )
        )
        if first_digit == second_digit
    )
)
