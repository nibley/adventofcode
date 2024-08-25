from math import sqrt

def presents(n):
    # from https://www.geeksforgeeks.org/sum-factors-number/
    if n == 1: 
       return 1
    result = 1
    for i in range(2, int(sqrt(n)) + 1): 
        if n % i == 0:
            if i == (n / i):
                result += i 
            else:
                result += i + n//i
    return result + n

goal = int(int(input()) / 10)
n = 500_000 # close starting point determined by trial and error
while True:
    house_presents = presents(n)
    if house_presents >= goal:
        print(f'{house_presents:_} presents')
        break
    n += 1

print(f'{n:_}')
