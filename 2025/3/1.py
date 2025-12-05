import math

banks = []

while True:
    try:
        line = input()
        banks.append(tuple(map(int, line)))
    except EOFError:
        break

def get_max_for_bank(bank):
    score = -1 * math.inf
    for i, first_value in enumerate(bank):
        for second_value in bank[ i + 1 : ]:
            bank_score = 10 * first_value + second_value
            if bank_score > score:
                score = bank_score
    
    return score

print(sum(map(get_max_for_bank, banks)))
