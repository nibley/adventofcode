from collections import defaultdict

_, initial_state = input().split(': ')
pots = defaultdict(
    lambda: False,
    {
        i : char == '#'
        for i, char in enumerate(initial_state)
    }
)
input()

rules = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    before, after = line.split(' => ')
    before = tuple( char == '#' for char in before )
    rules[before] = (after == '#')

def simulate_generation(pots):
    pots_next = defaultdict(lambda: False)
    for i in range(-2, len(pots) + 2):
        neighborhood = tuple(
            pots[i + step]
            for step in range(-2, 2 + 1)
        )
        pots_next[i] = rules[neighborhood]

    return pots_next

for _ in range(20):
    pots = simulate_generation(pots)

print(
    sum(
        i
        for i, pot in pots.items()
        if pot
    )
)
