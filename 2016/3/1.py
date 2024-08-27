triangles = []
while True:
    try:
        line = input()
    except EOFError:
        break
    
    pieces = line.split(' ')
    triangle = tuple(sorted(int(piece) for piece in pieces if piece))
    triangles.append(triangle)

def is_valid(triangle):
    return triangle[0] + triangle[1] > triangle[2]

print(len(list(filter(is_valid, triangles))))
