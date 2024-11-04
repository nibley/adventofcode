fish_initial = [ int(n) for n in input().split(',') ]
fish_by_timer = { timer_value : 0 for timer_value in range(9) }

for fish in fish_initial:
    fish_by_timer[fish] += 1

days = 256
for _ in range(days):
    next_generation= { timer_value : 0 for timer_value in range(9) }
    for timer_value in range(1, 9):
        num_fish = fish_by_timer[timer_value]
        next_generation[(timer_value - 1) % 8] = num_fish
    next_generation[8] += fish_by_timer[0]
    next_generation[6] += fish_by_timer[0]

    fish_by_timer = next_generation

print(sum(fish_by_timer.values()))
