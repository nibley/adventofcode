stream = input()

for i in range(len(stream) - 13):
    unique_chars = set()
    for j in range(14):
        unique_chars.add(stream[ i + j ])

    if len(unique_chars) == 14:
        print(i + 14)
        break
