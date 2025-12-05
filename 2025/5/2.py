from itertools import combinations

ingredient_ranges = []

while True:
    line = input()

    if not line:
        break

    ingredient_ranges.append(tuple(map(int, line.split('-'))))

while True:
    range_indices = range(len(ingredient_ranges))
    found_overlap = False
    for first_index, second_index in combinations(range_indices, 2):
        first_start, first_stop = ingredient_ranges[first_index]
        second_start, second_stop = ingredient_ranges[second_index]

        if (
            first_start in range(second_start, second_stop + 1)
            or second_start in range(first_start, first_stop + 1)
        ):
            first_index, second_index = sorted( (first_index, second_index) )
            del ingredient_ranges[second_index]
            del ingredient_ranges[first_index]

            ingredient_ranges.append(
                (
                    min( (first_start, second_start) ),
                    max( (first_stop, second_stop) )
                )
            )

            found_overlap = True
            break

    if not found_overlap:
        break

print(sum( stop - start + 1 for start, stop in ingredient_ranges ))
