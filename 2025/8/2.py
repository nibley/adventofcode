from itertools import combinations

boxes = []

while True:
    try:
        line = input()
    except EOFError:
        break

    box = tuple(map(int, line.split(',')))
    boxes.append(box)

distances = {}
for first_box, second_box in combinations(boxes, 2):
    first_x, first_y, first_z = first_box
    second_x, second_y, second_z = second_box
    distance = (
        (first_x - second_x) ** 2
        + (first_y - second_y) ** 2
        + (first_z - second_z) ** 2
    )
    distances[frozenset( (first_box, second_box) )] = distance

connections = sorted(distances.items(), key=lambda pair: pair[1])

groups = { # box to index of its group
    box : i
    for i, box in enumerate(boxes)
}

final_length = None
for connection in connections:
    boxes, _ = connection
    first_box, second_box = boxes

    first_group_id = groups[first_box]
    second_group_id = groups[second_box]
    
    groups = {
        box : (group_id if group_id != second_group_id else first_group_id)
        for box, group_id in groups.items()
    }

    if len(set(groups.values())) == 1:
        first_x, _, _ = first_box
        second_x, _, _ = second_box
        final_length = first_x * second_x
        break

assert final_length is not None
print(final_length)
