from collections import deque

cups = deque()
for digit in input():
    cups.append(int(digit))
num_cups = len(cups)

removed_cups = deque()

for _ in range(100):
    current_cup = cups[0]

    cups.rotate(-1)
    for _ in range(3):
        removed_cups.append(cups.popleft())

    current_cup = num_cups if current_cup == 1 else current_cup - 1
    while current_cup in removed_cups:
        current_cup = num_cups if current_cup == 1 else current_cup - 1

    shift_before_replacing = -1 * (cups.index(current_cup) + 1)
    cups.rotate(shift_before_replacing)
    for _ in range(3):
        cups.appendleft(removed_cups.pop())

    cups.rotate(-1 * shift_before_replacing)

cups.rotate(-1 * cups.index(1))
cups.popleft()
print(''.join(str(digit) for digit in cups))