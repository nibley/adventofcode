card_public, door_public = (
    int(input())
    for _ in range(2)
)

transform = lambda value, subject: (value * subject) % 20_201_227

value = 1
card_loop_size = 0
while value != card_public:
    card_loop_size += 1
    value = transform(value, 7)

encryption_key = 1
for _ in range(card_loop_size):
    encryption_key = transform(encryption_key, door_public)

print(encryption_key)
