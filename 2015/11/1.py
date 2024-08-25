import re
import os

def increment_password(password):
    reversed_password = reversed(password)
    result = ''
    carry = True # true initially triggers the low-digit increment
    for c in reversed_password:
        if carry and c == 'z':
            result = 'a' + result
            carry = True
        else:
            result = (increment_character(c) if carry else c) + result
            carry = False            
    return result

def increment_character(character):
    """ don't pass 'z' """
    return chr(ord(character) + 1)

def is_valid_password(password):
    for forbidden in 'iol':
        if forbidden in password:
            return False
    
    doubles = list(re.finditer(r'([a-z])\1\1?', password))
    if len(doubles) <= 1:
        return False

    for i, c in enumerate(password[:-2]):
        window = password[i:i+3]
        if ord(window[2]) - ord(window[1]) == 1:
            if ord(window[1]) - ord(window[0]) == 1:
                return True
    
    return False

password = ''
if not os.path.isfile('passwords.txt'):
    password = input()
    with open('passwords.txt', 'w') as passwords_file:
        for i in range(1000000):
            password = increment_password(password)
            passwords_file.write(f'{password}\n')

with open('passwords.txt', 'r') as passwords_file:
    for line in passwords_file:
        if is_valid_password(line):
            print(line)
            break
