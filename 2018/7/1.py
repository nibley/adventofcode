required_before = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, right_side = line.split(' must be finished before step ')
    before = left_side.split(' ')[1]
    after = right_side.split(' ')[0]

    required_before.setdefault(before, [])
    required_before.setdefault(after, [])

    required_before[after].append(before)

correct_order = ''
while required_before:
    new_step = sorted(
        [ step for step, required \
        in required_before.items() \
        if not required ]
    )[0]
    correct_order += new_step

    del required_before[new_step]
    for step, required in required_before.items():
        if new_step in required:
            required.remove(new_step)

print(correct_order)
