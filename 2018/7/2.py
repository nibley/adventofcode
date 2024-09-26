required_before = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, right_side = line.split(' must be finished before step ')
    before = left_side.split(' ')[1]
    after = right_side.split(' ')[0]

    required_before.setdefault(before, [])
    required_before.setdefault(after, [])

    required_before[after].append(before)

num_workers = 5
worker_assignments = { i : None for i in range(num_workers) }
worker_timers = [ 0 for i in range(num_workers) ]
t = 0
while required_before:
    for i in range(num_workers):
        if worker_assignments[i]:
            if worker_timers[i] == 1:
                finished_step = worker_assignments[i]
                worker_assignments[i] = None

                del required_before[finished_step]
                for step, required in required_before.items():
                    if finished_step in required:
                        required.remove(finished_step)

            if worker_timers[i] > 0:
                worker_timers[i] -= 1
    
    active_steps = worker_assignments.values()
    available_steps = sorted(
        [ step for step, required \
        in required_before.items() \
        if not required and step not in active_steps ]
    )

    for i in range(num_workers):
        if available_steps and not worker_assignments[i]:
            new_step = available_steps.pop(0)
            worker_assignments[i] = new_step
            worker_timers[i] = 60 + ord(new_step) - 64

    t += 1

print(t - 1)
