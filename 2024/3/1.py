from re import findall
from operator import mul # :)

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break

    lines.append(line)

PATTERN = r'mul\(\d+,\d+\)'
print(
    sum(
        map(eval, findall(PATTERN, ''.join(lines)))
    )
)
