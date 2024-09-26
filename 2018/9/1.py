pieces = input().split(' ')
num_players = int(pieces[0])
num_marbles = int(pieces[6]) + 1

marbles = [0]
scores = { i : 0 for i in range(num_players) }
current_player = 0
current_position = 0
for i in range(1, num_marbles + 1):
    if i % 23 == 0:
        current_position = (current_position - 7) % len(marbles)
        scores[current_player] += i + marbles[current_position]
        del marbles[current_position]
    else:
        current_position = (current_position + 1) % len(marbles) + 1
        marbles.insert(current_position, i)

    current_player = (current_player + 1) % num_players

print(sorted(scores.values())[-1])
