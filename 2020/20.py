from collections import Counter
from math import sqrt
from typing import List, Dict
from functools import reduce


class Tile:
    top = ""
    bottom = ""
    left = ""
    right = ""

    def _set_edges(self) -> None:
        self.top = self.img[0]
        self.bottom = self.img[-1]
        self.left = "".join(row[0] for row in self.img)
        self.right = "".join(row[-1] for row in self.img)

    def __init__(self, id: int, img: List[str]) -> None:
        self.id = id
        self.img = img
        self._set_edges()

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Tile) and self.id == o.id

    def __str__(self) -> str:
        return "\n".join(self.img)

    def __repr__(self) -> str:
        return str(self.id) + ": " + str(self)

    def edges(self) -> List[str]:
        return [self.top, self.bottom, self.left, self.right]

    def rotate(self) -> None:
        self.img = list(zip(*self.img[::-1]))
        self._set_edges()


def rotate(tile: List[str]) -> List[str]:
    return list(zip(*tile[::-1]))


def tile_edges(tile: List[str]) -> List[str]:
    return [
        tile[0],
        tile[-1][::-1],
        "".join(row[-1] for row in tile),
        "".join(row[0] for row in tile[::-1]),
    ]


def count_edges(tiles: Dict[str, List[str]]) -> Counter:
    edges = Counter()
    for tile in tiles.values():
        edges.update(tile_edges(tile))
        edges.update(tile_edges(tile[::-1]))
    return edges


def main():
    input = open("20-sample.txt").read()
    # input = open("20.txt").read()

    tiles = {
        int(t[0][5:-1]): t[1:]
        for t in (i.strip().split("\n") for i in input.split("\n\n"))
    }

    board_size = int(sqrt(len(tiles)))

    edges = count_edges(tiles)

    result = 1
    corners = []
    for id, tile in tiles.items():
        unique = []
        for edge in tile_edges(tile):
            if edges[edge] == 1:
                unique.append(edge)
            else:
                assert edges[edge] == 2
        if len(unique) == 2:
            corners.append((id, unique))
            result *= id

    print(f"Corners: {corners}")
    print(f"Part 1: {result}")

    # Part 2

    tiles = {i: Tile(i, t) for i, t in tiles.items()}
    remaining_corners = list(corners)

    tl_id, tl_edges = remaining_corners.pop()
    tl = tiles[tl_id]
    while not all([e in tl_edges for e in [tl.top, tl.left]]):
        tl.rotate()

    grid = []
    # pick one corner
    # orient to top-left
    # find tile with matching side to right edge

    for r in range(board_size):
        row = []
        for c in range(board_size):
            if r == c == 0:
                id, edges = remaining_corners.pop()

                tile = tiles[id]

                # for _ in range(3):
                #     if tile[0] and


if __name__ == "__main__":
    main()
