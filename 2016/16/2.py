TRANSLATION_TABLE = str.maketrans({ '1': '0', '0': '1' })
DISK_LENGTH = 35651584

data = input()
while len(data) < DISK_LENGTH:
    data = '{}0{}'.format(
        data,
        data[ : : -1 ].translate(TRANSLATION_TABLE)
    )

data = data[ : DISK_LENGTH ]

def checksum(data):
    result = ''.join(
        '1' if first == second else '0'
        for first, second in zip(
            data[    : -1 :  2 ],
            data[  1 :    :  2 ]
        )
    )

    return result if len(result) % 2 else checksum(result)

print(checksum(data))
