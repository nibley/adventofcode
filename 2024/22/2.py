from collections import deque, Counter

monkeys_initial = []
while True:
    try:
        line = input()
    except EOFError:
        break

    monkeys_initial.append(int(line))

MODULUS = 16777216

def secret(value):
    value ^= value * 64
    value %= MODULUS

    value ^= value // 32
    value %= MODULUS

    value ^= value * 2048
    value %= MODULUS

    return value

prices = Counter()
for value in monkeys_initial:
    monkey_prices = {}
    memory = deque(maxlen=4)
    last_price = value % 10

    for _ in range(2000 - 1):
        value = secret(value)

        price = value % 10
        memory.append(price - last_price)

        if len(memory) == 4:
            monkey_prices.setdefault(tuple(memory), price)

        last_price = price

    prices.update(monkey_prices)

(_, highest_bananas), *_ = prices.most_common(1)
print(highest_bananas)
