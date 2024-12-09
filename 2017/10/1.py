KNOT_LENGTHS = map(int, input().split(','))
ROPE_SIZE = 256

rope = [ i for i in range(ROPE_SIZE) ]
position = 0
skip_size = 0
for knot_length in KNOT_LENGTHS:
    knot_region_main = slice(
        position,
        min(ROPE_SIZE, position + knot_length)
    )
    wrap_length = position + knot_length - ROPE_SIZE

    if wrap_length < 1:
        rope[knot_region_main] = reversed(rope[knot_region_main])
    else:
        knot_region_wrap = slice(0, wrap_length)
        knot_region_reversed = (
            rope[knot_region_main] + rope[knot_region_wrap]
        )[ : : -1 ]

        rope[ : knot_region_wrap.stop ] = (
            knot_region_reversed[ -1 * knot_region_wrap.stop : ]
        )
        rope[position : ] = (
            knot_region_reversed[ : -1 * knot_region_wrap.stop ]
        )

    position = (position + knot_length + skip_size) % ROPE_SIZE
    skip_size += 1

print(rope[0] * rope[1])
