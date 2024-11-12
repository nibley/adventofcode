games = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, right_side = line.split(': ')
    game_id = int(left_side.split(' ')[1])

    game = { # keep only maximum numbers seen for each color
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for game_phase in right_side.split('; '):
        color_samples = game_phase.split(', ')
        for color_sample in color_samples:
            amount, color = color_sample.split(' ')
            amount = int(amount)

            if amount > game[color]:
                game[color] = amount

    games[game_id] = game

bag_contents = {
    'red': 12,
    'green': 13,
    'blue': 14
}

total_game_ids = 0
for game_id, game in games.items():
    game_possible = True
    for color in game:
        if game[color] > bag_contents[color]:
            game_possible = False

    if game_possible:
        total_game_ids += game_id

print(total_game_ids)
