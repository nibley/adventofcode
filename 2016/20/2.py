blocked_ranges = []
while True:
    try:
        line = input()
    except EOFError:
        break

    blocked_range = tuple(map(int, line.split('-')))
    blocked_ranges.append(blocked_range)

blocked_ranges.sort(key=lambda blocked_range: blocked_range[0])

address_max_value = 4294967295
num_allowed_addresses = 0
last_address_checked = 0
for blocked_range in blocked_ranges:
    range_start, range_end = blocked_range
    if range_start > last_address_checked:
        num_allowed_addresses += range_start - last_address_checked
    
    address_after_range = range_end + 1
    if address_after_range > last_address_checked:
        last_address_checked = address_after_range

last_address_checked -= 1 # in the final loop pass this was set 1 too high
allowed_addresses_after_final_range = address_max_value - last_address_checked
num_allowed_addresses += allowed_addresses_after_final_range

print(num_allowed_addresses)
