rounds = []
while True:
    try:
        line = input()
    except EOFError:
        break

    rounds.append(line)

score = 0
for round_string in rounds:
    round_outcome = round_string[2]
    if round_outcome == 'X':
        win_bonus = 0
    if round_outcome == 'Y':
        win_bonus = 3
    if round_outcome == 'Z':
        win_bonus = 6

    if round_string in ['B X', 'A Y', 'C Z']:
        move_bonus = 1
    if round_string in ['C X', 'B Y', 'A Z']:
        move_bonus = 2
    if round_string in ['A X', 'C Y', 'B Z']:
        move_bonus = 3

    score += win_bonus + move_bonus

print(score)
