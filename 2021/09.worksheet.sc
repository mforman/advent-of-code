import scala.io.Source
// val input = """2199943210
// 3987894921
// 9856789892
// 8767896789
// 9899965678"""
//   .split("\n")
//   .map(_.trim.split("").map(_.toInt).toList)
//   .toList

var fileName = "2021/09.txt"
var input =
  Source
    .fromFile(fileName)
    .getLines()
    .toList
    .map(_.trim.split("").map(_.toInt).toList)

case class Point(r: Int, c: Int) {
  def adjacent: List[Point] = {
    // No diagonals
    val x = (-1 to 1).map(i => { Point(r + i, c) })
    val y = (-1 to 1).map(i => { Point(r, c + i) })
    (x ++ y).filter(p => { (p.r >= 0 && p.c >= 0) && (p != this) }).toList
  }
}

val grid = input.zipWithIndex
  .map {
    case (row, r) => {
      row.zipWithIndex.map {
        case (v, c) => {
          Point(r, c) -> v
        }
      }
    }
  }
  .flatten
  .toMap

val lowPoints =
  grid
    .filter((p, v) => {
      p.adjacent
        .filter(grid.contains(_))
        .forall(grid(_) > v)
    })

val part1 = lowPoints
  .map((_, v) => { v + 1 })
  .sum

def dfs(src: Point, visited: List[Point]): List[Point] = {
  if (visited.contains(src) || !grid.contains(src) || grid(src) == 9) visited
  else {
    src.adjacent.foldLeft(src :: visited)((b, a) => dfs(a, b))
  }
}

val part2 = lowPoints
  .map((p, _) => { dfs(p, List()).length })
  .toList
  .sorted(Ordering.Int.reverse)
  .take(3)
  .product
