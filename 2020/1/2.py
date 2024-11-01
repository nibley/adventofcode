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
        for j, second_number in enumerate(numbers[ i : ]):
            for third_number in numbers[ j : ]:
                if first_number + second_number + third_number == 2020:
                    return first_number * second_number * third_number

print(find_em())
