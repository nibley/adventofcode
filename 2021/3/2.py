from collections import defaultdict

numbers = []
while True:
    try:
        line = input()
    except EOFError:
        break

    numbers.append(line)

def bit_frequencies(i, numbers):
    frequencies = [0, 0]

    for number in numbers:
        char = int(number[i])
        frequencies[char] += 1

    return frequencies

string_length = len(numbers[0])

oxygen_search_pool = numbers[:]
for i in range(string_length):
    if len(oxygen_search_pool) > 1:
        zero_frequency, one_frequency = bit_frequencies(i, oxygen_search_pool)

        oxygen_search_pool = [
            number for number in oxygen_search_pool
            if number[i] == 
                ('0' if zero_frequency > one_frequency else '1')
        ]

co2_search_pool = numbers[:]
for i in range(string_length):
    if len(co2_search_pool) > 1:
        zero_frequency, one_frequency = bit_frequencies(i, co2_search_pool)

        co2_search_pool = [
            number for number in co2_search_pool
            if number[i] == 
                ('1' if zero_frequency > one_frequency else '0')
        ]
    
assert len(oxygen_search_pool) == 1
assert len(co2_search_pool) == 1

oxygen = int(oxygen_search_pool[0], 2)
co2 = int(co2_search_pool[0], 2)
print(oxygen * co2)
