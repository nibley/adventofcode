# modified from 2023 18

from collections import defaultdict

directions = (
    ( 0, -1),
    ( 1,  0),
    ( 0,  1),
    (-1,  0)
)

grid = defaultdict(lambda: False)
y = 0
start_position = None
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, char in enumerate(line):
        if char in '.S':
            grid[ (x, y) ] = True

            if char == 'S':
                start_position = (x, y)

    y += 1

height = y
width = len(line)

# BFS to find possible positions for successive numbers of steps
positions_to_crawl = set([start_position])
for _ in range(64):
    new_positions_found = set()

    for x, y in positions_to_crawl:
        for x_offset, y_offset in directions:
            neighbor = (x + x_offset, y + y_offset)
            if grid[neighbor]:
                new_positions_found.add(neighbor)

    positions_to_crawl = new_positions_found

def visualize(highlight=()):
    for y in range(height):
        for x in range(width):
            position = (x, y)
            if position in highlight:
                char = 'O'
            elif position == start_position:
                char = 'S'
            elif grid[position]:
                char = '.'
            else:
                char = '#'

            print(char, end='')
        print()
    print()

# visualize(positions_to_crawl)
print(len(positions_to_crawl))
