def hash_algorithm(string):
    result = 0

    for char in string:
        result += ord(char)
        result *= 17
        result %= 256

    return result

print(sum(map(hash_algorithm, input().split(','))))
