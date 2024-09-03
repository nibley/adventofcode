blocked_ranges = []
while True:
    try:
        line = input()
    except EOFError:
        break

    blocked_ranges.append(tuple(map(int, line.split('-'))))

lowest_allowed = 0
while blocked_ranges:
    blocked_ranges_next_pass = []
    found_block = False
    for blocked_range in blocked_ranges:
        if blocked_range[0] <= lowest_allowed <= blocked_range[1]:        
            lowest_allowed = blocked_range[1] + 1
            found_block = True
        else:
            blocked_ranges_next_pass.append(blocked_range)
    
    if not found_block:
        break

    blocked_ranges = blocked_ranges_next_pass

print(lowest_allowed)
