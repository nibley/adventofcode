from collections import defaultdict

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break

    parse_side = lambda side: tuple(
        int(coord)
        for coord in side.split(',')
    )
    lines.append( map(parse_side, line.split(' -> ')) )

def trace_line(line):
    line_start, line_end = line
    if line_start[0] == line_end[0]:
        x = line_start[0]
        range_start, range_end = sorted([line_start[1], line_end[1]])
        for i in range(range_start, range_end + 1):
            histogram[(x, i)] += 1
    elif line_start[1] == line_end[1]:
        y = line_start[1]
        range_start, range_end = sorted([line_start[0], line_end[0]])
        for i in range(range_start, range_end + 1):
            histogram[(i, y)] += 1
    else:
        line_start, line_end = sorted(
            [line_start, line_end],
            key=lambda pair: pair[0]
        )
        y_direction = 1 if line_start[1] < line_end[1] else -1
        for i in range(line_end[0] - line_start[0] + 1):
            histogram[
                (line_start[0] + i, line_start[1] + y_direction * i)
            ] += 1


histogram = defaultdict(lambda: 0)

for line in lines:
    trace_line(line)

print(len([ k for k, count in histogram.items() if count >= 2 ]))
