def parse_license():
    global total
    global cursor

    num_children = numbers[cursor]
    cursor += 1

    num_metadata = numbers[cursor]
    cursor += 1

    for _ in range(num_children):
        parse_license()

    for _ in range(num_metadata):
        total += numbers[cursor]
        cursor += 1

numbers = list(map(int, input().split(' ')))

total = 0
cursor = 0
parse_license()

print(total)
