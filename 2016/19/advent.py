#! /usr/bin/env python
import sys
import time
from collections import deque

class Node:
    def __init__(self, id):
        self.id = id
        self.nxt = None
        self.prv = None
    
    def delete(self):
        self.prv.nxt = self.nxt
        self.nxt.prv = self.prv

def steal_from_left(elf_count):
    d = deque(maxlen=elf_count)
    for i in range(elf_count):
        d.appendleft(i+1)

    current_elf = None
    while len(d) > 0:
        current_elf = d.pop()
        if len(d) == 0:
            break
        d.pop() # victim
        d.appendleft(current_elf)
    return current_elf

def steal_from_across(n):
    items = list(map(Node, range(n))) # Create the list
    for i in range(n): # Set the links (mod n for wrap-around)
        items[i].nxt = items[(i+1)%n]
        items[i].prv = items[(i-1)%n]

    start = items[0]
    mid = items[int(n/2)]

    for i in range(n-1):
        mid.delete()
        mid = mid.nxt
        if (n-i)%2 == 1:
            mid = mid.nxt # Favor the left
        start = start.nxt

    return start.id+1



def main():
    elf_count = 5

    if len(sys.argv) > 1:
        elf_count = int(sys.argv[1])

    print('Number of elves: {}'.format(elf_count))

    l_start = time.perf_counter()
    from_left = steal_from_left(elf_count)
    l_stop = time.perf_counter()

    print('Steal from left (deque): {}  {}'.format(from_left, l_stop - l_start))

    a_start = time.perf_counter()
    amazing = int('0b' + bin(elf_count)[3:] + '1', 2)
    a_stop = time.perf_counter()
    print('Steal from left (math): {}   {}'.format(amazing, a_stop - a_start))

    across = steal_from_across(elf_count)

    print('Steal from across {}'.format(across))

if __name__ == '__main__':
    main()
