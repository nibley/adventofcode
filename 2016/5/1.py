# modified from 2015 4

import hashlib

secret = input()

n = 1
the_hash = ''
password = ''
while len(password) < 8:
    the_string = f'{secret}{n}'
    the_hash = hashlib.md5(the_string.encode()).hexdigest()
    if the_hash.startswith('00000'):
        password += the_hash[5]
    n += 1

print(password)
