goal = tuple(map(int, input()))

recipes = {
    0 : 3,
    1 : 7
}
first_elf_index, second_elf_index = (0, 1)
while True:
    first_elf_score = recipes[first_elf_index]
    second_elf_score = recipes[second_elf_index]

    for digit in f'{first_elf_score + second_elf_score}':
        recipes[ len(recipes )] = int(digit)

    first_elf_index = (first_elf_index + 1 + first_elf_score) % len(recipes)
    second_elf_index = (second_elf_index + 1 + second_elf_score) % len(recipes)

    if len(recipes) > len(goal):
        end_recipes = tuple(
            recipes[ len(recipes) - 1 - i ]
            for i in reversed(range(len(goal) + 1))
        )
        if goal in (end_recipes[ : -1 ], end_recipes[ 1 : ]):
            break

print(
    len(recipes)
    - len(goal)
    - (
        0 if goal == tuple(
            recipes[ len(recipes) - 1 - i ]
            for i in reversed(range(len(goal)))
        ) else 1
    )
)
