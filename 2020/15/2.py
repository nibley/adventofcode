
def speak(turn, number):
    turn_spoken_last = spoken_last.get(number)
    if turn_spoken_last is not None:
        spoken_before_last[number] = turn_spoken_last

    spoken_last[number] = turn

starting_numbers = map(int, input().split(','))
spoken_last = {}
spoken_before_last = {}

for turn, last_number in enumerate(starting_numbers):
    speak(turn, last_number)

for turn in range(turn + 1, 30_000_000):
    turn_spoken_before_last = spoken_before_last.get(last_number)
    last_number = (
        0 if turn_spoken_before_last is None
        else (turn - 1) - turn_spoken_before_last
    )

    speak(turn, last_number)

print(last_number)
