from collections import defaultdict

frequences = defaultdict(lambda: defaultdict(lambda: 0))
while True:
    try:
        line = input()
    except EOFError:
        break

    for i, char in enumerate(line):
        frequences[i][char] += 1

print(
    ''.join(
        max(chars, key=chars.get)
        for i, chars in sorted(frequences.items())
    )
)
