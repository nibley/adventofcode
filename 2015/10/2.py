from itertools import groupby

current = input()

for _ in range(50):
    current = ''.join(
        f'{sum(1 for _ in group)}{key}'
        for key, group in groupby(current)
    )

print(len(current))
