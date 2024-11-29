from hashlib import md5

secret = input()

n = 0
the_hash = ''
while not the_hash.startswith('000000'):
    n += 1
    the_hash = md5(f'{secret}{n}'.encode()).hexdigest()

print(n)
