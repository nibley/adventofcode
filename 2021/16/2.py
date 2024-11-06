# modified from 2020 18

from math import prod

packet_raw = input()
binary_length = len(packet_raw) * 4
packet = format(int(packet_raw, 16), f'0{binary_length}b')

def parse_packet(packet):
    packet_type = int(packet[ 3 : 6 ], 2)

    if packet_type == 4: # literal value packet
        cursor = 6
        group = packet[ cursor : cursor + 5]
        group_prefix = group[0]
        group_value = group[ 1 : ]

        packet_literal_value = group_value
        while group_prefix == '1':
            cursor += 5
            group = packet[ cursor : cursor + 5]
            group_prefix = group[0]
            group_value = group[ 1 : ]

            packet_literal_value += group_value

        cursor += 5
        packet_literal_value = int(packet_literal_value, 2)

        return (cursor, packet_literal_value)

    # operator packet
    packet_length_type = packet[6]
    subpacket_values = []

    if packet_length_type == '0': # total payload length given
        packet_payload_length = int(packet[ 7 : 22 ], 2)
        cursor = 22
        payload_bits_parsed = 0
        while payload_bits_parsed < packet_payload_length:
            subpacket_length, subpacket_value = (
                parse_packet(packet[ cursor : ])
            )

            subpacket_values.append(subpacket_value)
            cursor += subpacket_length
            payload_bits_parsed += subpacket_length
    else: # total number of payload subpackets given
        packet_num_subpackets = int(packet[ 7 : 18 ], 2)
        cursor = 18
        for _ in range(packet_num_subpackets):
            subpacket_length, subpacket_value = (
                parse_packet(packet[ cursor : ])
            )

            subpacket_values.append(subpacket_value)
            cursor += subpacket_length

    if packet_type in (5, 6, 7):
        assert len(subpacket_values) == 2
        first_value, second_value = subpacket_values

        if packet_type == 5:
            operator_test = first_value > second_value
        elif packet_type == 6:
            operator_test = first_value < second_value
        elif packet_type == 7:
            operator_test = first_value == second_value

        return (cursor, 1 if operator_test else 0)

    if packet_type == 0:
        packet_value = sum(subpacket_values)
    elif packet_type == 1:
        packet_value = prod(subpacket_values)
    elif packet_type == 2:
        packet_value = min(subpacket_values)
    elif packet_type == 3:
        packet_value = max(subpacket_values)

    return (cursor, packet_value)

_, packet_value = parse_packet(packet)
print(packet_value)
