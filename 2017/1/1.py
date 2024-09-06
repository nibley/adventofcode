raw = input()
digits = list(map(int, raw))
digits_length = len(digits)
total = 0
for i, digit in enumerate(digits[:-1]):
    if digit == digits[i + 1]:
        total += digit

if digits[-1] == digits[0]:
    total += digits[-1]

print(total)
