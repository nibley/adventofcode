raw = input()
digits = list(map(int, raw))
digits_length = len(digits)
half_length = len(digits) // 2
total = 0
for i, digit in enumerate(digits):
    if digit == digits[(i + half_length) % digits_length]:
        total += digit

print(total)
