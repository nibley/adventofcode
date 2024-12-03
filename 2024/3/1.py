from operator import mul
import re

pattern = r'mul\((\d+),(\d+)\)'

def get(line):
    return sum(
        int(a) * int(b)
        for a, b in re.findall(pattern, line)
    )
    # return 0

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break

    lines.append(
        line
    )

# total = 0
# for line in lines:
#     if (

#     ):
#         total += 1



print(
    sum(
        get(line)
        for line in lines
    )
)
