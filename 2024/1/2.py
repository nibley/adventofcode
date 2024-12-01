from collections import Counter

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break

    lines.append(map(int, line.split()))

first_list, second_list = zip(*lines)
second_list_counter = Counter(second_list)
print(
    sum(
        item * second_list_counter[item]
        for item in first_list
    )
)
