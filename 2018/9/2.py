from collections import deque

pieces = input().split(' ')
num_players = int(pieces[0])
num_marbles = 100 * int(pieces[6]) + 1

marbles = deque()
scores = { i : 0 for i in range(num_players) }
current_player = 0
for i in range(num_marbles):
    if i % 23 or i == 0:
        marbles.rotate(-2)
        marbles.appendleft(i)
    else:
        marbles.rotate(7 - len(marbles))
        scores[current_player] += i + marbles.popleft()

    current_player = (current_player + 1) % num_players

print(sorted(scores.values())[-1])
