from typing import List


def main():
    input = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10

"""

    input = open("22.txt").read()

    p1, p2 = (
        list(map(int, row.split("\n")[1:])) for row in input.strip().split("\n\n")
    )

    original1 = list(p1)
    original2 = list(p2)

    round = 1
    while p1 and p2:
        # print(f"-- Round {round} --")
        # print(f"Player 1's deck: {', '.join((str(i) for i in p1))}")
        # print(f"Player 2's deck: {', '.join((str(i) for i in p2))}")

        a = p1.pop(0)
        b = p2.pop(0)

        # print(f"Player 1 plays: {a}")
        # print(f"Player 2 plays: {b}")

        if a > b:
            winner = "1"
            p1 += [a, b]
        else:
            winner = "2"
            p2 += [b, a]

        # print(f"Player {winner} wins the round!\n")

        round += 1

    deck = p1 + p2
    # print(", ".join([str(i) for i in deck]))

    s = sum(i * x for i, x in enumerate(deck[::-1], 1))

    print(f"Part 1: {s}")

    # Part 2
    # True = player 1 wins
    def play_rec(p1: List[int], p2: List[int]) -> bool:
        seen = set()
        while p1 and p2:
            k = (tuple(p1), tuple(p2))
            if k in seen:
                return True
            seen.add(k)
            a = p1.pop(0)
            b = p2.pop(0)
            if len(p1) >= a and len(p2) >= b:
                if play_rec(p1[:a], p2[:b]):
                    p1 += [a, b]
                else:
                    p2 += [b, a]
            elif a > b:
                p1 += [a, b]
            else:
                p2 += [b, a]
        return len(p1) > 0

    p1 = original1
    p2 = original2

    play_rec(p1, p2)

    deck = p1 + p2
    s = sum(i * x for i, x in enumerate(deck[::-1], 1))

    print(f"Part 2: {s}")


if __name__ == "__main__":
    main()