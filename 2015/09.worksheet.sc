import scala.io.Source

val regex = """(.+) to (.+) = (\d+)""".r

val distances = io.Source
  .fromFile("2015/09.txt")
  .getLines
  .map { case regex(a, b, distance) =>
    (a, b) -> distance.toInt
  }
  .toMap

val paths = distances.keys
  .flatMap { case (a, b) => Seq(a, b) }
  .toVector
  .permutations
  .toVector

val calculated_paths = paths
  .map(path => {
    path
      .sliding(2)
      .map { case Seq(a, b) => distances.getOrElse((a, b), distances((b, a))) }
      .sum
  })

calculated_paths.min
calculated_paths.max

paths.zip(calculated_paths).sortBy(x => x._2).head
paths.zip(calculated_paths).sortBy(x => x._2).last
