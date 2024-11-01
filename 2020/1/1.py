numbers = []
while True:
    try:
        line = input()
    except EOFError:
        break

    number = int(line)
    numbers.append(number)

def find_em():
    for i, first_number in enumerate(numbers):
        for second_number in numbers[ i : ]:
            if first_number + second_number == 2020:
                return first_number * second_number

print(find_em())
