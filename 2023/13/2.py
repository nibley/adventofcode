patterns = []
while True:
    try:
        pattern = []

        row = input()
        while row:
            pattern.append(row)
            row = input()
    except EOFError:
        break
    finally:
        patterns.append(tuple(pattern))

def get_reflection_score(pattern):
    for y, row in enumerate(pattern[:-1]): # line goes below row y
        if 1 == sum(
            get_smudge_count(pattern[row_above], pattern[row_below])
            for row_above, row_below in zip(
                range(y, -1, -1),
                range(y + 1, len(pattern))
            )
        ):
            return 100 * (y + 1)

    for x in range(len(pattern[0]) - 1): # line goes right of column x
        if 1 == sum(
            get_smudge_count(
                ( row[column_left] for row in pattern ),
                ( row[column_right] for row in pattern )
            )
            for column_left, column_right in zip(
                range(x, -1, -1),
                range(x + 1, len(pattern[0]))
            )
        ):
            return x + 1

    assert False # should have returned already

def get_smudge_count(sequence_a, sequence_b):
    return sum(
        a != b
        for a, b in zip(sequence_a, sequence_b)
    )

print(sum(
    get_reflection_score(pattern)
    for pattern in patterns
))
