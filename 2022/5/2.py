crates_raw = []
while True:
    line = input()

    if not line.strip().startswith('['):
        input()
        break

    crates_raw.append(line)

num_stacks = len(crates_raw[-1].split(' '))
stacks = [ [] for i in range(num_stacks) ]
for row in reversed(crates_raw):
    for i in range(num_stacks):
        crate = row[ 4 * i : 4 * (i + 1) ][1]
        if crate != ' ':
            stacks[i].append(crate)

instructions = []
while True:
    try:
        line = input()
    except EOFError:
        break

    pieces = line.split(' ')
    num_crates = int(pieces[1])
    source_stack = int(pieces[3])
    destination_stack = int(pieces[5])

    instructions.append( (num_crates, source_stack, destination_stack) )

for num_crates, source_stack, destination_stack in instructions:
    crates_to_move = []
    for _ in range(num_crates):
        crates_to_move.insert(0, stacks[source_stack - 1].pop(-1))

    stacks[destination_stack - 1].extend(crates_to_move)

def visualize():
    tallest_height = sorted(len(stack) for stack in stacks)[-1]
    for row in reversed(range(tallest_height)):
        print(' '.join(
            (f'[{stack[row]}]' if len(stack) > row else '   ')
            for stack in stacks))

    print(' '.join(
        f' {i + 1} '
        for i in range(num_stacks)))

    print()
# visualize()

print(''.join(stack[-1] for stack in stacks))
