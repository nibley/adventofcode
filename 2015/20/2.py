from math import sqrt, floor

def presents(n):
    # from https://www.geeksforgeeks.org/sum-factors-number/
    # modified for part 2
    if n == 1: 
       return 1
    
    result = 0
    if n <= 50:
        result += 1
    
    for divisor in range(2, int(sqrt(n)) + 1): 
        if n % divisor == 0:
            matching_divisor = n / divisor
            
            if 50 * divisor >= n:
                result += divisor

            if divisor != matching_divisor:
                if 50 * matching_divisor >= n:
                    result += floor(matching_divisor)

    result += n
    return result

goal = int(input()) // 11 + 1
n = 750_000 # close starting point determined by trial and error

while True:
    house_presents = presents(n)
    if house_presents >= goal:
        print(f'{house_presents:_} presents')
        break
    n += 1

print(f'{n:_}')
