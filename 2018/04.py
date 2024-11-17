from collections import Counter
from datetime import datetime
import re

items = [
    '[1518-11-01 00:00] Guard #10 begins shift',
    '[1518-11-01 00:05] falls asleep',
    '[1518-11-01 00:25] wakes up',
    '[1518-11-01 00:30] falls asleep',
    '[1518-11-01 00:55] wakes up',
    '[1518-11-01 23:58] Guard #99 begins shift',
    '[1518-11-02 00:40] falls asleep',
    '[1518-11-02 00:50] wakes up',
    '[1518-11-03 00:05] Guard #10 begins shift',
    '[1518-11-03 00:24] falls asleep',
    '[1518-11-03 00:29] wakes up',
    '[1518-11-04 00:02] Guard #99 begins shift',
    '[1518-11-04 00:36] falls asleep',
    '[1518-11-04 00:46] wakes up',
    '[1518-11-05 00:03] Guard #99 begins shift',
    '[1518-11-05 00:45] falls asleep',
    '[1518-11-05 00:55] wakes up'
]

with open('04.txt', 'r') as f:
    items = f.read().splitlines()

items = sorted(items)

def updateLog(log, guard, newValues):
    if guard in log:
        log[guard] += newValues
    else:
        log[guard] = newValues


def solvePart1(items):
    log = {}
    guard = 0
    last_minute = 0
    for item in items:
        dt = datetime.strptime(item[1:17], '%Y-%m-%d %H:%M')
        if item[-12:] == 'begins shift':
            guard = int(re.findall(r'#(\d+)', item)[0])
            last_minute = 0
        elif item[-12:] == 'falls asleep':
            last_minute = dt.minute
        elif item[-8:] == 'wakes up':
            updateLog(log, guard, list(range(last_minute, dt.minute)))
            last_minute = dt.minute

    maxlen = max(len(v) for v in log.values())
    g = [k for k, v in log.items() if len(v) == maxlen][0]
    c = Counter(log[g])
    return g * c.most_common(1)[0][0]

def solvePart2(items):
    log = []
    guard = 0
    last_minute = 0
    for item in items:
        dt = datetime.strptime(item[1:17], '%Y-%m-%d %H:%M')
        if item[-12:] == 'begins shift':
            guard = int(re.findall(r'#(\d+)', item)[0])
            last_minute = 0
        elif item[-12:] == 'falls asleep':
            last_minute = dt.minute
        elif item[-8:] == 'wakes up':
            sleeps = [(guard, i) for i in range(last_minute, dt.minute)]
            log.extend(sleeps)
            last_minute = dt.minute

    c = Counter(log)
    top = c.most_common(1)[0][0]
    return top[0] * top[1]


print('Part 1: {0}'.format(solvePart1(items)))
print('Part 2: {0}'.format(solvePart2(items)))