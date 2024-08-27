from collections import defaultdict

def parse():
    unparsed_bots = list(bot_destinations.keys())
    while unparsed_bots:
        to_remove = []
        for bot in unparsed_bots:
            chips = bot_chips[bot]
            if len(chips) == 2:
                low_chip, high_chip = sorted(chips)
                low_destination, high_destination = bot_destinations[bot]

                bot_chips[low_destination].add(low_chip)
                bot_chips[high_destination].add(high_chip)
                to_remove.append(bot)
        while to_remove:
            parsed_bot = to_remove.pop()
            unparsed_bots.remove(parsed_bot)
        for bot, chips in bot_chips.items():
            if 61 in chips and 17 in chips:
                print()
                print(bot)
                return


bot_chips = defaultdict(set)
bot_destinations = defaultdict(list)
while True:
    try:
        line = input()
    except EOFError:
        break

    if line.startswith('value '):
        pieces = line.split(' goes to bot ')
        chip = int(pieces[0].split(' ')[1])
        bot = int(pieces[1])
        bot_chips[bot].add(chip)
    else:
        pieces = line.split(' gives ')
        bot = int(pieces[0].split(' ')[1])
        
        destinations = pieces[1].split(' and ')
        low_destination = destinations[0].split(' ')
        high_destination = destinations[1].split(' ')
        bot_destinations[bot] = [int(low_destination[-1]), int(high_destination[-1])]

parse()
