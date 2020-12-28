import scala.io.Source

case class Rule(min: Int, max: Int, c: Char)

def parse(x: String): (String, Rule) = {
  val ex = """(\d+)-(\d+)\s(\w):\s(\w+)""".r

  x match {
    case ex(mi, ma, ch, pw) => (pw, Rule(mi.toInt, ma.toInt, ch.charAt(0)))
  }
}

def checkPart1(x: String, r: Rule): Boolean = {
  val c = x.count(_ == r.c)
  c >= r.min && c <= r.max
}

def checkPart2(x: String, r: Rule): Boolean = {
  x.charAt(r.min - 1) == r.c ^ x.charAt(r.max - 1) == r.c
}

val fileName = "/Users/michael.forman/src/sandbox/advent/2020/02.txt"
val input = Source.fromFile(fileName).getLines().toList map {
  parse
}

//val input = "1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc" split ("\n") map {
//  parse
//}

val part1 = input count {
  (checkPart1 _).tupled
}

val part2 = input count {
  (checkPart2 _).tupled
}
