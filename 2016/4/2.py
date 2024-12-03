from string import ascii_lowercase

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

def rotate(letter, room_id):
    letter_index = ascii_lowercase.index(letter)
    return ascii_lowercase[ (letter_index + room_id) % 26 ]

print(
    next(
        room_id
        for name, room_id, checksum in rooms
        if 'north' in ''.join( # decryption
            rotate(letter, room_id)
            for letter in name
        )
    )
)
