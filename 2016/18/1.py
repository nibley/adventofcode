trap_cases = [
    (False, False, True),
    (True, False, False),
    (False, True, True),
    (True, True, False),
]
def generate_cell(i, prev_row):
    left = right = True
    center = prev_row[i]
    if i != 0:
        left = prev_row[i - 1]
    if i != width - 1:
        right = prev_row[i + 1]
    
    return not ( (left, center, right) in trap_cases )

rows = []
rows.append([char == '.' for char in input()])
width = len(rows[0])
num_rows = 40
for num_row in range(1, num_rows):
    prev_row = rows[num_row - 1]
    new_row = [generate_cell(i, prev_row) for i in range(width)]
    rows.append(new_row)

total_safe = 0
for row in rows:
    for tile in row:
        if tile:
            total_safe += 1

print(total_safe)
