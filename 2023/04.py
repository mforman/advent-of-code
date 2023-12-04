import aocd

import argparse
import logging
from collections import defaultdict

from aocd.models import count

parser = argparse.ArgumentParser()
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()

if args.debug:
    log_level = logging.DEBUG
else:
    log_level = logging.INFO
logging.basicConfig(level=log_level, format="%(message)s")

def ParseLine(input:str) -> tuple[int,tuple[set[int], set[int]]]:
    c = input.find(':')
    b = input.find('|')
    id = int(input[5:c])
    winning = {int(x) for x in input[c+1:b].strip().split()}
    have = {int(x) for x in input[b+1:].strip().split()}
    return (id, (winning, have))

assert ParseLine("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53") == (1,({17,41,48,83,86},{6,9,17,31,48,53,83,86}))

def ParseCards(input:list[str]) -> list[tuple[int, tuple[set[int], set[int]]]]:
    return [ParseLine(x) for x in input]

def GetMatches(card: tuple[set[int], set[int]]) -> set[int]:
    a,b = card
    return a & b

assert GetMatches(({17,41,48,83,86},{6,9,17,31,48,53,83,86})) == {17,48,83,86}

def Part1(input:list[str]) -> int:
    cards = ParseCards(input)
    points = 0
    for _, card in cards:
        matches = GetMatches(card)
        logging.debug("Card: %s", card)
        logging.debug("Matches (%s): %s", len(matches), matches)
        
        if matches:
            score = pow(2,len(matches)-1)
            logging.debug("Score: %s", score)
            points += score

    logging.debug("Total: %s", points)
    return points

def Part2(input:list[str]) -> int:
    cards = [(id, len(GetMatches(card))) for id, card in ParseCards(input)]
    logging.debug("\nPart 2 Cards (id, match count):\n%s", cards)

    size = len(cards)
    copies = defaultdict(int)
    for i in range(size):
        id, matches = cards[i]
        logging.debug("\nCard %s - %s matches", id, matches)  

        if matches > 0:
            j = i + matches + 1
            if j > size:
                j = size - i
            toCopy = [cid for cid, _ in cards[i+1:j]]
            logging.debug("Copying the next %s cards: %s", j, toCopy)
            for x in toCopy:
                copies[x] += (1 + copies[id]) 
            logging.debug("Counter: %s", dict(copies))
    
    
    total = sum(dict(copies).values()) + size
    logging.debug("Counter(%s): %s", total, copies)
    return total


sample = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".strip().splitlines()

assert Part1(sample) == 13
assert Part2(sample) == 30

input:list[str] = aocd.get_data(day=4, year=2023).splitlines()

print(f"Part 1: {Part1(input)}")
print(f"Part 2: {Part2(input)}")
