from itertools import combinations

def distance(first_point, second_point):
    return sum(
        abs(first_component - second_component)
        for first_component, second_component in zip(first_point, second_point)
    )

points = []
while True:
    try:
        line = input()
    except EOFError:
        break

    points.append(tuple( int(n) for n in line.split(',') ))

groups = []
for point in points:
    found_group = False
    for group in groups:
        if any(
            distance(point, group_point) <= 3
            for group_point in group
        ):
            group.add(point)

            found_group = True
            break

    if not found_group:
        groups.append(set( (point, ) ))

while True:
    merged_group = False
    for (i, first_group), (j, second_group) in combinations(enumerate(groups), 2):
        if any(
            distance(first_group_point, second_group_point) <= 3
            for first_group_point in first_group
            for second_group_point in second_group
        ):
            del groups[i]
            second_group.update(first_group)

            merged_group = True
            break

    if not merged_group:
        break

print(len(groups))
