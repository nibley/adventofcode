from functools import cache

codes = {
    'w' : 0,
    'u' : 1,
    'b' : 2,
    'r' : 3,
    'g' : 4
}

patterns = tuple(
    tuple( codes[char] for char in pattern )
    for pattern in input().split(', ')
)
input()

designs = []
while True:
    try:
        line = input()
    except EOFError:
        break

    designs.append(tuple( codes[char] for char in line ))

@cache
def valid(design, previous=()):
    total = 0
    for pattern in patterns:
        if pattern == design:
            # print('YES')
            # yield 1
            # yield previous + (pattern, )
            # return
            total += 1
            continue
        elif design[ : len(pattern) ] == pattern:
            # print(pattern, 'in', design, i)

            recursive = valid(
                design[ len(pattern) : ],
                # previous + (pattern, )
            )
            # for z in recursive:
                # yield z
                # yield 1
            total += recursive
        else:
            continue

    # print('NO')
    # return False
    # return
    return total


total = 0
for design in designs:
# for design in ['gbbr']:
# for design in [designs[0]]:
    print(design)
    # ways = tuple(valid(design))
    res = valid(design)
    # if ways:
        # total += len(ways)

    # for way in ways: print('  ', way)

    # ways = sum( 1 for _ in ways )
    ways = res
    print(ways)
    total += ways
    print()

print(total)

# print(designs)
# print(patterns)
