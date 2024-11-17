from collections import defaultdict, deque

items = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.'
]

with open('07.txt', 'r') as f:
    items = f.read().splitlines()

instructions = [[item[5], item[36]] for item in items]

edges = defaultdict(list)
in_degree = defaultdict(int)
work = []

for x, y in instructions:
    edges[x].append(y)
    in_degree[y] += 1

for k in edges:
     edges[k] = sorted(edges[k])
     if in_degree[k] == 0:
         work.append(k)

def solvePart1(edges, in_degree, work):
    result = ''
    while work:
        x = sorted(work)[0]
        work.remove(x)
        result += x
        for y in edges[x]:
            in_degree[y] -= 1
            if in_degree[y] == 0:
                work.append(y)
    return result


def startWork(work, events, workers, delay, time):
    while len(events) < workers and work:
        x = min(work)
        work.remove(x)
        end_time = time+delay+1+ord(x)-ord('A')
        print('Starting {} at {}. Will finish at {}'.format(x, time, end_time))
        events.append((end_time, x))

def solvePart2(edges, in_degree, work, workers, delay):
    time = 0
    events = []
    startWork(work, events, workers, delay, time)

    while events or work:
        time, x = min(events)
        print(time,x)
        events.remove((time,x))
        for y in edges[x]:
            in_degree[y] -= 1
            if in_degree[y] == 0:
                work.append(y)
        startWork(work, events, workers, delay, time)
    
    return time

# print ('Part 1: {}'.format(solvePart1(edges, in_degree, work)))
print ('Part 2: {}'.format(solvePart2(edges, in_degree, work, 5, 60)))