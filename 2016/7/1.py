addresses = []
while True:
    try:
        line = input()
    except EOFError:
        break

    sections = []
    sections_bracketed = []
    for piece in line.split('['):
        subpieces = piece.split(']')

        if len(subpieces) == 1:
            normal, *_ = subpieces
            sections.append(normal)
        else:
            bracketed, normal = subpieces
            sections_bracketed.append(bracketed)
            sections.append(normal)

    addresses.append( (sections, sections_bracketed) )

def has_abba(section):
    return any(
        first_letter != second_letter
        and (first_letter, second_letter) == (fourth_letter, third_letter)
        for (
            first_letter, second_letter, third_letter, fourth_letter
        ) in zip(
            section[    : -3 ],
            section[  1 : -2 ],
            section[  2 : -1 ],
            section[  3 :    ]
        )
    )

def is_valid(address):
    sections, sections_bracketed = address
    return (
        not any(map(has_abba, sections_bracketed))
        and any(map(has_abba, sections))
    )

print(
    sum(
        is_valid(address)
        for address in addresses
    )
)
