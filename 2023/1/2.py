number_replacements = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9' }

numbers = list(number_replacements.keys()) + \
    list(number_replacements.values())

total = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    numbers_found = []
    for number in numbers:
        index = 0
        while True:
            index = line.find(number, index)

            if index == -1:
                break

            index += 1 # search farther ahead next time
            numbers_found.append( (number, index) )

    numbers_sorted = sorted(numbers_found, key=lambda pair: pair[1])

    first_number = numbers_sorted[0][0]
    if first_number in number_replacements:
        first_number = number_replacements[first_number]

    last_number = numbers_sorted[-1][0]
    if last_number in number_replacements:
        last_number = number_replacements[last_number]

    line_calibration = f'{first_number}{last_number}'
    total += int(line_calibration)

print(total)
