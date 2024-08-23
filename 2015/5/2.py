total_nice = 0

debug_double = ''
debug_gap = ''

def pred_double_pair(line):
    pairs = set()
    for i, c in enumerate(line[:-1]):
        pair = line[i] + line[i+1]
        if pair in pairs:
            # print(' ', pair, line[i-1:i+1])
            if pair != line[i-1:i+1]:
                # print(line, 'doubles', pair)
                global debug_double
                debug_double = pair
                return True
        pairs.add(pair)
    return False

def pred_gap_repeat(line):
    for i, c in enumerate(line[:-2]):
        if c == line[i + 2]:
            # print(line, 'gap', line[i:i+3])
            global debug_gap
            debug_gap = line[i:i+3]
            return True
    return False

preds = [pred_double_pair, pred_gap_repeat]
def is_nice(line):
    return all(pred(line) for pred in preds)

while True:
    try:
        line = input()
    except EOFError:
        break
    
    good = is_nice(line)
    if good:
        total_nice += 1
        print(f'{total_nice}\t{line}\t{debug_double}\t{debug_gap}\n')

print(total_nice)
