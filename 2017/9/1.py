from collections import defaultdict

stream = input()

in_garbage = False
next_char_canceled = False
group_level = 1
group_count_by_level = defaultdict(lambda: 0)
for char in stream:
    if in_garbage:
        if next_char_canceled:
            next_char_canceled = False
        elif char == '!':
            next_char_canceled = True
        elif char == '>':
            in_garbage = False
    else:
        if char == '<':
            in_garbage = True
        elif char == '{':
            group_count_by_level[group_level] += 1
            group_level += 1
        elif char == '}':
            group_level -= 1

print(
    sum(
        level * num_groups
        for level, num_groups in group_count_by_level.items()
    )
)
