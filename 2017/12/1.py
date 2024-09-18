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

programs_in_group = set([0])
programs_to_crawl = [0]
while True:
    found_new_program = False

    new_programs_to_crawl = set()
    for program in programs_to_crawl:
        for connected_program in connections[program]:
            if connected_program not in programs_in_group:
                found_new_program = True
                new_programs_to_crawl.add(connected_program)

    if not found_new_program:
        break

    programs_in_group.update(new_programs_to_crawl)
    programs_to_crawl = new_programs_to_crawl

print(len(programs_in_group))
