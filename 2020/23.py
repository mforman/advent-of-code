from __future__ import annotations
from collections import deque
from typing import Dict, List
from tqdm import tqdm


def play(input, moves):
    cups = deque(input)

    for move in tqdm(range(moves)):
        current = cups[0]
        cups.rotate(-1)
        pickup = reversed([cups.popleft() for _ in range(3)])
        destination = current - 1

        if destination not in cups:
            min_val = min(cups)
            max_val = max(cups)
            destination -= 1
            while destination not in cups:
                if destination < min_val:
                    destination = max_val + 1
                destination -= 1

        while cups[0] != destination:
            cups.rotate(-1)
        cups.rotate(-1)
        cups.extendleft(pickup)

        while cups[0] != current:
            cups.rotate(-1)
        cups.rotate(-1)

    while cups[1] != 1:
        cups.rotate(-1)
    cups.rotate(-1)

    cups.popleft()

    return cups


class Node(object):
    def __init__(self, v: int, next: Node = None) -> None:
        self.val = v
        self.next = next


def play_big(input, n, moves):
    cups: List[Node] = input + list(range(max(input) + 1, n + 1))

    lookup: Dict[int, Node] = {}

    for i in range(1, n + 1):
        lookup[i] = Node(i)
    for i in range(n):
        lookup[cups[i]].next = lookup[cups[(i + 1) % n]]

    current: Node = lookup[cups[0]]

    for i in tqdm(range(moves)):
        pick = current.next
        current.next = current.next.next.next.next
        dest = current.val
        while dest in [current.val, pick.val, pick.next.val, pick.next.next.val]:
            dest = dest - 1 if dest - 1 > 0 else n
        ncup = lookup[dest]
        pick.next.next.next = ncup.next
        ncup.next = pick
        current = current.next

    return lookup[1].next.val * lookup[1].next.next.val


def main():
    input = [int(c) for c in "853192647"]
    part1 = "".join([str(i) for i in play(input, 100)])
    print(f"Part 1: {part1}")

    print(f"Part 2: {play_big(input, 1000000, 10000000)}")


if __name__ == "__main__":
    main()
