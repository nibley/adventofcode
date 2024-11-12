from math import log, remainder

numbers = []
while True:
    try:
        line = input()
    except EOFError:
        break

    numbers.append(line)

special_digits = {
    '-': '-1',
    '=': '-2'
}
def snafu_to_decimal(snafu):
    return sum(
        (5 ** i) * int(special_digits.get(char, char))
        for i, char in enumerate(reversed(snafu))
    )

snafu_digits = {
    -2: '=',
    -1: '-',
     0: '0',
     1: '1',
     2: '2'
}
def decimal_to_snafu(decimal):
    snafu = ''

    place_value = 5 ** round(log(decimal, 5))
    while place_value:
        delta_to_multiple = remainder(decimal, place_value)
        place = int((decimal - delta_to_multiple) / place_value)
        decimal = delta_to_multiple

        digit = snafu_digits.get(place)
        assert digit is not None

        if snafu or digit != '0': # prevent leading zeros
            snafu += digit

        place_value //= 5

    return snafu

total_fuel = sum(map(snafu_to_decimal, numbers))
print(decimal_to_snafu(total_fuel))
