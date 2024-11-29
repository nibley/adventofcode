clues = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    _, aunt_number, *aunt_clues = line.replace(':', '').split()
    clues[ int(aunt_number) ] = {
        clue_name : int(clue_value.replace(',', ''))
        for clue_name, clue_value in zip(
            aunt_clues[   : -1 : 2 ],
            aunt_clues[ 1 :    : 2 ]
        )
    }

KNOWLEDGE = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

print(
    next(
        aunt_number
        for aunt_number, aunt_clues in clues.items()
        if all(
            KNOWLEDGE.get(clue_name) == clue_value
            for clue_name, clue_value in aunt_clues.items()
        )
    )
)
