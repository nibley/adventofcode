digits = [int(char) for char in input()]

width = 25
height = 6
frame_pixels = width * height
num_frames = len(digits) // frame_pixels

frames = [
    digits[ frame_pixels * i : frame_pixels * (i + 1)]
    for i in range(num_frames)
]

image = [ [0 for _ in range(width)] for _ in range(height) ]
for frame in reversed(frames):
    for y in range(height):
        row = frame[ width * y : width * (y + 1) ]
        for x, digit in enumerate(row):
            if digit != 2:
                image[y][x] = digit

visualize_digit = lambda digit: '#' if digit == 1 else '.' 
for row in image:
    print(''.join(visualize_digit(digit) for digit in row))
