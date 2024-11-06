# modified from 2020 18

packet_raw = input()
binary_length = len(packet_raw) * 4
packet = format(int(packet_raw, 16), f'0{binary_length}b')

def parse_packet(packet):
    packet_version = int(packet[:3], 2)
    packet_type = int(packet[3:6], 2)

    if packet_type == 4: # literal value packet
        cursor = 6
        group = packet[ cursor : cursor + 5]
        group_prefix = group[0]
        group_value = group[1:]

        packet_literal_value = group_value
        while group_prefix == '1':
            cursor += 5
            group = packet[ cursor : cursor + 5]
            group_prefix = group[0]
            group_value = group[1:]

            packet_literal_value += group_value

        cursor += 5
        packet_literal_value = int(packet_literal_value, 2)

        # number of binary digits, version
        return (cursor, packet_version)

    # operator packet
    packet_length_type = packet[6]
    sum_of_versions = 0

    if packet_length_type == '0': # total payload length given
        packet_payload_length = int(packet[ 7 : 22 ], 2)
        cursor = 22
        payload_bits_parsed = 0
        while payload_bits_parsed < packet_payload_length:
            subpacket_length, subpacket_version = (
                parse_packet(packet[ cursor : ])
            )

            cursor += subpacket_length
            payload_bits_parsed += subpacket_length
            sum_of_versions += subpacket_version
    else: # total number of payload subpackets given
        packet_num_subpackets = int(packet[ 7 : 18 ], 2)
        cursor = 18
        for _ in range(packet_num_subpackets):
            subpacket_length, subpacket_version = \
                parse_packet(packet[ cursor : ])

            cursor += subpacket_length
            sum_of_versions += subpacket_version

    # number of binary digits, version
    return (cursor, packet_version + sum_of_versions)

_, sum_of_versions = parse_packet(packet)
print(sum_of_versions)
