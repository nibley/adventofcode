def decrypt(name, sector_id):
    shift = sector_id % 26
    ord_z = ord('z')

    plaintext = ''
    for char in name:
        if char == '-':
            plaintext += ' '
        else:
            new_ord = ord(char) + shift
            if new_ord > ord_z:
                new_ord -= 26
            plaintext += chr(new_ord)
    
    return plaintext

rooms = []
while True:
    try:
        line = input()
    except EOFError:
        break
    
    left_side, right_side = line.split('[')
    *name, sector_id = left_side.split('-')
    checksum = right_side.replace(']', '')
    rooms.append((int(sector_id), '-'.join(name), checksum))

for sector_id, name, checksum in rooms:
    frequencies = {}
    for char in name:
        frequencies.setdefault(char, 0)
        frequencies[char] += 1
    del frequencies['-']
    most_common = sorted(frequencies.items(), key=lambda item: (-item[1], item[0]))[:5]
    
    if checksum == ''.join([item[0] for item in most_common]):
        plaintext = decrypt(name, sector_id)
        if 'north' in plaintext:
            print(sector_id, plaintext)
