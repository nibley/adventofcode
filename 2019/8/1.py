digits = [int(char) for char in input()]

width = 25
height = 6
frame_pixels = width * height
num_frames = len(digits) // frame_pixels

frames = [
    digits[ frame_pixels * i : frame_pixels * (i + 1)]
    for i in range(num_frames)
]

frames_by_zero_count = sorted(frames, key=lambda frame: frame.count(0))
frame_with_fewest_zeros = frames_by_zero_count[0]

print(frame_with_fewest_zeros.count(1) * frame_with_fewest_zeros.count(2))
