from itertools import islice

the_input = input()

visited = {}
x_human = 0
y_human = 0
x_robot = 0
y_robot = 0

def chunk(arr_range, arr_size):
    arr_range = iter(arr_range)
    return iter(lambda: tuple(islice(arr_range, arr_size)), ())

for instr in chunk(the_input, 2):
    visited[(x_human, y_human)] = True
    visited[(x_robot, y_robot)] = True

    instr_human, instr_robot = instr

    if instr_human == '<': x_human -= 1
    if instr_human == '>': x_human += 1
    if instr_human == 'v': y_human -= 1
    if instr_human == '^': y_human += 1

    if instr_robot == '<': x_robot -= 1
    if instr_robot == '>': x_robot += 1
    if instr_robot == 'v': y_robot -= 1
    if instr_robot == '^': y_robot += 1

visited[(x_human, y_human)] = True
visited[(x_robot, y_robot)] = True

print(len(visited))
