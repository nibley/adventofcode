# modified from 2015 4

from hashlib import md5

secret = input()

n = 0
password = [ None for _ in range(8) ]
while not all(password):
    n += 1
    the_hash = md5(f'{secret}{n}'.encode()).hexdigest()

    if the_hash.startswith('00000'):
        i, character, *_ = the_hash[ 5 : 6 + 1 ]
        i = int(i) if i.isnumeric() else None

        if i in range(8) and password[i] is None:
            password[i] = character

print(''.join(password))
