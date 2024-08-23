the_input = input()
current_index = 0
floor = 0

for i, c in enumerate(the_input):
    current_index = i

    if c == '(': floor += 1
    elif c == ')': floor -= 1

    if floor == -1: break

print(i + 1)
