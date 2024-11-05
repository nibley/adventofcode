lines = []
while True:
    try:
        line = input()
    except EOFError:
        break

    lines.append(line)

matching_brackets = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

def line_is_corrupt(line):
    openers = []
    for char in line:
        if char in '([{<':
            openers.append(char)
        elif char in ')]}>':
            if openers[-1] == matching_brackets[char]:
                openers.pop()
            else:
                return True

    return False

good_scores = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

def get_good_score(line):
    openers = []
    for char in line:
        if char in '([{<':
            openers.append(char)
        elif char in ')]}>':
            if openers[-1] == matching_brackets[char]:
                openers.pop()
            else:
                break

    score = 0
    for opener in reversed(openers):
        score *= 5
        score += good_scores[opener]

    return score

scores = sorted(get_good_score(line) for line in lines if not line_is_corrupt(line))
print(scores[ len(scores) // 2 ])
