displays = []
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, right_side = line.split(' | ')
    
    patterns = {}
    for pattern_raw in left_side.split(' '):
        pattern = set(pattern_raw)
        length = len(pattern)
        patterns.setdefault(length, [])
        patterns[length].append(pattern)

    digits = right_side.split(' ')
    displays.append( (patterns, digits) )

total = 0
for patterns, digits in displays:
    wires = {}
    
    # set unambiguous patterns
    wire_one = patterns.pop(2)[0]
    wires[ tuple(sorted(wire_one)) ] = 1

    wire_four = patterns.pop(4)[0]
    wires[ tuple(sorted(wire_four)) ] = 4
    
    wire_seven = patterns.pop(3)[0]
    wires[ tuple(sorted(wire_seven)) ] = 7
    
    wire_eight = patterns.pop(7)[0]
    wires[ tuple(sorted(wire_eight)) ] = 8

    # 3 is a superset of 1
    wire_three = next(
        pattern
        for pattern in patterns[5]
        if pattern.issuperset(wire_one)
    )
    wires[tuple(sorted(wire_three))] = 3
    patterns[5].remove(wire_three)

    # 5 is a superset of 4 - 1
    in_four_not_one = wire_four.difference(wire_one)
    wire_five = next(
        pattern
        for pattern in patterns[5]
        if pattern.issuperset(in_four_not_one)
    )
    wires[tuple(sorted(wire_five))] = 5
    patterns[5].remove(wire_five)

    # 2 is unambiguous now
    wire_two = patterns.pop(5)[0]
    wires[tuple(sorted(wire_two))] = 2

    # 0 is the only one that is not a superset of 5 
    wire_zero = next(
        pattern
        for pattern in patterns[6]
        if not pattern.issuperset(wire_five)
    )
    wires[tuple(sorted(wire_zero))] = 0
    patterns[6].remove(wire_zero)

    # 9 is a superset of 1
    wire_nine = next(
        pattern
        for pattern in patterns[6]
        if pattern.issuperset(wire_one)
    )
    wires[tuple(sorted(wire_nine))] = 9
    patterns[6].remove(wire_nine)

    # 6 is the only digit left
    wire_six = patterns.pop(6)[0]
    wires[tuple(sorted(wire_six))] = 6

    total += int(
        ''.join(
            str(wires[ tuple(sorted(digit)) ])
            for digit in digits
        )
    )

print(total)
