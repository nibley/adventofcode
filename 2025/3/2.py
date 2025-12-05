banks = []

while True:
    try:
        line = input()
        banks.append(tuple(map(int, line)))
    except EOFError:
        break

def get_max_for_bank(bank):
    score = 0

    cursor = 0
    limit = len(line) - 12 # next battery choice can't be past here
    for _ in range(12):
        i, battery = max(
            enumerate(bank[ cursor : limit + 1 ]),
            key = lambda pair: pair[1]
        )
        score *= 10
        score += battery

        limit += 1
        cursor += i + 1
    
    return score

print(sum(map(get_max_for_bank, banks)))
