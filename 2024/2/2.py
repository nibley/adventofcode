lines = []
while True:
    try:
        line = input()
    except EOFError:
        break

    lines.append(
        tuple(int(item) for item in line.split())
    )

def valid(line, exclude):
    bad = False
    increasing = False
    decreasing = False
    line = list(line)
    del line[exclude]
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

    return not bad

total = 0
for line in lines:
    if any(
        valid(line, i)
        for i in range(len(line))
    ):
        total += 1

print(total)
