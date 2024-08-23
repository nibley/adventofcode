import hashlib

secret = input()

n = 1
the_hash = ''
while True:
    the_string = f'{secret}{n}'
    the_hash = hashlib.md5(the_string.encode()).hexdigest()
    # print(f'{the_string}\t\t{the_hash}')

    if the_hash.startswith('00000'): break
    n += 1

print(n)
