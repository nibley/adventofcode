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
        current_passport.extend(piece.split(':') for piece in pieces)
    else:
        passports.append(current_passport)
        current_passport = []

required = set([
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
])

num_valid_passports = 0
for passport in passports:
    valid = True
    passport_keys = set()
    for key, value in passport:
        if key in required:
            passport_keys.add(key)

        if not valid:
            break

        if key == 'cid':
            continue
        elif key == 'byr':
            if len(value) == 4:
                if 1920 <= int(value) <= 2002:
                    continue
        elif key == 'iyr':
            if len(value) == 4:
                if 2010 <= int(value) <= 2020:
                    continue
        elif key == 'eyr':
            if len(value) == 4:
                if 2020 <= int(value) <= 2030:
                    continue
        elif key == 'hgt':
            if value.endswith('cm'):
                if 150 <= int(value[:-2]) <= 193:
                    continue
            elif value.endswith('in'):
                if 59 <= int(value[:-2]) <= 76:
                    continue
        elif key == 'hcl':
            if value[0] == '#':
                if all(char in 'abcdef0123456789' for char in value[1:]):
                    continue
        elif key == 'ecl':
            if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                continue
        elif key == 'pid':
            if len(value) == 9:
                if value.isnumeric():
                    continue
        
        valid = False
    
    if valid and passport_keys == required:
        num_valid_passports += 1

print(num_valid_passports)
