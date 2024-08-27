def is_valid(address):
    sections, sections_bracketed = address

    abas = set(get_abas(sections))
    babs = set(get_abas(sections_bracketed))

    for aba in abas:
        a = aba[0]
        b = aba[1]
        matching_bab = (b, a, b)
        if matching_bab in babs:
            return True

def three_character_windows(section):
    for i, char_1 in enumerate(section[:-2]):
        char_2 = section[i + 1]
        char_3 = section[i + 2]

        yield (char_1, char_2, char_3)

def get_abas(sections):
    for section in sections:
        windows = three_character_windows(section)
    
        for char_1, char_2, char_3 in windows:
            if char_1 == char_3 and char_1 != char_2:
                yield (char_1, char_2, char_3)

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
            sections.append(subpieces[0])
        else:
            sections.append(subpieces[1])
            sections_bracketed.append(subpieces[0])
    
    addresses.append((sections, sections_bracketed))

total = 0
for address in addresses:
    if is_valid(address):
        total += 1

print(total)
