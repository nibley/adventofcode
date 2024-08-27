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
                
                low_destination_type, low_destination_number = low_destination
                if low_destination_type == 'bot':
                    bot_chips[low_destination_number].add(low_chip)
                else:
                    output_chips[low_destination_number] = low_chip
                
                high_destination_type, high_destination_number = high_destination
                if high_destination_type == 'bot':
                    bot_chips[high_destination_number].add(high_chip)
                else:
                    output_chips[high_destination_number] = high_chip

                to_remove.append(bot)
        while to_remove:
            parsed_bot = to_remove.pop()
            unparsed_bots.remove(parsed_bot)

        if 0 in output_chips and 1 in output_chips and 2 in output_chips:
            print(output_chips[0] * output_chips[1] * output_chips[2])
            return


bot_chips = defaultdict(set)
output_chips = {}
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
        
        pieces = pieces[1].split(' and ')
        low_destination = pieces[0].split(' ')
        high_destination = pieces[1].split(' ')
        bot_destinations[bot] = (
            (low_destination[-2], int(low_destination[-1])),
            (high_destination[-2], int(high_destination[-1]))
        )

parse()
