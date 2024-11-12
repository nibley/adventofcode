from collections import defaultdict, Counter

guard_shifts = defaultdict(list)
shift_logs = defaultdict(list)
while True:
    try:
        line = input()
    except EOFError:
        break

    timestamp, message = line.split('] ')
    first_word, second_word, *_ = message.split()

    date_raw, time_raw = timestamp[ 1 : ].split()
    _, month, day = map(int, date_raw.split('-'))

    hour, minute = map(int, time_raw.split(':'))
    if hour == 23:
        # guard arrived early for the shift
        if (
            day == 30 and month in (4, 6, 9, 11)
            or day == 28 and month == 2
            or day == 31
        ): # roll month over
            day = 1
            month += 1
        else: # just roll day
            day += 1
    else:
        assert hour == 0

    date = (month, day)

    if first_word == 'Guard':
        guard_id = int(second_word[ 1 : ])
        guard_shifts[guard_id].append(date)
    else:
        shift_logs[date].append(minute)

for shift_log in shift_logs.values():
    assert not len(shift_log) % 2
    shift_log.sort() # each log now consists of sleep, wake, sleep, wake, etc.

guard_sleep_periods = defaultdict(list)
for guard_id, shift_dates in guard_shifts.items():
    sleep_periods = guard_sleep_periods[guard_id]
    for shift_date in shift_dates:
        shift_log = shift_logs[shift_date]

        for sleep, wake in zip(
            shift_log[ : -1 : 2 ],
            shift_log[ 1 : : 2 ]
        ):
            sleep_periods.append(range(sleep, wake))

sleep_frequency = Counter()
for guard_id, sleep_periods in guard_sleep_periods.items():
    for sleep_period in sleep_periods:
        for minute in sleep_period:
            sleep_frequency[ (guard_id, minute) ] += 1

laziest_guard_id, best_minute = max(
    sleep_frequency,
    key=sleep_frequency.get
)
print(laziest_guard_id * best_minute)
