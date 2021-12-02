import scala.io.Source
import scala.util.matching.Regex

// val input =
//   """forward 5
//     |down 5
//     |forward 8
//     |up 3
//     |down 8
//     |forward 2""".stripMargin

val fileName = "2021/02.txt"
val input = Source.fromFile(fileName).getLines().mkString("\n")

val CommandRegex = """(\w+)\s(\d+)""".r
case class Command(x: Int, y: Int)
case class Position(x: Int, depth: Int)
case class AimedPosition(x: Int, depth: Int, aim: Int)

val directions = input.split("\n") map { case CommandRegex(dir, amt) =>
  var a = amt.toInt
  dir match {
    case "forward" => Command(a, 0)
    case "down"    => Command(0, a)
    case "up"      => Command(0, a * -1)
    case _         => Command(0, 0)
  }
}

def Move(p: Position, cmd: Command): Position = {
  Position(p.x + cmd.x, p.depth + cmd.y)
}

def MoveWithAim(p: AimedPosition, cmd: Command): AimedPosition = {
  cmd match {
    case c if c.x > 0 =>
      AimedPosition(p.x + cmd.x, p.depth + (p.aim * cmd.x), p.aim)
    case _ => AimedPosition(p.x, p.depth, p.aim + cmd.y)
  }
}

val end = directions.foldLeft(Position(0, 0))((p, c) => Move(p, c))
val part1 = end.x * end.depth

val end2 =
  directions.foldLeft(AimedPosition(0, 0, 0))((p, c) => MoveWithAim(p, c))
val part2 = end2.x * end2.depth
