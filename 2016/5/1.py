# modified from 2015 4

from hashlib import md5

secret = input()

n = 0
password = ''
while len(password) < 8:
    n += 1
    the_hash = md5(f'{secret}{n}'.encode()).hexdigest()

    if the_hash.startswith('00000'):
        password += the_hash[5]

print(password)
