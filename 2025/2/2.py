line = input()
ranges = []
for raw_range in line.split(','):
    new_range = tuple( map(int, raw_range.split('-')) )
    assert len(new_range) == 2 and new_range[1] > new_range[0]
    ranges.append(new_range)

total = 0
def is_valid(i):
    text = str(i)
    text_length = len(text)
    
    for segment_length in range(1, text_length // 2 + 1):
        if text_length % segment_length:
            continue

        segment = text[ : segment_length ]
    
        found_repeating = True
        for n in range(1, text_length // segment_length):
            next_segment = text[ segment_length * n : segment_length * (n + 1) ]
            if segment != next_segment:
                found_repeating = False
                break
        
        if found_repeating:
            return False

    return True

for start, stop in ranges:
    for i in range(start, stop + 1):
        if not is_valid(i):
            total += i
        
print(total)
