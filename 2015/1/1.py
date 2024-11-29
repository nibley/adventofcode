instructions = input()
floor = 0
for instruction in instructions:
    floor += 1 if instruction == '(' else -1

print(floor)
