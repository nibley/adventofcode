claims = []
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, right_side = line.split(' @ ')
    claim_id = int(left_side[1 : ])
    offset, dimensions = right_side.split(': ')
    offset = tuple(map(int, offset.split(',')))
    dimensions = tuple(map(int, dimensions.split('x')))

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

for claim in claims:
    claim_id, offset, dimensions = claim

    x_start, y_start = offset
    width, height = dimensions

    found_overlap = False
    for row in range(height):
        for column in range(width):
            if cloth[y_start + row][x_start + column] > 1:
                found_overlap = True
                break
        
        if found_overlap:
            break
    
    if found_overlap:
        continue
    
    print(claim_id)
    break

