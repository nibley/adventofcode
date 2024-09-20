from functools import reduce, cache
from itertools import product as cartesian_product

def knot_hash_row(input_string):
    knot_lengths = tuple(map(ord, input_string)) + (17, 31, 73, 47, 23)
    rope_size = 256
    rope = [i for i in range(rope_size)]
    position = 0
    skip_size = 0
    for _ in range(64):
        for knot_length in knot_lengths:
            knot_region_main = slice(position, min(rope_size, position + knot_length))
            wrap_length = position + knot_length - rope_size

            if wrap_length < 1:
                rope[knot_region_main] = reversed(rope[knot_region_main])
            else:
                knot_region_wrap = slice(0, wrap_length)
                knot_region_reversed = ( \
                    rope[knot_region_main] + rope[knot_region_wrap] \
                )[::-1]

                rope[ : knot_region_wrap.stop] = \
                    knot_region_reversed[-1 * knot_region_wrap.stop : ]
                rope[position : ] = \
                    knot_region_reversed[ : -1 * knot_region_wrap.stop]

            position = (position + knot_length + skip_size) % rope_size
            skip_size += 1

    chunks = (
        '{:08b}'.format(
            reduce(
                lambda a, b: a ^ b,
                rope[16 * i : 16 * (i + 1)]))
        for i in range(16)
    )

    return reduce(
        lambda a, b: a + b,
        ( [char == '1' for char in chunk] for chunk in chunks ))

@cache
def get_cell(x, y):
    if (
        0 <= x < 128
        and 0 <= y < 128
    ):
        return ropes[y][x]
    else:
        return False

def get_used_neighbors(x, y):
    return filter(
        lambda position: get_cell(*position),
        [
            (x, y - 1),
            (x - 1, y),
            (x + 1, y),
            (x, y + 1),
        ])

secret = input()
ropes = [ knot_hash_row(f'{secret}-{i}') for i in range(128) ]
latest_region = 1
regions = {}
for x, y in cartesian_product(range(len(ropes)), repeat=2):
    if not get_cell(x, y):
        continue

    neighbors = get_used_neighbors(x, y)
    neighboring_regions = []
    for neighbor in neighbors:
        if neighbor in regions:
            neighboring_regions.append(regions[neighbor])

    if neighboring_regions:
        region = neighboring_regions[0]
    else:
        region = latest_region
        latest_region += 1

    regions[ (x, y) ] = region

    for redundant_region in neighboring_regions[1:]:
        for coordinate, coordinate_region in regions.items():
            if coordinate_region == redundant_region:
                regions[coordinate] = region

print(len(set(regions.values())))
