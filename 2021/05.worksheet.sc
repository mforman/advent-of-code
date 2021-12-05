import scala.io.Source

// val input = """0,9 -> 5,9
// 8,0 -> 0,8
// 9,4 -> 3,4
// 2,2 -> 2,1
// 7,0 -> 7,4
// 6,4 -> 2,0
// 0,9 -> 2,9
// 3,4 -> 1,4
// 0,0 -> 8,8
// 5,5 -> 8,2""".stripMargin.split("\n").toList

def GetRange(a: Int, b: Int): List[Int] = {
  if (a <= b) { (a to b).toList }
  else { (a to b by -1).toList }
}

case class Point(x: Int, y: Int)

class Line(var a: Point, var b: Point) {
  def isHorizontal: Boolean =
    a.y == b.y
  def isVertical: Boolean =
    a.x == b.x
  def isStraight: Boolean =
    isHorizontal || isVertical
  def points(): Option[List[Point]] =
    if (isHorizontal) Some({ GetRange(a.x, b.x).map(x => Point(x, a.y)) })
    else if (isVertical) Some({ GetRange(a.y, b.y).map(y => Point(a.x, y)) })
    else {
      Some({
        val rx = GetRange(a.x, b.x)
        val ry = GetRange(a.y, b.y)
        rx.zip(ry).map(p => Point(p._1, p._2))
      })
    }

  override def toString: String =
    s"${a.x},${a.y} -> ${b.x},${b.y}"
}

def CountOverlaps(lines: List[Line]): Int = {
  lines
    .map(line => {
      line.points()
    })
    .flatten
    .flatten
    .groupBy(identity)
    .view
    .mapValues(_.size)
    .filter((k, v) => v >= 2)
    .toList
    .length
}

val fileName = "2021/05.txt"
val input = Source.fromFile(fileName).getLines()

val lines = input
  .map({ s =>
    val points = s
      .split(" -> ")
      .toList
      .map(s => {
        val i = s
          .split(",")
          .toList
          .map(x => { x.trim.toInt })
        Point(i(0), i(1))
      })
    Line(points(0), points(1))
  })
  .toList

CountOverlaps(lines.filter { _.isStraight })
CountOverlaps(lines)
