phrases = []
while True:
    try:
        line = input()
    except EOFError:
        break

    phrases.append(
        tuple(
            tuple(sorted(word))
            for word in line.split()
        )
    )

print(
    sum(
        len(phrase) == len(set(phrase))
        for phrase in phrases
    )
)
