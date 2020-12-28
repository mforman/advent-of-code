import scala.io.Source
import scala.util.matching.Regex

//val input =
//  """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
//    |hcl:#623a2f
//    |
//    |eyr:2029 ecl:blu cid:129 byr:1989
//    |iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
//    |
//    |hcl:#888785
//    |hgt:164cm byr:2001 iyr:2015 cid:88
//    |pid:545766238 ecl:hzl
//    |eyr:2022
//    |""".stripMargin

val fileName = "/Users/michael.forman/src/sandbox/advent/2020/04.txt"
val input = Source.fromFile(fileName).getLines().mkString("\n")

val Pair = """(\w+):(.+)""".r

val passports = input.split("\n\n") map {
  _.split("""\s""") map { case Pair(k, v) => k -> v } toMap
}

def year(s: String, start: Int, end: Int): Boolean = {
  val Year = """(\d{4})""".r
  s match {
    case Year(x) => x.toInt >= start && x.toInt <= end
    case _ => false
  }
}

assert(year("1992",1992,1992))
assert(!year("1992",1993,1995))


def height(s: String): Boolean = {
  val CM = """(\d+)cm""".r
  val IN = """(\d+)in""".r
  s match {
    case CM(x) => x.toInt >= 150 && x.toInt <= 193
    case IN(x) => x.toInt >= 59 && x.toInt <= 76
    case _ => false
  }
}

assert (List("150cm","193cm","59in","76in") forall height)

def patternMatch(s:String, p: Regex) : Boolean = {
  s match {
    case p(_) => true
    case _ => false
  }
}

def ecl(s: String): Boolean = {
  val valid = List("amb", "blu", "brn", "gry", "grn", "hzl", "oth").toSet
  valid.contains(s)
}


val rules = Map(
    "byr" -> { year(_, 1920, 2002) },
    "iyr" -> { year(_, 2010, 2020) },
    "eyr" -> { year(_, 2020, 2030) },
    "hgt" -> { height(_) },
    "hcl" -> { patternMatch(_, """(#[0-9a-f]{6})""".r) },
    "ecl" -> { ecl(_) },
    "pid" -> { patternMatch(_, """(\d{9})""".r) },
)

def isValid(ruleSet: Map[String, String => Boolean])(p: Map[String, String]): Boolean = {
  p forall {
    case (k, v) =>
      ruleSet.get(k) match {
        case Some(f) => f(v)
        case _ => true // Ignore keys that aren't in the rules
      }
  }
}

val part1 = passports filter { p => (p.keySet & rules.keySet) == rules.keySet }
part1.length

val part2 = part1 count {
  isValid(rules)
}
