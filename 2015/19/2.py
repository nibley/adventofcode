goal_molecule = ''
goal_molecule_length = 0
final_line_next = False
replacements = {}
graph = {}
crawl_queue = []
skipped = set()

total_edges = 0
def add_edge(start, end):
    if len(end) > goal_molecule_length:
        # print('LONG')
        return False

    graph.setdefault(start, [])
    graph[start].append(end)
    global total_edges
    total_edges += 1
    return True
    # print(f'{total_edges} edges')

def mutate_molecule(molecule):
    # if molecule in graph or molecule in skipped:
    
    # if molecule in graph:
        # print('REDUNDANT')
        # return
    
    # if len(molecule) >= goal_molecule_length:
    #     print('LONG', len(molecule), molecule)
    #     skipped.add(molecule)
    #     return

    start_indices = {}
    for start in starts:
        indices = [i for i in range(len(molecule) - len(start) + 1) if molecule[i : i + len(start)] == start]
        start_indices[start] = indices

    for start in starts:
        for start_index in start_indices[start]:
            for end in replacements[start]:
                before_start = molecule[:start_index]
                after_start = molecule[start_index + len(start):]
                new_molecule = f'{before_start}{end}{after_start}'
                
                added_edge = add_edge(molecule, new_molecule)
                if added_edge and new_molecule not in graph:
                    # if len(new_molecule) <= goal_molecule_length:
                        # mutate_molecule(new_molecule)
                        crawl_queue.append(new_molecule)


while True:
    try:
        line = input()
        if final_line_next:
            goal_molecule = line
            goal_molecule_length = len(goal_molecule)
        elif line == '':
            final_line_next = True
        else:
            start, end = line.split(' => ')
            replacements.setdefault(start, [])
            replacements[start].append(end)
    except EOFError:
        break

starts = replacements.keys()

mutate_molecule('e')

# prev_total_edges = 0

while len(crawl_queue):
    crawl_molecule = crawl_queue.pop()
    mutate_molecule(crawl_molecule)
    
    print(total_edges)
    
    # print(total_edges, total_edges - prev_total_edges)
    # prev_total_edges = total_edges

# print(total_edges)
