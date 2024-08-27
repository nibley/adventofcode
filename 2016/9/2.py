import re

compressed = input()
pattern = r'\((\d+x\d+)\)'

def uncompressed_length(compressed):
    match = re.search(pattern, compressed)

    if match is None:
        return len(compressed)

    result = 0
    length, repetitions = map(int, match.group(1).split('x'))
    start, end = match.start(), match.end()
    result += len(compressed[:start])
    
    data_region = compressed[end:end + length]
    result += uncompressed_length(data_region) * repetitions

    result += uncompressed_length(compressed[end + length:])

    return result

print(uncompressed_length(compressed))
