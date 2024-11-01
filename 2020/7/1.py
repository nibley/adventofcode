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
            _, *color, _ = bag_type.split(' ')
            inside.append(' '.join(color))

    rules[outside] = inside

my_bag = 'shiny gold'
del rules[my_bag] # because we only want the outermost

bags_to_crawl = [my_bag]
useful_bags = set()
while bags_to_crawl:
    new_bags_to_crawl = []
    for bag in bags_to_crawl:
        for candidate_bag in rules:
            if candidate_bag in useful_bags:
                continue # already know about it

            if bag in rules[candidate_bag]:
                new_bags_to_crawl.append(candidate_bag)
                useful_bags.add(candidate_bag)

    bags_to_crawl = new_bags_to_crawl

print(len(useful_bags))
