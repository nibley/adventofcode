from functools import reduce

raw = input()
knot_lengths = tuple(map(ord, raw)) + (17, 31, 73, 47, 23)

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

chunks = [ rope[16 * i : 16 * (i + 1)] for i in range(16) ]
hashes = [ reduce(lambda a, b: a ^ b, chunk) for chunk in chunks ]
print(''.join('{:02X}'.format(the_hash) for the_hash in hashes))
