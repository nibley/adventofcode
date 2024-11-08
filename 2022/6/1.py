stream = input()

for i, first_char in enumerate(stream[ : -3 ]):
    second_char = stream[ i + 1 ]
    third_char = stream[ i + 2 ]
    fourth_char = stream[ i + 3 ]

    unique_chars = set((
        first_char,
        second_char,
        third_char,
        fourth_char
    ))

    if len(unique_chars) == 4:
        print(i + 4)
        break
