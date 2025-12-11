connections = {}

while True:
    try:
        line = input()
    except EOFError:
        break

    server, *outputs = line.replace(':', '').split()
    connections[server] = tuple(outputs)

paths = [ ('you', ) ]
total = 0
while paths:
    current_path = paths.pop()
    current_server = current_path[-1]
    for output in connections[current_server]:
        if output == 'out':
            total += 1
        else:
            paths.append(current_path + (output, ))

print(total)
