def pred_double_pair(line):
    pairs = set()
    for i, char in enumerate(line[:-1]):
        pair = char + line[i + 1]

        if pair not in pairs:
            pairs.add(pair)
            continue

        if (
            pair != line[i - 1 : i + 1]
            or pair == line[i - 2 : i]
        ):
            return True

    return False

def pred_gap_repeat(line):
    for i, char in enumerate(line[:-2]):
        if char == line[i + 2]:
            return True

    return False

preds = [pred_double_pair, pred_gap_repeat]
total_nice = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    if all(pred(line) for pred in preds):
        total_nice += 1

print(total_nice)
