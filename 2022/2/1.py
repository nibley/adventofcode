rounds = []
while True:
    try:
        line = input()
    except EOFError:
        break

    rounds.append(line)

score = 0
for round_string in rounds:
    if round_string in ['A Y', 'B Z', 'C X']:
        win_bonus = 6
    if round_string in ['A X', 'B Y', 'C Z']:
        win_bonus = 3
    if round_string in ['A Z', 'B X', 'C Y']:
        win_bonus = 0

    my_move = round_string[2]
    if my_move == 'X':
        move_bonus = 1
    if my_move == 'Y':
        move_bonus = 2
    if my_move == 'Z':
        move_bonus = 3

    score += win_bonus + move_bonus

print(score)
