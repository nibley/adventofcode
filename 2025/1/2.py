turns = []
while True:
    try:
        line = input()
    except EOFError:
        break

    increment = -1 if line[0] == 'L' else 1
    turn = abs(int(line[ 1 : ]))
    turns.append( (increment, turn) )

dial = 50
password = 0
for increment, turn in turns:
    laps, turn = divmod(turn, 100)
    password += laps

    for i in range(turn):
        dial += increment   
        dial %= 100

        if dial == 0:
            password += 1

print(password)
