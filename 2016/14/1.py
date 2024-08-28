from hashlib import md5
from functools import cache

@cache
def get_hash(i):
    return md5(f'{salt}{i}'.encode()).hexdigest()

def triple_in_hash(i):
    the_hash = get_hash(i)
    for i in range(len(the_hash) - 2):
        char = the_hash[i]
        if char == the_hash[i + 1] == the_hash[i + 2]:
            return char
    
    return False

def quintuple_in_next_thousand(i, char):
    quint = char * 5
    for j in range(1000):
        the_hash = get_hash(i + j + 1)
        if quint in the_hash:
            return True
    
    return False

salt = input()
indices = []
i = 0
while len(indices) < 64:
    char = triple_in_hash(i)
    if char:
        if quintuple_in_next_thousand(i, char):
            indices.append(i)

    i += 1

print(indices[-1])
