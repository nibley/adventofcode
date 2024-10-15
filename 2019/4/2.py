range_start, range_end = map(int, input().split('-'))

num_valid_passwords = 0
for password in range(range_start, range_end + 1):
    password = str(password)

    found_decrease = False
    double_index = None
    for i, char in enumerate(password[:-1]):
        second_char = password[i + 1]

        if char > second_char:
            found_decrease = True
            break

        if char == second_char:
            if (
                double_index is None
                and (i == 0 or char != password[i - 1])
            ):
                double_index = i
            elif double_index == i - 1:
                double_index = None

    if (double_index is not None) and (not found_decrease):
        num_valid_passwords += 1

print(num_valid_passwords)
