from collections import defaultdict

rules = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, right_side = line.split(' contain ')

    outside = left_side[:-5]

    inside = []
    if right_side != 'no other bags.':
        for bag_type in right_side.split(', '):
            number, *rest = bag_type.split(' ')
            number = int(number)
            inside.append( (' '.join(rest[:-1]), number) )

    rules[outside] = inside

bags_to_crawl = { 'shiny gold' : 1 }
total_bags = 0
while bags_to_crawl:
    new_bags_to_crawl = defaultdict(lambda: 0)

    for bag_type, bag_number in bags_to_crawl.items():
        for contents_type, contents_number in rules[bag_type]:
            contents_total = bag_number * contents_number

            total_bags += contents_total
            new_bags_to_crawl[contents_type] += contents_total

    bags_to_crawl = new_bags_to_crawl

print(total_bags)
