from math import lcm

monkeys = []
monkey_inventories = []
while True:
    input()

    *_, starting_items = input().split(': ')
    *_, operation = input().split(': ')
    *_, test = input().split()

    *_, target_when_true = input().split()
    *_, target_when_false = input().split()

    test, target_when_false, target_when_true = map(
        int,
        (test, target_when_false, target_when_true)
    )

    monkeys.append(
        (operation, test, (target_when_false, target_when_true))
    )
    monkey_inventories.append(
        list(map(int, starting_items.split(', ')))
    )

    try:
        input()
    except EOFError:
        break

LCM_OF_TESTS = lcm(*tuple( test for _, test, _ in monkeys ))

inspections = [0] * len(monkeys)
for _ in range(10_000):
    for i, (operation, test, targets) in enumerate(monkeys):
        items = monkey_inventories[i]
        if not items:
            continue

        inspections[i] += len(items)

        for worry in items:
            operation_context = {'old': worry}
            exec(operation, None, operation_context)
            worry = operation_context['new'] % LCM_OF_TESTS

            target_monkey = targets[ int(not worry % test) ]
            monkey_inventories[target_monkey].append(worry)

        items.clear()

*_, second_highest, highest = sorted(inspections)
print(highest * second_highest)
