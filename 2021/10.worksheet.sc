import javax.sound.sampled.Line
import scala.io.Source

// val input = """[({(<(())[]>[[{[]{<()<>>
// [(()[<>])]({[<{<<[]>>(
// {([(<{}[<>[]}>{[]{[(<()>
// (((({<>}<{<{<>}{[]{[]{}
// [[<[([]))<([[{}[[()]]]
// [{[{({}]{}}([{[{{{}}([]
// {<[[]]>}<{[{[{[]{()[[[]
// [<(<(<(<{}))><([]([]()
// <{([([[(<>()){}]>(<<{{
// <{([{{}}[<[[[<>{}]]]>[]]""".split("\n").map(_.trim).toList

var fileName = "2021/10.txt"
var input =
  Source
    .fromFile(fileName)
    .getLines()
    .map(_.trim)
    .toList

val closers = Map(
  ')' -> ('(', 3),
  ']' -> ('[', 57),
  '}' -> ('{', 1197),
  '>' -> ('<', 25137)
)
val openers = closers.map((k, v) => { v._1 -> (k, v._2) })

abstract class Line {}
case class IncompleteLine(remaining: String) extends Line
case class CorruptLine(illegalChar: Char) extends Line
case class ValidLine() extends Line
case class UnsupportedChar(value: Char) extends Line

private def validateWithStack(
    input: List[Char],
    stack: List[Char]
): Line = {
  if (input.isEmpty) {
    if (stack.isEmpty) {
      return ValidLine()
    } else {
      return IncompleteLine(stack.mkString)
    }
  }
  val current :: remaining = input
  if (openers.contains(current)) {
    validateWithStack(remaining, openers(current)._1 :: stack)
  } else if (closers.contains(current)) {
    if (stack.isEmpty) { return CorruptLine(current) }
    val popped :: remainingStack = stack
    if (current == popped) { validateWithStack(remaining, remainingStack) }
    else { return CorruptLine(current) }
  } else {
    return UnsupportedChar(current)
  }
}

def validate(input: String): Line = {
  validateWithStack(input.toList, List())
}

val checked = input
  .map(validate(_))

val part1 =
  checked.collect { case a: CorruptLine => closers(a.illegalChar)._2 }.sum

val scores = Map(')' -> 1L, ']' -> 2L, '}' -> 3L, '>' -> 4L)

val autocomplete =
  checked.collect { case a: IncompleteLine =>
    a.remaining
      .map(scores(_))
      .foldLeft(0L)((acc, elem) => { (acc * 5) + elem })
  }

def median(s: List[Long]) = {
  val (lower, upper) = s.sortWith(_ < _).splitAt(s.size / 2)
  if (s.size % 2 == 0) (lower.last + upper.head) / 2.0 else upper.head
}

val part2 = median(autocomplete)
