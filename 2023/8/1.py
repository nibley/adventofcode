from itertools import cycle

turns = cycle(input())
input()

lefts = {}
rights = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    node, neighbors = line.split(' = ')
    left_neighbor, right_neighbor = neighbors[ 1 : -1 ].split(', ')
    lefts[node] = left_neighbor
    rights[node] = right_neighbor

node = 'AAA'
steps = 0
while node != 'ZZZ':
    steps += 1
    node = (lefts if next(turns) == 'L' else rights)[node]

print(steps)
