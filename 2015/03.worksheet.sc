import scala.io.Source

val directions = Map(
  '^' -> (0, 1),
  '>' -> (1, 0),
  'v' -> (0, -1),
  '<' -> (-1, 0)
)

val fileName = "2015/03.txt"
val input = Source
  .fromFile(fileName)
  .getLines()
  .mkString
  .toCharArray()
  .map(c => directions(c))

def move(start: (Int, Int), step: (Int, Int)): (Int, Int) = {
  (start._1 + step._1, start._2 + step._2)
}

val visited = input
  .scanLeft((0, 0))(move)
  .distinct
  .length

input
  .zip(input.indices.map(_ % 2))
  .groupBy(x => x._2)
  .values
  .map(x => {
    x
      .map(y => y._1)
      .scanLeft(0, 0)(move)
  })
  .flatten
  .toArray
  .distinct
  .length
