passwords = []
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, password = line.split(': ')
    letter_range, letter = left_side.split(' ')
    range_start, range_end = map(int, letter_range.split('-'))

    passwords.append( (range_start, range_end, letter, password) )

num_valid_passwords = 0
for range_start, range_end, letter, password in passwords:
    letter_count = password.count(letter)
    if range_start <= letter_count <= range_end:
        num_valid_passwords += 1

print(num_valid_passwords)
