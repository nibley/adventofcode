monkeys_initial = []
while True:
    try:
        line = input()
    except EOFError:
        break

    monkeys_initial.append(int(line))

MODULUS = 16777216

def secret(value):
    for _ in range(2000):
        value ^= value * 64
        value %= MODULUS

        value ^= value // 32
        value %= MODULUS

        value ^= value * 2048
        value %= MODULUS

    return value

print(sum(map(secret, monkeys_initial)))
