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

def get_abas(sections):
    return tuple(
        (first_letter, second_letter, third_letter)
        for section in sections
        for first_letter, second_letter, third_letter in zip(
            section[    : -2 ],
            section[  1 : -1 ],
            section[  2 :    ]
        ) if (
            first_letter == third_letter
            and first_letter != second_letter
        )
    )

def is_valid(address):
    sections, sections_bracketed = address

    abas = get_abas(sections)
    if not abas:
        return False

    return any(
        (a, b, a) in abas
        for b, a, _ in get_abas(sections_bracketed) # babs
    )

print(
    sum(
        is_valid(address)
        for address in addresses
    )
)
