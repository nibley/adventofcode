from collections import defaultdict
from math import prod

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
            bot, _, _, _,
            low_type, low_destination, _, _, _,
            high_type, high_destination
        ) = rest
        bot, low_destination, high_destination = map(
            int,
            (bot, low_destination, high_destination)
        )
        destinations[bot] = (
            (low_type, low_destination),
            (high_type, high_destination)
        )

def find_goal():
    bots_to_scan = set(destinations.keys())
    while bots_to_scan:
        bots_scanned = set()

        for bot in bots_to_scan:
            chips = bot_chips[bot]

            if len(chips) == 2:
                for (destination_type, destination), chip in zip(
                    destinations[bot], sorted(chips)
                ): # low and high destinations
                    if destination_type == 'bot':
                        bot_chips[destination].add(chip)
                    else:
                        assert destination not in output_chips
                        output_chips[destination] = chip

                bots_scanned.add(bot)

        bots_to_scan.difference_update(bots_scanned)

        goal_chips = tuple(
            output_chips.get(goal_output) for goal_output in (0, 1, 2)
        )
        if not any(goal_chip is None for goal_chip in goal_chips):
            return prod(goal_chips)

    assert False

output_chips = {}
print(find_goal())
