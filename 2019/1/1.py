# newline in input

fuel = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    mass = int(line)
    fuel += mass // 3 - 2

print(fuel)
