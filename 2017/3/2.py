square = int(input())

last_square_in_spiral_layer = [1]
# for i in range(1, 5):
layer = 1
while True:
    last_in_layer = last_square_in_spiral_layer[layer - 1] + (8 * layer)
    last_square_in_spiral_layer.append(last_in_layer)

    if square <= last_in_layer:
        break
    
    layer += 1

print()
print(square)
print(f'layer {layer}')

side_length_in_layer = 2 * layer + 1
print(f'side {side_length_in_layer}')

steps_from_last_in_layer = last_square_in_spiral_layer[layer] - square
steps_from_corner = steps_from_last_in_layer % (side_length_in_layer - 1)
steps_from_mid_side = abs(layer - steps_from_corner)
print(f'steps {steps_from_mid_side}')

print(steps_from_mid_side + layer)

'''
1
3
5
7
'''

'''
37  36  35  34  33  32  31
38  17  16  15  14  13  30
39  18   5   4   3  12  29
40  19   6   1   2  11  28
41  20   7   8   9  10  27
42  21  22  23  24  25  26
43  44  45  46  47  48  49

'''
