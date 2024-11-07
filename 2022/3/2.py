groups = []
while True:
    try:
        elf1 = input()
        elf2 = input()
        elf3 = input()
    except EOFError:
        break

    groups.append( (elf1, elf2, elf3) )

total_priority = 0
for elf1, elf2, elf3 in groups:
    shared_item = set(elf1).intersection( \
        set(elf2)).intersection(set(elf3)).pop()
    
    if shared_item.isupper():
        priority = ord(shared_item) - 65 + 1 + 26
    else:
        priority = ord(shared_item) - 97 + 1

    total_priority += priority

print(total_priority)
