passwords = []
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, password = line.split(': ')
    letter_range, letter = left_side.split(' ')
    first_position, second_position = map(int, letter_range.split('-'))

    passwords.append( (first_position, second_position, letter, password) )

num_valid_passwords = 0
for first_position, second_position, letter, password in passwords:
    test_positions = [
        password[first_position - 1], 
        password[second_position - 1]]
    letter_count = test_positions.count(letter)
    if letter_count == 1:
        num_valid_passwords += 1

print(num_valid_passwords)
