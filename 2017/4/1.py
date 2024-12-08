phrases = []
while True:
    try:
        line = input()
    except EOFError:
        break

    phrases.append(line.split())

print(
    sum(
        len(phrase) == len(set(phrase))
        for phrase in phrases
    )
)
