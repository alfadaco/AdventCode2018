import data_04dec2018
import dateutil.parser as dp
import numpy as np
import re

data = data_04dec2018.data

for entry in data:
    entry[0] = dp.parse(entry[0])

data.sort(key = lambda k: k[0])
first_day = data[0][0]
last_day = data[-1][0]
difference = last_day - first_day
n_days = difference.days + 1

table = np.zeros((n_days,60+2), dtype=int)

r = -1
first_minute = -1
last_minute = -1
guard_id = -1
guard_asleep_time = {}
for row in data:
    parsed = re.match('Guard #(\d*) begins shift', row[1])
    if parsed:
        if r > -1:
            day_asleep_minutes = table[r][0:-2].sum()
            table[r][-1] = day_asleep_minutes
            guard_asleep_time[guard_id] += day_asleep_minutes
        r += 1
        guard_id = int(parsed.group(1))
        table[r][-2] = guard_id
        if guard_id not in guard_asleep_time:
            guard_asleep_time[guard_id] = 0
    elif row[1] == 'falls asleep':
        first_minute = row[0].minute
    elif row[1] == 'wakes up':
        last_minute = row[0].minute - 1
        minutes_asleep = np.arange(first_minute,last_minute+1)
        table[r][np.ix_(minutes_asleep)] = 1
    else:
        print('Error!')

# Sum for last row
day_asleep_minutes = table[r][0:-2].sum()
table[r][-1] = day_asleep_minutes
guard_asleep_time[guard_id] += day_asleep_minutes

# Get guard with maximum overall asleep minutes and number of minutes
(guard_id,overall_asleep_minutes) = [(k,v) for k,v in guard_asleep_time.items() if v == max(guard_asleep_time.values())][0]

# Select rows with guard_id
table_selected_guard = table[table[:,-2] == guard_id]

# Get number of times guard was asleep in each minute
overall_asleep_per_minute = sum(table_selected_guard[:,0:60],0)

# Get minute with highest frequency
max_minute = np.argmax(overall_asleep_per_minute)

print("Strategy 1:")
print(str(max_minute * guard_id))

guard_id = -1
minute_id = -1
max_frequency = -1
for guard in guard_asleep_time.keys():
    table_selected_guard = table[table[:, -2] == guard]
    overall_asleep_per_minute = sum(table_selected_guard[:, 0:60], 0)
    curr_max = max(overall_asleep_per_minute)
    if curr_max > max_frequency:
        max_frequency = curr_max
        guard_id = guard
        minute_id = np.argmax(overall_asleep_per_minute)

print("Strategy 2:")
print(str(minute_id * guard_id))
