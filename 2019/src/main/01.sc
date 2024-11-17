import scala.io.Source


def GetFuel(m: Int): Int = {
  Math.floorDiv(m, 3) - 2
}

def GetTotalFuel(m: Int): Int = GetFuel(m) match {
  case x if x <= 0 => 0
  case x => x + GetTotalFuel(x)
}

val fileName = "/Users/melvin/Dropbox/Personal/CodingPuzzles/Advent/2019/01.txt"

def SolvePart1(filename: String): Int = {
  Source
    .fromFile(filename)
    .getLines
    .map(line => {
      val m = line.toInt
      GetFuel(m)
    })
    .sum
}


def SolvePart2(filename: String): Int = {
  Source
    .fromFile(filename)
    .getLines
    .map(line => {
      val m = line.toInt
      GetTotalFuel(m)
    })
    .sum
}
println(SolvePart1(fileName))
println(SolvePart2(fileName))