from re import finditer

def increment_password(password):
    result = ''

    # true initially triggers the first low-digit increment
    carry = True
    for c in reversed(password):
        if carry and c == 'z':
            result = 'a' + result
            carry = True
        else:
            result = (chr(ord(c) + 1) if carry else c) + result
            carry = False

    return result

def is_valid_password(password):
    for c in password:
        if c in 'iol':
            return False

    doubles = list(finditer(r'([a-z])\1\1?', password))
    if not len(doubles) >= 2:
        return False

    for window in zip(
        password[    : -2 ],
        password[  1 : -1 ],
        password[  2 :    ]
    ):
        first_ascii, second_ascii, third_ascii = map(ord, window)
        if (
            third_ascii - second_ascii == 1
            and second_ascii - first_ascii == 1
        ):
            return True

    return False

password = input()
for _ in range(2):
    while not is_valid_password(password):
        password = increment_password(password)

print(password)
