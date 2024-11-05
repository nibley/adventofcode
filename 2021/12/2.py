from collections import defaultdict

edges = defaultdict(list)
while True:
    try:
        line = input()
    except EOFError:
        break

    start, end = line.split('-')

    if end != 'start':
        edges[start].append(end)
    if start != 'start':
        edges[end].append(start)

def count_paths(start, path=None, repeat_cave=None):
    if start == 'end':
        return 1

    if path is None:
        path = tuple()
    
    if start.islower():
        start_visits = path.count(start)
        if (
            repeat_cave is None
            and start_visits == 1
        ):
            repeat_cave = start
        elif (
            (start == repeat_cave and start_visits == 2)
            or start_visits
        ):
            return 0

    choices = edges[start]
    return sum(
        count_paths(choice, path + (start, ), repeat_cave)
        for choice in choices
    )

print(count_paths('start'))
