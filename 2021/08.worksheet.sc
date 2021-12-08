import scala.io.Source

var fileName = "2021/08.txt"
var input =
  Source
    .fromFile(fileName)
    .getLines()
    .toList

val target = List(2, 3, 4, 7)
val part1 = input
  .map(
    _.trim
      .split('|')
      .last
      .trim
      .split(' ')
      .filter(x => { target.contains(x.length) })
  )
  .flatten
  .length

def mapSignalsToDigits(s: List[String]): Map[String, Int] = {
  val signals = s.map(_.sorted)
  val one = signals.filter(_.length == 2).head
  val seven = signals.filter(_.length == 3).head
  val four = signals.filter(_.length == 4).head
  val eight = signals.filter(_.length == 7).head
  val three =
    signals.filter(x => { x.length == 5 && one.intersect(x) == one }).head

  val nine =
    signals.filter(x => { x.length == 6 && three.intersect(x) == three }).head

  val two =
    signals.filter(x => { x.length == 5 && nine.diff(x).length == 2 }).head

  val five =
    signals.filter(x => { x.length == 5 && x != three & x != two }).head

  val zero = signals
    .filter(x => {
      x.length == 6 && x != nine && one.intersect(x) == one
    })
    .head

  val six =
    signals.filter(x => { x.length == 6 && x != zero && x != nine }).head

  Map(
    zero -> 0,
    one -> 1,
    two -> 2,
    three -> 3,
    four -> 4,
    five -> 5,
    six -> 6,
    seven -> 7,
    eight -> 8,
    nine -> 9
  )
}

val part2 = input
  .map(i => {
    i.split('|').map(_.trim.split(' ').toList) match {
      case Array(s, d) => {
        val m = mapSignalsToDigits(s)
        d.map(x => { m(x.sorted).toString }).mkString.toInt
      }
    }
  })
  .sum
