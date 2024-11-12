times = [ int(piece) for piece in input().split(':')[1].split(' ') if piece ]
records = [ int(piece) for piece in input().split(':')[1].split(' ') if piece ]
races = zip(times, records)

total = 1
for time, record in races:
    midpoint = time // 2 # list of decisions is symmetric

    first_winning_wait = None
    for wait in range(1, midpoint + 1):
        move_time = time - wait
        distance = move_time * wait

        if distance > record:
            first_winning_wait = wait
            break

    wins_until_midpoint = midpoint - first_winning_wait + 1
    wins = wins_until_midpoint * 2

    if time % 2 == 0:
        wins -= 1 # don't double-count the symmetric middle

    total *= wins

print(total)
