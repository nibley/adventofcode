from functools import cache

patterns = input().split(', ')
input()

designs = []
while True:
    try:
        line = input()
    except EOFError:
        break

    designs.append(line)

@cache
def ways(design):
    if not design:
        return 1

    return sum(
        ways(design[ len(pattern) : ])
        for pattern in patterns
        if design[ : len(pattern) ] == pattern
    )

print(sum(map(ways, designs)))
