turns = []
while True:
    try:
        line = input()
    except EOFError:
        break

    negative = line[0] == 'L'
    turn = (-1 if negative else 1) * int(line[ 1 : ])
    turns.append(turn)

dial = 50
password = 0
for turn in turns:
    dial += turn
    dial %= 100

    if dial == 0:
        password += 1

print(password)
