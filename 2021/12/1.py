from collections import defaultdict

edges = defaultdict(list)
while True:
    try:
        line = input()
    except EOFError:
        break

    start, end = line.split('-')
    edges[start].append(end)
    edges[end].append(start)

def count_paths(start, path=None):
    if start == 'end':
        return 1

    if path is None:
        path = []
    
    if (
        start.islower()
        and start in path
    ):
        return 0

    choices = edges[start]
    return sum(
        count_paths(choice, path + [start])
        for choice in choices
    )

print(count_paths('start'))
