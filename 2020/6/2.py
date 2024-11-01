def consensus(group):
    consensus_letters = group[0]
    for person in group[1:]:
        consensus_letters = consensus_letters.intersection(person)
    
    return len(consensus_letters)

total = 0
current_group = []
while True:
    try:
        line = input()

    except EOFError:
        total += consensus(current_group)
        break

    if line:
        current_group.append(set(line))
    else:
        total += consensus(current_group)
        current_group = []

print(total)
