TRAP_CASES = (
    (False, False, True),
    (True,  False, False),
    (False, True,  True),
    (True,  True,  False)
)
def generate_cell(x, last_row):
    center = last_row[x]
    left = True if x == 0 else last_row[x - 1]
    right = True if x == WIDTH - 1 else last_row[x + 1]

    return (left, center, right) not in TRAP_CASES

# True for safe, False for trap
FIRST_ROW = tuple( char == '.' for char in input() )
WIDTH = len(FIRST_ROW)

def simulate(first_row):
    yield sum(first_row)

    last_row = first_row
    for _ in range(1, 400_000):
        last_row = tuple( generate_cell(x, last_row) for x in range(WIDTH) )
        yield sum(last_row)

print(sum(simulate(FIRST_ROW)))
