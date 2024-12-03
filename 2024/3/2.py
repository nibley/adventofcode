from re import findall
from operator import mul # :)

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break

    lines.append(line)

PATTERN = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
total = 0
enabled = True
for match in findall(PATTERN, ''.join(lines)):
    if match == 'do()':
        enabled = True
    elif match == 'don\'t()':
        enabled = False
    elif enabled:
        total += eval(match)

print(total)
