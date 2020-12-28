import scala.io.Source

case class Slope(x: Int, y: Int)

def countTrees(s: Slope, grid: Array[String]) = {
  (s.y to grid.length - 1 by s.y) map { i =>
    {
      val step = (i - 1) / s.y + 1
      val col = (step * s.x) % grid(i).length
      grid(i).charAt(col)
      //(col, i)
    }
  } count {
    _ == '#'
  },
}

// val input =
//   """..##.......
//     |#...#...#..
//     |.#....#..#.
//     |..#.#...#.#
//     |.#...##..#.
//     |..#.##.....
//     |.#.#.#....#
//     |.#........#
//     |#.##...#...
//     |#...##....#
//     |.#..#...#.#
//     |""".stripMargin split ('\n')

val fileName = "../advent/2020/03.txt"
val input = Source.fromFile(fileName).getLines().toArray

val r = countTrees(Slope(3, 1), input)

var slopes = List((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)) map {
  Slope.tupled
} map {
  countTrees(_, input).toLong
} product
