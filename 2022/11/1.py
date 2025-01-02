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

inspections = [0] * len(monkeys)
for _ in range(20):
    for i, (operation, test, targets) in enumerate(monkeys):
        items = monkey_inventories[i]
        if not items:
            continue

        inspections[i] += len(items)

        for worry in items:
            operation_context = {'old': worry}
            exec(operation, None, operation_context)
            worry = operation_context['new'] // 3

            target_monkey = targets[ int(not worry % test) ]
            monkey_inventories[target_monkey].append(worry)

        items.clear()

*_, second_highest, highest = sorted(inspections)
print(highest * second_highest)
