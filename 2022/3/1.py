rucksacks = []
while True:
    try:
        line = input()
    except EOFError:
        break

    rucksacks.append(line)

total_priority = 0
for rucksack in rucksacks:
    num_items = len(rucksack)
    first_compartment = rucksack[ : num_items // 2 ]
    second_compartment = rucksack[ num_items // 2 : ]

    shared_item = set(first_compartment).intersection( \
        set(second_compartment)).pop()
    if shared_item.isupper():
        priority = ord(shared_item) - 65 + 1 + 26
    else:
        priority = ord(shared_item) - 97 + 1

    total_priority += priority

print(total_priority)
