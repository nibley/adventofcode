'''
1
1

1 2
1

1 2 3
1 3
3

1 2 3 4
1 2 4
1 2
1

1 2 3 4 5
1 2 4 5
1 2 4
2 4
2

1 2 3 4 5 6
1 2 3 5 6
1 2 3 6
2 3 6
3 6
3

floor(len(elves) / 2) + elf_index
'''

from math import floor
from functools import cache

# entering solutions for various num_elves into
# The On-Line Encyclopedia of Integer Sequences
# revealed that the problem is https://oeis.org/A334473

def white_elephant(active_elves):
    elves = list(range(1, active_elves + 1))
    elf_index = 0
    global num_elves
    while True:
        if num_elves == 1:
            return elves[0]

        # print(f'{elves} {elf_index}: {elves[elf_index]}')

        victim_index = (elf_index + floor(num_elves / 2)) % num_elves

        # print(f'elf {elves[elf_index]} takes elf {elves[victim_index]}')

        del elves[victim_index]
        num_elves -= 1

        if elf_index < victim_index:
            elf_index += 1
        elf_index = elf_index % num_elves

        # print(num_elves)

@cache
def try2(num_elves):
    print(f'{num_elves} elves')

    if num_elves == 1:
        # print(f'  base {0}')
        return 0
    
    if num_elves == 2:
        # print(f'  base {0}')
        return 0
    
    if num_elves == 3:
        # print(f'  base {2}')
        return 2
    
    elf_index = 0
    victim_index = (elf_index + floor(num_elves / 2)) % num_elves
    print(f'  victim {victim_index}')
    prev_case_winner_index = try2(num_elves - 1)
    print(f'  prev {prev_case_winner_index}')
    elf_index_next = elf_index + 1
    if elf_index_next >= victim_index:
        elf_index_next += 1
    print(f'  next {elf_index_next}')


    

# num_elves = int(input())

for num_elves in range(4, 5):
# for num_elves in [5]:
# for num_elves in [num_elves]:
    # print(f'{num_elves}:\t{white_elephant(num_elves)}')
    try2(num_elves)
    print()
