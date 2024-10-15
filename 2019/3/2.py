parse_wire = lambda wire: list(map(
    lambda piece: (piece[0], int(piece[1:])),
    wire.split(',')))

first_wire = parse_wire(input())
second_wire = parse_wire(input())

point_dicts = []
for wire in (first_wire, second_wire):
    x = 0
    y = 0
    step = 1
    point_dict = {}
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
            
            point_dict.setdefault((x, y), step)
            step += 1
    
    point_dicts.append(point_dict)

intersections = set(point_dicts[0].keys()).intersection(set(point_dicts[1].keys()))
print(sorted(map(
    lambda intersection: point_dicts[0][intersection] + point_dicts[1][intersection],
    intersections))[0])
