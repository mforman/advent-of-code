import scala.io.Source

val fileName = "2021/01.txt"
// val input = List(199, 200, 208, 210, 200, 207, 240, 269, 260, 263)
val input = Source.fromFile(fileName).getLines().toList map {
  _.toInt
}

def countIncreases(items: List[Int]): Int = {
  items.sliding(2).count { case List(a, b) => b > a }
}

val part1 = countIncreases(input)

val triples = input.sliding(3).toList.map(_.sum)
val part2 = countIncreases(triples)
