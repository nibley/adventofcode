def move_tail():
    global tail

    distance = taxicab_distance(head, tail)
    if distance < 2:
        return

    head_x, head_y = head
    tail_x, tail_y = tail

    same_row = head_y == tail_y
    same_column = head_x == tail_x

    diagonal_needed = \
        not (same_row or same_column) and \
        ( (abs(head_x - tail_x) == 2) or (abs(head_y - tail_y) == 2) )

    if diagonal_needed or same_row:
        tail_x += 1 if head_x > tail_x else -1
    
    if diagonal_needed or same_column:
        tail_y += 1 if head_y > tail_y else -1

    tail = (tail_x, tail_y)
    tail_locations.add(tail)


taxicab_distance = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])

instructions = []
while True:
    try:
        line = input()
    except EOFError:
        break

    direction, steps = line.split(' ')
    instructions.append( (direction, int(steps)) )

head = (0, 0)
tail = (0, 0)
tail_locations = set([tail])
for direction, steps in instructions:
    for _ in range(steps):
        head_x, head_y = head

        if direction == 'U':
            head = (head_x, head_y + 1)
        elif direction == 'D':
            head = (head_x, head_y - 1)
        elif direction == 'L':
            head = (head_x - 1, head_y)
        elif direction == 'R':
            head = (head_x + 1, head_y)

        move_tail()

print(len(tail_locations))
