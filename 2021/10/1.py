lines = []
while True:
    try:
        line = input()
    except EOFError:
        break

    lines.append(line)

bad_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,   
}

matching_brackets = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

def get_bad_score(line):
    openers = []
    for char in line:
        if char in '([{<':
            openers.append(char)
        elif char in ')]}>':
            if openers[-1] == matching_brackets[char]:
                openers.pop()
            else:
                return bad_scores[char]

    return 0

print(sum(get_bad_score(line) for line in lines))
