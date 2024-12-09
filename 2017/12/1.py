from collections import defaultdict

connections = defaultdict(set)
while True:
    try:
        line = input()
    except EOFError:
        break

    program, *connected_programs = map(
        int,
        line.replace(' <-> ', ', ').split(', ')
    )
    connections[program].update(connected_programs)

group = set([0])
programs_to_crawl = group
while programs_to_crawl:
    new_programs_found = set()
    for program in programs_to_crawl:
        new_programs_found.update(connections[program])

    new_programs_found.difference_update(group)
    group.update(new_programs_found)
    programs_to_crawl = new_programs_found

print(len(group))
