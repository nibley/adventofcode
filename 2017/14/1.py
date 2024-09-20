from functools import reduce

def knot_hash_bit_count(input_string):
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

    return sum( \
        reduce(lambda a, b: a ^ b, rope[16 * i : 16 * (i + 1)]).bit_count() \
        for i in range(16)
    )

secret = input()
print(sum(knot_hash_bit_count(f'{secret}-{i}') for i in range(128)))
