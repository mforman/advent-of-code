import scala.io.Source
import scala.collection

val input = """11111
19991
19191
19991
11111"""
  .split("\n")
  .toList
  .map(_.trim.split("").toList.map(_.toInt).toList)

// var fileName = "2021/11.txt"
// var input =
//   Source
//     .fromFile(fileName)
//     .getLines()
//     .toList
//     .map(_.trim.split("").map(_.toInt).toList)

val size = input.length

case class Point(r: Int, c: Int) {
  def adjacent(): List[Point] = {
    (-1 to 1)
      .flatMap(x => { (-1 to 1).map(y => { Point(r + x, c + y) }) })
      .filter(p => {
        p != this && p.r >= 0 && p.c >= 0 && p.r < size && p.c < size
      })
      .toList
  }
}

val grid = input.zipWithIndex.flatMap {
  case (row, r) => {
    row.zipWithIndex.map {
      case (v, c) => {
        Point(r, c) -> v
      }
    }
  }
}.toMap

def step(g: Map[Point, Int]): (Map[Point, Int], Int) = {
  val g = scala.collection.mutable.Map[Point, Int]()
  val flashed = scala.collection.mutable.Set[Point]()

  def flash(p: Point): scala.collection.mutable.Set[Point] = {
    val f = scala.collection.mutable.Set[Point]()
    if (flashed.contains(p)) { return f }
    flashed += p
    f += p
    p.adjacent()
      .foreach(a => {
        val v = g(a) + 1
        g(a) = v
        if (v > 9) { return f ++ flash(a) }
      })
    return f
  }

  g ++= grid.map((k, v) => { k -> (v + 1) })
  g.filter((_, v) => { v > 9 })
    .map((k, _) => flash(k))
    .flatMap(x => x.map(p => g(p) = 0))
  g.toMap -> flashed.toList.length
}

val next = step(grid)

"\n" +
  (0 until size)
    .map(x => {
      (0 until size)
        .map(y => {
          next._1(Point(x, y))
        })
        .mkString
    })
    .mkString("\n")
// def flash(p: Point) = {
//   if (flashed.contains(p)) return
// }

// g.filter((k, v) => { v > 9 })
