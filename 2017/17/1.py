steps = int(input())

buffer = [0]
buffer_length = 1
position = 0
for i in range(1, 2017 + 1):
    position = (position + steps + 1) % buffer_length
    buffer_length += 1
    buffer.insert(position, i)

print(buffer[ (position + 1) % buffer_length ])
