#!/usr/bin/env python3


def get_digits(num):
    for i in range(5, -1, -1):
        x = 10 ** i
        yield num // x
        num = num % x


def validate_part1(num):
    digits = get_digits(num)
    previous = -1
    found_double = False
    for i in digits:
        if i < previous:
            return False
        if i == previous:
            found_double = True
        previous = i
    return found_double


def validate_part2(num, target=2):
    if not validate_part1(num):
        return False
    digits = list(get_digits(num))
    previous = digits[0]
    count = 1
    for i in digits[1:]:
        if i > previous:
            if count == target:
                return True
            else:
                count = 1
        elif i == previous:
            count += 1
        previous = i
    return count == target


assert validate_part2(112233)
assert not validate_part2(123444)
assert validate_part2(111122)

part1 = [x for x in range(156218, 652527) if validate_part1(x)]
part2 = [x for x in part1 if validate_part2(x)]

print(f"Part 1: {len(part1)}")
print(f"Part 2: {len(part2)}")

