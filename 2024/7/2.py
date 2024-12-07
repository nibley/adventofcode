from operator import add, mul
from collections import deque
# from itertools import permutations
from itertools import product

def concat(a, b):
    return int(str(a) + str(b))

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break

    first, rest = line.split(': ')
    # print(first)
    # print(rest)
    # print()
    nums = tuple(map(int, rest.split()))
    # print(nums)

    lines.append(
        (
            # first, deque(nums)
            int(first), nums
        )
    )

def valid(line):
    first, nums_orig = line
    # for first, nums_orig in lines:
    # print('line', first, nums_orig, len(nums_orig))
    for ops in product((add, mul, concat), repeat=(len(nums_orig) - 1)):
        # print(ops)

        nums = deque(nums_orig)
        # print('  have', first, nums, 'ops', ops)
        # print('  have', first, nums)
        left = nums.popleft()
        # print(left)
        # op, *ops = ops
        while nums:
            right = nums.popleft()
            op, *ops = ops
            left = op(left, right)
            # left = nums.popleft()

        # print('    end', left, type(left), type(first))
        if left == first:
            # print('      yes')
            return True
        else:
            # print('      bad', left, ' '.join(
                # '+' if op == add else '*'
                # for op in ops
            # ))
            pass

    # print('      no')
    return False

total = 0
for i, (first, nums) in enumerate(lines):
    print(i)
# for first, nums in [lines[0]]:
# for first, nums in [lines[1]]:
    if valid((first, nums)):
        # print('\n--- yes---\n')
        total += first

print(total)
