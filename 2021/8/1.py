total = 0

while True:
    try:
        line = input()
    except EOFError:
        break

    _, right_side = line.split(' | ')
    digits = right_side.split(' ')

    for digit in digits:
        if len(digit) in [2, 4, 3, 7]:
            total += 1

print(total)
