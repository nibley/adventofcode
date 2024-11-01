seat_codes = []
while True:
    try:
        line = input()
    except EOFError:
        break

    seat_codes.append(line)

num_rows = 128
num_columns = 8

seat_ids = []
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

    seat_ids.append(seat_row * 8 + seat_column)

seat_ids.sort()
low_id = seat_ids[0]
high_id = seat_ids[-1]

seat_ids_set = set(seat_ids)

missing_ids = set(range(low_id, high_id + 1)).difference(seat_ids_set)
for missing_id in missing_ids:
    if missing_id - 1 in seat_ids_set and missing_id + 1 in seat_ids_set:
        print(missing_id)
        break
