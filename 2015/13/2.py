from itertools import permutations
from math import inf

feelings = {}

def get_feeling(first_person, second_person):
    if first_person is None or second_person is None:
        return 0
    else:
        return feelings[first_person][second_person]

def circular_permutations(people):
    # from https://stackoverflow.com/a/51532160
    gen = permutations(people[1:])
    return [[people[0]] + list(end) for end in gen]

def happiness_score(people):
    pairs = []
    score = 0
    for i, person in enumerate(people[:-1]):
        pairs.append((person, people[i + 1]))
    pairs.append((people[-1], people[0]))

    for first_person, second_person in pairs:
        score += get_feeling(first_person, second_person)
        score += get_feeling(second_person, first_person)
    
    return score

while True:
    try:
        line = input()
    except EOFError:
        break
    
    left_side, person_object = line.split(' happiness units by sitting next to ')
    person_subject, _, valence, n = left_side.split(' ')
    n = int(n)
    if valence == 'lose':
        n = -1 * n
    feelings.setdefault(person_subject, {})
    feelings[person_subject][person_object[:-1]] = n

arrangements = circular_permutations(list(feelings.keys()) + [None])
highest_score = -inf
highest_score_arrangement = None
for arrangement in arrangements:
    score = happiness_score(arrangement)
    if score > highest_score:
        highest_score = score
        highest_score_arrangement = arrangement

print(' '.join(str(person) for person in highest_score_arrangement))
print(highest_score)
