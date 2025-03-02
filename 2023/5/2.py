from itertools import chain
from math import inf

seed_ranges = []
seed_ranges_raw = iter(map(int, input().split(': ')[1].split()))
while True:
    try:
        start = next(seed_ranges_raw)
        length = next(seed_ranges_raw)
        seed_ranges.append(range(start, start + length))
    except StopIteration:
        break

input()

almanac_maps = []
while True:
    try:
        input()
        map_ranges = []

        map_range = input()
        while map_range:
            destination, source, length = map(int, map_range.split(' '))
            map_ranges.append( (range(source, source + length), destination) )
            map_range = input()
    except EOFError:
        break
    finally:
        almanac_maps.append(map_ranges)

def apply_almanac_map(input_values, almanac_map):
    # initial value so we can reuse the last good range sometimes
    # (it ends up being very often)
    check_range = range(0)
    check_range_start = None

    for input_value in input_values:
        # try the check_range from last loop iteration
        if input_value in check_range:
            input_value += offset - check_range_start
        else:
            for check_range, offset in almanac_map:
                if input_value in check_range:
                    check_range_start = check_range.start
                    input_value += offset - check_range_start
                    break

        yield input_value

seeds = chain(*seed_ranges)
for almanac_map in almanac_maps:
    seeds = apply_almanac_map(seeds, almanac_map)

print(min(seeds))
