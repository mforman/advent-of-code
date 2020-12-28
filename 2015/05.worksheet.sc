import scala.io.Source

val vowels = List('a', 'e', 'i', 'o', 'u')
val Illegal = """ab|cd|pq|xy""".r
val Double = """(.)\1""".r

val input = Source
  .fromFile("2015/05.txt")
  .getLines()
  .toList

input.count(s => {
  s.filter(c => vowels.contains(c)).length >= 3 &&
    Double.findFirstIn(s).isDefined &&
    Illegal.findFirstIn(s).isEmpty
})

val DoublePairLetters = """(..).*\1""".r
val Repeat = """(.).\1""".r

input.count(s => {
  DoublePairLetters.findFirstIn(s).nonEmpty &&
    Repeat.findFirstIn(s).nonEmpty
})
