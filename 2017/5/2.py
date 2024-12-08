program = []
while True:
    try:
        line = input()
    except EOFError:
        break

    program.append(int(line))

def access_program(i):
    offset = program[i]
    program[i] += 1 if offset < 3 else -1

    return offset

steps = 0
position = 0
while 0 <= position < len(program):
    steps += 1
    position += access_program(position)

print(steps)
