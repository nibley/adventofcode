from re import sub

lines = []
while True:
    try:
      line = input()
    except EOFError:
        break

    lines.append(line)

len_in_memory = lambda line: len(
    sub(
        r'\\x[a-f0-9]{2}',
        '_',
        line
            .replace(r'\\', '_')
            .replace(r'\"', '_')
    )
) - 2

print(sum( len(line) - len_in_memory(line) for line in lines ))
