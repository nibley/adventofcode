program = []
while True:
    try:
        line = input()
    except EOFError:
        break

    if line == 'noop':
        program.append(None)
    else:
        _, delay = line.split(' ')
        program.append(int(delay))

x_register = 1
cycle = 1
desired_cycles = (20, 60, 100, 140, 180, 220)
total_strength = 0
for operation in program:
    cycle_increment = 1 if operation is None else 2
    for subcycle in range(cycle_increment):
        cycle += 1

        if subcycle == 1 and operation is not None:
            x_register += operation

        if cycle in desired_cycles:
            total_strength += cycle * x_register

print(total_strength)
