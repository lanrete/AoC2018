import os

import numpy as np

def sort_input(file_name):
    logs = []
    with open(file_name, 'r') as f:
        for line in f:
            logs.append(line.strip())
    def time(raw_string):
        year, month, day = [int(_) for _ in raw_string.split(' ')[0][1:].split('-')]
        hour, minute = [int(_) for _ in raw_string.split(']')[0].split(' ')[-1].split(':')]
        return year*1e8 + month*1e6 + day*1e4 + hour*1e2 + minute
    logs.sort(key=time)
    return logs


def get_guard(log):
    if 'Guard' in log:
        return ''.join(log.split(' ')[3][1:])
    return None


def get_time(log):
    hour, minute = [int(_) for _ in log.split(']')[0].split(' ')[-1].split(':')]
    return hour, minute


def get_status(log):
    if get_guard(log):
        return 0
    if log.find('wakes up') > 0:
        return 0
    if log.find('falls asleep') > 0:
        return 1
    raise ValueError('Something wrong with %s' % log)


def process_log(logs):
    current_guard = 0
    current_status = 0
    current_hour = 0
    current_minute = 0
    # Status = 0 -> Awake
    # Status = 1 -> Asleep
    guard_list = {}
    timesheet = [0] * 60
    for log in logs:
        if get_guard(log):
            current_guard = get_guard(log)
        if current_guard not in guard_list:
            guard_list[current_guard] = timesheet.copy()
        hour, minute = get_time(log)
        if hour >= 1:
            hour, minute = 0, 0
        status = get_status(log)
        for _ in range(current_minute, minute):
            guard_list[current_guard][_] += current_status

        current_status = status
        current_hour = hour
        current_minute = minute

    print('%s guards found' % (len(guard_list)))

    max_ph = 0
    max_guard = 0
    for k, v in guard_list.items():
        minutes = sum(v)
        if minutes > max_ph:
            max_ph = minutes
            max_guard = k
    most_sleeped = np.argmax(guard_list[max_guard])
    print('Guard %s sleeps %s minutes' % (max_guard, max_ph) )
    print('Guard %s sleeps most in minute # %s' % (max_guard, most_sleeped))
    print('Number chosed ==> %s' % (int(max_guard) * most_sleeped))


if __name__ == '__main__':
    logs = sort_input('input/day4.txt')
    process_log(logs)
