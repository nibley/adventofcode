blocked_ranges = []
while True:
    try:
        line = input()
    except EOFError:
        break

    start, stop = map(int, line.split('-'))
    blocked_ranges.append(range(start, stop + 1))

ip_address = 0
for blocked_range in sorted(
    blocked_ranges,
    key=lambda blocked_range: blocked_range.start
):
    if ip_address in blocked_range:
        ip_address = blocked_range.stop

print(ip_address)
