lines = []
while True:
    try:
        line = input()
    except EOFError:
        break

    lines.append(
        tuple(int(item) for item in line.split())
    )

total = 0
for line in lines:
    bad = False
    increasing = False
    decreasing = False
    for item, two in zip(line[ : -1], line[ 1 : ]):
        if not increasing and not decreasing:
            if two > item:
                increasing = True
            elif item > two:
                decreasing = True
        if increasing:
            if two <= item:
                bad = True
        if decreasing:
            if two >= item:
                bad = True
        if not 1 <= abs(two - item) <= 3:
            bad = True

    if not bad:
        total += 1

print(total)
