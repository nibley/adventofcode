total_nice = 0

def pred_vowels(line):
    return len([c for c in line if c in 'aeiou']) >= 3

def pred_double(line):
    for i, c in enumerate(line[:-1]):
        if line[i + 1] == c:
            return True
    return False

def pred_forbidden(line):
    for forbidden in ['ab', 'cd', 'pq', 'xy']:
        if forbidden in line:
            return False
    return True

preds = [pred_vowels, pred_double, pred_forbidden]
def is_nice(line):
    return all(pred(line) for pred in preds)

while True:
    try:
        line = input()
    except EOFError:
        break
    
    if is_nice(line): total_nice += 1

print(total_nice)
