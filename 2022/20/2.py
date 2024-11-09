from collections import deque

numbers = deque()
while True:
    try:
        line = input()
    except EOFError:
        break

    numbers.append(811589153 * int(line))

numbers_length = len(numbers)

# manipulate indeces in lieu of numbers to create uniqueness
indeces = deque(range(numbers_length))
for _ in range(10):
    for i, number in enumerate(numbers):
        while indeces[0] != i:
            indeces.rotate(-1)

        indeces.popleft()
        indeces.rotate(-1 * number)
        indeces.appendleft(i)
        indeces.rotate(-1)

zero_index = indeces.index(numbers.index(0))

# rotate indeces so the index corresponding to the *number* 0 is at the front
indeces.rotate(-1 * zero_index)
print(sum(
    numbers[ indeces[(i * 1000) % numbers_length] ]
    for i in range(1, 4)
))
