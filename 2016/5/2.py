# modified from 2015 4

import hashlib

secret = input()

n = 1
the_hash = ''
password = [None] * 8
while None in password:
    the_string = f'{secret}{n}'
    the_hash = hashlib.md5(the_string.encode()).hexdigest()
    if the_hash.startswith('00000'):
        position_char = the_hash[5]
        if position_char in '01234567':
            position = int(position_char)
            if password[position] is None:
                password[position] = the_hash[6]
                print(password)
    n += 1

print()
print(''.join(password))
