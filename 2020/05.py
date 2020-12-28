input = ["FBFBBFFRLR"]

input = [row.strip() for row in open("05.txt").readlines()]


def parse_seat(s):
    def parse_char(c):
        if c in ["F", "L"]:
            return "0"
        if c in ["B", "R"]:
            return "1"

    row = int("".join([parse_char(x) for x in s[:7]]), 2)
    seat = int("".join([parse_char(x) for x in s[-3:]]), 2)

    return (row, seat)


seats = map(parse_seat, input)
seat_num = list([(row * 8) + seat for row, seat in seats])

min_seat = min(seat_num)
max_seat = max(seat_num)

print(f"Part 1: {max_seat}")

for n in range(min_seat, max_seat):
    if n not in seat_num and all(x in seat_num for x in [n - 1, n + 1]):
        print(f"Part 2: {n}")
        break
