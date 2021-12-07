import scala.io.Source

//var input = "16,1,2,0,4,2,7,1,2,14".split(",").map(_.toInt).toVector
var fileName = "2021/07.txt"
var input =
  Source
    .fromFile(fileName)
    .getLines()
    .mkString("\n")
    .split(",")
    .map(_.toInt)
    .toVector
var a = input.min
var b = input.max

val part1 = (a to b)
  .map(n => {
    input.map { x => (x - n).abs }.sum
  })
  .min

val part2 = (a to b)
  .map(n => {
    input
      .map(x => {
        val steps = (x - n).abs
        (steps * (steps + 1)) / 2
      })
      .sum
  })
  .min
