rooms = []
while True:
    try:
        line = input()
    except EOFError:
        break
    
    left_side, right_side = line.split('[')
    *name, sector_id = left_side.split('-')
    checksum = right_side.replace(']', '')
    rooms.append((int(sector_id), ''.join(name), checksum))

total = 0
for sector_id, name, checksum in rooms:
    frequencies = {}
    for char in name:
        frequencies.setdefault(char, 0)
        frequencies[char] += 1
    most_common = sorted(frequencies.items(), key=lambda item: (-item[1], item[0]))[:5]
    
    # print(most_common)
    
    if checksum == ''.join([item[0] for item in most_common]):
        total += sector_id

print(total)
