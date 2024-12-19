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
    for pattern in patterns:
        try:
            i = design.index(pattern)
            if i == 0:
                if pattern == design:
                    print('YES')
                    return True

                print(pattern, 'in', design, i)
                recursive = valid(design[ i + len(pattern) : ])
                if recursive:
                    return True
        except ValueError:
            continue

    print('NO')
    return False


total = 0
for design in designs:
# for design in [designs[0]]:
    print(design)
    if valid(design):
        total += 1

    print()

print(total)
