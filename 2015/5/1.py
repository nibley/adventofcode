passwords = []
while True:
    try:
        line = input()
    except EOFError:
        break

    passwords.append(line)

print(
    sum(
        # vowel count
        sum(letter in 'aeiou' for letter in password) >= 3
        # at least one double
        and any(
            first_letter == second_letter
            for first_letter, second_letter in zip(
                password[    : -1 ],
                password[  1 :    ]
            )
        )
        # no forbidden pairs
        and not any(
            forbidden in password
            for forbidden in {'ab', 'cd', 'pq', 'xy'}
        )
        for password in passwords
    )
)
