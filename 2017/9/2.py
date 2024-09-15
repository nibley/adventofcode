raw = input()

garbage_count = 0
in_garbage = False
next_char_canceled = False
for char in raw:
    if in_garbage:
        if next_char_canceled:
            next_char_canceled = False
        elif char == '>':
            in_garbage = False
        elif char == '!':
            next_char_canceled = True
        else:
            garbage_count += 1
    else:
        if char == '<':
            in_garbage = True

print(garbage_count)
