import scala.io.Source

case class Point(x: Int, y: Int)
case class Command(cmd: String, start: Point, end: Point)

val Instruction =
  """(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)""".r

def getLights(start: Point, end: Point, gridSize: Int): Set[Int] = {
  val first = (start.y * gridSize) + start.x
  val lights =
    for (
      x <- 0 to (end.x - start.x);
      y <- 0 to (end.y - start.y)
    ) yield first + (y * gridSize) + x

  lights.toSet
}

def apply(lights: Set[Int], c: Command, gridSize: Int): Set[Int] = {
  val current = getLights(c.start, c.end, gridSize)
  c.cmd match {
    case "turn on"  => lights | current
    case "turn off" => lights.diff(current)
    case "toggle" => {
      val on = lights & current
      val off = current.diff(lights)
      lights.diff(on) | off
    }
  }
}

val input = Source
  .fromFile("2015/06.txt")
  .getLines()
  .toStream
  .map(x => {
    x match {
      case Instruction(cmd, x1, y1, x2, y2) => {
        Command(cmd, Point(x1.toInt, y1.toInt), Point(x2.toInt, y2.toInt))
      }
    }
  })

val applyFunction = apply _
def apply1000 = applyFunction.curried(_: Set[Int])(_: Command)(1000)

input
  .foldLeft(Set.empty[Int])(apply1000)
  .toList
  .length
