goal = int(input())

recipes = [3, 7]
first_elf_index, second_elf_index = (0, 1)
while len(recipes) < goal + 10:
    first_elf_score = recipes[first_elf_index]
    second_elf_score = recipes[second_elf_index]

    recipes.extend(map(int, f'{first_elf_score + second_elf_score}'))

    first_elf_index = (first_elf_index + 1 + first_elf_score) % len(recipes)
    second_elf_index = (second_elf_index + 1 + second_elf_score) % len(recipes)

print(''.join(map(str, recipes[ -10 : ])))
