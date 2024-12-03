from hashlib import md5
from functools import cache

get_hash = cache(
    lambda i: md5(f'{SALT}{i}'.encode()).hexdigest()
)

def triple_in_hash(i):
    the_hash = get_hash(i)
    for first, second, third in zip(
        the_hash[    : -2 ],
        the_hash[  1 : -1 ],
        the_hash[  2 :    ]
    ):
        if first == second == third:
            return first

    return None

def quintuple_in_next_thousand(i, char):
    goal = char * 5
    for j in range(1000):
        if goal in get_hash(i + j + 1):
            return True

    return False

SALT = input()
i = 0
hits = 0
last_hit = None
while hits < 64:
    char = triple_in_hash(i)
    if char is not None and quintuple_in_next_thousand(i, char):
        hits += 1
        last_hit = i

    i += 1

print(last_hit)
