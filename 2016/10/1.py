from collections import defaultdict

bot_chips = defaultdict(set)
destinations = defaultdict(list)
while True:
    try:
        line = input()
    except EOFError:
        break

    first_word, *rest = line.split()
    if first_word == 'value':
        chip, *_, bot = rest
        chip, bot = map(int, (chip, bot))
        bot_chips[bot].add(chip)
    else:
        (
            bot, _, _, _, _,
            low_destination, _, _, _, _,
            high_destination
        ) = rest
        bot, low_destination, high_destination = map(
            int,
            (bot, low_destination, high_destination)
        )
        destinations[bot] = (low_destination, high_destination)

def find_goal():
    bots_to_scan = set(destinations.keys())
    while bots_to_scan:
        bots_scanned = set()

        for bot in bots_to_scan:
            chips = bot_chips[bot]

            if len(chips) == 2:
                low_chip, high_chip = sorted(chips)
                low_destination, high_destination = destinations[bot]

                bot_chips[low_destination].add(low_chip)
                bot_chips[high_destination].add(high_chip)

                bots_scanned.add(bot)

        bots_to_scan.difference_update(bots_scanned)

        for bot, chips in bot_chips.items():
            if {61, 17}.issubset(chips):
                return bot

    assert False

print(find_goal())
