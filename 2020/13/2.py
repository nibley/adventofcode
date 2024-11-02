from functools import reduce

input()
routes = []
remainders = []
for remainder, route in enumerate(input().split(',')):
    if route != 'x':
        route = int(route)
        routes.append(route)
        remainders.append(route - remainder)

def chinese_remainder_theorem(numbers, remainders):
    # from https://rosettacode.org/wiki/Category:Python

    def multiplicative_inverse(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 1

        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0

        if x1 < 0:
            x1 += b0

        return x1

    total = 0
    product = reduce(lambda a, b: a * b, numbers)
    for number, remainder in zip(numbers, remainders):
        p = product // number
        total += remainder * multiplicative_inverse(p, number) * p

    return total % product

print(chinese_remainder_theorem(routes, remainders))
