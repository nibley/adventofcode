from json import dumps

lines = []
while True:
    try:
      line = input()
    except EOFError:
        break

    lines.append(line)

print(sum( len(dumps(line)) - len(line) for line in lines ))
