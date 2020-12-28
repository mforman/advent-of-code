import scala.io.Source

val solve = (x: List[Int], n: Int) =>
  x combinations (n) find {
    _.sum == 2020
  } map {
    _.product
  } getOrElse (0)


val fileName = "2020/01.txt"
//val input = List(1721, 979, 366, 299, 675, 1456)
val input = Source.fromFile(fileName).getLines().toList map {
  _.toInt
}

val part1 = solve(input, 2)
val part2 = solve(input, 3)


