from itertools import permutations

def circular_permutations(people):
    # from https://stackoverflow.com/a/51532160
    head, *tail = people
    for tail_permutation in permutations(tail):
        yield (head, *tail_permutation)

def happiness_score(people):
    return sum(
        (
            feelings[first_person][second_person]
            + feelings[second_person][first_person]
        )
        for first_person, second_person in zip(
            people,
            (*people[ 1 : ], people[0])
        )
    )

feelings = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    *rest, person_object = line.split()
    person_object = person_object[ : -1 ]
    person_subject, _, valence, units, *_ = rest
    delta = int(units) * (-1 if valence == 'lose' else 1)

    feelings.setdefault(person_subject, {})
    feelings[person_subject][person_object] = delta

arrangements = circular_permutations(feelings)
print(max(map(happiness_score, arrangements)))
