from collections import defaultdict

program = []
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, right_side = line.split(' = ')

    if left_side != 'mask': # set memory
        left_side = int(left_side.split('[')[1][ : -1 ])
        right_side = '{:036b}'.format(int(right_side))

    program.append( (left_side, right_side) )

memory = defaultdict(lambda: 0)
mask = None
for operation, argument in program:
    if operation == 'mask': # set mask
        mask = argument
    else: # set memory
        assert mask is not None

        masked_value = ''.join(
            bit if mask_bit == 'X' else mask_bit
            for bit, mask_bit in zip(argument, mask)
        )
        memory[operation] = int(masked_value, 2)

print(sum(memory.values()))
