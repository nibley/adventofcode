clues = {}

def accuse_aunt(aunt_number):
    aunt_clues = clues[aunt_number]
    for clue_name, clue_value in aunt_clues.items():
        if clue_name in knowledge and knowledge[clue_name] != clue_value:
            return False
    
    # didn't end up needing to try the given knowledge against the aunt
    
    return True

def parse_aunt(line):
    pieces = line.split(', ')
    aunt_info, *real_first_piece = pieces[0].split(': ')
    pieces[0] = ': '.join(real_first_piece)
    
    aunt_number = aunt_info.split(' ')[1]
    aunt_clues = {}

    for piece in pieces:
        clue_name, clue_value = piece.split(': ')
        aunt_clues[clue_name] = int(clue_value)

    clues[aunt_number] = aunt_clues

while True:
    try:
        line = input()
    except EOFError:
        break
    
    parse_aunt(line)

knowledge = {
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

for aunt_number in clues:
    if accuse_aunt(aunt_number):
        print(aunt_number)
        break
