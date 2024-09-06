from itertools import combinations

checksum = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    
    row = [int(piece) for piece in line.split('\t')]
    row.sort()
    
    pairs = combinations(row, 2)
    correct_pair = None
    for pair in pairs:
        if pair[1] % pair[0] == 0:
            correct_pair = pair
            break

    checksum += correct_pair[1] // correct_pair[0]

print(checksum)
