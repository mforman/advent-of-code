import scala.io.Source

var fileName = "2021/14.txt"
var input =
  Source
    .fromFile(fileName)
    .getLines()
    .toList

val start = input.head
  .sliding(2)
  .map(_.toList)
  .map(x => x.head -> x.last)
  .toList
  .groupMapReduce(identity)(_ => 1L)(_ + _)

val pairs = input
  .drop(2)
  .map(x => {
    val r = x.split(" -> ")
    (r(0)(0), r(0)(1)) -> r(1)(0)
  })
  .toMap

type PairMap = Map[(Char, Char), Char]
type PairCounter = Map[(Char, Char), Long]
type CharCounter = Map[Char, Long]

def step(
    s: PairCounter,
    c: CharCounter,
    pairs: PairMap
): (PairCounter, CharCounter) = {
  s.foldLeft((Map.empty[(Char, Char), Long], c)) {
    //      acc              elem
    case ((map, cs), (pair @ (x, y), count)) => {
      val insertion = pairs(pair)
      val a = (x, insertion)
      val b = (insertion, y)

      val nextMap = map ++ Map(
        a -> (count + map.getOrElse(a, 0L)),
        b -> (count + map.getOrElse(b, 0L))
      )

      val nextCounts =
        (cs + (insertion -> (cs.getOrElse(insertion, 0L) + count)))

      nextMap -> nextCounts
    }
  }
}

def solve(
    s: PairCounter,
    n: Int,
    p: PairMap
): Long = {
  val c = input.head.groupMapReduce(identity)(_ => 1L)(_ + _)
  val (_, r) = (0 until n).foldLeft((s, c)) { case ((m, c), _) =>
    step(m, c, pairs)
  }

  val sorted = r.toList.map(_._2).sorted
  sorted.last - sorted.head
}

val part1 = solve(start, 10, pairs)
val part2 = solve(start, 40, pairs)

// val start :: rawPairs = input.split("\n").toList
// val pairs = rawPairs
//   .drop(1)
//   .map(x => {
//     val r = x.split(" -> ")
//     (r(0)(0), r(0)(1)) -> r(1)(0)
//   })
//   .toMap

// def insert(start: String, pairs: Map[(Char, Char), Char]): String = {
//   val inserted = (" " + start)
//     .zip(start)
//     .drop(1)
//     .map(x => {
//       pairs.contains(x) match {
//         case true  => s"${x._1}${pairs(x)}${x._2}"
//         case false => s"${x._1}${x._2}"
//       }
//     })
//     .toList

//   inserted.map(_.dropRight(1)).mkString + inserted.last.last
// }

// def solve(s: String, n: Int, p: Map[(Char, Char), Char]): Long = {
//   val chain = (0 until n).foldLeft(s)((acc, _) => insert(acc, p))
//   val counts = chain.groupBy(identity).view.mapValues(_.size)
//   val max = counts.maxBy(_._2)._2
//   val min = counts.minBy(_._2)._2
//   max - min
// }

// val part1 = solve(start, 10, pairs)
// //val part2 = solve(start, 40, pairs)
