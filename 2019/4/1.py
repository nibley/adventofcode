range_start, range_end = map(int, input().split('-'))

num_valid_passwords = 0
for password in range(range_start, range_end + 1):
    password = str(password)

    found_double = False
    found_decrease = False
    for i, char in enumerate(password[:-1]):
        next_char = password[i + 1]
        
        if char > next_char:
            found_decrease = True
            break
        
        if char == next_char:
            found_double = True
            continue # can't also be a decrease
        
    if found_double and not found_decrease:
        num_valid_passwords += 1

print(num_valid_passwords)
