discs = []
disc_number = 1
while True:
    try:
        line = input()
    except EOFError:
        break
    
    left_side, right_side = line.split(';')
    disc_positions = int(left_side.split(' ')[3])
    initial_position = int(right_side.split(' ')[-1][:-1])
    corrected_initial_position = (initial_position + disc_number) % disc_positions
    discs.append((disc_positions, corrected_initial_position))

    disc_number += 1

discs.append((11, 7))

time = 0
while True:
    right_time = True
    for disc_positions, initial_position in discs:
        position = (initial_position + time) % disc_positions
        if position:
            right_time = False
            break
    
    if right_time:
        break

    time += 1

print(time)
