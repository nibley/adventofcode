from math import prod
import re

pattern = r'mul\((\d+),(\d+)\)|(do)\(\)|(don\'t)\(\)'

on = True

def get(line):
    total = 0
    # on = True
    global on
    for match in re.findall(pattern, line):
        if 'do' in match:
            on = True
            print('ON', match, on)
        elif 'don\'t' in match:
            on = False
            print('OFF', match, on)
        else:
            print('  ', match, on)
            if on:
                print('    yes')
                total += prod(
                    int(item)
                    for item in match
                    if item
                )
            else:
                print('    no')

        print()

    return total

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break

    lines.append(
        line
    )

print(
    sum(
        get(line)
        for line in lines
    )
)
