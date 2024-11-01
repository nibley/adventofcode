total = 0
current_group = set()
while True:
    try:
        line = input()

    except EOFError:
        total += len(current_group)
        break

    if line:
        current_group.update(line)
    else:
        total += len(current_group)
        current_group = set()

print(total)
