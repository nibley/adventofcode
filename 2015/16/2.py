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

def check_aunt(aunt_clues):
    for clue_name, aunt_value in aunt_clues.items():
        knowledge_value = KNOWLEDGE.get(clue_name)

        if knowledge_value is None:
            continue # aunt not ruled out
        elif clue_name in {'cats', 'trees'}:
            if knowledge_value >= aunt_value:
                return False
        elif clue_name in {'pomeranians', 'goldfish'}:
            if knowledge_value <= aunt_value:
                return False
        elif knowledge_value != aunt_value:
            return False

    return True

print(
    next(
        aunt_number
        for aunt_number, aunt_clues in clues.items()
        if check_aunt(aunt_clues)
    )
)
