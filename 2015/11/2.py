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
    if len(doubles) < 2:
        return False

    for i, c in enumerate(password[:-2]):
        first_char_code = ord(password[i])
        second_char_code = ord(password[i + 1])
        third_char_code = ord(password[i + 2])
        if (
            second_char_code - first_char_code == 1
            and third_char_code - second_char_code == 1
        ):
            return True

    return False

password = input()
found_one_password = False
while True:
    if is_valid_password(password):
        if found_one_password:
            print(password)
            break
        else:
            found_one_password = True

    password = increment_password(password)
