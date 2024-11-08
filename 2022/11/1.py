monkeys = []
monkey_inventories = []
while True:
    try:
        monkey_id = int(input()[:-1].split(' ')[1])
        starting_items = list(map(int, input().split(': ')[1].split(', ')))
        operation = input().split(': ')[1]
        test = int(input().split(' ')[-1])
        target_when_true = int(input().split(' ')[-1])
        target_when_false = int(input().split(' ')[-1])
        input()
    except EOFError:
        break
    finally:
        monkeys.append((
            operation,
            test,
            (target_when_false, target_when_true)
        ))
        monkey_inventories.append(starting_items)

inspections = [0] * len(monkeys)
for _ in range(20):
    for i, monkey in enumerate(monkeys):
        operation, test, targets = monkey
        items = monkey_inventories[i]

        if not items:
            continue

        inspections[i] += len(items)

        for worry in items:
            operation_context = {'old': worry}
            exec(operation, None, operation_context)
            worry = operation_context['new'] // 3

            test_passed = not worry % test
            target_monkey = targets[test_passed]
            monkey_inventories[target_monkey].append(worry)

        items.clear()

inspections.sort()
print(inspections[-2] * inspections[-1])
