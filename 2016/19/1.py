def white_elephant(active_elves):
    elves = list(range(1, active_elves + 1))
    was_odd = False
    while True:
        active_elves = len(elves)

        if active_elves == 1:
            return elves[0]
        elif active_elves == 2:
            if was_odd:
                return elves[1]
            else:
                return elves[0]
        
        if was_odd:
            # if the previous round had odd # elves then
            # the last elf needs a chance to take the first
            elves = [elves[-1]] + elves[:-1]
        elves = elves[::2]

        was_odd = active_elves % 2

num_elves = int(input())
print(white_elephant(num_elves))
