stream = input()

in_garbage = False
next_char_canceled = False
garbage_count = 0
for char in stream:
    if in_garbage:
        if next_char_canceled:
            next_char_canceled = False
        elif char == '!':
            next_char_canceled = True
        elif char == '>':
            in_garbage = False
        else:
            garbage_count += 1
    else:
        if char == '<':
            in_garbage = True

print(garbage_count)
