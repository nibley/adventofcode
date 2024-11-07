total_contained = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    elf_1, elf_2 = line.split(',')
    elf_1_start, elf_1_end = map(int, elf_1.split('-'))
    elf_2_start, elf_2_end = map(int, elf_2.split('-'))

    narrower_range, wider_range = sorted([(elf_1_start, elf_1_end), (elf_2_start, elf_2_end)], key=lambda pair: pair[1] - pair[0])
    narrower_start, narrower_end = narrower_range
    wider_start, wider_end = wider_range

    if wider_start <= narrower_start and wider_end >= narrower_end:
        total_contained += 1

print(total_contained)
