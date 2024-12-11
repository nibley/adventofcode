from collections import deque

stones = deque(map(int, input().split()))

def step(stones):
    result = deque()

    for stone in stones:
        if stone == 0:
            result.append(1)
        else:
            stone_string = str(stone)
            stone_length = len(stone_string)

            if stone_length % 2:
                result.append(stone * 2024)
            else:
                half_length = stone_length // 2

                result.append(int(stone_string[ : half_length ]))
                result.append(int(stone_string[ half_length : ]))

    return result

for _ in range(25):
    stones = step(stones)

print(len(stones))
