total_contained = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    elf_1, elf_2 = line.split(',')
    elf_1_start, elf_1_end = map(int, elf_1.split('-'))
    elf_2_start, elf_2_end = map(int, elf_2.split('-'))

    if elf_1_start > elf_2_end or elf_2_start > elf_1_end:
        continue

    total_contained += 1

print(total_contained)
