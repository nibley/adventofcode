claims = []
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, right_side = line.split(' @ ')
    claim_id = int(left_side[1 : ])
    offset, dimensions = right_side.split(': ')
    offset = map(int, offset.split(','))
    dimensions = map(int, dimensions.split('x'))

    claims.append( (claim_id, offset, dimensions) )

cloth_length = 1000
cloth = []
for _ in range(cloth_length):
    cloth.append([0] * cloth_length)

for claim in claims:
    _, offset, dimensions = claim
    
    x_start, y_start = offset
    width, height = dimensions

    for row in range(height):
        for column in range(width):
            cloth[y_start + row][x_start + column] += 1

total = 0
for row in cloth:
    for column in row:
        if column > 1:
            total += 1

print(total)
