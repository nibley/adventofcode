def parse_line(line):
    pieces = line.split(' ')
    return [int(piece) for piece in pieces if piece]

triangles = []
while True:
    try:
        line1 = input()
        line2 = input()
        line3 = input()
    except EOFError:
        break
    
    rows = zip(parse_line(line1), parse_line(line2), parse_line(line3))
    for row in rows:
        triangle = tuple(sorted(row))
        triangles.append(triangle)

def is_valid(triangle):
    return triangle[0] + triangle[1] > triangle[2]

print(len(list(filter(is_valid, triangles))))
