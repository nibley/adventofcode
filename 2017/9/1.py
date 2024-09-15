raw = input()

group_level = 1
group_count_by_level = {}
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
        if char == '<':
            in_garbage = True
        elif char == '{':
            group_count_by_level.setdefault(group_level, 0)
            group_count_by_level[group_level] += 1

            group_level += 1
        elif char == '}':
            group_level -= 1

print(sum( (k * v for k, v in group_count_by_level.items()) ), 'score')
