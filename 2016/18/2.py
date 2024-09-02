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

prev_row = [char == '.' for char in input()]
total_safe = len([tile for tile in prev_row if tile])
width = len(prev_row)
num_rows = 400000
for num_row in range(1, num_rows):
    new_row = [generate_cell(i, prev_row) for i in range(width)]
    for tile in new_row:
        if tile:
            total_safe += 1
    prev_row = new_row

print(total_safe)
