from collections import deque

target = [ int(digit) for digit in input() ]
# target = [5,9,4,1,4]
# target = [9, 2, 5, 1, 0]

recipes = deque([3, 7])
first_elf_index = 0
second_elf_index = 1
done = False

while True:
    if not len(recipes) % 1000:
        print(len(recipes))

    first_elf_score = recipes[first_elf_index]
    second_elf_score = recipes[second_elf_index]

    new_recipe = str(first_elf_score + second_elf_score)
    for digit in new_recipe:
        recipes.append(int(digit))
        # if recipes[ -1 * len(target) : ] == target:
            # done = True
            # break
        # print(len(recipes))
        if (
            len(recipes) >= len(target)
            and all(
                recipes[ -1 * len(target) + i ] == target_digit
                for i, target_digit in enumerate(target)
            )
        ):
            done = True
            break
    
    if done:
        break

    first_elf_index = (first_elf_index + 1 + first_elf_score) % len(recipes)
    second_elf_index = (second_elf_index + 1 + second_elf_score) % len(recipes)

# print(recipes)
print(len(recipes) - len(target))

# while True:
#     first_elf_score = recipes[-1 * (first_elf_index + 1)]
#     second_elf_score = recipes[-1 * (second_elf_index + 1)]

#     new_recipe = str(first_elf_score + second_elf_score)
#     for digit in new_recipe:
#         recipes.append(int(digit))

#     first_elf_index = (first_elf_index + 1 + first_elf_score) % len(recipes)
#     second_elf_index = (second_elf_index + 1 + second_elf_score) % len(recipes)

#     # print(recipes)
#     print(len(recipes))
