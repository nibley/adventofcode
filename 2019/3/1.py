parse_wire = lambda wire: list(map(
    lambda piece: (piece[0], int(piece[1:])),
    wire.split(',')))

first_wire = parse_wire(input())
second_wire = parse_wire(input())

point_sets = []
for wire in (first_wire, second_wire):
    x = 0
    y = 0
    point_set = set()
    for direction, steps in wire:
        for _ in range(steps):
            if direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            elif direction == 'L':
                x -= 1
            elif direction == 'R':
                x += 1
            
            point_set.add( (x, y) )
    
    point_sets.append(point_set)

intersections = point_sets[0].intersection(point_sets[1])
print(sorted(map(
    lambda intersection: abs(intersection[0]) + abs(intersection[1]),
    intersections))[0])
