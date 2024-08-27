from collections import defaultdict

frequences = defaultdict(lambda: defaultdict(lambda: 0))
while True:
    try:
        line = input()
    except EOFError:
        break
    
    for i, char in enumerate(line):
        frequences[i][char] += 1

message = ''
for i, chars in sorted(frequences.items(), key=lambda item: item[0]):
    message += sorted(chars.items(), key=lambda item: item[1])[-1][0]

print(message)
