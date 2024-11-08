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
for operation in program:
    cycle_increment = 1 if operation is None else 2
    for subcycle in range(cycle_increment):
        x = (cycle - 1) % 40

        if x == 0:
            print()

        char = ' ' if abs(x - x_register) > 1 else '#'
        print(char * 2, end='') # double up to make output more legible

        cycle += 1

        if subcycle == 1 and operation is not None:
            x_register += operation

print()
``
