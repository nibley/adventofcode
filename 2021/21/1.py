player_positions = list(
    int(input().split(' ')[-1]) - 1
    for _ in range(2)
)
player_scores = [0, 0]

die_rolls = 0
def deterministic_die():
    global die_rolls

    while True:
        for i in range(1, 100 + 1):
            die_rolls += 1
            yield i

die = deterministic_die()
done = False
while True:
    for player in range(2):
        steps = sum(next(die) for _ in range(3))

        new_position = (player_positions[player] + steps) % 10
        player_positions[player] = new_position
        player_scores[player] += new_position + 1

        if player_scores[player] >= 1000:
            done = True
            break

    if done:
        break

print(die_rolls * min(player_scores))
