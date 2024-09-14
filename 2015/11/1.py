import re

def increment_password(password):
    reversed_password = reversed(password)
    result = ''
    # true initially triggers the first low-digit increment
    carry = True
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

password = input()
while not is_valid_password(password):
    password = increment_password(password)

print(password)
