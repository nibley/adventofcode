from collections import defaultdict

connections = defaultdict(set)
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, right_side = line.split(' <-> ')
    program = int(left_side)
    connected_programs = map(int, right_side.split(', '))
    connections[program].update(connected_programs)

def crawl_group(program):
    group = set([program])
    programs_to_crawl = [program]
    while True:
        found_new_program = False
        new_programs_to_crawl = set()
        for program in programs_to_crawl:
            for connected_program in connections[program]:
                if connected_program not in group:
                    found_new_program = True
                    new_programs_to_crawl.add(connected_program)

        if not found_new_program:
            break

        group.update(new_programs_to_crawl)
        programs_to_crawl = new_programs_to_crawl

    return tuple(group)

groups = set()
for program in connections.keys():
    group_containing_program = None
    for group in groups:
        if program in group:
            group_containing_program = group
            break
    
    if group_containing_program is not None:
        continue

    # don't yet know about the group containing this program 
    new_group = crawl_group(program)
    print(f'Found group {new_group}')
    groups.add(new_group)

print()
print(len(groups))
