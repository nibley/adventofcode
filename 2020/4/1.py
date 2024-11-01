passports = []
current_passport = []
while True:
    try:
        line = input()
    except EOFError:
        passports.append(current_passport)
        break

    if line:
        pieces = line.split(' ')
        current_passport.extend(piece.split(':')[0] for piece in pieces)
    else:
        passports.append(current_passport)
        current_passport = []

required = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]

num_valid_passports = 0
for passport in passports:
    valid = True
    for field in required:
        if field not in passport:
            valid = False
            break
    
    if valid:
        num_valid_passports += 1

print(num_valid_passports)
