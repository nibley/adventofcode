from itertools import combinations

passwords = []
while True:
    try:
        line = input()
    except EOFError:
        break

    passwords.append(line)

print(
    sum(
        # at least one double pair
        any(
            first_pair == second_pair and abs(i - j) > 1
            for (i, first_pair), (j, second_pair) in combinations(
                enumerate(
                    zip(
                        password[    : -1 ],
                        password[  1 :    ]
                    )
                ),
                2
            )
        )
        # repeat with gap
        and any(
            first_letter == third_letter
            for first_letter, _, third_letter in zip(
                password[    : -2 ],
                password[  1 : -1 ],
                password[  2 :    ]
            )
        )
        for password in passwords
    )
)
