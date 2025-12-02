line = input()
ranges = []
for raw_range in line.split(','):
    new_range = tuple( map(int, raw_range.split('-')) )
    assert len(new_range) == 2 and new_range[1] > new_range[0]
    ranges.append(new_range)

total = 0
for start, stop in ranges:
    for i in range(start, stop + 1):
        text = str(i)
        
        if len(text) % 2:
            continue
        
        if text[ : len(text) // 2 ] == text[ len(text) // 2 : ]:
            total += i

print(total)
