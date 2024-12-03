blocked_ranges = []
while True:
    try:
        line = input()
    except EOFError:
        break

    start, stop = map(int, line.split('-'))
    blocked_ranges.append(range(start, stop + 1))

num_allowed_addresses = 0
last_address_checked = 0
for blocked_range in sorted(
    blocked_ranges,
    key=lambda blocked_range: blocked_range.start
):
    num_allowed_addresses += max(0, blocked_range.start - last_address_checked)
    last_address_checked = max(last_address_checked, blocked_range.stop)

MAX_ADDRESS = 4_294_967_295
num_allowed_addresses += MAX_ADDRESS - (last_address_checked - 1)

print(num_allowed_addresses)
