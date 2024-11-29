def presents(n):
    # from https://www.geeksforgeeks.org/sum-factors-number/

    if n == 1:
       return 1

    result = 1
    for divisor in range(2, int(n ** 0.5) + 1):
        quotient, remainder = divmod(n, divisor)
        if not remainder:
            result += divisor

            if divisor != quotient:
                result += quotient

    return result + n

goal = int(input()) // 10
n = 500_000 # close starting point determined by trial and error
while presents(n) < goal:
    n += 1

print(n)
