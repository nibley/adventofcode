import itertools
import math

banks = []

while True:
    try:
        line = input()
        bank = tuple(map(int, line))
        banks.append(bank)
    except EOFError:
        break

def get_max_for_bank(bank):
    max_score = -1 * math.inf
    for i, first_value in enumerate(bank):
        for second_value in bank[ i + 1 : ]:
            bank_score = 10 * first_value + second_value
            if bank_score > max_score:
                max_score = bank_score
    
    return max_score

total = 0
for bank in banks:
    total += get_max_for_bank(bank)

print(total)
