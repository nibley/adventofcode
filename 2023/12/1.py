from itertools import groupby, zip_longest, product as cartesian_product

records = []
while True:
    try:
        line = input()
    except EOFError:
        break

    springs, groups = line.split()
    groups = tuple( int(n) for n in groups.split(',') )
    records.append( (springs, groups) )

def substitute_springs(springs, choice):
    (choice_index, spring_working), *choice = choice
    for i, spring in enumerate(springs):
        if i == choice_index:
            yield '.' if spring_working else '#'
            if choice:
                (choice_index, spring_working), *choice = choice
        else:
            yield spring


def choice_is_valid(springs, groups, choice):
    springs_with_choice = substitute_springs(springs, choice)
    choice_groups = (
        len(tuple(group))
        for key, group in groupby(springs_with_choice)
        if key == '#'
    )

    return all(
        group_length == correct_group_length
        for group_length, correct_group_length in zip_longest(
            choice_groups,
            groups
        )
    )

def count_possibilities(record):
    springs, groups = record

    unknown_indeces = tuple(
        i
        for i, spring in enumerate(springs)
        if spring == '?'
    )

    choices = (
        zip(unknown_indeces, choice)
        for choice in cartesian_product(
            (True, False),
            repeat=springs.count('?')
        )
    )

    return sum(
        choice_is_valid(springs, groups, choice)
        for choice in choices
    )

print(sum(map(count_possibilities, records)))
