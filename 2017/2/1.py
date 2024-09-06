checksum = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    
    row = [int(piece) for piece in line.split('\t')]
    row.sort()
    checksum += row[-1] - row[0]

print(checksum)
