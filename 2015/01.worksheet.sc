import scala.io.Source

val fileName = "2015/01.txt"
val input = Source.fromFile(fileName).getLines().mkString("")

def move(floor: Int, step: Char): Int = {
  if (step == '(') { floor + 1 }
  else { floor - 1 }
}

input.toCharArray
  .foldLeft(0)(move)

input.toCharArray
  .scanLeft(0)(move)
  .indexOf(-1)
