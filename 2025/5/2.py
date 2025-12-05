from itertools import combinations

ingredient_ranges = []

while True:
    line = input()

    if not line:
        break

    ingredient_ranges.append(tuple(map(int, line.split('-'))))

while True:
    found_overlap = False
    for first_range, second_range in combinations(ingredient_ranges, 2):
        first_start, first_stop = first_range
        second_start, second_stop = second_range

        if (
            first_start in range(second_start, second_stop + 1)
            or second_start in range(first_start, first_stop + 1)
        ):
            ingredient_ranges.remove(first_range)
            ingredient_ranges.remove(second_range)

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
