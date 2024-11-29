def presents(n):
    # from https://www.geeksforgeeks.org/sum-factors-number/
    # modified for part 2

    if n == 1:
       return 1

    result = 0
    if n <= 50:
        result += 1

    for divisor in range(2, int(n ** 0.5) + 1):
        quotient, remainder = divmod(n, divisor)
        if not remainder:
            if 50 * divisor >= n:
                result += divisor

            if divisor != quotient and 50 * quotient >= n:
                result += quotient

    result += n
    return result

goal = int(input()) // 11 + 1
n = 750_000 # close starting point determined by trial and error
while presents(n) < goal:
    n += 1

print(n)
