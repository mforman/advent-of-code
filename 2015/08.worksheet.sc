import scala.io.Source

val regex = """(\\+)(x[^\\]{2}|.)""".r

// val input = Array("\"\"", "\"abc\"", "\"aaa\"aaa\"")
val input = Source
  .fromFile("2015/08.txt")
  .getLines()
  .toList

input
  .map(line => {
    regex
      .findAllIn(line)
      .matchData
      .map(m => {
        val backslashes = m.group(1).size
        val evenNumber = backslashes % 2 == 0
        backslashes / 2 + (if (evenNumber) 0 else m.group(2).size)
      })
      .sum + 2
  })
  .sum

input
  .map(
    _.count(Seq('\\', '"').contains) + 2
  )
  .sum
