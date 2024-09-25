total = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    delta = int(line)
    total += delta

print(total)
