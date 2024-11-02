from collections import defaultdict
from itertools import product as cartesian_product

program = []
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, right_side = line.split(' = ')

    if left_side != 'mask': # set memory
        left_side = '{:036b}'.format(int(left_side.split('[')[1][ : -1 ]))
        right_side = int(right_side)

    program.append( (left_side, right_side) )

def get_floating_addresses(masked_address):
    floating_indeces = [
        i
        for i, char in enumerate(masked_address)
        if char == 'X'
    ]

    floating_choices = (
        zip(floating_indeces, choice)
        for choice in cartesian_product(
            ('0', '1'),
            repeat=len(floating_indeces)
        )
    )

    for indeces_and_bits in floating_choices:
        realized_address = masked_address[:]
        for i, bit in indeces_and_bits:
            realized_address[i] = bit

        yield int(''.join(realized_address), 2)

memory = defaultdict(lambda: 0)
mask = None
for operation, argument in program:
    if operation == 'mask': # set mask
        mask = argument
    else: # set memory
        assert mask is not None

        masked_address = [
            bit if mask_bit == '0' else mask_bit
            for bit, mask_bit in zip(operation, mask)
        ]
        for realized_address in get_floating_addresses(masked_address):
            memory[realized_address] = argument

print(sum(memory.values()))
