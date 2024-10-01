# prepare yourself for tuples

def get_rotations(pattern):
    # yields all rotation / flip states
    flipped = pattern[::-1]
    double_flipped = tuple(row[::-1] for row in flipped)

    yield pattern
    yield flipped
    yield double_flipped

    for _ in range(3):
        pattern = tuple(zip(*pattern[::-1]))
        yield pattern

        flipped = tuple(zip(*flipped[::-1]))
        yield flipped

        double_flipped = tuple(zip(*double_flipped[::-1]))
        yield double_flipped

def get_sections(pattern):
    # gets rows of size-n subsections from pattern
    # n is either 2 or 3, per divisibility
    size = 2 if not len(pattern) % 2 else 3

    for y in range(0, len(pattern), size):
        yield tuple(
            tuple(row[ x : x + size ] for row in pattern[ y : y + size ])
            for x in range(0, len(pattern), size)
        )

rules = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    start, end = line.split(' => ')
    start = tuple( tuple(row) for row in start.split('/') )
    end = tuple( tuple(row) for row in end.split('/') )

    rules[start] = end

pattern = (
    ('.', '#', '.'),
    ('.', '.', '#'),
    ('#', '#', '#'),
)

for _ in range(5):
    new_section_size = 3 if not len(pattern) % 2 else 4
    new_pattern = []

    for section_row in get_sections(pattern):
        new_pattern_row = [ () for _ in range(new_section_size) ]

        for section in section_row:
            for candidate in get_rotations(section):
                if candidate in rules:
                    break

            replacement = rules[candidate]
            for i, replacement_row in enumerate(replacement):
                new_pattern_row[i] = new_pattern_row[i] + replacement_row

        new_pattern.extend(new_pattern_row)
    
    pattern = tuple(new_pattern)

for row in pattern:
    print(''.join(row))
print()

print(sum(row.count('#') for row in pattern))
