import scala.io.Source

case class Point(x: Int, y: Int)

val Instruction =
  """(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)""".r

val input = Source
  .fromFile("2015/06.txt")
  .getLines()
  .toStream
  .map(x => {
    x match {
      case Instruction(cmd, x1, y1, x2, y2) => {
        (cmd, Point(x1.toInt, y1.toInt), Point(x2.toInt, y2.toInt))
      }
    }
  })
