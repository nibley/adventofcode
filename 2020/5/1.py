seat_codes = []
while True:
    try:
        line = input()
    except EOFError:
        break

    seat_codes.append(line)

num_rows = 128
num_columns = 8

largest_id = 0
for code in seat_codes:
    row_code = code[:7]
    region_size = num_rows // 2
    seat_row = 0
    for letter in row_code:
        if letter == 'B':
            seat_row += region_size

        region_size = region_size // 2

    column_code = code[7:]
    region_size = num_columns // 2
    seat_column = 0
    for letter in column_code:
        if letter == 'R':
            seat_column += region_size
        
        region_size = region_size // 2

    seat_id = seat_row * 8 + seat_column
    if seat_id > largest_id:
        largest_id = seat_id

print(largest_id)
