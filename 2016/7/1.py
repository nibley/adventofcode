def is_valid(address):
    sections, sections_bracketed = address

    for section_bracketed in sections_bracketed:
        if has_abba(section_bracketed):
            return False

    for section in sections:
        if has_abba(section):
            return True

def has_abba(section):
    for i, char_1 in enumerate(section[:-3]):
        char_2 = section[i + 1]
        char_3 = section[i + 2]
        char_4 = section[i + 3]

        if char_1 == char_2:
            continue
        
        if char_1 == char_4 and char_2 == char_3:
            return True
    
    return False

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
