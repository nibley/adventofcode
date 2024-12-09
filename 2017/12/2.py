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

def crawl_group(starting_program):
    group = set([starting_program])
    programs_to_crawl = group
    while programs_to_crawl:
        new_programs_found = set()
        for program in programs_to_crawl:
            new_programs_found.update(connections[program])

        new_programs_found.difference_update(group)
        group.update(new_programs_found)
        programs_to_crawl = new_programs_found

    return group

num_groups = 1
grouped_programs = crawl_group(0)
ungrouped_programs = set(connections).difference(grouped_programs)
while ungrouped_programs:
    num_groups += 1
    grouped_programs.update(crawl_group(ungrouped_programs.pop()))
    ungrouped_programs.difference_update(grouped_programs)

print(num_groups)
