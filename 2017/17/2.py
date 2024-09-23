from collections import deque

steps = int(input())
buffer = deque([0])
rotation = len(buffer) - 1 - steps
for i in range(1, 50_000_000 + 1):
    buffer.rotate(rotation)
    buffer.append(i)

zero_position = buffer.index(0)
print(buffer[ (zero_position + 1) % len(buffer) ])
