from re import findall
from operator import mul

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break

    lines.append(line)

def parse(match):
    global enabled

    if match == 'do()':
        enabled = True
        return 0
    elif match == 'don\'t()':
        enabled = False
        return 0
    else:
        return eval(match) if enabled else 0

PATTERN = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
enabled = True
print(
    sum(
        map(parse, findall(PATTERN, ''.join(lines)))
    )
)
