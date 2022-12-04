import scala.io.Source

val fileName = "2021/13.txt"
val input =
  Source
    .fromFile(fileName)
    .getLines()
    .mkString("\n")
    .split("\n\n")
    .map(_.trim.split("\n").toList)
    .toList

def print(s: Set[(Int, Int)]): String = {
  val b = s.unzip.toList.map(_.max)
  val bx = b(0)
  val by = b(1)
  "\n" + (0 to by)
    .map(y => {
      (0 to bx)
        .map(x => {
          s.contains((x, y)) match {
            case true  => "#"
            case false => " "
          }
        })
        .mkString
    })
    .mkString("\n")
}

def fold(
    s: Set[(Int, Int)],
    f: (String, Int)
): Set[(Int, Int)] = {
  val (a, v) = f
  val m = (v + 1 to 2 * v).zip(((v - 1) to 0 by -1)).map((s, t) => s -> t).toMap
  a match {
    case "x" =>
      s.map(p => {
        m.contains(p._1) match {
          case true  => (m(p._1), p._2)
          case false => p
        }
      })
    case "y" =>
      s.map(p => {
        m.contains(p._2) match {
          case true  => (p._1, m(p._2))
          case false => p
        }
      })
  }
}

val dots = input(0)
  .map(x => {
    val a = x.split(",").map(_.toInt)
    (a(0), a(1))
  })
  .toSet

val folds = input(1).map(x => {
  val f =
    x.split(" ")
      .last
      .split("=")
  (f(0), f(1).toInt)
})

val part1 = fold(dots, folds.head).toList.length

val folded = folds.foldLeft(dots)((acc, elem) => {
  fold(acc, elem)
})

val part2 = print(folded)
