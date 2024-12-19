patterns = input().split(', ')
input()

designs = []
while True:
    try:
        line = input()
    except EOFError:
        break

    designs.append(line)

def valid(design):
    if not design:
        return True

    return any(
        valid(design[ len(pattern) : ])
        for pattern in patterns
        if design[ : len(pattern) ] == pattern
    )

print(sum(map(valid, designs)))
