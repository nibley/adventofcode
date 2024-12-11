
from collections import Counter

stones = Counter(map(int, input().split()))

def step(stones):
    result = Counter()
    for stone, count in stones.items():
        if stone == 0:
            result[1] += count
        else:
            stone_string = str(stone)
            stone_length = len(stone_string)

            if stone_length % 2:
                result[stone * 2024] += count
            else:
                half_length = stone_length // 2

                result[int(stone_string[ : half_length ])] += count
                result[int(stone_string[ half_length : ])] += count

    return result

for _ in range(75):
    stones = step(stones)

print(stones.total())
