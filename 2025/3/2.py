banks = []

while True:
    try:
        line = input()
        banks.append(tuple(map(int, line)))
    except EOFError:
        break

def get_max_for_bank(bank):
    cursor = 0
    limit = len(line) - 12 # next battery choice can't be past here
    batteries = []

    for _ in range(12):
        i, battery = max(
            enumerate(bank[ cursor : limit + 1 ]),
            key = lambda pair: pair[1]
        )
        batteries.append(battery)
        limit += 1
        cursor += i + 1
    
    return int(''.join(map(str, batteries)))

total = 0
for bank in banks:
    total += get_max_for_bank(bank)

print(total)
