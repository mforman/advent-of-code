import aocd

import argparse
import logging
import re

parser = argparse.ArgumentParser()
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()

if args.debug:
    log_level = logging.DEBUG
else:
    log_level = logging.INFO
logging.basicConfig(level=log_level, format="%(message)s")


def ParseInput(input:list[str]) -> list[tuple[int, int]]:
    num_re = re.compile(r'(\d+)')
    t = [int(i) for i in num_re.findall(input[0])]
    d = [int(i) for i in num_re.findall(input[1])]
    return list(zip(t,d))

sample = """
Time:      7  15   30
Distance:  9  40  200
""".strip().splitlines()

assert ParseInput(sample) == [(7,9),(15,40),(30,200)]

