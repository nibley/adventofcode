offset = int(input())

recipes = [3, 7]
first_elf_index = 0
second_elf_index = 1

while len(recipes) < offset + 10:
    first_elf_score = recipes[first_elf_index]
    second_elf_score = recipes[second_elf_index]

    new_recipe = str(first_elf_score + second_elf_score)
    for digit in new_recipe:
        recipes.append(int(digit))

    first_elf_index = (first_elf_index + 1 + first_elf_score) % len(recipes)
    second_elf_index = (second_elf_index + 1 + second_elf_score) % len(recipes)

print(''.join(str(n) for n in recipes[offset : offset + 10]))
