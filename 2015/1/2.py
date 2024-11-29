instructions = input()
floor = 0
enumeration = iter(enumerate(instructions, start=1))
while floor > -1:
    i, instruction = next(enumeration)
    floor += 1 if instruction == '(' else -1

print(i)
