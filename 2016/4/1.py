from collections import Counter

rooms = []
while True:
    try:
        line = input()
    except EOFError:
        break

    name_and_room_id, checksum = line.split('[')
    *name_pieces, room_id = name_and_room_id.split('-')

    rooms.append(
        (
            ''.join(name_pieces),
            int(room_id),
            checksum[ : -1 ] # exclude final ]
        )
    )

print(
    sum(
        room_id
        for name, room_id, checksum in rooms
        if checksum == ''.join(
            letter
            for letter, _ in Counter(sorted(name)).most_common(5)
        )
    )
)
