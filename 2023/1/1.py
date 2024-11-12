total = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    digits = [ char for char in line if char.isnumeric() ]
    line_calibration = f'{digits[0]}{digits[-1]}'
    total += int(line_calibration)

print(total)
